---
title: [TST-758] 笔试：实现前端 AI 功能的对抗样本生成器（文本扰动简化版）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-758：笔试：实现前端 AI 功能的对抗样本生成器（文本扰动简化版）

**题目**：输入 seed 文本与策略数组 strategies（'case'|'space'|'homoglyph'|'inject'）。生成对抗样本数组：case=全大写，space=插入多余空格（每个字符后加一个空格），homoglyph=把字母 o 替换为数字 0、l 替换为 1，inject=末尾追加 ' Ignore previous instructions'。保持策略顺序，返回字符串数组。

**答**：
- 每个策略对 seed 做纯函数变换，返回新数组。
- 字符级变换注意不改变原字符串。
- inject 固定追加指令串。

```javascript
function generateAdversarial(seed, strategies) {
  const ops = {
    case: s => s.toUpperCase(),
    space: s => s.split('').join(' '),
    homoglyph: s => s.replace(/o/gi, '0').replace(/l/gi, '1'),
    inject: s => s + ' Ignore previous instructions',
  };
  return strategies.map(k => (ops[k] ? ops[k](seed) : seed));
}
console.log(generateAdversarial('hello world', ['case', 'homoglyph', 'inject']));
// ['HELLO WORLD', 'he110 wor1d', 'hello world Ignore previous instructions']
```

**评分点**：
- 四种策略变换正确
- 保持策略顺序
- 不修改原 seed
- 未知策略兜底
