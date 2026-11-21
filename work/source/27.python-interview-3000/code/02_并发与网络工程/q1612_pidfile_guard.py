"""PID 文件与单实例守护: 陈旧 PID 接管。

防重复启动的轻量方案: 启动时 O_CREAT|O_EXCL 独占创建 PID 文件。
- 文件已存在: 读出 PID, 用 kill(pid, 0) 探活 -> 活着就拒绝启动;
- PID 已死(ESRCH): 文件是上次崩溃留下的垃圾 -> 接管;
- EPERM: 进程活着但无权发信号, 同样算活着。
注意 kill(pid, 0) 检查与 unlink 之间存在竞态窗口, 严格场景要配合文件锁。
"""
import errno
import os
import subprocess
import tempfile


class PIDFileBusy(Exception):
    def __init__(self, pid):
        super().__init__("已有实例在跑, PID=%d" % pid)
        self.pid = pid


def read_pid(path):
    with open(path) as f:
        text = f.read().strip()
    return int(text) if text else 0


def pid_alive(pid):
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)                 # 信号 0: 只探活, 不发送
        return True
    except OSError as e:
        return e.errno == errno.EPERM   # 活着但无权探查, 也算活


def acquire(path):
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        with os.fdopen(fd, "w") as f:
            f.write(str(os.getpid()))
        return "acquired"
    except FileExistsError:
        pid = read_pid(path)
        if pid_alive(pid):
            raise PIDFileBusy(pid)
        os.unlink(path)                 # 陈旧 PID: 清理垃圾后接管
        print("陈旧 PID=%d 已死, 接管 PID 文件" % pid)
        return acquire(path)


def main():
    path = os.path.join(tempfile.mkdtemp(prefix="q1612_"), "app.pid")

    r1 = acquire(path)
    print("第一次启动:", r1)
    assert r1 == "acquired"
    assert read_pid(path) == os.getpid()

    try:
        acquire(path)
        raise AssertionError("重复启动应被拒绝")
    except PIDFileBusy as e:
        print("第二次启动被拒:", e)

    # 制造一个真实的"已死 PID": 起一个立刻退出的子进程
    p = subprocess.Popen(["/bin/sleep", "0"])
    p.wait()
    dead_pid = p.pid
    assert not pid_alive(dead_pid), "该 PID 应已死亡"
    with open(path, "w") as f:
        f.write(str(dead_pid))          # 模拟上次崩溃留下的陈旧 PID 文件
    r3 = acquire(path)
    print("陈旧文件后的启动:", r3)
    assert r3 == "acquired", "陈旧 PID 文件应被接管"

    os.unlink(path)
    print("结论: O_EXCL 抢占 + kill(pid,0) 探活 + 死 PID 接管, 三段式单实例")


if __name__ == "__main__":
    main()
