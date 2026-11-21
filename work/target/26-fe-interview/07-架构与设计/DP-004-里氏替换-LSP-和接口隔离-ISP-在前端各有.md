---
title: [DP-004] 里氏替换 LSP 和接口隔离 ISP 在前端各有什么实例？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-004：里氏替换 LSP 和接口隔离 ISP 在前端各有什么实例？
**答**：
- LSP：所有用到父类/基接口的地方，换成子类实现必须行为正确——子类不能违背父类约定的语义（如不能抛异常、不能返回异常类型）。
- 前端实例：React 中接收 `onChange(value: string)` 的组件，传入的子组件回调签名与语义必须兼容；Vue 的 `v-model` 组件必须遵守 `modelValue` + `update:modelValue` 协议。
- ISP：不要强迫客户端依赖它用不到的方法——组件 props 应按需拆分，而不是塞一个 20 个字段的大对象。
- 前端实例：把"列表配置"从"编辑配置"中拆开，避免只读列表组件被迫接收一堆编辑态字段。

```typescript
// LSP：基类接口的替换必须语义兼容
interface DataFetcher {
  fetch(url: string): Promise<JSON>;
}
class HttpFetcher implements DataFetcher {
  async fetch(url: string) {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`); // 约定：失败抛错
    return res.json();
  }
}
class CacheFetcher implements DataFetcher {
  private cache = new Map<string, JSON>();
  async fetch(url: string) {
    if (this.cache.has(url)) return this.cache.get(url)!; // 行为兼容：成功返回JSON，失败同样抛错
    const data = await new HttpFetcher().fetch(url);       // 替换后上层代码无需任何感知
    this.cache.set(url, data);
    return data;
  }
}
// 上层只依赖抽象，CacheFetcher 可以无感替换 HttpFetcher（同时体现 DIP）

// ISP：把大而全的 props 按使用方隔离
interface ListProps { items: Item[]; onRowClick: (id: string) => void; }            // 列表只需要这些
interface EditProps { item: Item; onSave: (item: Item) => void; onDelete: (id: string) => void; }
// 只读列表组件绝不接收 onSave/onDelete，避免依赖用不到的契约
```
