#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSDN 独立发表改造 · 第一轮（机械层，v3）
========================================
目标（两条硬约束）：
  R1 每篇文章不引用其他文章（面试题相关除外：py-interview / campus）
  R2 每篇博客有可见序号，由浅入深，顺序推进

处理内容（仅机械可判定部分）：
  A. 可见序号落到 title/H1：  "# 标题" -> "# N. 标题"；front-matter title 同步
     - 旧章号前缀（第X章/第X节/12-3 ）先清洗
     - front-matter 课程的正文 H1 同步加序号；步骤型 H1（"# 1) xxx"）跳过
     - py-interview: H1 "# 400 X" -> "# 100 X"（对齐文件名序号，-300）
  B. 删除纯导航行（页脚/进入下一章/下一步进入）；ops 提示行只剥链接不删行
  C. 剥死链语法：
     C1 动词+链接整体删除（按/参见/见/回到/进入 [..](x.md)）
     C2 句级删除（进入/回到/详见 [..](x.md)[^。]*。）
     C3 裸链接 [text](x.md) -> text；全角（x.md）-> 删除
  D. 删除跨卡短横指针（仅非面试课）：
     整括号引用/见族带尾删除/第N-M节章族/是第N-M/动词族(在·复用·同·对应·叠加在·回到)
     保护：见 2.1（同卡小节）、第 5.3 节（课件）、得到 1-33、70-80%、第 1-2 步
  E. py-interview 卡内互引重编号（见 409 -> 见 109）：
     仅三类上下文：见族直引 / 「下一题」行 / 已在·系列·与…同源·配套主卡
     保护：512G、PEP 484、HTTP 状态码(301/302/400/404/500)、rwx=421
     附：把 "467-xxx.md"/"467.deep.md" 旧文件名引用换成真实新文件名
  验证保护名单：12_type-hints(484) 120_builder(512) 147_permission(421)
               174_http-status(301/302/304/400/401/403/404/405/500) 不得变动

用法： dry（默认）/ run / verify
  python3 ai/scripts/number_and_strip_refs.py dry
  python3 ai/scripts/number_and_strip_refs.py run    # 先自动备份再执行
  python3 ai/scripts/number_and_strip_refs.py verify
