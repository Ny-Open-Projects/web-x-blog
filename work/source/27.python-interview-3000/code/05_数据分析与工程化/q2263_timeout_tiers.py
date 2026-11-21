"""管道任务的超时分级: 软超时告警, 硬超时终止"""

from collections import namedtuple

Task = namedtuple("Task", "name cls seconds")
TASKS = [
    Task("ods_sync", "快任务", 3),
    Task("dwd_build", "慢任务", 95),
    Task("ads_agg", "快任务", 8),
    Task("dwd_build", "慢任务", 200),   # 注入一个超硬超时的任务
]
POLICY = {"快任务": (5, 15), "慢任务": (60, 180)}   # 类别 -> 软超时秒, 硬超时秒


def evaluate(task):
    soft, hard = POLICY[task.cls]
    if task.seconds > hard:
        return "硬超时", f"超过硬阈值 {hard}s, 终止进程保留现场并升级告警"
    if task.seconds > soft:
        return "软超时", f"超过软阈值 {soft}s, 发告警继续观察不杀进程"
    return "正常", f"{task.seconds}s 在 [{soft}s, {hard}s] 内"


if __name__ == "__main__":
    for t in TASKS:
        state, action = evaluate(t)
        print(f"{t.name:<10} {t.cls} 用时 {t.seconds:>3}s -> {state}: {action}")
    print("要点: 软超时是观察点硬超时是止损点; 阈值按类别按基线 P99 定; 频繁触软是基线劣化的早期信号")
