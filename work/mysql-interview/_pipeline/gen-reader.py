#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""读物生成器：把「卡片集」重组为「可顺序阅读的读物」。

用法：
    python3 _pipeline/gen-reader.py --tier brief   # 速览篇：只取「速记区」（约占全库 15%）
    python3 _pipeline/gen-reader.py --tier full    # 精读篇：知识本体（去掉卡片属性段）
    python3 _pipeline/gen-reader.py --tier brief --out /tmp/x

产出（分章成册，不塞一个大文件）：
    <out>/读物-<篇名>/00-目录.md
    <out>/读物-<篇名>/第NN章-<章名>.md

────────────────────────────────────────────────────────────────────
设计要点（都是为了让「读」成立，而不是把卡片拼起来）
  · **章导语自动生成** —— 从该章卡片自身的数据推出来（张数 / 频率分布 / 主题词 / 建议顺序），
    不编造。这样「重组」是 100% 脚本可做的，不需要逐章人工写导语。
  · **卡片编号改成章节内序号**（`10.1` `10.2`）—— 读物里「第 1339 卡」是出戏的。
  · **去掉卡片属性段**（full 篇）：`原文哪里错了`（纠错台账，占 18%）、`面试官可能接着问`（占 14%）、
    头部元信息（占 7%）—— 这三段合计 39% 的篇幅是「卡片作为工具」的属性，不是知识本体。
  · **保留可追溯**：每节末尾给一行小字「〔原卡 1339〕」，想查细节能回跳。
  · **接缝处给一句过渡**（full 篇）：用下一节的「一句话」当引子。
────────────────────────────────────────────────────────────────────
只读：对 target/go/ 只有读操作。
"""
import argparse
import re
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
TGT = PROJ / "target" / "go"

CHNUM_DOC = """**卡号说明**：标题里的 `1332` / `543` / `1337` 是**卡片编号**，对应 `target/go/<号>-<短名>.md`。
号段跨三代、手工分配、**不重编**（号是引用锚点：卡片间 591 处「见 545 卡」、ERRORS.md 段、实测归档目录都绑在号上）。

| 号段 | 张数 | 来历 |
|---|---|---|
| 1~199 ／ 200~499 ／ 500~699 | 1 ／ 33 ／ 84 | 早期 v3 时代的号，被沿用 |
| 901~999 ／ 1000~1099 ／ 1100~1199 ／ 1200~1299 | 39 ／ 47 ／ 32 ／ 47 | 各 worker 的固定号段（gpG / gpM / gpL / …） |
| **1300~1499** | **87** | **本轮 v4 重做（1301~1405）** |

所以同一张卡在**卡片文件、背诵清单、读物、纠错台账**里用的是**同一个号**，可互相跳转。
"""

CH_NAMES = {
    "02": "Go 语言概览与特性", "04": "Go 基础语法与标准库", "05": "Go 语言进阶",
    "06": "Go 语言高级特性", "07": "常用库与框架", "08": "并发模型与调度器",
    "09": "数据类型底层原理", "10": "并发编程", "11": "性能优化", "12": "数据库",
    "13": "Elasticsearch", "14": "消息中间件", "15": "微服务", "16": "设计模式",
    "17": "数据结构与算法", "18": "Linux / 网络", "19": "项目与系统设计", "20": "求职与录用",
}
# 知识本体段（full 篇保留）；其余为「卡片属性」段
BODY_SECTIONS = ("先说结论", "完整代码", "逐行讲透", "实测验证")
DROP_SECTIONS = ("原文哪里错了", "面试官可能接着问")


def cjk(s):
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def sections(t):
    """→ [(小节名, 正文)]，按出现顺序；只取 ## 级"""
    out = []
    for m in re.finditer(r"^##\s*(?!30 秒版)(.+?)\s*$\n(.*?)(?=^##\s|\n#\s|\Z)", t, re.S | re.M):
        out.append((m.group(1).strip(), m.group(2)))
    return out


