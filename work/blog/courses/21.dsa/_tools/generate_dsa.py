#!/usr/bin/env python3
"""
将 _meta/all_urls.tsv + _meta/articles/<id>.html 解析后，
按 dsa/<lang>/<topic>/lc_<id>_<name>/ 结构生成多语言代码文件。
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

sys.path.insert(0, str(Path(__file__).parent))
from csdn_parser import extract_blog

DSA_DIR = Path("/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa")
META_DIR = DSA_DIR / "_meta"
ART_DIR = META_DIR / "articles"
TSV = META_DIR / "all_urls.tsv"
LANGS = ("ts", "python", "go", "java")
EXT_MAP = {"ts": "ts", "python": "py", "go": "go", "java": "java"}

# 主题归一化
TOPIC_MAP = {
    "数组": "array",
    "字符串": "string",
    "链表": "linked_list",
    "栈": "stack",
    "队列": "queue",
    "字典": "hash",
    "集合": "hash",
    "Set": "hash",
    "堆": "heap",
    "二叉树": "tree",
    "矩阵": "matrix",
    "图": "graph",
    "动态规划": "dp",
    "递归": "backtrack",
    "贪心": "greedy",
    "查找": "binary_search",
    "排序": "sort",
    "LRU": "linked_list",
    "异步": "concurrency",
    "笔记": "notes",
}


def parse_title(title: str) -> Tuple[Optional[str], Optional[str], str]:
    """从标题解析 (题号, 题目, 主题)。"""
    m = re.match(
        r"数据结构与算法之([^:]+):\s*"
        r"(?:(LeetCode\s+(\S+)\.\s*)?(.+?))\s*"
        r"\(([^)]+)\)$",
        title.strip(),
    )
    if not m:
        return None, None, "other"
    topic_cn = m.group(1).strip()
    lc_id = m.group(3)
    problem_name = m.group(4).strip()
    topic_en = TOPIC_MAP.get(topic_cn, "other")
    return lc_id, problem_name, topic_en


def title_to_slug(s: str) -> str:
    s = re.sub(r"[\s,，。：:；;!?]", "_", s)
    s = re.sub(r"_+", "_", s)
    s = s.strip("_")
    return s.lower()[:40]


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_\-]", "_", name)


def render_ts(name: str, code: str, problem_title: str, blog_url: str) -> str:
    return (
        "/**\n"
        f" * LeetCode 题目：{problem_title}\n"
        f" * 方案：{name}\n"
        f" * 来源：{blog_url}\n"
        " *\n"
        " * 注意：本文件代码由原博客 TypeScript 解法整理而来。\n"
        " * 使用方式：\n"
        " *   npm install -D typescript ts-node\n"
        " *   npx ts-node solution_xxx.ts\n"
        " */\n\n"
        f"{code}\n"
    )


def render_python(name: str, code: str, problem_title: str, blog_url: str) -> str:
    return (
        '"""\n'
        f"LeetCode 题目：{problem_title}\n"
        f"方案：{name}\n"
        f"来源：{blog_url}\n"
        "\n"
        "本文件代码由 TypeScript 版本等价转写为 Python 实现。\n"
        "运行：python3 solution_xxx.py\n"
        '"""\n\n'
        f"{code}\n"
    )


def render_go(name: str, code: str, problem_title: str, blog_url: str) -> str:
    return (
        "// Package main 提供 LeetCode 题目的 Go 实现。\n"
        "//\n"
        f"// 题目：{problem_title}\n"
        f"// 方案：{name}\n"
        f"// 来源：{blog_url}\n"
        "//\n"
        "// 运行：go run solution_xxx.go\n"
        "//\n"
        "// 本文件代码由 TypeScript 版本等价转写为 Go 实现。\n"
        "package main\n\n"
        f"{code}\n"
    )


def render_java(name: str, code: str, problem_title: str, blog_url: str, class_name: str) -> str:
    return (
        "package com.webfault.dsa;\n\n"
        "/**\n"
        f" * LeetCode 题目：{problem_title}\n"
        f" * 方案：{name}\n"
        f" * 来源：{blog_url}\n"
        " */\n"
        f"public class {class_name} {{\n\n"
        f"    {code}\n"
        "}}\n"
    )


