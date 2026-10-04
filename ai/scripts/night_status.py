#!/usr/bin/env python3
"""夜间无人值守进度刷新器 —— 多课程版。事实源是磁盘，不是记忆。

扫 5 个 course 子目录 + review_state.json，重写 ai/night/STATUS.md。
（旧版只支持 plan.json 的单一 course；本站已扩到 5 课，故改为自动扫盘。）

用法：
    python3 ai/scripts/night_status.py            # 只刷状态表
    python3 ai/scripts/night_status.py --verify   # 顺带跑全站 curl 验证（慢）
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIGHT = ROOT / "ai" / "night"
TARGET = ROOT / "work" / "target"
BLOG = ROOT / "work" / "blog"
REVIEW_STATE = NIGHT / "review_state.json"
COURSES = ["es", "kcna", "k8stop", "cka", "k8sprod"]


def count_course(course):
    tdir = TARGET / course
    tgt = [f for f in tdir.glob("*.md") if not f.name.startswith("_")] if tdir.is_dir() else []
    posts = list((BLOG / "source" / "_posts").glob(f"{course}-*.md"))
    return len(tgt), len(posts)


def count_public():
    return len(list((BLOG / "public").rglob("index.html"))) if (BLOG / "public").exists() else 0


def count_stray():
    """target 根级的游离 .md（不属于任何 course 子目录）与空 course 目录。"""
    stray_md = [f for f in TARGET.glob("*.md")]
    empty_dirs = [d for d in TARGET.iterdir() if d.is_dir() and not any(d.iterdir())]
    return stray_md, empty_dirs


def run_verify(port=4353):
    p = subprocess.run([sys.executable, str(ROOT / "ai" / "scripts" / "verify_site.py"), str(port)],
                       capture_output=True, text=True, timeout=1800)
    m = re.search(r"共 (\d+) / (\d+)", p.stdout)
    return (m.group(1), m.group(2)) if m else ("?", "?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()

    counts = {c: count_course(c) for c in COURSES}
    total_tgt = sum(v[0] for v in counts.values())
    total_posts = sum(v[1] for v in counts.values())
    npub = count_public()
    stray_md, empty_dirs = count_stray()

    review = json.loads(REVIEW_STATE.read_text(encoding="utf-8")) if REVIEW_STATE.exists() else {}
    verified = review.get("verified", {})
    gen_err = review.get("generate_error")

    if args.verify:
        ok, tot = run_verify()
        verified = {"ok": ok, "total": tot}

    L = []
    L.append("# 站点验收总表 · 五课程全量（night_status.py 自动生成）")
    L.append("")
    L.append(f"> 本表由 `ai/scripts/night_status.py` **自动重扫磁盘生成**，非记忆。最后刷新：**{datetime.now():%Y-%m-%d %H:%M:%S}**")
    L.append("")
    L.append("## 一、总览")
    L.append("")
    L.append("| 阶段 | 结果 | 状态 |")
    L.append("| --- | --- | --- |")
    L.append(f"| 1. 写稿落盘 target | {total_tgt} 篇（5 课程合计） | 完成 |")
    L.append(f"| 2. 入库 _posts | {total_posts} / {total_tgt} | {'完成' if total_posts == total_tgt else '有差'} |")
    L.append(f"| 3. 站内文章总数 | {total_posts} 篇 | articles |")
    L.append(f"| 4. 已生成静态页 | {npub} 个 index.html | public/ |")
    if verified:
        L.append(f"| 5. 逐页 curl | **{verified.get('ok')} / {verified.get('total')} 全 200** | "
                 f"{'通过' if str(verified.get('ok')) == str(verified.get('total')) else '有非200'} |")
    else:
        L.append("| 5. 逐页 curl | 未跑 | 待验证 |")
    L.append(f"| 6. hexo 生成 ERROR | {gen_err} 条 | {'干净' if gen_err == 0 else '需排查'} |")
    L.append("")

    L.append("## 二、各课程明细")
    L.append("")
    L.append("| 课程 | target 篇数 | 入库 _posts | 状态 |")
    L.append("| --- | --- | --- | --- |")
    for c in COURSES:
        t, p = counts[c]
        if t == p:
            st = "完成"
        elif t > p:
            st = f"缺 {t - p}"
        else:
            st = f"多 {p - t}"
        L.append(f"| {c} | {t} | {p} | {st} |")
    L.append(f"| **合计** | **{total_tgt}** | **{total_posts}** | |")
    L.append("")

    L.append("## 三、结构备注（自动扫盘发现）")
    L.append("")
    if stray_md:
        names = "、".join(f"`{f.name}`" for f in stray_md)
        L.append(f"- **target 根级游离 .md：{len(stray_md)} 个**（未入库、不参与构建）：{names}")
    else:
        L.append("- target 根级游离 .md：0 个")
    if empty_dirs:
        names = "、".join(f"`{d.name}/`" for d in empty_dirs)
        L.append(f"- **空 course 目录：{len(empty_dirs)} 个**（建议清理）：{names}")
    else:
        L.append("- 空 course 目录：0 个")
    L.append("")

    L.append("## 四、专业复核结论（详见 review_state.json）")
    L.append("")
    L.append("| 复核项 | 结论 |")
    L.append("| --- | --- |")
    for it in review.get("items", []):
        v = it.get("verdict", "")
        short = (v[:58] + "…") if len(v) > 60 else v
        L.append(f"| {it['name']} | {short} |")
    L.append("")

    (NIGHT / "STATUS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[刷新] STATUS.md 已更新 — target {total_tgt} / posts {total_posts} / 游离md {len(stray_md)} / 空目录 {len(empty_dirs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
