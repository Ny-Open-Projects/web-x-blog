---
title: [XP-189] Electron 数据存储：本地数据库选型（SQLite/LevelDB）
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-189：Electron 数据存储：本地数据库选型（SQLite/LevelDB）

**答**：
- 本地存储选型：key-value（LevelDB/IndexedDB）vs 关系（SQLite/better-sqlite3）vs 文件（JSON/NDJSON）——按查询需求选。
- SQLite：复杂查询/事务/大量记录（如离线消息历史）；LevelDB：高性能 KV（缓存/配置）；JSON 文件：配置类（简单）。
- 同步 vs 异步：better-sqlite3 同步（主进程阻塞风险——数据量小可用）；异步版或 utility process 处理大数据。

```javascript
// 数据库选型决策
const storageDecision = {
  keyvalue: { use: '缓存/配置/设置', impl: 'LevelDB / conf 包',
    note: 'O(1) 读写，无查询能力' },
  sqlite: { use: '消息历史/日志/结构化数据',
    impl: 'better-sqlite3（同步，快）或 sql.js（WASM，兼容好）',
    note: '支持 SQL 查询/事务/索引' },
  jsonFile: { use: '配置文件/小数据', impl: 'JSON/NDJSON', note: '简单但无并发安全' },
};
// SQLite 大数据：放 utility process（不阻塞主进程）
const dbWorker = new UtilityProcess('db-worker.js');             // 独立进程
dbWorker.postMessage({ op: 'query', sql: 'SELECT * FROM messages LIMIT 100' });
```
