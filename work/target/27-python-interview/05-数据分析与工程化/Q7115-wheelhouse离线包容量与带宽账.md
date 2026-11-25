---
title: [Q7115] wheelhouse 离线包的容量与带宽账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7115 · wheelhouse 离线安装包的容量与带宽账

难度：P6 ｜ 标签：容量规划 / 离线部署 / 交付工程

**问**：要把一个数据平台交付到无外网环境（客户内网/隔离区），方案是 wheelhouse 全量离线包。包体积、平台矩阵、增量更新这三本账怎么算？"pip download 打包一切"的 naive 方式会在哪里翻车？

**答**：
- **结论**：三本账：① **体积账**——naive `pip download -r requirements.txt` 下载的是**当前平台**的 wheel，而 requirements 解析出的传递依赖在无网环境无法补齐；体积大头是带 C 扩展的包（numpy/torch/pandas/psycopg 等多平台 wheel 各自数百 MB），"全平台矩阵"（linux x86_64/aarch64 × cp310/311/312）下载量是单平台的 10~20 倍——必须锁定目标平台用 `--only-binary --platform --python-version` 精准拉取，体积可控在 1~3GB；② **平台账**——无网环境装不上 sdist（没有编译器/没法拉构建链），必须全 wheel 化：`pip download --only-binary=:all:` 提前暴露"某依赖没有对应平台 wheel"的问题，这一步是 naive 方案第一个翻车点（某些小众包只发 sdist）；③ **增量账**——全量重打 2GB 包每次交付/校验成本高，应按"锁定版本清单 diff"做增量包（只新增变化的 wheel），配合哈希清单（requirements.txt 带 `--hash`）做完整性校验。翻车点清单：传递依赖的 extras 缺失、依赖解析在离线端重新进行时找不到包（要用 `--no-deps` + 完整冻结清单或直接在打包端解析好）、pip 版本差异导致 resolver 行为不同。
- **取舍**：交付形态选择：wheelhouse 目录（可挂载、可 rsync 增量）vs 单文件 zip（`pip download --dest` + 打包，一次交付不可增量）vs 内网 PyPI 镜像（devpi/Nexus——持续交付、多项目共享，但要在客户内网运维一个服务）。单次交付用 zip，长期合作/多环境用内网镜像。校验策略：清单哈希锁定（`--require-hashes`）让离线端不解析、只按哈希装，消灭"离线端 resolver 走偏"这一最大不确定性。
- **实战**：流水线化：① 打包 job 在 CI 固定 Python 版本 + `--only-binary=:all: --platform manylinux2014_x86_64` 等目标矩阵，产出 wheel + SHA256 清单；② 交付包带 `install.sh`：校验哈希 → `pip install --no-index --find-links` → 冒烟 import；③ 版本升级用 diff 清单出增量包；④ 留"逃生舱"：万一离线端缺包，内网镜像可临时补传。

```python
# wheelhouse 容量与增量账：平台矩阵 x 依赖冻结
# 基线：Python 3.9+ 标准库；真实打包 pip download --only-binary=:all:
from dataclasses import dataclass


@dataclass
class Wheelhouse:
    core_wheels_mb: float           # 全量（单平台）
    platform_matrix: int            # 目标平台数（python版本x架构）
    full_matrix_mb: float           # 全平台盲打体积


def delivery_size(wh: Wheelhouse, platforms: int) -> float:
    return wh.core_wheels_mb  # 锁定平台后与矩阵无关


def increment_size(wh: Wheelhouse, changed_ratio: float) -> float:
    return wh.core_wheels_mb * changed_ratio


def naive_pitfalls() -> list[str]:
    return [
        "未锁平台：全矩阵体积膨胀 10~20 倍",
        "sdist 依赖：离线端无编译器直接失败",
        "离线端重新解析依赖：resolver 行为漂移",
        "未带哈希清单：完整性无法校验",
    ]


def main() -> None:
    wh = Wheelhouse(core_wheels_mb=1800, platform_matrix=6, full_matrix_mb=24000)
    # 精准拉取：单平台体积固定；naive 全矩阵 24GB 不可交付
    assert delivery_size(wh, platforms=1) == 1800
    assert wh.full_matrix_mb / wh.core_wheels_mb > 10
    print(f"锁定平台交付 {delivery_size(wh, 1)/1024:.1f}GB；全矩阵盲打 {wh.full_matrix_mb/1024:.0f}GB")

    # 增量更新：版本清单 diff 10% 变化
    inc = increment_size(wh, 0.1)
    assert inc == 180
    print(f"增量包 {inc:.0f}MB vs 全量 1800MB，交付/校验成本降一个量级")

    # naive 翻车点必须在打包端全部前移解决
    for p in naive_pitfalls():
        assert p
    print("OK: only-binary 提前暴露无 wheel 依赖, require-hashes 消灭离线端解析漂移")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么离线端要 `--require-hashes` 而不是让它自己解析依赖？
→ 一句话提示：离线端 pip 版本/缓存状态不同，resolver 可能选出不同版本或因找不到某传递依赖而失败；带哈希的冻结清单让安装变成"按清单校验+复制"，把解析留在有网的打包端完成。

**追问 2**：某些依赖只发 sdist 怎么办？
→ 一句话提示：在打包端自建 wheel（`pip wheel` 需要匹配目标平台的编译环境，常用容器交叉构建），把二进制化前移到交付前；实在无法二进制化的依赖要在选型评审时就替换——离线环境现场编译不是可交付方案。

## 背诵要点
- 三本账：体积（锁平台 `--platform --python-version --only-binary=:all:`，全矩阵盲打膨胀 10~20 倍）、平台（离线端只能装 wheel，sdist 依赖必须打包端二进制化）、增量（按冻结清单 diff 出增量包）。
- 交付铁律：`--require-hashes` 哈希清单 + `--no-index --find-links`，解析留在打包端、离线端只校验安装。
- 形态选择：单次交付 zip，持续交付内网镜像（devpi/Nexus）；install.sh 要做哈希校验 + 冒烟 import。

## 复盘追问
- 为什么"打包端能装、离线端装不上"是常态？提示：打包端有网络缓存兜底与宽松 resolver，离线端任何缺失都是硬失败；唯一对策是打包端模拟离线（`--no-index` 本地试装）完成闭环验证再交付。
- 多个交付项目共享一台内网镜像时，容量与治理账怎么变？提示：镜像仓成为共享基础设施——需要保留策略/清理任务/权限治理，一次建设的成本摊到多项目，但运维责任也要显式交接。
