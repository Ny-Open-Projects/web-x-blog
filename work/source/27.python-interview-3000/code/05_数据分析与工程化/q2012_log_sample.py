"""日志分级采样:过滤器按级别确定性采样,保留丢弃计数用于审计"""

import logging

RATES = {"DEBUG": 10, "INFO": 2, "WARNING": 1, "ERROR": 1}   # 每 N 条放行 1 条


class SamplerFilter(logging.Filter):
    """确定性计数采样:第 1 条放行,之后每 N 条放行 1 条,可复现"""

    def __init__(self, rates):
        super().__init__()
        self.rates = rates
        self.counters = {}
        self.passed = {}
        self.dropped = {}

    def filter(self, record):
        level = record.levelname
        self.counters[level] = self.counters.get(level, 0) + 1
        rate = self.rates.get(level, 1)
        keep = True if rate <= 1 else (self.counters[level] - 1) % rate == 0
        if keep:
            self.passed[level] = self.passed.get(level, 0) + 1
        else:
            self.dropped[level] = self.dropped.get(level, 0) + 1
        return keep


if __name__ == "__main__":
    logger = logging.getLogger("sampler")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    sampler = SamplerFilter(RATES)
    handler.addFilter(sampler)
    logger.addHandler(handler)

    for i in range(1, 31):
        logger.debug("debug 细节 %d", i)
        logger.info("info 请求 %d", i)
        if i % 10 == 0:
            logger.warning("warning 慢查询 %d", i)
        if i == 30:
            logger.error("error 任务失败")
    print("-" * 40)
    print("丢弃审计:", {k: v for k, v in sampler.dropped.items() if v})
    print("放行统计:", {k: v for k, v in sampler.passed.items() if v})
    print("要点:采样按确定性计数不按随机,同一输入可复现;WARNING 以上永不丢;丢弃数本身要可观测,高峰期丢了多少日志要说得清")
