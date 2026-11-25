---
title: [OPS-195] 双活发布（双 CDN 双写检测）怎么落地？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-195：双活发布（双 CDN 双写检测）怎么落地？
**答**：
- 双写：发布产物同时上传两家 CDN 的源（对象存储双桶），入口刷新两家同时执行——备份 CDN 永远是"热的"。
- 常驻分流验证：80/20 分流，20% 流量持续验证备用 CDN 的真实服务能力（OPS-190 的"经过验证"）。
- 漂移检测：定时从两家并发拉取入口与代表资源比对内容指纹，发布窗口外不一致即告警。
- 切换 = DNS 权重对调（分钟级），无需紧急上传——因为一直在双写。
- 双写成本可控：存储翻倍但流量按实际分流计费；演练验证切换全链路（OPS-170）。

```bash
# 双 CDN 双写与漂移检测
#!/usr/bin/env bash
CDN_A=cdn-a.example.com; CDN_B=cdn-b.example.com
check() {
  local path=$1
  HA=$(curl -s "https://$CDN_A$path" | sha256sum | cut -d' ' -f1)
  HB=$(curl -s "https://$CDN_B$path" | sha256sum | cut -d' ' -f1)
  if [ "$HA" != "$HB" ]; then
    # 发布灰度窗口内两版本共存属正常；窗口外不一致即漂移告警
    echo "MISMATCH $path" | tee -a /var/log/dual-cdn-drift.log
  else
    echo "OK $path"
  fi
}
for p in /index.html /static/app.js /static/app.css; do check "$p"; done

# 双写原则：
# 1. 产物同时上传两家源（对象存储双桶），入口刷新两家同时执行（OPS-117 任务化）
# 2. DNS 80/20 常驻分流，20% 流量持续验证备用 CDN 服务能力
# 3. 主 CDN 故障 → DNS 权重对调（分钟级），无需紧急上传——备份一直是热的
```
