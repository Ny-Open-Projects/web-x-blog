#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""34.java-suite M4（精英进阶六大项目）：merged 1671 稿 → 写作单元切分。

用法：
  python3 ai/scripts/m4_build_units.py build   # 生成 _units.json（幂等，重跑覆盖）
  python3 ai/scripts/m4_build_units.py status  # 单元/断点统计

设计：
  - manifest.json 权威映射：阶段(六大项目) → 章 → 视频（章内按 video_id 排序即课时序）
  - 单元预算：累计 >=10 个视频 且 >=90KB 即成单元；硬顶 20 视频（控制单次写作输入）
  - 断点：_m4_state.json {done:[], failed:[], cursor}
"""
from __future__ import annotations
import json
import re
import sys
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
M4 = ROOT / "work/source/34.java-suite/m4-advanced-6projects"
OUT = ROOT / "work/target/34-java-suite/m4"
UNITS = OUT / "_units.json"
STATE = OUT / "_m4_state.json"

MIN_VIDEOS, MIN_BYTES, MAX_VIDEOS = 10, 90_000, 20

STAGE_SLUG = {
    "阶段一": "中台战略与组件化开发",
    "阶段二": "品达物流TMS",
    "阶段三": "智牛股",
    "阶段四": "千亿级电商秒杀解决方案",
    "阶段五": "物联网新零售-亿可控",
    "阶段六": "物联网新零售-立可得",
}

def build() -> None:
    m = json.load(open(M4 / "manifest.json", encoding="utf-8"))
    pat = re.compile(r"\d+、(阶段[一二三四五六七八九十])[^\\]*\\(.+?)\\([^\\]+)\.mp4$")
    tree: dict[str, dict[str, list[dict]]] = collections.OrderedDict()
    for v in m["videos"]:
        mm = pat.search(v.get("source_video", ""))
        if not mm:
            continue
        stage, chap = mm.group(1), mm.group(2)
        tree.setdefault(stage, collections.OrderedDict()).setdefault(chap, []).append(v)

    units: list[dict] = []
    uid = 0
    used: dict[str, str] = {}   # video_id -> 首个使用它的单元 out（merged 按唯一文件归属，重名条目不重复写作）
    dup_log: list[dict] = []
    for stage, chaps in tree.items():
        proj = STAGE_SLUG.get(stage, stage)
        for chap, vids in chaps.items():
            vids.sort(key=lambda x: x["video_id"])
            buf: list[dict] = []
            buf_bytes = 0

            def flush(buf, buf_bytes):
                nonlocal uid
                if not buf:
                    return
                uid += 1
                first = re.sub(r"【一手：[^】]*】", "", buf[0]["video_id"])
                first = re.sub(r"【一手：.*$", "", first)
                first = re.sub(r"[\\/:*?\"<>|\s]+", "-", first)[:40]
                units.append({
                    "id": f"u{uid:03d}",
                    "stage": stage,
                    "project": proj,
                    "chapter": chap,
                    "videos": [b["video_id"] for b in buf],
                    "bytes": buf_bytes,
                    "out": f"m4-{uid:03d}-{first}.md",
                })

            for v in vids:
                vid = v["video_id"]
                if vid in used:
                    dup_log.append({"video_id": vid, "stage": stage, "chapter": chap,
                                    "claimed_by": used[vid]})
                    continue
                f = M4 / f"{vid}_merged.md"
                if not f.exists():
                    dup_log.append({"video_id": vid, "stage": stage, "chapter": chap,
                                    "claimed_by": "MERGED_MISSING"})
                    continue
                used[vid] = None  # 先占位，flush 时回填
                buf.append(v)
                buf_bytes += f.stat().st_size
                if len(buf) >= MIN_VIDEOS and buf_bytes >= MIN_BYTES:
                    flush(buf, buf_bytes)
                    for b in buf:
                        used[b["video_id"]] = units[-1]["out"]
                    buf, buf_bytes = [], 0
                elif len(buf) >= MAX_VIDEOS:
                    flush(buf, buf_bytes)
                    for b in buf:
                        used[b["video_id"]] = units[-1]["out"]
                    buf, buf_bytes = [], 0
            flush(buf, buf_bytes)
            for b in buf:
                used[b["video_id"]] = units[-1]["out"] if units else None

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "posts").mkdir(exist_ok=True)
    UNITS.write_text(json.dumps(units, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "_dup_report.json").write_text(json.dumps(dup_log, ensure_ascii=False, indent=1), encoding="utf-8")
    if not STATE.exists():
        STATE.write_text(json.dumps({"done": [], "failed": [], "cursor": 0}, ensure_ascii=False), encoding="utf-8")
    total_v = sum(len(u["videos"]) for u in units)
    print(f"单元 {len(units)} 个，覆盖唯一 merged {total_v}/1671，重名/缺失条目 {len(dup_log)}（见 _dup_report.json）")
    print(f"最小 {min(u['bytes'] for u in units)//1000}KB，最大 {max(u['bytes'] for u in units)//1000}KB")
    by_proj = collections.Counter(u["project"] for u in units)
    for k, n in by_proj.items():
        print(f"  {k}: {n} 单元")

def status() -> None:
    if not UNITS.exists():
        print("尚未 build")
        return
    units = json.loads(UNITS.read_text(encoding="utf-8"))
    st = json.loads(STATE.read_text(encoding="utf-8"))
    done = set(st["done"])
    posts = OUT / "posts"
    written = {p.name for p in posts.glob("*.md")} if posts.exists() else set()
    expect = {u["out"] for u in units if u["id"] in done}
    missing = expect - written
    print(f"单元 {len(units)} | 已写 {len(written)} | done 标记 {len(done)} | 标记缺文件 {len(missing)}")
    nxt = [u["id"] for u in units if u["id"] not in done and u["out"] not in written][:5]
    print("下一批:", nxt)
    if missing:
        print("标记了 done 但文件缺失:", sorted(missing)[:5])

def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "build":
        build()
    else:
        status()

if __name__ == "__main__":
    main()
