---
title: [Q6588] Django 4.2 到 5.0 升级破坏点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6588 · Django 4.2 → 5.0 升级破坏点与迁移路线

难度：P6 ｜ 标签：Django / 版本演进 / 升级

**问**：团队一套 Django 4.2 LTS 项目要升到 5.0/5.1 LTS 路线，涉及哪些破坏点？Python 版本、ORM 行为、模板与表单层各有什么要处理的？

**答**：
- **结论**：Django 5.0 的主要破坏点：① Python 最低版本升到 3.10（5.1 支持 3.13），升级 Django 前必须先确认 Python 基线；② ORM：`QuerySet.explain()` 参数校验更严、`Meta.constraints` 支持扩展，但一些隐式行为收紧——如 `bulk_create` 在有 `db_default` 字段时的返回值、`qs.update()` 对 `F()` 表达式的处理；③ 表单/模板：`django.forms` 的模板渲染全面切到 div-based 模板（旧 `<p>`/`<table>` 输出形态变了），依赖 DOM 结构的前端测试会碎；④ 移除项：`USE_TZ=False` 的隐性容忍降低、若干 4.x deprecation 到期移除（如 `STATICFILES_STORAGE`/`DEFAULT_FILE_STORAGE` 换成 STORAGES 字典）。这些属于"文档能查到的破坏点"，真正的坑在第三方插件（django-filters、django-rest-framework 版本矩阵）。
- **取舍**：升级路线选择：4.2 LTS → 5.2 LTS 一步到位（省一次中间迁移）vs 先 5.0 再 5.2（每步破坏面小、易回滚）。依赖矩阵强的团队（DRF、celery、插件多）建议分步；干净项目可一步。升级窗口配合 Python 3.12 升级时要警惕，一次改两个大变量会让回归面无法归因。
- **实战**：步骤：① 先跑 `python -Wd`（把 DeprecationWarning 变可见）在 4.2 下清掉所有弃用告警——Django 的弃用周期是两个版本，4.2 的告警就是 5.x 的雷；② CI 建立"升级分支 + 全量测试 + 兼容层"流程，第三方插件逐个核对 release note 的 Django 5 支持版本；③ div-based 表单模板：给依赖旧 DOM 的测试加显式 `django.forms.renderers` 回退，分批迁移前端断言；④ 复盘项：把"每半年跟随一次 Django 小版本"写进维护日历，避免再攒出跨两个 LTS 的大迁移。

```python
# Django 升级前的 deprecation 告警扫描器（纯标准库模拟）
# 基线：Python 3.10+（Django 5.0 最低版本）

import warnings


DEPRECATIONS_4_2 = [
    ("STATICFILES_STORAGE", "4.2", "5.1"),
    ("DEFAULT_FILE_STORAGE", "4.2", "5.1"),
    ("USE_TZ implicit False", "5.0", "5.1"),
]


def scan_settings(settings: dict) -> list[str]:
    """模拟升级检查：settings 里是否用了将被移除的项"""
    hits = []
    for key, since, removed in DEPRECATIONS_4_2:
        if key in settings:
            hits.append(
                f"[{key}] deprecated since {since}, "
                f"removed in {removed} -> 迁移到 STORAGES/显式配置"
            )
    return hits


def main() -> None:
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("USE_TZ not set", DeprecationWarning)
        assert len(w) == 1
    fake_settings = {"STATICFILES_STORAGE": "django.contrib..."}
    for msg in scan_settings(fake_settings):
        print(msg)
    assert len(scan_settings(fake_settings)) == 1
    clean = scan_settings({"STORAGES": {}})
    assert clean == []
    print("OK: 升级前清零弃用告警")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 Django 的弃用策略能用来规划升级？
→ 一句话提示：Django 承诺"弃用后保留两个特性版本、在 A.B 后的 A+2.0 移除"，因此在 4.2 上用 `-Wd` 跑清所有 DeprecationWarning，升 5.x 就不会有移除项击穿——这是可规划的迁移而非赌博。

**追问 2**：`STORAGES` 字典替代两个独立 setting，解决的是什么问题？
→ 一句话提示：旧的两个全局 setting 无法表达"不同用途用不同存储"的组合；STORAGES 按 key（default/staticfiles）映射引擎与选项，是一处配置的收敛，迁移时旧 setting 会被忽略而不是报错，要靠检查清单兜底。

## 背诵要点
- Django 5.0 破坏面：Python ≥3.10、STORAGES 字典、div-based 表单模板、ORM 隐式行为收紧。
- 升级黄金法则：4.2 用 `python -Wd` 清零 DeprecationWarning 再升；第三方插件版本矩阵逐个核对。
- LTS 路线选择：依赖矩阵复杂分步升（4.2→5.0→5.2），干净项目一步 4.2→5.2；避免与 Python 大版本升级同批。

## 复盘追问
- 为什么"一次升 Django + 一次升 Python"要拆开？提示：两个大变量的失败无法归因，回归面爆炸；每次只动一个基线变量，出问题二分定位。
- 表单渲染从 `<p>` 改 `<div>` 为什么会击穿"后端团队"？提示：大量前向测试和 JS 选择器绑死了 DOM 结构；后端渲染形态变更本质是前端契约变更，要用 renderer 配置做缓冲、分批迁移断言。
