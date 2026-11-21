---
title: [R19-325] 笔试：手写一个支持重试的 Suspense 容器
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-325：笔试：手写支持重试的 Suspense 容器
**题**：实现 `MySuspense` 类组件：捕获子树 throw 的 promise（getDerivedStateFromError 无法区分——用 componentDidCatch 判断是否 promise）；pending 时渲染 fallback；promise resolve 后重渲染子树；rejected 渲染 error UI 并提供 retry（重挂载子组件，key 自增）。

```javascript
class MySuspense extends React.Component {
  state = { pending: false, error: null, attempt: 0 }
  componentDidCatch(thrown) {
    if (thrown && typeof thrown.then === 'function') {
      this.setState({ pending: true })
      thrown.finally?.(() => this.setState({ pending: false })) // resolve 后重试渲染
    } else {
      this.setState({ error: thrown })
    }
  }
  retry = () => this.setState(s => ({ error: null, attempt: s.attempt + 1 }))
  render() {
    if (this.state.pending) return this.props.fallback
    if (this.state.error) {
      return typeof this.props.renderError === 'function'
        ? this.props.renderError(this.state.error, this.retry)
        : <div>出错了 <button onClick={this.retry}>重试</button></div>
    }
    return <div key={this.state.attempt}>{this.props.children}</div> // key 强制重建子树
  }
}
```
**评分点**：
- componentDidCatch 区分 promise（thenable）与真实错误。
- resolve 后重渲染（真实 React 在调度器层做，此处简化）。
- retry 用 key 自增强制子树重建。
- 说明真实 Suspense 在 render 阶段（非错误通道）捕获，性能远优于 componentDidCatch 模拟。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-2e71b4d6-d634-4d6c-a073-fb5ff050fe15-cwd'; fi
exit "$__zcode_status"