"""
import os, re, sys, tarfile, datetime

ROOT = "/Users/Wang/Code/github/web-x-blog/work"
TARGET = os.path.join(ROOT, "target")
PYI = os.path.join(ROOT, "py-interview", "target")
BACKUP_DIR = "/Users/Wang/Code/github/web-x-blog/ai/backups"

MODE = sys.argv[1] if len(sys.argv) > 1 else "dry"
RUN = (MODE == "run")

INTERVIEW = {"py-interview", "campus"}
CN = "一二三四五六七八九十百千"

# ---------------------------------------------------------------- utils
def split_front_matter(data):
    if data.startswith("---\n"):
        end = data.find("\n---\n", 4)
        if end != -1:
            return data[:end + 5], data[end + 5:]
    return "", data

def first_h1_outside_fences(body):
    infence = False
    for i, l in enumerate(body.split("\n")):
        if l.strip().startswith("```"):
            infence = not infence
            continue
        if not infence and l.startswith("# "):
            return i, l
    return None, None

def clean_title_prefix(t):
    t = t.strip()
    t = re.sub(r'^第\s*[0-9' + CN + r']+\s*[章节]\s*', '', t)
    t = re.sub(r'^\d{1,3}(?:[-.]\d{1,2})?\s+(?=[A-Za-z\u4e00-\u9fff])', '', t)
    t = re.sub(r'^\d{1,3}\.\s+', '', t)
    return t.strip()

def serial_of(fn):
    m = re.match(r'(\d+)_', fn)
    return int(m.group(1)) if m else None

def course_dirs():
    dirs = []
    for d in sorted(os.listdir(TARGET)):
        p = os.path.join(TARGET, d)
        if os.path.isdir(p) and d != "code":
            dirs.append((d, p))
    dirs.append(("py-interview", PYI))
    return dirs

# ---------------------------------------------------------------- B
NAV_LABEL_LINE = re.compile(r'^\s*>\s*\*\*(下一章|下一节|下一步|上一章|上一节|上一篇|前一节|章节收尾|章节串联)\*\*')
INLINE_NAV = re.compile(r'^\*\*(下一步|下一节|下一章)\*\*：进入')
NEXT_SAYS = re.compile(r'^\s*下一[节章]讲')
OPS_KEEP = re.compile(r'^\s*>\s*\*\*(国内网络提示|替代路径|生产对接|附)')
NAV_KW = re.compile(r'(下一章|下一节|下一步|上一章|上一节|下一篇|前一节|章节收尾|章节串联)')
STEP_H1 = re.compile(r'^#\s*\d+[).、]')

# ---------------------------------------------------------------- C
C_VERB_LINK = re.compile(r'(?:按|参见?|详见|见|回到|进入)\s*\[[^\]]*\]\((?!http)[^)]*\.md\)')
C_SENT_LINK = re.compile(r'(?:进入|回到|详见)\s*\[[^\]]*\]\((?!http)[^)]*\.md\)[^。\n]*。?')
LINK_BARE = re.compile(r'\[([^\]]*)\]\((?!http)[^)]*\.md\)')
FW_LINK = re.compile(r'（\s*[^（）]*\.md\s*）')

# ---------------------------------------------------------------- D（非面试课）
DASH = r'\d{1,3}-\d{1,2}'
D_WHOLE_PAREN = re.compile(
    r'（\s*(?:[^（），,。；]{0,5})?'
    r'(?:第\s*' + DASH + r'\s*[节章]?|(?:详见|参见|另见|见|同|复用|对应|标注|在)\s*' + DASH + r')'
    r'(?:\s*卡片)?(?:\s*/\s*' + DASH + r'|\s*[、,]\s*' + DASH + r')*'
    r'(?:\s*的)?(?:\s*[^\s。，；）]{1,10}){0,2}\s*）')
D_SEE_TAIL = re.compile(
    r'[，,]?\s*(?:详见|参见|另见|见)\s*' + DASH +
    r'(?:\s*卡片)?(?:\s*的)?(?:\s*[、,]\s*' + DASH + r')*'
    r'(?:\s+[^\s。，；）]{1,10}){0,2}')
D_ISHI = re.compile(r'是第\s*' + DASH + r'\s*[，,。]?\s*')
D_CHAPTER = re.compile(
    r'(?:本系列)?第\s*' + DASH + r'(?![.\d%])(?!\s*步)(?:\s*[节章])?(?:\s*讲的?)?\s*')
D_VERB = re.compile(
    r'(?:在|复用|同|对应|叠加在|标注为?|由|回到第?)\s*' + DASH +
    r'(?:\s*/\s*' + DASH + r')*\s*(?:(?:的|中|里)\s*(?:[^\s。，；）]{1,4})?)?\s*')

# ---------------------------------------------------------------- E（py-interview）
PY_TOKEN = re.compile(r'(?<!\d)(3\d{2}|4\d{2}|5\d{2})(?!\d)(?![GMK%])')
PY_SEE = re.compile(r'(详见|参见|另见|见)\s*$')
PY_HAS = re.compile(r'(已在|系列)\s*$')
PROTECT_PRE = re.compile(r'(PEP\s*|rwx[=/]?|HTTP|状态码)\s*$')
PY_FILEREF = re.compile(r'(?<!\d)(\d{1,3})((?:-[a-z0-9-]+)?\.(?:deep\.)?md)\b')

def renumber_py_line(line):
    cnt = 0
    def core(m):
        n = int(m.group(1))
        if not (301 <= n <= 535):
            return m.group(1)
        pre = line[:m.start()]
        if PROTECT_PRE.search(pre[-8:]):
            return m.group(1)
        return str(n - 300)
    if "下一题" in line:
        def rep_nextq(m):
            nonlocal cnt
            n = int(m.group(1))
            if not (301 <= n <= 535):
                return m.group(1)
            pre = line[:m.start()]
            if PROTECT_PRE.search(pre[-8:]):
                return m.group(1)
            cnt += 1
            return str(n - 300)
        return PY_TOKEN.sub(rep_nextq, line), cnt
    def rep_ctx(m):
        n = int(m.group(1))
        if not (301 <= n <= 535):
            return m.group(1)
        pre = line[:m.start()]
        post = line[m.end():m.end() + 2]
        if PROTECT_PRE.search(pre[-8:]):
            return m.group(1)
        if PY_SEE.search(pre[-6:]) or PY_HAS.search(pre[-6:]):
            return str(n - 300)
        if "同源" in line and re.search(r'与\s*$', pre[-4:]):
            return str(n - 300)
        if "配套主卡" in line and post[:1] in ("-", "."):
            return str(n - 300)
        return m.group(1)
    return PY_TOKEN.sub(rep_ctx, line), cnt

# ---------------------------------------------------------------- transform
def cleanup_outside_fences(body):
    """标点/空白清理只作用于代码围栏之外，围栏内（mermaid/yaml/tree）原样保留"""
    out, infence = [], False
    for l in body.split("\n"):
        if l.strip().startswith("```"):
            infence = not infence
            out.append(l)
            continue
        if infence:
            out.append(l)
            continue
        l = re.sub(r'（\s*）', '', l)
        l = re.sub(r'  +', ' ', l)
        l = re.sub(r'([，,])\1+', r'\1', l)
        l = re.sub(r'。\s*。', '。', l)
        l = re.sub(r'，\s*([。；])', r'\1', l)
        l = re.sub(r'：\s*——\s*', '：', l)
        l = re.sub(r'([，,；;])\s+', r'\1', l)
        out.append(l)
    return "\n".join(out)

def transform(course, fn, data, serialmap=None):
    ch = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    fm, body = split_front_matter(data)
    is_interview = course in INTERVIEW
    n = serial_of(fn)

    # ---- A ----
    if fm:
        mt = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.M)
        if mt:
            old_t = mt.group(1).strip()
            new_t = clean_title_prefix(old_t)
            if not re.match(r'^\d{1,3}\.\s', new_t):
                new_t = f"{n}. {new_t}"
            if new_t != old_t:
                fm = fm[:mt.start()] + f'title: "{new_t}"\n' + fm[mt.end() + 1:]
                ch["A"] += 1
        idx, h1 = first_h1_outside_fences(body)
        if idx is not None and not STEP_H1.match(h1):
            new_h1 = f"# {n}. {clean_title_prefix(h1[2:])}"
            if new_h1 != h1:
                lines = body.split("\n")
                lines[idx] = new_h1
                body = "\n".join(lines)
                ch["A"] += 1
    else:
        idx, h1 = first_h1_outside_fences(body)
        if idx is not None:
            h1text = h1[2:]
            if course == "py-interview":
                m = re.match(r'^(\d{1,3})\s+(.*)$', h1text)
                if m and 301 <= int(m.group(1)) <= 535:
                    new_h1 = f"# {n}. {m.group(2)}"
                else:
                    new_h1 = f"# {n}. {clean_title_prefix(h1text)}"
            else:
                new_h1 = f"# {n}. {clean_title_prefix(h1text)}"
            if new_h1 != h1 and not STEP_H1.match(h1):
                lines = body.split("\n")
                lines[idx] = new_h1
                body = "\n".join(lines)
                ch["A"] += 1

    # ---- B ----
    out, bcnt = [], 0
    for l in body.split("\n"):
        if NAV_LABEL_LINE.match(l) or INLINE_NAV.match(l) or NEXT_SAYS.match(l):
            bcnt += 1
            continue
        if OPS_KEEP.match(l):
            out.append(l)
            continue
        if l.lstrip().startswith(">") and NAV_KW.search(l):
            i = NAV_KW.search(l).start()
            p = l[:i].rstrip().rstrip("，, ")
            if not p.endswith(("。", "；")):
                p += "。"
            out.append(p)
            bcnt += 1
            continue
        out.append(l)
    body = "\n".join(out)
    ch["B"] = bcnt

    # ---- C ----
    ccnt = 0
    body, n1 = C_VERB_LINK.subn("", body); ccnt += n1
    body, n2 = C_SENT_LINK.subn("", body); ccnt += n2
    body, n3 = FW_LINK.subn("", body); ccnt += n3
    body, n4 = LINK_BARE.subn(lambda m: m.group(1), body); ccnt += n4
    ch["C"] = ccnt

    # ---- D（非面试课）----
    dcnt = 0
    if not is_interview:
        for pat in (D_WHOLE_PAREN, D_SEE_TAIL, D_ISHI, D_CHAPTER, D_VERB):
            body, nn = pat.subn("", body)
            dcnt += nn
        body = cleanup_outside_fences(body)
        ch["D"] = dcnt

    # ---- E ----
    if course == "py-interview":
        lines, ecnt, infence = [], 0, False
        for l in body.split("\n"):
            if l.strip().startswith("```"):
                infence = not infence
                lines.append(l)
                continue
            if infence or l.startswith("# "):
                lines.append(l)
                continue
            nl, c = renumber_py_line(l)
            ecnt += c
            lines.append(nl)
        body = "\n".join(lines)
        if serialmap:
            def fix_ref(m):
                num = int(m.group(1))
                rest = m.group(2)
                target = serialmap.get(num)
                if not target:
                    return m.group(0)
                if ".deep.md" in rest and not target.endswith(".deep.md"):
                    cand = target[:-3] + ".deep.md"
                    target = cand if os.path.exists(os.path.join(PYI, cand)) else target
                return target
            body = PY_FILEREF.sub(fix_ref, body)
        ch["E"] = ecnt

    return fm + body, ch

# ---------------------------------------------------------------- modes
def backup():
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR, f"pass1-pre-{ts}.tar.gz")
    with tarfile.open(path, "w:gz") as tar:
        tar.add(TARGET, arcname="work/target")
        tar.add(PYI, arcname="work/py-interview/target")
    return path

def do_run():
    serialmap = {}
    for fn in sorted(os.listdir(PYI)):
        if fn.endswith(".md") and not fn.startswith("_"):
            s = serial_of(fn)
            if s:
                serialmap[s] = fn
    report = {}
    for course, cdir in course_dirs():
        agg = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "files": 0}
        for fn in sorted(os.listdir(cdir)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            if serial_of(fn) is None:
                continue
            fp = os.path.join(cdir, fn)
            data = open(fp, encoding="utf-8").read()
            new, ch = transform(course, fn, data, serialmap if course == "py-interview" else None)
            if new != data:
                agg["files"] += 1
                if RUN:
                    with open(fp, "w", encoding="utf-8") as fh:
                        fh.write(new)
            for k in ("A", "B", "C", "D", "E"):
                agg[k] += ch[k]
        report[course] = agg
    return report

def do_verify():
    problems = []
    stats = {"cards": 0, "titlefield_num": 0, "h1num": 0, "mdlink": 0,
             "fwlink": 0, "navfoot": 0, "dash": 0, "pyh1": 0}
    for course, cdir in course_dirs():
        for fn in sorted(os.listdir(cdir)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            n = serial_of(fn)
            if n is None:
                continue
            stats["cards"] += 1
            fp = os.path.join(cdir, fn)
            data = open(fp, encoding="utf-8").read()
            fm, body = split_front_matter(data)
            if fm:
                mt = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.M)
                if mt and re.match(r'^\d{1,3}\.\s', mt.group(1)):
                    stats["titlefield_num"] += 1
                else:
                    problems.append(f"[title无序号] {course}/{fn}")
            idx, h1 = first_h1_outside_fences(body)
            has_h1_num = h1 and (re.match(r'^#\s*\d{1,3}\.\s', h1) or STEP_H1.match(h1))
            if has_h1_num:
                stats["h1num"] += 1
            elif not fm:
                problems.append(f"[H1无序号] {course}/{fn}")
            stats["mdlink"] += len(re.findall(r'\]\([^)]*\.md\)', data))
            stats["fwlink"] += len(re.findall(r'（[^（）]*\.md）', data))
            stats["navfoot"] += len([l for l in data.split("\n")
                                     if NAV_LABEL_LINE.match(l)])
            if course not in INTERVIEW:
                for m in re.finditer(DASH, data):
                    ln = data[:m.start()].count("\n")
                    line = data.split("\n")[ln]
                    ctx = line[max(0, m.start() - 6):m.end() + 6]
                    if re.search(r'(得到|例如|\d+年|\d+月|~|—|—)', ctx):
                        continue
                    stats["dash"] += 1
                    if stats["dash"] <= 12:
                        problems.append(f"[残留短横] {course}/{fn}: {ctx.strip()}")
            if course == "py-interview":
                if h1 and re.match(r'^#\s*(\d{1,3})\.', h1):
                    if int(re.match(r'^#\s*(\d{1,3})\.', h1).group(1)) == n:
                        stats["pyh1"] += 1
                    else:
                        problems.append(f"[py H1序号≠文件名] {fn} H1={h1[:24]} N={n}")
                for m in re.finditer(r'(?:详见|参见|另见|见)\s*(\d{1,3})\b', body):
                    ref = int(m.group(1))
                    if not os.path.exists(os.path.join(cdir, f"{ref}_")):
                        problems.append(f"[py 死互引] {fn}: 见 {ref} 无对应卡")
    PROTECT = {
        "12_type-hints-annotation.md": ["484"],
        "120_builder-pattern.md": ["512"],
        "147_file-permission-commands.md": ["421"],
        "174_http-status-codes.md": ["301", "302", "304", "400", "401", "403", "404", "405", "500"],
    }
    for fn, toks in PROTECT.items():
        fp = os.path.join(PYI, fn)
        if not os.path.exists(fp):
            problems.append(f"[保护名单缺文件] {fn}")
            continue
        data = open(fp, encoding="utf-8").read()
        for t in toks:
            if t not in data:
                problems.append(f"[保护名单被误改] {fn} 数字 {t} 丢失")
    return stats, problems

# ---------------------------------------------------------------- main
if MODE == "verify":
    stats, problems = do_verify()
    print("== VERIFY ==")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  problems: {len(problems)}")
    for p in problems[:40]:
        print("   ", p)
    sys.exit(0)

if RUN:
    bp = backup()
    print("backup ->", bp)

report = do_run()
print(f"MODE: {MODE}")
print(f"{'course':13}{'A':>5}{'B':>5}{'C':>5}{'D':>5}{'E':>5}{'files':>7}")
tot = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "files": 0}
for c in sorted(report):
    a = report[c]
    print(f"{c:13}{a['A']:>5}{a['B']:>5}{a['C']:>5}{a['D']:>5}{a['E']:>5}{a['files']:>7}")
    for k in tot:
        tot[k] += a[k]
print("TOTAL:", tot)
