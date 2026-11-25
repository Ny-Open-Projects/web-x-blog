---
title: [TS-191] 如何实现类型安全的 EventEmitter 完整版？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-191：如何实现类型安全的 EventEmitter 完整版？
**答**：
- 事件表 `Record<string, unknown[]>`：键是事件名、值是 payload 元组，on/emit/off/once 四个方法全联动。
- once 用"包装函数先退订再执行"实现；on 返回退订函数是现代事件 API 惯例。
- 内部存储与对外签名之间的函数类型转换收敛在两处 as，边界清晰。

```typescript
type Listener<Args extends unknown[]> = (...args: Args) => void;

class EventEmitter<E extends Record<string, unknown[]>> {
  private map = new Map<keyof E, Set<(...args: unknown[]) => void>>();

  on<K extends keyof E>(event: K, fn: Listener<E[K]>): () => void {
    const set = this.map.get(event) ?? new Set();
    set.add(fn as (...args: unknown[]) => void);
    this.map.set(event, set);
    return () => this.off(event, fn); // 返回退订函数
  }

  once<K extends keyof E>(event: K, fn: Listener<E[K]>): void {
    const wrap = (...args: E[K]) => {
      this.off(event, wrap as Listener<E[K]>);
      fn(...args);
    };
    this.on(event, wrap as Listener<E[K]>);
  }

  off<K extends keyof E>(event: K, fn: Listener<E[K]>): void {
    this.map.get(event)?.delete(fn as (...args: unknown[]) => void);
  }

  emit<K extends keyof E>(event: K, ...args: E[K]): void {
    this.map.get(event)?.forEach((fn) => fn(...args));
  }
}

interface Events {
  login: [userId: string];
  error: [code: number, message: string];
}

const bus = new EventEmitter<Events>();
bus.on("error", (code, message) => console.log(code, message)); // 参数自动推断
const stop = bus.on("login", (userId) => userId.toUpperCase());
stop();
bus.emit("login", "u1");
// bus.emit("login", 1);     // 报错：payload 不是 string
// bus.on("nope", () => {}); // 报错：事件不存在
```

**追问**：

1. `emit` 遍历 Set 时，监听器里调用 off 移除自己，会影响本次遍历吗？ → 会，Set 的 forEach 是活迭代器，删除尚未访问的元素会被跳过，新增元素甚至可能被本轮执行；应先 `[...set]` 快照再遍历。
2. `once` 注册后调用 `off(event, 原fn)` 能注销掉吗？ → 不能，Set 里存的是 wrap，引用不同删不掉，监听器会残留；需要保存 wrap 到 fn 的映射，或让 once 返回自己的退订函数。
3. 某个监听器抛异常，后面的监听器还会执行吗？ → 不会，forEach 里 throw 会直接跳出并冒泡给 emit 调用方；要按需 try/catch 逐个隔离，并用 AggregateError 汇总上报。
