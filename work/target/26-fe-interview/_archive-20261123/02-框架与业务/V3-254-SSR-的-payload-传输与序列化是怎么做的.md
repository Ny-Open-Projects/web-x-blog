---
title: [V3-254] SSR 的 payload 传输与序列化是怎么做的？为什么不能直接 JSON.stringify？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-254：SSR 的 payload 传输与序列化是怎么做的？为什么不能直接 JSON.stringify？
**答**：
- 传输方式：服务端把"水合所需数据"序列化后塞进 `<script type="application/json" id="__NUXT_DATA__">`（Nuxt）或 window 变量，客户端直接读取，避免二次请求。
- 为什么不能裸 JSON.stringify：用户数据里的 `</script>` 会截断标签造成 XSS 或语法错误，必须转义（`<`→`\u003C`）。
- 富结构序列化：Date/Map/Set/RegExp 等需要支持——Nuxt 用 devalue（去环引用 + 类型标注），Vue 官方 SSG 场景也内置类似方案。
- 函数不可序列化：payload 只包含数据，组件、方法靠客户端 JS 恢复（代码与数据分离）。
- 体积控制：只序列化"客户端初次渲染需要"的数据，大列表分页或折叠内容可延迟到客户端请求。

```javascript
// 安全序列化要点
function serializePayload(data) {
  return JSON.stringify(data).replace(/</g, '\\u003C'); // 防 </script> 截断
}
// devalue：支持环引用与特殊类型
import { stringify, parse } from 'devalue';
const payload = stringify({ user: { name: 'a', createdAt: new Date() }, tags: new Set(['x']) });
// '({"name":"a","createdAt":Date|1}, {"tags":Set|2}) [["name","createdAt"],["tags"]] [["x"]] 0'
```
