#!/usr/bin/env python3
# blog_qa.py — 博客全面质量审核（结构 / 代码可运行 / 链接 / SVG XML / 占位符 / 一致性）
# 用法: python3 blog_qa.py [--fast]   （--fast 跳过代码运行）
import os, re, sys, glob, subprocess, tempfile
import xml.etree.ElementTree as ET

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
FAST = "--fast" in sys.argv
issues = []  # (severity, blog, desc)

def add(sev, blog, desc):
    issues.append((sev, blog, desc))

def run(cmd, timeout=60):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

def extract_block(txt, header_pat, lang):
    m = re.search(header_pat + r"[^\n]*\s*```" + lang + r"\n(.*?)```", txt, re.S)
    return m.group(1) if m else None

# 收集博客
pilot = "001_二叉树的最大深度"
blogs = sorted(d for d in os.listdir(f"{DSA}/") if os.path.isdir(f"{DSA}/{d}"))
langs_head = ["Go", "Java", "Rust", "Lua", "C", "C++", "R", "Zig", "Dart", "Python"]

tmpdir = tempfile.mkdtemp()
for d in blogs:
    p = f"{DSA}/{d}/index.md"
    if not os.path.exists(p):
        add("P0", d, "缺 index.md")
        continue
    txt = open(p, encoding="utf-8").read()
    is_pilot = (d == pilot)

    # ---- 结构 ----
    if not is_pilot:
        for sec in ["## 题目描述", "## 题目分析", "## 解题思路",
                    "## TypeScript 解题方案", "## 逐步拆解", "## 附录", "## 内容总结"]:
            if sec not in txt:
                add("P0", d, f"缺章节: {sec}")
        if txt.count("```mermaid") < 1:
            add("P0", d, "缺 mermaid 流程图")
        if "![动态算法图" not in txt:
            add("P0", d, "动画未用图片引用式")
        if txt.count("```typescript") < 1:
            add("P0", d, "正文缺 TS 方案代码")
    # 围栏配对
    if txt.count("```") % 2 != 0:
        add("P0", d, "代码围栏不配对")
    # 语言标签合法性
    for m in re.finditer(r"```(\w+)", txt):
        if m.group(1) not in {"typescript", "ts", "python", "go", "java", "rust", "lua", "c", "cpp", "r", "zig", "dart", "mermaid", "text"}:
            add("P1", d, f"异常代码语言标签: {m.group(1)}")
    # 占位符 / 乱码
    for pat, desc in [(r"\{title\}", "模板占位符 {title}"), (r"\{ts_code\}", "模板占位符 {ts_code}"),
                      (r"\{anim\}", "模板占位符 {anim}"), (r"\{sol_list\}", "模板占位符 {sol_list}"),
                      (r"�", "乱码替换符")]:
        if re.search(pat, txt):
            add("P0", d, desc)
    # 11 语言附录
    if not is_pilot:
        for l in langs_head:
            if f"### {l}" not in txt:
                add("P0", d, f"附录缺 {l}")
    # 每个附录代码块非空
    app = re.search(r"## 9\. 附录.*", txt, re.S)
    if not is_pilot and app:
        n_groups = len(re.findall(r"### \S+ 实现（\d+ 种方案）", app.group(0)))
        if n_groups != 10:
            add("P0", d, f"附录语言组 {n_groups}/11")
    for mm in re.finditer(r"```mermaid\n(.*?)```", txt, re.S):
        body = mm.group(1)
        if not re.match(r"graph (TD|LR)", body):
            add("P1", d, "mermaid 缺 graph 声明")
        if body.count('"') % 2 != 0:
            add("P1", d, "mermaid 引号疑似不配对")
    if app:
        for m in re.finditer(r"```(\w+)\n(.*?)```", app.group(0), re.S):
            if len(m.group(2).strip()) < 20:
                add("P0", d, f"附录 {m.group(1)} 代码块过短/为空")

    # ---- TS 主解法代码块可运行 ----
    m1 = re.search(r"### 方案 1.*?```typescript\n(.*?)```", txt, re.S) if not is_pilot else None
    ts = m1.group(1) if m1 else None
    if ts is None and not is_pilot:
        add("P0", d, "未提取到 TypeScript 方案 1 代码块")
    elif ts is not None:
        if len(ts.strip()) < 40:
            add("P0", d, "TS 方案 1 代码块过短")
        elif not FAST:
            f = os.path.join(tmpdir, f"qa_{abs(hash(d))}.ts")
            open(f, "w", encoding="utf-8").write(ts)
            r = run(["node", f], timeout=30)
            if r is None:
                add("P1", d, "TS 代码运行超时")
            elif r.returncode != 0:
                err = (r.stderr or r.stdout).strip().split("\n")
                add("P0", d, "TS 主解法运行失败: " + err[-1][:120] if err else "TS 运行失败")
    # ---- Python 对照代码块可运行（exit 0 判据）----
    py = extract_block(txt, r"## 5\. Python 对照实现", "python")
    if py is not None and not FAST:
        if len(py.strip()) < 20:
            add("P1", d, "Python 对照代码块过短")
        else:
            f = os.path.join(tmpdir, f"qa_{abs(hash(d))}.py")
            open(f, "w", encoding="utf-8").write(py)
            r = run(["python3", f], timeout=30)
            if r is None:
                add("P1", d, "Python 代码运行超时")
            elif r.returncode != 0:
                err = (r.stderr or r.stdout).strip().split("\n")
                add("P0", d, "Python 对照运行失败: " + err[-1][:120] if err else "Python 运行失败")

    # ---- 相对链接有效性（剥离代码块，避免把 C++ lambda 等代码内容当链接）----
    base = f"{DSA}/{d}"
    prose = re.sub(r"```.*?```", "", txt, flags=re.S)
    for m in re.finditer(r"\]\(([^)]+)\)", prose):
        link = m.group(1)
        if link.startswith("http") or link.startswith("#"):
            continue
        rel = link.split("#")[0].replace("%28", "(").replace("%29", ")")
        if not rel:
            continue
        if rel.startswith("../"):
            target = f"{DSA}/{rel[3:]}"
        else:
            target = f"{base}/{rel}"
        # glob 兜底（导航链接形如 001_最小栈/index.md）
        if not os.path.exists(target):
            add("P1", d, f"坏相对链接: {link}")

    # ---- 动画：XML 合法性 + 内嵌与文件一致 ----
    import glob as _glob
    for svgf in _glob.glob(f"{base}/animation*.svg"):
        try:
            ET.fromstring(open(svgf, encoding="utf-8").read())
        except ET.ParseError as e:
            add("P0", d, f"SVG XML 解析失败 {os.path.basename(svgf)}: {e}")
    svg_file = f"{base}/animation.svg"
    if os.path.exists(svg_file):
        if not is_pilot and "![动态算法图" not in txt:
            add("P1", d, "动画未用图片引用式")
        if "<svg" in txt and not is_pilot:
            add("P2", d, "仍残留内联 SVG（应图片引用式）")
    # 每方案 GIF 动画引用与文件配对
    for m in re.finditer(r"\]\((animation[^)]*\.gif)\)", txt):
        if not os.path.exists(f"{base}/{m.group(1)}"):
            add("P1", d, f"缺动画 GIF: {m.group(1)}")
    sec5 = re.search(r"## TypeScript 解题方案(.*?)## 逐步拆解", txt, re.S)
    n_sec5 = len(re.findall(r"### 方案 \d+：", sec5.group(1))) if sec5 else 0
    n_anim = len(re.findall(r"\]\(animation_\d+\.gif\)", sec5.group(1))) if sec5 else 0
    if n_sec5 and n_anim < n_sec5 and not is_pilot:
        add("P2", d, f"方案专属动画不全: {n_anim}/{n_sec5}")
    # 官方示例配图引用与文件配对
    for m in re.finditer(r"\]\((imgs/[^)]+)\)", txt):
        if not os.path.exists(f"{base}/{m.group(1)}"):
            add("P1", d, f"缺官方配图: {m.group(1)}")

    # div 配对
    if txt.count("<div") != txt.count("</div>"):
        add("P1", d, f"div 标签不配对: {txt.count('<div')}/{txt.count('</div>')}")

# ---- 汇总 ----
from collections import Counter
sev = Counter(i[0] for i in issues)
print(f"审核 {len(blogs)} 篇博客 ｜ 问题: P0={sev.get('P0',0)} P1={sev.get('P1',0)} P2={sev.get('P2',0)}")
by_type = Counter(i[2].split(":")[0].split(" ")[0] if ":" in i[2] else i[2] for i in issues)
for (s, b, desc) in issues:
    print(f"[{s}] {b} :: {desc}")
