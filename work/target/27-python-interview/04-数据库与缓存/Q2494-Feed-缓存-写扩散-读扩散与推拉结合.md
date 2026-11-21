---
title: [Q2494] Feed 缓存: 写扩散 读扩散与推拉结合
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2494 · Feed 缓存: 写扩散 读扩散与推拉结合

> 难度:★★★★ | 标签:架构, Feed

**问**:时间线(Timeline)缓存为什么不能一套策略走天下?

**答**:因为写扩散和读扩散的代价分布相反。写扩散(push):发帖时写入每个粉丝的收件箱,读时只取自己的收件箱——读 O(1),但大 V 发帖就是百万次写,扇出风暴;读扩散(pull):发帖不写任何人的收件箱,读时实时聚合所有关注对象——写 O(1),但每次刷时间线的代价是 O(关注数)。推拉结合是标准折中:普通人发帖走推(粉丝少,扇出便宜),大 V 发帖走拉(粉丝太多,不扇出),读者刷时间线时合并"收件箱 + 关注的大 V 的最新帖"。实测百万粉大 V 场景:纯推的写操作 100 万,推拉只要 1200,读操作只多了一档。

```python
# file: code/04_数据库与缓存/q2494_feed_push_pull.py
"""Feed 缓存: 写扩散 读扩散与推拉结合的算术"""
users = {"bigv": {"followers": 1000000}}
for i in range(1, 11):
    users["u%d" % i] = {"followers": 12}
FOLLOWING = {name: 10 + 1 for name in users if name != "bigv"}   # 关注 10 个普通人 + 大 V
POSTS_NORMAL = 10                                                # 每个普通人发 1 条
POSTS_BIGV = 1

def simulate(mode):
    write_ops = read_ops = 0
    for name in users:
        if name == "bigv":
            if mode in ("push", "push_pull"):        # 大 V 的帖子是否扇出?
                if mode == "push":
                    write_ops += users["bigv"]["followers"] * POSTS_BIGV
                # push_pull: 大 V 走拉, 不扇出
            else:
                pass                                  # pull: 不扇出
        else:
            if mode in ("push", "push_pull"):
                write_ops += users[name]["followers"] * POSTS_NORMAL
    for name in users:
        if name == "bigv":
            continue
        if mode == "push":
            read_ops += 1                             # 只读自己收件箱
        elif mode == "pull":
            read_ops += FOLLOWING[name]               # 聚合所有关注对象的发件箱
        else:
            read_ops += 1 + 1                         # 收件箱 + 拉一次大 V
    return write_ops, read_ops

print("%-12s %14s %14s" % ("策略", "写操作", "读操作"))
for mode, label in [("push", "纯写扩散"), ("pull", "纯读扩散"), ("push_pull", "推拉结合")]:
    w, r = simulate(mode)
    print("%-12s %14d %14d" % (label, w, r))
print("场景: 大 V 百万粉丝, 其余用户十几个粉丝; 大 V 发 1 条, 普通用户各发 1 条")
print("结论: 写扩散把读做便宜但大 V 发帖就是事故, 读扩散把写做便宜但读聚合是 O(关注数),")
print("      推拉结合让大 V 走拉 普通人走推, 是粉丝量悬殊时的标准折中")
```

**追问**:
- 推拉的阈值怎么定?—— 按作者粉丝数分档(如超过 1 万走拉),阈值要可配置并配合扇出任务的异步化。
- 收件箱缓存放什么结构?—— Redis zset(分数为时间戳)支持按时间范围拉取与分页,配合修剪策略控长。

---
