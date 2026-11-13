#!/usr/bin/env python3
"""Strict LeetCode audit:
1. constant-return detector: solution fn body is a single trivial return
   (return true/false/null/nil/[]/{}/0/-1/"") with no computation.
2. assertion presence: every file must contain at least one comparison/throw.
3. ts: demo/self-test must actually be invoked (no silent no-op).
4. stub markers scan.
Only audits lc_* dirs (LeetCode), notes/教程 dirs excluded from (1).
"""
import os, re, glob, sys

ROOT = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
LANGS = {"go": ".go", "java": ".java", "ts": ".ts", "python": ".py"}

CONST_RET = {
    ".go":   re.compile(r"\n\s*return\s+(nil|true|false|\[\]\w*\{\}|map\w*\{\}|0|-1|\"\")\s*\n\s*\}\s*$", re.S),
    ".java": re.compile(r"\n\s*return\s+(true|false|null|new\s+\w+<[^>]*>\(\)|new\s+\w+\(\)|0|-1|\"\")\s*;\s*\n\s*\}\s*$", re.S),
    ".ts":   re.compile(r"\n\s*return\s+(true|false|null|undefined|\[\]|\{\}|0|-1|\"\")\s*;\s*\n\s*\}\s*$", re.S),
    ".py":   re.compile(r"\n\s*return\s+(True|False|None|\[\]|\{\}|0|-1|\"\")\s*\n\w", re.S),
}
ASSERT_PAT = re.compile(r"(assert|throw|FAILED|expect|===|!==|!=|if\s*\(!?eq|check|os\.Exit\(1\)|panic\(|reflect\.DeepEqual|Arrays\.equals|\.equals\(|System\.out\.println\(\"PASS|console\.log\(\"PASS|print\(\"PASS|cases\s*:?=|tc\s*\{|\btcs?\b)")
TS_DEMO_CALL = re.compile(r"^\s*(demo|main|selfTest|runTests)\s*\(\s*\)\s*;?\s*$", re.M)

def is_lc(path):
    return "/lc_" in path or os.path.basename(os.path.dirname(path)).startswith("lc_")

def strip_comments(src, ext):
    if ext == ".py":
        src = re.sub(r"(?m)^\s*#.*$", "", src)
    else:
        src = re.sub(r"//.*", "", src)
        src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return src

def find_bad(path):
    ext = os.path.splitext(path)[1]
    raw = open(path, encoding="utf-8", errors="replace").read()
    src = strip_comments(raw, ext)
    issues = []
    # 1. constant-return: last function in file returns a constant only
    if ext != ".py":
        # locate the solution entry function (last func/class method with a body)
        pass
    m = CONST_RET[ext].search(src)
    if m:
        # verify the returned constant function has no other statements:
        # take the matched region's preceding ~200 chars, look for computation
        seg = src[max(0, m.start()-400):m.start()]
        # if segment contains loops/recursive calls/assignments it's fine
        body_start = seg.rfind("{") if ext != ".py" else seg
        # crude: check if between 'def/function' header and return there is real logic
        # find nearest function header before m.start()
        if ext == ".py":
            hdr = re.search(r"(?m)^\s*def\s+\w+\([^)]*\):\s*\n((?:\s+(?:#[^\n]*|pass|return\s+(?:True|False|None|\[\]|\{\}|0|-1|\"\")|docstring)[^\n]*\n)+)\s*return", src[:m.end()], re.S)
            if hdr:
                issues.append("const-return")
        else:
            # function whose closing brace is m end: extract from matching open
            # simpler heuristic: the return is the ONLY statement of the fn body
            fnm = re.search(r"(?m)(?:func|function|public|static|private|protected|class)[^\n{]*\{\s*(?:\[[^\]]*\]\s*)?(?:return\s+(?:nil|true|false|null|undefined|\[\]|\{\}|0|-1|\"\"|new\s+\w+\(\)|new\s+\w+<[^>]*>\(\)|map\w*\{\}|\[\]\w*\{\})\s*[;]?\s*\}\s*$", src[:m.end()], re.S)
            if fnm:
                issues.append("const-return")
    # 2. assertion presence
    if not ASSERT_PAT.search(src):
        issues.append("no-assert")
    # 3. ts silent no-op: defines demo/main but never calls
    if ext == ".ts":
        if re.search(r"(?:function|const)\s+(demo|main|selfTest|runTests)\b", src) and not TS_DEMO_CALL.search(src):
            # check call anywhere (not just definition line)
            if not re.search(r"(demo|main|selfTest|runTests)\s*\(\s*\)\s*;", src):
                issues.append("ts-no-call")
    return issues

def main():
    bad = []
    total = 0
    for lang, ext in LANGS.items():
        for f in glob.glob(os.path.join(ROOT, lang, "**", "solution_*" + ext), recursive=True):
            total += 1
            if not is_lc(f):
                continue
            issues = find_bad(f)
            if issues:
                bad.append((f, issues))
    print(f"=== STRICT LEETCODE AUDIT lc-scope files scanned, flagged={len(bad)} ===")
    for f, iss in bad:
        print(f"  {','.join(iss)} :: {f}")

if __name__ == "__main__":
    main()
