---
title: [Q956] ORM 与缓存结合: 读路径薄缓存与失效
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q956 · ORM 与缓存结合: 读路径薄缓存与失效

> 难度:★★★★ | 标签:缓存, 架构

**问**:ORM 查询结果能缓存吗?失效怎么做才可靠?

**答**:可以,但只对"按主键取实体"这类稳定查询做薄缓存:cache key = 实体类 + id + 版本,值是可序列化的 DTO(不是 ORM 实体——携带 session 状态)。失效三种策略:一、TTL 短窗(30~60s)容忍短暂陈旧,最简单;二、写路径主动失效——Repository save/commit 后按受影响实体键删除缓存,与 Q178 的旁路缓存一致;三、版本号/代际——表级 version 递增,key 带版本,写一次全部失效(实现简单但写频繁时缓存命中率崩)。纪律:缓存层放 Repository 之上或之下要全团队统一;统计类实时查询不缓存而走物化汇总;永远缓存 DTO,杜绝 detached ORM 对象跨请求复用。

```python
# file: code/04_数据库与缓存/q956_orm_cache.py
"""主键级薄缓存: 读走缓存 写后失效"""
import time

class FakeCache:
    def __init__(self):
        self._data = {}

    def get(self, key):
        item = self._data.get(key)
        if item and item[0] > time.monotonic():
            return item[1]
        return None

    def set(self, key, value, ttl):
        self._data[key] = (time.monotonic() + ttl, value)

    def delete(self, key):
        self._data.pop(key, None)

class UserRepo:
    def __init__(self, db, cache):
        self.db, self.cache = db, cache
        self.hits = self.miss = 0

    def get(self, uid):
        key = f"user:{uid}"
        if (v := self.cache.get(key)) is not None:
            self.hits += 1
            return v
        self.miss += 1
        row = self.db.get(uid)                    # 模拟 DB 查询
        if row:
            self.cache.set(key, row, ttl=60)
        return row

    def save(self, uid, row):
        self.db[uid] = row
        self.cache.delete(f"user:{uid}")          # 写后失效

if __name__ == "__main__":
    db = {1: {"name": "alice"}}
    repo = UserRepo(db, FakeCache())
    print(repo.get(1), "miss")
    print(repo.get(1), "hit")
    repo.save(1, {"name": "alice2"})
    print(repo.get(1), "失效后回源")
    print(f"命中率统计: {repo.hits} hit / {repo.miss} miss")
```

**追问**:
- 为什么缓存 ORM 实体是坑?——实体绑定 session 与懒加载代理,跨请求复用会触发 DetachedInstanceError 或陈旧脏读,DTO 才是缓存的正确单位。
- 表级版本失效的代价?——一次写把该表所有缓存清空,写多的表命中率接近零,只适合配置类、类目类低频写数据。

---
