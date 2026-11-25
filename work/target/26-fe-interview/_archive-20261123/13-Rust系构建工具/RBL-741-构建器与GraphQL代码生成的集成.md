---
title: [RBL-741] 代码生成类工具与构建器的集成：GraphQL/RTK query 的增量生成与类型一致性
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-741：代码生成类工具与构建器的集成：GraphQL/RTK Query 的增量生成与类型一致性

**答**:
- 代码生成（GraphQL codegen/openapi-typescript）与构建器的三种集成形态：1) 独立步骤（CI 前置：schema 变化 → 生成 types → 再构建——简单但 schema 检查与构建解耦，dev 里要手动跑）；2) 构建器插件（resolve/load 虚拟模块拦截 `*.graphql` import 实时生成——dev 即时但生成器重计算进热路径）；3) 混合（dev 用 watcher 常驻生成进程、CI 独立步骤 + 一致性校验）——工程上第三种最稳。
- 一致性校验是关键：生成产物与源 schema 必须同步——「生成的类型过期」是静默 bug 源（TS 按旧类型通过、运行时字段不存在）；构建器在 CI 里做「生成器幂等校验」（重新生成 → diff 产物 → 不一致 fail）。
- 增量生成：schema 大（几千类型）时全量生成秒级——增量策略：按「使用的 operation 文件」分片生成（codegen 按 document 分组缓存），schema 变化只重新生成受影响分片；缓存键 = schema hash + document hash。
- 生成产物的存放哲学：提交入仓（review 可见、消费简单——多数团队选择）vs 构建时生成（无入仓噪音但要保证 CI 幂等）——选择必须全组织统一，混用会出现「本地生成的类型与入仓版本打架」。
- 追问钩子：为什么 GraphQL codegen 的增量比模块 transform 难？——生成的类型文件是全局耦合（一个 fragment 类型被多处引用），「受影响分片」的判定需要类型依赖图（schema 类型 → 使用它的 document）；这是「codegen 的模块图」，多数工具没做，所以增量收益打折。

```javascript
// 构建器插件式 GraphQL 虚拟模块（dev 形态）
function graphqlPlugin(schemaLoader, codegen) {
  const VIRTUAL = '\0/graphql-types.ts';
  return {
    name: 'graphql-types',
    resolveId(id) { if (id === 'virtual:gql-types') return VIRTUAL; },
    async load(id) {
      if (id !== VIRTUAL) return;
      const schema = await schemaLoader();
      return codegen(schema);                            // 实时生成 dev 类型
    },
  };
}
// CI 幂等校验
async function verifyCodegenFreshness({ schemaPath, outPath, regenerate }) {
  const committed = fs.readFileSync(outPath, 'utf8');
  const fresh = await regenerate(schemaPath);
  if (committed !== fresh)
    fail('codegen 产物过期：schema 已变但未重新生成并提交——请运行 pnpm codegen');
}
```
