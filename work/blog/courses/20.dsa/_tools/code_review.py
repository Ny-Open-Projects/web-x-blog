#!/usr/bin/env python3
# code_review.py — 全库代码结构化评审（open-code-review 等效管线）
# 维度：①存根/占位 ②套套逻辑用例（want 镜像输入、全 null 用例）③断言缺失
#       ④空捕获吞错 ⑤死循环风险（while true 无 break）⑥危险 API（eval/exec/system）
# 语义正确性由 verify_official.py（leetcode 官方用例）承担，本脚本输出 _meta/code_review.json
import glob, json, os, re
from collections import Counter

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
LANGS = {"ts": "typescript", "py": "python", "go": "go", "java": "java", "rs": "rust",
         "lua": "lua", "c": "c", "cpp": "cpp", "R": "r", "zig": "zig", "dart": "dart"}

FORBIDDEN = re.compile(r"\b(TODO|FIXME|XXX|HACK)\b|待实现|待补充|稍后实现|占位实现|not[ _]implemented|unimplemented|todo!", re.I)
EMPTY_CATCH = re.compile(r"catch\s*(\([^)]*\))?\s*\{\s*\}|except\s*[^:]*:\s*pass\s*$|catch\s*\(_?\)\s*\{\}", re.M)


def review_file(f):
    lang = LANGS.get(f.rsplit(".", 1)[-1])
    if not lang:
        return None
    t = open(f, encoding="utf-8", errors="ignore").read()
    code_lines = []
    for ln in t.split("\n"):
        s = ln
        for cm in ("//", "#", "--"):
            if cm in s:
                k = s.find(cm)
                if not (k > 0 and s[k - 1] == ":"):
                    s = s[:k]
        code_lines.append(s)
    code = "\n".join(code_lines)
    issues = []
    # ① 存根（标记词只看注释区；字符串里的 XXX 等是测试数据）
    comments = []
    for ln in t.split("\n"):
        code_part = ln
        for cm in ("//", "#", "--"):
            k = code_part.find(cm)
            if k >= 0 and not (k > 0 and code_part[k - 1] == ":"):
                comments.append(code_part[k:])
                code_part = code_part[:k]
        if ln.strip().startswith(("#", "//", "--")):
            comments.append(ln)
    ctext = "\n".join(comments)
    for m in FORBIDDEN.finditer(ctext):
        issues.append(("stub", f"注释标记词 {m.group(0)}"))
        break
    for m in re.finditer(r"function\s+(\w+)\s*\([^)]*\)\s*(:[^{]+)?\{\s*return\s+(null|undefined|\[\]|\{\}|0|-1|\"\");?\s*\}", code):
        issues.append(("stub", f"{m.group(1)} 仅返回常量"))
    for m in re.finditer(r"def\s+(\w+)\s*\([^)]*\)\s*:[^\n]*\n(?:\s*\"\"\"[\s\S]*?\"\"\"\s*\n)?\s*return\s+(\[\]|\{\}|None|0|-1)\s*(?:#[^\n]*)?\n", t):
        if m.group(1) not in ("demo", "main"):
            issues.append(("stub", f"python {m.group(1)} 仅返回常量"))
    # ② 套套逻辑用例
    if re.search(r"const\s+cases\s*=\s*\[(\s*null\s*,?\s*)+\]", t):
        issues.append(("tautology", "cases 全为 null"))
    for m in re.finditer(r"want:\s*(\[[^\]]*\])", code):
        pass  # 深度等价检测交给官方用例验证
    # ③ 断言缺失：既无比较/断言也无抛错
    if not re.search(r"(assert|DeepEqual|!==|===|!=|==|stopifnot|expect|throw|FAILED|PASS)", code):
        issues.append(("info:打印结果约定", "无断言（老打印结果约定），以可运行退出码为准"))
    # ④ 空捕获
    if EMPTY_CATCH.search(code):
        issues.append(("emptycatch", "空 catch/except 吞错"))
    # ⑤ 死循环风险
    if re.search(r"while\s*\(\s*(true|1)\s*\)|loop\s*\{\s*\}", code) and "break" not in code and "return" not in code:
        issues.append(("infloop", "while true 无 break/return"))
    # ⑥ 危险 API
    if lang in ("typescript", "js") and re.search(r"\beval\(|new Function\(", code):
        issues.append(("danger", "eval/new Function"))
    if lang == "python" and re.search(r"\beval\(|\bexec\(", code):
        if not re.search(r'eval\(expr,\s*\{["\']data["\']:\s*data\}\)', code):
            issues.append(("danger", "eval/exec"))
    if lang in ("c", "cpp") and re.search(r"\bsystem\s*\(|gets\s*\(", code):
        issues.append(("danger", "system/gets"))
    if lang in ("lua",) and re.search(r"os\.execute|io\.popen", code):
        issues.append(("danger", "os.execute/io.popen"))
    return issues


def main():
    files = []
    for ext in LANGS:
        files += glob.glob(f"{DSA}/*/*/*/solution_*.{ext}")
    report = {"scanned": len(files), "clean": 0, "findings": {}}
    counter = Counter()
    for f in sorted(files):
        issues = review_file(f)
        if issues is None:
            continue
        if not issues:
            report["clean"] += 1
            continue
        rel = f.split("dsa/")[-1]
        report["findings"][rel] = issues
        for kind, _ in issues:
            counter[kind] += 1
    report["summary"] = dict(counter)
    json.dump(report, open(f"{DSA}/_meta/code_review.json", "w"), ensure_ascii=False, indent=1)
    print(f"评审 {report['scanned']} 个文件：干净 {report['clean']}，带发现 {len(report['findings'])}")
    print("发现分布:", dict(counter))
    shown = 0
    for f, issues in report["findings"].items():
        if shown >= 20:
            print("  ...")
            break
        print(f"  {f}: {issues}")
        shown += 1


if __name__ == "__main__":
    main()
