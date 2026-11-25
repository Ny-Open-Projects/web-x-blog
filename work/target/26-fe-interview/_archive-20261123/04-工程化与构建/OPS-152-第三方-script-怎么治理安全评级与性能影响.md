---
title: [OPS-152] 第三方 script 怎么治理？安全评级与性能影响怎么管？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-152：第三方 script 怎么治理？安全评级与性能影响怎么管？
**答**：
- 清单制：所有第三方 script 登记用途/版本/体积/评级/复审时间，未登记的域名在 CSP 层直接拦掉。
- 统一出网：第三方资源统一从自建反代域名加载（/tp/xxx），缓存可控、出向连接收敛、下线只需要改一条配置。
- 性能影响量化：全部 async/延迟注入，用 PerformanceObserver 统计第三方对 long task 的贡献占比。
- 安全复审到期自动告警，过期未复审的第三方建议下线；加载失败必须不影响主功能（错误隔离）。
- 季度复审：结合用量数据（是否真的被使用）与安全评级决定保留/替换/下线。

```json
{
  "third_party_scripts": {
    "policy": "新增第三方 script 须登记评审；季度复审清退；CSP 白名单与清单同步",
    "inventory": [
      {
        "name": "ga4",
        "purpose": "流量统计",
        "version": "locked-2026.10",
        "size_kb": 92,
        "load_mode": "async",
        "sri": true,
        "security_review": "2026-09 过审",
        "perf_impact": "延迟加载，LCP 影响 < 20ms"
      },
      {
        "name": "chat-widget",
        "purpose": "在线客服",
        "version": "3.12.0",
        "size_kb": 410,
        "load_mode": "idle-inject-3s",
        "sri": false,
        "security_review": "Q4 复审中",
        "perf_impact": "主线程 long task 贡献 4%，观察项"
      }
    ],
    "governance_rules": [
      "统一从自建反代域名加载（/tp/ga/*），出网收敛、缓存可控",
      "加载失败不影响主功能：全部 async 且错误隔离",
      "security_review 过期未复审自动告警并建议下线",
      "PerformanceObserver 统计第三方 long task 贡献占比，超 10% 立项优化"
    ]
  }
}
```

---

## 十七、成本与效率（OPS-153 ~ OPS-159）

运维的另一半是账本与效率：CDN 流量、构建时长、服务器、多环境、包体积、DORA 指标与自动化优先级。
