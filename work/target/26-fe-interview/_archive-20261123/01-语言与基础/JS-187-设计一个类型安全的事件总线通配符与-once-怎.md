---
title: [JS-187] 设计一个类型安全的事件总线？通配符与 once 怎么配合？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-187：设计一个类型安全的事件总线？通配符与 once 怎么配合？

**答**：
- 类型安全靠 TS 泛型映射：定义 `interface EventMap { 事件名: 载荷类型 }`，on/emit 的参数由事件名自动推导，事件名拼错或载荷类型不符在编译期报错。
- 通配符监听 `'*'` 收全部事件，便于调试与埋点；emit 返回是否有监听者接收，方便发现孤儿事件。
- once = 用包装函数先 off 再执行原回调；on 返回注销函数，组件卸载时直接调用，避免手管 off。
- 运行时能力（通配符）与编译期约束（精确事件）并存：通配监听的载荷声明为 unknown，强制使用者窄化后再用。
- 跨模块通信建议 key 常量化或 Symbol 化，杜绝手写字符串拼错。

```typescript
// 1. 类型定义：事件名 -> 载荷 的映射，on 与 emit 双向约束
type EventMap = {
  login: { userId: string };
  logout: undefined;
  error: Error;
};
type Handler<T> = T extends undefined ? () => void : (payload: T) => void;

class TypedEventBus<M extends Record<string, unknown>> {
  private handlers = new Map<string, Set<(p: unknown) => void>>();

  // K | '*'：精确事件或通配符；返回注销函数
  on<K extends keyof M>(event: K | '*', fn: Handler<M[K]> | ((p: unknown) => void)): () => void {
    const set = this.handlers.get(event as string) ?? new Set();
    set.add(fn as (p: unknown) => void);
    this.handlers.set(event as string, set);
    return () => this.off(event as K, fn as Handler<M[K]>);
  }

  once<K extends keyof M>(event: K, fn: Handler<M[K]>): () => void {
    const wrap = ((p: unknown) => {
      this.off(event, wrap as Handler<M[K]>);      // 先注销再执行，保证只触发一次
      (fn as (p: unknown) => void)(p);
    }) as Handler<M[K]>;
    return this.on(event, wrap);
  }

  off<K extends keyof M>(event: K, fn: Handler<M[K]>) {
    this.handlers.get(event as string)?.delete(fn as (p: unknown) => void);
  }

  emit<K extends keyof M>(event: K, ...args: M[K] extends undefined ? [] : [M[K]]): boolean {
    const p = args[0];
    let delivered = false;
    const call = (set?: Set<(p: unknown) => void>) =>
      set?.forEach((fn) => { delivered = true; fn(p); });
    call(this.handlers.get(event as string));      // 精确监听
    if (event !== '*') call(this.handlers.get('*')); // 通配监听收到全部事件
    return delivered;                              // 无人接收返回 false，便于调试
  }
}

// 2. 使用：事件名与载荷全部受编译期约束
const bus = new TypedEventBus<EventMap>();
bus.on('login', (p) => console.log(p.userId));     // p 自动推导为 { userId: string }
bus.on('logout', () => console.log('登出'));
bus.once('error', (e) => console.error(e.message));
bus.on('*', (p) => console.log('通配收到', p));     // unknown 载荷，窄化后再用
const dispose = bus.on('login', () => {});         // 返回注销函数
dispose();                                          // 组件卸载时调用
// bus.emit('logn', {})   // 编译错误：事件名拼错
// bus.emit('login', 1)   // 编译错误：载荷类型不符
bus.emit('login', { userId: 'u1' });               // 精确 + 通配两个监听都触发
```
