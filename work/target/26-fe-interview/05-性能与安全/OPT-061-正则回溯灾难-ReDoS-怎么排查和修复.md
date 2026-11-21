---
title: [OPT-061] 正则回溯灾难（ReDoS）怎么排查和修复？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-061：正则回溯灾难（ReDoS）怎么排查和修复？

**答**：
- 嵌套量词如 `(a+)+`、`(.*)*` 在失配时指数回溯，一个恶意/巧合的输入能把主线程卡死几十秒——等于一次前端 DoS。
- 高危场景：校验 URL、HTML 片段清洗、日志匹配用在了用户输入上；lighthouse 与 Performance 面板表现为单次超长 RegExp 执行帧。
- 排查：Node 下用 `--prof` 或直接怀疑清单；更直接的是用 recheck/safe-regex 扫代码里的正则，标出超线性模式。
- 修复三板斧：改写为线性结构（量词互斥）、限定输入长度后再匹配、或改用字符串 API（indexOf/split）替代正则。

```javascript
// 一一对应：ReDoS 的复现、检测与修复对照
// 反例：嵌套量词，对 "aaaaaaaaaaaaaaaaaaaaaaaa!" 指数回溯
const badUrlRegex = /^(\w+\.)+[a-z]{2,6}$/;           // 最坏 O(2^n)
const badCsvRegex = /^(\s*,*\s*(\d+\s*,*\s*)*)*$/;    // 经典 CVE 形态

// 检测：用 recheck 扫描正则的输入长度-耗时曲线
// npx recheck badUrlRegex.json --input "aaaa...!" 输出 exponential 结论

// 修复一：改写为线性结构——外层别再包 + 量词
const goodUrlRegex = /^[a-z0-9-]+(\.[a-z0-9-]+)*$/i; // 无嵌套量词，O(n)

// 修复二：先限长度再匹配（防御纵深，任何正则都该做）
function safeMatch(input, regex, maxLen = 512) {
  if (typeof input !== 'string' || input.length > maxLen) return null;
  return input.match(regex);
}

// 修复三：能不用正则就不用——split/indexOf 是 O(n)
function parseCsvLenient(line) {
  return line.split(',').map((s) => s.trim()); // 替代 badCsvRegex
}

// 运行时兜底：给不可信正则套超时（放 Worker，超时直接 terminate）
function matchWithTimeout(pattern, input, ms = 50) {
  return new Promise((resolve) => {
    const w = new Worker(URL.createObjectURL(new Blob([`
      onmessage = (e) => {
        const re = new RegExp(e.data.pattern);
        postMessage(e.data.input.match(re));
      };`])));
    w.postMessage({ pattern, input });
    const timer = setTimeout(() => { w.terminate(); resolve(null); }, ms);
    w.onmessage = (e) => { clearTimeout(timer); w.terminate(); resolve(e.data); };
  });
}
```
