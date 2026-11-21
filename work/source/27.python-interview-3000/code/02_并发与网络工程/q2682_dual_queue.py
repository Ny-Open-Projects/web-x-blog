# -*- coding: utf-8 -*-
"""双队列加权轮询: 优先级的比例保证, 而非绝对抢占。

- 严格优先级: 高队列为空才轮到低队列, 低优先级延迟不可控;
- 加权轮询 3:1: 每抢 3 个名额就强制留给低队列 1 个, 低延迟有上界;
- 单堆优先级队列只保证顺序, 双队列才保证比例。
"""
from collections import deque


def simulate(jobs, policy):
    """jobs: (到达时刻, 优先级 0高/1低, 时长, 名字); 返回 (名字, 延迟)。"""
    hi, lo = deque(), deque()
    t = 0.0
    i = 0
    picks = 0
    done = []
    while i < len(jobs) or hi or lo:
        while i < len(jobs) and jobs[i][0] <= t:
            arr, prio, dur, name = jobs[i]
            (hi if prio == 0 else lo).append(jobs[i])
            i += 1
        if not hi and not lo:
            t = jobs[i][0]                       # 空转: 快进到下一到达
            continue
        if policy == "strict":
            q = hi if hi else lo                 # 高队列非空就绝不看低队列
        else:                                    # weighted 3:1
            if hi and lo:
                q = lo if picks % 4 == 3 else hi  # 每 4 拍里第 4 拍给低队列
            else:
                q = hi or lo
        arr, prio, dur, name = q.popleft()
        t += dur
        picks += 1
        done.append((name, t - arr))
    return done


def build_jobs():
    jobs = []
    for k in range(12):                          # 高优先级: 每 0.5s 一个, 每个 0.45s
        jobs.append((round(k * 0.5, 2), 0, 0.45, "hi-%d" % k))
    for k in range(6):                           # 低优先级: 每 2s 一个, 每个 0.5s
        jobs.append((round(0.3 + k * 2.0, 2), 1, 0.5, "lo-%d" % k))
    jobs.sort(key=lambda j: j[0])
    return jobs


def report(title, done):
    hi_lat = [lat for name, lat in done if name.startswith("hi")]
    lo_lat = [lat for name, lat in done if name.startswith("lo")]
    print("%s: hi 平均延迟 %.2fs, lo 平均延迟 %.2fs, lo 最大 %.2fs"
          % (title, sum(hi_lat) / len(hi_lat),
             sum(lo_lat) / len(lo_lat), max(lo_lat)))


if __name__ == "__main__":
    jobs = build_jobs()
    report("严格优先级", simulate(jobs, "strict"))
    report("加权 3:1    ", simulate(jobs, "weighted"))
    print("要点: 加权轮询用 hi 的一点延迟, 换来 lo 的延迟上界")
    print("要点: 比例保证在过载时最值钱——低优先级至少活着")
