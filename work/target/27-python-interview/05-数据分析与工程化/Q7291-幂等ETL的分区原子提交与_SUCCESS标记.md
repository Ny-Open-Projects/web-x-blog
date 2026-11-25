---
title: "[Q7291] 幂等 ETL 的原子提交：分区覆盖、_SUCCESS 标记与 os.replace 的边界"
date: 2026-11-25
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7291 · 幂等 ETL 的原子提交：分区覆盖、_SUCCESS 标记与 os.replace 的边界

难度：P7 ｜ 标签：ETL、幂等、分区覆盖、_SUCCESS、os.replace、原子提交、重跑

基线：库知识卡，代码用标准库模拟——用 tempfile 目录 + `os.replace` 复现提交协议与失败窗口，不依赖 Spark/Hive。

**问**：一个日分区 ETL 任务重跑时直接往 `dt=2026-11-25/` 里覆盖写，跑到 60% 进程被 OOM kill，下游 8 点的报表读到"3 个 part 只有 1 个"，当天数据少了一半。后来改成"先写临时目录、成功后再改名"，但重跑同一分区时 `os.replace` 直接报错；再后来加了 `_SUCCESS` 文件，运维说"有标记就是成功"，结果标记写了、数据还没落盘。分区覆盖到底怎么做才是原子的？`_SUCCESS` 能保证什么、不能保证什么？

**答**：

- **结论**：可靠的提交协议是 **staging + 完成标记 + 原子改名**，但每一步的保证都有边界。① **staging**：所有数据写到一个不会被读者看到的临时目录（同文件系统、同分区），失败就丢弃，目标分区始终是"上一次成功"的完整版本；② **`_SUCCESS`**：写给读者的"可读"信号，但必须**在数据写完并 fsync 之后**再写，否则标记可见而数据还在 page cache，断电后就是"有标记的空分区"；③ **`os.replace(tmp, final)`**：POSIX 下同文件系统内的 `rename` 是原子的（读者要么看到旧目录、要么看到新目录，不会看到半份），但有两个硬边界——**跨设备会 `EXDEV`**（临时目录必须与目标同盘），**目标是已存在的非空目录会 `ENOTEMPTY`**（不能直接"覆盖"一个已有分区）。
- **取舍**：因为"覆盖非空目录"不是原子操作，分区重跑有三条路。① **先删后改名**：`rm -rf final && mv tmp final`，中间有一个读者看到"分区不存在"的窗口，只适合能容忍短暂缺口的场景；② **版本目录 + 指针**：写 `dt=.../v=1712345678/`，再用 `os.replace` 原子替换一个**指针文件**（内容是新版本路径），读者先读指针再读数据，旧版本保留到清理，零缺口但要多一份存储；③ **表格式的事务提交**（Iceberg/Hudi/Delta 的 manifest）：把"哪些文件属于这个分区"做成原子元数据更新，能力最强、依赖也最重。多数团队用②就够了。
- **实战**：一次重跑把分区写坏，根因是 `df.to_parquet(final_path, mode="overwrite")` 在文件级别删了再写，中途失败留下部分文件。改造后：写 `_staging/<run_id>/`，每个 part 写完 `flush + os.fsync`，最后写 `_SUCCESS`（内容含行数与校验和），再 `os.replace` 到 `dt=.../v=<run_id>`，最后原子替换 `CURRENT` 指针。下游读取统一走"读 CURRENT → 检查 _SUCCESS → 校验行数"，重跑三次结果校验和一致，缺口归零。

下面把提交协议、失败窗口与 `os.replace` 的两个边界跑一遍。

