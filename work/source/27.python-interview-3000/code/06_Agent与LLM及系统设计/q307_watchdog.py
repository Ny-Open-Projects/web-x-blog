import subprocess
import time


def is_alive(proc: subprocess.Popen) -> bool:
    return proc.poll() is None


def watchdog(command: list, max_restarts: int = 3, backoff: float = 1.0,
             max_observations: int = 60):
    restarts = 0
    proc = subprocess.Popen(command)
    observations = 0
    while True:
        observations += 1
        if observations > max_observations:  # 保险丝:观察超限直接告警退出
            print("[alert] watchdog observation budget exhausted, give up")
            proc.terminate()
            return
        time.sleep(1)  # 观察间隔
        if is_alive(proc):
            restarts = 0  # 稳定运行后重置计数
            continue
        restarts += 1
        print(f"process died, restart {restarts}")
        if restarts > max_restarts:
            print("[alert] too many restarts, give up and page human")
            break
        time.sleep(backoff * (2 ** (restarts - 1)))  # 退避防重启风暴
        proc = subprocess.Popen(command)


if __name__ == "__main__":
    import sys
    # 演示:被守护的进程一启动就崩,退避重启 2 次后放弃并告警(有界,可自动收尾)
    victim = [sys.executable, "-c", "import sys; sys.exit(1)"]
    watchdog(victim, max_restarts=2, backoff=0.1)
    print("演示结束:watchdog 已放弃并告警,生产中这里应触发人工介入")
