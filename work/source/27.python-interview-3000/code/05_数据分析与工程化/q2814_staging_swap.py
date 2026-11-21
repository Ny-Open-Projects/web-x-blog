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
