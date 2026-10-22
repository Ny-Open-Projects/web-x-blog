#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pass-1d（收尾补丁）：pass-1c 后残留的 6 处真引用
  D1 SUBS 补充：与 N-M 暴露 / 沿用 N-M 的 / 来自 N-M 定义（apm/54）
  D2 括号尾巴放宽标点要求：（7-4 测试时老师专门停下来等下载）（mksz948/13）
  D3 围栏内注释行也清括号引用：<!-- ...（9-3）... -->（mksz948/18）
排除器补强：红球/蓝球/Intn/档位/固定区间（es/lottery 区间误报）
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
        r'\d+\.\d+-\d+', r'\d+-\d+[A-Za-z]', r'[0-9a-fA-F]{6,}-', r'\[\^?\\?[a-z0-9{(\[]',
        r'20\d\d-\d\d-\d\d', r'2006-01-02', r'15:04:05', r'T\d\d:\d\d:\d\d',
        r'得到|例如|比如|按区间|映射一|~|%', r'redis-\d+-\d+', r'Pod …-\d+-\d+',
        r'\d+-\d+\s*\|\s*v\d+', r'\|\s*\d+-\d+\s*\|', r'5-4-11-2', r'5-8-4-5',
        r'第\s*\d+-\d+\s*步', r'步骤\s*\d+-\d+', r'/课件|code/',
        r'原文锚点：第\d+章', r'fsid|clusterID|csi-vol-',
        r'本卡覆盖|合并原|按课程口径重构', r'`[^`]*`', r'\d+-\d+\.el',
        r'cut -c1-', r'0\.0\.0\.0', r'cron\(', r'"[^"]*\d+-\d+[^"]*"',
        r"'[^']*\d+-\d+[^']*'", r'1<<', r'<<', r'5-4=1', r'元/月', r'\$\d+-\d+',
        r'20-30 年', r'3-5 年|3-5 月|3-5 本', r'5-10 年', r'70-80', r'10-15',
        r'红球|蓝球|Intn|档位|固定区间|区间按钮|\d+-\d+\s*[/、]\s*\d',
    ]
]

def protected(ctx):
    return any(p.search(ctx) for p in PROTECT)

SUBS = [
    (re.compile(r'与\s*' + DASH + r'\s*暴露'), '与前述暴露'),
    (re.compile(r'沿用\s*' + DASH + r'\s*的'), '沿用前述的'),
    (re.compile(r'来自\s*' + DASH + r'\s*定义'), '来自前述定义'),
]
# 括号尾巴放宽：允许无标点直接接中文
RE_PAREN = re.compile(r'（\s*' + DASH + r'(?:\s*/\s*\d{1,2})?(?:\s*[^（）]{0,16})?\s*）')
RE_CMT_START = re.compile(r'^\s*(#|//|<!--)')
RE_HAS_CMT = re.compile(r'#|//|<!--')
RE_URL = re.compile(r'https?://')

def split_front_matter(data):
    if data.startswith("---\n"):
        end = data.find("\n---\n", 4)
        if end != -1:
            return data[:end + 5], data[end + 5:]
    return "", data

def transform(body):
    ch = {"sub": 0, "paren": 0}
    out, infence = [], False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            infence = not infence
            out.append(line)
            continue
        # R—— 围栏内的行内注释（yaml # 注释 / go // 注释 / html 注释）也清（D3）
        in_comment = (RE_CMT_START.match(line) or (infence and RE_HAS_CMT.search(line) and not RE_URL.search(line)))
        if infence and not in_comment:
            out.append(line)
            continue
        # 括号引用
        for m in list(RE_PAREN.finditer(line)):
            ctx = line[max(0, m.start() - 22):m.end() + 22]
            if not protected(ctx):
                line = line.replace(m.group(0), "", 1)
                ch["paren"] += 1
        # 动词族
        for pat, repl in SUBS:
            def rep(m):
                ctx = line[max(0, m.start() - 22):m.end() + 22]
                if protected(ctx):
                    return m.group(0)
                ch["sub"] += 1
                return m.expand(repl)
            line = pat.sub(rep, line)
        line = re.sub(r'（\s*）', '', line)
        out.append(line)
    return "\n".join(out), ch

def main():
    import difflib
    tot = {"sub": 0, "paren": 0, "files": 0}
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
                tot["sub"] += ch["sub"]; tot["paren"] += ch["paren"]
                print(f"MODE: {'RUN' if RUN else 'DRY'}  TOTAL: {tot}")
                for x in difflib.unified_diff(data.split("\n"), new.split("\n"), lineterm="", n=0):
                    if x.startswith(("+", "-")) and not x.startswith(("+++", "---")):
                        print("   " + x[0] + " " + x[1:].strip()[:112])
    print(f"MODE: {'RUN' if RUN else 'DRY'}  FINAL: {tot}")

if __name__ == "__main__":
    main()
