"""生产就绪检查器:逐项检查配置,输出上线前报告。"""

CHECKLIST = {
    "可靠性": ["timeout_configured", "retry_policy", "fallback_path", "idempotent_tools"],
    "安全": ["injection_guard", "tool_whitelist", "pii_redaction", "audit_log"],
    "可观测": ["trace_enabled", "cost_dashboard", "badcase_collection"],
    "评估": ["offline_eval_set", "canary_release", "prompt_versioned"],
}


class ProdReadiness:
    def __init__(self, config: dict):
        self.config = config

    def check(self) -> tuple[bool, list[str]]:
        missing = []
        for category, items in CHECKLIST.items():
            for item in items:
                if not self.config.get(item):
                    missing.append(f"{category}/{item}")
        return not missing, missing

    def report(self) -> str:
        ok, missing = self.check()
        lines = ["== 生产就绪报告 ==", f"结论: {'可上线' if ok else '不可上线'}"]
        lines += [f"  缺失项: {m}" for m in missing] or ["  全部通过"]
        return "\n".join(lines)


if __name__ == "__main__":
    partial = {"timeout_configured": True, "retry_policy": True,
               "injection_guard": True, "trace_enabled": True}
    print(ProdReadiness(partial).report())
    print()
    full = {k: True for items in CHECKLIST.values() for k in items}
    print(ProdReadiness(full).report().splitlines()[1])