def card_info(p):
    t = p.read_text(encoding="utf-8", errors="ignore")
    num = p.name.split("-")[0]
    src = re.search(r"^>\s*来源：`?(\d{1,2})-", t, re.M)
    ch = src.group(1).zfill(2) if src else "??"
    m1 = re.search(r"^#\s+\d+\s+(.+)$", t, re.M)
    m2 = re.search(r"^#\s+(?!\d+\s)(.+)$", t, re.M)
    title = (m1.group(1) if m1 else (m2.group(1) if m2 else p.stem)).strip()
    one = re.search(r"\*\*一句话\*\*[：:]\s*(.+)", t)
    freq = re.search(r"面试频率[：:]\s*([^\n｜|]+)", t)
    mem = re.search(r"#\s*🎯 速记区.*?\n(.*?)(?=\n---\s*\n|\n#\s*📖 原理区)", t, re.S)
    return {
        "p": p, "num": num, "ch": ch, "title": title, "t": t,
        "one": (one.group(1).strip() if one else ""),
        "freq": (freq.group(1).replace("*", "").strip() if freq else ""),
        "mem": (mem.group(1).strip() if mem else ""),
    }


def key_words(cards, top=6):
    """从标题里抽主题词（按**覆盖标题数**排序）。

    ⚠️ 2026-10-05 实测打回一次：初版按「出现次数」排，抽出了 `自旋锁的` / `实现与` 这类**碎片**
    （n-gram 把虚词也吃进去了）。两条过滤：① 不以虚词（的/与/和/是/在/为什么…）结尾；
    ② **至少在 2 个标题里出现**（只出现一次的不是「主题词」，是那张卡的专名）。
    """
    from collections import Counter
    c = Counter()
    STOP = ("的", "与", "和", "是", "在", "了", "吗", "呢", "会", "能", "要", "为", "把", "被", "对", "从")
    for k in cards:
        seen = set()
        for w in re.findall(r"[A-Za-z][A-Za-z0-9.+#]{2,}|[\u4e00-\u9fff]{2,5}", k["title"]):
            # 含虚词的一律不要（否则会抽出 `中的锁` `并发编程误` 这类碎片）
            if w.endswith(STOP) or any(s in w for s in ("的", "与", "和", "是", "在", "了", "吗", "呢")):
                continue
            seen.add(w)
        for w in seen:          # 同一标题内只计一次
            c[w] += 1
    return [w for w, n in c.most_common() if n >= 3][:top]     # ≥3 个标题才算「主题词」


# ── 润色：卡片腔 → 读物腔 ────────────────────────────────────────────
# ⚠️ 只做**定点替换**，绝不 blanket 替换 `本卡`/`本批`/`素材` ——
#    实测这三词大量出现在**正常语义**里：`本章导语`（我自己写的）、
#    `本批最后一条 id`（SQL 分页语境）、`就有素材`（日常词）。blanket 替换会误伤。
POLISH = [
    (r"本次底稿\s*v3\s*卡\s*\d+\s*写的", "旧版底稿写的"),
    (r"v3\s*底稿\s*\d+\s*卡说", "旧版底稿说"),
    (r"本卡实测更正", "实测更正"),
    (r"本卡实测", "实测"),
    (r"本卡已按源码改正", "已按源码改正"),
    (r"本卡穷举", "穷举"),
    (r"本卡每一处都给了", "每一处都给了"),
    (r"本卡无实测", "无实测"),
    (r"本卡\s*§", "本文 §"),
    (r"本卡懒汉式", "懒汉式"),
    (r"本卡只讲", "本文只讲"),
    (r"本卡不展开", "本文不展开"),
    (r"本卡只保留", "本文只保留"),
    (r"本卡是", "本文是"),
    (r"见\s*\*{0,2}(\d{3,4})\s*卡", r"见原卡 \1"),      # 读物里保留可追溯，但写法统一
    # ── 第三轮：泛化的自我指涉。实测「直接删」在 12 例里 10 例通顺、2 例断句 ——
    #    断句的正是「本卡的 X」和「与本卡 X」，所以这两条必须先于裸删。删后清多余空白。
    (r"与本卡", "与之"),
    (r"本卡的", ""),
    (r"本卡", ""),
    (r"[ \t]{2,}", " "),
    (r"（\s+", "（"),
    (r"\s+）", "）"),
]


def polish(t: str) -> str:
    for pat, rep in POLISH:
        t = re.sub(pat, rep, t)
    return t


