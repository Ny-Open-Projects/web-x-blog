"""Q2832 工具参数的资源级授权:引用 id 必须归属当前租户。

字段类型对了不代表能引用:LLM 可能拿别人的 doc_id 当参数。给工具声明
哪些参数是资源引用,执行前逐个校验归属与可见性,越权引用一律拒收
并写审计痕迹,而不是等工具自己抛权限异常。
"""

RESOURCE_OWNER = {
    "doc_1": "t_acme",
    "doc_2": "t_acme",
    "doc_9": "t_beta",
}

TOOL_REFS = {
    "read_doc": ["doc_id"],
    "delete_doc": ["doc_id"],
}


def authorize_args(tool, args, tenant, audit):
    """校验资源引用归属,返回是否放行,所有结论都写审计。"""
    for field in TOOL_REFS.get(tool, []):
        rid = args.get(field)
        if rid is None:
            audit.append("reject:" + tool + ":" + field + ":missing")
            return False
        owner = RESOURCE_OWNER.get(rid)
        if owner != tenant:
            audit.append("reject:" + tool + ":" + field + ":"
                         + rid + ":owner=" + str(owner))
            return False
    audit.append("allow:" + tool + ":" + ",".join(sorted(args)))
    return True


def main():
    audit = []
    ok = authorize_args("read_doc", {"doc_id": "doc_1"}, "t_acme", audit)
    assert ok is True, audit
    assert audit[-1] == "allow:read_doc:doc_id", audit
    # 跨租户引用:acme 想读 beta 的文档
    ok2 = authorize_args("delete_doc", {"doc_id": "doc_9"}, "t_acme", audit)
    assert ok2 is False, audit
    assert "reject:delete_doc:doc_id:doc_9:owner=t_beta" in audit, audit
    # 无引用字段的工具默认放行
    ok3 = authorize_args("list_docs", {}, "t_acme", audit)
    assert ok3 is True, audit
    print("审计轨迹:", audit)
    print("结论:越权引用在参数层被拦,工具本体根本没被调用")


if __name__ == "__main__":
    main()
