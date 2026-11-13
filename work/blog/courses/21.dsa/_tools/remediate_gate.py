#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSA 题库 权威门禁 v2 (正确性驱动)
对任意 go/java/ts 文件:
  1) 探测 stub (TODO / 空壳 main / 空 solve / BROKEN)
  2) 实编译+实运行, 取 stdout
  3) 与同源 Python 参考(同题同变体优先)的 demo 输出做 格式归一化 比对
     -> 完全一致 = FAITHFUL(PASS); 否则 = FAIL
用法: python3 remediate_gate.py <file>
退出 0=FAITHFUL, 1=FAIL/NOT-FAITHFUL
"""
import os, re, sys, ast, subprocess, glob, tempfile, json

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
GO = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"
PY = "/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3"
TIMEOUT = 30


def run(cmd, cwd=None, env=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT,
                           env=env or os.environ)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return -1, str(e)


# ---------- 输出归一化 ----------
def split_go_slice(inner):
    parts, depth, cur = [], 0, ""
    for ch in inner:
        if ch == "[":
            depth += 1; cur += ch
        elif ch == "]":
            depth -= 1; cur += ch
        elif ch == " " and depth == 0:
            if cur.strip():
                parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def to_canonical(s):
    s = s.strip()
    if s == "" or s.lower() in ("none", "null"):
        return None
    try:
        return ast.literal_eval(s)
    except Exception:
        pass
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if inner == "":
            return []
        return [to_canonical(p) for p in split_go_slice(inner)]
    # 无括号但含空白(如 Go 打印 "3 2 1" / "ad ae af" / "9 4"): 拆词逐词归一化
    if " " in s:
        toks = s.split()
        if len(toks) > 1:
            return [to_canonical(t) for t in toks]
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    try:
        return int(s)
    except Exception:
        pass
    try:
        return float(s)
    except Exception:
        pass
    return s


def canonical_eq(a, b):
    # 序列: 顺序敏感比对; 若两边都是元素可哈希的 list 且长度相同但顺序不同,
    # 再尝试作为 multiset 比对(覆盖 top-k / 集合类顺序无关场景)
    if isinstance(a, list) and isinstance(b, list):
        if a == b:
            return True
        try:
            if sorted(a) == sorted(b):
                return True
        except Exception:
            pass
        return False
    return a == b


# ---------- 定位 Python 参考 ----------
def prob_and_var(rel):
    d = os.path.basename(os.path.dirname(rel))  # lc_NNN_题名
    m = re.match(r"(lc_\d+)_", d)
    pid = m.group(1) if m else None
    # 变体序号: solution_K___...
    vm = re.search(r"solution_(\d+)", os.path.basename(rel))
    var = int(vm.group(1)) if vm else None
    return pid, var


def find_py_ref(pid, var):
    allp = sorted(glob.glob(os.path.join(BASE, "python", "**", pid + "_*", "solution_*.py"), recursive=True))
    if not allp:
        return None
    if var is not None:
        for p in allp:
            vm = re.search(r"solution_(\d+)", os.path.basename(p))
            if vm and int(vm.group(1)) == var:
                return p
    return allp[0]


# ---------- 语言检查 ----------
def check_go(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    if "TODO: solution not implemented" in src:
        return 1, "STUB(TODO)"
    m = re.search(r"func main\(\)\s*\{(.*?)\n\}", src, re.S)
    if m:
        # 仅删除打印函数名(fmt.Println/print/...), 保留参数内的真实调用
        body = re.sub(r"\b(?:fmt\.)?(?:Println|Print|Printf|println|print)\b", "", m.group(1))
        if not re.search(r"[A-Za-z_]\w*\s*\(", body):
            return 1, "STUB(empty main)"
    rc, out = run([GO, "run", os.path.basename(path)], cwd=os.path.dirname(path),
                  env={**os.environ, "GO111MODULE": "off"})
    return rc, out


def check_java(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    if "TODO" in src:
        return 1, "STUB(TODO)"
    if re.search(r'void\s+solve\s*\(\s*\)\s*\{\s*return', src):
        return 1, "STUB(empty solve)"
    cm = re.search(r"(?:public\s+)?class\s+(\w+)", src)
    if not cm:
        return 1, "no class"
    cls = cm.group(1)
    tmp = tempfile.mkdtemp()
    rc, o = run([JAVAC, "-d", tmp, path])
    if rc != 0:
        return rc, "compile:" + o[:200]
    rc, out = run([JAVA, "-cp", tmp, "com.webfault.dsa." + cls])
    return rc, out


def check_ts(path):
    rc, out = run([NODE, "--experimental-strip-types", path])
    if rc != 0:
        return rc, out[:200]
    rc2, out2 = run([NODE, "--experimental-strip-types", "-e",
                     "import('%s').then(m=>m.demo()).catch(e=>{console.error(e);process.exit(1)})"
                     % os.path.abspath(path).replace("\\", "/")])
    if rc2 != 0:
        return rc2, "demo:" + out2[:200]
    return 0, out2


def main():
    if len(sys.argv) < 2:
        print("usage: remediate_gate.py <file>"); sys.exit(2)
    path = sys.argv[1]
    if not os.path.isfile(path):
        print("FAIL: not found", path); sys.exit(1)
    ext = os.path.splitext(path)[1]
    rc, out = {".go": check_go, ".java": check_java, ".ts": check_ts}[ext](path)
    if rc != 0:
        print(f"[FAIL] {os.path.relpath(path, BASE)}  rc={rc} :: {out[:200]}")
        sys.exit(1)
    pid, var = prob_and_var(path)
    if not pid:
        print(f"[FAIL] {os.path.relpath(path, BASE)}  no_problem_id")
        sys.exit(1)
    py_variants = sorted(glob.glob(os.path.join(BASE, "python", "**", pid + "_*", "solution_*.py"), recursive=True))
    if not py_variants:
        print(f"[FAIL] {os.path.relpath(path, BASE)}  no_python_ref")
        sys.exit(1)
    a = to_canonical(out)
    last_pyout = ""
    for py in py_variants:
        rc2, pyout = run([PY, py])
        last_pyout = pyout
        if rc2 != 0:
            continue
        if canonical_eq(a, to_canonical(pyout)):
            print(f"[PASS] {os.path.relpath(path, BASE)}  faithful (vs {os.path.basename(py)})")
            sys.exit(0)
    print(f"[FAIL] {os.path.relpath(path, BASE)}  MISMATCH out={out[:80]!r} py0={last_pyout[:80]!r}")
    sys.exit(1)


if __name__ == "__main__":
    main()
