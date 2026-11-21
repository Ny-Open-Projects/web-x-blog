def ci_gate(results: dict[str, bool]) -> tuple[bool, str]:
    # CI 门禁逻辑:按阶段顺序短路,先挂先报
    order = ["lint", "typecheck", "test", "build"]
    for stage in order:
        if not results.get(stage, False):
            return False, f"failed at {stage}"
    return True, "all green"

def test_gate_order():
    assert ci_gate({"lint": True, "typecheck": True,
                    "test": True, "build": True}) == (True, "all green")
    assert ci_gate({"lint": False}) == (False, "failed at lint")
