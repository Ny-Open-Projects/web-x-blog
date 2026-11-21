---
title: 事务化发布：为什么发布接口必须开事务
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 原理, 事务, TypeORM]
---

## 事务化发布：为什么发布接口必须开事务

发布一次页面 = 多条写操作：置空并更新 Page → 删旧 Component →（保留 component_data）→ 插入新组件 → 回填 ID。任何一步失败都可能留下"删了旧的、新的没插进去"的脏数据——所以必须原子化。

**本项目实例**（TypeORM QueryRunner 三段式）：

```ts
const queryRunner = this.dataSource.createQueryRunner();
await queryRunner.connect();
await queryRunner.startTransaction();
try {
  // 按用户 ID（account_id）查：存在则先置空 components、删旧组件行、插新组件行
  await queryRunner.manager.save(...);  // 事务内操作必须走 queryRunner.manager
  await queryRunner.commitTransaction();
} catch (err) {
  await queryRunner.rollbackTransaction();   // catch 必须回滚
  throw new InternalServerErrorException(err); // 失败要抛具体 error（教学实现；生产应对外固定文案、err 只进日志）
} finally {
  await queryRunner.release();  // 防连接泄漏
}
```

三个坑：①事务内混用普通 repository 会脱离事务管辖；②catch 不回滚则半成品落库；③不 release 则连接池泄漏。

课程版修正点：最终仓库修正点：课程原始实现会连问卷数据一起删；参考实现已改为保留 component_data 行——但组件 id 每次发布重生成，历史答案与组件的关联断裂，统计端对失效 id 容错。

出处「课程25 · 14-4、10-8；scan3」
