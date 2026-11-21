import multiprocessing as mp

N = 20000  # 演示规模: 跨进程锁粒度重, 规模控制在 25s 内跑完


def unlocked_worker(val) -> None:
    for _ in range(N):
        v = val.value      # 读
        val.value = v + 1  # 写: 读-改-写之间可能被其他进程插入


def locked_worker(val) -> None:
    for _ in range(N):
        with val.get_lock():   # Value 自带的进程锁
            val.value += 1


def run(target, lock: bool) -> int:
    val = mp.Value("i", 0, lock=lock)
    ps = [mp.Process(target=target, args=(val,)) for _ in range(4)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    return val.value


if __name__ == "__main__":
    lost = run(unlocked_worker, lock=False)
    print(f"无锁结果: {lost} / 期望 {4 * N} (丢失 {4 * N - lost})")
    ok = run(locked_worker, lock=True)
    print(f"加锁结果: {ok} / 期望 {4 * N}")
    assert ok == 4 * N
