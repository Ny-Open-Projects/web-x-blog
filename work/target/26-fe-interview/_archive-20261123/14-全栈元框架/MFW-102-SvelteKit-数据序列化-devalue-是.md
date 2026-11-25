---
title: [MFW-102] SvelteKit 的 devalue 是什么？为什么不用 JSON.stringify？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-102：SvelteKit 的 devalue 是什么？为什么不用 JSON.stringify？
**答**：
- load 函数返回值要跨「服务端 → HTML 内联脚本 → 客户端」传输。直接 JSON.stringify 有两个问题：① 不支持 Map/Set/Date/循环引用/BigInt；② 注入 HTML 时可能被 `</script>` 逃逸造成 XSS。
- devalue 把值转成**可还原的表达式**（不是纯字符串）：支持循环引用、自定义类型（`string.stringify`/`parse` 可注册类型），且输出经过转义防注入。
- SvelteKit 用 devalue 序列化 load 数据、form action 结果、`__data.json` 响应——面试中能说出「load 返回非可序列化值会运行时报错」即达标。
- 实操约束：load 里不要返回 class 实例/函数/闭包；Date 可以，Map/Set 可以；想传特殊结构就先转成 plain object。

```js
// devalue 的能力演示（SvelteKit 内部用法）
import { stringify, parse } from 'devalue';

const data = {
  createdAt: new Date('2026-01-01'), // Date 可还原
  tags: new Set(['ssr', 'svelte']),  // Set 可还原
  meta: new Map([['views', 120]]),   // Map 可还原
};

const serialized = stringify(data);
// 输出形如：'[{"createdAt":1,"tags":2,"meta":3},"2026-01-01T00:00:00.000Z",...'
// 引用式编码：值与索引分离，天然支持循环引用

const restored = parse(serialized);
restored.tags instanceof Set; // true —— 不是普通对象，类型还原
```

```js
// ❌ load 返回不可序列化值：运行时直接报错
export function load() {
  return {
    handler: () => console.log('hi'), // 函数 —— Error: Data must be serializable
    instance: new SomeClass(),        // 类实例 —— 同样报错
  };
}
```
