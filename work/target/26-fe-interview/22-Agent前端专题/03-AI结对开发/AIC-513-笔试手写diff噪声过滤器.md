---
title: [AIC-513] 笔试：手写 diff 噪声过滤器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-513：笔试：手写 diff 噪声过滤器

**答**：实现 `filterDiffNoise(diffLines)`。diffLines: string[]（git diff 格式的行）。规则：1) **格式噪声**：引号变化（`'x'` → `"x"`）、分号增删、尾逗号、空行增删——全部标记为 noise；2) **import 重排**：import 语句的位置变化（import 语句的 -/+ 行 = 重排——语义不变）；3) **语义变更保留**：变量名/逻辑/条件/函数签名——语义变更不过滤；4) 返回 `{ semantic: string[], noise: string[], noiseRatio: number }`。噪声判定：`-` 行与 `+` 行的"规范化后内容"相同 → noise（规范化 = 去引号差异/去分号/去空格/统一引号）；单独的 `-` 或 `+` 行（无对应行）→ semantic。边界：diffLines 空；全 noise（semantic 空）；全 semantic。

```javascript
function normalizeLine(line) {
  return line.replace(/^[-+]\s*/, '')          // 去 diff 前缀
    .replace(/['"]/g, '')                     // 去引号
    .replace(/;$/, '')                        // 去分号
    .replace(/,\s*$/, '')                     // 去尾逗号
    .replace(/\s+/g, ' ').trim();             // 规范空格
}
function filterDiffNoise(diffLines = []) {
  const semantic = [], noise = [];
  const used = new Set();                       // 已匹配的 - 行索引
  for (let i = 0; i < diffLines.length; i++) {
    const line = diffLines[i];
    if (!line.startsWith('-') && !line.startsWith('+')) {
      semantic.push(line); continue;           // 上下文行
    }
    if (used.has(i)) continue;
    const norm = normalizeLine(line);
    // 找配对行（相邻 3 行内）
    let paired = false;
    for (let j = Math.max(0, i - 3); j <= Math.min(diffLines.length - 1, i + 3); j++) {
      if (j === i || used.has(j)) continue;
      const other = diffLines[j];
      if ((other[0] === '-' || other[0] === '+') && other[0] !== line[0] &&
          normalizeLine(other) === norm) {
        paired = true;
        noise.push(line, other);
        used.add(i); used.add(j);
        break;
      }
    }
    if (!paired) semantic.push(line);           // 无配对 = 语义变更
  }
  const total = semantic.length + noise.length;
  return { semantic, noise, noiseRatio: total ? +(noise.length / total * 100).toFixed(1) : 0 };
}

// 自测
const diff = [
  '-import B from "b"',
  '+import B from \'b\'',                        // 引号变化 = noise
  '-const x = getValue();',
  '+const x = getValue()',                      // 分号变化 = noise
  '-if (age > 18) {',
  '+if (age >= 18) {',                          // 语义变更！
  ' context line',
  '-',
  '+',                                          // 空行变化 = noise
];
let r = filterDiffNoise(diff);
console.log(r.semantic.includes('-if (age > 18) {'));   // 语义保留
console.log(r.semantic.includes('+if (age >= 18) {'));
console.log(r.noise.length >= 4);                        // 引号+分号+空行 = 噪声
console.log(r.noiseRatio > 0);
// 空
console.log(filterDiffNoise([]).noiseRatio === 0);
// 全语义
const allSemantic = ['-const x = fn();', '+const y = fn2();'];
r = filterDiffNoise(allSemantic);
console.log(r.semantic.length === 2 && r.noise.length === 0);
```

**评分点**：
- 配对噪声检测（-/+ 行规范化后相同 = noise——引号/分号/空格的规范化）
- 语义变更保留（无配对的 -/+ 行 = 语义变更——逻辑/条件/函数签名不误过滤）
- 边界（空/全语义/全 noise/上下文行透传）；noiseRatio 可量化
- 能说清「diff 噪声过滤让审查者聚焦语义变更——引号/分号/import 重排是 AI 的高频噪声」属于加分
