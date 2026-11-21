"""磁盘用量:disk_usage 与最小 du 实现。"""
import os
import shutil
import tempfile


def du(path):
    """目录总字节数:walk 累加,不跟随目录符号链接。"""
    total = 0
    for root, _dirs, files in os.walk(path):
        for name in files:
            try:
                total += os.path.getsize(os.path.join(root, name))
            except OSError:
                pass
    return total


if __name__ == "__main__":
    usage = shutil.disk_usage("/")
    print(f"磁盘: 总 {usage.total / 2**30:.0f} GiB, "
          f"已用 {usage.used / 2**30:.0f} GiB, "
          f"余 {usage.free / 2**30:.0f} GiB")

    tmp = tempfile.mkdtemp()
    with open(os.path.join(tmp, "a.bin"), "wb") as f:
        f.write(b"\0" * 4096)
    print("临时目录体积:", du(tmp), "字节")
