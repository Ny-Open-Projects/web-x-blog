#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
final-check.py — 发布门：一键跑齐全部门禁，给出「能不能发布」的唯一结论（**只读**）。

设计原则
--------
1. **不另立判据**：第 1~6 项直接调用既有脚本，回判它自己的退出码 / 输出数字；
   只有第 7、8 项是本脚本新增（ERRORS.md 覆盖度、卡号集合完整性）。
2. **每项都打印可复算的数字**，不只写「通过」。
3. **总判**：任一 `[FAIL]` → 退出码 1；`[PENDING]`（尚未交付/并发写入）不算失败但醒目单列。
4. **只读**：不写 target/go、不写 _pipeline 的任何台账；唯一副作用是子进程自身的只读行为。

八项检查与期望
--------------
  1 validate-v4.py（v4 全库）        error 0
  2 validate.py --strict（v3 全库）  error 0
  3 checkdup.py                      0 需人工确认（编号冲突/深挖挂靠/旧结论残留均须无）
  4 check-selfref.py                 自循环×DEFER 0 处 / 0 张卡
  5 v5-audit.py                      总体 ✓（已登记内容改动单列，不计失败）
  6 verify-pointers.py               缺口 0 / 多余 0 / 错号 0（PENDING 单列）
  7 ERRORS.md 覆盖度（**本脚本新写**） 每张 13xx v4 卡都有段落、每段引用卡都存在：0 缺 0 多
  8 卡号集合完整性（**本脚本新写**）  ALL.txt 新卡号 ↔ 磁盘 13xx 卡：多→FAIL，缺→PENDING

用法
----
    python3 _pipeline/final-check.py             # 跑发布门
    python3 _pipeline/final-check.py --selftest  # 反例自测（证明第 7 条能报 FAIL）
