---
title: [TST-645] 笔试：实现 XSS payload 上下文生成器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-645：笔试：实现 XSS payload 上下文生成器

**题目**：实现 genPayloads(base)。针对 html/attr/js/url 四种上下文分别包装 payload 使其尝试逃逸，输出 [{context,payload,expectMarker}]。payload 集固定可复现。

**答**：
- 四种上下文用不同包装模板，确保 payload 逃逸当前上下文。
- 输出 {context,payload,expectMarker}，测试脚本注入后检查 marker。
- 生成器要可复现（固定 payload 集）。

```javascript
function genPayloads(base) {
  const wrappers = {
    html: p => `</div>${p}<div>`,
    attr: p => `" onmouseover="${p}`,
    js: p => `';${p};//`,
    url: p => `javascript:${encodeURIComponent(p)}`,
  };
  return Object.entries(wrappers).map(([context, fn]) => ({
    context,
    payload: fn(base),
    expectMarker: '__xss_probe__',
  }));
}
console.log(genPayloads('<img src=x onerror=1>').map(x => x.context));
// ['html','attr','js','url']
```

**评分点**：
- 四种上下文包装模板准确
- 逃逸写法符合各上下文语法
- 输出结构统一带 marker
- 可复现性（无随机）
