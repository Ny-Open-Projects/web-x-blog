"""调度防重入:文件锁原子创建 + 租约过期接管,进程崩溃后锁不会永久卡死"""

import os
import tempfile
import time

LOCK_DIR = tempfile.mkdtemp(prefix="q1732_")
LEASE_SECONDS = 2.0


def acquire(name, ttl=LEASE_SECONDS):
    path = os.path.join(LOCK_DIR, name + ".lock")
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        if time.time() - os.path.getmtime(path) > ttl:  # 租约过期,尝试接管
            try:
                os.unlink(path)
            except FileNotFoundError:
                return None  # 别的进程刚好接走
            return acquire(name, ttl)
        return None
    else:
        os.write(fd, f"{time.time()}|owner".encode())
        os.close(fd)
        return path


def release(path):
    if path and os.path.exists(path):
        os.unlink(path)


if __name__ == "__main__":
    lock = acquire("nightly_job")
    print("第一次获锁:", bool(lock))
    print("重入获锁(应失败):", acquire("nightly_job"))
    print("等待租约过期 ...")
    time.sleep(LEASE_SECONDS + 0.1)
    lock2 = acquire("nightly_job")
    print("租约过期后接管:", bool(lock2))
    release(lock2)
    print("要点:O_EXCL 创建即原子加锁;锁文件时间戳当租约,超过 TTL 才允许接管;接管与释放都要容忍竞态,宁可少跑不可重跑")
