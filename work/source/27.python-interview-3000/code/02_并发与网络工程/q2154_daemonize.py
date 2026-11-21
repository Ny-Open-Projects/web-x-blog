# -*- coding: utf-8 -*-
"""守护进程化: setsid 与双重 fork。

- 一次 fork + setsid 摆脱终端; 第二次 fork 让 daemon 永远不是会话首进程;
- 会话首进程才可能意外拿回控制终端, 二次 fork 是历史上防这一手的;
- 实测: 孙进程 ppid 变 1 由 launchd 收养, 自己是自己的会话首。
"""
import os
import subprocess
import tempfile
import time

pidfile = tempfile.mktemp(prefix="q2154_pid_")
beatfile = tempfile.mktemp(prefix="q2154_beat_")


def ps_field(pid, field):
    r = subprocess.run(["ps", "-o", field + "=", "-p", str(pid)],
                       capture_output=True, text=True)
    return r.stdout.strip()


def main():
    pid = os.fork()
    if pid == 0:
        os.setsid()                       # 第一次: 自成会话, 脱离终端
        pid2 = os.fork()                  # 第二次: 甩掉会话首身份
        if pid2 == 0:
            devnull = os.open(os.devnull, os.O_RDWR)
            os.dup2(devnull, 0)           # 三件套: 断开 stdio 与终端
            os.dup2(devnull, 1)
            os.dup2(devnull, 2)
            for i in range(8):
                with open(beatfile, "a") as bf:
                    bf.write("beat-%d\n" % i)
                time.sleep(0.15)
            os._exit(0)
        with open(pidfile, "w") as pf:    # 中间进程把孙 pid 交给父进程
            pf.write(str(pid2))
        os._exit(0)

    os.waitpid(pid, 0)                    # 原始子进程立刻退出
    time.sleep(0.2)
    gpid = int(open(pidfile).read())
    print("孙进程 pid:", gpid)
    print("收养检查: ppid =", ps_field(gpid, "ppid"),
          "(1 表示由 launchd 收养)")
    sid = os.getsid(gpid)
    print("会话检查: sid =", sid, "| 自身 pid =", gpid,
          "(sid 是中间进程, 孙进程不是会话首, 永远拿不回终端)")
    time.sleep(0.4)                       # daemon 还在心跳
    try:
        os.kill(gpid, 0)
        alive = True
    except OSError:
        alive = False
    print("运行中探活:", alive, "| 心跳:",
          open(beatfile).read().split()[-1])
    os.kill(gpid, 15)                     # 收工
    time.sleep(0.3)
    print("SIGTERM 后 stat:", ps_field(gpid, "stat") or "<gone>",
          "-> 已由收养者收尸, 无僵尸残留")
    for p in (pidfile, beatfile):
        try:
            os.remove(p)
        except OSError:
            pass


if __name__ == "__main__":
    main()
