"""三种时钟的选择演示。"""
import time

if __name__ == "__main__":
    # 基准测量:perf_counter 精度最高
    start = time.perf_counter()
    sum(range(1_000_000))
    print(f"CPU 耗时 perf_counter: {time.perf_counter() - start:.6f}s")

    # 业务限速/超时:monotonic
    deadline = time.monotonic() + 0.2
    while time.monotonic() < deadline:
        pass
    print("deadline 轮询结束, 未超时:", time.monotonic() <= deadline + 0.05)

    # 墙钟:用于日志时间戳、对外展示
    print("wall clock:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 对比:process_time 不含 sleep
    s = time.process_time()
    time.sleep(0.1)
    print(f"sleep 0.1s 后 process_time 只增加 {time.process_time() - s:.6f}s")
