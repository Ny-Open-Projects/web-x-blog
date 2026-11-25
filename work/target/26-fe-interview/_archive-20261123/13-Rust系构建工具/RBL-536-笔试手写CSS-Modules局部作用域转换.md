---
title: [RBL-536] 笔试：手写 CSS Modules 局部作用域转换（类名替换 + 导出映射）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-536：手写 CSS Modules 局部作用域转换（类名替换 + 导出映射）
**需求**：实现 `transformCssModules(css, filename, { hashLength = 6 })`：1) 提取所有类选择器的类名（`.btn`、`.btn.primary`）；2) 生成局部名 `filename__class__contentHash`（内容 hash 稳定）；3) 生成导出映射 `exports = { btn: 'btn__hash' }`（供 JS `styles.btn` 引用）；4) `:global(.x)` 豁免保持原名；5) 附用例：替换/映射/global 豁免/hash 稳定。

```javascript
import { createHash } from 'crypto'
const hash = (s, n) => createHash('sha256').update(s).digest('hex').slice(0, n)

function transformCssModules(css, filename, { hashLength = 6 } = {}) {
  const exports = {}
  const base = filename.replace(/\W/g, '_')

  // 提取类名：.class（排除 :global 内的）
  const classRe = /(\.)([A-Za-z_][\w-]*)(?![\w-])/g
  const globals = new Set()
  const css2 = css.replace(/:global\(([^)]+)\)/g, (_, inner) => {
    inner.replace(/\.([\w-]+)/g, (_, c) => globals.add(c))
    return inner                                       // global 豁免：保持原名
  })

  // 类名替换（跳过 global）
  const outCss = css2.replace(classRe, (dot, cls) => {
    if (globals.has(cls)) return dot + cls
    const local = `${base}__${cls}__${hash(`${filename}:${cls}`, hashLength)}`
    exports[cls] = local
    return `.${local}`
  })

  // 导出语句（JS 引用 styles.btn）
  const exportJs = `module.exports = ${JSON.stringify(exports, null, 2)}`

  return { css: outCss, exports, exportJs }
}

// 用例
const src = `
.btn { color: red; }
.btn.primary { font-weight: bold; }
:global(.reset) { all: unset; }
.icon { width: 16px; }
`
const r = transformCssModules(src, 'Button.css')
console.log(r.exports.btn?.startsWith('Button_css__btn__'))        // true：局部名
console.log(r.exports.primary)                                     // 局部名
console.log(r.css.includes('.reset'))                              // true：global 保持原名
console.log(r.css.includes('.Button_css__icon__'))                 // true：.icon 已替换
const r2 = transformCssModules(src, 'Button.css')
console.log(r2.exports.btn === r.exports.btn)                      // true：hash 稳定（内容 hash 非随机）
console.log(r.exportJs.includes('"btn"'))                          // JS 导出映射
```
**评分点**：
- 类名提取与替换（正则 + 局部名格式 filename__class__hash）
- :global 豁免（保持原名不替换）
- 导出映射生成（JS styles.btn 引用的地基）
- hash 内容稳定性（跨构建一致）
