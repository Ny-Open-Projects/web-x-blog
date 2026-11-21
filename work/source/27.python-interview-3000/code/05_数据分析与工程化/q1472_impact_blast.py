"""变更影响面:血缘图反查下游,输出爆炸半径与通知名单"""

LINEAGE = {
    # 上游表: 直接下游列表
    "ods_orders": ["dwd_orders", "dws_sales_daily"],
    "ods_users": ["dwd_users"],
    "dwd_orders": ["dws_sales_daily", "ads_funnel"],
    "dwd_users": ["ads_funnel", "ads_retention"],
    "dws_sales_daily": ["ads_sales_report", "api_gmv"],
    "ads_funnel": ["bi_board_growth"],
    "ads_retention": ["bi_board_growth"],
    "ads_sales_report": [],
    "api_gmv": [],
    "bi_board_growth": [],
}

OWNERS = {
    "ads_funnel": "增长组", "ads_retention": "增长组", "ads_sales_report": "销售组",
    "api_gmv": "交易中台", "bi_board_growth": "BI 平台", "dws_sales_daily": "数仓组",
    "dwd_orders": "数仓组", "dwd_users": "数仓组",
}


def blast_radius(changed):
    """BFS 反查全部下游,区分直接下游与全部受影响"""
    all_down, direct, frontier = set(), LINEAGE[changed], [changed]
    while frontier:
        node = frontier.pop()
        for child in LINEAGE.get(node, []):
            if child not in all_down:
                all_down.add(child)
                frontier.append(child)
    endpoints = [n for n in all_down if not LINEAGE.get(n)]
    owners = sorted({OWNERS.get(n, "未知") for n in all_down})
    return sorted(direct), sorted(all_down), endpoints, owners


if __name__ == "__main__":
    direct, all_down, endpoints, owners = blast_radius("ods_orders")
    print("改动表: ods_orders")
    print("直接下游:", direct)
    print("全部受影响:", all_down)
    print("末端消费点:", endpoints)
    print("需通知团队:", owners)
    print("要点:阻断级变更直接给下游任务挂 skip 并在群里点名到人")
