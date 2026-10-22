#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pass-1c（补丁层）：清 pass-1b 漏掉的真残留形态
================================================
通用（非面试课）：
  C1 括号引用扩展： （13-11/12） （8-5，核心坑） （10-2 实测） （8-8 节） （7-4 测试时...）
  C2 围栏内注释清理： #/ //  <!-- 注释里的旧节号与篇章导航（注释会随代码发布）
  C3 动词族补充： 再去 N-M 写 / 把 N-M 留下 / 与 N-M 暴露 / 沿用 N-M 的指标定义 /
                 与 N-M 定义 / 接 N-M 的 / （...详见下篇 N-M）
  C4 mksz952/40 专用： **7-23 优化五点** / ## 四、7-23 五点优化总结
  C5 围栏内路径树清编号： ```text 里的 "12-1  什么是 Service Mesh ← 当前"
  C6 排除器补强： cron( / 裸日期 / 字符串字面量
py-interview 专属（面试豁免删除，但互引必须指向真实卡）：
  P1 围栏内注释的卡号重编号：# ...（见 376） → （见 76）
  P2 正文/表格括号裸号 （378） → （78）
  P3 正文 复用/接/按 NNN → 减 300（行含 状态码/HTTP 跳过）

用法： dry / run
"""
import os, re, sys

ROOT = "/Users/Wang/Code/github/web-x-blog/work"
TARGET = os.path.join(ROOT, "target")
PYI = os.path.join(ROOT, "py-interview", "target")
RUN = (len(sys.argv) > 1 and sys.argv[1] == "run")
INTERVIEW = {"py-interview", "campus"}
DASH = r'\d{1,3}-\d{1,2}'

PROTECT = [
    re.compile(p) for p in [
        r'\d+\.\d+-\d+', r'\d+-\d+[A-Za-z]', r'[0-9a-fA-F]{6,}-',
        r'\[\^?\\?[a-z0-9{(\[]', r'date:\s*20\d\d-\d\d-\d\d', r'20\d\d-\d\d-\d\d',
        r'2006-01-02', r'15:04:05', r'T\d\d:\d\d:\d\d',
        r'得到|例如|比如|按区间|映射一|~|%|\d+年|\d+月|\d+天',
        r'redis-\d+-\d+', r'Pod …-\d+-\d+', r'\d+-\d+\s*\|\s*v\d+', r'\|\s*\d+-\d+\s*\|',
        r'5-4-11-2', r'5-8-4-5', r'第\s*\d+-\d+\s*步', r'步骤\s*\d+-\d+',
        r'/课件|code/', r'原文锚点：第\d+章',
        r'fsid|clusterID|csi-vol-', r'本卡覆盖|合并原|按课程口径重构',
        r'`[^`]*`', r'\d+-\d+\.el', r'cut -c1-', r'0\.0\.0\.0',
        r'cron\(', r'"[^"]*\d+-\d+[^"]*"', r"'[^']*\d+-\d+[^']*'", r'1<<', r'<<',
        r'5-4=1', r'元/月', r'\$\d+-\d+', r'20-30 年', r'3-5 年|3-5 月|3-5 本',
        r'5-10 年', r'70-80', r'10-15',
    ]
]

def protected(ctx):
    return any(p.search(ctx) for p in PROTECT)

# ---------- 通用清理 ----------
RE_PAREN_EXT = re.compile(
    r'（\s*' + DASH + r'(?:\s*/\s*\d{1,2})?' +
    r'(?:\s*[，,、][^（）]{0,14})?\s*）')
RE_CMT_NAV = re.compile(r'(?://|#)\s*见后续篇章[^\n]*$')
RE_PATHLINE = re.compile(
    r'^(\s*)\d{1,2}-\d{1,2}(?:\s*~\s*\d{1,2}-\d{1,2})?\s+(?=[\u4e00-\u9fffA-Za-z*])')
SUBS2 = [
    (re.compile(r'([先再])去\s*' + DASH + r'\s*(?=写)'), r'\1'),
    (re.compile(r'[、,]\s*' + DASH + r'\s*(?=写)'), '、'),
    (re.compile(r'把\s*' + DASH + r'\s*(?=留下)'), '把前述'),
    (re.compile(r'与\s*' + DASH + r'\s*暴露'), '与前述暴露'),
    (re.compile(r'沿用\s*' + DASH + r'\s*的指标定义'), '沿用前述的指标定义'),
    (re.compile(r'与\s*' + DASH + r'\s*定义'), '与前述定义'),
    (re.compile(r'接\s*' + DASH + r'\s*的'), '接前述的'),
    (re.compile(r'[（(]\s*[^（）)]{0,12}详见下篇\s*' + DASH + r'[^（）)]{0,6}[）)]'), ''),
    (re.compile(r'\*\*' + DASH + r' 优化五点\*\*'), '**前述五点优化**'),
    (re.compile(r'(## [一二三四五六七八九十]+、)' + DASH + r' 五点优化总结'), r'\1前述五点优化总结'),
]
RE_CMT_START = re.compile(r'^\s*(#|//|<!--)')

