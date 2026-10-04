#!/usr/bin/env python3
"""
抽取 md 里 '''go 围栏的代码块，逐个真编译，验证「可直接复制运行」不是嘴上说说。

用法:
    python3 ai/scripts/check_go_blocks.py work/target/es/xxx.md
环境变量:
    GOPROXY  默认走 goproxy.cn（国内源）
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

BLOCK = re.compile(r"^'''go\s*\n(.*?)^'''\s*$", re.S | re.M)
# 也兼容标准 ```go 围栏（进 hexo 转换后的产物）
BLOCK_MD = re.compile(r"^```go\s*\n(.*?)^```\s*$", re.S | re.M)

GO = shutil.which("go") or "/usr/local/go1.26.5/bin/go"


def extract(md: Path):
    text = md.read_text(encoding="utf-8")
    blocks = [(m.start(), m.group(1)) for m in BLOCK.finditer(text)]
    blocks += [(m.start(), m.group(1)) for m in BLOCK_MD.finditer(text)]
    return sorted(blocks)


def main():
    if len(sys.argv) < 2:
        sys.exit("用法: check_go_blocks.py <md 文件>")
    md = Path(sys.argv[1])
    if not md.exists():
        sys.exit(f"文件不存在: {md}")

    blocks = extract(md)
    if not blocks:
        print("没有 go 代码块，跳过")
        return

    base = Path("/tmp/gocheck") / md.stem
    if base.exists():
        shutil.rmtree(base, ignore_errors=True)

    env = dict(os.environ)
    env.setdefault("GOPROXY", "https://goproxy.cn,direct")
    env.setdefault("GOFLAGS", "-mod=mod")
    # 沙箱写不了 ~/go，整套缓存挪到 /tmp，顺带跨篇复用已下载依赖
    gopath = Path("/tmp/gocheck/gopath")
    gopath.mkdir(parents=True, exist_ok=True)
    env["GOPATH"] = str(gopath)
    env["GOMODCACHE"] = str(gopath / "pkg" / "mod")
    env["GOCACHE"] = "/tmp/gocheck/gocache"

    ok = fail = 0
    for i, (pos, code) in enumerate(blocks, 1):
        d = base / f"block{i}"
        d.mkdir(parents=True, exist_ok=True)
        (d / "main.go").write_text(code, encoding="utf-8")

        (d / "go.mod").write_text("module gocheck\n\ngo 1.21\n", encoding="utf-8")

        def run(*args):
            return subprocess.run(args, cwd=d, env=env, capture_output=True, text=True, timeout=300)

        r1 = run(GO, "mod", "tidy")
        r2 = run(GO, "build", "./...")
        if r2.returncode == 0:
            ok += 1
            print(f"  ✅ 块 {i} 编译通过")
        else:
            fail += 1
            print(f"  ❌ 块 {i} 编译失败")
            for line in (r1.stderr + r2.stderr).strip().splitlines()[:12]:
                print(f"     {line}")

    print(f"\n{md.name}: 通过 {ok} / 失败 {fail}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
