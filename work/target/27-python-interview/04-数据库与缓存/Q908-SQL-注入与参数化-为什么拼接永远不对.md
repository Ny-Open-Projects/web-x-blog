---
title: [Q908] SQL 注入与参数化: 为什么拼接永远不对
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q908 · SQL 注入与参数化: 为什么拼接永远不对

> 难度:★★★☆ | 标签:安全, 参数化

**问**:什么是 SQL 注入?参数化查询为什么能防住?ORM 还有风险吗?

**答**:注入的本质是"数据被当作代码执行":字符串拼接把用户输入嵌进 SQL 结构,攻击者用引号闭合原语句再附加任意逻辑(绕过 WHERE、UNION 拖库、堆叠语句)。参数化(prepared statement)把 SQL 结构与数据分离——SQL 先编译成模板,参数只作为绑定值填入占位符,永远不会改变语句结构,所以注入无从谈起。ORM 默认参数化,风险残留点:text() 拼接、动态表名/列名/排序字段(无法参数化,必须白名单校验)、存储过程动态拼接、日志与第三方接口的二次注入。原则:结构白名单,数据全参数化。

```python
# file: code/04_数据库与缓存/q908_sql_injection.py
"""同一条登录查询: 拼接被注入绕过, 参数化安全"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE user (name TEXT, pwd TEXT)")
        conn.execute("INSERT INTO user VALUES ('admin', 's3cret')")

        evil = "' OR '1'='1"          # 攻击payload

        # 反面教材: f-string 拼接
        unsafe = f"SELECT * FROM user WHERE name='{evil}' AND pwd='x'"
        print("拼接查询返回:", conn.execute(unsafe).fetchall(), "<- 全表绕过")

        # 正确: 参数化
        safe = "SELECT * FROM user WHERE name = ? AND pwd = ?"
        print("参数化查询返回:", conn.execute(safe, (evil, "x")).fetchall(), "<- 当作普通字符串查无此人")
```

**追问**:
- 表名排序字段为什么不能参数化?——占位符只能绑"值",标识符在编译期就定型,动态结构只能白名单映射到允许的列名。
- 参数化能防越权吗?——不能,注入与权限是两回事,仍需最小权限账号、行级过滤与业务层鉴权。

---
