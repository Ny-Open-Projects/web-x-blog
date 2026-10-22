#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二轮·语义层：散文跨文章引用的去引用化
========================================
原则：CSDN 独立发表，每篇自含。把「引用其他文章」的行文改写为
「篇内/软性」行文，不改写正文语义，不碰：
  - H1 标题行（# 开头，章名是内容）
  - 代码围栏（mermaid/yaml 等）
  - code/ 课件路径行
  - 本章/本节/本篇/上文/下文（同篇内指，本就不违规）

规则集（顺序执行，先具体后通用）：
  1. 前文（第N章）/ 前文（第二章）聊过 → 前面聊过
  2. 后续章节|后续篇章|后续篇|后续讲|后续课|后续内容|后续会 → 后续
  3. 第N章主线|目标|内容|结构|就是|要|会|讲 → 本篇X
  4. 在第四章/在第 3 章 → 在前面
  5. 前文讲|前文提|前文聊|前文的|前文（第二章） → 前面；前文 → 前面
  6. 后面会讲|后面展开|后面再说 → 后面讲|后面展开|后面再说
  7. 下一章|下一节|下一篇|下一讲|下一课|下节课 → 下面
  8. 上一章|上一节|下一篇|上一讲 → 前面
  9. 后文 → 后面；稍后讲 → 稍后
 10. 前述/如前所述 保持不变（已是软行文）

用法： dry / run
"""
import os, re, sys

ROOT = "/Users/Wang/Code/github/web-x-blog/work"
TARGET = os.path.join(ROOT, "target")
RUN = (len(sys.argv) > 1 and sys.argv[1] == "run")
INTERVIEW = {"py-interview", "campus"}
CN = "0-9一二三四五六七八九十百"

EXCL = re.compile(r'code/|课件|第[二三四五六七八九十0-9]+章代码')

# 子句起点（防止「当前文档」这类复合词被误伤）；Python lookbehind 需定宽，故用 ^|(?<=..) 组合
CLAUSE = r'(?:^|(?<=[，。；：、！？\s“”"\'（）()在按把被从与和及]))'

RULES = [
    # 1. 前文（第N章） → 前面（子句起点保护）
    (re.compile(CLAUSE + r'前文\s*[（(]\s*第\s*[' + CN + r']+\s*章\s*[）)]'), '前面'),
    # 2. 后续X → 后续
    (re.compile(r'后续(?:章节|篇章|篇|讲|课|内容|会)'), '后续'),
    # 3. 多章引用 第N/M章、第N、M章 → 后续
    (re.compile(r'第\s*[' + CN + r']+\s*[/、，]\s*[' + CN + r']+\s*章'), '后续'),
    # 4. 第N章主线/目标/内容/结构 → 本篇X
    (re.compile(r'第\s*[' + CN + r']+\s*章(?=(?:主线|目标|内容|结构|地图|路线|就是|要|会|讲|聚焦|围绕|先))'), '本篇'),
    # 5. 在第N章 → 在前面
    (re.compile(r'在(?:第\s*[' + CN + r']+\s*章)'), '在前面'),
    # 6. 前文+动词 → 前面（保留动词；子句起点保护，不伤「当前文档」）
    (re.compile(CLAUSE + r'前文(?=(?:讲|提|聊|说|的|用|定义|封))'), '前面'),
    # 7. 后文 → 后面（子句起点保护）
    (re.compile(CLAUSE + r'后文'), '后面'),
    # 8. 稍后讲 → 稍后
    (re.compile(r'稍后讲'), '稍后'),
    # 8b. 后面讲/后面展开/后面再说 → 下面讲/下面展开/下面再说（篇内前指）
    (re.compile(r'后面(?=(?:讲|展开|再?说))'), '下面'),
    # 9. 下一X → 下面
    (re.compile(r'下一(?:章|节|篇|讲|课)|下节课'), '下面'),
    # 10. 上一X → 前面
    (re.compile(r'上一(?:章|节|篇|讲)'), '前面'),
    # 11. 兜底：裸「第N章」（非 EXCL 语境）→ 前述
    (re.compile(r'第\s*[' + CN + r']+\s*章'), '前述'),
]

def transform_line(line):
    for pat, repl in RULES:
        line = pat.sub(repl, line)
    return line

def transform(body):
    changed = []
    out, infence = [], False
    for l in body.split("\n"):
        if l.strip().startswith("```"):
            infence = not infence
            out.append(l)
            continue
        if infence or l.startswith("# ") or EXCL.search(l):
            out.append(l)
            continue
        nl = transform_line(l)
        if nl != l:
            changed.append((l, nl))
        out.append(nl)
    return "\n".join(out), changed

def main():
    total_files = 0
    all_changes = []
    for course in sorted(os.listdir(TARGET)):
        cd = os.path.join(TARGET, course)
        if not os.path.isdir(cd) or course == "code" or course in INTERVIEW:
            continue
        for fn in sorted(os.listdir(cd)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            if not re.match(r'\d+_', fn):
                continue
            fp = os.path.join(cd, fn)
            data = open(fp, encoding="utf-8").read()
            fm = data[:5] if data.startswith("---\n") else ""
            body = data[len(fm):] if fm else data
            new_body, changed = transform(body)
            if new_body != body:
                total_files += 1
                all_changes.extend((course, fn, o, n) for (o, n) in changed)
                if RUN:
                    open(fp, "w", encoding="utf-8").write(fm + new_body)
    print("MODE: %s  files=%d  changed-lines=%d" % ("RUN" if RUN else "DRY", total_files, len(all_changes)))
    import collections
    bycourse = collections.Counter(c for c, *_ in all_changes)
    print("per-course:", dict(bycourse))
    if not RUN:
        for course, fn, o, n in all_changes[:60]:
            print(f"[{course}/{fn[:22]}]")
            print("   -", o.strip()[:118])
            print("   +", n.strip()[:118])
        print("...(dry 只显示前 60 行)")

if __name__ == "__main__":
    main()
