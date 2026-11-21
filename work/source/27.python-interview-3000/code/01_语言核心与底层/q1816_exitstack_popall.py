"""ExitStack 的所有权转移:pop_all 与事务式交接。"""
import os
import tempfile
from contextlib import ExitStack


class Batch:
    """提交成功后长期持有临时文件;失败则逐个清理。"""

    def __init__(self):
        self.stack = ExitStack()
        self.keep = None

    def add_temp(self):
        fd, path = tempfile.mkstemp()
        os.close(fd)
        self.stack.callback(os.remove, path)
        return path

    def commit(self):
        # 成功:把清理责任原样移交,外层 with 退出时不再触碰这些文件
        self.keep = self.stack.pop_all()

    def close(self):
        if self.keep is not None:
            self.keep.close()      # 幂等:空栈 close 无害


def produce(commit=True):
    with ExitStack() as outer:
        batch = Batch()
        paths = [batch.add_temp() for _ in range(2)]
        outer.callback(batch.stack.close)   # 失败兜底:清空 batch 的栈
        if not commit:
            raise RuntimeError("中途失败")
        batch.commit()                      # 责任移交,batch.stack 已空
        return paths


if __name__ == "__main__":
    kept = produce(commit=True)
    print("提交后文件仍在:", [os.path.exists(p) for p in kept])
    for p in kept:
        if os.path.exists(p):
            os.remove(p)
    try:
        produce(commit=False)
    except RuntimeError as e:
        print("失败路径:", e, "→ 临时文件已随栈清理")