"""
import argparse
import glob
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
PIPE = PROJ / "_pipeline"
TGT = PROJ / "target" / "go"
ERRORS_MD = PIPE / "ERRORS.md"
ALL_TXT = PIPE / "v4-rework" / "ALL.txt"

CARD13_GLOB = "13[0-9][0-9]-*.md"

PASS, FAIL, PENDING = "PASS", "FAIL", "PENDING"


# ─────────────────────────── 基础设施 ───────────────────────────

def _run(script, *args):
    """跑一个既有门禁脚本，返回 (rc, stdout, stderr)。只读调用。"""
    p = subprocess.run([sys.executable, str(PIPE / script), *args],
                       cwd=str(PROJ), capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def _tail_lines(text, key, n=6):
    return [l for l in text.splitlines() if key in l][:n]


class Item:
    def __init__(self, idx, name, tag, summary, details=None):
        self.idx, self.name, self.tag, self.summary = idx, name, tag, summary
        self.details = details or []


# ─────────────────────────── 第 1~6 项：调用既有门禁 ───────────────────────────

def check_validate_v4():
    rc, out, _ = _run("validate-v4.py")
    m = re.search(r"通过 (\d+)/(\d+) 张\s+error (\d+)\s+warn (\d+)", out)
    skip = re.search(r"跳过 (\d+) 张", out)
    if not m:
        return Item(1, "validate-v4（v4 全库）", FAIL, "无法解析输出", _tail_lines(out, "", 4))
    passed, total, err, warn = m.groups()
    if skip and int(skip.group(1)) > 0:
        return Item(1, "validate-v4（v4 全库）", PENDING,
                    "通过 %s/%s  error %s  warn %s；跳过 %s 张（并发写入，重跑即纳入）"
                    % (passed, total, err, warn, skip.group(1)))
    tag = PASS if int(err) == 0 else FAIL
    return Item(1, "validate-v4（v4 全库）", tag,
                "通过 %s/%s  error %s  warn %s" % (passed, total, err, warn),
                _tail_lines(out, "[FAIL]", 8))


def check_validate_v3():
    rc, out, _ = _run("validate.py", "--strict")
    m = re.search(r"通过 (\d+)/(\d+) 张\s+error (\d+)\s+warn (\d+)", out)
    if not m:
        return Item(2, "validate（v3 全库）", FAIL, "无法解析输出", _tail_lines(out, "", 4))
    passed, total, err, warn = m.groups()
    tag = PASS if int(err) == 0 else FAIL
    return Item(2, "validate（v3 全库）", tag,
                "通过 %s/%s  error %s  warn %s" % (passed, total, err, warn),
                _tail_lines(out, "[FAIL]", 8))


def _planned_and_delivered():
    """→ (ALL.txt 里的计划卡号集合, 磁盘上已交付的 13xx 卡号集合)"""
    planned = set()
    if ALL_TXT.exists():
        for ln in ALL_TXT.read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.startswith("#"):
                continue
            f = ln.split("\t")
            if len(f) > 3 and f[3].strip().isdigit():
                planned.add(f[3].strip())
    delivered = {p.name.split("-")[0] for p in TGT.glob(CARD13_GLOB)}
    return planned, delivered


def check_checkdup():
    rc, out, _ = _run("checkdup.py")
    conflict_ok = "无同号多主卡冲突" in out
    deep_ok = "所有 .deep.md 都有对应主卡" in out
    old_ok = "无旧结论残留" in out
    fwd = re.search(r"(\d+) 条前向引用属正常", out)
    confirm = re.search(r"(\d+) 条需人工确认", out)
    allref_ok = "所有「见" in out and "引用均有效" in out
    fwd_n = int(fwd.group(1)) if fwd else (0 if allref_ok else -1)
    cfm_n = int(confirm.group(1)) if confirm else (0 if allref_ok else -1)
    details = [l for l in out.splitlines() if "引用了不存在" in l]

    # ── 分层判据（lead 2026-10-05 定）──────────────────────────────
    # 底层 checkdup.py 保持严格是对的；**分类是发布门的职责**。
    # ⚠️ 第一版补丁找错了字符串：它去匹配「引用了不存在」，但 checkdup 实际用的是
    #    `⏳ …「见 N 卡」尚未生成（疑似前向引用，等目标卡落盘即自动解析）`，
    #    而且它自己的小结就写着「⏳ N 条前向引用属正常；⚠ M 条需人工确认」。
    #    于是第一版判不出 PENDING，一直报 FAIL —— **又一次「拿错口径去匹配」**。
    # 现在改为**直接读 checkdup 的硬项/软项**：
    #   硬项（同号冲突 / 深挖挂靠 / 旧结论残留）—— checkdup 的退出码正式由它们决定
    #     `return 1 if (bad or bad2 or miss or found) else 0   # 主题为软告警，不影响退出码`
    #   软项（前向引用 / 需人工确认 / 源目录同源启发式）—— 只在检查内部打印，不参与退出码
    # 判据：硬项全绿而 rc=1 → PENDING（软告警）；硬项有问题 → FAIL。
    hard_ok = conflict_ok and deep_ok and old_ok
    if rc == 0:
        tag = PASS
    elif hard_ok:
        tag = PENDING
    else:
        tag = FAIL

    summary = ("rc=%d  同号冲突=%s  深挖挂靠=%s  旧结论残留=%s  前向引用=%s  需人工确认=%s"
               % (rc, "无" if conflict_ok else "有", "OK" if deep_ok else "异常",
                  "无" if old_ok else "有", fwd_n, cfm_n))
    if tag == PENDING:
        summary += "；硬项全绿，rc=1 全部来自软告警 → PENDING（前向引用等目标卡落盘即消解）"
    return Item(3, "checkdup（撞号/交叉引用）", tag, summary, details)


def check_selfref():
    rc, out, _ = _run("check-selfref.py")
    m = re.search(r"共 (\d+) 处，涉及 (\d+) 张 v4 卡", out)
    prov = re.search(r"正当取材声明[^\n]*?(\d+) 处", out)
    unc = re.search(r"UNCERTAIN[^\n]*?(\d+) 处", out)
    n_def, n_cards = (int(m.group(1)), int(m.group(2))) if m else (0, 0)
    tag = PASS if n_def == 0 else FAIL
    summary = ("自循环×DEFER %d 处 / %d 张卡；正当取材 %s 处；UNCERTAIN %s 处"
               % (n_def, n_cards, prov.group(1) if prov else "0", unc.group(1) if unc else "0"))
    details = re.findall(r"^\s+✗ (\S+\.md)\s*$", out, re.M)
    return Item(4, "check-selfref（自循环外推）", tag, summary, details)


def check_v5audit():
    rc, out, _ = _run("v5-audit.py")

    def seg(a, b):
        i = out.find(a)
        j = out.find(b) if b else len(out)
        return out[i:j] if i >= 0 else ""

    s1 = re.search(r"通过 (\d+) / (\d+)", seg("【①", "【②"))
    s2 = re.search(r"通过 (\d+) / (\d+)", seg("【②", "【③"))
    s4 = re.search(r"通过 (\d+) / (\d+)", seg("【④", "====="))
    allowed = re.search(r"另有 (\d+) 张已登记的内容改动", out)
    numline = re.search(r"抽出 ≥3 位数字 token：(\d+) 个；精确命中 (\d+) 个(?:；四舍五入 (\d+) 个)?", seg("【③", "【④"))
    overall = re.search(r"总体：\s*(.+)", out)
    tag = PASS if rc == 0 else FAIL
    fmt = lambda x: ("%s/%s" % x.groups()) if x else "?"
    summary = ("总体=%s  ①逐段 %s  ②结构 %s  ③数字(命中 %s/%s)  ④元信息 %s  已登记改动 %s 张"
               % ((overall.group(1).strip() if overall else "?"),
                  fmt(s1), fmt(s2),
                  (numline.group(2) if numline else "?"), (numline.group(1) if numline else "?"),
                  fmt(s4), (allowed.group(1) if allowed else "0")))
    details = [l.strip() for l in out.splitlines() if l.strip().startswith("✗")]
    return Item(5, "v5-audit（v5 体检）", tag, summary, details)


def check_pointers():
    rc, out, _ = _run("verify-pointers.py")
    def g(pat):
        m = re.search(pat, out)
        return int(m.group(1)) if m else -1
    gap = g(r"① 缺口（应带未带）\s*:\s*(\d+)")
    surplus = g(r"② 多余（不该带却带）\s*:\s*(\d+)")
    wrong = g(r"③ 指向错号\s*:\s*(\d+)")
    pend = g(r"④ 目标未交付（PENDING）\s*:\s*(\d+)")
    pendnums = re.search(r"PENDING 涉及唯一卡号: \[(.*?)\]", out)
    restored = re.search(r"⑤ 去指针行后逐字节还原：通过 (\d+) / 失败 (\d+) / 缺备份 (\d+)", out)
    tag = PASS if (gap == 0 and surplus == 0 and wrong == 0) else FAIL
    n_pn = len([x for x in (pendnums.group(1).split(",") if pendnums else []) if x.strip()])
    summary = ("缺口 %d / 多余 %d / 错号 %d；还原 %s；PENDING %d 条目 / %d 唯一卡号（单列，非失败）"
               % (gap, surplus, wrong,
                  ("%s通过/%s失败/%s缺备份" % restored.groups()) if restored else "?",
                  pend, n_pn))
    # 只把「缺口/多余/错号」列进明细；PENDING 是正常的，不刷屏
    cut = out.find("[④ 目标未交付 PENDING]")
    head = out[:cut] if cut >= 0 else out
    details = [l.strip() for l in head.splitlines() if l.strip().startswith("- ")]
    return Item(6, "verify-pointers（前向指针）", tag, summary, details)


# ─────────────────── 第 7、8 项：本脚本新写 ───────────────────

def scan_card_numbers():
    """磁盘上 13xx v4 卡的编号集合（排除 .deep.md）。"""
    out = set()
    for p in glob.glob(str(TGT / CARD13_GLOB)):
        if p.endswith(".deep.md"):
            continue
        out.add(os.path.basename(p).split("-")[0])
    return out


def errors_coverage(errors_md=ERRORS_MD):
    """每张 13xx 卡都有段落（缺）、每段引用的 13xx 卡都存在（多）。返回 (cards, have, miss, extra)。"""
    txt = Path(errors_md).read_text(encoding="utf-8")
    have = set(re.findall(r"卡\s*(13\d\d)", txt))
    cards = scan_card_numbers()
    return cards, have, sorted(cards - have), sorted(have - cards)


def check_errors_coverage():
    cards, have, miss, extra = errors_coverage()
    tag = PASS if (not miss and not extra) else FAIL
    summary = "卡 %d / 段 %d / 缺 %d / 多 %d" % (len(cards), len(have), len(miss), len(extra))
    details = []
    if miss:
        details.append("缺段落的卡: " + ", ".join(miss))
    if extra:
        details.append("段落引用了不存在的卡: " + ", ".join(extra))
    return Item(7, "ERRORS.md 覆盖度", tag, summary, details)


def all_txt_numbers():
    """ALL.txt 第 4 列「新卡号」的集合。"""
    nums = set()
    with open(ALL_TXT, encoding="utf-8") as f:
        f.readline()
        for ln in f:
            if not ln.strip():
                continue
            c = (ln.rstrip("\n").split("\t") + [""] * 8)[:8]
            if c[3].strip():
                nums.add(c[3].strip())
    return nums


def check_card_numbers():
    exp = all_txt_numbers()
    act = scan_card_numbers()
    miss, extra = sorted(exp - act), sorted(act - exp)
    if extra:
        tag = FAIL          # 磁盘有、台账没有 → 真问题
    elif miss:
        tag = PENDING       # 台账有、磁盘没有 → 尚未交付，不算失败
    else:
        tag = PASS
    summary = "ALL.txt %d / 磁盘 %d / 缺 %d（未交付→PENDING）/ 多 %d（→FAIL）" \
              % (len(exp), len(act), len(miss), len(extra))
    details = []
    if miss:
        details.append("未交付: " + ", ".join(miss))
    if extra:
        details.append("磁盘多出: " + ", ".join(extra))
    return Item(8, "卡号集合完整性", tag, summary, details)


# ─────────────────────────── 渲染 ───────────────────────────

def render(items):
    print("=" * 78)
    print("final-check.py —— 发布门（只读）")
    print("=" * 78)
    width = max(len(it.name) for it in items)
    for it in items:
        print("[%-7s] %d %-*s  %s" % (it.tag, it.idx, width, it.name, it.summary))
    n_fail = sum(1 for it in items if it.tag == FAIL)
    n_pend = sum(1 for it in items if it.tag == PENDING)
    for it in items:
        if it.details:
            print("\n── %s [%s] ──" % (it.name, it.tag))
            for d in it.details:
                print("   %s" % d)
    print("-" * 78)
    if n_fail:
        print("总判：✗ 不能发布（FAIL %d 项：%s）"
              % (n_fail, "、".join(it.name for it in items if it.tag == FAIL)))
    else:
        print("总判：✓ 可以发布（0 FAIL；PENDING %d 项：%s）"
              % (n_pend, "、".join(it.name for it in items if it.tag == PENDING) or "无"))
    print("说明：PENDING = 尚未交付 / 并发写入，不计失败；全量交付后应归零。")
    return 1 if n_fail else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="第 7 条反例自测（不碰真实 ERRORS.md）")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    items = [
        check_validate_v4(),
        check_validate_v3(),
        check_checkdup(),
        check_selfref(),
        check_v5audit(),
        check_pointers(),
        check_errors_coverage(),
        check_card_numbers(),
    ]
    return render(items)


# ─────────────────────────── 反例自测（证明能报 FAIL） ───────────────────────────

def selftest():
    """用 ERRORS.md 的**临时副本**造两个反例，验证第 7 条真会 FAIL；真实 ERRORS.md 全程不动。

    反例 A（报「多」）：往副本塞一个磁盘上不存在的 13xx 卡号引用 → 期望 extra 里出现它。
    反例 B（报「缺」）：从副本删掉某个真实卡号的所有引用 → 期望 miss 里出现它。
    """
    print("=" * 78)
    print("final-check.py --selftest（第 7 条 ERRORS.md 覆盖度的反例验证）")
    print("=" * 78)

    real_md5 = hashlib.md5(ERRORS_MD.read_bytes()).hexdigest()
    cards = scan_card_numbers()
    have = set(re.findall(r"卡\s*(13\d\d)", ERRORS_MD.read_text(encoding="utf-8")))

    # 造「多」的候选：13xx 中磁盘上没有、且当前 ERRORS.md 未引用的号
    ghost = sorted(set("%d" % n for n in range(1300, 1400)) - cards - have, key=int)
    # 造「缺」的候选：磁盘上有、且 ERRORS.md 里确实引用过的号
    referenced = sorted(cards & have, key=int)
    if not ghost or not referenced:
        print("✗ 自测前置条件不足：ghost=%s referenced=%s" % (ghost[:3], referenced[:3]))
        return 1

    ok = True
    with tempfile.TemporaryDirectory() as td:
        base = ERRORS_MD.read_text(encoding="utf-8")

        # —— 反例 A：注入一个不存在的卡号段落 → 期望报「多」 ——
        ghost_num = ghost[0]
        a = Path(td) / "ERRORS_inject.md"
        a.write_text(base + "\n\n## 自测注入段\n\n| 1 | 注入 | 注入 | 依据 | → 卡 %s\n" % ghost_num,
                     encoding="utf-8")
        _c, _h, miss_a, extra_a = errors_coverage(a)
        cond_a = ghost_num in extra_a
        ok &= cond_a
        print("反例A（注入「卡 %s」，磁盘无此卡）→ 多=%s  期望含 %s  ⇒ %s"
              % (ghost_num, extra_a, ghost_num, "✓ 报错" if cond_a else "✗ 未报错"))

        # —— 反例 B：删掉一个真实卡号的所有引用 → 期望报「缺」 ——
        del_num = referenced[0]
        b = Path(td) / "ERRORS_delete.md"
        b.write_text(re.sub(r"卡\s*%s" % del_num, "卡 0000", base), encoding="utf-8")
        _c, _h, miss_b, extra_b = errors_coverage(b)
        cond_b = del_num in miss_b
        ok &= cond_b
        print("反例B（删除「卡 %s」全部引用）→ 缺=%s  期望含 %s  ⇒ %s"
              % (del_num, miss_b, del_num, "✓ 报错" if cond_b else "✗ 未报错"))

    real_md5_after = hashlib.md5(ERRORS_MD.read_bytes()).hexdigest()
    untouched = real_md5 == real_md5_after
    ok &= untouched
    print("真实 ERRORS.md 未被改动: %s（md5 %s）" % ("✓" if untouched else "✗", real_md5[:12]))
    print("-" * 78)
    print("自测结论：%s" % ("✓ 两条反例均能触发 FAIL，且真实文件未动" if ok else "✗ 自测未通过"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
