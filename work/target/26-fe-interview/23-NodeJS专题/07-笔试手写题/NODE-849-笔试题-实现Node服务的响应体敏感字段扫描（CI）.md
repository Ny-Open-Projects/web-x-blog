---
title: [NODE-849] 笔试题——实现响应体敏感字段扫描（CI 自动化）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-849：手写敏感扫描

**需求与边界**：
- 需求：响应体敏感扫描（SCN-NODE-698/联想-849）——① 测试环境响应捕获（接口测试的响应——SCN-联想-849 抽样）；② 敏感模式扫描（手机号/身份证/密钥——SCN-联想-849 模式库）；③ 归因（响应字段 → schema 定义——SCN-FIN-544）；④ CI 门禁（未脱敏响应阻断——SCN-OPS-289）。
- 边界：① 测试数据的真实性（真实感测试数据——非 "test123"）；② 模式库更新（新敏感类型——SCN-联想-849）；③ 报告的修复指引（哪个字段哪个接口——SCN-FIN-544）。

**答**：
```javascript
const PATTERNS = [
  { name: 'phone', re: /1[3-9]\d{9}/, mask: 'phone' },
  { name: 'idcard', re: /\d{17}[\dXx]/, mask: 'idcard' },
  { name: 'secret', re: /(api[_-]?key|secret)['":\s]*[\w-]{20,}/i, mask: 'hidden' },
];
async function scanResponses(e2eCapture) {
  const issues = [];
  for (const resp of e2eCapture) {                     // E2E 响应捕获（SCN-联想-849 抽样）
    for (const p of PATTERNS) {
      const hits = scanDeep(resp.body, p.re);          // 深层扫描（SCN-FIN-773）
      hits.forEach(h => issues.push({
        api: resp.route, path: h.path, pattern: p.name,
        fix: `schema 标记 ${p.mask}（SCN-FIN-544）或加 redact（SCN-NODE-646）` }));   // 修复指引
    }
  }
  return { issues, gate: issues.length === 0 ? 'PASS' : 'BLOCK' };   // CI 门禁（SCN-OPS-289）
}
// CI：E2E 测试捕获响应 → 扫描 → 门禁
afterAll(async () => { const r = await scanResponses(captured); expect(r.gate).toBe('PASS'); });
```

**评分点**:
- E2E 响应捕获扫描（真实响应——SCN-联想-849）。
- 模式库 + 修复指引（SCN-FIN-544/646 联动）。
- 深层扫描（嵌套/数组——SCN-FIN-773）。
- CI 门禁（SCN-OPS-289 跑数据）。
