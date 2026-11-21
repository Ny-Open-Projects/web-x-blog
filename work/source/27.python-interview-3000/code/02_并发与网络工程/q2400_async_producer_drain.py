# -*- coding: utf-8 -*-
"""异步生产者的优雅排空: 听到停机令, 把手里的活干完再走。

- 直接 cancel 会把批内数据切在半截, 下游读到脏流;
- 优雅排空: 生产者在安全检查点看停止标志, 看到了就补完当前批再冲刷退出;
- 消费者一直读到队列关闭标记, 天然拿到完整的最后一段。
"""
import asyncio


class StopRequested(Exception):
    pass


async def producer(q, stop_flag, log, total=10):
    try:
        for i in range(total):
            if stop_flag.is_set() and i >= 5:      # 检查点: 批边界才可停
                raise StopRequested
            await asyncio.sleep(0.02)
            await q.put(i)
            log.append("生产 %d" % i)
    except StopRequested:
        log.append("收到停机令, 补完当前批")
    finally:
        await q.put(None)                          # 关门标记: 下游可以收工
        log.append("生产者退出")


async def consumer(q, log):
    while True:
        item = await q.get()
        if item is None:
            log.append("读到关门标记, 消费者退出")
            return
        log.append("消费 %d" % item)
        await asyncio.sleep(0.01)


async def main():
    q = asyncio.Queue(maxsize=4)
    stop_flag = asyncio.Event()
    plog, clog = [], []

    async def operator():
        await asyncio.sleep(0.08)                  # 中途下达停机令
        stop_flag.set()

    await asyncio.gather(producer(q, stop_flag, plog),
                         consumer(q, clog),
                         operator())
    print("生产侧:", plog)
    print("消费侧: 共 %d 件" % len([x for x in clog if x.startswith("消费")]))
    produced = [x for x in plog if x.startswith("生产 ")]
    consumed = [x for x in clog if x.startswith("消费 ")]
    assert len(produced) == len(consumed), "优雅排空下生产多少就消费多少"
    assert produced == [x.replace("消费", "生产") for x in consumed], \
        "消费序必须覆盖全部生产序, 不掉尾"
    assert "生产者退出" in plog and any("关门标记" in x for x in clog), \
        "双方都以关门标记优雅收场"


if __name__ == "__main__":
    asyncio.run(main())
