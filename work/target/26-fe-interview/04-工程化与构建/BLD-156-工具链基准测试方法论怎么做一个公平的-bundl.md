---
title: [BLD-156] 工具链基准测试方法论：怎么做一个公平的 bundler benchmark？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-156：工具链基准测试方法论：怎么做一个公平的 bundler benchmark？
**答**：
- **变量控制**：同一份真实项目快照（含 node_modules、相同 lockfile）、同机独占（禁 turbo boost? 至少记录 CPU 频率）、多次运行取中位数（冷/热缓存分开统计）、报告 p95 而非均值。
- **口径定义**：冷启动（无缓存）、增量（改 N 个文件后 rebuild）、产物质量（体积/gzip/首屏请求数）、dev 体感（首屏 TTFB、HMR 全链路延迟）——只测"构建耗时"是最常见的错误。
- **公平性陷阱**：配置不等价（webpack 未开缓存 vs vite 有预构建缓存）、压缩器不同（terser vs esbuild 比时间无意义）、插件差异（babel 配置不同）——每个差异要在报告中显式声明。
- 产出物：可复现脚本（repo + 命令）+ 数据表 + 结论边界（"在本场景下 X 快 Y%，在 Z 场景结论不成立"）。

```bash
#!/usr/bin/env bash
# bench/run-bench.sh：可复现的多工具基准脚本骨架
set -euo pipefail
REPO_SNAPSHOT=$1   # 项目快照目录（含 lockfile）
RUNS=${RUNS:-5}
OUT=bench-results/$(date +%s).csv
echo "tool,scenario,run,ms" >> "$OUT"

measure() { # $1=tool $2=scenario $3=command
  for i in $(seq 1 "$RUNS"); do
    rm -rf "$REPO_SNAPSHOT/dist" "$REPO_SNAPSHOT/node_modules/.cache"
    local start end
    start=$(python3 - <<'PY' 2>/dev/null || date +%s%N
import time; print(time.time_ns())
PY
)
    (cd "$REPO_SNAPSHOT" && eval "$3" > /dev/null 2>&1)
    end=$(date +%s%N)
    echo "$1,$2,$i,$(( (end - start) / 1000000 ))" >> "$OUT"
  done
}

measure webpack cold "pnpm exec webpack --mode production"
measure webpack warm "pnpm exec webpack --mode production"   # 第二组前不清缓存才是热跑
measure rspack  cold "pnpm exec rspack build --mode production"
# 产物体积口径（非时间）：
for f in "$REPO_SNAPSHOT"/dist/*.js; do
  gzip -c "$f" | wc -c >> bench-results/sizes.txt
done
# 汇总：中位数 + p95，禁用均值单一口径；报告必须附配置 diff 说明
```

## 十七章 缓存与增量构建体系（BLD-157 ~ BLD-163）
