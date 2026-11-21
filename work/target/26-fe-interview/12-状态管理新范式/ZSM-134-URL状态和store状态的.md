---
title: [ZSM-134] 筛选条件放 URL 还是 store？两种方案的边界和迁移路径是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-134：筛选条件放 URL 还是 store？两种方案的边界和迁移路径是什么？
**答**：
- 放 URL 的判据：需要分享链接、刷新保留、前进后退、SEO 可见——列表页筛选、分页、tab、排序全部归 URL。
- 放 store 的判据：跨页面无感共享、值本身不适合暴露在地址栏（长文本、复杂结构）、纯交互态（多选临时勾选未提交）。
- 灰色地带用「URL + store 混合」：URL 存可分享的主条件，store 存临时副条件（如勾选的行），提交时把 store 条件合入 URL。
- 迁移路径：老项目 store 筛选迁 URL 时，先做双向同步（store 变化写 URL，URL 变化写 store）过渡一版，稳定后删掉 store 侧 owner，避免一次性大改。

```javascript
// 混合方案：主条件 URL 化，临时勾选留 store
function GoodsListPage() {
  const [sp, setSp] = useSearchParams()                 // owner：URL
  const kw = sp.get('kw') ?? '', page = Number(sp.get('page') ?? 1)
  const checked = useTempSelection(s => s.ids)          // owner：store（临时）
  const { data } = useQuery({
    queryKey: ['goods', { kw, page }],
    queryFn: () => api.goods({ kw, page }),
  })

  function applyFilters(next) {
    const nsp = new URLSearchParams(sp)
    Object.entries(next).forEach(([k, v]) =>
      v === '' ? nsp.delete(k) : nsp.set(k, v))         // 空值清参数，保持 URL 干净
    setSp(nsp)                                          // URL 变化驱动重取
  }
  return <Table rows={data?.list} checked={checked} onFilter={applyFilters}/>
}
```
