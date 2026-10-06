#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""学习路径版生成器：把卡片集变成「按依赖排序 + 带自测题」的学习材料。

用法：
    python3 _pipeline/gen-study-path.py            # 全库
    python3 _pipeline/gen-study-path.py --out /tmp/x

产出：
    <out>/读物-学习路径/00-总目录.md
    <out>/读物-学习路径/第NN章-<章名>.md      ← 每章：阅读顺序 + 每篇「自测题 / 参考答案」

────────────────────────────────────────────────────────────────────
一句话设计：**不出新内容，只做两件已有信息的重组**
  ① **顺序**：用卡内既有的**卡间引用**（`见 545 卡`）建图，做拓扑排序 ——
     「被引用的先读」是**从数据推出来的依赖**，不是我拍的顺序。同层按原卡号序（稳定）。
  ② **题目**：从卡内**既有的两处结构**派生，零创作 ——
     · 「30 秒版」的 `N. **引导词** —— 内容`  → 题 = 引导词，答 = 内容
     · 「面试官可能接着问」的 `**Qn：问题** / 答：答案` → 题 = 问题，答 = 答案
  实测可出题 ≈ 2,762 道（骨架 ~1,480 + 追问 ~1,282），全部有卡内原文兜底 ⇒ **可门禁**。
