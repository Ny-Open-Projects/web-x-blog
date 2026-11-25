---
title: [MFW-120] 笔试：手写一个 markdown frontmatter 解析器（含校验）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-120：笔试：手写一个 markdown frontmatter 解析器（含校验）
**答**：内容站构建期要解析 markdown 文件的 frontmatter。实现 `parseFrontmatter(source, schema)`：① 解析文件头 `---` 包裹的 YAML 简化子集（key: value、数组 `- item`、嵌套一层）；② 用 schema（形如 zod 的 `{ validate(v) }` 对象）校验；③ 校验失败抛出带字段名的错误；④ 无 frontmatter 或格式错时给出明确错误；⑤ 返回 `{ data, content }`。

```ts
type Schema = { validate: (v: Record<string, unknown>) => { ok: true } | { ok: false; errors: string[] } };

function parseScalar(raw: string): unknown {
  const s = raw.trim();
  if (s === 'true') return true;
  if (s === 'false') return false;
  if (/^-?\d+(\.\d+)?$/.test(s)) return Number(s);
  return s.replace(/^["']|["']$/g, ''); // 去引号
}

function parseFrontmatter(source: string, schema: Schema): { data: Record<string, unknown>; content: string } {
  const m = source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!m) throw new Error('缺少 frontmatter（文件头需以 --- 开始并闭合）');

  const data: Record<string, unknown> = {};
  let currentKey: string | null = null;

  for (const line of m[1].split(/\r?\n/)) {
    if (!line.trim()) continue;
    if (/^\s+-\s/.test(line)) {
      // 数组项：挂到上一个 key
      if (!currentKey) throw new Error('数组项出现在无主键位置: ' + line);
      if (!Array.isArray(data[currentKey])) data[currentKey] = [];
      (data[currentKey] as unknown[]).push(parseScalar(line.replace(/^\s+-\s*/, '')));
      continue;
    }
    const kv = line.match(/^([A-Za-z_][\w-]*):\s*(.*)$/);
    if (!kv) throw new Error('无法解析的行: ' + line);
    currentKey = kv[1];
    if (kv[2].trim() === '' || kv[2].trim() === '[]') {
      data[currentKey] = kv[2].trim() === '[]' ? [] : [];
    } else {
      data[currentKey] = parseScalar(kv[2]);
    }
  }

  const result = schema.validate(data);
  if (!result.ok) {
    throw new Error('frontmatter 校验失败: ' + result.errors.join('; ')); // 字段级错误
  }
  return { data, content: source.slice(m[0].length) };
}

// —— 用例 ——
const schema: Schema = {
  validate(v) {
    const errors: string[] = [];
    if (typeof v.title !== 'string' || !v.title) errors.push('title 必须为非空字符串');
    if (!Array.isArray(v.tags)) errors.push('tags 必须为数组');
    return errors.length ? { ok: false as const, errors } : { ok: true as const };
  },
};
const src = `---
title: "Astro 入门"
tags:
  - ssr
  - astro
draft: false
---
正文内容…`;
// parseFrontmatter(src, schema).data => { title: 'Astro 入门', tags: ['ssr','astro'], draft: false }
```

**评分点**：
1. frontmatter 边界正则正确处理 `---` 开闭与换行（含 CRLF 更佳）。
2. 类型推导顺序：布尔 → 数字 → 去引号字符串，数值不误伤 `1.5`、负数。
3. 数组项 `- item` 挂到最近主键，无主键时报错而不是静默丢失。
4. 校验错误带字段名聚合输出，方便内容团队定位。
5. content 切分用 match 长度而非硬编码索引，避免少剥换行。
