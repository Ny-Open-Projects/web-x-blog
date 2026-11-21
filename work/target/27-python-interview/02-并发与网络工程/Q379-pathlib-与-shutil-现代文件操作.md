---
title: [Q379] pathlib 与 shutil:现代文件操作
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q379 · pathlib 与 shutil:现代文件操作

> 难度:★★☆ | 标签:pathlib, shutil, 文件 IO

**问**:pathlib 相比 os.path 好在哪?批量备份一个目录用什么?

**答**:pathlib 用 `/` 运算符拼路径、面向对象、跨平台,`Path.glob`/`rglob`/`read_text`/`with_suffix` 一气呵成,替代 `os.path.join` 的字符串拼接。批量复制/归档用 `shutil.copy2`(保留元数据)、`shutil.copytree`、`shutil.make_archive`、`shutil.rmtree`、`shutil.move`,以及 `glob` 过滤。注意 `rmtree` 不可恢复,先校验路径前缀。

```python
# file: code/02_并发与网络工程/q379_pathlib_shutil.py
"""pathlib + shutil:构建与打包一个项目快照。"""
import shutil
import tempfile
from pathlib import Path

if __name__ == "__main__":
    project = Path(tempfile.mkdtemp()) / "myproj"
    src = project / "src"
    src.mkdir(parents=True)
    (src / "main.py").write_text("print('hi')", encoding="utf-8")
    (project / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")
    (project / "cache.tmp").write_text("junk", encoding="utf-8")

    # pathlib 遍历:只找 .py 文件
    for py in project.rglob("*.py"):
        print("py file:", py.relative_to(project), py.stat().st_size, "bytes")

    # shutil.copytree 备份,忽略 tmp 文件
    backup = project.parent / "myproj_backup"
    if backup.exists():
        shutil.rmtree(backup)
    shutil.copytree(project, backup, ignore=shutil.ignore_patterns("*.tmp"))

    # 打 zip 归档
    archive = shutil.make_archive(str(project.parent / "snapshot"), "zip",
                                  root_dir=str(backup))
    print("archive:", archive, Path(archive).stat().st_size, "bytes")
    print("备份内容:", sorted(p.name for p in backup.rglob("*")))
```

**追问**:
- `copyfile`/`copy`/`copy2` 区别?`copyfile` 只拷内容;`copy` 尽量保留权限;`copy2` 连 mtime 等元数据一起保留,备份首选。
- 大文件拷贝怎么省 IO?`shutil.copyfile` 底层用 `os.sendfile`/`fcopyfile` 零拷贝,比自己逐块读快。
