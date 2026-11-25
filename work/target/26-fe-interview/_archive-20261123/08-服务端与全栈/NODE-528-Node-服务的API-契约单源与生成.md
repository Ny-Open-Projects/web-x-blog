---
title: [NODE-528] Node 服务的 API 契约单源（proto/OpenAPI 驱动）工程如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-528：API 契约单源工程
**答**:
- 单源选择：REST 生态 OpenAPI（描述力全/生态广——BFF 对外主流）、内部高频 gRPC proto（NODE-483）、tRPC（全栈 TS 同仓库 NODE-366）——契约文件是唯一事实源（ARC-162/448）。
- 工程链路：契约仓库（契约变更 MR 评审——接口变更先改契约）、生成矩阵（服务端骨架/客户端/TS 类型/文档/mock 数据——NODE-513）、校验器（运行时请求/响应按契约校验——dev 模式全量校验快速发现偏差）。
- 一致性强制：CI 校验（实现与契约 diff——未同步阻断）、契约测试（NODE-334 消费者验证）、mock 服务从契约生成（联调期可用 NODE-366）。
- 版本治理：契约版本化 + 变更分级（NODE-447 diff 分级——兼容自动/不兼容走 sunset 流程）、契约历史（每版本归档——老客户端兼容验证依据 ARC-557）。
- 反模式：契约与代码双写（改代码忘了改契约——CI 强制消灭）、契约文件散落多仓库多格式（统一契约仓库）。
```bash
# 契约工程流水线
api/contracts/goods.yaml      # 唯一事实源
pnpm gen:all                  # → server-stub / ts-client / docs / mock
pnpm ci:contract-check        # 实现 diff + 消费者契约测试 + 版本分级检查
```
