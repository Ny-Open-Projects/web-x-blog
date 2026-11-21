"""子进程看门狗: 崩溃退避重启。

守护子进程的三条纪律:
- 崩溃重启带指数退避, 别把 CPU 烧成重启风暴;
- 挂死的子进程用超时杀, 不能无限等;
- 重启次数有上限, 超过就放弃并告警——程序性 bug 重启一百次也没用。
"""
import subprocess
import sys
import time

CRASHY = ("import sys, time\n"
          "n = int(sys.argv[1])\n"
          "if n < 2:\n"
          "    sys.exit(1)\n"          # 前两次快速崩溃
          "time.sleep(0.2)\n"
          "print('done')\n")
HANGING = "import time\ntime.sleep(30)\n"


def supervise(argv, wait_timeout, max_restarts, backoff=0.15):
    events = []
    attempt = 0
    delay = backoff
    while attempt <= max_restarts:
        events.append(("start", attempt))
        try:
            p = subprocess.run(argv + [str(attempt)],
                               capture_output=True, timeout=wait_timeout)
            code, out = p.returncode, p.stdout.decode().strip()
            events.append(("exit", attempt, code))
        except subprocess.TimeoutExpired:
            code, out = None, ""
            events.append(("timeout-kill", attempt))
        if code == 0:
            events.append(("success", attempt, out))
            return events, True
        if attempt == max_restarts:
            break
        attempt += 1
        events.append(("backoff", round(delay, 2)))
        time.sleep(delay)
        delay = min(delay * 2, 1.0)
    events.append(("giveup", attempt))
    return events, False


def main():
    # 场景 1: 间歇崩溃, 退避两次后成功
    events, ok = supervise([sys.executable, "-c", CRASHY],
                           wait_timeout=3.0, max_restarts=4)
    for e in events:
        print("  ", e)
    print("间歇崩溃场景: 最终成功 =", ok)
    assert ok, "两次崩溃后第三次应成功"
    starts = sum(1 for e in events if e[0] == "start")
    assert starts == 3, "应恰好启动 3 次"
    backoffs = [e for e in events if e[0] == "backoff"]
    assert len(backoffs) == 2 and backoffs[0][1] < backoffs[1][1], (
        "重启之间必须有指数增长的退避")

    # 场景 2: 挂死进程, 超时杀 + 达到上限放弃
    events, ok = supervise([sys.executable, "-c", HANGING],
                           wait_timeout=0.4, max_restarts=1)
    for e in events:
        print("  ", e)
    print("挂死场景: 最终成功 =", ok)
    assert not ok, "挂死进程重启一次后仍挂死, 应放弃"
    timeouts = sum(1 for e in events if e[0] == "timeout-kill")
    assert timeouts == 2, "两次都应被超时杀掉"

    print("结论: 退避 + 超时杀 + 上限放弃, 看门狗自己也不能变成风暴源")


if __name__ == "__main__":
    main()
