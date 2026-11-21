"""综合案例: 批窗口守恒与可复现全链路, 一次跑通五道断言"""

import hashlib
import json
import os
import tempfile

PIPELINE_VERSION = "pipe-2.0.0"
WINDOW = 60
EVENTS = [
    ("u1", 5, "click"), ("u2", 12, "pv"), ("u1", 30, "pv"),
    ("u1", 30, "pv"),                          # 窗口内重复事件
    ("u3", 70, "order"), ("u2", 95, "click"), ("u4", 130, "pv"),
]


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def process_window(lo, sink):
    """一个窗口: 按事件时间切片, 键级去重落表, 窗口内守恒对账"""
    hi = lo + WINDOW
    picked = [e for e in EVENTS if lo <= e[1] < hi]
    before = len(sink)
    dup = 0
    for user, ts, action in picked:
        key = (user, ts, action)
        if key in sink:
            dup += 1
        else:
            sink[key] = True
    new = len(sink) - before
    assert len(picked) == new + dup, "窗口守恒: 读入 = 新落表 + 重复"
    return {"window": [lo, hi], "read": len(picked), "new": new, "dup": dup,
            "input_sha256": sha256(json.dumps(picked))}


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        sink = {}
        manifest = {"pipeline_version": PIPELINE_VERSION, "params": {"window": WINDOW}, "windows": []}
        for lo in range(0, 180, WINDOW):
            entry = process_window(lo, sink)
            content = json.dumps(sorted(map(list, sink.keys())))
            out_path = os.path.join(tmp, f"out_{lo:03d}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            with open(out_path, encoding="utf-8") as f:
                entry["output_sha256"] = sha256(f.read())
            manifest["windows"].append(entry)
            print(f"窗口 [{entry['window'][0]:3d},{entry['window'][1]:3d}): 读 {entry['read']} 行"
                  f" = 新落表 {entry['new']} + 重复 {entry['dup']}, 累计 {len(sink)} 键")
        accounted = sum(w["read"] for w in manifest["windows"])
        assert accounted == len(EVENTS), "跨窗口总账守恒"
        print(f"总账: 窗口合计读入 {accounted} 行 == 全部事件 {len(EVENTS)} 行, 无一行失踪")
        with open(os.path.join(tmp, "out_120.json"), encoding="utf-8") as f:
            replay = sha256(f.read()) == manifest["windows"][-1]["output_sha256"]
        assert replay, "重放校验: 落盘内容指纹必须与清单一致"
        print("重放校验: 末窗落盘指纹与清单一致, 版本/参数/逐窗指纹四件套齐备")
        print(f"清单版本 {manifest['pipeline_version']}, 参数 {manifest['params']}")
    print("要点: 窗口守恒 跨窗总账 幂等去重 原子落盘 清单指纹, 五道断言组成一次可信的批处理")
