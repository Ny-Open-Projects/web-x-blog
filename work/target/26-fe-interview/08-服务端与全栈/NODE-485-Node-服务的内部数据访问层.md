---
title: [NODE-485] Node 服务的数据访问层（Repository 模式）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-485：Repository 数据访问层
**答**:
- 定位：service 只依赖 Repository 接口（业务语义方法：findPayableOrders），SQL 细节封装在实现内——可测试（mock repo）、可替换（换存储不动业务）、权限/租户注入的统一收口（NODE-361/395）。
- 设计纪律：方法按业务语义命名（不是泛化 CRUD——findByUserAndStatus 而非 generic query）、不做跨域 join（跨聚合取数走服务调用或视图，保持数据所有权边界）、分页/排序协议统一（NODE-400 cursor）。
- 读写分离落点：repo 方法声明读写（read 方法走副本 NODE-385）——路由决策收敛在 repo 层而不是 service 层散写。
- 事务边界：repo 方法单事务小而完整；跨 repo 事务由 service 用事务上下文编排（tx 参数传递 NODE-412），repo 不自作主张嵌套事务。
- 实现映射：一个 repo 对应一个聚合根（订单/商品），复杂查询（报表类）单独 query 服务（不塞进业务 repo）。
```javascript
// Repository 接口与实现
interface OrderRepo {
  findPayableByUser(uid: string, cursor?: Cursor): Promise<Page<Order>>;   // 业务语义
  markPaid(orderId: string, payNo: string, tx?: Tx): Promise<number>;      // 条件更新幂等
}
class PgOrderRepo implements OrderRepo {
  findPayableByUser(uid, cursor) { return replicaPool.query(cursorSql, [uid]); }  // 读副本
  markPaid(id, payNo, tx) {
    return (tx ?? pool).query(`update orders set status='paid', pay_no=$2
      where id=$1 and status='pending'`, [id, payNo]);           // 状态机条件更新
  }
}
```
