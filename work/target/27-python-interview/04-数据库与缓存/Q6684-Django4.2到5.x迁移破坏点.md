---
title: [Q6684] Django 4.2 LTS 到 5.x 迁移破坏点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6684 · Django 4.2 LTS → 5.0/5.1/5.2 迁移：破坏点清单与升级剧本

难度：P6 ｜ 标签：版本演进、Django、ORM 迁移
基线：Django 4.2 LTS（Python 3.8-3.12）→ 5.0（3.10+）→ 5.1 → 5.2 LTS（3.10-3.13）。

**问**：团队把一个 Django 4.2 的服务升到 5.2 LTS，`pip install -U django` 之后跑起来就报错。4.2→5.2 有哪些必踩的破坏点？升级的正确顺序是什么？

**答**：**结论**：三块必踩：① **Python 版本硬门**——Django 5.0 起要求 Python 3.10+，升级 Django 前先升 Python，顺序错了 `pip install` 阶段就解不出依赖；② **ORM/表单移除项**——4.x 弃用的 API 在 5.0 被移除，典型如 `django.utils.timezone.utc`（改用 `datetime.timezone.utc`）、`USE_TZ=False` 下的部分行为收紧、`form.renderer` 默认变化影响自定义模板；③ **模型默认行为**——Django 5.0 起 `Model.save()`/`QuerySet.update` 对 `auto_now` 与表达式默认值处理变化（`db_default` 新特性引入后与旧 `default` 混用的语义差异），以及 `QuerySet.explain` 各后端参数收紧。另外 `DEFAULT_AUTO_FIELD` 若仍是大迁移遗留的 `AutoField`，升 5.x 时最好一并规范成 `BigAutoField`，否则新表主键仍是 32 位。

**取舍**：升级策略选"LTS 直达 + 分支隔离"：4.2 LTS → 5.2 LTS 跳过 5.0/5.1，官方支持 LTS 间直达，但**弃用检查必须先跑满**——在 4.2 上开 `-W error::DeprecationWarning`（或 `SILENCED_SYSTEM_CHECKS` 清零）跑全量测试，把弃用 API 清干净后 5.2 一次通过的把握才高。反过来逐版本 4.2→5.0→5.1→5.2 也能走，工作量分散但 CI 矩阵要维护三套。团队规模小选直达，选逐级。

**实战**：升级剧本四步：依赖矩阵确认 → 弃用清零 → 测试与 `manage.py check --deploy` → 灰度环境跑真实流量。用脚本核对破坏点：

```python
# Django 4.2 -> 5.2 升级预检脚本（不依赖 Django，检查项目源码信号）
import ast, pathlib, sys

# 4.2 弃用且 5.0 移除的常见符号
REMOVED = [
    "django.utils.timezone.utc",      # -> datetime.timezone.utc
    "django.contrib.postgres.fields.CICharField",  # 改用 CICharField 的 collation 方案
    "USE_L10N",                        # 4.0 起废弃，5.0 移除
    "get_storage_class",               # -> django.core.files.storage.storages
]
CHECKS = {
    "python_requires": (3, 10),        # Django 5.x 最低 3.10
    "default_auto_field": "BigAutoField",
}

def scan(root: str) -> list[str]:
    issues = []
    for p in pathlib.Path(root).rglob("*.py"):
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError as e:
            issues.append(f"{p}: 语法错误 {e}")
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                for alias in node.names:
                    mod = f"{node.module}.{alias.name}" if alias.name != "*" else node.module
                for sym in REMOVED:
                    base = sym.split(".")[0]
                    if node.module.startswith(base) and sym.split(".")[-1] in mod:
                        issues.append(f"{p}:{node.lineno} 引用了移除项 {mod}")
                        break
            if isinstance(node, ast.Import):
                for a in node.names:
                    for sym in REMOVED:
                        if sym.split(".")[0] in a.name and sym.split(".")[-1] in a.name:
                            issues.append(f"{p}:{node.lineno} 引用了移除项 {a.name}")
    return issues

if __name__ == "__main__":
    # 无参数时用临时目录自演示，避免误扫整个工作区
    import tempfile
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = tempfile.mkdtemp()
        (pathlib.Path(root) / "demo.py").write_text(
            "from django.utils.timezone import utc\n"
            "from django.conf import settings\n"
            "settings.USE_L10N = True\n", encoding="utf-8")
    found = scan(root)
    print(f"扫描完成：{len(found)} 个疑似破坏点")
    for f in found[:10]:
        print(" -", f)
    print("后续动作：python -W error::DeprecationWarning manage.py test")
```

**追问 1**：为什么要在旧版本上先跑 `-W error::DeprecationWarning` 再升级，而不是升级后修？
提示：4.2 的弃用警告就是 5.x 的移除清单，先清零等于提前消化 5.x 的破坏面；升级后再修会陷入"升不上来也回不去"的中间态。

**追问 2**：`USE_TZ` 相关在 5.x 有什么坑？
提示：5.0 起对 naive datetime 与 aware datetime 的比较更严格，`timezone.now()` 在 `USE_TZ=False` 下也返回 aware 时间的项目要自查模型 default 与序列化层，跨时区字段建议迁移期统一 aware。

**追问 3**：第三方包（django-filter、django-storages 等）版本怎么跟着动？
提示：按 Django 版本的支持矩阵逐一升，先在 CI 里用 pip-tools/uv 锁定矩阵；任何包不支持 5.2 时优先找替代或 fork 修补，不回退 Django。

## 背诵要点
1. 4.2→5.2 三大破坏面：Python 3.10+ 硬门、4.x 弃用 API 在 5.0 移除（timezone.utc / USE_L10N / get_storage_class）、ORM 默认行为收紧。
2. 升级顺序：Python 先行 → 旧版上 `-W error::DeprecationWarning` 清零 → LTS 直达 → `check --deploy` + 灰度。
3. `DEFAULT_AUTO_FIELD` 统一 `BigAutoField`，避免新表残留 32 位主键。

## 复盘追问
1. 你们的 Django 项目 CI 里有没有把 DeprecationWarning 当错误的门禁？没有的话，这次升级暴露了多少存量弃用？
2. 升级后哪些第三方包成了阻塞项？当时的锁文件策略（pip freeze / uv lock）能否快速回滚？
