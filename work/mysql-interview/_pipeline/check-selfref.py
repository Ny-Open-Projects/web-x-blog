#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自循环引用门禁：查出「v4 卡 A 指向 v3 卡 B，而 B 的取代者正是 A」的引用。

────────────────────────────────────────────────────────────────────
为什么要有这个脚本（2026-10-05 立）
────────────────────────────────────────────────────────────────────
本轮靠人工扫全库发现 28 处自循环引用，其中真缺陷集中在同一名 worker 名下 ——
根因是**口径的两条传达通道都不可靠**：
  · 只发消息 → worker 上下文里旧理解的权重更高，会忽略或读反（实测读反两次）
  · 只改 TODO-worker.md → worker 不一定每批都重读
这与本项目早先「号段约定传达不可靠 → 把撞号检查放进 validate-v4.py」是**同一类问题**。
**解法也一样：把检查落成脚本**，谁都能跑、每批都该跑。

────────────────────────────────────────────────────────────────────
判定规则（lead 定，2026-10-05）
────────────────────────────────────────────────────────────────────
  A 卡引用 v3 卡 B，B 的取代者记为 S（从 v4-rework/ALL.txt 推导）：
    · S == A          → ★DEFER：自循环，**必须改**（读者 A→B→A 死路）
    · S != A（第三方） → OK：允许保留（两跳可达：A→B→（B 的指针）→S）
  引用还必须区分**语体**：
    · PROVENANCE（正当）：「本卡合并 v3 主卡 `136-…`」「顺手纠正 v3 底稿（133 卡）」
      —— 它是**对取材来源的声明/纠错**，不是把内容甩出去
    · DEFER（缺陷）：「细节见 120 卡」「三张 v3 卡保持原样作为深挖层」
      —— 它把**本卡该讲的内容**甩给被取代的卡
  所以脚本只报 **自循环 × DEFER** 的交集，PROVENANCE / UNCERTAIN 分开列出供人工判读。

用法：
    python3 _pipeline/check-selfref.py              # 全库
    python3 _pipeline/check-selfref.py --selftest   # 已知答案自测
