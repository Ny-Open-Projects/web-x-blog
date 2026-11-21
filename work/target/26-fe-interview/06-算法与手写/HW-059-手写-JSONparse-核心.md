---
title: [HW-059] 手写 JSON.parse 核心
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-059：手写 JSON.parse 核心

**答**：
- 评分点：递归下降解析器（LL(1)）：一个全局索引 i + 按首字符分发——`{` 进 object、`[` 进 array、`"` 进 string、`t/f/n` 三个字面量、其余进 number；string 要处理转义（`\" \\ \/ \b \f \n \r \t \uXXXX`）；number 要支持负号、小数、指数（简化版可用 `parseFloat` + 边界校验）；每步跳过空白；**末尾校验**——解析完必须确保索引已到字符串末尾，`JSON.parse('{} x')` 要抛错；非法输入抛 SyntaxError 与原生行为对齐。

```javascript
// ===== 5 分钟速写版 =====
function jsonParse(str) {
  let i = 0;
  function value() {
    const ch = str[i];
    if (ch === '{') return obj();
    if (ch === '[') return arr();
    if (ch === '"') return string();
    if (str.startsWith('true', i)) { i += 4; return true; }
    if (str.startsWith('false', i)) { i += 5; return false; }
    if (str.startsWith('null', i)) { i += 4; return null; }
    return number();
  }
  function obj() {
    const o = {};
    i++; // 跳过 {
    while (str[i] !== '}') {
      const key = string();       // key 必须是字符串
      i++;                        // 跳过 :
      o[key] = value();
      if (str[i] === ',') i++;    // 跳过 ,
    }
    i++; // 跳过 }
    return o;
  }
  function arr() {
    const a = [];
    i++; // 跳过 [
    while (str[i] !== ']') {
      a.push(value());
      if (str[i] === ',') i++;
    }
    i++; // 跳过 ]
    return a;
  }
  function string() {
    let s = '';
    i++; // 跳过开引号
    while (str[i] !== '"') s += str[i++];
    i++; // 跳过闭引号
    return s;
  }
  function number() {
    const start = i;
    while (i < str.length && /[\d.eE+-]/.test(str[i])) i++;
    return parseFloat(str.slice(start, i));
  }
  return value();
}

// ===== 标准完整版（含边界处理）=====
function jsonParsePro(str) {
  if (typeof str !== 'string') throw new TypeError('input must be a string');
  let i = 0;
  const error = msg => { throw new SyntaxError(`${msg} at position ${i}`); };
  const skipWs = () => { while (i < str.length && /\s/.test(str[i])) i++; };
  function parseValue() {
    skipWs();
    if (i >= str.length) error('unexpected end');
    const ch = str[i];
    if (ch === '{') return parseObject();
    if (ch === '[') return parseArray();
    if (ch === '"') return parseString();
    if (str.startsWith('true', i)) { i += 4; return true; }
    if (str.startsWith('false', i)) { i += 5; return false; }
    if (str.startsWith('null', i)) { i += 4; return null; }
    return parseNumber();
  }
  function parseObject() {
    const o = {};
    i++; skipWs();
    if (str[i] === '}') { i++; return o; }         // 空对象
    for (;;) {
      skipWs();
      if (str[i] !== '"') error('object key must be string');
      const key = parseString();
      skipWs();
      if (str[i] !== ':') error('expected colon');
      i++;
      o[key] = parseValue();
      skipWs();
      if (str[i] === ',') { i++; continue; }        // 逗号后继续下一个键值对
      if (str[i] === '}') { i++; return o; }
      error('expected comma or brace');
    }
  }
  function parseArray() {
    const a = [];
    i++; skipWs();
    if (str[i] === ']') { i++; return a; }          // 空数组
    for (;;) {
      a.push(parseValue());
      skipWs();
      if (str[i] === ',') { i++; continue; }
      if (str[i] === ']') { i++; return a; }
      error('expected comma or bracket');
    }
  }
  function parseString() {
    let s = '';
    i++; // 跳过 "
    while (i < str.length) {
      const ch = str[i++];
      if (ch === '"') return s;
      if (ch === '\\') {
        const esc = str[i++];
        const map = { '"': '"', '\\': '\\', '/': '/', b: '\b', f: '\f', n: '\n', r: '\r', t: '\t' };
        if (esc in map) s += map[esc];
        else if (esc === 'u') {
          const hex = str.slice(i, i + 4);
          if (!/^[0-9a-fA-F]{4}$/.test(hex)) error('invalid unicode escape');
          s += String.fromCharCode(parseInt(hex, 16));
          i += 4;
        } else error(`invalid escape \\${esc}`);
      } else {
        s += ch; // 控制字符严格校验略（原生会拒绝未转义换行）
      }
    }
    error('unterminated string');
  }
  function parseNumber() {
    const start = i;
    if (str[i] === '-') i++;
    if (!/\d/.test(str[i] ?? '')) error('invalid number');
    while (/\d/.test(str[i] ?? '')) i++;
    if (str[i] === '.') { i++; while (/\d/.test(str[i] ?? '')) i++; }
    if (str[i] === 'e' || str[i] === 'E') {
      i++;
      if (str[i] === '+' || str[i] === '-') i++;
      while (/\d/.test(str[i] ?? '')) i++;
    }
    return parseFloat(str.slice(start, i));
  }
  const result = parseValue();
  skipWs();
  if (i < str.length) error('unexpected trailing content'); // '{} x' 必须报错
  return result;
}
```

---
