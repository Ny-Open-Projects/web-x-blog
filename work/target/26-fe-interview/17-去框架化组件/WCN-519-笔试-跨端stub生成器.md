---
title: [WCN-519] 笔试：实现跨端元素契约（JSON Schema）→ 三端 stub 代码生成器。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-519：笔试：实现跨端元素契约（JSON Schema）→ 三端 stub 代码生成器。

**答**：
- 结论：生成器接收 Schema 与目标端，输出该端可编译的骨架代码，含类型声明与事件映射表。
- 属性类型映射：boolean/string/number 各端一致，object 在小程序转 JSON 字符串。
- 事件映射表把统一事件名映射到端事件名，避免各端手写不一致。
- 追问：新增一端（如 Flutter）如何扩展而不改核心？（答：注册端适配器插件）

```javascript
const TYPE_MAP = {
  web:   t => t,
  mini:  t => t === 'object' ? 'String' : t,
  rn:    t => ({ boolean: 'bool', string: 'string', number: 'number' }[t] || 'any'),
};
const EVENT_MAP = { web: n => n, mini: n => 'bind' + n, rn: n => 'on' + cap(n) };
function cap(s) { return s[0].toUpperCase() + s.slice(1); }
function gen(schema, platform) {
  const props = schema.props.map(p => `${p.name}: ${TYPE_MAP[platform](p.type)}`).join('\n  ');
  const events = schema.events.map(e => `  ${EVENT_MAP[platform](e.name)}: (payload) => {}`).join('\n');
  return [`// ${platform} stub for ${schema.name}`, `interface Props {\n  ${props}\n}`,
          `// events\n${events}`].join('\n');
}
```

**评分点**：
- 三端类型映射表
- 事件名统一映射
- 可编译骨架含接口声明
- 端适配器插件扩展
