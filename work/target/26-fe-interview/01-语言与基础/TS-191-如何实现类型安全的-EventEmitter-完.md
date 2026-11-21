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
