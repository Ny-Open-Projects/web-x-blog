---
title: [PER-064] 存储型 XSS 如何检测与应急？发现被注入后止血顺序是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-064：存储型 XSS 如何检测与应急？发现被注入后止血顺序是什么？

**答**：
- 检测三层：**上线前**对富文本入库做净化与单测（payload 用例集）、**线上扫描**定期检索存量数据中的 `<script`/`onerror=`/`javascript:` 特征、**运行时**CSP report 与错误监控告警。
- 止血顺序：**先断传播**（下线受影响接口或加全局净化中间层）→ **清数据**（批量转义/删除存量恶意 payload）→ **补漏洞**（定位注入点修复）→ **评估影响面**（会话是否被盗、是否要强制下线）。
- 应急中不要先修代码再清数据：存量 payload 会让每个打开页面的用户反复触发，修复期同步“读取时转义”最稳妥。
- 复盘沉淀：payload 库进回归测试、注入点清单进安全台账、CSP report 接入告警。

```javascript
// 应急止血脚本：读取时转义 + 特征扫描，配合数据清理
// 1) 全局兜底：富文本渲染入口统一先过净化，即使存量数据已脏
import DOMPurify from 'dompurify';
window.renderRichText = (dirty) => DOMPurify.sanitize(dirty, { USE_PROFILES: { html: true } });

// 2) 线上扫描：拉取存量内容，匹配恶意 payload 特征生成清理工单
async function scanStoredXss(api) {
  const signals = [/<script[\s>]/i, /on(error|load|click)\s*=/i, /javascript\s*:/i, /<iframe/i];
  const dirtyItems = [];
  for await (const item of api.fetchAllComments()) {
    const hit = signals.find((re) => re.test(item.content));
    if (hit) {
      dirtyItems.push({ id: item.id, rule: String(hit) });
      navigator.sendBeacon('/api/xss-alert', JSON.stringify({ id: item.id, rule: String(hit) })); // 实时告警
    }
  }
  // 3) 交给后端批量清理接口（服务端事务内执行，前端只发起与展示进度）
  if (dirtyItems.length) await api.post('/admin/xss-cleanup', { ids: dirtyItems.map((d) => d.id) });
  return dirtyItems.length;
}
scanStoredXss(commentApi);
```

## 十一、认证与会话安全
