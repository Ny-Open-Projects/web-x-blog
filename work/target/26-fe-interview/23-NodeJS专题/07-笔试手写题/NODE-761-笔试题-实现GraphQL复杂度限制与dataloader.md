---
title: [NODE-761] 笔试题——实现 GraphQL 复杂度限制与 per-request loader？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-761：手写 GraphQL 防护

**需求与边界**：
- 需求：GraphQL 网关防护（SCN-NODE-662）——① 复杂度计算（depth + 字段成本——恶意深查询防御）；② per-request Dataloader（SCN-NODE-742）；③ 错误脱敏（不泄露堆栈）；④ APQ（持久查询——防任意查询注入）。
- 边界：① 复杂度按字段声明（每字段 cost——列表字段 ×分页大小）；② introspection 生产禁用（schema 泄露防御）；③ 错误统一格式（errors 数组——message 脱敏 + extensions.code）。

**答**：
```javascript
function complexityRule({ maxCost = 1000 } = {}) {
  return (query) => {
    let cost = 0;
    visit(query, { Field: { enter: (node) => {
      cost += FIELD_COST[node.name.value] ?? 1;
      const arg = node.arguments?.find(a => a.name.value === 'first');
      if (arg) cost += (FIELD_COST[node.name.value] ?? 1) * intArg(arg) * 0.5;   // 列表 × 分页
      if (cost > maxCost) throw new GraphQLError('COST_EXCEEDED', { extensions: { code: 'TOO_COMPLEX' } });
    } } });
    return cost;
  };
}
app.use('/graphql', graphqlHTTP({
  schema,
  context: () => ({ loaders: { user: new DataLoader(batch) } }),   // per-request（SCN-NODE-662）
  validationRules: [depthLimit(10)],
  customValidateFn: (schema, doc) => validate(schema, doc, [complexityRule()]),
  formatError: (e) => ({ message: mask(e.message), extensions: { code: e.extensions?.code } }),   // 脱敏
}));
```

**评分点**:
- 复杂度按字段 cost + 列表放大（恶意深查询/大分页防御）。
- per-request Dataloader（SCN-NODE-742 安全红线）。
- formatError 脱敏（message 掩码 + code——SCN-NODE-676）。
- APQ/depthLimit 双防（任意查询注入）。
