---
title: [WCN-625] 笔试：实现 WC 的 hydration 一致性检测与修复器（对比 DSD 快照与客户端 DOM）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-625：笔试：实现 WC 的 hydration 一致性检测与修复器（对比 DSD 快照与客户端 DOM）

**答**：
- 需求：实现 checkHydration(host)：比对服务端 DSD 快照（template[shadowrootmode] 内容）与客户端 attachShadow 后的结构，列出差异节点；提供 repair() 以服务端结构为准修复。
- 思路：把两侧 DOM 序列化为规范字符串（忽略属性顺序与空白）；diff 用简单树对比；repair 用服务端 outerHTML 重建 shadow 内容。
- 边界：忽略无关属性顺序；差异为空时返回 null；修复后重验一次。

```javascript
function normalize(node) {
  const attrs = [...node.attributes].map(a => `${a.name}=${a.value}`).sort().join(' ');
  const kids = [...node.childNodes].map(n =>
    n.nodeType === 3 ? n.textContent.trim() : normalize(n)).filter(Boolean);
  return `<${node.nodeName} ${attrs}>${kids.join('')}</${node.nodeName}>`;
}
function checkHydration(host) {
  const tpl = host.querySelector('template[shadowrootmode]');
  const root = host.shadowRoot;
  if (!tpl || !root) return null;
  const server = normalize(tpl.content);
  const client = normalize(root);
  return server === client ? null : { server, client };
}
function repair(host) {
  const tpl = host.querySelector('template[shadowrootmode]');
  if (tpl) host.shadowRoot.innerHTML = tpl.innerHTML;
  return checkHydration(host);
}
const diff = checkHydration(document.querySelector('ds-goods'));
if (diff) console.warn('水合不一致', diff);
```

**评分点**：
- 规范化序列化忽略属性顺序与空白（避免假阳性）。
- 同时处理 template.content（DocumentFragment）与 shadowRoot。
- 差异返回结构化结果（便于上报/断言），一致返回 null。
- repair 以服务端为准且修复后重验（闭环）。
