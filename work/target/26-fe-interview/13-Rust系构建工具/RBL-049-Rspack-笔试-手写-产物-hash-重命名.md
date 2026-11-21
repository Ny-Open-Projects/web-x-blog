---
title: [RBL-049] 笔试：手写产物重命名与 HTML 引用同步器（contenthash）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-049：笔试：手写产物重命名与 HTML 引用同步器（contenthash）
**题目**：实现 applyContentHash(files)：1) 对每个 .js/.css 计算内容 sha256 前 8 位；2) 把 `app.js` 重命名为 `app.<hash>.js`；3) HTML 内引用（script src / link href）同步替换为新文件名；4) css 内 url() 引用的图片也参与重命名与替换；5) 循环引用（css 引 js 无此场景，但 html↔manifest）要保证替换只发生一轮不重复。

```javascript
const crypto = require('crypto');

function hash8(content) {
  return crypto.createHash('sha256').update(content).digest('hex').slice(0, 8);
}

function applyContentHash(files) { // files: Map<name, content>
  const renamed = new Map();          // oldName -> newName
  const output = new Map();

  // 1) 先重命名资源文件（图片/js/css），收集映射
  for (const [name, content] of files) {
    if (!/\.(js|css|png|svg|jpe?g)$/.test(name)) continue;
    const newName = name.replace(/\.(\w+)$/, `.${hash8(content)}.$1`);
    renamed.set(name, newName);
    output.set(newName, content);
  }

  // 2) 替换引用方（HTML 与 CSS），一轮内完成
  for (const [name, content] of renamed) {
    if (!/\.html$|\.css$/.test(name)) continue;
    let src = output.get(content && name) || files.get(name);
    for (const [oldN, newN] of renamed) {
      // 只替换引用边界（引号/括号包裹），避免 hash 字符串误伤
      const esc = oldN.replace(/\./g, '\\.');
      src = src.replace(new RegExp(`(['"(])${esc}(['")])`, 'g'), `$1${newN}$2`);
    }
    output.set(name, src);
  }
  return output;
}
module.exports = { applyContentHash };
```
**评分点**：
- 先收集完整映射再统一替换（一轮完成，避免链式二次替换）。
- 引用替换限定引号/括号边界（正则转义 + 分组捕获）。
- hash 取 sha256 前 8 位（与 webpack contenthash 惯例一致）。
- css 内 url() 资源也纳入重命名映射（完整性）。
- 能指出：真实构建器中 hash 在 emit 前由资产管道统一处理，且替换基于 AST/token 而非正则。
