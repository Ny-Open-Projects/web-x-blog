from typing import Iterator


def iter_error_lines(path: str, chunk: int = 1 << 20) -> Iterator[tuple[int, str]]:
    """流式统计:逐行迭代,内存 O(1),返回行号与内容。"""
    with open(path, encoding="utf-8", errors="replace") as f:
        for lineno, line in enumerate(f, 1):  # 文件对象即迭代器
            if "ERROR" in line:
                yield lineno, line.rstrip("\n")


def count_by_chunk(path: str) -> int:
    """二进制块读取版本,适合无行概念的大文件。"""
    count = 0
    with open(path, "rb") as f:
        while True:
            block = f.read(1 << 20)
            if not block:
                break
            count += block.count(b"ERROR")
    return count


if __name__ == "__main__":
    with open("demo.log", "w") as f:
        for i in range(1000):
            f.write(f"{i} INFO ok\n" if i % 10 else f"{i} ERROR boom\n")
    hits = list(iter_error_lines("demo.log"))[:3]
    print(hits, "total:", len(list(iter_error_lines("demo.log"))))
    print(count_by_chunk("demo.log"))
