---
title: [AIC-146] 笔试：实现一个 AI 输出 JSON 校验器，宽容解析围栏/注释/尾逗号，失败生成修复提示？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-146：笔试：实现一个 AI 输出 JSON 校验器，宽容解析围栏/注释/尾逗号，失败生成修复提示？
**需求**：实现 `parseAiJson(text, schema)`：
1. 预处理：剥离 markdown 围栏、`//` 注释、尾随逗号；
2. JSON.parse 失败时提取具体错误位置并生成「给模型的修复提示」；
3. 通过 JSON.parse 后按 schema 做字段校验（必填/类型/枚举），校验失败同样产出修复提示。

```javascript
const F = '\u0060'.repeat(3);   // 围栏用码点构造，避免源码内出现字面围栏
function preprocess(text) {
  return text
    .replace(new RegExp('^[\\s\\S]*?' + F + '(?:json)?\\s*\\n'), '')   // 去开头围栏（含解释文字）
    .replace(new RegExp('\\n?' + F + '\\s*$'), '')                     // 去结尾围栏
    .replace(/^\s*\/\/.*$/gm, '')                 // 去 // 注释
    .replace(/,(\s*[}\]])/g, '$1')                // 去尾随逗号
    .trim();
}

function validate(data, schema) {
  const errs = [];
  for (const [k, rule] of Object.entries(schema)) {
    const v = data?.[k];
    if (rule.required && (v === undefined || v === null)) {
      errs.push(`缺少必填字段 "${k}"`);
      continue;
    }
    if (v !== undefined && rule.type === 'array' && !Array.isArray(v)) errs.push(`"${k}" 应为数组`);
    if (v !== undefined && rule.type === 'number' && typeof v !== 'number') errs.push(`"${k}" 应为数字`);
    if (rule.enum && v !== undefined && !rule.enum.includes(v)) {
      errs.push(`"${k}" 必须是 ${rule.enum.join('/')} 之一`);
    }
  }
  return errs;
}

function parseAiJson(text, schema) {
  let data, errors = [];
  try {
    data = JSON.parse(preprocess(text));
    errors = validate(data, schema);
  } catch (e) {
    const pos = e.message.match(/position (\d+)/)?.[1];
    errors.push(`JSON 语法错误${pos ? `（位置 ${pos} 附近）` : ''}：${e.message}`);
  }
  if (errors.length) {
    return {
      ok: false,
      repairPrompt: `你的输出存在以下问题：\n${errors.map((e, i) => `${i + 1}. ${e}`).join('\n')}\n请只输出修正后的完整 JSON，不要任何解释。`,
    };
  }
  return { ok: true, data };
}

// 测试
const bad = '好的，结果如下：' + F + 'json\n{ "level": "高", "items": [1,2,] } // done\n' + F;
console.log(parseAiJson(bad, { level: { required: true, type: 'string', enum: ['low', 'high'] } }));
// ok:false + 修复提示（"高" 不在枚举里）
```

**评分点**：
1. 围栏剥离要处理「围栏前有解释文字」（用 `[\s\S]*?` 惰性匹配开头），只去围栏不去文字的写法是常见 bug；
2. 尾逗号正则 `,(\s*[}\]])` 方向正确（逗号在括号前），写反了会把合法 JSON 改坏；
3. 结构化输出必须做 schema 校验而非仅 JSON 合法性，能想到这层是区分度；
4. 失败时要产出可回喂模型的「修复提示」而非只抛错——闭环思维；
5. 注释剥离要区分字符串内的 `//`（说出此 limitation 加分）。
