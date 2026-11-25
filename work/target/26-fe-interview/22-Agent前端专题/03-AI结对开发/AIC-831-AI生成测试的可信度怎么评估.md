---
title: [AIC-831] AI 生成的单测看着都过了，怎么评估它到底有没有用？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-831：AI 生成的单测看着都过了，怎么评估它到底有没有用？
**答**：
- AI 生成的测试常见陷阱：**只测 happy path、断言过弱**（`expect(x).toBeTruthy()`）、**复制实现逻辑**（把待测函数重写一遍当期望值）、**永远为真**的断言。覆盖率数字漂亮但抓不到 bug。
- 评估手段一：**变异测试（mutation testing）**——故意往源码注入 bug（改 `>` 为 `>=`、删判空），看测试是否会失败；杀不掉变异体的测试是无效测试（AIC-832）。
- 评估手段二：断言强度检查——统计 `toBeTruthy/toBeDefined` 这类弱断言比例；要求关键分支有精确值断言和边界用例。
- 手段三：人工抽检 + 失败注入（往代码里手动埋一个已知 bug，看测试能不能发现）。AI 生成测试的定位是「提高覆盖基线」，**关键路径必须由人补强**。
- 追问钩子：能说出「用变异分数而不是行覆盖率评价测试有效性」的候选人，理解覆盖率的谎言（coverage ≠ quality）。

```typescript
// 变异测试原理：对源码做微小改动，检验测试能否发现
type Mutant = { id: string; desc: string; patch: (src: string) => string };

const mutants: Mutant[] = [
  { id: 'm1', desc: '边界 > 改为 >=',
    patch: s => s.replace('a > b', 'a >= b') },
  { id: 'm2', desc: '删除空值保护',
    patch: s => s.replace('x ?? 0', 'x') },
];

function mutationScore(source: string, test: (src: string) => boolean) {
  const killed = mutants.filter(m => {
    const mutated = m.patch(source);
    if (mutated === source) return false;      // 变异未生效，跳过
    try { test(mutated); return false; }        // 测试仍通过 → 变异存活（测试无效）
    catch { return true; }                      // 测试失败 → 变异被杀死
  });
  return {
    score: +(killed.length / mutants.length).toFixed(2),
    survivors: mutants.filter(m => !killed.includes(m)).map(m => m.desc),
  };
}
// 分数越高说明测试越能抓 bug；存活的变异体指出测试盲区
```
