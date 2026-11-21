#!/usr/bin/env python3
"""从 docs/*.md 提取标注了 `# file: <path>` 的 python 代码块到 code/ 目录,
并校验:题号连续、每个题号恰好有一个代码块、md 代码块与文件内容一一对应。

用法: python3 scripts/extract_code.py [--check]
  --check  只校验不写文件(文件内容不一致时退出码非 0)
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CODE_RE = re.compile(r"```\w*\n# file: (code/[^\n]+)\n(.*?)```", re.S)
Q_RE = re.compile(r"^### (Q\d+) · ", re.M)
CONTENT_CATS = {
    "01_语言核心与底层", "02_并发与网络工程", "03_Web后端开发",
    "04_数据库与缓存", "05_数据分析与工程化", "06_Agent与LLM及系统设计",
}


def discover_docs():
    """唯一事实来源:六大类目录下的内容 md。
    排除 docs/paths/ 生成物、backups/ 归档与 macOS 副本(文件名带空格+数字)。
    """
    return sorted(
        p for p in DOCS.rglob("*.md")
        if p.parent.name in CONTENT_CATS
        and not re.search(r"\s\d+\.md$", p.name)
    )


def main() -> int:
    check_only = "--check" in sys.argv
    total_q = 0
    total_code = 0
    global_q = []
    problems = []

    for md in discover_docs():
        text = md.read_text(encoding="utf-8")
        questions = Q_RE.findall(text)
        global_q.extend(questions)
        blocks = CODE_RE.findall(text)
        print(f"{md.relative_to(ROOT)}: {len(questions)} 题, {len(blocks)} 个代码块")

        # 题号连续性
        nums = [int(q[1:]) for q in questions]
        if nums and nums != list(range(nums[0], nums[0] + len(nums))):
            problems.append(f"{md.name}: 题号不连续")

        # 每题恰好一个代码块,且 file 路径里的题号一致
        q_to_files: dict[str, list[str]] = {}
        for path, body in blocks:
            m = re.search(r"q(\d+)_", path)
            if not m:
                problems.append(f"{md.name}: 路径缺题号 {path}")
                continue
            q = f"Q{int(m.group(1)):03d}"
            q_to_files.setdefault(q, []).append(path)
        for q in questions:
            got = q_to_files.get(q, [])
            if len(got) != 1:
                problems.append(f"{md.name}: {q} 有 {len(got)} 个代码块")
        for q, paths in q_to_files.items():
            if q not in questions:
                problems.append(f"{md.name}: {paths} 对应不存在的 {q}")

        for path, body in blocks:
            target = ROOT / path
            content = body if body.endswith("\n") else body + "\n"
            if check_only:
                if not target.exists() or target.read_text(encoding="utf-8") != content:
                    problems.append(f"内容不一致: {path}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            total_code += 1
        total_q += len(questions)

    print(f"\n总计: {total_q} 题, {total_code} 个代码文件")
    dup = [q for q, c in Counter(global_q).items() if c > 1]
    if dup:
        problems.append(f"全局题号重复 {len(dup)} 个: {sorted(dup)[:10]}")
    if total_q != 3000:
        problems.append(f"全局题目数 {total_q} != 3000")
    if problems:
        print(f"\n发现 {len(problems)} 个问题:")
        for p in problems:
            print(" -", p)
        return 1
    print("校验通过:题号连续且全局唯一,题目与代码文件一一对应。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
