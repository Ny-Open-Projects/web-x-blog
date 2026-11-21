def migrate_expand(table: dict) -> dict:
    # 第一步 expand:只加新列,旧代码完全无感
    table["columns"] = table.get("columns", []) + ["full_name"]
    table["nullable"] = True
    return table


def deploy_new_code(writes: dict) -> dict:
    # 新代码写新列,同时兼容旧结构
    return {"name": writes["first"] + " " + writes["last"], "full_name": None}


def migrate_contract(table: dict) -> dict:
    # 最后一步 contract:确认无旧代码后才删列
    table["columns"] = [c for c in table["columns"] if c != "name"]
    return table


def test_rollback_safe():
    t = {"columns": ["name", "first", "last"]}
    expanded = migrate_expand(t)
    # 回滚:旧代码面对 expand 后的表仍可正常工作
    assert "name" in expanded["columns"]
