---
title: [V3-395] 笔试：手写 useRequest composable（竞态 + 重试 + 卸载取消）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-395：笔试：手写 useRequest composable（竞态 + 重试 + 卸载取消）
**题**：实现 `useRequest(loader, { watch, retry = 2 })` 返回 `{ data, error, loading, run }`：watch 源变化自动重发；快速连发时只保留最后一次结果（竞态防护）；失败重试带退避；组件卸载后 resolve 不再写 data。

```javascript
function useRequest(loader, { watch: src, retry = 2 } = {}) {
  const data = ref(null), error = ref(null), loading = ref(false)
  let seq = 0
  async function run() {
    const id = ++seq
    loading.value = true; error.value = null
    for (let i = 0; i <= retry; i++) {
      try {
        const res = await loader()
        if (id !== seq || getCurrentScope()?.active === false) return // 竞态/已卸载
        data.value = res
        break
      } catch (e) {
        if (i === retry) { if (id === seq) error.value = e }
        else await new Promise(r => setTimeout(r, 500 * 2 ** i))
      }
    }
    if (id === seq) loading.value = false
  }
  if (src) watch(src, run, { immediate: true })
  return { data, error, loading, run }
}
```
**评分点**：
- seq 序号竞态防护（核心得分点）。
- 卸载后不写入（getCurrentScope().active 判断）。
- 指数退避重试与最终失败落 error。
- loading 的最终状态由最后一次请求决定。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-e113c188-7404-4992-ba49-86f54c09998c-cwd'; fi
exit "$__zcode_status"
