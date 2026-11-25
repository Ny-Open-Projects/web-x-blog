---
title: [RBL-657] 构建器的 Fuzz 策略：语料库、结构感知生成与崩溃最小化
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-657：构建器的 Fuzz 策略：语料库、结构感知生成与崩溃最小化

**答**:
- 纯随机 fuzz 对解析器（RBL-585 提过）有效，但对打包器整体还不够——打包器的输入是「项目结构」（多文件 + 依赖关系 + 配置），结构性 fuzz：随机生成合法 JS/TS 文件 + 随机依赖图（含环/动态 import/条件导出）+ 随机配置组合，断言不变量（RBL-656 的闭合/确定性/语义等价）。
- 语料库（corpus）驱动：fuzz 的高价值输入来自真实 bug——历史 crash 样本 + OSS 项目摘录做种子，变异（语法级变异：插入语句/交换块/改导出）比盲变异（字节翻转）高效得多；覆盖引导（覆盖率反馈优先探索未覆盖路径，cargo-fuzz/libfuzzer 模式）。
- 崩溃最小化（test case reduction）：fuzz 找到 crash 后要自动最小化到可提交 fixture（ddmin 算法：反复尝试删除代码块，保持 crash 复现）——没有最小化，一个 10MB crash 样本无法变成回归测试。
- 不变量分层：fuzz 的「发现」不是断言崩溃，而是断言语义性质被破坏——崩溃（panic/segfault）只是最低层信号；「产物解析失败」「hash 不确定」「同输入两次构建产物不同」都是 fuzz 目标。
- 追问钩子：为什么 fuzz 对「转换正确性」比「崩溃」更有价值？——崩溃暴露的是工具自身的 bug（影响开发体验），转换语义破坏暴露的是「静默产出错误代码」（影响线上用户）；前者吵闹、后者致命，fuzz 资源应向后倾斜。

```javascript
// 结构感知 fuzz（JS 侧概念）
function* structuredCases() {
  for (let i = 0; i < 1000; i++) {
    const files = genRandomFiles(rnd(1, 8));             // 随机合法模块
    const graph = genRandomGraph(files, { cycles: rndBool(), dynamic: rndBool() });
    const config = genRandomConfig();                    // 随机 chunk/sourcemap/target
    yield { files, graph, config };
  }
}
for (const c of structuredCases()) {
  const out1 = tryBuild(c), out2 = tryBuild(c);
  if (out1.crash || out2.crash) minimizeAndReport(c);    // 崩溃 -> ddmin 最小化
  else if (out1.hash !== out2.hash)                      // 不变量：确定性
    report('非确定性', minimizeAndReport(c));
  else if (!parses(out1.code))
    report('产物不可解析', minimizeAndReport(c));
}

// ddmin 崩溃最小化（简化：按行块删除）
function ddmin(crashCase, stillCrashes) {
  let current = crashCase;
  let n = 2;
  while (current.lines.length > 1) {
    const chunkSize = Math.ceil(current.lines.length / n);
    let reduced = false;
    for (let i = 0; i * chunkSize < current.lines.length; i++) {
      const candidate = { ...current, lines: current.lines.filter((_, j) =>
        j < i * chunkSize || j >= (i + 1) * chunkSize) };
      if (stillCrashes(candidate)) { current = candidate; reduced = true; n = 2; break; }
    }
    if (!reduced) n = Math.min(n * 2, current.lines.length);
  }
  return current;                                        // 最小 crash 样本 -> fixture
}
```
