---
title: [PER-783] 手写一个 WebView 复用复位器：按清单逐项复位并校验复位完整性，不合格降级销毁
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-783：手写一个 WebView 复用复位器：按清单逐项复位并校验复位完整性，不合格降级销毁

**答**：
- 需求：输入一个 webview 抽象对象（含 clearStorage/clearCookies/resetScroll 等能力），release 时执行复位清单（同步项+异步项），复位后逐项校验（URL 为空、scroll=0、storage 前缀清空），任何校验失败则销毁并返回降级原因。
- 边界：清单项执行要 try/catch 隔离，单项失败不阻断其余项；校验函数可注入（容器能力差异）。
- 评分点：单项失败隔离；校验不合格的降级路径。

```javascript
class WebViewResetter {
  constructor(checklist, verify) { this.list = checklist; this.verify = verify; }
  async release(w) {
    const failed = [];
    for (const item of this.list.sync) {      // 同步项逐个隔离执行
      try { item.fn(w); } catch (e) { failed.push(item.name); }
    }
    await Promise.all(this.list.async.map(item =>
      item.fn(w).catch(() => failed.push(item.name))));   // 异步项并行，失败记录
    let ok = true;
    for (const v of this.verify) {            // 逐项校验复位完整性
      try { if (!v.check(w)) { ok = false; failed.push('verify:' + v.name); } }
      catch (e) { ok = false; }
    }
    if (!ok) return { reused: false, destroyed: true, reason: failed };
    return { reused: true, destroyed: false, reason: failed };
  }
}
// 用法：resetter.release(w) 后按 destroyed 决定进池还是重建
```
