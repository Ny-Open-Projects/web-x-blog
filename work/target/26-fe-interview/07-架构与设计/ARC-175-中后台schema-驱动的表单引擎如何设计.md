---
title: [ARC-175] 中后台：schema 驱动的表单引擎如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-175：中后台：schema 驱动的表单引擎如何设计？
**答**：
- 协议核心四要素：字段（类型/默认值/校验规则）、布局（栅格/分组/分步）、联动（显隐/禁用/取值的依赖表达式）、数据源（字典/远程选项/默认值计算）。
- 联动引擎用声明式表达式（如 `visible: "{{type === 'refund'}}"`）而不是回调钩子——表达式可静态分析（依赖收集）、可校验（引用了不存在的字段直接报错）。
- 执行架构：schema → 解析器产出表单状态机（值/错误/可见性三大状态）→ 渲染器按状态渲染，逻辑与渲染分离（同一引擎可渲染到 antd/element）。
- 逃生舱与版本化：自定义渲染组件白名单注册、协议带 version 与迁移脚本；表单 schema 本身要可测试（联动表达式单测）。

```typescript
// 表单 schema 协议与引擎核心
interface FormSchema {
  version: '1.2';
  fields: FieldDef[];
  layout?: { cols?: number; steps?: string[] };
}
interface FieldDef {
  key: string; type: 'input' | 'select' | 'date' | 'custom';
  label: string; required?: boolean; rules?: Rule[];
  visible?: string; disabled?: string;        // 联动表达式（声明式）
  options?: { source: 'dict' | 'remote'; ref: string; filter?: string };
  component?: string;                          // type=custom 时的白名单组件
}

// 表单状态机（逻辑与渲染分离）
class FormEngine {
  value = reactive<Record<string, unknown>>({});
  private visibility = reactive<Record<string, boolean>>({});
  constructor(private schema: FormSchema) {
    // 预编译联动表达式：静态分析依赖，形成依赖图
    for (const f of schema.fields) {
      if (f.visible) this.linkGraph.add(f.key, extractDeps(f.visible));
    }
  }
  setValue(key: string, v: unknown) {
    this.value[key] = v;
    for (const dep of this.linkGraph.dependentsOf(key)) {       // 只重算受影响字段
      const f = this.fieldOf(dep);
      this.visibility[dep] = f.visible ? evalExpr(f.visible, this.value) : true;  // 沙箱表达式求值
    }
  }
  validate(): Promise<Record<string, string>> { /* 按 rules 批量校验，返回错误 map */ }
}
// 表达式沙箱：new Function 白名单上下文（只暴露 value），禁 Math 外全局
// schema 单测：联动表达式用例（type=refund 时 reason 必填可见）——schema 本身可测是协议设计成功标志
```