# ---------- py 专属 ----------
PY_TOKEN = re.compile(r'(?<!\d)(3\d{2}|4\d{2}|5\d{2})(?!\d)(?![GMK%])')
PY_SEE = re.compile(r'(详见|参见|另见|见)\s*$')
PY_HAS = re.compile(r'(已在|系列)\s*$')
PROTECT_PRE = re.compile(r'(PEP\s*|rwx[=/]?|HTTP|状态码|状态|码)\s*$')
PY_PAREN = re.compile(r'（(3\d{2}|4\d{2}|5\d{2})）')
PY_VERB = re.compile(r'(?:复用|接|按)\s*(3\d{2}|4\d{2}|5\d{2})(?!\d)(?![GMK%])')
PY_SKIP_LINE = re.compile(r'状态码|HTTP')

def py_renumber_line(line):
    def rep_ctx(m):
        n = int(m.group(1))
        if not (301 <= n <= 535):
            return m.group(1)
        pre = line[:m.start()]
        if PROTECT_PRE.search(pre[-8:]):
            return m.group(1)
        if PY_SEE.search(pre[-6:]) or PY_HAS.search(pre[-6:]):
            return str(n - 300)
        if re.search(r'(复用|接|按)\s*$', pre[-6:]):
            return str(n - 300)
        return m.group(1)
    def rep_paren(m):
        n = int(m.group(1))
        if not (301 <= n <= 535):
            return m.group(0)
        pre = line[:m.start()]
        if PROTECT_PRE.search(pre[-8:]):
            return m.group(0)
        return "（%d）" % (n - 300)
    line = PY_TOKEN.sub(rep_ctx, line)
    line = PY_PAREN.sub(rep_paren, line)
    return line

def transform_generic(body):
    ch = {"paren": 0, "cmt": 0, "path": 0, "sub": 0}
    out, infence = [], False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            infence = not infence
            out.append(line)
            continue
        stripped = line.strip()
        is_comment = (not infence) and bool(RE_CMT_START.match(line))
        # 注释导航整行删（围栏内外）
        if RE_CMT_NAV.search(line):
            ch["cmt"] += 1
            continue
        # 围栏内路径树
        if infence:
            for m in list(RE_PATHLINE.finditer(line)):
                ctx = line[:m.start()] + line[m.end():m.end() + 16]
                if not protected(ctx) and not re.search(r'20\d\d-', line):
                    line = RE_PATHLINE.sub(r'\1', line, count=1)
                    ch["path"] += 1
            out.append(line)
            continue
        # 括号引用扩展
        for m in list(RE_PAREN_EXT.finditer(line)):
            ctx = line[max(0, m.start() - 22):m.end() + 22]
            if not protected(ctx):
                line = line.replace(m.group(0), "", 1)
                ch["paren"] += 1
        # 动词族
        for pat, repl in SUBS2:
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

def transform_py(body):
    ch = {"py": 0}
    out, infence = [], False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            infence = not infence
            out.append(line)
            continue
        if infence:
            if RE_CMT_START.match(line):           # 围栏内注释：重编号
                before = line
                line = py_renumber_line(line)
                if line != before:
                    ch["py"] += 1
            out.append(line)
            continue
        if line.startswith("# "):
            out.append(line)
            continue
        if PY_SKIP_LINE.search(line):
            out.append(line)
            continue
        before = line
        line = py_renumber_line(line)
        if line != before:
            ch["py"] += 1
        out.append(line)
    return "\n".join(out), ch

def split_front_matter(data):
    if data.startswith("---\n"):
        end = data.find("\n---\n", 4)
        if end != -1:
            return data[:end + 5], data[end + 5:]
    return "", data

def main():
    import difflib
    tot = {"paren": 0, "cmt": 0, "path": 0, "sub": 0, "py": 0, "files": 0}
    log = []
    # 目标目录：target/* 各课 + py-interview/target
    dirs = []
    for course in sorted(os.listdir(TARGET)):
        cd = os.path.join(TARGET, course)
        if os.path.isdir(cd) and course != "code":
            dirs.append((course, cd))
    dirs.append(("py-interview", PYI))
    for course, cd in dirs:
        for fn in sorted(os.listdir(cd)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            fp = os.path.join(cd, fn)
            data = open(fp, encoding="utf-8").read()
            fm, body = split_front_matter(data)
            if course in INTERVIEW:
                new_body, ch = transform_py(body)
            else:
                new_body, ch = transform_generic(body)
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
        d = [x for x in difflib.unified_diff(old.split("\n"), new.split("\n"), lineterm="", n=0)
             if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]
        total_lines += len(d)
        i = 0
        while i < len(d) and shown < 80:
            if d[i].startswith("-"):
                print(f"[{course}/{fn[:22]}]")
                print(f"   - {d[i][1:].strip()[:114]}")
                if i + 1 < len(d) and d[i + 1].startswith("+"):
                    print(f"   + {d[i+1][1:].strip()[:114]}")
                    i += 1
            i += 1
            shown += 1
    print("改动行总数:", total_lines)

if __name__ == "__main__":
    main()
