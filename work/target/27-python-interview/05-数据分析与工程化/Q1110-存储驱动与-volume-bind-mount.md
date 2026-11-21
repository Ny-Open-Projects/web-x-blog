---
title: [Q1110] 存储驱动与 volume/bind mount
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1110 · 存储驱动与 volume/bind mount

> 难度:★★★☆ | 标签:Docker, 存储

**问**:overlay2 是什么?数据库数据为什么必须放 volume 而不是容器层?

**答**:overlay2 是镜像层叠文件系统:多个只读镜像层 + 一个容器可写层,读文件逐层向上找,写文件走写时复制(COW)到可写层,容器删除可写层即消失。数据持久化的三种挂载:volume(docker 管理,生命周期独立,性能好,生产首选)、bind mount(宿主机目录直挂,开发热加载方便,注意权限映射)、tmpfs(内存文件系统,敏感临时数据)。数据库高频写入放容器层会走 COW 变慢且随容器销毁丢失,必须 volume。

```python
# file: code/05_数据分析与工程化/q1110_docker_storage.py

MOUNTS = {
    "volume": "docker 管理 生命周期独立 数据库等持久数据首选",
    "bind mount": "宿主机目录直挂 开发热加载注意 uid 权限映射",
    "tmpfs": "内存文件系统 敏感临时数据 容器停止即消失",
}

if __name__ == "__main__":
    for k, v in MOUNTS.items():
        print(f"{k:<12} {v}")
    print("""
存储驱动 overlay2:镜像只读层 + 容器可写层 写时复制
高频写入放 volume 避免写穿容器层
""")
    print("$ docker run -v pgdata:/var/lib/postgresql/data postgres")
    print("$ docker run -v $(pwd)/app:/app -w /app python:3.12 python main.py")
```

**追问**:
- 追问 1:镜像层和容器层怎么看?—— `docker history 镜像` 看各层大小与指令,`docker diff 容器` 看可写层改动。
- 追问 2:volume 数据怎么备份?—— `docker run --rm -v pgdata:/data -v $(pwd):/backup alpine tar czf /backup/pg.tgz /data`。
