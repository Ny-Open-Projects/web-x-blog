---
title: [Q164] Alembic 数据库迁移管理
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q164 · Alembic 数据库迁移管理

> 难度:★★★ | 标签:SQLAlchemy, Alembic, 迁移

**问**:团队如何管理表结构变更?说说 Alembic 的工作流程。

**答**:Alembic 为每次变更生成带版本号的迁移脚本(up/down),数据库用 alembic_version 表记录当前版本,`upgrade head` 按链回放未应用脚本。流程:模型变更 → `alembic revision --autogenerate` 生成差异 → 人工审查脚本 → 测试库验证 → 各环境 `upgrade head`。要点:autogenerate 结果必须人工检查(它识别不了改列名等语义变更),脚本只前进不修改历史。

```python
# file: code/04_数据库与缓存/q164_alembic_workflow.py
"""封装常用 Alembic 命令; 未安装时打印等价手工命令"""
import shutil
import subprocess

STEPS = [
    (["alembic", "init", "migrations"], "初始化迁移目录(仅首次)"),
    (["alembic", "revision", "--autogenerate", "-m", "add orders table"], "生成差异脚本"),
    (["alembic", "upgrade", "head"], "应用全部待执行迁移"),
    (["alembic", "downgrade", "-1"], "回滚上一个版本"),
    (["alembic", "history", "--verbose"], "查看版本链"),
]

if __name__ == "__main__":
    has_alembic = shutil.which("alembic") is not None
    for cmd, desc in STEPS:
        print(f"[{desc}] {' '.join(cmd)}")
        if has_alembic and cmd[0:2] == ["alembic", "history"]:
            subprocess.run(cmd, check=False)
    # env.py 关键配置: target_metadata = 模型 Base.metadata
    # sqlalchemy.url 建议从环境变量读取, 避免把生产连接串写进仓库
```

**追问**:
- autogenerate 有什么坑?——无法感知列重命名(会生成 drop+add 丢数据)、服务端默认值和部分索引,必须人工审查。
- 多人并行开发版本冲突怎么办?——出现多 heads 时用 `alembic merge` 合并版本链。

---
