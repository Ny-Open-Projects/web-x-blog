import ast

SAMPLE = '''
import asyncio
import threading
import time

lock = threading.Lock()

async def bad_sleep():
    time.sleep(1)          # L1: async 内阻塞
    async with lock:       # L2: asyncio.Lock 与 threading.Lock 混用 (示例简化)
        pass

def unbalanced():
    lock.acquire()
    if True:
        return             # L3: acquire 后无 release
    lock.release()

def lock_pair():
    lock.acquire()
    try:
        pass
    finally:
        lock.release()
'''


def lint(source: str) -> list[str]:
    issues: list[str] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    name = ast.unparse(sub.func)
                    if name == "time.sleep":
                        issues.append(
                            f"第 {sub.lineno} 行: async 函数 {node.name} 内调用 time.sleep 会阻塞事件循环, 应改用 await asyncio.sleep")
        if isinstance(node, ast.FunctionDef):
            acquires = sum(
                1 for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "acquire"
            )
            releases = sum(
                1 for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "release"
            )
            if acquires > releases and not any(
                isinstance(n, ast.Try) for n in ast.walk(node)
            ):
                issues.append(
                    f"第 {node.lineno} 行: 函数 {node.name} 中 acquire {acquires} 次但 release {releases} 次, 且无 try/finally 保护")
    return issues


if __name__ == "__main__":
    for msg in lint(SAMPLE):
        print("[lint]", msg)
    print("人工清单补充项: 锁顺序 / 临界区完整性 / CancelledError 不得吞掉")
