"""构造一个小连接池, 演示并发获取超时与 pool.status 水位"""
import threading
import time

try:
    from sqlalchemy import create_engine, text
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///q917_pool.db",               # 文件库使用 QueuePool, 支持池参数
        pool_size=2, max_overflow=0, pool_timeout=0.3, pool_pre_ping=True)

    def hold(i, out):
        try:
            with engine.connect() as conn:      # with 保证归还
                out.append(i)
                time.sleep(0.4)                 # 模拟慢查询占用
        except Exception:
            out.append(f"timeout-{i}")          # 池耗尽快速失败

    out = []
    threads = [threading.Thread(target=hold, args=(i, out)) for i in range(4)]
    t0 = time.perf_counter()
    try:
        [t.start() for t in threads]
        [t.join() for t in threads]
        print(f"全部完成 {out}, 总耗时 {time.perf_counter() - t0:.1f}s (串行化于池大小)")
    except Exception as e:
        print("池耗尽:", type(e).__name__)
    print("池状态:", engine.pool.status())
