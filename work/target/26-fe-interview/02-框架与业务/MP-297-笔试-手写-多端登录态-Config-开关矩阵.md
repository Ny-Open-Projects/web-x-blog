---
title: [MP-297] 笔试：手写远程 Config 开关矩阵（含缓存与兜底）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 笔试题
---

## MP-297：笔试：手写远程 Config 开关矩阵
**题**：实现 ConfigManager：init() 启动拉取远程配置（带本地缓存兜底——网络失败用上次配置）；get(key, defaultValue)；支持灰度分组（config 按 userBucket 返回不同值）；配置版本号 diff（相同版本不写 storage）；暴露订阅（key 变化通知）。

```javascript
class ConfigManager {
  constructor() { this.config = {}; this.subs = new Map() }
  async init(userId) {
    this.bucket = hashBucket(userId) // 0-99
    try {
      const res = await wx.request({ url: '/api/config', data: { bucket: this.bucket }, timeout: 3000 })
      if (res.data.version !== wx.getStorageSync('cfgVersion')) {
        this.config = res.data.config
        wx.setStorageSync('cfg', this.config)
        wx.setStorageSync('cfgVersion', res.data.version)
        this._notify()
      } else this.config = wx.getStorageSync('cfg') || {}
    } catch {
      this.config = wx.getStorageSync('cfg') || DEFAULT_CONFIG // 网络失败兜底
    }
  }
  get(key, dft) { return this.config[key] ?? dft }
  watch(key, fn) {
    if (!this.subs.has(key)) this.subs.set(key, new Set())
    this.subs.get(key).add(fn)
    return () => this.subs.get(key).delete(fn)
  }
  _notify() {
    this.subs.forEach((set, key) => { const v = this.config[key]; set.forEach(fn => fn(v)) })
  }
}
```
**评分点**：
- 本地缓存兜底（网络失败降级）。
- 版本 diff 减少 storage 写。
- 灰度 bucket 分组。
- watch 订阅让开关变化驱动 UI（热更新降级的前提）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-735dfdc4-6180-4141-920c-5470e58e19e9-cwd'; fi
exit "$__zcode_status"
