
def phase_plan(current: dict, target: dict) -> list:
    return [
        "expand: 新旧字段同时写 old_price 与 price_v2, 读仍走 old_price",
        "migrate: 回填历史行 price_v2, 校验对齐后读切换新字段",
        "contract: 观察一个发布周期后移除 old_price 与双写代码",
    ]

for step in phase_plan({}, {}):
    print(step)