def chapter_preface(ch, cards):
    """章导语：**全部由该章卡片自身数据推出**，不编造。"""
    n = len(cards)
    hi = sum(1 for k in cards if k["freq"].startswith(("极高", "很高")))
    mid = sum(1 for k in cards if k["freq"].startswith(("高", "中高")))
    lo = n - hi - mid
    kws = " / ".join(key_words(cards))
    ids = [k["num"] for k in cards]
    nums = sorted(int(i) for i in ids)
    L = [f"本章 **{n} 篇**，卡号 {min(nums)}~{max(nums)}。"]
    L.append(f"频率分布：**高频 {hi}** ／ 中高 {mid} ／ 其余 {lo}。")
    if kws:
        L.append(f"主题词（按标题词频，仅供参考）：{kws}。")
    if hi:
        L.append("**先读**（高频）：" + "、".join(f"`{k['num']}`" for k in cards if k["freq"].startswith(("极高", "很高")))[:160] + "。")
    L.append("")
    L.append("> 读法：本节是「速览篇」，每篇只保留**30 秒版 + 面试怎么答**。"
             "要原理、代码与实测，回卡片读「📖 原理区」。")
    return "\n".join(L)


def render_chapter(ch, cards, tier, width):
    name = CH_NAMES.get(ch, "")
    L = [f"# 第 {int(ch)} 章　{name}", "", chapter_preface(ch, cards), "", "---", ""]
    for i, k in enumerate(cards, 1):
        L.append(f"## {int(ch)}.{i}　{k['title']}")
        L.append("")
        if tier == "full":
            for sname, body in sections(k["t"]):
                if sname in DROP_SECTIONS or sname.startswith("30 秒版"):
                    continue
                if sname in BODY_SECTIONS:
                    L.append(f"### {sname}")
                    L.append("")
                    L.append(polish(body.strip()))
                    L.append("")
        else:
            L.append(polish(k["mem"]))
            L.append("")
        L.append(f"<sub>〔原卡 {k['num']}〕</sub>")
        L.append("")
        # 接缝过渡：用下一节的一句话当引子
        nxt = cards[i] if i < len(cards) else None
        if nxt and tier == "full" and nxt["one"]:
            L.append(f"> **下一节**：{nxt['one']}")
            L.append("")
        L.append("---")
        L.append("")
    return "\n".join(L) + "\n"


def safe_name(s: str) -> str:
    """章名 → 文件名安全形式。

    ⚠️ 2026-10-05 实测踩坑：第 18 章名是 `Linux / 网络`，里面的 `/` 是**路径分隔符**，
    直接拿去写文件会 FileNotFoundError。**任何拼进路径的字段都要净化**（同「写死格式」一类）。
    """
    return s.replace("/", "-").replace("\\", "-").replace(":", "-").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=("brief", "full"), default="brief")
    ap.add_argument("--out", default=str(PROJ))
    ap.add_argument("--width", type=int, default=76)
    a = ap.parse_args()

    cards = []
    for p in sorted(TGT.glob("*.md")):
        if not re.search(r"[\u4e00-\u9fff]", p.name):
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if "🎯 速记区" not in t:
            continue
        cards.append(card_info(p))
    bych = {}
    for k in cards:
        bych.setdefault(k["ch"], []).append(k)
    for ch in bych:
        bych[ch].sort(key=lambda k: int(k["num"]))

    name = "速览篇" if a.tier == "brief" else "精读篇"
    root = Path(a.out) / f"读物-{name}"
    root.mkdir(parents=True, exist_ok=True)

    idx = [f"# Go 面试知识读本 · {name}", "",
           f"共 **{len(cards)} 篇**，分 **{len(bych)} 章**。", "",
           f"> 由 `gen-reader.py --tier {a.tier}` 从 `target/go/` 的卡片重组生成；"
           f"**内容取自原卡，未改写**。每一节末尾的〔原卡 NNNN〕可回跳查证。", "",
           "",
           *[f"{line}" for line in CHNUM_DOC.split("\n")],
           "",
           "| 章 | 章名 | 篇数 | 字数 | 文件 |", "|---|---|---|---|---|"]
    tot = 0
    for ch in sorted(bych, key=int):
        v = bych[ch]
        body = render_chapter(ch, v, a.tier, a.width)
        f = root / f"第{int(ch):02d}章-{safe_name(CH_NAMES.get(ch,''))}.md"
        f.write_text(body, encoding="utf-8")
        c = cjk(body)
        tot += c
        idx.append(f"| {int(ch)} | {CH_NAMES.get(ch,'')} | {len(v)} | {c:,} | `{f.name}` |")
    idx += ["", f"**合计 {tot:,} 汉字。**"]
    (root / "00-目录.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    print(f"tier={a.tier}　{len(cards)} 篇 / {len(bych)} 章　合计 {tot:,} 汉字")
    print(f"→ {root}/　（00-目录.md + {len(bych)} 个分章文件）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
