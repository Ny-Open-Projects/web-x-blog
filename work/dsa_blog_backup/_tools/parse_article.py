#!/usr/bin/env python3
"""
从 CSDN 博客 HTML 中提取：
- 题目描述、示例、提示、进阶
- 每个 TS/Py/Go/Java 代码块 + 方案名

输出为结构化 JSON。
"""
import re
import json
import sys
from html import unescape
from pathlib import Path

META_DIR = Path("/Users/Wang/Code/webfault-ai/dsa/_meta")
ART_DIR = META_DIR / "articles"


def decode_entities(s: str) -> str:
    s = unescape(s)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    s = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), s)
    return s


def clean_html(s: str) -> str:
    s = decode_entities(s)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</?p[^>]*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</li[^>]*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\n\s*\n", "\n", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def extract_from_prism_code(html_code: str) -> str:
    html_code = decode_entities(html_code)
    text = re.sub(r"</?span[^>]*>", "", html_code)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\xa0", " ")
    lines = []
    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def extract_blog(html: str):
    title_match = re.search(
        r'<h1[^>]*class="title-article"[^>]*>(.*?)</h1>', html, re.DOTALL
    )
    blog_title = clean_html(title_match.group(1)) if title_match else ""

    # 找描述段（描述内容 <p> 紧跟 #### 题目标题）
    # 取 h1 之后到下一个 h4 之前的内容
    after_h1 = html[title_match.end():] if title_match else html
    desc_block = re.search(
        r'(<h[1-6][^>]*>(?:<a[^>]*></a>)?\s*[^<]{1,100}?</h[1-6]>)(.*?)(?=<h[1-6])',
        after_h1, re.DOTALL
    )

    problem_title = ""
    description_lines = []
    if desc_block:
        # 描述段的 h 内容是 "描述" 或题目标题
        problem_title = clean_html(desc_block.group(1))
        desc_html = desc_block.group(2)
        # 截取到下一个 h4 为止的 <p> 和 <li>
        end = re.search(r'<h[1-6]', desc_html)
        if end:
            desc_html = desc_html[:end.start()]
        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", desc_html, re.DOTALL)
        for p in paragraphs:
            t = clean_html(p)
            if t and "收录于" not in t and "Data Structure" not in t and "CSDN" not in t:
                description_lines.append(t)
        items = re.findall(r"<li[^>]*>(.*?)</li>", desc_html, re.DOTALL)
        for it in items:
            t = clean_html(it)
            if t and "收录于" not in t:
                description_lines.append(t)

    def get_section(label: str) -> str:
        pat = re.compile(
            r'<h[1-6][^>]*>(?:<a[^>]*></a>)?\s*' + label + r'\s*</h[1-6]>(.*?)(?=<h[1-6])',
            re.DOTALL
        )
        m = pat.search(html)
        if not m:
            return ""
        section_html = m.group(1)
        # 截断到下一个 h
        end = re.search(r'<h[1-6]', section_html)
        if end:
            section_html = section_html[:end.start()]
        result_parts = []
        # pre 块（如示例）
        for pb in re.findall(
            r'<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>', section_html, re.DOTALL
        ):
            text = decode_entities(re.sub(r"<[^>]+>", "", pb))
            result_parts.append(text.strip())
        # <p> 块
        for p in re.findall(r'<p[^>]*>(.*?)</p>', section_html, re.DOTALL):
            t = clean_html(p)
            if t:
                result_parts.append(t)
        # <li> 块
        for it in re.findall(r'<li[^>]*>(.*?)</li>', section_html, re.DOTALL):
            t = clean_html(it)
            if t:
                result_parts.append(t)
        return "\n\n".join(result_parts)

    examples = get_section("示例")
    hint = get_section("提示")
    advance = get_section("进阶")

    # 提取方案标题：方案N: 名称
    sol_title_pat = re.compile(
        r'<h[1-6][^>]*>(?:<a[^>]*></a>)?\s*([^<]*?方案\s*\d+\s*[:：]\s*[^<]+?)\s*</h[1-6]>',
        re.DOTALL
    )
    sol_titles = [clean_html(m.group(1)) for m in sol_title_pat.finditer(html)]

    code_pat = re.compile(
        r'<pre[^>]*>\s*<code[^>]*class="[^"]*language-(\w+)[^"]*"[^>]*>(.*?)</code>\s*</pre>',
        re.DOTALL
    )
    solutions = []
    matches = list(code_pat.finditer(html))
    for i, m in enumerate(matches):
        lang = m.group(1).lower()
        body = extract_from_prism_code(m.group(2))
        # 找对应方案名
        sol_name = None
        prefix = html[max(0, m.start() - 2000):m.start()]
        candidates = re.findall(
            r'<h[1-6][^>]*>(?:<a[^>]*></a>)?\s*([^<]*?方案\s*\d+\s*[:：][^<]+?)\s*</h[1-6]>',
            prefix
        )
        if candidates:
            sol_name = clean_html(candidates[-1])
        elif sol_titles and i < len(sol_titles):
            sol_name = sol_titles[i]
        elif sol_titles:
            sol_name = f"方案{i + 1}"
        else:
            sol_name = f"方案{i + 1}"

        solutions.append({
            "lang": lang,
            "name": sol_name,
            "code": body,
        })

    return {
        "blog_title": blog_title,
        "problem_title": problem_title,
        "description_lines": description_lines,
        "examples": examples,
        "hint": hint,
        "advance": advance,
        "solutions": solutions,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: parse_article.py <id>")
        sys.exit(1)

    aid = sys.argv[1]
    html_path = ART_DIR / f"{aid}.html"
    if not html_path.exists():
        print(f"Not found: {html_path}")
        sys.exit(1)

    html = html_path.read_text(encoding="utf-8", errors="ignore")
    result = extract_blog(html)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()