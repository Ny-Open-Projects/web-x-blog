"""Q2577 多租户的 prompt 隔离审计:渲染结果里不许出现别家密文。

模板渲染后的 prompt 落审计库,离线扫描器逐条检查是否包含其他
租户的敏感令牌;命中即拦截发送并升级告警。用注入的坏模板演示
一次真实泄漏被审计逮住,干净模板必须零误报。
"""

TENANT_SECRET = {"t1": "ACCT-111", "t2": "ACCT-222"}


def render_prompt_ok(tenant):
    return "你是助手,服务对象账号 " + TENANT_SECRET[tenant]


def render_prompt_buggy(tenant):
    """事故模板:误用了全局最近租户的状态,跨租户串号。"""
    return "你是助手,服务对象账号 " + TENANT_SECRET["t2"]


def audit(prompt, tenant):
    leaks = []
    for other, secret in TENANT_SECRET.items():
        if other != tenant and secret in prompt:
            leaks.append(other)
    return leaks


def main():
    clean = render_prompt_ok("t1")
    assert audit(clean, "t1") == []
    dirty = render_prompt_buggy("t1")
    leaks = audit(dirty, "t1")
    assert leaks == ["t2"], leaks
    print("干净 prompt 审计通过:零泄漏零误报")
    print("泄漏 prompt 命中租户:", leaks, "→ 拦截发送并升级告警")


if __name__ == "__main__":
    main()
