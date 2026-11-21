
STAGES = ["脚本期", "模块期", "服务期", "平台期", "自治期"]
SIGNALS = {
    "脚本期": ["单文件 cron", "无测试", "配置硬编码"],
    "模块期": ["函数拆分", "有单测", "配置外置"],
    "服务期": ["容器化", "健康检查", "结构化日志"],
    "平台期": ["CI/CD", "可观测面板", "SLO 与告警"],
    "自治期": ["自动扩缩", "错误预算驱动", "混沌演练常态化"],
}

def next_step(stage):
    i = STAGES.index(stage)
    return STAGES[i + 1] if i + 1 < len(STAGES) else None

if __name__ == "__main__":
    for s in STAGES:
        print(f"{s}: {', '.join(SIGNALS[s])}")
    print("当前 脚本期 -> 下一步:", next_step("脚本期"))
    print("演进原则:每步独立交付价值,先测试再拆分,绞杀者模式并行切换")
