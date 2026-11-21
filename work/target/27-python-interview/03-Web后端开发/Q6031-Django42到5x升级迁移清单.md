---
title: [Q6031] Django 4.2→5.x 升级迁移清单
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6031 · Django 4.2→5.x 升级迁移清单

> 难度:★★★★ | 标签:版本演进, Django, 升级工程

**问**：Django 4.2 LTS 升到 5.x，除了改 requirements 还要过哪些关？5.0/5.1/5.2 各有什么破坏性变化值得背？异步视图普及后升级风险怎么变？

**答**：升级路径纪律是**逐小版本走**（4.2→5.0→5.1→5.2），每步对照 release notes 的 "Backwards incompatible changes"，因为弃用策略保证"上一版警告、下一版移除"。各版本要点：**5.0**——Python 3.10 门槛；数据库层面要求 PostgreSQL 12+/MySQL 8+；`USE_TZ` 默认 True（时区语义收紧，naive datetime 写入告警，Q802）；ORM 增 `db_default`（数据库层默认值，迁移语义变化）。**5.1**——`QuerySet.explain` 增强；异步 ORM 接口扩展（`aaggregate`/`acount` 等批量 a 开头方法），async views 与 sync ORM 桥接的线程池耗尽问题（Q6006）在升级时要重审。**5.2**——LTS；composite primary keys（CompositePrimaryKey）；Python 3.13 支持。迁移清单六步：1) **依赖矩阵先行**——DRF/兜底三方库声明支持的 Django 版本先核实；2) **消警告**——4.2 下跑测试到 0 warning（`-W error::DeprecationWarning` 门禁）；3) **migration 冷检**——升级后 `makemigrations --check` 与 `migrate --plan` 在 staging 全量跑；4) **settings 审计**——`DEFAULT_AUTO_FIELD`、时区、`STORAGES`（4.2 起新式配置）等默认值变化；5) **异步路径压测**——async view + sync 桥接在线程池打满下的表现（Q6006）；6) **灰度与回滚**——迁移与代码发布解耦（Q6017/Q816 的两阶段兼容）。

```python
# file: code/03_Web后端开发/q6031_django_upgrade.py
"""Django 未安装时降级为纯清单检查; 已安装则做 settings/migration 冷检."""
import subprocess
import sys

def django_version():
    try:
        import django
        return django.get_version()
    except ImportError:
        return None

def release_notes_gate(current: str, target: str) -> list[str]:
    """逐小版本升级的关卡清单(LTS 内每一步都要过 release notes)."""
    steps = {"4.2->5.0": ["Python>=3.10", "DB 版本门槛(PG12+/MySQL8+)",
                          "USE_TZ 默认 True", "db_default 语义"],
             "5.0->5.1": ["async ORM 扩展(aaggregate/acount)",
                          "线程池耗尽重审(Q6006)"],
             "5.1->5.2": ["Python 3.13 支持", "CompositePrimaryKey"],
             }
    order = ["4.2->5.0", "5.0->5.1", "5.1->5.2"]
    try:
        i = order.index(f"{current}->{target}")
    except ValueError:
        return ["非法路径: 只允许逐小版本"]
    out = []
    for step in order[:i + 1]:
        out += steps[step]
    return out

def management_cold_checks(app_name: str = "yourapp") -> list[tuple[str, bool]]:
    """已装 Django 时跑的冷检命令(无 Django 返回占位)."""
    checks = [
        (["python", "-m", "django", "makemigrations", "--check", "--dry-run"], "migration 无遗漏"),
        (["python", "-m", "django", "check", "--deploy"], "deploy 检查"),
    ]
    results = []
    for cmd, name in checks:
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            results.append((name, r.returncode == 0))
        except FileNotFoundError:
            results.append((name, None))            # django 未安装
    return results

if __name__ == "__main__":
    v = django_version()
    print("当前 Django:", v or "(未安装, 降级演示)")
    print("4.2->5.2 升级关卡:")
    for g in release_notes_gate("4.2", "5.2"):
        print("  -", g)
    print("冷检结果:", management_cold_checks())
    print("纪律: 逐小版本走 + 消警告门禁 + 迁移与代码解耦发布")
```

**追问**：1) 为什么不允许从 4.2 直接跳 5.2？——跨版本跳级会同时引入两版破坏性变化与"未经历弃用警告期"的移除项，出问题时无法二分定位；逐级走保证每步可回滚、可归因。2) `USE_TZ=True` 升级后最容易爆什么？——历史代码里 naive `datetime.now()` 与 ORM 的 aware 字段混用，比较/入库抛 TypeError 或静默偏移；升级前用 linter 扫 `datetime.now()` 调用点，统一 `timezone.now()`。3) 升级窗口期"新 Django + 旧迁移未跑"的组合怎么防？——发布编排把 migrate 与代码 rollout 排序（先加兼容迁移后代码），加 `makemigrations --check` 进 CI 防"模型改了迁移没生成"。

## 背诵要点
- 升级路径逐小版本走（4.2→5.0→5.1→5.2），每步过 release notes 与 0-warning 门禁。
- 版本锚点：5.0 的 USE_TZ 默认/db_default、5.1 的 async ORM 扩展、5.2 的复合主键与 py3.13。
- 冷检三件套：`makemigrations --check`、`migrate --plan`、`check --deploy`；迁移与代码解耦发布。

## 复盘追问
- 你的 Django 项目升级到 5.x 后 async 视图比例上升，线程池耗尽回归怎么测？
- 4.2 下 23 条 DeprecationWarning，按什么优先级清（会移除的先 vs 影响数据语义的先）？
