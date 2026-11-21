---
title: [Q2814] 分区 staging 交换的原子提交
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2814 · 分区 staging 交换的原子提交

> 难度:★★★☆ | 标签:重跑, 原子提交

**问**:面试官:重跑分区写到一半进程挂了,读者会看到半成品吗?

**答**:不会,前提是"staging 加 rename"。流程:先写旁名 .staging_分区 文件,校验(行数下限等)通过后 os.replace 原子换名到 final;校验不过就删除 staging,final 分毫不动。实测:合法重跑提交成功,final 从 2 行变 3 行;非法重跑(空文件)在校验处被拒,残留 staging 清理干净,final 保持新数据 3 行——读者任何时刻看到的都是完整旧版或完整新版,绝无半成品。os.replace 在同一文件系统内是原子操作,这是文件系统上最便宜的原子性;两个注意点:staging 与 final 必须同一挂载点,跨文件系统 rename 会退化成拷贝;校验必须前移到 rename 之前,坏分区根本不该进正式路径。

```python
# file: code/05_数据分析与工程化/q2814_staging_swap.py
"""分区 staging 交换的原子提交: 校验不过就丢弃, 旧分区毫发无损"""
import os
import tempfile

OLD_CONTENT = "dt,amt\n2026-11-01,100\n2026-11-01,101\n"
NEW_GOOD = "dt,amt\n2026-11-01,200\n2026-11-01,201\n2026-11-01,202\n"
NEW_EMPTY = ""


def publish_partition(base, part, content, min_rows):
    """写 staging -> 校验 -> 原子换名; 任一步失败, final 保持旧内容"""
    final = os.path.join(base, f"{part}.csv")
    staging = os.path.join(base, f".staging_{part}.csv")
    with open(staging, "w") as f:
        f.write(content)
    try:
        with open(staging) as f:
            rows = sum(1 for _ in f) - 1  # 去掉表头
        if rows < min_rows:
            raise ValueError(f"staging 行数 {rows} 低于下限 {min_rows}")
        os.replace(staging, final)  # 同一文件系统内 rename 是原子的
        return True, rows
    except ValueError as e:
        os.remove(staging)
        return False, str(e)


if __name__ == "__main__":
    base = tempfile.mkdtemp(prefix="q2814_")
    final = os.path.join(base, "2026-11-01.csv")
    with open(final, "w") as f:
        f.write(OLD_CONTENT)
    ok, info = publish_partition(base, "2026-11-01", NEW_GOOD, min_rows=2)
    with open(final) as f:
        now = f.read()
    print(f"合法重跑: 提交 {ok}, 新行数 {info}, 现文件行数 {now.count(chr(10)) - 1}")
    assert ok and now == NEW_GOOD, "合法数据应原子替换成功"
    ok2, info2 = publish_partition(base, "2026-11-01", NEW_EMPTY, min_rows=2)
    with open(final) as f:
        kept = f.read()
    leftover = [n for n in os.listdir(base) if n.startswith(".staging")]
    print(f"非法重跑: 提交 {ok2}, 原因 {info2!r}, final 内容保留旧行数 {kept.count(chr(10)) - 1}, 残留 staging {leftover}")
    assert not ok2 and kept == NEW_GOOD, "校验失败后 final 应保持新数据不变"
    assert leftover == [], "被拒绝的 staging 必须清理干净"
    print("要点: 先写旁名 staging 再 rename, 是文件系统上能拿到的最便宜的原子性; 校验前移让坏分区进不来")
```

**追问**:
- 追问 1:数据库表的等价做法?—— 写影子表后 rename/swap 分区,或分区级事务加写后读校验,思路相同。
- 追问 2:残留在 staging 的僵尸文件谁清理?—— 启动时扫 staging 前缀文件,超过租约时间即删,防崩溃残留累积。
