"""fcntl 文件锁:保证脚本单实例运行,标准库可运行。"""
import fcntl
import os
import tempfile
import time


class SingleInstance:
    def __init__(self, name="myjob"):
        self.lock_path = os.path.join(tempfile.gettempdir(), f"{name}.lock")
        self.fd = None

    def __enter__(self):
        self.fd = open(self.lock_path, "w")
        try:
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  # 非阻塞排他锁
        except BlockingIOError:
            raise RuntimeError("已有实例在运行, 退出") from None
        self.fd.write(str(os.getpid()))
        self.fd.flush()
        return self

    def __exit__(self, *exc):
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        self.fd.close()


if __name__ == "__main__":
    with SingleInstance("demojob"):
        print(f"pid {os.getpid()} 获得锁, 开始干活")
        # 模拟第二个实例尝试进入
        try:
            with SingleInstance("demojob"):
                print("不可能执行到这里")
        except RuntimeError as e:
            print("第二个实例被拒绝:", e)
        time.sleep(0.1)
    print("锁已释放, 下一轮 cron 可正常进入")
