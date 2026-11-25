---
title: "[Q7241] ARG 传密码：删掉文件也没用，密钥留在镜像层里"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7241 · ARG 传密码：删掉文件也没用，密钥留在镜像层里

难度：P6 ｜ 标签：Docker、多阶段构建、镜像层、密钥管理

基线：Python 3.12；用"层 = 文件快照 + 元数据"的模型模拟 `docker build` 与 `docker history`。

**问**：Dockerfile 里写 `ARG PIP_TOKEN`，`RUN pip install --index-url https://user:$PIP_TOKEN@private/simple ...`，同一条 `RUN` 里又 `rm -f /root/.pip/pip.conf`。以为"删掉就没了"，结果安全扫描在镜像里扫出了 token，`docker history` 也能直接看到。文件明明已经删了，为什么还能被捞出来？

**答**：
- **结论**：镜像不是"最终文件系统"，而是**层的叠加**。每一条 `RUN`/`COPY`/`ARG` 都生成一层，层是只读的；后一层的 `rm` 只是在合并视图里加了一个"白障（whiteout）"，**前一层的文件内容仍然完整地存在于 layer tar 里**。`docker save` 导出的每个 layer 都能解开看到原始文件；`docker history` 还会显示 `ARG` 的值与构建命令。所以"同一层里下载再删除"在旧版 builder 下是无效的（文件确实在中间状态落盘过）。
- **取舍**：三种正确做法：① **多阶段构建**：在 builder 阶段用密钥装依赖，最终阶段只 `COPY --from=builder` 产物（venv/二进制），密钥与中间文件留在 builder，不进最终镜像；② **BuildKit secret mount**：`RUN --mount=type=secret,id=pip_token ...`，secret 以 tmpfs 挂载、不落层，构建结束即消失（需要 `DOCKER_BUILDKIT=1`，CI 里用 `--secret` 传）；③ **运行时注入**：镜像里完全不放密钥，容器启动时从 KMS/Vault 取（但要考虑启动延迟与泄露面）。
- **实战**：① CI 里加 `docker history --no-trunc` 与镜像层扫描（trivy/grype + 自定义正则），把"密钥进镜像"变成构建失败；② `.dockerignore` 排除 `.env`、`*.pem`、`pip.conf`；③ 依赖私有源时优先用构建机的凭证助手（`--mount=type=secret` + `pip --config-settings`），不要写进 URL；④ 一旦泄露，**轮换密钥**是第一步——镜像可能已被推到 registry 并被拉取，删镜像不等于没发生。

```python
"""镜像层模型：rm 只是白障，secret 仍在旧层；多阶段才真正隔离。"""
import json

SECRET = "glpat-EXAMPLE-TOKEN-9f2a"


class Image:
    def __init__(self) -> None:
        self.layers: list[dict] = []

    def add(self, instruction: str, files: dict[str, str] | None = None,
            args: dict[str, str] | None = None, env: dict[str, str] | None = None,
            deleted: list[str] | None = None) -> None:
        self.layers.append({
            "instruction": instruction,
            "files": files or {},
            "args": args or {},
            "env": env or {},
            "deleted": deleted or [],
        })

    def filesystem(self) -> dict[str, str]:
        fs: dict[str, str] = {}
        for layer in self.layers:                 # 合并视图：后层删除生效
            for path in layer["deleted"]:
                fs.pop(path, None)
            fs.update(layer["files"])
        return fs

    def history(self) -> None:
        print("  docker history:")
        for layer in self.layers:
            meta = {**layer["args"], **layer["env"]}
            print(f"    {layer['instruction'][:58]:<60}{json.dumps(meta, ensure_ascii=False)}")

    def scan(self, needle: str) -> list[str]:
        hits = []
        for i, layer in enumerate(self.layers):
            blob = json.dumps(layer, ensure_ascii=False)
            if needle in blob:
                hits.append(f"layer {i}: {layer['instruction'][:40]}")
        return hits


def single_stage() -> Image:
    img = Image()
    img.add("ARG PIP_TOKEN", args={"PIP_TOKEN": SECRET})
    img.add("RUN pip install --index-url https://user:$PIP_TOKEN@private/simple pkg",
            files={"/root/.pip/pip.conf": f"index-url = https://user:{SECRET}@private/simple\n"},
            env={"PIP_INDEX_URL": f"https://user:{SECRET}@private/simple"})
    img.add("RUN rm -f /root/.pip/pip.conf", deleted=["/root/.pip/pip.conf"])
    img.add("COPY app /app", files={"/app/main.py": "print('hi')\n"})
    return img


def multi_stage() -> Image:
    builder = Image()
    builder.add("ARG PIP_TOKEN", args={"PIP_TOKEN": SECRET})
    builder.add("RUN pip install --prefix=/install ...",
                files={"/install/lib/pkg.py": "# pkg\n"},
                env={"PIP_INDEX_URL": f"https://user:{SECRET}@private/simple"})

    final = Image()
    final.add("COPY --from=builder /install /usr/local", files={"/usr/local/lib/pkg.py": "# pkg\n"})
    final.add("COPY app /app", files={"/app/main.py": "print('hi')\n"})
    return final


if __name__ == "__main__":
    print("单阶段构建:")
    img = single_stage()
    img.history()
    print("  合并视图里有 pip.conf 吗:", "/root/.pip/pip.conf" in img.filesystem())
    print("  但层扫描命中:", img.scan(SECRET))
    print("  -> rm 只加了白障，layer tar 里仍有完整文件\n")

    print("多阶段构建（最终镜像只有 final 的层）:")
    final = multi_stage()
    final.history()
    print("  层扫描命中:", final.scan(SECRET))
    print("  最终文件系统:", sorted(final.filesystem()))
    print("\n结论：密钥不能进任何要发布的层；多阶段 + BuildKit secret 才是边界")
```

**追问一**：为什么 `RUN export TOKEN=xxx && pip install ... && unset TOKEN` 也躲不过？

→ 解析：`export` 只影响该 shell 进程的环境，而**层的 `created_by` 元数据会记录整条命令字符串**（变量在构建时已展开），扫描器与 `docker history --no-trunc` 直接读这行就能拿到。即使不展开，环境变量在 `RUN` 执行期间也会被写进容器的 `/proc/self/environ`，任何读该文件的东西都能看到。结论：**只要密钥出现在 Dockerfile 文本或层元数据里，就等于公开**；唯一安全的是"密钥从不进入构建上下文"——即 BuildKit secret mount 或运行时注入。

**追问二**：多阶段构建就一定安全吗？

→ 解析：只有当密钥**只出现在被丢弃的中间阶段**时才安全。常见反例：`COPY . .` 把 `.env` 拷进 builder，然后 `COPY --from=builder /app /app` 把整个 `/app`（含 `.env`）带进最终阶段；或者在最终阶段 `ARG` 又用了一次。判断标准不是"有没有多阶段"，而是"最终镜像的每一层里有没有"。落地检查：对最终镜像跑 `docker save | tar -x` 后 grep，或直接用 trivy 的 secret 扫描；再把这条检查放进 CI 的构建后步骤，失败即阻断发布。