退出码：0 = 无「自循环 × DEFER」；1 = 有
"""
import re
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
TARGET = PROJ / "target" / "go"
ALL_TXT = PROJ / "_pipeline" / "v4-rework" / "ALL.txt"

# 语体判据（**顺序有意义**：先判本体内部的"合并/纠错/取材"叙述，再判"往外指"）
# ⚠️ 2026-10-05 自测打回两次：
#   ① `且与现用 v3 卡 `276-…` 一致。` 属取材声明（PROV）→ 补 `现用 v3` / `取材`
#   ② 用**整句**判语体太宽：卡片里的句子可能是一整段，末尾有「见 X 卡」就把整段判成 DEFER，
#      于是「**顺手纠正**：源文说…」这种正当纠错段被误判 → 改为**窗口判语体**（见 WINDOW）。
#      并补 `纠正`（「顺手纠正」是纠错节，不是外推）。
PROV = re.compile(r"合并|取代|重做|底稿|纠错|纠正|反纠错|已重做|替代|对应 v3|出处|现用 v3|取材")
DEFER = re.compile(r"保持原样|深挖层|详见|细节见|细节（|见 \*\*\d+ 卡|见 \d+ 卡|见卡|参考卡")

# 语体判定的字符窗口：只取引用处 ±WINDOW 字符内的文本，避免"整段末尾有个见"污染判据
WINDOW = 45
# PROV 的宽窗口：**只对 PROV 放宽**（PROV = 不算违规的方向，放宽是安全的）。
# 原因（2026-10-05 实测）：`本卡合并 v3 主卡 `106-…` + 卫星卡 `107…`、`108…`、`109…``
# 这种**取材清单**里，第 3 个引用离「合并」有 60+ 字符 → 窄窗口判成 UNCERTAIN。
# ⚠️ 反向不放宽：DEFER 仍只用窄窗口 —— 否则长句里"段首写合并、段尾甩细节"会被 PROV 掩盖。
WINDOW_PROV = 150

# 引用形式：`NNN 卡` / `见 **NNN 卡**` / `\`NNN-slug\``
REF_NUM = re.compile(r"(?<!\d)(\d{3,4})\s*卡")
REF_SLUG = re.compile(r"`(\d{3,4})-[a-z][^`]*`")


def load_supersede():
    """→ {v3 编号: 新卡号}"""
    sup = {}
    if not ALL_TXT.exists():
        return sup
    for ln in ALL_TXT.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.split("\t")
        if len(f) < 4:
            continue
        new = f[3].strip()
        cols = [f[2]] + (f[6].split(";") if len(f) > 6 else []) + (f[7].split(";") if len(f) > 7 else [])
        for c in cols:
            c = c.strip()
            if c:
                sup[c.split("-")[0]] = new
    return sup


def sentence_at(text: str, pos: int) -> str:
    """取 pos 所在的句子（以换行 / 。！？ 为界）。"""
    left = max(text.rfind("\n", 0, pos), text.rfind("。", 0, pos),
               text.rfind("！", 0, pos), text.rfind("？", 0, pos))
    right_cands = [i for i in (text.find("\n", pos), text.find("。", pos),
                               text.find("！", pos), text.find("？", pos)) if i != -1]
    right = min(right_cands) if right_cands else len(text)
    return text[left + 1:right + 1].strip()


def classify_window(text: str, pos: int) -> str:
    """按引用处的窗口判语体（不用整句 —— 整句会被段尾的「见」污染）。

    次序有讲究：**窄窗口 PROV → 窄窗口 DEFER → 宽窗口 PROV → UNCERTAIN**。
    窄窗口 DEFER 必须先于宽窗口 PROV，否则「段首写合并、段尾甩细节见 X 卡」会被掩盖。
    """
    seg = text[max(0, pos - WINDOW): pos + WINDOW]
    if PROV.search(seg):
        return "PROV"
    if DEFER.search(seg):
        return "DEFER"
    wide = text[max(0, pos - WINDOW_PROV): pos + WINDOW_PROV]
    if PROV.search(wide):
        return "PROV"
    return "UNCERTAIN"


def classify(sent: str) -> str:
    """兼容旧接口：整句判语体（自测用例用）。"""
    if PROV.search(sent):
        return "PROV"
    if DEFER.search(sent):
        return "DEFER"
    return "UNCERTAIN"


def scan(sup):
    """→ (defects, prov, uncertain)"""
    defects, prov, uncertain = [], [], []
    for p in sorted(TARGET.glob("*.md")):
        if not re.search(r"[\u4e00-\u9fff]", p.name):
            continue                      # 只看 v4 中文卡
        own = p.name.split("-")[0]
        text = p.read_text(encoding="utf-8", errors="ignore")
        hits = set()
        for m in REF_NUM.finditer(text):
            hits.add((m.group(1), m.start()))
        for m in REF_SLUG.finditer(text):
            hits.add((m.group(1), m.start()))
        for num, pos in sorted(hits, key=lambda x: x[1]):
            if num not in sup:
                continue                  # 不是被取代卡，不管
            sent = sentence_at(text, pos)
            kind = classify_window(text, pos)
            rec = (p.name, num, sup[num], sent)
            if sup[num] == own:
                if kind == "PROV":
                    prov.append(rec)
                elif kind == "DEFER":
                    defects.append(rec)
                else:
                    uncertain.append(rec)
            elif kind == "DEFER":
                prov.append(rec)          # 第三方取代者 → 允许，归入"允许保留"
            else:
                prov.append(rec)
    return defects, prov, uncertain


def _selftest():
    """已知答案自测 —— 用例全部取自 2026-10-05 人工判读过的真实句子。"""
    sup = {"136": "1318", "120": "1327", "209": "1334", "203": "1337", "276": "1377",
           "502": "1340", "135": "1332"}
    cases = [
        ("本卡合并 v3 主卡 `136-parseform-body-consumed-and-maxmemory-threshold.md` 与其深挖件。", "PROV"),
        ("g 的**状态机**（12 个基础态 + `_Gscan` 位）细节见 120 卡；", "DEFER"),
        ("### 顺手纠正 v3 底稿（209 卡）里也讲反的一处", "PROV"),
        ("细节（`readerCount` 负值编码、`readerWait` 配平）**见 203 卡**，本卡不重复。", "DEFER"),
        ("且与现用 v3 卡 `276-array-stack-vs-linked-stack-alloc.md` 一致。", "PROV"),
        ("**同源的另外三张 v3 卡保持原样作为深挖层**：分片见 `502-*.md`；", "DEFER"),
    ]
    bad = 0
    for sent, want in cases:
        got = classify(sent)
        ok = got == want
        if not ok:
            bad += 1
        print(f"  {'✓' if ok else '✗'} [{got:9s} 期望 {want:9s}] {sent[:60]}")
    print(f"\n  自测{'全部通过' if bad == 0 else f'有 {bad} 条不符'}")
    return 0 if bad == 0 else 1


def main():
    if "--selftest" in sys.argv:
        print("【已知答案自测】")
        return _selftest()
    sup = load_supersede()
    print(f"被取代 v3 编号 = {len(sup)}（来自 v4-rework/ALL.txt 三列）\n")
    defects, prov, uncertain = scan(sup)

    print("【★ 自循环 × DEFER —— 必须改】")
    print(f"  共 {len(defects)} 处，涉及 {len(set(d[0] for d in defects))} 张 v4 卡")
    cur = None
    for name, v3, new, sent in defects:
        if name != cur:
            print(f"    ✗ {name}")
            cur = name
        print(f"        [{v3}→{new}] {sent[:100]}")

    print(f"\n【允许保留 / 正当取材声明 —— 共 {len(prov)} 处】")
    print(f"【UNCERTAIN —— 需人工判读 —— 共 {len(uncertain)} 处】")
    for name, v3, new, sent in uncertain[:15]:
        print(f"    ? {name}  [{v3}→{new}] {sent[:90]}")

    print("\n" + "=" * 50)
    if defects:
        print(f"  结论：✗ 有 {len(defects)} 处自循环外推，必须修")
        return 1
    print("  结论：✓ 无自循环外推")
    return 0


if __name__ == "__main__":
    sys.exit(main())
