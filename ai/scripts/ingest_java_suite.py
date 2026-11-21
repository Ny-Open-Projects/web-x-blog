#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""34.java-suite 四模块新课：M1/M2/M3 机械处理流水线。

用法：
  python3 ai/scripts/ingest_java_suite.py m1      # 面试专题 260 篇：front-matter + 图片/demos 改写 + QC
  python3 ai/scripts/ingest_java_suite.py m2      # 就业指导 12 篇：同上（逐篇精修另做）
  python3 ai/scripts/ingest_java_suite.py m3      # 十大中级项目 1629 篇：重命名 + front-matter + 坏图处置 + QC
  python3 ai/scripts/ingest_java_suite.py sync    # target → blog _posts + 静态资产落位
  python3 ai/scripts/ingest_java_suite.py status  # 各段计数

设计：
  - source 只读；target/34-java-suite/<m>/ 是带 front-matter 的工作副本；sync 才进 _posts/java-suite/
  - 机械改写仅限：front-matter 添加、图片/demos 相对路径改写、坏图剔除、m3 重命名防冲突
  - QC 门禁：首行必须 # 标题 / 无 ''' 围栏 / 引用资产必须存在 / 文件必须被索引收录（M1）
"""
from __future__ import annotations
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "work/source/34.java-suite"
TGT = ROOT / "work/target/34-java-suite"
POSTS = ROOT / "work/blog/source/_posts/java-suite"
IMG_DST = ROOT / "work/blog/source/images/java-suite"
DEMO_DST = ROOT / "work/blog/source/demos/java-suite"
RPT = TGT / "_reports"

COURSE = "Java后端进阶全套"
DATE = "2026-11-18"

# M1：管线元文档不发布；INDEX 漏收的 5 篇成稿手工定章（2026-11-18 实核：快排属基础篇，CHM/HashMap 并发属并发篇）
M1_SKIP_META = {"改写规范.md", "课件资源利用与关联映射.md"}
M1_CHAPTER_OVERRIDES = {
    "170-25-快速排序_单边循环(lomuto)_演示.md": "基础篇",
    "176-26-快速排序_单边循环(lomuto)_实现_分区.md": "基础篇",
    "182-27-快速排序_单边循环(lomuto)_实现_递归.md": "基础篇",
    "180-27-ConcurrentHashMap_v7_演示Segment[0].md": "并发篇",
    "246-53-HashMap_并发扩容死链(1.7).md": "并发篇",
}

M1_IMG_PREFIX = "/images/java-suite/m1"
M1_DEMO_PREFIX = "/demos/java-suite"

# ---------------------------------------------------------------- helpers

def parse_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return fallback

def first_heading_ok(text: str) -> bool:
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        return s.startswith("# ")
    return False

def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text

def m1_chapter_map() -> dict[str, str]:
    """从 m1 的 INDEX.md 解析 文件名 → 章名 映射（权威分组）。"""
    idx = SRC / "m1-interview/INDEX.md"
    mapping: dict[str, str] = {}
    if not idx.exists():
        return mapping
    chapter = "未分组"
    pat_sec = re.compile(r"^##\s+(.+?)（\d+\s*篇）")
    pat_link = re.compile(r"^- \[([^\]]+)\]\(\./([^)]+\.md)\)")
    for line in idx.read_text(encoding="utf-8").splitlines():
        m = pat_sec.match(line.strip())
        if m:
            chapter = m.group(1).strip()
            continue
        m = pat_link.match(line.strip())
        if m:
            mapping[m.group(2)] = chapter
    return mapping

def qc_text(rel: str, text: str, issues: list[str]) -> None:
    if not first_heading_ok(text):
        issues.append(f"{rel}: 首个非空行不是 # 标题")
    if "'''" in text:
        issues.append(f"{rel}: 出现三单引号围栏 '''")
    for pat, label in [
        (r"(?<![`\w])机器翻译(?![`\w])", "机翻残留字样"),
        (r"##\s*(?:总结|小结)\s*[:：]?\s*$", "空总结节"),
        (r"\bTODO\b", "TODO 残留"),
    ]:
        if re.search(pat, text):
            issues.append(f"{rel}: {label}")

def write_report(name: str, data: dict) -> None:
    RPT.mkdir(parents=True, exist_ok=True)
    (RPT / f"{name}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# ---------------------------------------------------------------- M1

def run_m1() -> None:
    src_dir = SRC / "m1-interview"
    out_dir = TGT / "m1"
    out_dir.mkdir(parents=True, exist_ok=True)
    chapters = m1_chapter_map()
    issues: list[str] = []
    processed: list[dict] = []
    skipped = {"INDEX.md", "Java术语白话注解.md"}

    files = sorted(src_dir.glob("*.md"))
    for f in files:
        if f.name in skipped or f.name in M1_SKIP_META:
            continue
        raw = strip_front_matter(f.read_text(encoding="utf-8"))
        if f.name not in chapters and f.name not in M1_CHAPTER_OVERRIDES:
            issues.append(f"{f.name}: 未被 INDEX 收录且无章名覆盖表")
        chapter = chapters.get(f.name) or M1_CHAPTER_OVERRIDES.get(f.name, "未分组")
        rel = f.name
        # 资产路径改写
        raw = re.sub(r"!\[([^\]]*)\]\(images/", rf"![\1]({M1_IMG_PREFIX}/", raw)
        raw = re.sub(r"\]\(demos/", f"]({M1_DEMO_PREFIX}/", raw)
        # 校验引用资产存在
        for m in re.finditer(r"!\[[^\]]*\]\((/images/java-suite/m1/[^\)]+)\)", raw):
            rel_asset = m.group(1).replace(M1_IMG_PREFIX, "images", 1)
            if not (src_dir / rel_asset).exists():
                issues.append(f"{rel}: 坏图 {rel_asset}")
        for m in re.finditer(r"\((/demos/java-suite/[^\)]+)\)", raw):
            rel_asset = m.group(1).replace(M1_DEMO_PREFIX, "demos", 1)
            if not (src_dir / rel_asset).exists():
                issues.append(f"{rel}: 坏 demos 链接 {rel_asset}")
        qc_text(rel, raw, issues)
        title = parse_title(raw, f.stem)
        fm = (
            "---\n"
            f"title: \"{title}\"\n"
            f"date: {DATE}\n"
            f"categories: [{COURSE}, M1 面试专题, {chapter}]\n"
            "tags: [Java, 面试]\n"
            "---\n\n"
        )
        (out_dir / f.name).write_text(fm + raw, encoding="utf-8")
        processed.append({"file": f.name, "chapter": chapter, "title": title})

    # 术语白话注解 → 一篇独立卡
    gl = src_dir / "Java术语白话注解.md"
    if gl.exists():
        raw = strip_front_matter(gl.read_text(encoding="utf-8"))
        title = parse_title(raw, "Java 术语白话注解")
        fm = (
            "---\n"
            f"title: \"{title}\"\n"
            f"date: {DATE}\n"
            f"categories: [{COURSE}, M1 面试专题, 术语速查]\n"
            "tags: [Java, 面试, 术语]\n"
            "---\n\n"
        )
        raw = re.sub(r"!\[([^\]]*)\]\(images/", rf"![\1]({M1_IMG_PREFIX}/", raw)
        raw = re.sub(r"\]\(demos/", f"]({M1_DEMO_PREFIX}/", raw)
        (out_dir / "m1-000-Java术语白话注解.md").write_text(fm + raw, encoding="utf-8")
        processed.append({"file": "m1-000-Java术语白话注解.md", "chapter": "术语速查", "title": title})

    write_report("m1", {
        "source_files": len(files), "processed": len(processed),
        "chapters": chapters, "issues": issues, "posts": processed})
    print(f"M1: 源 {len(files)} 篇（含 INDEX/术语注解 2 篇特殊），产出 {len(processed)} 篇，问题 {len(issues)}")
    for i in issues[:20]:
        print("  -", i)
    if len(issues) > 20:
        print(f"  ... 其余 {len(issues) - 20} 条见 _reports/m1.json")

# ---------------------------------------------------------------- M2

def run_m2() -> None:
    src_dir = SRC / "m2-jobguide"
    out_dir = TGT / "m2"
    out_dir.mkdir(parents=True, exist_ok=True)
    issues: list[str] = []
    processed: list[dict] = []
    for f in sorted(src_dir.glob("*.md")):
        raw = strip_front_matter(f.read_text(encoding="utf-8"))
        raw = re.sub(r"!\[([^\]]*)\]\(images/", rf"![\1]({M1_IMG_PREFIX.replace('/m1', '/m2')}/", raw)
        qc_text(f.name, raw, issues)
        title = parse_title(raw, f.stem)
        # 主题 tag 从文件名推断（工作篇/市场篇/求职篇/面试篇/试用期篇/拓展）
        stem = f.stem
        topic = "拓展"
        for key in ["工作篇", "市场篇", "求职篇", "面试篇", "试用期篇"]:
            if key in stem:
                topic = key
                break
        fm = (
            "---\n"
            f"title: \"{title}\"\n"
            f"date: {DATE}\n"
            f"categories: [{COURSE}, M2 就业指导, {topic}]\n"
            f"tags: [Java, 求职, {topic}]\n"
            "---\n\n"
        )
        out_name = f"m2-{f.name}"
        (out_dir / out_name).write_text(fm + raw, encoding="utf-8")
        processed.append({"file": out_name, "topic": topic, "title": title})
    write_report("m2", {"source_files": len(list(src_dir.glob('*.md'))),
                        "processed": len(processed), "issues": issues, "posts": processed})
    print(f"M2: 产出 {len(processed)} 篇，问题 {len(issues)}")
    for i in issues:
        print("  -", i)

# ---------------------------------------------------------------- M3

def run_m3() -> None:
    src_root = SRC / "m3-javaee-10projects/blog"
    out_dir = TGT / "m3"
    out_dir.mkdir(parents=True, exist_ok=True)
    issues: list[str] = []
    processed: list[dict] = []
    stage_dirs = sorted(d for d in src_root.iterdir() if d.is_dir())
    total = 0
    for sd in stage_dirs:
        sm = re.match(r"^(\d{2})\.", sd.name)
        stage_no = sm.group(1) if sm else "xx"
        stage_name = re.sub(r"^\d{2}\.", "", sd.name)
        for f in sorted(sd.glob("*.md")):
            total += 1
            raw = strip_front_matter(f.read_text(encoding="utf-8"))
            # 坏图：引用但源里没有 images 目录 → 剔除该图行
            bad_img = re.compile(r"^!\[[^\]]*\]\([^)]+\)\s*$", re.M)
            n_bad = len(bad_img.findall(raw))
            if n_bad:
                raw = bad_img.sub("", raw)
                raw = re.sub(r"\n{3,}", "\n\n", raw)
                issues.append(f"{sd.name}/{f.name}: 剔除 {n_bad} 处坏图（源无 images）")
            # 相对 md 内链 → 去链接留文字
            inner = re.compile(r"\[([^\]]+)\]\(\./?[^)]+\.md\)")
            if inner.search(raw):
                raw = inner.sub(r"\1", raw)
                issues.append(f"{sd.name}/{f.name}: 相对 md 内链已降级为纯文字")
            qc_text(f"{sd.name}/{f.name}", raw, issues)
            title = parse_title(raw, f.stem)
            fm = (
                "---\n"
                f"title: \"{title}\"\n"
                f"date: {DATE}\n"
                f"categories: [{COURSE}, M3 十大中级项目, {stage_name}]\n"
                "tags: [Java, 项目实战]\n"
                "---\n\n"
            )
            out_name = f"m3-s{stage_no}-{f.name}"
            (out_dir / out_name).write_text(fm + raw, encoding="utf-8")
            processed.append({"file": out_name, "stage": stage_name, "title": title})
    write_report("m3", {"source_files": total, "processed": len(processed),
                        "issues": issues, "stages": [d.name for d in stage_dirs]})
    print(f"M3: 源 {total} 篇，产出 {len(processed)} 篇，问题 {len(issues)}")
    for i in issues[:15]:
        print("  -", i)
    if len(issues) > 15:
        print(f"  ... 其余 {len(issues) - 15} 条见 _reports/m3.json")

# ---------------------------------------------------------------- sync

def sync() -> None:
    POSTS.mkdir(parents=True, exist_ok=True)
    counts = {}
    for m in ("m1", "m2", "m3"):
        src_dir = TGT / m
        if not src_dir.exists():
            continue
        n = 0
        for f in sorted(src_dir.glob("*.md")):
            shutil.copy2(f, POSTS / f.name)
            n += 1
        counts[m] = n
    # M4 重写稿（target/m4/posts → _posts，QC PASS 的才进站）
    m4_posts = TGT / "m4/posts"
    if m4_posts.exists():
        import json as _json
        units = {u["out"]: u["id"] for u in _json.loads((TGT / "m4/_units.json").read_text(encoding="utf-8"))}
        failed = set(_json.loads((TGT / "m4/_m4_state.json").read_text(encoding="utf-8")).get("failed", []))
        n = 0
        for f in sorted(m4_posts.glob("*.md")):
            if units.get(f.name) in failed:
                continue
            shutil.copy2(f, POSTS / f.name)
            n += 1
        counts["m4"] = n
    # 静态资产
    img_src = SRC / "m1-interview/images"
    if img_src.exists():
        dst = IMG_DST / "m1"
        dst.mkdir(parents=True, exist_ok=True)
        if not any(dst.iterdir()):
            shutil.copytree(img_src, dst, dirs_exist_ok=True)
    demo_src = SRC / "m1-interview/demos"
    if demo_src.exists():
        DEMO_DST.mkdir(parents=True, exist_ok=True)
        if not (DEMO_DST / "m1").exists():
            shutil.copytree(demo_src, DEMO_DST / "m1")
    print("sync 完成:", counts, "| _posts/java-suite 总数:", len(list(POSTS.glob('*.md'))))
    print("images:", sum(1 for _ in IMG_DST.rglob('*.png')), "demos:", sum(1 for _ in DEMO_DST.rglob('*.html')))

def status() -> None:
    for seg, p in [("source", SRC), ("target", TGT), ("posts", POSTS)]:
        if p.exists():
            n = len(list(p.rglob("*.md")))
            print(f"{seg}: {p}  {n} md")
        else:
            print(f"{seg}: {p}  (缺)")

# ---------------------------------------------------------------- main

def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "m1":
        run_m1()
    elif cmd == "m2":
        run_m2()
    elif cmd == "m3":
        run_m3()
    elif cmd == "sync":
        sync()
    else:
        status()

if __name__ == "__main__":
    main()
