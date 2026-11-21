---
title: [TST-125] 笔试：手写 mini 变异测试器（运算符变异 + 存活统计）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-125：笔试：手写 mini 变异测试器（运算符变异 + 存活统计）
**答**：
- 需求：实现 `mutantRun(sourcePath, testCmd)`——对源码做运算符变异（`>` ↔ `>=`、`===` ↔ `!==`、`+` ↔ `-`、`&&` ↔ `||`），每个变异体生成临时文件 → 跑测试 → 测试失败记 killed、通过记 survived；输出 mutation score，低于阈值退出码 1。
- 核心：字符串扫描按优先级替换（先长运算符 `===` 再 `==`，避免子串误替换）；每次只注入一个变异（标准做法）；用 child_process 跑 vitest/jest。
- 边界：变异后语法不合法（如 `a +` 末尾）跳过该变异体；测试命令超时按失败算（killed by timeout）；字符串里的运算符（'a >= b'）误替换是简化版的已知局限，注明即可。

```javascript
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';

const MUTATIONS = [
  ['===', '!=='], ['!==', '==='],
  ['>=', '>'], ['>', '>='], ['<=', '<'], ['<', '<='],
  ['&&', '||'], ['||', '&&'],
  ['+', '-'], ['-', '+'],
];

function* mutants(code) {
  for (const [from, to] of MUTATIONS) {
    let idx = 0;
    while ((idx = code.indexOf(from, idx)) !== -1) {
      const mutated = code.slice(0, idx) + to + code.slice(idx + from.length);
      yield { desc: `${from}→${to}@${idx}`, code: mutated };
      idx += from.length;
    }
  }
}

function mutantRun(srcPath, testCmd, { threshold = 60, timeoutMs = 30000 } = {}) {
  const code = readFileSync(srcPath, 'utf8');
  const tmp = srcPath.replace(/\.ts$/, '.mutant.ts');
  let killed = 0, total = 0;
  const survivors = [];

  for (const m of mutants(code)) {
    writeFileSync(tmp, m.code);
    total++;
    try {
      execSync(testCmd, { stdio: 'ignore', timeout: timeoutMs });
      survivors.push(m.desc);                    // 测试仍绿 → 变异存活，测试有洞
    } catch { killed++; }                        // 测试失败 → 变异被杀死
  }
  require('fs').unlinkSync(tmp);

  const score = total ? Math.round((killed / total) * 100) : 100;
  console.log(`mutation score: ${score}% (${killed}/${total})`);
  console.log('survived:', survivors);
  if (score < threshold) process.exit(1);
}

// mutantRun('src/utils/pricing.ts', 'npx vitest run src/utils/pricing.spec.ts');
// 输出示例：score 67% (2/3), survived: ['>→>=@41']
// → discount 函数里 > 边界没测到，补 score=90 的用例
```

**评分点**：
1. 每个变异体独立注入（不叠加），符合变异测试规范。
2. 「测试失败 = killed」语义正确，且超时按 killed 处理。
3. mutation score 计算与阈值退出码正确。
4. 是否意识到字符串/注释内误替换的局限（说明思考深度）。
