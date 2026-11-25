---
title: "[Q7228] 没写 .dockerignore：2.3GB 构建上下文，缓存层天天失效"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7228 · 没写 .dockerignore：2.3GB 构建上下文，缓存层天天失效

难度：P6 ｜ 标签：Docker、构建上下文、.dockerignore、层缓存

基线：Python 3.12；Docker/BuildKit 构建上下文与 `.dockerignore` 匹配规则；纯 Python 模拟上下文打包与层哈希。

**问**：`docker build` 每次先传 2.3GB 上下文，CI 上光这一步就 90 秒；`COPY . .` 这层缓存几乎从不命中，改一行代码就要重装全部依赖。上下文明明只是个小项目，为什么这么大？

**答**：
- **结论**：`docker build <context>` 会把**整个目录递归打包**发给 daemon，包括 `.git`、`node_modules`、`.venv`、`data/`、日志、`__pycache__`，除非 `.dockerignore` 显式排除。上下文大小直接决定传输时间；`COPY . .` 的缓存键是**被复制内容的哈希**，只要有一份"git 忽略但 docker 没忽略"的文件变了（日志、`.pytest_cache`、`.DS_Store`），这层就失效，后续 `RUN pip install` 全部重跑。
- **取舍**：`.dockerignore` 越小越干净，但**不能排除构建需要的文件**（`pyproject.toml`、`uv.lock`、源码、迁移脚本），忽略过宽会导致镜像缺文件、运行期 ImportError。多阶段构建 + 先拷依赖清单再拷源码，是让依赖层独立缓存的标准手法。
- **实战**：① 至少排除 `.git`、`.venv`、`__pycache__`、`*.pyc`、`.pytest_cache`、`.mypy_cache`、`.ruff_cache`、`data`、`*.log`；② Dockerfile 顺序 `COPY pyproject.toml uv.lock` → `RUN uv sync --frozen --no-dev` → `COPY . .`；③ CI 用 `docker build --progress=plain` 看每层耗时；④ 用 `du -sh` 对比"目录实际大小"和"上下文大小"验证忽略是否生效。

```python
"""构建上下文打包与 COPY 层缓存键：.dockerignore 前后的对比。"""
import hashlib
import os


def collect(context_root: str, patterns: list[str]) -> dict[str, int]:
    """收集上下文文件（大小），patterns 里是简单后缀/目录名忽略规则。"""
    out: dict[str, int] = {}
    for dirpath, dirnames, filenames in os.walk(context_root):
        rel_dir = os.path.relpath(dirpath, context_root)
        dirnames[:] = [d for d in dirnames
                       if not any(p.strip("*") in d for p in patterns)]
        for name in filenames:
            if any(name.endswith(p.lstrip("*")) or p.strip("*") in rel_dir for p in patterns):
                continue
            path = os.path.join(dirpath, name)
            out[os.path.relpath(path, context_root)] = os.path.getsize(path)
    return out


def layer_hash(files: dict[str, int]) -> str:
    """模拟 COPY 层缓存键：内容与路径的有序哈希。"""
    h = hashlib.sha256()
    for path in sorted(files):
        h.update(path.encode())
        h.update(str(files[path]).encode())
    return h.hexdigest()[:12]


def human(n: int) -> str:
    if n >= 1024 * 1024:
        return f"{n / 1024 / 1024:.1f}MB"
    if n >= 1024:
        return f"{n / 1024:.1f}KB"
    return f"{n}B"


if __name__ == "__main__":
    root = "/tmp/demo_ctx"
    os.makedirs(f"{root}/app", exist_ok=True)
    os.makedirs(f"{root}/.git/objects", exist_ok=True)
    os.makedirs(f"{root}/.venv/lib", exist_ok=True)
    os.makedirs(f"{root}/data", exist_ok=True)
    os.makedirs(f"{root}/app/__pycache__", exist_ok=True)

    with open(f"{root}/app/main.py", "w") as f:
        f.write("print('hi')\n")
    with open(f"{root}/pyproject.toml", "w") as f:
        f.write("[project]\nname='demo'\n")
    with open(f"{root}/.git/objects/pack", "w") as f:
        f.write("x" * 300_000)
    with open(f"{root}/.venv/lib/site.py", "w") as f:
        f.write("y" * 200_000)
    with open(f"{root}/data/dump.csv", "w") as f:
        f.write("z" * 400_000)
    with open(f"{root}/app/__pycache__/main.pyc", "wb") as f:
        f.write(b"\x00" * 100_000)

    ignore = [".git", ".venv", "data", "__pycache__", ".pytest_cache", ".mypy_cache"]
    everything = collect(root, [])
    cleaned = collect(root, ignore)

    print("无 .dockerignore:", len(everything), "个文件", human(sum(everything.values())))
    print("有 .dockerignore:", len(cleaned), "个文件", human(sum(cleaned.values())))
    print("  传输量下降:", f"{1 - sum(cleaned.values()) / sum(everything.values()):.0%}")

    h1 = layer_hash(cleaned)
    with open(f"{root}/app/__pycache__/main.pyc", "ab") as f:   # 无关文件变化
        f.write(b"\x00" * 10_000)
    no_ignore = collect(root, [])
    dirty = collect(root, ignore)
    print("改动 __pycache__ 后：")
    print("  无 ignore 的 COPY 层哈希:", layer_hash(no_ignore), "变了:",
          layer_hash(no_ignore) != h1)
    print("  有 ignore 的 COPY 层哈希:", layer_hash(dirty), "变了:", layer_hash(dirty) != h1)

    print("结论：上下文与缓存键都受忽略规则支配；依赖清单先拷，源码后拷")
```

**追问一**：`COPY . .` 和 `ADD . .` 有什么区别？
→ 解析：`ADD` 额外支持自动解压 tar、从 URL 下载，语义不透明、缓存行为更难预测；官方建议除"确实需要解压"外一律用 `COPY`。解压需求可以拆成 `COPY x.tar.gz` + `RUN tar -xzf`，步骤显式、缓存可控。

**追问二**：为什么 `COPY . .` 放在 `pip install` 之前会导致"改一行代码重装依赖"？
→ 解析：镜像层缓存是链式的，某一层的内容哈希变了，它和它之后的**所有层**都失效。`COPY . .` 在依赖安装之前，源码一变这层就变，`RUN pip install` 自然重跑。把依赖清单单独 `COPY` 并安装，源码改动只影响最后一两层。