```python
# 分区原子提交: staging + _SUCCESS + rename, 以及 ENOTEMPTY/EXDEV 边界
import hashlib
import os
import tempfile

ROOT = tempfile.mkdtemp(prefix="etl_")
FINAL = os.path.join(ROOT, "dt=2026-11-25")


def build(staging, rows):
    os.makedirs(staging, exist_ok=True)
    part = os.path.join(staging, "part-0.csv")
    with open(part, "w") as f:
        f.writelines(f"{r}\n" for r in rows)
        f.flush()
        os.fsync(f.fileno())              # 先落盘, 再允许写标记
    digest = hashlib.sha256(open(part, "rb").read()).hexdigest()
    return digest, len(rows)


def mark_success(staging, digest, n):
    with open(os.path.join(staging, "_SUCCESS"), "w") as f:
        f.write(f"rows={n}\nsha256={digest}\n")
        f.flush()
        os.fsync(f.fileno())


# 1) 失败重跑: 数据写完但没写 _SUCCESS, 不提交
st1 = os.path.join(ROOT, "_staging_run1")
d1, n1 = build(st1, [1, 2, 3])
assert not os.path.exists(FINAL), "未提交时读者看不到任何东西"
print(f"[1] 失败窗口: staging 有数据, 目标不存在 -> 读者看到 0 行 (不是半份)")

# 2) 成功: 写标记后原子改名
mark_success(st1, d1, n1)
os.replace(st1, FINAL)
print(f"[2] 提交后: {sorted(os.listdir(FINAL))}, _SUCCESS={os.path.exists(os.path.join(FINAL, '_SUCCESS'))}")
assert os.path.exists(os.path.join(FINAL, "_SUCCESS"))

# 3) 重跑同分区: 目标非空, rename 失败(ENOTEMPTY)
st2 = os.path.join(ROOT, "_staging_run2")
d2, n2 = build(st2, [1, 2, 3])
mark_success(st2, d2, n2)
try:
    os.replace(st2, FINAL)
    replaced = True
except OSError as e:
    replaced = False
    print(f"[3] 重跑直接覆盖: {type(e).__name__} (errno={e.errno}) — 非空目录不能原子替换")
assert not replaced

# 4) 版本目录 + 指针: 重跑写新版本, 原子替换指针
v1 = FINAL
v2 = os.path.join(ROOT, "dt=2026-11-25", "v=2")
os.makedirs(os.path.dirname(v2), exist_ok=True)
os.replace(st2, v2)                      # v2 不存在, rename 成功
pointer = os.path.join(ROOT, "CURRENT")
with open(pointer + ".tmp", "w") as f:
    f.write(v2)
os.replace(pointer + ".tmp", pointer)    # 文件级原子替换
print(f"[4] 指针 -> {open(pointer).read()}, 旧版本仍可读: {os.path.exists(v1)}")
assert open(pointer).read() == v2 and os.path.exists(v1)
assert d1 == d2, "同输入重跑校验和必须一致"
print("    → 实测 幂等 = 同输入同输出 + 原子可见性; _SUCCESS 只保证'可读', 不保证'已落盘'")
```

**追问一**：为什么 `_SUCCESS` 不能只在目录里 `touch` 一下就完事？—— `touch` 只创建目录项，内容和数据都可能还在 page cache；断电/宿主机崩溃后会出现"标记存在、part 缺失或截断"的分区。正确顺序是：写 part → `flush` + `fsync`（必要时对目录也 fsync，保证目录项持久）→ 写 `_SUCCESS`（内容建议带行数/校验和，便于读者验证）→ fsync → rename。`_SUCCESS` 的语义是"**数据已经完整且可读**"，不是"任务跑过了"；如果标记里带行数与校验和，读者可以在打开文件前先做一次廉价的一致性检查。

**追问二**：`os.replace` 在什么情况下不是原子的？跨盘复制为什么危险？—— `os.replace` 底层是 `rename(2)`，**只有同一文件系统内**才是原子的；源和目标是不同挂载点（比如临时目录在 `/tmp`、数据在另一块盘）时，Python 会退化成"复制 + 删除"（或直接抛 `EXDEV`，取决于实现），复制过程中目标可能已经出现半份内容。所以 staging 目录必须与目标分区**同盘同文件系统**，并且不要用 `/tmp` 当 staging（很多环境 `/tmp` 是 tmpfs）。另一个边界是网络文件系统（NFS）：`rename` 的原子性依赖服务端实现，跨客户端的可见性有延迟，"原子"不能按本地 POSIX 假设。

## 背诵要点

- 提交协议：写 staging（同文件系统）→ fsync 数据 → 写 `_SUCCESS`（带行数/校验和）→ fsync → `os.replace` 到最终路径。
- `os.replace` 只在同文件系统原子；跨设备退化为复制（或 EXDEV），目标非空目录会 `ENOTEMPTY`，不能直接覆盖已有分区。
- 分区重跑用"版本目录 + 原子替换指针"实现零缺口；幂等 = 同输入校验和一致 + 读者只看到完整版本。

## 复盘追问

- 重跑同一分区为什么不能直接 `os.replace`？（POSIX rename 要求目标为空或不存在；非空目录会 ENOTEMPTY，先删再换会有缺口）
- `_SUCCESS` 存在但下游读不到数据，可能是什么顺序问题？（标记先于数据 fsync 写入；标记只表示"任务写过"，不表示"数据持久化"）
