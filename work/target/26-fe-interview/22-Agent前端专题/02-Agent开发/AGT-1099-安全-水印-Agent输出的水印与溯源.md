---
title: [1099] Agent 输出内容的水印与溯源怎么实现
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 水印]
type: 面试题
---

## 1099：Agent 输出内容的水印与溯源怎么实现

**答**：
- 水印两类：显式水印（输出带来源声明/版本号，防抵赖）、统计水印（token 采样偏置编码指纹，可从纯文本检测出「是否本系统生成」——用于追查泄漏源与滥用）。
- 统计水印实现：生成时对候选 token 按绿/红名单偏置采样（密钥控制），检测时算绿名单命中率，超基线即判定为本系统输出；代价是可能轻微影响质量。
- 元数据溯源：输出内容嵌入不可见元数据（taskId、时间、模型版本），外泄内容可定位到具体会话。
- 追问钩子：水印会被洗掉吗？——改写/翻译能削弱统计水印；工程目标是「提高溯源概率」不是绝对防伪，配合访问日志与输出审查形成组合证据。

```ts
async function watermarkedGen(prompt, key) {
  const green = hashToSet(key, vocab);
  return llm.sample(prompt, {
    bias: tok => green.has(tok) ? +2 : 0,          // 绿名单偏置采样
    meta: { taskId: ctx.taskId, ver: MODEL_VER },  // 溯源元数据
  });
}
function detect(text, key) {
  const green = hashToSet(key, vocab);
  const rate = tokenize(text).filter(t => green.has(t)).length / tokenize(text).length;
  return { likely: rate > BASELINE + 0.15, rate }; // 超基线判定
}
```
