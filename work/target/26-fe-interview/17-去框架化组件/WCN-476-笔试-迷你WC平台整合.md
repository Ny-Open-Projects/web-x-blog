---
title: [WCN-476] 笔试：整合题——迷你元素平台核心（注册/版本/token/审计）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-476：笔试：整合题——迷你元素平台核心（注册/版本/token/审计）。
**题目**：整合：defineOnce（版本协商）+ token 注入（主题类切换）+ registry（版本盘点）+ audit（泄漏/裸值）。接口 `platform.register(tag, Impl, version)`、`platform.theme('dark')`、`platform.audit()`。

```javascript
const platform = {
  registry: new Map(),
  register(tag, Impl, version = '1.0.0') {
    const cur = this.registry.get(tag);
    if (cur && cmpVer(cur.version, version) > 0)
      console.warn(`[${tag}] 已有 ${cur.version}，复用`);
    else { customElements.define(tag, Impl); this.registry.set(tag, { version }); }
  },
  theme(name) { document.documentElement.className = name; },   // 变量继承零 JS 参与
  audit() {
    return { versions: [...this.registry].map(([t, r]) => ({ tag: t, v: r.version })),
      leaks: auditLeaksAll(), bareValues: lintTokensAll() };
  },
};

```

**评分点**：
- 四模块职责清晰（注册协商/主题/盘点/审计数据流贯通）。
- 注册写 data-version（盘点数据源）。
- 主题切换 = root 类切换（元素零参与）。
- audit 汇总三源（版本分布/泄漏/裸值扫描）。
