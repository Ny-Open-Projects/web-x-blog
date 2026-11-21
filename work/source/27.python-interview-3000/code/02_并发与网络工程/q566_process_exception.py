from multiprocessing import Pool


def divide(a: float, b: float) -> float:
    return a / b


def on_error(e: BaseException) -> None:
    print("error_callback 收到:", repr(e))


if __name__ == "__main__":
    with Pool(processes=2) as pool:
        r = pool.apply_async(divide, (10, 2))
        print("正常结果:", r.get())

        bad = pool.apply_async(divide, (1, 0), error_callback=on_error)
        try:
            bad.get()
        except ZeroDivisionError as e:
            print("子进程异常透传到父进程:", repr(e))

        # 进程池仍然可用: 异常不会杀死 worker
        print("恢复后继续:", pool.apply_async(divide, (9, 3)).get())
