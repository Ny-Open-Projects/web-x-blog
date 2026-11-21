# -*- coding: utf-8 -*-
"""被信号杀死的 returncode: 负数的含义。

- 进程被信号 N 杀死时, Python 侧 returncode 是 -N, 这是 waitpid 的原始语义;
- terminate() 发 SIGTERM, kill() 发 SIGKILL, SIGKILL 不可捕获不可忽略;
- 退出码判定的完整规则: 正数是 exit(n), 负数是被信号 N 终止。
"""
import subprocess
import sys
import time


def main():
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    time.sleep(0.3)
    p.terminate()             # SIGTERM: 可捕获, 进程可先收尾
    rc = p.wait()
    print("terminate 后 returncode:", rc, "-> 被信号 %d 终止" % -rc)

    p2 = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    time.sleep(0.3)
    p2.kill()                 # SIGKILL: 无 opportunity 收尾
    rc2 = p2.wait()
    print("kill 后 returncode:", rc2, "-> 被信号 %d 终止" % -rc2)

    # 自捕获 SIGTERM 的子进程: 干净退出, returncode 为正
    p3 = subprocess.Popen([sys.executable, "-c",
                           "import signal,sys;"
                           "signal.signal(signal.SIGTERM,"
                           "lambda s,f:(print('graceful'),sys.exit(0)));"
                           "import time; time.sleep(30)"],
                          text=True)
    time.sleep(0.5)
    p3.terminate()
    rc3 = p3.wait()
    print("自捕获 SIGTERM 后 returncode:", rc3, "-> 0 是干净退出")
    print("编排规则: rc==0 成功; rc>0 业务失败; rc<0 信号终止需按 -rc 分诊")


if __name__ == "__main__":
    main()
