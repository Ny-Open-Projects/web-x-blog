---
title: [AIC-349] 训练团队识别「AI 做不好的任务类型」，边界清单应包含哪些？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-349：训练团队识别「AI 做不好的任务类型」，边界清单应包含哪些？
**答**：
- 隐性知识任务：依赖未文档化的业务背景/历史决策的判断——AI 只能猜。
- 超长程一致性任务：跨 100 文件保持统一抽象风格，AI 会前后不一致。
- 新颖性任务：团队自己的新架构模式（无训练数据先例），AI 会往通用模式上套。
- 对策而非禁用：这类任务要求人类提供更丰富的上下文/先做原型示范/结果加严人审——边界清单是「使用策略」不是「禁用清单」。

```javascript
const boundaries = [
  { type: 'implicit-context', strategy: '人补业务背景后再派' },
  { type: 'long-range-consistency', strategy: '里程碑切分 + 末段统一人审' },
  { type: 'novel-pattern', strategy: '人先写原型示例，AI 批量展开' },
];
r
```
