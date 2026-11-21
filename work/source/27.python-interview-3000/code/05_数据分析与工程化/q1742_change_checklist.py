"""变更影响面清单:按变更类型套注册表生成检查项,清单跟着类型走不靠记忆"""

CHECKLISTS = {
    "field_type_change": [
        "反查字段级血缘,列出下游任务",
        "下游读写方确认新类型兼容",
        "准备历史分区回填脚本",
        "观察期 1 天,新旧口径双跑一致",
    ],
    "metric_caliber_change": [
        "指标字典登记新版本号",
        "报表与看板同步切换时间",
        "历史数据是否重算由业务拍板",
        "对外报表提前一周公告",
    ],
    "schedule_time_change": [
        "确认数据就绪水位线时间",
        "检查下游任务起始时间联动",
        "核对冻结日历,冻结期内不得调整",
    ],
}


def gen_checklist(change_type, target):
    items = CHECKLISTS.get(change_type)
    if not items:
        raise ValueError(f"未登记的变更类型: {change_type}")
    lines = [f"## 变更清单 {change_type} @ {target}", ""]
    lines += [f"- [ ] {item}" for item in items]
    lines += ["", "- 变更人:____  评审人:____  回滚方案:____"]
    return "\n".join(lines)


if __name__ == "__main__":
    print(gen_checklist("metric_caliber_change", "ads.vip_board.pay_users_7d"))
    try:
        gen_checklist("db_drop_table", "dwd.pay_order_d")
    except ValueError as e:
        print("\n已拦截未登记类型:", e)
    print("要点:清单本质是'变更类型 x 强制动作'注册表,新类型进注册表要走评审;执行记录留档,审计能查到谁在何时改了什么")
