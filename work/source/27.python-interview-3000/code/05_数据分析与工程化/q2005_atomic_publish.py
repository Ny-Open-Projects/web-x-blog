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
