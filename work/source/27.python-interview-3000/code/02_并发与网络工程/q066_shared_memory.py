import multiprocessing
import multiprocessing.shared_memory as shm


def child(name: str, size: int) -> None:
    existing = shm.SharedMemory(name=name)
    try:
        # 读取父进程写入的数据
        data = bytes(existing.buf[:size])
        print("child 读到:", data.decode())
        existing.buf[:5] = b"CHILD"  # 回写(切片长度必须与数据等长)
    finally:
        existing.close()


if __name__ == "__main__":
    block = shm.SharedMemory(create=True, size=10)
    try:
        block.buf[:10] = b"PARENTDATA"  # 10 字节, 与切片等长
        p = multiprocessing.Process(target=child, args=(block.name, 10))
        p.start()
        p.join()
        print("parent 读回:", bytes(block.buf[:10]).decode())
    finally:
        # close + unlink 成对出现, 避免 resource_tracker 报泄漏
        block.close()
        block.unlink()  # 最后由创建者释放
