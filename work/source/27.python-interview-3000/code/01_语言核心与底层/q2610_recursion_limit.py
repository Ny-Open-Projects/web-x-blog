"""setrecursionlimit 的代价:门闩不等于栈,大栈线程里才能安全调高。"""
import sys
import threading


def count_depth_with_big_stack(limit, stack_bytes):
    """在指定栈大小的线程里递归到极限,返回达到的深度。"""
    result = {}

    def deep():
        sys.setrecursionlimit(limit)
        count = [0]

        def r():
            count[0] += 1
            r()

        try:
            r()
        except RecursionError:
            result["depth"] = count[0]

    threading.stack_size(stack_bytes)
    t = threading.Thread(target=deep)
    t.start()
    t.join()
    threading.stack_size(0)            # 恢复默认,避免影响后续线程
    return result.get("depth")


if __name__ == "__main__":
    # 主线程:默认限制下干净地抛 RecursionError
    sys.setrecursionlimit(1000)

    def boom(n):
        return boom(n + 1)

    try:
        boom(0)
    except RecursionError:
        print("主线程:限制 1000,RecursionError 被正常捕获")

    # 大栈线程:限制 300000 也能干净收场
    depth = count_depth_with_big_stack(300000, 256 * 1024 * 1024)
    print(f"256MB 栈线程:限制 300000,实际递归到 {depth} 层")
