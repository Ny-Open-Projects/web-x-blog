---
title: [WCN-458] 笔试：实现「SSR HTML vs 客户端 DOM」的语义 diff 工具。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-458：笔试：实现「SSR HTML vs 客户端 DOM」的语义 diff 工具。
**题目**：解析两棵树（简化：tag/attrs/text），忽略白名单属性（随机 id），文本空白归一；输出差异路径列表。

```javascript
const IGNORE = new Set(['id', 'data-reactroot', 'data-v-app']);
function semDiff(a, b, path = 'root', out = []) {
  if (a.tag !== b.tag) { out.push(`${path}: tag ${a.tag}≠${b.tag}`); return out; }
  for (const k of new Set([...Object.keys(a.attrs), ...Object.keys(b.attrs)])) {
    if (IGNORE.has(k)) continue;
    if (a.attrs[k] !== b.attrs[k]) out.push(`${path}@${k}: ${a.attrs[k]}≠${b.attrs[k]}`);
  }
  const ta = (a.text || '').trim().replace(/\s+/g, ' ');
  const tb = (b.text || '').trim().replace(/\s+/g, ' ');
  if (ta !== tb) out.push(`${path}: text "${ta}"≠"${tb}"`);
  (b.children || []).forEach((c, i) => c && (a.children || [])[i] &&
    semDiff(a.children[i], c, `${path}[${i}]`, out));
  return out;
}

```

**评分点**：
- 白名单忽略属性（噪声消除）。
- 递归 diff + 路径输出。
- 文本归一（空白折叠）。
- 空 diff 通过（水合一致）。
