#!/usr/bin/env python3
"""Strict LeetCode audit v2 — structural checks beyond runtime PASS:
  A. empty test-case array (vacuous PASS)
  B. entry/harness-called function body is a bare constant return (stub)
  C. ts harness defined but never invoked (silent no-op)
  D. duplicate top-level declarations (shadowing)
Brace-matching based, no monster regex.
"""
import os, re, glob

ROOT = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
LANGS = {"go": ".go", "java": ".java", "ts": ".ts", "python": ".py"}
CONSTS = {"true", "false", "nil", "null", "undefined", "none", "true", "false",
          "[]", "{}", "0", "-1", '""', "''", "new arraylist()", "new arraylist<>()",
          "new hashmap()", "new hashmap<>()", "new linkedlist<>()", "map[string]int{}",
          "[]int{}", "[]string{}", "list<integer>[]", "list<integer>()"}

def strip_comments(src, ext):
    if ext == ".py":
        src = re.sub(r"(?m)^\s*#.*$", "", src)
    else:
        src = re.sub(r"//.*", "", src)
        src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return src

def match_brace(src, open_idx):
    """Return index of matching close brace, or -1."""
    depth = 0
    i = open_idx
    in_str = None
    while i < len(src):
        ch = src[i]
        if in_str:
            if ch == "\\":
                i += 2; continue
            if ch == in_str: in_str = None
        elif ch in "\"'":
            in_str = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1

def body_is_bare_const(body):
    b = body.strip()
    b = re.sub(r"\breturn\b", "", b, count=1).strip()
    b = b.rstrip(";").strip()
    b = re.sub(r"\(\s*\)", "", b)          # ()
    b = re.sub(r"<[^<>]*>", "", b)         # generics
    b = re.sub(r"\{\s*\}", "", b)         # empty literal braces
    b = b.strip().lower()
    return b in CONSTS or b == ""

def find_stub_fns(src, ext):
    """Yield names of functions whose body is a bare constant return."""
    stubs = []
    if ext == ".py":
        for m in re.finditer(r"(?m)^def\s+(\w+)\([^)]*\):\s*\n", src):
            # python: check indented body lines
            start = m.end()
            body_lines = []
            for line in src[start:].split("\n"):
                if line.strip() == "" or line.startswith(("    ", "\t")):
                    if line.strip(): body_lines.append(line.strip())
                    continue
                break
            if len(body_lines) == 1 and body_lines[0].startswith("return"):
                val = body_lines[0][6:].strip().rstrip(";").lower()
                if val in CONSTS:
                    stubs.append(m.group(1))
        return stubs
    hdr_pat = {"go": r"(?m)^func\s+(?:\([^)]*\)\s+)?(\w+)[^\n{]*\{",
               "java": r"(?m)^\s*(?:public|private|protected|static|final|\s)+\w[\w<>\[\],\s]*\s(\w+)\s*\([^)]*\)\s*\{",
               "ts": r"(?m)^(?:export\s+)?(?:function|const)\s+(\w+)[^\n{=]*\{",
               }[ext.lstrip(".")]
    for m in re.finditer(hdr_pat, src):
        oi = src.find("{", m.end() - 1)
        if oi < 0: continue
        ci = match_brace(src, oi)
        if ci < 0: continue
        body = src[oi+1:ci]
        if body_is_bare_const(body):
            stubs.append(m.group(1))
    return stubs

EMPTY_CASES = {
    ".go":   re.compile(r"cases\s*:?=\s*\[\]\w*\{\s*\}", re.S),
    ".java": re.compile(r"cases\s*=\s*\{\s*\}", re.S),
    ".ts":   re.compile(r"cases\s*(:\w+)?\s*=\s*\[\s*\]", re.S),
    ".py":   re.compile(r"cases\s*=\s*\[\s*\]", re.S),
}
TS_HARNESS = re.compile(r"(?m)(?:function|const)\s+(demo|main|selfTest|runTests)\b")
TS_CALL = re.compile(r"(?m)^\s*(demo|main|selfTest|runTests)\s*\(\s*\)\s*;?\s*$")

def is_lc(p):
    return "/lc_" in p

def audit(path):
    ext = os.path.splitext(path)[1]
    raw = open(path, encoding="utf-8", errors="replace").read()
    src = strip_comments(raw, ext)
    issues = []
    m = EMPTY_CASES[ext].search(src)
    if m and re.search(r"(PASS|for|while|forEach)", src[m.end():m.end()+400]):
        issues.append("empty-cases")
    stubs = find_stub_fns(src, ext)
    # only flag stubs that the harness actually calls (self-test entry)
    called = set(re.findall(r"(?m)(?:got|res|result|ans|out)\s*=\s*(\w+)\(", src))
    real_stubs = [s for s in stubs if s in called]
    if real_stubs:
        issues.append("stub-entry:" + ",".join(sorted(set(real_stubs))))
    if ext == ".ts" and TS_HARNESS.search(src) and not TS_CALL.search(src):
        issues.append("ts-harness-never-called")
    if ext in (".go", ".ts", ".py"):
        decl_pat = {"go": r"(?m)^func\s+(?:\([^)]*\)\s+)?(\w+)",
                    "ts": r"(?m)^(?:export\s+)?(?:function|const|class)\s+(\w+)",
                    "py": r"(?m)^def\s+(\w+)"}[ext.lstrip(".")]
        names = re.findall(decl_pat, src)
        dup = sorted({n for n in names if names.count(n) > 1})
        if dup:
            issues.append("dup-decls:" + ",".join(dup))
    return issues

def main():
    flagged = []
    total = 0
    for lang, ext in LANGS.items():
        for f in glob.glob(os.path.join(ROOT, lang, "**", "solution_*" + ext), recursive=True):
            if not is_lc(f):
                continue
            total += 1
            iss = audit(f)
            if iss:
                flagged.append((f, iss))
    print(f"=== STRICT AUDIT v2 :: lc-scope files={total} flagged={len(flagged)} ===")
    for f, iss in flagged:
        print(f"  [{','.join(iss)}] {f}")

if __name__ == "__main__":
    main()
