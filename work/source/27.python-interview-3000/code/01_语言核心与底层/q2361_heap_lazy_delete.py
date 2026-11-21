"""堆的延迟删除:标记作废,出堆时过滤,代替 O(n) 的 remove。"""
import heapq
import itertools


class TaskQueue:
    """支持按 id 作废任务的最小堆。"""

    def __init__(self):
        self._heap = []
        self._cancelled = set()
        self._tie = itertools.count()   # 平局裁决,避免比较 payload

    def push(self, priority, task_id, payload):
        heapq.heappush(self._heap, (priority, next(self._tie), task_id, payload))

    def cancel(self, task_id):
        self._cancelled.add(task_id)

    def pop(self):
        while self._heap:
            priority, _, task_id, payload = heapq.heappop(self._heap)
            if task_id in self._cancelled:
                self._cancelled.discard(task_id)
                continue
            return task_id, payload
        raise IndexError("堆已空")


if __name__ == "__main__":
    q = TaskQueue()
    q.push(1, "t1", "低优先")
    q.push(0, "t2", "最优先")
    q.push(0, "t3", "次优先")
    q.cancel("t2")
    print("t2 已作废,直接跳到次优先:", q.pop())
    print("继续弹出:", q.pop())
    try:
        q.pop()
    except IndexError as exc:
        print("全部弹完:", exc)
