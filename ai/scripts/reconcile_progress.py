#!/usr/bin/env python3
"""把 work/target/<course>/_PROGRESS.md 和磁盘真实产出对账。

两个方向都要修，只修一个不够：
1. 滞后（写了文件但表还是 pending） -> 补成 done
2. 超前（表写 done 但文件不存在）   -> 打回 pending 并清空「产出博客」列

顺带洗掉组名里的课程推广噪音（`本章导学_ev【 微信号：itcodeba 】` -> `本章导学_ev`），
因为 `_PROGRESS.md` 是 NOISE 规则升级前那一版生成的，脚本又不会覆盖它。

用法:
    python3 ai/scripts/reconcile_progress.py kcna k8stop cka k8sprod
    python3 ai/scripts/reconcile_progress.py k8stop --dry-run
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target"

# 每一列都必须写 [^|]*：用 (.*) 是贪婪的，会把竖线一起吞掉导致整行错位
ROW = re.compile(r"^\|\s*(done|skip|pending)\s*\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|\s*$")
FENCED = re.compile(r"`([^`]+)`")


def clean_group(name: str) -> str:
    """洗掉【微信号：…】这类课程推广噪音。"""
    out = re.sub(r"【[^】]*】", "", name)
    out = re.sub(r"\[\d+\]", "", out)
    out = re.sub(r"微信号[：:]?\s*\S*", "", out)
    out = out.replace("_ev", "").strip(" --–—_")
    return out or name


def main():
    args = [a for a in sys.argv[1:]]
    # 默认是只读的：这脚本会改进度状态，误跑一次就可能把一大片 done 打成 pending。
    # 必须显式给 --write 才落盘。
    dry = "--write" not in args
    courses = [a for a in args if a not in ("--dry-run", "--write")]
    if not courses:
        print(__doc__)
        return 1
    if dry:
        print("（默认只读，加 --write 才落盘）\n")

    grand = {"补 done": 0, "打回 pending": 0, "洗组名": 0}
    for course in courses:
        prog = TARGET / course / "_PROGRESS.md"
        if not prog.exists():
            print(f"[跳过] {course}: 没有 _PROGRESS.md")
            continue
        existing = {p.name for p in (TARGET / course).glob("*.md") if not p.name.startswith("_")}
        lines = prog.read_text(encoding="utf-8").splitlines()
        fixed_done = fixed_back = fixed_name = 0

        for i, ln in enumerate(lines):
            m = ROW.match(ln)
            if not m:
                continue
            status, num, g, fc, wc, oc = (x.strip() for x in m.groups())
            fm = FENCED.search(oc)
            out_file = fm.group(1) if fm else ""
            is_outline = "不写文" in oc or (not out_file and status == "skip")

            new_status, new_out = status, oc
            if status == "skip":
                # 导学/小结 这类本来就不产出文件，一概要保持 skip，不能被误改成 pending
                pass
            elif is_outline:
                # 导学/小结 这类本来就不产出文件，不动
                pass
            elif out_file:
                # 「产出博客」列可能是完整文件名（`10-2_xxx.md`），也可能只是编号前缀
                # （`10-2` 起，build_source_index.py 生成的就是这种）
                if out_file in existing:
                    hit = True
                else:
                    stem = out_file[:-3] if out_file.endswith(".md") else out_file
                    hit = any(f.startswith(stem.rstrip("_") + "_") for f in existing)
                if hit:
                    if status != "done":
                        new_status, fixed_done = "done", fixed_done + 1
                elif status != "pending":
                    # 表上写 done 但文件不存在 -> 打回 pending。
                    # 本来就是 pending 的行不动，否则会把它们「产出博客」列的文件名洗掉。
                    new_status, new_out = "pending", "待处理"
                    fixed_back += 1
            else:
                # 「产出博客」列还是「待处理」：用组号前缀反查磁盘。
                # 必须是 startswith(num+"_")，用子串 in 会让组号 1 命中 10-1_… 造成误判。
                cand = [f for f in existing if f.startswith(num + "_")]
                if cand:
                    new_status, new_out = "done", f"`{cand[0]}`"
                    fixed_done += 1

            new_group = clean_group(g)
            if new_group != g:
                fixed_name += 1

            new = f"| {new_status} | {num} | {new_group} | {fc} | {wc} | {new_out} |"
            if dry:
                if new_status != status:
                    print(f"  将改 #{num}: {status} -> {new_status}  {new_out[:40]}")
            elif new != ln:
                lines[i] = new

        if not dry and lines:
            tmp = prog.with_suffix(".md.tmp")
            tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
            shutil.move(str(tmp), str(prog))

        grand["补 done"] += fixed_done
        grand["打回 pending"] += fixed_back
        grand["洗组名"] += fixed_name
        print(f"[{course}] 补 done {fixed_done}，打回 pending {fixed_back}，洗组名 {fixed_name}")
        if dry:
            continue

    print(f"\n合计: {grand}（dry-run={dry}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
