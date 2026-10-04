#!/usr/bin/env python3
"""把 bash 块里的尖括号占位符 `<pod>` 换成可执行的 shell 变量 `$POD`。

判据（踩过的坑）：`<none>` 这种是**命令输出里的真实值**，绝不能动。
本项目的惯例是输出行以 `#` 开头，所以：
    - 只处理 ```bash / ```shell 代码块内
    - 跳过以 `#` 开头的行（输出 / 注释）
    - 只替换紧跟命令动词行的 `<xxx>`

用法:
    python3 ai/scripts/fix_placeholders.py <文件或目录> [--apply]
不带 --apply 时只打印将改动的内容。
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

VAR_MAP = {
    "pod": "POD", "Pod": "POD", "svc": "SVC", "ns": "NS", "namespace": "NAMESPACE",
    "node": "NODE", "name": "NAME", "deploy": "DEPLOY", "cm": "CM", "secret": "SECRET",
    "pvc": "PVC", "pv": "PV", "sa": "SA", "id": "ID", "key": "KEY", "value": "VALUE",
    "n": "N", "ip": "IP", "port": "PORT", "image": "IMAGE", "tag": "TAG",
    "container": "CONTAINER", "dir": "DIR", "file": "FILE", "user": "USER",
    "crd": "CRD", "ctx": "CTX", "cluster": "CLUSTER", "url": "URL", "host": "HOST",
    "path": "PATH", "cert": "CERT", "token": "TOKEN", "rp": "RP", "sts": "STS",
}
TIP = "# 下面命令中的变量按你的集群环境赋值后再执行"

OPEN = re.compile(r"^```(bash|shell|sh)\s*$")
CLOSE = re.compile(r"^```\s*$")   # 闭合围栏没有语言标记，必须单独匹配，否则块永不结束
PLACE = re.compile(r"<([一-龥A-Za-z_][一-龥A-Za-z0-9_]*)>")

# 不能当 shell 变量名的保留字（$PATH 会把系统 PATH 冲掉）
RESERVED = {"PATH", "HOME", "USER", "HOSTNAME", "PWD", "IFS", "PS1", "PS2", "UID",
            "TERM", "SHELL", "LANG", "HOST", "TMPDIR", "OLDPWD", "SHLVL"}
OVERRIDE = {"path": "SRC_PATH", "host": "TARGET_HOST", "user": "USER_NAME",
            "home": "HOME_DIR", "pwd": "WORK_DIR", "id": "RES_ID"}


def tovar(name: str) -> str:
    if name in OVERRIDE:
        return OVERRIDE[name]
    v = VAR_MAP.get(name, name.upper())
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", v) or v in RESERVED:
        # 中文占位符（如 `<pod名>`）或撞了 shell 保留字：按关键词落到目标变量
        low = v.lower()
        for kw, target in (("pod", "POD"), ("命名空间", "NS"), ("ns", "NS"),
                           ("node", "NODE"), ("节点", "NODE"), ("svc", "SVC"), ("服务", "SVC"),
                           ("容器", "CONTAINER"), ("container", "CONTAINER"),
                           ("路径", "SRC_PATH"), ("目录", "SRC_PATH"), ("path", "SRC_PATH"),
                           ("镜像", "IMAGE"), ("端口", "PORT"), ("用户", "USER_NAME"),
                           ("集群", "CLUSTER"), ("索引", "INDEX"), ("文件", "FILE_NAME")):
            if kw in low:
                return target
        return "RES_NAME"
    return v


def process(path: Path, apply: bool):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out, changed, blocks = [], 0, 0
    in_block = False
    block_has = False
    for ln in lines:
        stripped = ln.rstrip("\n")
        if OPEN.match(stripped):
            in_block, block_has = True, False
            out.append(ln)
            continue
        if CLOSE.match(stripped) and in_block:
            in_block = False
            out.append(ln)
            continue
        if in_block:
            bare = stripped.strip()
            if bare.startswith("#") or not PLACE.search(bare):
                out.append(ln)
                continue
            if not block_has:
                out.append(TIP + "\n")
                block_has = True
                blocks += 1
            new = PLACE.sub(lambda m: "$" + tovar(m.group(1)), ln)
            if new != ln:
                changed += 1
            out.append(new)
            continue
        out.append(ln)

    if apply and changed:
        bak = Path("/tmp/fix-ph-bak") / path.name
        bak.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, bak)
        path.write_text("".join(out), encoding="utf-8")
    return changed, blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    p = Path(args.target)
    files = [p] if p.is_file() else sorted(p.glob("*.md"))
    files = [f for f in files if not f.name.startswith("_")]

    tot_files, tot_lines, tot_blocks = 0, 0, 0
    for f in files:
        c, b = process(f, args.apply)
        if c:
            tot_files += 1
            tot_lines += c
            tot_blocks += b
            print(f"  {f.name[:62]:<64} {c:>3} 处 / {b} 块")
    mode = "已修复" if args.apply else "待修复（加 --apply 落盘）"
    print(f"\n[{mode}] {tot_files} 个文件 / {tot_lines} 处占位符 / {tot_blocks} 个代码块")
    return 0


if __name__ == "__main__":
    sys.exit(main())
