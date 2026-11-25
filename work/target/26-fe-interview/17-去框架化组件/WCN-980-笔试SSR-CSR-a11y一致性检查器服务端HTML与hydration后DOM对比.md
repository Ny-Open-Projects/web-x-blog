---
title: [WCN-980] 手写 SSR+CSR 的 a11y 一致性检查器：对比服务端 HTML 与 hydration 后 DOM
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-980：手写 SSR+CSR 的 a11y 一致性检查器：对比服务端 HTML 与 hydration 后 DOM

**题目**：实现 `compareA11y(serverHTML, clientHTML)`，用正则提取各标签的「tag + id/class + role/aria-* 属性 + 可见文本」，对比两者无障碍相关差异。返回 `{ diffs:[{ label, server, client }], consistent }`。要求：① 提取标签序列，忽略属性顺序与空白差异；② 只比较无障碍相关：tag、role、aria-* 属性、img alt、button 文本；③ 服务端有而客户端缺、或值不同的记为差异（label 描述差异，server/client 给出各自值或 '缺失'）；④ 数量不一致记为一条差异；⑤ 输入非字符串按空串处理；consistent = diffs 为空。请自足实现并给出可运行示例（服务端有 aria-label、客户端丢失）。

**答**：

```javascript
function extract(html) {
  if (typeof html !== 'string') return [];
  const out = [];
  const re = /<([a-z]+)\b([^>]*)>([\s\S]*?)<\/\1>|<([a-z]+)\b([^>]*)\/>/gi;
  let m;
  while ((m = re.exec(html))) {
    const tag = (m[1] || m[4]).toLowerCase();
    const attrs = m[2] || m[5] || '';
    const text = (m[3] || '').replace(/<[^>]*>/g, '').trim();
    const rel = {};
    for (const key of ['role', 'aria-label', 'aria-labelledby', 'alt']) {
      const r = new RegExp(key + '\\s*=\\s*["']([^"']*)["']', 'i').exec(attrs);
      if (r) rel[key] = r[1];
    }
    if (text) rel.text = text;
    out.push({ tag, rel });
  }
  return out;
}
function compareA11y(serverHTML, clientHTML) {
  const a = extract(serverHTML), b = extract(clientHTML);
  const diffs = [];
  if (a.length !== b.length) diffs.push({ label: '节点数量', server: a.length, client: b.length });
  const n = Math.min(a.length, b.length);
  for (let i = 0; i < n; i++) {
    const keys = new Set([...Object.keys(a[i].rel), ...Object.keys(b[i].rel)]);
    for (const k of keys) {
      const sv = a[i].rel[k], cv = b[i].rel[k];
      if (sv !== cv) diffs.push({ label: `节点${i}.${k}`, server: sv || '缺失', client: cv || '缺失' });
    }
  }
  return { diffs, consistent: diffs.length === 0 };
}
console.log(compareA11y('<button aria-label="购买"> Buy </button>', '<button> Buy </button>'));
```

**评分点**：
- 提取无障碍相关属性（role/aria-*/alt/文本）正确。
- 忽略属性顺序与空白差异，只比语义。
- 差异记录 server/client 各自值或'缺失'，label 清晰。
- 数量不一致单独记一条，consistent 计算正确。
- 示例（服务端有 aria-label 客户端丢失）可运行、输出正确。
