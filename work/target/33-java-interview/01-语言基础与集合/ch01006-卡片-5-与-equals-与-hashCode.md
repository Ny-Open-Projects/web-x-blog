---
title: "卡片 5：== 与 equals 与 hashCode"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 5：== 与 equals 与 hashCode
- `==`：基本类型比值；引用类型比**地址**。
- `equals`：默认就是 ==（Object 源码 `return this == obj;`），重写后比内容。
- **契约**：重写 equals 必须重写 hashCode，否则 HashMap/HashSet 出错。
  契约内容：equals 相等 ⇒ hashCode 必须相等；hashCode 相等 ≠ equals 相等（哈希冲突）。
- 反例：只重写 equals 不重写 hashCode，两个"相等"的对象放进 HashSet 会出现两份。
