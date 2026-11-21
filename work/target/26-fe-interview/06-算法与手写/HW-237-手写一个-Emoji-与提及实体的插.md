---
title: [HW-237] 手写一个 Emoji 与提及实体的插入与序列化
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-237：手写一个 Emoji 与提及实体的插入与序列化

**答**：
- 需求：实现 EntityEditor：插入实体（emoji / mention @用户）为不可分割原子（内部用占位符 \uFFFC + 实体表映射），光标处插入后光标落在实体后；删除时实体整体删除（一次 Backspace）；序列化时把占位符替换回实体标记（mention → `[mention:id]`，emoji → unicode）。
- 边界：占位符不可被部分选中删除（选区含实体时删除单位为实体）；粘贴含占位符文本要重建实体映射；跨 block 复制粘贴保持实体。
- 评分点：原子删除；序列化双向；粘贴重建映射。

```javascript
class EntityEditor {
  constructor() { this.doc = ''; this.entities = new Map(); }   // key(占位符) -> entity
  insert(entity, pos) {
    const key = '\uFFFC' + this.entities.size + '\uFFFC';
    this.entities.set(key, entity);
    this.doc = this.doc.slice(0, pos) + key + this.doc.slice(pos);
    return pos + key.length;                                   // 光标在实体后
  }
  backspace(pos) {                                             // 原子删除
    const before = this.doc.slice(0, pos);
    const m = /\uFFFC\d+\uFFFC$/.exec(before);
    if (m) { this.doc = before.slice(0, -m[0].length) + this.doc.slice(pos);
      this.entities.delete(m[0]); return pos - m[0].length; }
    this.doc = before.slice(0, -1) + this.doc.slice(pos);
    return pos - 1;
  }
  serialize() {                                                // 占位符 → 实体标记
    return this.doc.replace(/\uFFFC\d+\uFFFC/g, k => {
      const e = this.entities.get(k);
      return e.type === 'mention' ? `[mention:${e.id}]` : e.value;
    });
  }
  static deserialize(str, resolveMention) {                    // 反序列化重建映射
    const ed = new EntityEditor();
    ed.doc = str.replace(/\[mention:(\d+)\]/g, (_, id) => {
      const key = '\uFFFC' + ed.entities.size + '\uFFFC';
      ed.entities.set(key, { type: 'mention', id, label: resolveMention(id) });
      return key;
    });
    return ed;
  }
}
```
