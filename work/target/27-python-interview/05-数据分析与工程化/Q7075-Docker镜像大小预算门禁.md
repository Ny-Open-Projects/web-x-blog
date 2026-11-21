---
title: "[Q7075] Docker 镜像大小预算与瘦身门禁"
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7075 · Docker 镜像大小预算与瘦身门禁

难度：P6 ｜ 标签：Docker / CI / 容量规划 / 镜像分层

**问**：服务的 Docker 镜像半年从 300 MB 涨到 1.6 GB，拉取时间拖慢发布与扩容。怎么给镜像定"大小预算"并在 CI 里强制执行，而不是每次靠人肉瘦身？

**答**：

**结论**：镜像膨胀的标准剧本是：`COPY . .` 把 .git/数据集/测试夹带进去、构建依赖（gcc、dev 头文件）留在最终层、pip 缓存未清、依赖越加越多。治理必须是"预算制"而非"运动式"：在 CI 里构建后测量镜像大小，超过预算（如 450 MB）直接 fail 并输出层大小排行（dive/`docker history` 的机读版本）。预算要分层定：基础镜像层预算 + 依赖层预算 + 代码层预算，超哪层修哪层，避免"总账超了不知道谁的责任"。

**取舍**：两个常见极端——① 瘦到极致（distroless + 静态编译）：小但调试困难，shell 都没有，事故时进不了容器；② 不在乎大小：拉取慢只是表象，更大的是攻击面（镜像里多一个工具就多一份 CVE 扫描噪音）与存储账（镜像仓库按 GB 计费，1.6 GB × 每日构建 × 保留 90 天是 TB 级账单）。中间解：runtime 用 slim 基础镜像（~60 MB），调试需求用单独的 debug tag 满足。多阶段构建是标准答案，但要注意 `pip install` 单独成层 + 先 COPY lockfile 再装依赖，让依赖层可缓存。

**实战**：Python 专属清单：`pip install --no-cache-dir`、`PYTHONDONTWRITEBYTECODE=1`、`--compile` 权衡（pyc 加速启动但增体积，容器常驻服务建议要 pyc）；`COPY . .` 改为显式 COPY 目录清单 + `.dockerignore` 兜底（.git、tests、data、*.parquet 必须列进去）；heavy 依赖（torch/pandas）评估拆分到独立服务或按需加载。CI 门禁输出：预算表、实际、diff、TOP10 层——让超预算的 PR 自己贴上"谁涨的"。

```python
# 镜像层预算门禁：按层分配预算并定位膨胀源（仅标准库，Python 3.9+）
from __future__ import annotations


BUDGET_MB = {"base": 60, "deps": 260, "app": 40, "assets": 20}


def parse_layers(history: list[tuple[str, float]]) -> dict[str, float]:
    """history: [(layer_tag, size_mb)]，按 tag 归层（生产用 docker history --no-trunc）。"""
    layers: dict[str, float] = {k: 0.0 for k in BUDGET_MB}
    for tag, size in history:
        if tag not in layers:
            tag = "assets"  # 未归类默认进 assets 层（最容易夹带的层）
        layers[tag] += size
    return layers


def gate(layers: dict[str, float]) -> list[str]:
    violations = []
    for k, b in BUDGET_MB.items():
        if layers[k] > b:
            violations.append(f"{k}: {layers[k]:.0f}MB 超预算 {b}MB (+{layers[k]-b:.0f})")
    total = sum(layers.values())
    print(f"总大小 {total:.0f} MB / 预算 {sum(BUDGET_MB.values())} MB")
    return violations


def main() -> None:
    # 一次"膨胀"构建：deps 装了 gcc 工具链 + app 层夹带了 .git 与数据集
    history = [
        ("base", 55), ("deps", 620), ("app", 380), ("assets", 0),
    ]
    layers = parse_layers(history)
    v = gate(layers)
    print("门禁违规:", v)
    assert any(s.startswith("deps") for s in v)
    assert any(s.startswith("app") for s in v)

    # 瘦身后：多阶段构建 + .dockerignore
    slim = parse_layers([("base", 55), ("deps", 240), ("app", 35), ("assets", 5)])
    assert not gate(slim), "瘦身后应全部达标"
    print("结论：预算分层后，超支能定位到具体层与 PR")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么依赖层要先 COPY lockfile 再 COPY 代码？——层缓存按内容 hash 失效；代码天天变、依赖偶尔变，先锁依赖让 95% 的构建直接复用依赖层，构建时间从分钟级降到秒级，这也是"预算门禁"不会拖慢 CI 的前提。
- 追问 1.1：pyc（--compile）到底要不要？——容器常驻服务启动一次跑很久，pyc 省 import 时间值得；Serverless 冷启动敏感场景更值得。但 pyc 让镜像变大 10-20%，且必须与 Python 小版本一致（3.12.x 与 3.13 的 pyc 不通用），基线镜像升级时 pyc 全作废。
- 追问 2：镜像预算门禁会不会阻碍"必须加一个大依赖"的合法变更？——预算调整要走 PR：改 BUDGET_MB 的 diff 必须附上"为什么这 100 MB 值得 + 有没有替代方案"的说明，把成本决策显性化、留痕化，而不是默认放行。

**背诵要点**：

1. 预算分层制（base/deps/app/assets 各有上限）+ CI 门禁 fail，比运动式瘦身可持续；未归类层默认进 assets 层防夹带。
2. 瘦身三板斧：多阶段构建、--no-cache-dir、.dockerignore 显式清单；pyc 对常驻/冷启动敏感服务值得，小版本升级即作废。
3. 大小不只是速度：攻击面、CVE 扫描噪音、镜像仓库 GB 计费都是账；调试需求走单独 debug tag 不进 runtime。

**复盘追问**：

1. 如果镜像里发现有人半年前 COPY 进去的 800 MB 压测数据，流程上哪一环失守了？
2. 门禁上线第一天 20 个团队集体超预算，你如何设计豁免与整改节奏？
