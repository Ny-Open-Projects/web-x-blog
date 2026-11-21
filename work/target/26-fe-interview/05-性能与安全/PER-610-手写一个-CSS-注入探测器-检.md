---
title: [PER-610] 手写一个 CSS 注入探测器：检测页面是否存在可被属性选择器外泄数据的可探测输入组合
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-610：手写一个 CSS 注入探测器：检测页面是否存在可被属性选择器外泄数据的可探测输入组合

**答**：
- 检测两条件组合：页面存在**用户可控 CSS**（inline style 或 <style> 内容包含用户输入）且**同页存在敏感输入控件**（密码框、搜索框等）——二者同现即存在字符探测外泄面。
- 实现：扫 DOM 收集带 style 属性的元素，检查其值是否包含用户可控特征（测试时注入标记串）；收集 input[type=password/text name 含敏感词]；两者同容器（同 document）即输出风险。
- 要点：可控 CSS 的判定用注入探针值验证——往数据里塞 `probe-css-123` 再检查是否出现在 style 中；密码输入框永远算敏感目标。
- 评分点：探针注入验证法与敏感输入识别。

```javascript

function probeCssInjection() {
  const PROBE = 'probe-css-zz9';
  // 1) 找出所有 style 属性/样式标签中包含探针的元素（说明用户输入进了 CSS）
  const injectable = [...document.querySelectorAll('[style], style')]
    .filter(el => (el.getAttribute?.('style') ?? el.textContent ?? '').includes(PROBE));
  // 2) 收集敏感输入目标
  const sensitive = [...document.querySelectorAll('input')]
    .filter(i => i.type === 'password' || /name|phone|idcard|search/i.test(i.name ?? ''));
  // 3) 属性选择器可达性：同一 document 即可写 input[value^=x] 选择器
  const risky = injectable.length > 0 && sensitive.length > 0;
  return {
    injectableCss: injectable.map(e => e.tagName),
    sensitiveInputs: sensitive.map(i => i.type + ':' + (i.name ?? '')),
    leakSurface: risky,
    verdict: risky ? '存在 CSS 字符探测外泄面：净化 style 或隔离敏感输入' : '未发现',
  };
}
// 测试流程：先往可控字段写入 PROBE 值，再运行探测
```
