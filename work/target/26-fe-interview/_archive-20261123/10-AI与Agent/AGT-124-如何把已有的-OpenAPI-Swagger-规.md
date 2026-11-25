---
title: [AGT-124] 如何把已有的 OpenAPI/Swagger 规范自动生成 MCP 工具？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-124：如何把已有的 OpenAPI/Swagger 规范自动生成 MCP 工具？
**答**：
- 思路：OpenAPI 文档已经是「工具名+描述+参数 schema」的机器可读来源，写一个转换器即可批量生成 MCP tools，避免手写重复定义。
- 关键裁剪：只暴露安全的 GET（读）与明确标记可写的 POST，DELETE 等高危方法默认排除；`operationId` 映射工具名，`description` 来自文档注释。
- 参数映射：path/query/body 参数合并为一个 JSON Schema 对象，`required` 从 OpenAPI 的 required 字段推导。
- 补一层执行适配：注入 base URL 与鉴权头（凭证不进模型上下文），模型只看到工具签名，看不到 Key。

```typescript
// OpenAPI → MCP tools 转换器
interface OpenApiSpec { paths: Record<string, Record<string, any>>; }

const ALLOWED_METHODS = new Set(['get', 'post']); // DELETE/PUT 默认不暴露给模型
const EXCLUDED = [/\/internal\//, /\/admin\//];   // 内部与管道路径排除

function openApiToTools(spec: OpenApiSpec, baseUrl: string, headers: Record<string, string>) {
  const tools: any[] = [];
  for (const [path, methods] of Object.entries(spec.paths)) {
    if (EXCLUDED.some((re) => re.test(path))) continue;
    for (const [method, op] of Object.entries(methods)) {
      if (!ALLOWED_METHODS.has(method) || !op.operationId) continue;
      const props: Record<string, any> = {};
      const required: string[] = [];
      for (const p of op.parameters ?? []) {
        props[p.name] = { type: p.schema?.type ?? 'string', description: p.description ?? '' };
        if (p.required) required.push(p.name);
      }
      if (op.requestBody?.content?.['application/json']?.schema) {
        props.body = { type: 'object', description: '请求体' }; // body 整体透传，细化交给服务端校验
      }
      tools.push({
        name: op.operationId,
        description: `${method.toUpperCase()} ${path} —— ${op.summary ?? ''}`,
        inputSchema: { type: 'object', properties: props, required },
        execute: async (args: Record<string, any>) => {
          const url = new URL(baseUrl + path.replace(/\{(\w+)\}/g, (_, k) => encodeURIComponent(args[k] ?? '')));
          for (const p of op.parameters ?? []) {
            if (p.in === 'query' && args[p.name] != null) url.searchParams.set(p.name, String(args[p.name]));
          }
          const res = await fetch(url, {
            method: method.toUpperCase(),
            headers: { 'Content-Type': 'application/json', ...headers }, // 鉴权凭证只在执行层
            body: method === 'post' ? JSON.stringify(args.body ?? {}) : undefined,
          });
          if (!res.ok) throw new Error(`API ${res.status}`);
          return res.json();
        },
      });
    }
  }
  return tools;
}
```
