"""批量窗口的水位推进: 提交后才推进 崩溃重跑 空窗也要走"""

import json
import os
import tempfile

WINDOW = 60          # 窗口长度: 分钟
EVENTS = [("e1", 5), ("e2", 30), ("e3", 70)]      # 事件 id, 事件时间(分钟)


class WatermarkState:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {"watermark": 0}

    def save(self):
        """原子写: 先落临时文件再 rename, 防止半截状态"""
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self.data, f)
        os.replace(tmp, self.path)


def run_window(state, sink, commit=True):
    lo = state.data["watermark"]
    hi = lo + WINDOW
    picked = [e for e in EVENTS if lo <= e[1] < hi]
    for eid, _ in picked:                       # upsert 语义: 重复执行不产生重复行
        sink[eid] = True
    if not commit:
        raise RuntimeError("提交前崩溃, 水位不得推进")
    state.data["watermark"] = hi
    state.data["last_note"] = f"窗口 [{lo},{hi}) 处理 {len(picked)} 行" + ("(空窗)" if not picked else "")
    state.save()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        state = WatermarkState(os.path.join(tmp, "state.json"))
        sink = {}
        try:
            run_window(state, sink, commit=False)
        except RuntimeError as e:
            print(f"窗口 [0,60) 崩溃: {e}, 水位仍为 {state.data['watermark']}")
        assert state.data["watermark"] == 0, "未提交不得推进水位"
        run_window(state, sink)                 # 重跑同一窗口, upsert 幂等
        print(f"重跑窗口 [0,60): 处理 2 行, 水位推进到 {state.data['watermark']}, 落表 {len(sink)} 行")
        run_window(state, sink)                 # 窗口 [60,120)
        run_window(state, sink)                 # 窗口 [120,180) 空窗
        print(f"空窗也推进: 水位 {state.data['watermark']}, 备注: {state.data['last_note']}")
        assert state.data["watermark"] == 180 and len(sink) == 3
    print("要点: 水位是'已提交边界'不是'已处理边界', 推进必须与输出同事务, 空窗不停摆")
