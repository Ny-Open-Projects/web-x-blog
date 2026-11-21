---
title: [AIC-003] AI 编程工具的 Agent 模式和补全模式的本质区别是什么？各自适合什么任务？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-003：AI 编程工具的 Agent 模式和补全模式的本质区别是什么？各自适合什么任务？
**答**：
- 补全模式是「单轮续写」：无工具调用、无自主规划，输入当前上下文输出代码，延迟低、可控性强。
- Agent 模式是「多轮循环」：模型可读文件、搜索、执行命令、编辑多文件，根据观察结果迭代，直到完成任务或达到步数上限。
- 适合补全：局部实现、样板代码、已知签名的函数体——目标明确、范围单文件。
- 适合 Agent：跨文件重构、新 feature 脚手架、批量迁移（如 Options API → Composition API）——需要探索与多步修改。
- Agent 的代价是可控性下降：可能改到不该改的文件、执行破坏性命令，必须配合 diff 审查与权限白名单。
- 追问钩子：面试官常追「你们团队怎么防止 Agent 乱改」——答规则文件 + 只读挂载 + 提交前 diff 评审。

```typescript
// 任务分流示意：同一需求「给列表加排序」两种模式的切法
// 补全模式：人写好框架，AI 只填 sortFn
function useSortedList<T>(list: T[], initialKey: keyof T) {
  const [key, setKey] = useState<keyof T>(initialKey);
  const sorted = useMemo(() => {
    return [...list].sort((a, b) => /* AI 续写此处 */ String(a[key]).localeCompare(String(b[key])));
  }, [list, key]);
  return { sorted, setKey };
}

// Agent 模式：交给 Agent 的任务描述要点
const agentTask = `
任务：为商品列表页新增「按销量/价格排序」。
约束：
1. 只允许修改 src/pages/goods/ 与 src/hooks/ 下的文件。
2. 复用现有 useSortedList，禁止引入新依赖。
3. 完成后运行 pnpm test goods，保证全绿再汇报。
`;
```
