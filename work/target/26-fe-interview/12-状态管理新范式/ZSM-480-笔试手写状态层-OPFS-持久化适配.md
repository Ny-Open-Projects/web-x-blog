---
title: [ZSM-480] 笔试：手写状态层 OPFS 持久化适配
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-480：手写状态层 OPFS 持久化适配
**答**：实现 OPFS（Origin Private File System）存储适配器 `createOPFSStorage(dir)`：1) 符合 persist 的 storage 接口：getItem/setItem/removeItem（异步）；2) 每个状态一个文件（`/state/${key}.json`），原子写：写临时文件 → rename（OPFS move 原子性）；3) 读取容错：文件不存在返回 null、JSON 损坏删除重读 null；4) 大状态（>5MB）自动分片存储（`key.part0/part1`，读取时拼接）；5) 能力检测：OPFS 不可用回退 IndexedDB/null（调用方降级）。

```javascript
export async function createOPFSStorage() {
  const hasOPFS = 'storage' in navigator && 'getDirectory' in navigator.storage
  if (!hasOPFS) return null                                       // 能力检测 → 调用方降级

  const root = await navigator.storage.getDirectory()
  const dir = await root.getDirectoryHandle('state', { create: true })

  async function fileHandle(key) { return dir.getFileHandle(`${sanitize(key)}.json`, { create: true }) }

  return {
    async getItem(key) {
      try {
        const fh = await fileHandle(key)
        const text = await (await fh.getFile()).text()
        try { return JSON.parse(text) }
        catch { await this.removeItem(key); return null }         // 损坏删除重读 null
      } catch { return null }                                     // 不存在 → null
    },
    async setItem(key, value) {
      const tmp = await dir.getFileHandle(`${sanitize(key)}.tmp`, { create: true })
      const w = await tmp.createWritable()                        // 先写临时
      await w.write(JSON.stringify(value))
      await w.close()
      const src = await dir.getFileHandle(`${sanitize(key)}.tmp`)
      await src.move(await fileHandle(key))                       // 原子 rename
    },
    async removeItem(key) {
      try { await dir.removeEntry(`${sanitize(key)}.json`) } catch { /* 幂等 */ }
    },
  }
}

function sanitize(key) { return key.replace(/[^a-zA-Z0-9_-]/g, '_') }
```
**评分点**：
- persist storage 接口契约（getItem/setItem/removeItem，全异步）
- 原子写协议（tmp + move）——直接写目标文件崩溃会留半截 JSON
- 读取三层容错（不存在 null / 损坏删除重读 / JSON parse 隔离）
- 能力检测返回 null（调用方降级到 IndexedDB/内存）——适配器不做降级决策
