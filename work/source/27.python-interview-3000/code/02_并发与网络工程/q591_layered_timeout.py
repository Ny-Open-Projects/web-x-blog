import asyncio

TOTAL_BUDGET = 0.6  # 总预算 600ms


async def phase(name: str, cost: float) -> str:
    await asyncio.sleep(cost)  # 模拟阶段耗时
    return name


async def request(phases, budget: float = TOTAL_BUDGET) -> list:
    loop = asyncio.get_running_loop()
    deadline = loop.time() + budget
    results = []
    for name, coro in phases:
        remaining = deadline - loop.time()
        if remaining <= 0:
            raise TimeoutError(f"总预算耗尽, 无法进入阶段 {name}")
        try:
            results.append(await asyncio.wait_for(coro, remaining))
        except asyncio.TimeoutError:
            raise TimeoutError(
                f"阶段 {name} 超出剩余预算 {remaining * 1000:.0f}ms"
            ) from None
    return results


async def main() -> None:
    ok_phases = [
        ("connect", phase("connect", 0.1)),
        ("read", phase("read", 0.2)),
        ("process", phase("process", 0.2)),
    ]
    print("正常:", await request(ok_phases))

    slow_phases = [
        ("connect", phase("connect", 0.1)),
        ("read", phase("read", 0.4)),    # 单段不超预算, 但会吃光总预算
        ("process", phase("process", 0.4)),
    ]
    try:
        await request(slow_phases)
    except TimeoutError as e:
        print("按预期失败:", e)


asyncio.run(main())
