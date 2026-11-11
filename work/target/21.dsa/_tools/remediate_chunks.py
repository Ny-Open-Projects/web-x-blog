#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSA remediation 分块枚举器
枚举 go/java/ts 中需要修复的文件（stub / 编译运行失败 / BROKEN / ts 需补 demo），
按 (lang, abspath) 输出为互斥 chunk，供并行 agent 断点续跑。
用法: python3 remediate_chunks.py [--langs go,java,ts] [--n 12] [--out remediate_chunks.json]
"""
import os, re, sys, json, glob

BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
LANGS = ["go", "java", "ts"]


def is_go_stub(src):
    if "TODO: solution not implemented" in src:
        return True
    m = re.search(r"func main\(\)\s*\{(.*?)\n\}", src, re.S)
    if m:
        body = re.sub(r"fmt\.Println\([^)]*\)", "", m.group(1))
        body = re.sub(r"print\([^)]*\)", "", body)
        if re.search(r"[A-Za-z_]\w*\s*\(", body):
            return False
        return True
    return False


def java_stub(src):
    return bool(re.search(r"TODO", src))


def ts_broken(src):
    if re.search(r"BROKEN", src):
        return True
    # demo 调参错误（空参调用）即视为需修
    if re.search(r"(?:^|\n)\s*demo\s*\(\s*\)\s*;?\s*(?:$|\n)", src):
        # 顶层 demo() 自调用是好的；这里只标记 export function demo 内调参错误的由 agent 处理
        pass
    return False


def needs_work(lang, path):
    # 纳入全部文件：agent 会按 Python 参考逐一重写，门禁只做编译/运行兜底
    return True


def main():
    args = sys.argv[1:]
    langs = LANGS
    n = 12
    out = "remediate_chunks.json"
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--langs":
            langs = args[i+1].split(","); i += 2
        elif a == "--n":
            n = int(args[i+1]); i += 2
        elif a == "--out":
            out = args[i+1]; i += 2
        else:
            i += 1
    items = []
    for lang in langs:
        for dp, _, fns in os.walk(os.path.join(BASE, lang)):
            for fn in fns:
                if fn == "README.md" or not fn.endswith((".go", ".java", ".ts")):
                    continue
                p = os.path.join(dp, fn)
                if needs_work(lang, p):
                    rel = os.path.relpath(p, BASE)
                    items.append({"lang": lang, "path": p, "rel": rel})
    # 互斥分块：轮转
    chunks = [[] for _ in range(n)]
    for idx, it in enumerate(items):
        chunks[idx % n].append(it)
    report = {
        "total": len(items),
        "n_chunks": n,
        "lang_breakdown": {l: sum(1 for it in items if it["lang"] == l) for l in langs},
        "chunks": chunks,
    }
    json.dump(report, open(os.path.join(BASE, "_tools", out), "w"), ensure_ascii=False, indent=1)
    print("total files to remediate:", len(items))
    print("lang_breakdown:", report["lang_breakdown"])
    print("chunks:", n, "-> sizes:", [len(c) for c in chunks])
    print("wrote _tools/" + out)


if __name__ == "__main__":
    main()
