---
title: [MFW-063] 笔试：手写一个简化版 Hydration 校验器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-063：笔试：手写一个简化版 Hydration 校验器
**答**：实现 `hydrateCheck(serverHTML, rootEl)`，模拟水合一致性校验：① 按 DOM 节点顺序比较服务端 HTML 字符串解析结果与客户端实际 DOM 的标签名；② 发现第一个不一致时返回 `{ ok: false, path, expected, actual }`；③ 全一致返回 `{ ok: true }`。

```ts
type Mismatch = { ok: false; path: string; expected: string; actual: string } | { ok: true };

function parseTree(html: string): { tag: string; children: NodeListOf<unknown> } | null {
  const container = document.createElement('div');
  container.innerHTML = html;
  return container.firstElementChild as any;
}

function compare(
  serverEl: Element,
  clientEl: Element,
  path: string,
): Mismatch | null {
  if (serverEl.tagName !== clientEl.tagName) {
    return { ok: false, path: path || '/', expected: serverEl.tagName, actual: clientEl.tagName };
  }
  const s = serverEl.children;
  const c = clientEl.children;
  if (s.length !== c.length) {
    return {
      ok: false,
      path: `${path}/${serverEl.tagName}`,
      expected: `${s.length} children`,
      actual: `${c.length} children`,
    };
  }
  for (let i = 0; i < s.length; i++) {
    const res = compare(s[i], c[i], `${path}/${serverEl.tagName}[${i}]`);
    if (res) return res; // 只报第一个不一致
  }
  return null;
}

function hydrateCheck(serverHTML: string, rootEl: Element): Mismatch {
  const serverEl = parseTree(serverHTML);
  if (!serverEl) return { ok: true };
  const diff = compare(serverEl, rootEl, '');
  return diff ?? { ok: true };
}

// 用法
// const r = hydrateCheck('<div><p>a</p><span>b</span></div>', document.querySelector('#app'));
// if (!r.ok) console.error(`水合不一致 @${r.path}: 期望 ${r.expected}，实际 ${r.actual}`);
```

**评分点**：
1. 递归比较结构且深度优先，遇到第一个不一致立即短路返回（真实 React 就是这么定位首个 mismatch 的）。
2. path 记录了从根到出错节点的链路，而不是只报「不一致」。
3. 除标签名外还比较了子节点数量差异（对应非法 HTML 嵌套被浏览器纠偏的典型场景）。
4. 能口头补充：真实水合还要比文本节点与属性，且 React 19 会输出两侧 HTML diff。
