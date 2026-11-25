---
title: [SCN-139] 创作者后台的富文本草稿，要求 PC 写一半、手机上能接着写，怎么做多端同步？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-139：创作者后台的富文本草稿，要求 PC 写一半、手机上能接着写，怎么做多端同步？
**答**：
- 本地先行：每次编辑防抖 2s 写入 IndexedDB（草稿 id 为 key），弱网/未登录也不丢。
- 云端同步带版本：`draft = { content, baseVersion, updatedAt }`，PUT 时带 baseVersion 做乐观锁；冲突时不能默默覆盖——保留两版让用户选。
- 内容用结构化 JSON（而不是 HTML 字符串）同步，多端渲染器各自还原，规避不同端富文本实现的标签差异。
- 网络恢复后统一 flush：监听 online 事件 + 启动时扫描"脏草稿"队列。

```javascript
// 富文本草稿多端同步：IndexedDB 先行 + 乐观锁 + 冲突双版本
const DB_NAME = 'drafts', STORE = 'draft';
const db = indexedDB.open(DB_NAME, 1);
db.onupgradeneeded = e => e.target.result.createObjectStore(STORE, { keyPath: 'id' });

export async function saveLocal(draft) {
  const store = (await db).transaction(STORE, 'readwrite').objectStore(STORE);
  store.put({ ...draft, dirty: true });                // 本地先行，标脏
}

export function debounceSync(draftId, getDraft, wait = 2000) {
  let timer;
  return () => {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      await saveLocal(getDraft());
      try {
        const d = getDraft();
        await api.putDraft(draftId, { content: d.content, baseVersion: d.version }); // 乐观锁
        saveLocal({ ...d, version: d.version + 1, dirty: false });
      } catch (e) {
        if (e.code === 'VERSION_CONFLICT') {           // 冲突：不覆盖，双版本让用户选
          const remote = await api.getDraft(draftId);
          saveConflict(draftId, { mine: getDraft(), theirs: remote });
        }
        // 网络失败保持 dirty，等 online 再 flush
      }
    }, wait);
  };
}

window.addEventListener('online', flushDirtyDrafts);   // 网络恢复统一补交
async function flushDirtyDrafts() {
  const dirty = await listDirtyDrafts();
  dirty.forEach(d => debounceSync(d.id, () => d, 0)());
}

function saveConflict(id, pair) {
  localStorage.setItem(`conflict:${id}`, JSON.stringify(pair));
}
```
