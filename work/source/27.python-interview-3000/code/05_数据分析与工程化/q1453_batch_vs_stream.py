"""批处理与流处理:同一'每5分钟 PV'任务的两种实现对照"""
try:
    import pandas as pd
except ImportError:
    pd = None

EVENTS = [
    # ts 秒, page
    (0, "home"), (60, "item"), (120, "home"), (180, "item"),
    (240, "home"), (299, "home"), (301, "item"), (500, "home"),
]
WINDOW = 300


def batch_recompute(all_events):
    """批处理:每次全量重算,简单可靠,结果永远自洽"""
    windows = {}
    for ts, page in all_events:
        windows.setdefault(ts // WINDOW * WINDOW, 0)
        windows[ts // WINDOW * WINDOW] += 1
    return dict(sorted(windows.items()))


class StreamAggregator:
    """流处理:增量累加,低延迟,但要自己处理乱序与状态恢复"""

    def __init__(self):
        self.counts = {}

    def push(self, ts, page):
        key = ts // WINDOW * WINDOW
        self.counts[key] = self.counts.get(key, 0) + 1


if pd is None:
    print("标准库对照:")
    print("批处理全量重算:", batch_recompute(EVENTS))
    agg = StreamAggregator()
    for ts, page in EVENTS:
        agg.push(ts, page)
    print("流处理增量累加:", dict(sorted(agg.counts.items())))
else:
    df = pd.DataFrame(EVENTS, columns=["ts", "page"])
    df["window"] = df["ts"] // WINDOW * WINDOW
    print("批处理 pandas groupby:")
    print(df.groupby("window").size())
    agg = StreamAggregator()
    for ts, page in EVENTS:
        agg.push(ts, page)
    print("流处理增量:", dict(sorted(agg.counts.items())))
print("选型要点:结果表以'窗口键'为幂等键,批流写同一张表即 Kappa 思路")