────────────────────────────────────────────────────────────────────
只读：对 target/go/ 只有读操作。
"""
import argparse
import re
from collections import defaultdict
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


def safe_name(s):
    return s.replace("/", "-").replace("\\", "-").replace(":", "-").strip()


def sec(t, pat):
    m = re.search(pat, t, re.S)
    return m.group(1) if m else ""


POLISH = [
    (r"本次底稿\s*v3\s*卡\s*\d+\s*写的", "旧版底稿写的"),
    (r"v3\s*底稿\s*\d+\s*卡说", "旧版底稿说"),
    (r"本卡实测更正", "实测更正"), (r"本卡实测", "实测"),
    (r"本卡", "本文"), (r"见\s*\*{0,2}(\d{3,4})\s*卡", r"见原卡 \1"),
]


def polish(t):
    for pat, rep in POLISH:
        t = re.sub(pat, rep, t)
    return t


def parse_card(p):
    t = p.read_text(encoding="utf-8", errors="ignore")
    num = p.name.split("-")[0]
    src = re.search(r"^>\s*来源：`?(\d{1,2})-", t, re.M)
    m1 = re.search(r"^#\s+\d+\s+(.+)$", t, re.M)
    m2 = re.search(r"^#\s+(?!\d+\s)(.+)$", t, re.M)
    title = (m1.group(1) if m1 else (m2.group(1) if m2 else p.stem)).strip()
    one = re.search(r"\*\*一句话\*\*[：:]\s*(.+)", t)

    # ① 骨架：30 秒版里 `N. **引导词**〔（补充）〕—— 内容`
    # ⚠️ 2026-10-05 实测踩坑：引导词和 `——` 之间**可能夹一个括号补充**
    #    （`2. **六种方式排序**（1 万次 × 5 字节）—— …`）。初版用 `\*\*(.+?)\*\*\s*——`，
    #    `.+?` 会一路吃到括号自己的 `**`，把题面污染成 `六种方式排序**（1 万次 × 5 字节）`。
    #    改为：引导词限定**不含 `*`**，中间允许 `[^\n]*?` 跳过括号。
    mem = sec(t, r"##\s*30 秒版(.*?)(?=\n##\s|\n#\s|\Z)")
    skel = []
    for m in re.finditer(r"^\s*\d+\.\s*\*\*([^*\n]+)\*\*[^\n]*?——\s*(.+?)(?=\n\s*\d+\.\s|\Z)", mem, re.S | re.M):
        q = m.group(1).strip()
        a = re.sub(r"\s+", " ", m.group(2)).strip()
        if q and len(a) > 10:
            skel.append((q, a))

    # ② 追问：`**Qn：问题**` 后跟答案
    # ⚠️ 2026-10-05 实测踩坑（同一类连踩两次）：答案标记有**三种**写法 ——
    #    `答：`(193 条) ／ `A：`(164 条) ／ **完全不带标记、直接接**(863 条，多数派)。
    #    初版只写 `答[：:]` → 1,297 条只解析出 237 条（漏 82%）；第二版加上 `A` 也只到 434 条。
    #    现在把标记整段设为**可选**，靠「下一个 `**Q`」作终止符 —— 三种写法通吃。
    qa = []
    for m in re.finditer(
        r"\*\*Q\d*\s*[：:]\s*([^*\n]+?)\*\*[^\n]*\n+\s*"
        r"(?:(?:答|A|Answer|答案)\s*[：:]\s*)?"
        r"(.+?)(?=\n\s*\*\*Q|\Z)", t, re.S):
        q = m.group(1).strip()
        a = re.sub(r"\s+", " ", m.group(2)).strip()
        if q and len(a) > 10:
            qa.append((q, a))

    refs = {r for r in re.findall(r"见\s*\*{0,2}(\d{3,4})\s*[号]?卡", t) if r != num}
    return {
        "p": p, "num": num, "ch": (src.group(1).zfill(2) if src else "??"),
        "title": title, "one": (one.group(1).strip() if one else ""),
        "skel": skel, "qa": qa, "refs": refs,
    }


def topo(cards):
    """章内拓扑排序：被引用的排在前面。稳定 tie-break = 原卡号序。"""
    nums = [c["num"] for c in cards]
    idx = {n: i for i, n in enumerate(nums)}
    ins = {n: set() for n in nums}            # n 的上游
    for c in cards:
        for r in c["refs"]:
            if r in idx:                       # 只算章内边
                ins[c["num"]].add(r)
    out, done = [], set()
    while len(out) < len(nums):
        ready = [n for n in nums if n not in done and ins[n] <= done]
        if not ready:                          # 有环 → 按原序放掉，别死循环
            ready = [n for n in nums if n not in done]
        ready.sort(key=lambda n: idx[n])       # 稳定：同层按原卡号序
        pick = ready[0]
        out.append(pick); done.add(pick)
    bynum = {c["num"]: c for c in cards}
    return [bynum[n] for n in out]


def render_chapter(ch, cards, stat):
    ordered = topo(cards)
    L = [f"# 第 {int(ch)} 章　{CH_NAMES.get(ch, '')}　·　学习路径", "",
         f"本章 **{len(ordered)} 篇**。阅读顺序由**卡间引用**推出（被引用的先读）；同层按原卡号序。", ""]
    L += ["## 阅读顺序", ""]
    for i, c in enumerate(ordered, 1):
        dep = sorted((r for r in c["refs"] if any(x["num"] == r for x in cards)), key=int)
        suffix = f"　← 先读 {'、'.join(dep)}" if dep else ""
        L.append(f"{i}. **{c['num']}**　{c['title']}{suffix}")
    L += ["", "---", ""]

    for i, c in enumerate(ordered, 1):
        L.append(f"## {int(ch)}.{i}　{c['title']}　<sub>〔原卡 {c['num']}〕</sub>")
        L.append("")
        qs = [(q, a, "骨架") for q, a in c["skel"]] + [(q, a, "追问") for q, a in c["qa"]]
        stat["q"] += len(qs); stat["cards"] += 1
        if not qs:
            L.append("> 本卡无自测题（原卡未含 30 秒版骨架与追问段）。")
            L.append("")
            continue
        L += [f"**自测题**（{len(qs)} 道；先合上材料答，再对下面的参考答案）", ""]
        for j, (q, a, kind) in enumerate(qs, 1):
            mark = "🔹" if kind == "骨架" else "❓"
            L.append(f"{j}. {mark} {q}")
        L += ["", "**参考答案**", ""]
        for j, (q, a, kind) in enumerate(qs, 1):
            L.append(f"{j}. **{q}**")
            L.append(f"   {polish(a)}")
            L.append("")
        L += ["---", ""]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(PROJ))
    a = ap.parse_args()

    cards = []
    for p in sorted(TGT.glob("*.md")):
        if not re.search(r"[\u4e00-\u9fff]", p.name):
            continue
        if "🎯 速记区" not in p.read_text(encoding="utf-8", errors="ignore"):
            continue
        cards.append(parse_card(p))
    bych = defaultdict(list)
    for c in cards:
        bych[c["ch"]].append(c)

    root = Path(a.out) / "读物-学习路径"
    root.mkdir(parents=True, exist_ok=True)
    stat = {"q": 0, "cards": 0}
    idx = ["# Go 面试学习路径 · 总目录", "",
           "**顺序怎么来的**：用卡片之间既有的引用关系（`见 545 卡`）建图做拓扑排序 —— "
           "被引用的先读。这不是我拍的学习顺序，是**卡片自己声明过的依赖**。", "",
           "**题目怎么来的**：全部从卡内既有结构派生（30 秒版的要点骨架 + 面试官可能接着问），"
           "**没有一道是凭空造的**，每题答案都能在原卡里找到。", "",
           "",
           *[f"{line}" for line in CHNUM_DOC.split("\n")],
           "",
           "| 章 | 章名 | 篇数 | 题数 | 文件 |", "|---|---|---|---|---|"]
    for ch in sorted(bych, key=int):
        v = bych[ch]
        body = render_chapter(ch, v, stat)
        f = root / f"第{int(ch):02d}章-{safe_name(CH_NAMES.get(ch, ''))}.md"
        f.write_text(body, encoding="utf-8")
        nq = sum(len(c["skel"]) + len(c["qa"]) for c in v)
        idx.append(f"| {int(ch)} | {CH_NAMES.get(ch, '')} | {len(v)} | {nq} | `{f.name}` |")
    idx += ["", f"**合计 {stat['cards']} 篇 / {stat['q']} 道自测题。**"]
    (root / "00-总目录.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # ── 自证 ──────────────────────────────────────────────
    no_q = [c["num"] for c in cards if not (c["skel"] or c["qa"])]
    # 题面污染自检：题面里不该出现 `**`（那是解析吃多了的signature）或超长（>90 字符多半是把答案当题了）
    bad = [(c["num"], q) for c in cards for q, _ in (c["skel"] + c["qa"]) if "**" in q or len(q) > 90]
    print(f"cards={len(cards)}  chapters={len(bych)}  questions={stat['q']}")
    print(f"  自证：有题卡 {len(cards)-len(no_q)}/{len(cards)}" + (f"　无题卡 {len(no_q)}：{'、'.join(no_q[:6])}…" if no_q else ""))
    print(f"  题面污染自检：{len(bad)} 处（应为 0）" + (f"　例：{bad[0][0]} 「{bad[0][1][:40]}」" if bad else " ✓"))
    print(f"  平均 {stat['q']/max(1,len(cards)-len(no_q)):.1f} 题/卡")
    print(f"→ {root}/　（00-总目录.md + {len(bych)} 个分章文件）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
