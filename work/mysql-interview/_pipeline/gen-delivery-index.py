#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交付索引生成器：把 ALL.txt 的 82 个源 ↔ 磁盘上的卡 ↔ ERRORS.md 段 ↔ speed30 拼成一张表。

用法：
    python3 _pipeline/gen-delivery-index.py            # 生成 _pipeline/DELIVERY-INDEX.md
    python3 _pipeline/gen-delivery-index.py --selftest # 已知答案自测（含反例）

只读：本脚本对 target/go/ 与 ERRORS.md **只有读操作**（自证：见文件末 SELFTEST 的零写检查）。
"""
import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
PIPE = PROJ / "_pipeline"
TGT = PROJ / "target" / "go"
ALL_TXT = PIPE / "v4-rework" / "ALL.txt"
ERRORS_MD = PIPE / "ERRORS.md"
OUT = PIPE / "DELIVERY-INDEX.md"

V5_HEADS = ("# 🎯 速记区", "## 30 秒版", "# 📖 原理区")


def load_rows(all_txt: Path):
    """→ [(源id, 章节, 卡号, 标题)]"""
    out = []
    for ln in all_txt.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.split("\t")
        if len(f) < 5:
            continue
        out.append((f[0].strip(), f[1].strip(), f[3].strip(), f[4].strip()))
    return out


def gate_map(tgt: Path):
    """跑一次全库 validate-v4，解析 {文件名: '✓6 ✗0 ⚠0'} 或 {'文件名': 'FAIL'}"""
    try:
        p = subprocess.run([sys.executable, str(PIPE / "validate-v4.py")],
                           cwd=str(PROJ), capture_output=True, text=True, timeout=600)
        out = p.stdout
    except Exception:
        return {}
    m = {}
    for line in out.splitlines():
        g = re.match(r"\[(PASS|FAIL)\]\s+(\S+\.md)\s*(.*)$", line)
        if g:
            m[g.group(2)] = ("✓6 ✗0 ⚠0" if g.group(1) == "PASS" else "FAIL")
    return m


def errors_linemap(errors_md: Path):
    """→ {卡号: 首次出现 '卡 N' 的行号}

    ⚠️ 2026-10-05 自测打回一次：初版正则写成 `卡\\s*(1[34]\\d\\d)`（只匹配 1300~1499），
    用 9002 造的用例直接暴露「超出范围就静默漏掉」。已改成 `\\d{3,4}` 的通用范围 ——
    **写死区间的正则 = 埋一颗以后才炸的雷**（本项目的章节名/编号范围都踩过同类坑）。
    """
    m = {}
    if not errors_md.exists():
        return m
    for i, ln in enumerate(errors_md.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        for num in re.findall(r"卡\s*(\d{3,4})", ln):
            m.setdefault(num, i)
    return m


def build(tgt: Path, all_txt: Path, errors_md: Path, speed_dir: Path, run_gate=True):
    rows = load_rows(all_txt)
    gates = gate_map(tgt) if run_gate else {}
    elines = errors_linemap(errors_md)
    recs, missing = [], []
    for src, ch, num, title in rows:
        hits = sorted(tgt.glob(f"{num}-*.md"))
        if not hits:
            missing.append(num)
            recs.append(dict(src=src, ch=ch, num=num, title=title, fname="（未交付）",
                             md5="-", size=0, gate="-", v5="-", eline="-", sp="-"))
            continue
        p = hits[0]
        b = p.read_bytes()
        t = b.decode("utf-8", errors="ignore")
        counts = [t.count(h) for h in V5_HEADS]
        recs.append(dict(
            src=src, ch=ch, num=num, title=title, fname=p.name,
            md5=hashlib.md5(b).hexdigest(), size=len(b),
            gate=gates.get(p.name, "（未解析）"),
            v5="/".join(str(c) for c in counts),
            eline=elines.get(num, "-"),
            sp="有" if (speed_dir / f"{num}.md").exists() else "无",
        ))
    return recs, missing, len(rows)


def render(recs, missing, total):
    lines = ["# 交付索引（自动生成，勿手改）", ""]
    lines += [f"> 由 `_pipeline/gen-delivery-index.py` 生成；覆盖 `ALL.txt` 的 **{total} 个源**。",
              "> 重跑本脚本即可刷新（有新卡落盘时）。", ""]
    lines += ["| 源id | 章节 | 卡号 | 标题 | 卡文件名 | md5 | bytes | 门禁 | v5结构 | ERRORS段 | speed30 |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in recs:
        lines.append(f"| {r['src']} | {r['ch']} | {r['num']} | {r['title']} | `{r['fname']}` | "
                     f"`{r['md5'][:12] if r['md5'] != '-' else '-'}` | {r['size'] or '-'} | {r['gate']} | "
                     f"{r['v5']} | {r['eline']} | {r['sp']} |")
    # 摘要 1：按章
    bych = {}
    for r in recs:
        bych.setdefault(r["ch"], []).append(r)
    lines += ["", "## 一、按章汇总", "", "| 章 | 卡数 | 合计 bytes | 平均 bytes |", "|---|---|---|---|"]
    for ch in sorted(bych, key=int):
        v = bych[ch]
        ss = [x["size"] for x in v if x["size"]]
        lines.append(f"| ch{ch} | {len(v)} | {sum(ss):,} | {(sum(ss)//len(ss)):,} |" if ss
                     else f"| ch{ch} | {len(v)} | - | - |")
    # 摘要 2：交付状态
    lines += ["", "## 二、交付状态", "",
              f"- 已交付 **{total - len(missing)} / {total}**", f"- 未交付 **{len(missing)}**" +
              (f"：{'、'.join(sorted(missing, key=int))}" if missing else "（无）")]
    # 摘要 3：总计
    sizes = [r["size"] for r in recs if r["size"]]
    if sizes:
        lines += ["", "## 三、总计", "",
                  f"- 卡数 **{len(sizes)}**",
                  f"- 总 bytes **{sum(sizes):,}**（{sum(sizes)/1024/1024:.2f} MB）",
                  f"- 平均 **{sum(sizes)//len(sizes):,}**（{sum(sizes)/len(sizes)/1024:.1f} KB）",
                  f"- 最小 / 最大 **{min(sizes):,} / {max(sizes):,}**"]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    recs, missing, total = build(TGT, ALL_TXT, ERRORS_MD, PIPE / "speed30")
    OUT.write_text(render(recs, missing, total), encoding="utf-8")

    # ── 三个计数自证 ──────────────────────────────────────────
    idx_rows = len(recs)
    on_disk = sum(1 for r in recs if r["size"])
    print(f"ALL.txt 源数        = {total}")
    print(f"索引行数            = {idx_rows}")
    print(f"磁盘命中（已交付）  = {on_disk}")
    print(f"未交付              = {len(missing)}" + (f"：{'、'.join(sorted(missing, key=int))}" if missing else ""))
    print(f"→ 写入 {OUT}（{len(OUT.read_text(encoding='utf-8').splitlines())} 行）")
    if idx_rows != total:
        print("✗ 自证失败：索引行数 != ALL.txt 源数")
        return 1
    if on_disk + len(missing) != total:
        print("✗ 自证失败：已交付 + 未交付 != 总数")
        return 1
    print("✓ 三处计数自洽")
    return 0


def selftest():
    """已知答案自测：3 行假 ALL.txt + 假磁盘；含一个「磁盘缺卡」反例。"""
    tmp = Path(tempfile.mkdtemp(prefix="di-selftest-"))
    try:
        (tmp / "_pipeline").mkdir(); (tmp / "target" / "go").mkdir(parents=True)
        allx = tmp / "_pipeline" / "ALL.txt"
        allx.write_text(
            "# 源id\t章节\t主v3卡\t新卡号\t标题\tv3主卡数\t同源其它v3主卡\t同源deep伴随件\n"
            "1-1\t01\t\t9001\t甲题\t1\t\t\n"
            "1-2\t01\t\t9002\t乙题\t1\t\t\n"
            "1-3\t01\t\t9003\t丙题\t1\t\t\n", encoding="utf-8")
        err = tmp / "_pipeline" / "ERRORS.md"
        err.write_text("## 第 1 章 X·甲题（源 1-1，卡 9001）\n## 第 1 章 X·乙题（源 1-2，卡 9002）\n",
                       encoding="utf-8")
        # 造 9001/9002 两张卡（v5 形态），9003 故意不造 = 反例
        for n, name in (("9001", "9001-甲.md"), ("9002", "9002-乙.md")):
            (tmp / "target" / "go" / name).write_text(
                f"# {n} 题\n\n> 来源：`1-x 题`\n\n# 🎯 速记区（考前只看这里）\n\n## 30 秒版\n\nx\n\n"
                f"# 📖 原理区（要搞懂原理再往下）\n\n正文\n", encoding="utf-8")
        sp = tmp / "_pipeline" / "speed30"; sp.mkdir()
        (sp / "9001.md").write_text("x", encoding="utf-8")

        recs, missing, total = build(tmp / "target" / "go", allx, err, sp, run_gate=False)
        ok = True
        def chk(label, got, want):
            nonlocal ok
            good = got == want
            ok &= good
            print(f"  {'✓' if good else '✗'} {label}: {got}" + ("" if good else f"（应 {want}）"))
        print("【自测】")
        chk("总源数", total, 3)
        chk("索引行数", len(recs), 3)
        chk("已交付", sum(1 for r in recs if r['size']), 2)
        chk("★反例：缺卡识别", missing, ["9003"])
        chk("v5结构计数(9001)", recs[0]["v5"], "1/1/1")
        chk("ERRORS 段行号(9002)", recs[1]["eline"], 2)
        chk("speed30(9001)", recs[0]["sp"], "有")
        chk("speed30(9002)", recs[1]["sp"], "无")
        print(f"  自测{'全部通过' if ok else '有不符'}")
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
