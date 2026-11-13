#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSA 题库 remediation 门禁校验器
对任意一个 go/java/ts 文件，按语言实编译/实运行校验，输出 PASS/FAIL。
用法: python3 remediate_check.py <file>
退出码 0=PASS, 1=FAIL
"""
import os, re, sys, subprocess, tempfile

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
GO = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"
TIMEOUT = 30


def run(cmd, cwd=None, env_extra=None):
    env = {**os.environ}
    if env_extra:
        env.update(env_extra)
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT)
        return r.returncode, (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"
    except Exception as e:
        return -1, str(e)


def find_java_class(src):
    for line in src.splitlines():
        m = re.match(r'^(?:public\s+)?class\s+(\w+)', line)
        if m and (line.startswith('class') or line.startswith('public')):
            return m.group(1)
    return None


def check_go(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    if "TODO: solution not implemented" in src:
        return 1, "STUB (TODO placeholder)"
    # 空壳 main：main 体去掉打印后没有任何真实函数调用 -> 视为 stub
    m = re.search(r"func main\(\)\s*\{(.*?)\n\}", src, re.S)
    if m:
        # 仅删除打印函数名(fmt.Println/print/...), 保留参数内的真实调用
        body = re.sub(r"\b(?:fmt\.)?(?:Println|Print|Printf|println|print)\b", "", m.group(1))
        if not re.search(r"[A-Za-z_]\w*\s*\(", body):
            return 1, "STUB (empty main, no real call)"
    d = os.path.dirname(path)
    return run([GO, "run", os.path.basename(path)], cwd=d,
               env_extra={"GO111MODULE": "off"})


def check_java(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    if "TODO" in src:
        return 1, "STUB (TODO placeholder)"
    if re.search(r'void\s+solve\s*\(\s*\)\s*\{\s*return', src):
        return 1, "STUB (empty solve())"
    cls = find_java_class(src)
    if not cls:
        return 1, "no top-level class found"
    tmp = tempfile.mkdtemp()
    r1 = run([JAVAC, "-d", tmp, path])
    if r1[0] != 0:
        return r1[0], r1[1][:300]
    return run([JAVA, "-cp", tmp, "com.webfault.dsa." + cls])


def check_ts(path):
    rc, out = run([NODE, "--experimental-strip-types", path])
    if rc != 0:
        return rc, out[:300]
    # 真实正确性：import 并调用 demo()
    rc2, out2 = run([NODE, "--experimental-strip-types", "-e",
                     "import('%s').then(m=>m.demo()).catch(e=>{console.error(e);process.exit(1)})"
                     % os.path.abspath(path).replace("\\", "/")])
    if rc2 != 0:
        return rc2, ("demo-error: " + out2)[:300]
    return 0, out2[:200]


def main():
    if len(sys.argv) < 2:
        print("usage: remediate_check.py <file>")
        sys.exit(2)
    path = sys.argv[1]
    if not os.path.isfile(path):
        print("FAIL: file not found:", path)
        sys.exit(1)
    ext = os.path.splitext(path)[1]
    if ext == ".go":
        rc, out = check_go(path)
    elif ext == ".java":
        rc, out = check_java(path)
    elif ext == ".ts":
        rc, out = check_ts(path)
    else:
        print("FAIL: unsupported ext", ext)
        sys.exit(1)
    status = "PASS" if rc == 0 else "FAIL"
    print(f"[{status}] {os.path.relpath(path, BASE)}  rc={rc}")
    if rc != 0 or ext == ".ts":
        print("    ->", out[:300])
    sys.exit(0 if rc == 0 else 1)


if __name__ == "__main__":
    main()
