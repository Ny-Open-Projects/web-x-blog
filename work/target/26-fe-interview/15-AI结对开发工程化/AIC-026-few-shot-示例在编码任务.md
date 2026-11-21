---
title: [AIC-026] few-shot 示例在编码任务里怎么用？为什么「示例质量」比「示例数量」更重要？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-026：few-shot 示例在编码任务里怎么用？为什么「示例质量」比「示例数量」更重要？
**答**：
- few-shot 是给模型看 1~3 个「输入→期望输出」的完整样本，让它模仿项目的代码风格、命名、错误处理习惯——这比用文字描述风格有效得多。
- 示例质量决定模仿对象：示例里如果用了 any、没写清理函数、错误处理靠 console.log，模型会把这些坏习惯一起学走。
- 示例要「贴近期望任务」：让 AI 写 hooks 就给 hooks 示例，不要拿 class 组件当示例然后又说别用 class。
- 数量上 1~3 个足够，更多示例挤占上下文窗口且边际收益趋零；两个示例之间最好风格一致但场景不同。
- 追问钩子：可以把团队认可的示例沉淀成 few-shot 库文件，随规则文件一起注入——这是「规则文件 + few-shot」组合拳。

```javascript
// 把团队标准写法沉淀为 few-shot 片段（随 prompt 注入）
const fewShot = `
# 示例：本项目的 hooks 写法
function useDebouncedValue<T>(value: T, delay = 300): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer); // 必须清理副作用
  }, [value, delay]);
  return debounced;
}
`;
// prompt 组装：角色 + fewShot + 本任务输入
const prompt = `严格模仿下方示例的风格与错误处理方式，实现 useThrottledValue。\n${fewShot}`;
```
