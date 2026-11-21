#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""背诵清单生成器（v2，面向人读）

用法：
    python3 _pipeline/gen-recite-list.py                 # 本批 87 张
    python3 _pipeline/gen-recite-list.py --scope all     # 全库 v4 中文卡
    python3 _pipeline/gen-recite-list.py --width 60      # 改折行宽度（默认 76 显示列）

产出（同名不同后缀，两份并存）：
    <out>/背诵清单-<范围>.txt   纯文本：硬折行、无 Markdown 标记，可打印/手机看
    <out>/背诵清单-<范围>.md    预览友好：真正的 GFM 复选框（`- [ ]`）

────────────────────────────────────────────────────────────────────
v2 相对 v1 修的 7 个「不像给人读的」问题（都是实测出来的，不是感觉）
  1. **MD 复选框是假的** —— v1 写 `[ ] 标题`，GFM 要求 `- [ ] 标题`；实测真复选框 0 个。
  2. **答案区零分章** —— v1 答案区 744 行连续输出、章标题 0 个，查第 12 章只能盲翻。
  3. **答案区没标题** —— 只给 `1339 一句话…`，脱离自测区不知道题是什么。
  4. **超长行** —— v1 最长 432 字符、178 行 >100 字符，手机上折成一团。
  5. **频率/难度是自由文本** —— 实测 40+ 种频率写法（含 40 字括号注释）、3 套难度体系混用、
     25 张卡根本没有这两个字段 → 直接打印既不可靠又助长第 4 条。改为**归一成 ★★ 少量档位**。
  6. **要点挤在 meta 行** —— 拆成独立一行并折行。
  7. **无高频优先入口** —— 顶部加「先背这些」（极高/很高）。
