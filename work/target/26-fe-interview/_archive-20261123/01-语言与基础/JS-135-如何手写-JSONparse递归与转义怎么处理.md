---
title: [JS-135] 如何手写 JSON.parse？递归与转义怎么处理？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-135：如何手写 JSON.parse？递归与转义怎么处理？

**答**：
- 手写方案：游标 + 递归下降——一个 `parseValue` 按 `{`/`[`/`"`/t/f/n/数字 分派。
- 字符串解析要处理转义：`\n \t \r \b \f \" \\ \/` 与 `\uXXXX`（String.fromCharCode）。
- 数字用正则匹配完整 token（含小数与指数）后交给 Number。
- 结束后校验游标是否到尾，避免 `{"a":1}garbage` 被静默接受。

```javascript
function jsonParse(text) {
  let i = 0;
  const isWs = (ch) => ch === ' ' || ch === '\t' || ch === '\n' || ch === '\r';
  const skip = () => { while (i < text.length && isWs(text[i])) i++; };
  const fail = (msg) => { throw new SyntaxError(`${msg}（位置 ${i}）`); };

  function parseValue() {
    skip();
    const c = text[i];
    if (c === '{') return parseObject();
    if (c === '[') return parseArray();
    if (c === '"') return parseString();
    if (text.startsWith('true', i))  { i += 4; return true; }
    if (text.startsWith('false', i)) { i += 5; return false; }
    if (text.startsWith('null', i))  { i += 4; return null; }
    return parseNumber();
  }

  function parseObject() {
    const obj = {}; i++; skip();
    if (text[i] === '}') { i++; return obj; }
    while (true) {
      skip();
      if (text[i] !== '"') fail('对象键必须是字符串');
      const key = parseString(); skip();
      if (text[i] !== ':') fail('缺少冒号');
      i++;
      obj[key] = parseValue(); skip();
      if (text[i] === ',') { i++; continue; }
      if (text[i] === '}') { i++; return obj; }
      fail('对象格式错误');
    }
  }

  function parseArray() {
    const arr = []; i++; skip();
    if (text[i] === ']') { i++; return arr; }
    while (true) {
      arr.push(parseValue()); skip();
      if (text[i] === ',') { i++; continue; }
      if (text[i] === ']') { i++; return arr; }
      fail('数组格式错误');
    }
  }

  function parseString() {
    i++; let out = '';
    while (text[i] !== '"') {
      if (i >= text.length) fail('字符串未闭合');
      if (text[i] === '\\') {
        i++;
        const esc = text[i];
        if (esc === 'u') {
          out += String.fromCharCode(parseInt(text.slice(i + 1, i + 5), 16));
          i += 4;
        } else {
          out += { n: '\n', t: '\t', r: '\r', b: '\b', f: '\f' }[esc] ?? esc; // " \ / 走默认
        }
      } else {
        out += text[i];
      }
      i++;
    }
    i++; return out;
  }

  function parseNumber() {
    const m = /^-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?/.exec(text.slice(i));
    if (!m || m[0] === '') fail('非法数字');
    i += m[0].length;
    return Number(m[0]);
  }

  const result = parseValue();
  skip();
  if (i < text.length) fail('末尾有多余内容'); // 防止 {"a":1}xxx
  return result;
}

console.log(jsonParse('{"a":[1,2.5,true,null,"x\\n\\u4e2d"],"b":{"c":-3e2}}'));
// { a: [1, 2.5, true, null, 'x\n中'], b: { c: -300 } }
```
