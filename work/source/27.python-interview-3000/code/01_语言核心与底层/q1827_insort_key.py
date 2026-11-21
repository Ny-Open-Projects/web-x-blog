"""bisect.insort:对象列表的有序维护与版本差异。"""
import bisect
import sys


def plain_insort():
    xs = []
    for n in [5, 1, 9, 3, 7]:
        bisect.insort(xs, n)          # 二分找插入点,保持升序
    return xs


def object_list_39():
    # 3.9 没有 key= 参数:用「键列表 + 对象列表」平行数组维护对象有序
    keys, events = [], []

    def add(event):
        k = event["ts"]
        i = bisect.bisect_right(keys, k)
        keys.insert(i, k)
        events.insert(i, event)

    for ts in [30, 10, 20, 10]:
        add({"ts": ts, "tag": "e" + str(ts)})
    return events


if __name__ == "__main__":
    print("纯数字 insort:", plain_insort())
    events = object_list_39()
    print("对象有序(平行数组):", [e["ts"] for e in events])
    if sys.version_info >= (3, 10):
        rows = []
        for ts in [30, 10, 20]:
            bisect.insort(rows, {"ts": ts}, key=lambda e: e["ts"])
        print("3.10+ key= 版:", [r["ts"] for r in rows])
    else:
        print("3.10+ 的 key= 在本机",
              ".".join(map(str, sys.version_info[:3])), "不可用,已用平行数组替代")
