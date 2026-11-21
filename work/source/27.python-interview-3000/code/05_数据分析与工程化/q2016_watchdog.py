"""子进程超时看门狗:超时兜底终止,保留已产生的输出现场"""

import subprocess
import sys

CHILD = "print('step1 done', flush=True); import time; time.sleep(30)"


def run_with_watchdog(cmd, timeout):
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=timeout)
        return proc.returncode, proc.stdout
    except subprocess.TimeoutExpired as e:
        out = e.stdout or ""
        if isinstance(out, bytes):
            out = out.decode("utf-8", "ignore")
        return "TIMEOUT-KILL", out


if __name__ == "__main__":
    code, out = run_with_watchdog([sys.executable, "-c", CHILD], timeout=2)
    print(f"超时任务: 状态 {code}, 现场输出: {out.strip()!r}")
    code, out = run_with_watchdog([sys.executable, "-c", "print('fast ok')"],
                                  timeout=5)
    print(f"正常任务: 状态 {code}, 输出 {out.strip()!r}")
    print("要点:所有外部调用必须带 timeout;超时先杀再留现场,部分输出是排查第一证据;timeout 值按任务耗时基线的 P99 加余量,而不是统一 30 秒")
