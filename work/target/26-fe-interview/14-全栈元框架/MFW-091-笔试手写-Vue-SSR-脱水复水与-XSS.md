---
title: [MFW-091] 笔试：手写 Vue SSR 的脱水复水模块（含 XSS 防护）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-091：笔试：手写 Vue SSR 的脱水复水模块（含 XSS 防护）
**答**：实现 `serialize(state)` 与 `rehydrate(windowVar)`：① 状态安全地嵌入 HTML（防 `</script>` 闭合逃逸与 `<!--` 注入）；② 客户端解析后还原为对象；③ 支持 Date/undefined 等非纯 JSON 类型；④ 解析失败返回空对象不崩溃。

```ts
// serialize.ts —— 服务端：状态 -> 安全脚本字符串
function serialize(state: Record<string, unknown>): string {
  const json = JSON.stringify(state, (_k, v) => {
    if (v instanceof Date) return { __type: 'Date', value: v.toISOString() };
    if (v === undefined) return { __type: 'Undefined' };
    return v;
  });
  // XSS 防线：
  // 1) < 转义，防 '</script>' 提前闭合标签
  // 2) 防 <!-- 注入被 HTML 解析器吞掉后续内容
  return json
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026')
    .replace(/\u2028/g, '\\u2028') // JS 行终止符在 JSON 里合法但会打断 <script>
    .replace(/\u2029/g, '\\u2029');
}

function scriptTag(varName: string, state: Record<string, unknown>): string {
  return `<script>window.${varName} = JSON.parse('${serialize(state)}');</script>`;
}
```

```ts
// rehydrate.ts —— 客户端：还原 + 类型恢复
type Reviver = (key: string, value: unknown) => unknown;

const reviver: Reviver = (_key, v) => {
  if (v && typeof v === 'object' && (v as any).__type === 'Date') return new Date((v as any).value);
  return v;
};

function rehydrate(windowVar = '__INITIAL_STATE__'): Record<string, unknown> {
  const raw = (window as any)[windowVar];
  if (!raw) return {};
  try {
    // raw 已是 JSON.parse 结果（serialize 时转义的引号被外层 parse 消化）
    return typeof raw === 'string' ? JSON.parse(raw, reviver) : raw;
  } catch {
    console.error('rehydrate 失败，使用空状态'); // ⑤ 容错：不阻塞首屏
    return {};
  }
}

export { scriptTag, rehydrate, reviver };
```

**评分点**：
1. XSS 三连转义（`<`/`>`/`&`）并解释 `</script>` 逃逸攻击——只转义 `<` 也算对，但能说全更佳。
2. 处理 `\u2028/\u2029` 行终止符（JSON 合法但 JS 字符串字面量会报错），是面试高频冷知识。
3. Date/undefined 自定义序列化 + reviver 还原，知道 JSON.parse 第二参数。
4. rehydrate 有 try/catch 兜底，解析失败降级空对象。
5. 能口头补充：状态注入必须放 body 内且在业务脚本之前。
