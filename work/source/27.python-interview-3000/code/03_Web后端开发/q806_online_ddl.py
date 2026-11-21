
def plan_add_column(big_table: str, column: str) -> list:
    return [
        f"迁移A: {big_table} 加可空列 {column} 不带默认值, 秒级完成",
        f"代码双写: 新写入同时填旧字段与 {column}",
        f"回填: 按主键分批 UPDATE 历史行, 控制每批速率",
        f"迁移B: 数据对齐后收紧约束, 观察一个发布周期",
        f"迁移C: 移除旧字段与双写代码",
    ]

for step in plan_add_column("orders", "status_v2"):
    print(step)