def generate_for_one(aid: str, title: str, blog_url: str, html_path: Path, only_lang: str = None) -> bool:
    if not html_path.exists():
        return False
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    if 'class="title-article"' not in html:
        return False

    lc_id, problem_name, topic_en = parse_title(title)
    if not lc_id:
        topic_en = "notes"
        lc_id = aid
        problem_name = title.split(":", 1)[-1].strip().split("(")[0].strip()
        if not problem_name:
            problem_name = title

    slug = title_to_slug(problem_name)
    folder_name = f"lc_{lc_id.replace('.', '_')}_{slug}"
    blog_url = blog_url.replace(
        "active.blog.csdn.net/article/details/",
        "blog.csdn.net/tyro_java/article/details/",
    )

    data = extract_blog(html)

    description = "\n".join(f"- {line}" for line in data["description_lines"])
    if not description:
        description = "(原始博客未提供题目描述)"
    examples = data["examples"] or "(无)"
    hint = data["hint"] or "(无)"
    advance = data["advance"] or "(无)"

    solutions = data["solutions"]
    if not solutions:
        return False

    target_langs = [only_lang] if only_lang else LANGS

    for lang in target_langs:
        ext = EXT_MAP[lang]
        out_dir = DSA_DIR / "code" / lang / topic_en / folder_name
        out_dir.mkdir(parents=True, exist_ok=True)

        readme_path = out_dir / "README.md"
        if not readme_path.exists():
            readme_text = (
                f"# LeetCode {lc_id}. {problem_name} ({lang})\n\n"
                f"> 来源：[Wang's Blog]({blog_url})\n"
                f"> 语言：**{lang}**（{'博客原文' if lang == 'ts' else '由 TypeScript 等价转写'}）\n\n"
                "## 题目描述\n\n"
                f"{description}\n\n"
                "## 示例\n\n"
                f"```\n{examples}\n```\n\n"
                "## 提示\n\n"
                f"{hint}\n\n"
                "## 进阶\n\n"
                f"{advance}\n\n"
                "## 解法列表\n\n"
                "| 方案 | 文件 | 来源语言 |\n"
                "| --- | --- | --- |\n"
            )
            for i, sol in enumerate(solutions, start=1):
                fname = f"solution_{i}_{title_to_slug(sol['name']).strip('_')}.{ext}"
                readme_text += f"| {sol['name']} | `{fname}` | {sol['lang']} |\n"
            readme_path.write_text(readme_text, encoding="utf-8")

        for i, sol in enumerate(solutions, start=1):
            fname = f"solution_{i}_{title_to_slug(sol['name']).strip('_')}.{ext}"
            fpath = out_dir / fname
            if fpath.exists():
                continue
            problem_title = f"LeetCode {lc_id}. {problem_name}"
            if lang == "ts":
                content = render_ts(sol["name"], sol["code"], problem_title, blog_url)
            elif lang == "python":
                content = render_python(sol["name"], sol["code"], problem_title, blog_url)
            elif lang == "go":
                content = render_go(sol["name"], sol["code"], problem_title, blog_url)
            elif lang == "java":
                class_name = f"Solution{safe_filename(problem_name.replace(' ', ''))}{i}"
                content = render_java(sol["name"], sol["code"], problem_title, blog_url, class_name)
            else:
                continue
            fpath.write_text(content, encoding="utf-8")
    return True


def main():
    if not TSV.exists():
        print(f"Missing {TSV}")
        sys.exit(1)

    only_lang = sys.argv[1] if len(sys.argv) > 1 else None

    ok = fail = 0
    with TSV.open(encoding="utf-8") as f:
        header = f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            aid, title, url, page = parts[:4]
            html_path = ART_DIR / f"{aid}.html"
            try:
                if generate_for_one(aid, title, url, html_path, only_lang):
                    ok += 1
                else:
                    fail += 1
            except Exception as e:
                print(f"FAIL {aid} ({title}): {e}")
                fail += 1
    print(f"\nDone. Success: {ok}, Fail: {fail}")


if __name__ == "__main__":
    main()