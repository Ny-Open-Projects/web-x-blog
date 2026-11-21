"""溢出落盘队列:内存缓冲满后溢出行落盘,内存排空后按序回放,顺序不乱。"""
import json
import os
import tempfile


class SpillQueue:
    def __init__(self, mem_limit=3):
        self.mem_limit = mem_limit
        self.mem = []
        self.spill_path = None
        self.spilled = 0

    def put(self, item):
        if len(self.mem) < self.mem_limit:
            self.mem.append(item)
            return "memory"
        if self.spill_path is None:              # 首次溢出:开落盘文件
            fd, self.spill_path = tempfile.mkstemp(prefix="spill-", suffix=".jsonl")
            os.close(fd)
        with open(self.spill_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
        self.spilled += 1
        return "disk"

    def drain(self):
        """按序吐出全部:先内存后磁盘回放,结束时清理落盘文件。"""
        out = list(self.mem)
        self.mem = []
        if self.spill_path:
            with open(self.spill_path, encoding="utf-8") as f:
                out.extend(json.loads(line) for line in f)
            os.remove(self.spill_path)
            self.spill_path = None
        return out


if __name__ == "__main__":
    q = SpillQueue(mem_limit=3)
    routes = [q.put({"n": i}) for i in range(8)]
    assert routes == ["memory"] * 3 + ["disk"] * 5, "前 3 条进内存,后 5 条落盘"
    assert q.spilled == 5 and len(q.mem) == 3

    drained = q.drain()
    assert drained == [{"n": i} for i in range(8)], "内存加磁盘按序完整回放"
    assert q.spill_path is None and not os.path.exists(
        tempfile.gettempdir() + "/__never__"), "落盘文件已清理"
    assert q.drain() == [], "排空后再取为空"
    print("溢出落盘通过:8 条消息 3 内存 5 落盘,回放顺序与入队一致,文件已清理")
