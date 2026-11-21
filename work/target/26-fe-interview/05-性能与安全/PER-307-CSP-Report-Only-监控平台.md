---
title: [PER-307] 笔试题：手写 CSP 违规上报的收集端与聚合分析（report-uri 端点 + 聚合报表）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-307：笔试题：手写 CSP 违规上报的收集端与聚合分析（report-uri 端点 + 聚合报表）

**题目**：实现：① Node 收集端点 `POST /csp-report`：接收浏览器 CSP 违规 JSON（`{"csp-report": {...}}`），做基本校验、按 `violated-directive + source-file 域` 生成聚合键、限流写入（内存 Map 滚动窗口）；② 聚合函数 `topViolations(windowMs, limit)`：按聚合键返回计数 Top N 与最近一次样本；③ 防止恶意刷量（同 UA+IP 限频）与超大 payload 截断。

**答**：CSP 收集端要当"公网暴露端点"对待：解析要 try-catch（浏览器发送的 JSON 可能变形）、限流、去 PII（不存完整 URL 里的用户路径）。

```javascript
const crypto = require('crypto');

class CSPCollector {
  constructor({ windowMs = 300000 } = {}) {
    this.windowMs = windowMs;
    this.buckets = new Map();          // key -> {count, lastSample, firstAt}
    this.ipCount = new Map();          // 限流：ip -> [{ts}]
  }
  handle(req, res) {
    const ip = req.socket.remoteAddress;
    if (!this.#allow(ip)) return res.writeHead(429).end();
    let body = '';
    req.on('data', (c) => { body += c; if (body.length > 16384) req.destroy(); }); // 16KB 截断
    req.on('end', () => {
      try {
        const report = JSON.parse(body)['csp-report'];
        if (!report || !report['violated-directive']) return res.writeHead(400).end();
        const source = (report['source-file'] || '').replace(/\?.*$/, '');
        const key = `${report['violated-directive']}|${new URL(source, 'https://x').host}`;
        const b = this.buckets.get(key) || { count: 0, lastSample: null, firstAt: Date.now() };
        b.count++;
        if (b.count <= 3) b.lastSample = {              // 只存前 3 个样本，防内存暴涨
          directive: report['violated-directive'],
          blocked: (report['blocked-uri'] || '').slice(0, 200),
          sample: report['script-sample']?.slice(0, 100) ?? null,   // 内联脚本前 100 字符
        };
        this.buckets.set(key, b);
      } catch { /* 坏数据忽略 */ }
      res.writeHead(204).end();
    });
  }
  #allow(ip) {                                         // 同 IP 每分钟最多 30 条
    const now = Date.now(), arr = (this.ipCount.get(ip) || []).filter((t) => now - t < 60000);
    if (arr.length >= 30) return false;
    arr.push(now); this.ipCount.set(ip, arr);
    return true;
  }
  topViolations(limit = 10) {
    const now = Date.now();
    return [...this.buckets]
      .filter(([, b]) => now - b.firstAt < this.windowMs)
      .sort((a, b) => b[1].count - a[1].count).slice(0, limit)
      .map(([key, b]) => ({ key: key.split('|'), count: b.count, samples: b.lastSample }));
  }
}
// 挂载：app.post('/csp-report', (req, res) => collector.handle(req, res));
// 巡检：每小时 topViolations(10) 进安全群；连续 3 天为 0 的白名单域名可从策略移除
```

**评分点**：
- 解析 `csp-report` 信封结构正确（浏览器发送格式）；坏数据 try-catch 不崩。
- 聚合键设计（directive + source host）合理，样本截断防内存（script-sample 100 字符、样本数上限）。
- 公网端点防护：IP 限频 + payload 大小截断。
- 聚合输出支持 Top N 排行与"降白名单"运营动作。
