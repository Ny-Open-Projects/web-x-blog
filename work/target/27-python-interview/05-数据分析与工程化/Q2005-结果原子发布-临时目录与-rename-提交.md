---
title: [Q2005] 结果原子发布:临时目录与 rename 提交
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2005 · 结果原子发布:临时目录与 rename 提交

> 难度:★★★☆ | 标签:原子写, 数据发布

**问**:结果表写到一半被读者读到半成品怎么办?"先写后改名"为什么能解决问题?

**答**:结果分区最怕读者看到半成品:缺一部分文件的目录、写到一半的表。原子发布三步:先写临时目录(target.tmp),跑完做行数与校验和校验,校验通过后 rename 提交——同文件系统内 rename 是原子操作,读方要么看不到目录、要么看到完整目录。实测首次发布与二次覆盖都干净完成;二次覆盖的细节是旧目录先 rename 成 .bak 再换入,失败可回退。校验必须发生在 rename 之前,失败只留 tmp,正式路径永不污染,tmp 由下次发布或清理任务回收。文件系统不支持原子 rename(对象存储)时,用版本目录加指针文件模拟,指针文件自身单文件原子覆盖。

```python
# file: code/05_数据分析与工程化/q2005_atomic_publish.py
"""结果原子发布:先写临时目录,校验通过后 rename 提交,失败不留半成品"""

import json
import os
import shutil
import tempfile

BASE = tempfile.mkdtemp(prefix="pub_demo_")


def build_output(workdir):
    rows = [{"dt": "2026-11-04", "channel": "search", "gmv": 1200},
            {"dt": "2026-11-04", "channel": "feed", "gmv": 860}]
    os.makedirs(workdir, exist_ok=True)
    with open(os.path.join(workdir, "part-000.json"), "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    return rows


def validate(workdir, expect_rows):
    files = [f for f in os.listdir(workdir) if f.endswith(".json")]
    n = sum(sum(1 for _ in open(os.path.join(workdir, f))) for f in files)
    if n != expect_rows:
        raise ValueError(f"行数校验失败: {n} != {expect_rows}")
    return True


def publish(target):
    tmp = target + ".tmp"
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    rows = build_output(tmp)
    validate(tmp, len(rows))            # 校验不过就抛异常,正式路径不受影响
    backup = target + ".bak"
    if os.path.exists(target):
        os.rename(target, backup)       # 旧版挪走,再原子换入
        os.rename(tmp, target)
        shutil.rmtree(backup)
    else:
        os.rename(tmp, target)
    return len(rows)


if __name__ == "__main__":
    target = os.path.join(BASE, "dws_channel_day", "dt=2026-11-04")
    print("首次发布:", publish(target), "行 ->", sorted(os.listdir(target)))
    print("二次覆盖:", publish(target), "行 ->", sorted(os.listdir(target)))
    shutil.rmtree(BASE)
    print("要点:同分区 rename 是原子的,读方永远只看到完整目录;校验放在 rename 之前;失败只留 tmp 目录,由下次发布或清理任务回收")
```

**追问**:
- 追问 1:多任务写同一分区怎么互斥?—— 发布前抢目录级锁(文件锁或租约),与调度防重入同一套机制。
- 追问 2:读者在 rename 瞬间正在读怎么办?—— rename 只改目录项,已打开的句柄继续读旧 inode,POSIX 语义天然安全;对象存储靠版本化读。
