"""收官综合: 发布检查单引擎, 全绿才 GO(纯标准库)。"""

FIX_MIGRATION = False


def gate_tests():
    return True, "单元与契约测试全绿"


def gate_config():
    return True, "配置校验通过, secret 来自 vault"


def gate_migration():
    if FIX_MIGRATION:
        return True, "迁移改为加列两阶段, 可随时回退"
    return False, "迁移含删列, 未做两阶段发布"


def gate_drain():
    return True, "readiness 摘流与排空已演练"


def gate_rollback():
    return True, "回滚脚本与版本台账就绪"


GATES = [("自动化测试", gate_tests), ("配置校验", gate_config),
         ("迁移可逆", gate_migration), ("排空演练", gate_drain),
         ("回滚预案", gate_rollback)]


def release():
    results = [(name, fn()) for name, fn in GATES]
    blockers = [name for name, (ok, _) in results if not ok]
    print("--- 发布检查单 ---")
    for name, (ok, note) in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {note}")
    print("决策:", "GO" if not blockers else f"NO-GO 阻断项: {', '.join(blockers)}")
    print()


print("第一轮:")
release()
FIX_MIGRATION = True
print("修复迁移后第二轮:")
release()
print("要点: 检查单把人脑记忆变成机器门禁, 任一项 FAIL 就 NO-GO, 宁可延期不可带病上线")
