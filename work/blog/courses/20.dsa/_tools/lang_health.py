#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSA 多语言题库 —— go/java/ts 三层同源体检 harness
对每一层做：① stub 检测 ② 编译/运行 ③ broken-pattern(TS 残留/坏 demo)检测
输出 _tools/lang_health_report.json
"""
import os, re, sys, json, shutil, tempfile, subprocess, concurrent.futures, functools

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
GOBIN = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"
TIMEOUT = 25

def find_files(lang):
    root = os.path.join(BASE, lang)
    ext = {"go": ".go", "java": ".java", "ts": ".ts"}[lang]
    out = []
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if fn.endswith(ext):
                out.append(os.path.join(dp, fn))
    return out

# ---------- stub / broken-pattern 启发式 ----------
def go_stub(src):
    if "TODO: solution not implemented" in src:
        return True
    # main() 只打印一个常量串（done/空）且无调用用户函数 => 空壳
    m = re.search(r"func main\(\)\s*\{(.*?)\n\}", src, re.S)
    if m:
        body = m.group(1)
        # 去掉 fmt.Println / print 这类输出后，是否还有"标识符("的调用
        body2 = re.sub(r"fmt\.Println\([^)]*\)", "", body)
        body2 = re.sub(r"print\([^)]*\)", "", body2)
        if re.search(r"[A-Za-z_]\w*\s*\(", body2):
            return False
        return True
    return False

def java_stub(src):
    if re.search(r"TODO", src):
        return True
    return False

def ts_stub(src):
    if re.search(r"TODO", src):
        return True
    return False

def ts_broken_patterns(src):
    """返回检测到的坏模式标签列表（TS 层的同源病根）"""
    tags = []
    if re.search(r"BROKEN", src):
        tags.append("BROKEN_marker")
    # new ListNode/TreeNode 但没有对应 class/interface 定义（类只在注释里）
    for cls in ("ListNode", "TreeNode", "Node"):
        if re.search(r"\bnew\s+" + cls + r"\b", src) and not re.search(r"(class|interface)\s+" + cls + r"\b", src):
            tags.append(f"missing_class_{cls}")
    # 顶层 demo() 自调用（决定 TS 能否被 node 实测）；仅定义不算
    if re.search(r"(?:^|\n)\s*demo\s*\(\s*\)\s*;?\s*(?:$|\n)", src):
        tags.append("demo_self_call")
    # 未定义的 guess / external API（LeetCode 全局）
    if re.search(r"\bguess\s*\(", src) and not re.search(r"function\s+guess\s*\(", src) and "guess =" not in src:
        tags.append("undefined_guess")
    return tags

# ---------- 运行探针 ----------
def run_go(path):
    d = os.path.dirname(path)
    try:
        r = subprocess.run([GOBIN, "run", os.path.basename(path)],
                           cwd=d, env={**os.environ, "GO111MODULE": "off"},
                           capture_output=True, text=True, timeout=TIMEOUT)
        return (r.returncode == 0, (r.stderr or r.stdout).strip().splitlines()[-1][:160] if (r.stderr or r.stdout).strip() else "")
    except subprocess.TimeoutExpired:
        return (False, "TIMEOUT")
    except Exception as e:
        return (False, f"EXC {e}")

def run_java(path):
    # 去掉 package 行，拷到临时目录编译+运行
    try:
        src = open(path, encoding="utf-8").read()
        cls = None
        mm = re.search(r"(?:public\s+)?class\s+(\w+)", src)
        if mm:
            cls = mm.group(1)
        if not cls:
            return ("no_class", "", "cannot find class name")
        tmp = tempfile.mkdtemp()
        cleaned = re.sub(r"^\s*package\s+[\w.]+;", "", src, flags=re.M)
        jf = os.path.join(tmp, cls + ".java")
        open(jf, "w", encoding="utf-8").write(cleaned)
        c = subprocess.run([JAVAC, jf], cwd=tmp, capture_output=True, text=True, timeout=TIMEOUT)
        if c.returncode != 0:
            lines = [l for l in (c.stderr or "").splitlines() if l.strip()]
            err = None
            for l in lines:
                if any(k in l for k in ("错误", "error", "Exception", "symbol", "不兼容", "找不到")):
                    err = l; break
            err = err or (lines[0] if lines else "compile_fail")
            return ("compile_fail", "", err[:160])
        r = subprocess.run([JAVA, "-cp", tmp, cls], cwd=tmp, capture_output=True, text=True, timeout=TIMEOUT)
        if r.returncode != 0:
            lines = [l for l in (r.stderr or "").splitlines() if l.strip()]
            err = None
            for l in lines:
                if "Exception" in l or "Error" in l:
                    err = l; break
            err = err or (lines[0] if lines else "run_fail")
            return ("run_fail", "", err[:160])
        return ("ok", (r.stdout or "").strip()[:200], "")
    except subprocess.TimeoutExpired:
        return ("timeout", "", "TIMEOUT")
    except Exception as e:
        return ("exc", "", f"EXC {e}")

def run_ts(path):
    try:
        # node 22 strip-types：仅捕获语法错与顶层抛错；TS 模块多不自调用
        r = subprocess.run([NODE, "--experimental-strip-types", path],
                           capture_output=True, text=True, timeout=TIMEOUT)
        if r.returncode != 0:
            lines = [l for l in (r.stderr or "").splitlines()
                     if l.strip() and "MODULE_TYPELESS" not in l and "Reparsing" not in l
                     and "trace-warnings" not in l and "Node.js v" not in l]
            err = lines[0] if lines else "run_fail"
            return ("run_fail", "", err[:160])
        return ("ok", "", "")
    except subprocess.TimeoutExpired:
        return ("timeout", "", "TIMEOUT")
    except Exception as e:
        return ("exc", "", f"EXC {e}")

def probe(lang, path):
    if lang == "go":
        return (path, run_go(path))
    if lang == "java":
        return (path, run_java(path))
    if lang == "ts":
        return (path, run_ts(path))
    return (path, ("unknown", "", ""))

def process(lang):
    files = find_files(lang)
    res = {"lang": lang, "total": len(files), "stub": 0, "stub_files": [],
           "compile_or_run_fail": 0, "fail_files": [], "runnable": 0,
           "broken_pattern_files": [], "broken_pattern_counts": {}}
    src_cache = {}
    def get_src(p):
        if p not in src_cache:
            try:
                src_cache[p] = open(p, encoding="utf-8").read()
            except Exception:
                src_cache[p] = ""
        return src_cache[p]

    # 1) stub 检测（不跑）
    for p in files:
        src = get_src(p)
        if lang == "go" and go_stub(src):
            res["stub"] += 1; res["stub_files"].append(p)
        elif lang == "java" and java_stub(src):
            res["stub"] += 1; res["stub_files"].append(p)
        elif lang == "ts" and ts_stub(src):
            res["stub"] += 1; res["stub_files"].append(p)

    # 2) 非 stub 文件的编译/运行探针（并行）
    todo = [p for p in files if p not in set(res["stub_files"])]
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as ex:
        for p, out in ex.map(functools.partial(probe, lang), todo, chunksize=8):
            if lang == "go":
                ok, msg = out
                if ok:
                    res["runnable"] += 1
                else:
                    res["compile_or_run_fail"] += 1; res["fail_files"].append((p, msg))
            else:
                status, out1, err = out
                if status == "ok":
                    res["runnable"] += 1
                else:
                    res["compile_or_run_fail"] += 1; res["fail_files"].append((p, err or out1))

    # 3) TS 坏模式检测（全量）
    if lang == "ts":
        for p in files:
            tags = ts_broken_patterns(get_src(p))
            if tags:
                res["broken_pattern_files"].append((p, tags))
                for t in tags:
                    res["broken_pattern_counts"][t] = res["broken_pattern_counts"].get(t, 0) + 1
    return res

def main():
    langs = sys.argv[1].split(",") if len(sys.argv) > 1 else ["go", "java", "ts"]
    report = {}
    for lang in langs:
        print(f"[*] processing {lang} ...", flush=True)
        report[lang] = process(lang)
        r = report[lang]
        print(f"    total={r['total']} stub={r['stub']} runnable={r['runnable']} "
              f"compile_or_run_fail={r['compile_or_run_fail']}", flush=True)
        if lang == "ts":
            print(f"    ts broken_patterns={r['broken_pattern_counts']}", flush=True)
    # 截断超大明细列表，保留准确计数
    for lang in report:
        for k in ("stub_files", "fail_files", "broken_pattern_files"):
            if k in report[lang] and len(report[lang][k]) > 300:
                report[lang][k] = report[lang][k][:300] + [f"... +{len(report[lang][k])-300} more"]
    json.dump(report, open(os.path.join(BASE, "_tools", "lang_health_report.json"), "w"),
              ensure_ascii=False, indent=1)
    print("Wrote _tools/lang_health_report.json")

if __name__ == "__main__":
    main()
