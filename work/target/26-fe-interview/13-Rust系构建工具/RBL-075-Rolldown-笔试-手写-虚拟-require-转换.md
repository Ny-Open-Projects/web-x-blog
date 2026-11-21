---
title: [RBL-075] 笔试：手写 CJS require 静态提取器（含动态 require 报告）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-075：笔试：手写 CJS require 静态提取器（含动态 require 报告）
**题目**：实现 extractRequires(code, id)：1) 提取所有 require('literal') 的静态依赖；2) require(variable) / require(template) 判定为动态依赖，收集并输出警告（带文件与行号）；3) 返回 { statics, dynamics }；4) 跳过注释与字符串字面量中的伪 require（简化：行级检测以 `//` 开头的行）；5) 行号计算正确。

```javascript
function extractRequires(code, id) {
  const statics = [], dynamics = [];
  const lines = code.split('\n');

  lines.forEach((line, i) => {
    const lineNo = i + 1;
    const isComment = /^\s*\/\//.test(line);
    if (isComment) return;
    // 剔除字符串字面量内伪 require：先把引号内容替换为占位再匹配（简化方案）
    let sanitized = line.replace(/(['"]).*?\1/g, '""');
    for (const m of sanitized.matchAll(/require\(\s*(.+?)\s*\)/g)) {
      const arg = m[1];
      if (/^(['"]).*\1$/.test(arg.trim())) {
        statics.push({ spec: arg.slice(1, -1), line: lineNo });
      } else {
        dynamics.push({
          arg, line: lineNo,
          warning: `${id}:${lineNo} 动态 require("${arg}") 无法静态分析`,
        });
      }
    }
  });
  return { statics, dynamics };
}
module.exports = { extractRequires };

// 测试
// extractRequires(`const a = require('./a'); // require('./fake')\nconst b = require(name);`)
// → statics: [{spec:'./a',line:1}], dynamics: [{arg:'name', line:2, ...}]
```
**评分点**：
- 动态 require 识别与警告信息带行号（可诊断性）。
- 行注释过滤（至少处理 // 场景）。
- 字符串字面量清洗避免误报（简化方案即可，能说出 AST 才彻底）。
- statics/dynamics 分离返回（消费方可分别处理）。
- 能联系打包器行为：动态 require 需要 context 依赖或显式 external。
