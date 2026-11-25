---
title: [FRP-135] defineProps 的泛型（类型）声明是如何编译成运行时 props 的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-135：defineProps 的泛型（类型）声明是如何编译成运行时 props 的？

**答**：
- 编译器拿到 `defineProps<{ title: string; tags?: string[]; mode: 'a' | 'b' }>()` 后做 **TS 类型节点 → runtime 声明**的翻译：`string→String`、`string[]→Array`、字面量联合→`{ type: String, validator }`、`?`→`required: false`。
- 只支持**可静态分析**的类型子集：基本类型、引用接口、元组、字面量联合；条件类型、`infer`、依赖运行时计算的类型无法编译，直接报编译错误。
- 宏的运行时不存在：`defineProps` 会被整体替换成 `__props` 声明，不需要 import（这就是"编译器宏"的含义）。
- 运行时校验与 IDE 类型是两条链路：runtime props 只做开发态告警，真正的类型检查靠 TS —— 编译器的翻译要让两者尽量一致。

```javascript
// 简化实现，帮助理解类型到运行时声明的翻译
function compileGenericProps(typeNode) {
  // 输入（TS AST 摘要）：{ title: string; tags?: string[]; mode: 'a' | 'b'; count: number }
  const runtimeProps = {};
  for (const member of typeNode.members) {
    const key = member.key;                       // 'title'
    const optional = member.optional;             // '?' 存在
    runtimeProps[key] = {
      type: mapType(member.type),                 // 递归翻译类型节点
      required: !optional,
    };
  }
  return runtimeProps;
}

function mapType(typeNode) {
  switch (typeNode.kind) {
    case 'StringKeyword':   return String;
    case 'NumberKeyword':   return Number;
    case 'BooleanKeyword':  return Boolean;
    case 'ArrayKeyword':    return Array;              // string[] -> Array
    case 'TupleKeyword':    return Array;              // [string, number] -> Array
    case 'LiteralUnion':    // 'a' | 'b' -> String + 自定义校验
      return { type: String, validator: (v) => typeNode.literals.includes(v) };
    case 'FunctionKeyword': return Function;
    default:
      // 条件类型等无法静态分析 —— 编译期直接抛错
      throw new Error(`无法为类型 ${typeNode.kind} 生成运行时 props 声明`);
  }
}

// 编译前后对照
// 源码：
//   const props = defineProps<{ title: string; mode: 'a' | 'b' }>()
// 产物（伪代码）：
const __props = __setupProps({
  title: { type: String, required: true },
  mode:  { type: String, validator: v => ['a', 'b'].includes(v), required: true },
});
// defineProps(...) 调用本身被删除 —— 宏在运行时不存在
```
