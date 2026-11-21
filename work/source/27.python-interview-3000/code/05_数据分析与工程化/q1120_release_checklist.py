
CHECKS = [
    ("单测与 lint 通过", lambda ctx: ctx.get("ci_green")),
    ("迁移可回滚", lambda ctx: ctx.get("migration_reversible")),
    ("特性开关默认关闭", lambda ctx: ctx.get("flag_off")),
    ("回滚步骤演练过", lambda ctx: ctx.get("rollback_drilled")),
    ("监控与告警就位", lambda ctx: ctx.get("alerts_ready")),
]

def run_checklist(ctx):
    results = [(name, bool(fn(ctx))) for name, fn in CHECKS]
    for name, passed in results:
        print(("通过" if passed else "阻塞"), "-", name)
    return all(r for _, r in results)

if __name__ == "__main__":
    ctx = {"ci_green": True, "migration_reversible": True, "flag_off": True,
           "rollback_drilled": False, "alerts_ready": True}
    ok = run_checklist(ctx)
    print("结论:", "允许发布" if ok else "禁止发布,先补齐检查项")