────────────────────────────────────────────────────────────────────
只读：对 target/go/ 只有读操作。
"""
import argparse
import re
import unicodedata
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
TGT = PROJ / "target" / "go"
ALL_TXT = PROJ / "_pipeline" / "v4-rework" / "ALL.txt"
BLOCK_E = PROJ / "_pipeline" / "v4-rework" / "block-E.txt"

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
    "01": "课程导学", "02": "Go 语言概览与特性", "03": "简历与求职准备",
    "04": "Go 基础语法与标准库", "05": "Go 语言进阶", "06": "Go 语言高级特性",
    "07": "常用库与框架", "08": "并发模型与调度器", "09": "数据类型底层原理",
    "10": "并发编程", "11": "性能优化", "12": "数据库", "13": "Elasticsearch",
    "14": "消息中间件", "15": "微服务", "16": "设计模式", "17": "数据结构与算法",
    "18": "Linux / 网络", "19": "项目与系统设计", "20": "求职与录用",
}


# ── 显示宽度与折行（中文算 2 列；按显示宽度折，不按字符数）────────────
def dwidth(s: str) -> int:
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def chunks(text: str) -> list:
    """切成「不可断块」：CJK/全角标点各成一块；**连续的 ASCII 词整块**（`goroutine` 不许切成 `gorout`+换行）。"""
    out, cur = [], ""
    for ch in text:
        if unicodedata.east_asian_width(ch) in "WF" or ch in "·—…、，。；：！？「」（）":
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        elif ch == " ":
            if cur:
                out.append(cur); cur = ""
            out.append(" ")
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


# 不许出现在行首的字符（避免「续行以 · 开头」这种读起来别扭的断法）
NO_LEAD = set("·、，。；：！？）」』%·…")


def wrap(text: str, indent: str, width: int, first_prefix: str = "") -> list:
    """按显示宽度折行；**拉丁词不拆**、**行首不留悬挂标点（禁则处理）**、续行用 indent 缩进。

    禁则处理：断行点前若「当前块或下一块是禁止行首的标点」，则不在该处断 ——
    宁可让本行多出 ≤2 列的标点（悬挂标点，中文排版惯例），也不把 `、` `）` 甩到下一行行首。
    """
    items = chunks(text)
    out, cur, curw = [], [], dwidth(first_prefix)
    prefix = first_prefix
    indw = dwidth(indent)
    for i, ck in enumerate(items):
        w = dwidth(ck)
        if curw + w > width and cur:
            nxt = items[i + 1] if i + 1 < len(items) else ""
            # 禁则：本块或下一块是禁行首标点 → 不在此断（允许本行超出 ≤2 列）
            if ck in NO_LEAD:
                pass
            elif nxt in NO_LEAD and curw + w + dwidth(nxt) <= width + 2:
                pass
            else:
                out.append((prefix + "".join(cur)).rstrip())
                cur, curw, prefix = [], indw, indent
        cur.append(ck)
        curw += w
    if cur:
        out.append((prefix + "".join(cur)).rstrip())
    return out


# ── 字段归一（v1 的坑：直接把自由文本打出来）──────────────────────────
def norm_freq(raw: str) -> str:
    """频率自由文本 → 5 档星标。实测取值 40+ 种，必须归一。"""
    s = raw.replace("*", "").strip()
    if not s or s in ("—", "——", "-"):
        return "  ? "                       # 字段缺失
    for key, star in (("极高", "★★★"), ("很高", "★★★"), ("高", "★★"), ("中高", "★★"),
                      ("中", "★"), ("低", "·")):
        if s.startswith(key):
            return f"{star:>3} "
    return "  ? "


def norm_diff(raw: str) -> str:
    """难度自由文本（进阶/L3/高级 三套体系混用）→ 2 档。"""
    s = raw.replace("*", "").strip()
    if not s or s in ("—", "——", "-"):
        return " ?"
    if re.match(r"^(L[34]|进阶|高级|难)", s):
        return "难"
    if re.match(r"^(L[12]|入门|基础|中级|中等|易)", s):
        return "中"
    return " ?"


def info_of(num: str):
    hits = list(TGT.glob(f"{num}-*.md"))
    if not hits:
        return None
    t = hits[0].read_text(encoding="utf-8", errors="ignore")
    one = re.search(r"\*\*一句话\*\*[：:]\s*(.+)", t)
    meta = re.search(r"^>\s*难度[：:]\s*([^｜|]+)[｜|]\s*面试频率[：:]\s*([^\n｜|]+)", t, re.M)
    sec = re.search(r"##\s*30 秒版(.*?)(?=\n##\s|\n#\s|\Z)", t, re.S)
    cues = [c.strip() for c in re.findall(r"^\s*\d+\.\s*\*\*(.+?)\*\*", sec.group(1) if sec else "", re.M)]
    return {
        "one": (one.group(1).strip() if one else ""),
        "freq": norm_freq(meta.group(2)) if meta else "  ? ",
        "diff": norm_diff(meta.group(1)) if meta else " ?",
        "cues": cues,
        "test": "[实测]" in t,
    }


# ── 取卡清单 ────────────────────────────────────────────────────────
def batch_cards():
    out = []
    for f in (ALL_TXT, BLOCK_E):
        if not f.exists():
            continue
        for ln in f.read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.startswith("#"):
                continue
            c = ln.split("\t")
            if len(c) >= 5:
                out.append((c[1].strip().zfill(2), c[3].strip(), c[4].strip()))
    return out


def all_cards():
    """全库中文卡 → [(章, 卡号, H1 标题)]

    ⚠️ H1 两级回退：`# 904 标题`（主流）→ `# 标题`（904~928 那批例外）→ 文件名兜底。
    """
    out = []
    for p in sorted(TGT.glob("*.md")):
        if not re.search(r"[\u4e00-\u9fff]", p.name):
            continue
        num = re.match(r"(\d+)-", p.name)
        if not num:
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        src = re.search(r"^>\s*来源：`?(\d{1,2})-", t, re.M)
        m1 = re.search(r"^#\s+\d+\s+(.+)$", t, re.M)
        m2 = re.search(r"^#\s+(?!\d+\s)(.+)$", t, re.M)
        title = m1.group(1) if m1 else (m2.group(1) if m2 else p.stem.split("-", 1)[-1])
        out.append((src.group(1).zfill(2) if src else "??", num.group(1), title.strip()))
    return out


def build(scope: str):
    rows = batch_cards() if scope == "batch" else all_cards()
    bych, missing = {}, []
    for ch, num, title in rows:
        it = info_of(num)
        (missing.append(num) if it is None else bych.setdefault(ch, []).append((num, title, it)))
    return bych, missing, len(rows)


# ── 渲染 ────────────────────────────────────────────────────────────
def render(bych, missing, total, scope, width, as_md):
    box = "- [ ]" if as_md else "[ ]"
    L = []
    head = "面试卡背诵清单" + ("（本批）" if scope == "batch" else "（全库）")
    L += [head, "═" * 46, ""]
    L.append(f"共 {total - len(missing)} 张" + (f"　未交付 {len(missing)} 张：{'、'.join(missing)}" if missing else ""))
    L += ["",
          "【怎么背】",
          "  1. 翻到「自测区」，一篇只看两行：标题 + 要点骨架。",
          "  2. 顺着骨架一条条往下讲；讲完再看下一张。",
          "  3. 讲不出来的，去「答案区」按卡号对一句话，再回卡片读「速记区」。",
          "  4. 讲得出来的，在方括号里打勾，下次跳过。",
          "",
          "",
          *CHNUM_DOC.split("\n"),
          "",
          "【标记】★★★ 极高/很高频率　★★ 高/中高　★ 中　· 低　? 原卡未标",
          "        【实测】卡内有本机跑出来的数字，被追问细节时用它兜底",
          ""]

    # 高频优先入口：给档位人数 + 只列最高档（370 张时全列会失去"优先"的意义）
    tiers = {}
    for ch in bych:
        for n, t, it in bych[ch]:
            tiers.setdefault(it["freq"].strip(), []).append((n, t))
    order = ["★★★", "★★", "★", "·", "?"]
    dist = "　".join(f"{k} {len(tiers.get(k, []))} 张" for k in order if tiers.get(k))
    L += [f"【频率分布】{dist}"]
    hot = sorted(tiers.get("★★★", []), key=lambda x: int(x[0]))
    if hot:
        L.append(f"【先背这些】★★★ 共 {len(hot)} 张")
        for n, t in hot:
            L += wrap(f"{n}  {t}", " " * 12, width - 4, "            ")
    L.append("")

    # 目录速览
    L += ["── 目录速览 " + "─" * 26]
    for ch in sorted(bych):
        v = bych[ch]
        nums = sorted((x[0] for x in v), key=int)
        rng = f"{nums[0]}" if len(nums) == 1 else f"{nums[0]}~{nums[-1]}"
        L.append(f"  第 {int(ch):>2} 章 {CH_NAMES.get(ch, ''):<14} {len(v):>3} 张   {rng}")

    # 自测区
    L += ["", "", "═" * 46, "　自测区　（只看这里，别看答案区）", "═" * 46]
    for ch in sorted(bych):
        v = bych[ch]
        L += ["", f"── 第 {int(ch)} 章 {CH_NAMES.get(ch, '')}（{len(v)} 张）" + "─" * 14, ""]
        for num, title, it in sorted(v, key=lambda x: int(x[0])):
            flag = "　【实测】" if it["test"] else ""
            L.append(f"{box} {num}  {title}")
            L.append(f"        {it['diff']} {it['freq']}{flag}")
            if it["cues"]:
                L += wrap(" · ".join(it["cues"]), " " * 8, width, "        要点  ")

    # 答案区
    L += ["", "", "═" * 46, "　答案区　（对答案用；按章分组）", "═" * 46]
    for ch in sorted(bych):
        v = bych[ch]
        L += ["", f"── 第 {int(ch)} 章 {CH_NAMES.get(ch, '')}（{len(v)} 张）" + "─" * 14, ""]
        for num, title, it in sorted(v, key=lambda x: int(x[0])):
            L.append(f"{num}  {title}")
            if it["one"]:
                one = it["one"] if as_md else it["one"].replace("**", "")
                L += wrap(one, " " * 6, width, "      ")
            L.append("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", choices=("batch", "all"), default="batch")
    ap.add_argument("--out", default=str(PROJ))
    ap.add_argument("--width", type=int, default=76, help="折行宽度（显示列，中文算 2）")
    a = ap.parse_args()

    bych, missing, total = build(a.scope)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    sfx = "-全库" if a.scope == "all" else "-本批"
    f_txt = out / f"背诵清单{sfx}.txt"; f_md = out / f"背诵清单{sfx}.md"
    f_txt.write_text(render(bych, missing, total, a.scope, a.width, False), encoding="utf-8")
    f_md.write_text(render(bych, missing, total, a.scope, a.width, True), encoding="utf-8")

    n = sum(len(v) for v in bych.values())
    no_one = [x[0] for v in bych.values() for x in v if not x[2]["one"]]
    no_cue = [x[0] for v in bych.values() for x in v if len(x[2]["cues"]) < 2]
    tested = sum(1 for v in bych.values() for x in v if x[2]["test"])
    qmark = sum(1 for v in bych.values() for x in v if x[2]["freq"].strip() == "?")
    print(f"scope={a.scope}　台账 {total} 张 / 命中 {n} 张" + (f" / 未交付 {len(missing)}：{'、'.join(missing)}" if missing else ""))
    print(f"  自证：一句话 {n-len(no_one)}/{n}　要点骨架 {n-len(no_cue)}/{n}　【实测】标记 {tested}/{n}　频率缺失 {qmark}/{n}")
    for f in (f_txt, f_md):
        lines = f.read_text(encoding="utf-8").split("\n")
        hang = sum(1 for l in lines if dwidth(l) > a.width)
        bad = sum(1 for l in lines if dwidth(l) > a.width + 4)
        nolead = sum(1 for l in lines if l.strip() and l.strip()[0] in NO_LEAD)
        print(f"  → {f.name}  {len(lines)} 行　"
              f"含悬挂标点行 {hang}　真超宽(>{a.width+4}) {bad}　行首悬挂标点 {nolead}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
