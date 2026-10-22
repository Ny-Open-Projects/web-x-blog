#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pass-1b（v3）：句中/括号内跨卡引用的中性化与清除（在 pass-1 之后跑）
====================================================================
只处理非面试课（campus / py-interview 豁免，面试题互引允许存在）。

v3 修正记录：
  - front-matter YAML 区整体跳过（YAML 缩进有语义，不得压缩）
  - ``` 围栏内只做 mermaid 节点编号 / 树编号清理，其余原样
  - 取消全文空格压缩（曾压平 YAML/tags 缩进与代码对齐）
  - 「前述/此前 」后的多余空格收敛

处置口径：
  ① 溯源/覆盖说明保留（本卡覆盖 8-4/8-5、合并原 13-8 节、原文锚点第8章）
  ② 跳转/复用指引中性化或删除（沿用 9-2 思路、（4-13）、// 见后续篇章）
  ③ 旧节号标注删除（## 一、什么是提示词工程（1-1） → ## 一、什么是提示词工程）
保护：版本号/模型名/UUID/Pod hash/正则/日期/数字区间/表格版本/DFS 路径/
      第 1-2 步/课件 5.3 节/反引号内/本卡覆盖·合并原·按课程口径重构

用法： dry / run
"""
import os, re, sys

ROOT = "/Users/Wang/Code/github/web-x-blog/work"
TARGET = os.path.join(ROOT, "target")
RUN = (len(sys.argv) > 1 and sys.argv[1] == "run")
INTERVIEW = {"py-interview", "campus"}

DASH = r'\d{1,3}-\d{1,2}'

PROTECT = [
    re.compile(p) for p in [
        r'\d+\.\d+-\d+',            # Qwen2.5-7B, ChatGLM3-6B, 1.2.13-3
        r'\d+-\d+[A-Za-z]',         # Qwen2-72B, fe40eb16-1a4e, v1-6d9f8b6c4
        r'[0-9a-fA-F]{6,}-',        # UUID 片段
        r'\[\^?\\?[a-z0-9{(\[]',    # 正则字符类
        r'date:\s*20\d\d-\d\d-\d\d', r'20\d\d-\d\d-\d\d\s+\d\d:\d\d',
        r'2006-01-02', r'15:04:05', r'T\d\d:\d\d:\d\d',
        r'得到|例如|比如|按区间|映射一|~|%|\d+年|\d+月',
        r'redis-\d+-\d+', r'Pod …-\d+-\d+',
        r'\d+-\d+\s*\|\s*v\d+', r'\|\s*\d+-\d+\s*\|',
        r'5-4-11-2', r'5-8-4-5',
        r'第\s*\d+-\d+\s*步',
        r'/课件|code/',
        r'原文锚点：第\d+章',
        r'2010-1\d-\d\d', r'1990-01-01', r'2026-01-01', r'2022-1\d-\d\d',
        r'fsid|clusterID|csi-vol-',
        r'本卡覆盖|合并原|按课程口径重构',
    ]
]

def protected(ctx):
    return any(p.search(ctx) for p in PROTECT)

SUBS = [
    (re.compile(r'沿用\s*' + DASH + r'(\s*)'), r'沿用前述\1'),
    (re.compile(r'和\s*' + DASH + r'\s*一致'), '和前述一致'),
    (re.compile(r'与\s*' + DASH + r'\s*一致'), '与前述一致'),
    (re.compile(r'与\s*' + DASH + r'\s*的'), '与前述的'),
    (re.compile(r'是\s*' + DASH + r'\s*中'), '是前述中'),
    (re.compile(r'相对\s*' + DASH + r'(\s*)'), r'相对前述\1'),
    (re.compile(r'把\s*' + DASH + r'\s*讲的?'), '把前述'),
    (re.compile(r'把\s*' + DASH + r'(?=\s*在)'), '把前述'),
    (re.compile(r'把\s*' + DASH + r'\s*的概念'), '把前述概念'),
    (re.compile(r'前面\s*' + DASH + r'(\s*)'), r'前述\1'),
    (re.compile(r'写出\s*' + DASH + r'\s*那样的'), '写出前述那样的'),
    (re.compile(r'后续\s*' + DASH + r'\s*的'), '后续的'),
    (re.compile(r'源于\s*' + DASH + r'\s*那张'), '源于前述那张'),
    (re.compile(r'按\s*' + DASH + r'(\s*)'), r'按前述\1'),
    (re.compile(r'靠\s*' + DASH + r'\s*的'), '靠前述的'),
    (re.compile(r'V1\s*' + DASH + r'\s*已'), 'V1 已'),
    (re.compile(r'此节与\s*' + DASH + r'\s*的'), '此节与前述的'),
    (re.compile(r'"\s*' + DASH + r'\s*给出'), '"给出'),
]
RE_HEAD = re.compile(r'^(\s*)' + DASH + r'\s*(?:里|中)?\s*')

RE_PAREN = re.compile(r'（\s*' + DASH + r'(?:\s*/\s*' + DASH + r')*\s*）')
RE_CMT_NAV = re.compile(r'^\s*//\s*见后续篇章[^\n]*$', re.M)
RE_MERMAID_NODE = re.compile(r'\["\s*(?:第[0-9一二三四五六七八九十]+\s*章\s*)?' + DASH + r'\s+')
RE_TREE = re.compile(r'([├└]──)\s*\d{1,2}-\d{1,2}\s*')

def split_front_matter(data):
    if data.startswith("---\n"):
        end = data.find("\n---\n", 4)
        if end != -1:
            return data[:end + 5], data[end + 5:]
    return "", data

def transform(body):
    ch = {"sub": 0, "paren": 0, "cmt": 0, "mermaid": 0, "tree": 0}
    out, infence = [], False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            infence = not infence
            out.append(line)
            continue
        if infence:
            # 围栏内：只清理 mermaid 节点编号 / 树编号
            line, n1 = RE_MERMAID_NODE.subn('["', line)
            ch["mermaid"] += n1
            for m in list(RE_TREE.finditer(line)):
                ctx = line[max(0, m.start() - 22):m.end() + 22]
                if not protected(ctx):
                    line = RE_TREE.sub(lambda mm: mm.group(1) + " ", line, count=1)
                    ch["tree"] += 1
            out.append(line)
            continue
        # ---- 围栏外 ----
        for m in list(RE_PAREN.finditer(line)):
            ctx = line[max(0, m.start() - 22):m.end() + 22]
            if not protected(ctx):
                line = line.replace(m.group(0), "", 1)
                ch["paren"] += 1
        for pat, repl in SUBS:
            def rep(m):
                ctx = line[max(0, m.start() - 22):m.end() + 22]
                if protected(ctx):
                    return m.group(0)
                ch["sub"] += 1
                return m.expand(repl)
            line = pat.sub(rep, line)
        m = RE_HEAD.match(line)
        if m and re.search(r'[\u4e00-\u9fff]', line[m.end():m.end() + 6]):
            if not protected(line[:m.end() + 22]):
                line = "此前" + line[m.end():].lstrip()
                ch["sub"] += 1
        # 注释导航行
        if RE_CMT_NAV.match(line):
            ch["cmt"] += 1
            continue
        # 轻清理（不动缩进）
        line = re.sub(r'（\s*）', '', line)
        line = re.sub(r'，\s*。', '。', line)
        line = re.sub(r'(前述|此前) (?=[\u4e00-\u9fff])', r'\1', line)
        out.append(line)
    return "\n".join(out), ch

def main():
    tot = {"sub": 0, "paren": 0, "cmt": 0, "mermaid": 0, "tree": 0, "files": 0}
    log = []
    for course in sorted(os.listdir(TARGET)):
        cd = os.path.join(TARGET, course)
        if not os.path.isdir(cd) or course == "code" or course in INTERVIEW:
            continue
        for fn in sorted(os.listdir(cd)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            fp = os.path.join(cd, fn)
            data = open(fp, encoding="utf-8").read()
            fm, body = split_front_matter(data)
            new_body, ch = transform(body)
            new = fm + new_body
            if new != data:
                tot["files"] += 1
                if RUN:
                    open(fp, "w", encoding="utf-8").write(new)
                for k in ch:
                    tot[k] += ch[k]
                log.append((course, fn, ch, data, new))
    print(f"MODE: {'RUN' if RUN else 'DRY'}  TOTAL: {tot}")
    shown = 0
    total_lines = 0
    for course, fn, ch, old, new in log:
        for lo, ln in zip(old.split("\n"), new.split("\n")):
            if lo != ln:
                total_lines += 1
                if shown < 85:
                    print(f"[{course}/{fn[:22]}]")
                    print(f"   - {lo.strip()[:116]}")
                    print(f"   + {ln.strip()[:116]}")
                    shown += 1
    print("改动行总数:", total_lines)

if __name__ == "__main__":
    main()
