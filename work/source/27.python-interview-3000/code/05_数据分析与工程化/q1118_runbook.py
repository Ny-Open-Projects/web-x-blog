
RUNBOOK = {
    "api-5xx-激增": {
        "确认": ["打开 SLO 看板确认 burn rate", "区分全量还是部分实例"],
        "处置": ["回滚最近 30 分钟发布", "必要时扩容或开启限流"],
        "升级": ["15 分钟未恢复升级 P0 负责人与平台组"],
        "恢复后": ["确认错误预算消耗", "24h 内出复盘"],
    },
}

def show(name):
    rb = RUNBOOK[name]
    for section, steps in rb.items():
        print(f"## {section}")
        for i, s in enumerate(steps, 1):
            print(f"  {i}. {s}")

if __name__ == "__main__":
    show("api-5xx-激增")
    print("纪律:与告警同仓库评审,命令可复制执行,值班交接抽测防过期")
