from collections import deque

def task(name, steps):
    for i in range(steps):
        yield f"{name} step {i}"          # 暂停点:交还控制权

def scheduler(tasks):
    queue = deque(tasks)
    started = set()
    tick = 0
    while queue:
        current = queue.popleft()
        try:
            if current in started:
                current.send(f"tick {tick}")
            else:
                started.add(current)
                next(current)             # 首次调度:先预激
        except StopIteration:
            continue                      # 任务完成,不再入队
        queue.append(current)             # 未完成的任务回到队尾
        tick += 1

if __name__ == "__main__":
    scheduler([task("A", 2), task("B", 3)])
