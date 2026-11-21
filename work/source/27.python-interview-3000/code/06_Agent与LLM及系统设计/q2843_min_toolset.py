"""Q2843 按任务模板装配最小工具集:运行期裁剪与越界拦截。

权限系统常见漏洞:全局注册了几十个工具,每个 Agent 都看得到。收口
办法是按任务模板装配:客服模板只给检索 读文档,支付类工具根本不进
本次运行的注册表,想调都没得调,而不是注册了再靠提示词求它别调。
"""

FULL_REGISTRY = {
    "search": "搜索知识库",
    "read_doc": "读文档详情",
    "send_mail": "发邮件",
    "pay.refund": "发起退款",
}

TASK_TEMPLATES = {
    "faq_bot": {"tools": ["search", "read_doc"]},
    "ops_bot": {"tools": ["search", "read_doc", "send_mail"]},
}


def assemble(task, available):
    """按模板从全量注册表裁出本次运行的工具集。"""
    declared = TASK_TEMPLATES[task]["tools"]
    missing = [t for t in declared if t not in available]
    run_tools = {t: available[t] for t in declared if t in available}
    return run_tools, missing


def guard_call(run_tools, tool):
    if tool not in run_tools:
        raise PermissionError("工具不在本任务最小集:" + tool)
    return run_tools[tool]


def main():
    run_tools, missing = assemble("faq_bot", FULL_REGISTRY)
    assert sorted(run_tools) == ["read_doc", "search"], run_tools
    assert missing == [], missing
    assert "pay.refund" not in run_tools, run_tools  # 压根不装配
    # faq_bot 试图发邮件:拦截
    err = ""
    try:
        guard_call(run_tools, "send_mail")
    except PermissionError as exc:
        err = str(exc)
    assert "不在本任务最小集" in err, err
    # 模板依赖的工具缺失要显式暴露,而不是静默缺功能
    run_tools2, missing2 = assemble("ops_bot", {"search": "搜索知识库"})
    assert missing2 == ["read_doc", "send_mail"], missing2
    print("faq_bot 工具集:", sorted(run_tools))
    print("越界调用拦截:", err)
    print("模板依赖缺失:", missing2)


if __name__ == "__main__":
    main()
