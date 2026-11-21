---
title: [V3-341] 手写：把简单模板编译成带 patchFlag 的 render 函数
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-341：手写：把简单模板编译成带 patchFlag 的 render 函数
**题**：实现 `compileSimple(template)`，输入形如 `<div><span>{{msg}}</span><p class="a">static</p></div>`，输出等价的 render 函数字符串：静态节点生成常量、动态文本节点标 patchFlag=TEXT。要求：静态节点提升、动态节点保留表达式占位。

```javascript
function compileSimple(tpl) {
  const doc = new DOMParser().parseFromString(tpl, 'text/html')
  const root = doc.body.firstElementChild
  const hoisted = []; let id = 0
  function gen(node) {
    const isStatic = !node.textContent.includes('{{')
    const tag = node.tagName.toLowerCase()
    if (isStatic && node.children.length === 1 && node.firstChild.nodeType === 3) {
      const name = `_hoisted_${id++}`
      hoisted.push(`const ${name} = createVnode('${tag}', null, ${JSON.stringify(node.textContent)})`)
      return name
    }
    if (isStatic) return `createVnode('${tag}', null, ${JSON.stringify(node.innerHTML)})`
    // 动态文本节点
    const child = node.textContent.replace(/{{\s*(\w+)\s*}}/, '$1')
    return `createVnode('${tag}', null, String(_ctx.${child}), 1 /* TEXT */)`
  }
  const code = hoisted.join('\n') + `\nreturn () => createVnode('${root.tagName.toLowerCase()}', null, [${[...root.children].map(gen).join(',')}])`
  return code
}
// 产出：const _hoisted_0 = ...; return () => createVnode('div', null, [createVnode('span', null, String(_ctx.msg), 1)])
```
**评分点**：
- 能区分静态/动态节点并给动态文本标 patchFlag=1（TEXT）。
- 静态节点提升为模块级常量。
- 用正则或简易解析提取插值表达式（DOMParser/正则均可），不需完整 AST 但结构不能硬编码死。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-aa513259-2959-498b-b5e5-881f417bdf3b-cwd'; fi
exit "$__zcode_status"
