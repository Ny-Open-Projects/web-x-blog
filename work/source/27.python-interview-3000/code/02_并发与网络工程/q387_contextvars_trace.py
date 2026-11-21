"""contextvars + logging 实现请求级 trace_id。"""
import asyncio
import logging
import uuid
from contextvars import ContextVar

trace_id_var: ContextVar[str] = ContextVar("trace_id", default="-")


class TraceFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


log = logging.getLogger("svc")
log.setLevel(logging.INFO)
h = logging.StreamHandler()
h.setFormatter(logging.Formatter("[%(trace_id)s] %(message)s"))
h.addFilter(TraceFilter())
log.addHandler(h)


async def handle_request(tag: str):
    trace_id_var.set(uuid.uuid4().hex[:8])  # 每个请求设置自己的 trace_id
    log.info("%s 收到请求", tag)
    await asyncio.sleep(0.05)               # await 期间上下文不串
    log.info("%s 处理完成", tag)


async def main():
    # 两个并发请求,日志各自携带不同 trace_id
    await asyncio.gather(handle_request("req-A"), handle_request("req-B"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
