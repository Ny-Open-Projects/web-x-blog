---
title: [PER-604] 手写一个 XSS sink 静态扫描器：扫描代码里危险的 DOM 写入点并给出风险评级
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-604：手写一个 XSS sink 静态扫描器：扫描代码里危险的 DOM 写入点并给出风险评级

**答**：
- 静态扫描思路：正则/AST 匹配危险 sink（`innerHTML=`、`outerHTML=`、`document.write`、`insertAdjacentHTML`、`eval`、`new Function`、`setAttribute('href'/'src', 动态值)`），再看数据源是否为用户可控（URL 参数、存储、接口返回）。
- 要点：AST（如 babel parser）比正则准——能识别别名调用（`const w = window.document.write`）与经过净化的调用（包了 DOMPurify 的标记为低危）；评级规则：未净化直接赋值=high、净化后=low、常量字符串=info。
- 边界：扫描器自身误报要有白名单注释机制（`// security: sanitized`）；CI 增量扫描只查 diff 文件控制耗时。
- 评分点：净化识别与白名单机制。

```javascript

const SINKS = ['innerHTML', 'outerHTML', 'insertAdjacentHTML', 'document.write', 'eval', 'new Function'];
function scan(code, file) {
  const findings = [];
  const lines = code.split('\n');
  lines.forEach((line, i) => {
    for (const sink of SINKS) {
      const re = new RegExp(`\\b${sink.replace(' ', '\\s+')}\\s*\\(`);  // 调用形式
      const assign = new RegExp(`\\.${sink}\\s*=`);                            // 赋值形式
      if (re.test(line) || assign.test(line)) {
        const sanitized = /DOMPurify|sanitize/i.test(line);                     // 净化识别
        const dynamic = !/['"`]\\s*['"`]/.test(line.split('=')[1] ?? '');      // 非纯常量
        findings.push({
          file, line: i + 1, sink,
          level: sanitized ? 'low' : dynamic ? 'high' : 'info',
          hint: sanitized ? '已净化' : dynamic ? '动态值未净化，需白名单校验' : '常量，无风险',
          wl: /security:\s*sanitized/.test(line),                              // 白名单注释
        });
      }
    }
  });
  return findings.filter(f => !f.wl);                       // 白名单注释可豁免
}
// CI 用法：git diff --name-only -> 只扫变更文件，high 级阻断合并
```
