---
title: [AGT-150] 消息树与分支对话（regenerate / 多版本对比）的状态管理怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-150：消息树与分支对话（regenerate / 多版本对比）的状态管理怎么实现？
**答**：
- 线性数组撑不住 regenerate：重新生成不是覆盖旧答案，而是新建兄弟分支，用户可来回切换比较——数据模型要从「消息数组」升级为「消息树」。
- 树结构：每条消息存 `parentId`，会话只存根 id；「当前路径」是从根到叶的一条链，切换分支 = 换子节点索引。
- 关键状态：每个节点记录 `children: string[]` 与 `activeChildIndex`，regenerate 在同一 parent 下 append 子节点并切换激活；编辑历史消息则在其后新建分支子树。
- UI 要点：在有多分支的节点上显示 `< 2/3 >` 导航器；token 成本与评价数据挂在节点上做分支间对比。

```typescript
// 消息树：regenerate 建分支 + 路径切换
import { reactive } from 'vue';

interface MsgNode { id: string; parentId: string | null; role: 'user' | 'assistant';
  content: string; children: string[]; activeChildIndex: number; meta?: { model?: string; costUsd?: number; rating?: 1 | -1 }; }

export function useMessageTree() {
  const nodes = reactive<Record<string, MsgNode>>({});
  const rootId = 'root';
  nodes[rootId] = { id: rootId, parentId: null, role: 'user', content: '', children: [], activeChildIndex: 0 };

  const currentPath = (): MsgNode[] => {                       // 根到叶的激活链
    const path: MsgNode[] = [];
    let cur = nodes[rootId];
    while (cur.children.length) {
      path.push(cur);
      cur = nodes[cur.children[cur.activeChildIndex]];
    }
    path.push(cur);
    return path;
  };

  function append(parentId: string, msg: Omit<MsgNode, 'id' | 'parentId' | 'children' | 'activeChildIndex'>): string {
    const id = crypto.randomUUID();
    nodes[id] = { ...msg, id, parentId, children: [], activeChildIndex: 0 };
    const p = nodes[parentId];
    p.children.push(id);
    p.activeChildIndex = p.children.length - 1;               // 新分支自动激活
    return id;
  }

  function regenerate(assistantId: string, newText: string, meta: MsgNode['meta']) {
    const node = nodes[assistantId];
    return append(node.parentId!, { role: 'assistant', content: newText, meta }); // 兄弟分支，不覆盖
  }

  function switchBranch(parentId: string, dir: 1 | -1) {
    const p = nodes[parentId];
    p.activeChildIndex = Math.min(Math.max(p.activeChildIndex + dir, 0), p.children.length - 1);
  }

  return { nodes, rootId, currentPath, append, regenerate, switchBranch };
}
```
