---
title: [XP-102] Electron 应用的数据存储怎么选型？SQLite、LevelDB 与其他方案对比？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-102：Electron 应用的数据存储怎么选型？SQLite、LevelDB 与其他方案对比？
**答**：
- 候选矩阵：**better-sqlite3**（关系查询、事务、WAL 高并发读——结构化业务数据首选）、**LevelDB/rocksdb 风格 KV**（高写入吞吐、无查询需求——日志缓冲、索引缓存）、**electron-store/JSON**（少量配置）、**IndexedDB**（渲染进程页面级数据）、**内存 Map + 落盘**（易变临时态）。
- 选型三问：数据要不要**查询与聚合**（要→SQLite）、写入是不是**高频追加**（是→KV/WAL）、要不要**多进程共享**（是→主进程独占 + IPC 服务化，SQLite 文件锁多进程写易脏）。
- 架构纪律：所有持久化收敛到主进程或 utilityProcess 的 **data service**，渲染进程经 IPC 访问（统一鉴权与迁移入口），禁止渲染进程各自落地存储（多窗口一致性，衔接 XP-104）。
- 迁移与体积：schema 版本表 + 增量迁移脚本；better-sqlite3 是原生模块，需按 Electron ABI 重编译（`electron-rebuild`）并纳入打包白名单。
- 数据安全：敏感字段应用层加密（safeStorage 存密钥）、定期 VACUUM/备份、磁盘满与损坏兜底（备份恢复链路演练）。

```javascript
// main/data/store.js —— better-sqlite3：WAL + 事务 + IPC 服务化
import Database from 'better-sqlite3';

export function openStore(file) {
  const db = new Database(file);
  db.pragma('journal_mode = WAL');        // 读写并发：写不阻塞读
  db.pragma('synchronous = NORMAL');      // WAL 下安全且更快
  db.pragma('busy_timeout = 3000');
  migrate(db);                            // schema 版本表 + 增量迁移
  return db;
}

const db = openStore(storePath);
// 事务批写：同步 API 但 O(1) 级开销，1w 行批量 insert 毫秒级
const insertMany = db.transaction((rows) => {
  const stmt = db.prepare('INSERT INTO tasks (id, name, state) VALUES (?, ?, ?)');
  for (const r of rows) stmt.run(r.id, r.name, r.state);
});

// 主进程数据服务：渲染进程一律 IPC 访问，禁止多进程直连 sqlite 文件
ipcMain.handle('data:tasks:list', (_e, filter) =>
  db.prepare('SELECT * FROM tasks WHERE state = ? ORDER BY created_at DESC LIMIT ?')
    .all(filter.state, filter.limit));
ipcMain.handle('data:tasks:create', (_e, row) =>
  db.prepare('INSERT INTO tasks ...').run(row));

// 选型落位：
//   任务/元数据/历史记录 → better-sqlite3（本文件）
//   日志缓冲与上报队列   → 内存 Map + 定期批量落 SQLite（高频追加不逐条写）
//   应用偏好设置         → electron-store（JSON，几十个 key）
//   页面级临时数据       → IndexedDB（渲染进程内，可丢弃）
```
