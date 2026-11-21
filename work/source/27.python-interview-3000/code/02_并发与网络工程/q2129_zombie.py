# -*- coding: utf-8 -*-
"""僵尸进程: 子进程死后没人 wait 的后果。

- 子进程先死, 内核保留其退出状态等父进程 wait, 这个残壳就是僵尸 Z;
- 僵尸不占内存但占用 pid 与进程表槽位, 大量僵尸会耗尽 pid;
- waitpid 收尸即可清除; 父进程先死则由 init/launchd 接管收尸。
"""
import os
import subprocess
import time


def zombie_stat(pid):
    r = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)],
                       capture_output=True, text=True)
    return r.stdout.strip() or "<gone>"


def main():
    # 场景一: 子进程先死, 父进程迟迟不收尸
    pid = os.fork()
    if pid == 0:
        os._exit(7)                    # 子进程立刻退出, 状态无人认领
    time.sleep(0.2)
    print("子进程 %d 死后 stat: %s (Z 开头即僵尸)" % (pid, zombie_stat(pid)))
    _, status = os.waitpid(pid, 0)     # 收尸
    print("waitpid 拿到退出状态:", os.waitstatus_to_exitcode(status))
    print("收尸后 stat:", zombie_stat(pid))

    # 场景二: WNOHANG 轮询是服务端管理子进程的常规手法
    pid2 = os.fork()
    if pid2 == 0:
        time.sleep(0.3)
        os._exit(0)
    r = os.waitpid(pid2, os.WNOHANG)
    print("存活时 WNOHANG 返回:", r, "(0 表示还没退)")
    time.sleep(0.5)
    r2 = os.waitpid(pid2, os.WNOHANG)
    print("退出后 WNOHANG 返回:", r2, "(pid 与状态一次取走)")
    print("最终 stat:", zombie_stat(pid2))


if __name__ == "__main__":
    main()
