
CHECKLIST = [
    "变更单含回滚方案与负责人",
    "数据库变更已评审且向后兼容",
    "关键路径测试与灰度指标已配置",
    "发布窗口避开业务高峰",
    "发布后观察 30 分钟核心指标",
]

passed = {name: True for name in CHECKLIST[:4]}
print("门禁通过:", all(passed.values()))
print("未完成项:", [c for c in CHECKLIST if c not in passed])
