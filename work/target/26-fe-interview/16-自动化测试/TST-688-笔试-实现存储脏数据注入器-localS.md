---
title: [TST-688] 笔试：实现存储脏数据注入器（localStorage / sessionStorage）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-688：笔试：实现存储脏数据注入器（localStorage / sessionStorage）

**题目**：实现 dirtyInjector(storage,keys,{version})：备份后按随机类型注入 bad-json/null/旧版本数据，返回 restore 精确还原；另实现 safeRead(storage,key,fallback) 解析失败或版本缺失返回 fallback。

**答**：
- 支持三类脏数据：非法 JSON、null、过期版本（version < 当前）。
- 注入前备份原值，返回 restore 精确还原。
- 提供 safeRead 辅助：解析失败返回默认值而不抛错。

```javascript
function dirtyInjector(storage, keys, { version = 1 } = {}) {
  const backup = new Map();
  const kinds = ['bad-json', 'null', 'old-version'];
  keys.forEach(k => {
    backup.set(k, storage.getItem(k));
    const kind = kinds[Math.floor(Math.random() * kinds.length)];
    const val = kind === 'bad-json' ? '{oops'
      : kind === 'null' ? 'null'
      : JSON.stringify({ version: version - 1 });
    storage.setItem(k, val);
  });
  return {
    restore: () => backup.forEach((v, k) =>
      v == null ? storage.removeItem(k) : storage.setItem(k, v)),
  };
}
function safeRead(storage, key, fallback) {
  try {
    const v = JSON.parse(storage.getItem(key));
    return v && v.version !== undefined ? v : fallback;
  } catch (_) { return fallback; }
}
```

**评分点**：
- 三类脏数据注入正确
- 备份与还原精确
- safeRead 容错不抛错
- 版本校验逻辑清晰
