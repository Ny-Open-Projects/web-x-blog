---
title: [R19-341] 笔试：手写「发布商品后精准失效」的缓存计划
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-341：笔试：手写「发布商品后精准失效」的缓存计划
**题**：商品创建成功后需要：失效详情页缓存、失效列表页缓存、失效首页推荐位。实现 createGoodsAction 的 revalidate 编排，要求：tag 设计（goods:{id} / goods:list / home:recommend），避免全站失效；失效失败的补偿（重试/对账）。

```javascript
'use server'
export async function createGoods(prev, fd) {
  const user = await auth()
  if (!user?.perms.includes('goods:write')) return { ok: false, code: 'AUTH' }
  const parsed = goodsSchema.safeParse(Object.fromEntries(fd))
  if (!parsed.success) return { ok: false, fieldErrors: flatten(parsed.error) }
  const goods = await db.goods.create({ data: parsed.data })

  // 精准失效：按 tag
  revalidateTag(`goods:${goods.id}`)   // 详情页 fetch tags
  revalidateTag('goods:list')          // 列表页
  revalidateTag('home:recommend')      // 首页推荐
  return { ok: true, id: goods.id }
}
// 数据获取侧：
// fetch(api, { next: { tags: [`goods:${id}`, 'goods:list'] } })
```
**评分点**：
- tag 三层设计（详情/列表/聚合位）而非全站 revalidatePath('/')。
- fetch 侧 tags 挂载与 action 侧 revalidate 对齐。
- 说出补偿思路：revalidate 失败重试队列 / 定时对账 job。
- 权限校验在 revalidate 之前（失败不产生副作用）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-ab356313-5d62-420c-89ff-94dce41008a9-cwd'; fi
exit "$__zcode_status"
