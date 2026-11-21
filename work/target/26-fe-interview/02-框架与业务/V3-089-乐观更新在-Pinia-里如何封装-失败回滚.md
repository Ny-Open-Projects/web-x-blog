---
title: [V3-089] 乐观更新在 Pinia 里如何封装（失败回滚）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-089：乐观更新在 Pinia 里如何封装（失败回滚）？
**答**：
- 乐观更新：请求发出前先改本地状态，用户零等待感知；成功后用服务端数据替换，失败则回滚。
- 关键是保留原状态快照（或记录插入位置），catch 里精确还原。
- 临时项用 `tmp-` 前缀 id 标记 pending 态，UI 可展示“发送中”。
- 并发场景下回滚要按引用定位，不能按 index（前面可能又插入了新项）。

```typescript
// stores/modules/comments.ts —— 乐观更新 + 失败回滚
import { defineStore } from "pinia";
import { ref } from "vue";
import { createComment, type Comment } from "@/services/comments";

export const useCommentStore = defineStore("comments", () => {
  const list = ref<Comment[]>([]);

  async function addComment(text: string) {
    // 1. 乐观插入临时项，UI 立即展示
    const temp: Comment = { id: `tmp-${Date.now()}`, text, pending: true };
    list.value.push(temp);

    // 2. 记录回滚动作：按引用定位，避免并发下 index 漂移
    const rollback = () => {
      const index = list.value.indexOf(temp);
      if (index > -1) list.value.splice(index, 1);
    };

    try {
      // 3. 服务端成功后用真实数据替换临时项
      const saved = await createComment(text);
      const index = list.value.indexOf(temp);
      if (index > -1) list.value.splice(index, 1, saved);
    } catch (e) {
      rollback(); // 4. 失败回滚，并向上抛出让 UI 提示
      throw e;
    }
  }

  return { list, addComment };
});
```
