---
disableNunjucks: true
title: "715 Viper 动态监听：WatchConfig + OnConfigChange"
date: 2026-10-07 10:28:46
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：配置中心 / Viper | 难度：L3 | 题型：工程题 | 频率：极高 | 关键词：**WatchConfig、OnConfigChange、热更新、回调、全局配置重映射**

> 原文锚点：第 52~57 段「使用 WatchConfig 方法监听配置文件变更…注册 OnConfigChange 回调，在回调里拿到变更后的值并重新映射到全局配置变量」

## 一句话总述
动态监听靠 `WatchConfig()` 开启文件监听，再用 `OnConfigChange` 注册回调：文件变更时回调拿到新值，把最新配置重新 Unmarshal 进全局变量即可热更新，无需重启进程。

## 面试官视角
P6 能写出 WatchConfig+OnConfigChange；P7 要讲清「回调里必须重新 Unmarshal 整个结构体」，以及热更新只改内存变量、要配合校验和并发安全，不能只打印。

## 主问答
**Q（面试官原话）：** 不重启服务怎么让配置生效？

1. **开启监听**：`v.WatchConfig()` 启动对配置文件的 fsnotify 监听 `[源码]`。
2. **注册回调**：`v.OnConfigChange(func(e fsnotify.Event))` 在变更时触发，入参是文件事件 `[源码]`。
3. **回调用新值**：回调里再次 `v.Unmarshal(&cfg)` 把最新值映射到全局变量，并打印确认 `[源码]`。
4. **演示验证**：改 ENV 从 DEV 存盘，终端即打印出新值 PROD，证明通知真的到达 `[实测]`。
5. **工程注意**：热更新只改内存；需做配置校验，且全局变量读写要考虑并发安全（原子或锁）`[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 哪两个 API？ | 答不出 Watch/OnConfigChange |
| L2 | 回调做什么？ | 说不出重 Unmarshal |
| L3 | 怎么验证？ | 答不出改文件看日志 |
| L4 | 只打印够吗？ | 答不出校验+并发安全 |
| L5 | 生产风险？ | 答不出脏配置/校验缺失 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| spf13/viper 1.x | 默认集成 fsnotify | WatchConfig 即用 |
| 任意版本 | 仅文件监听 | 远程配置需配合 poll/etcd |
| 任意版本 | 回调串行 | 重映射要快，别阻塞 |

## 关键代码
```go
v.WatchConfig()
v.OnConfigChange(func(e fsnotify.Event) {
    var c Config
    if err := v.Unmarshal(&c); err != nil {
        log.Printf("reload skip: %v", err) // 校验失败不覆盖旧值
        return
    }
    atomic.StorePointer(&gCfg, unsafe.Pointer(&c)) // 并发安全替换
})
```

## 总结与追问预判
**动态监听是「能监但不能滥用」的典型**。下一步常问：哪些配置绝不能热更新——见同批 715-config-safety。

## ⚠️ 原文纠错
1. 事实核校：WatchConfig 开启监听、OnConfigChange 在变更时回调并重新 Unmarshal 的描述准确，与官方 API 一致 `[经验]`。
2. 补充：原文演示用 log.Printf 打印，生产应做「校验失败不覆盖旧值」的防御，避免脏配置击穿 `[经验]`。
3. 崩坏词归一：源码将 Viper、回调、全局配置等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
