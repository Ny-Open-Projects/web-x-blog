---
title: [NODE-762] 笔试题——实现压测影子路由（DB/MQ 影子化）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-762：手写影子路由

**需求与边界**：
- 需求：全链路压测影子化（SCN-NODE-717）——① ALS 标记贯穿（x-loadtest——SCN-NODE-670 同构）；② DB 影子路由（表名替换 t_order → t_order_shadow）；③ MQ 影子 topic（topic_suffix）；④ 下游调用影子 header 透传（全链——SCN-NODE-717）。
- 边界：① 表名替换的可靠方式（ORM 层 hook——不是正则改 SQL）；② 影子数据清理（定时任务——SCN-NODE-689 增长治理）；③ 接入门禁（新存储影子路由验证——SCN-联想-717）。

**答**：
```javascript
app.use((req, res, next) => {
  if (req.headers['x-loadtest'])
    tenantCtx.run({ ...tenantCtx.getStore(), shadow: true }, next);   // ALS 标记
  else next();
});
// ORM 层影子路由（Sequelize hook 示例）
sequelize.addHook('beforeFind', (options) => {
  if (tenantCtx.getStore()?.shadow)
    options.tableName = options.tableName + '_shadow';   // ORM hook（非正则 SQL）
});
sequelize.addHook('beforeCreate', (model, options) => {
  if (tenantCtx.getStore()?.shadow) options.tableName += '_shadow';
});
// MQ 影子 topic
async function publish(topic, payload) {
  const t = tenantCtx.getStore()?.shadow ? `${topic}_shadow` : topic;
  await mq.publish(t, payload);                        // 影子队列
}
// 下游透传
axios.interceptors.request.use(cfg => {
  if (tenantCtx.getStore()?.shadow) cfg.headers['x-loadtest'] = '1';   // 全链透传
  return cfg;
});
```

**评分点**:
- ALS 标记 + ORM hook 影子路由（非正则改 SQL——可靠性）。
- MQ 影子 topic + 下游 header 透传（全链——SCN-NODE-717）。
- 影子数据清理（增长治理——SCN-NODE-689）。
- 接入门禁意识（新存储未接入影子 = 污染生产）。
