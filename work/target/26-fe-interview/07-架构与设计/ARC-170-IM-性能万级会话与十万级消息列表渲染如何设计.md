---
title: [ARC-170] IM 性能：万级会话与十万级消息列表渲染如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-170：IM 性能：万级会话与十万级消息列表渲染如何设计？
**答**：
- 会话列表：虚拟滚动 + 增量排序（新消息只调整受影响会话的位置，用有序索引而不是全量 sort）；未读数聚合，避免每会话独立订阅推送放大（按需订阅可视区会话）。
- 消息列表难点是"逆向虚拟滚动"：锚定底部、向上加载历史时保持视觉位置不跳（锚点消息 offset 补偿）；图片/引用卡片高度不定，用测量缓存 + 预估高度双保险。
- 渲染降级：消息体按类型懒渲染（图片进视口才加载、长文本折叠），表情/提及等富文本用轻量模板而不是通用 markdown 全量解析。
- 数据层：IndexedDB 分页读取（按 seq 范围），内存窗口只保留当前会话 ± 若干页，切会话即时切换不卡顿。

```typescript
// 逆向虚拟滚动：向上加载保持锚点（核心逻辑）
class MessageListVirtualizer {
  private anchor: { msgId: string; offsetTop: number } | null = null;

  async prependHistory(): Promise<void> {
    // 1. 加载前记录锚点：当前视口顶部消息与其位置
    const top = this.getVisibleTopItem();
    this.anchor = { msgId: top.msgId, offsetTop: top.offsetTop };
    const older = await this.store.loadPrev(this.anchor.msgId, 30);   // IndexedDB 分页
    this.items = [...older, ...this.items];
    await this.measure(older);                          // 真实高度测量（缓存命中则跳过）
    // 2. 渲染后补偿：scrollTop += 新增内容总高度，视口停在原消息上不跳动
    const addedHeight = older.reduce((s, m) => s + this.heightCache.get(m.msgId)!, 0);
    this.scrollTop += addedHeight;
    this.anchor = null;
  }
  // 高度不定解法：先按类型预估渲染，measure 后校正
  estimateHeight(m: Message) { return TYPE_HEIGHT[m.type] ?? 64; }
  // 图片懒加载：进视口才换真图，加载完成高度变化走增量补偿
}
// 会话列表：新消息增量上浮（有序索引 map，不 sort 全量）
// 未读数：只订阅可视区会话的实时推送，离屏会话走红点聚合数
```
