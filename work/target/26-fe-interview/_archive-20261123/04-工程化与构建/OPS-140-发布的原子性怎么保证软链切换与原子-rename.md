---
title: [OPS-140] 发布的原子性怎么保证？软链切换与原子 rename 各用在哪？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-140：发布的原子性怎么保证？软链切换与原子 rename 各用在哪？
**答**：
- 目标：切换瞬间所有用户要么看到旧版本要么看到新版本，不存在半新半旧的中间态。
- 目录软链：ln -sfn 一步完成 current 指向切换，读侧原子感知；配合 nginx open_file_cache 注意元数据缓存（OPS-102），切换后 reload 或缩短 valid。
- 单文件原子写：写入临时文件后 mv（同分区 rename 是原子的），用于入口清单、灰度规则等 JSON 配置。
- 覆盖式发布（rsync/cp 直接写 current）是事故温床：中间态窗口 + 失败难以回退，必须禁止。
- 切换后冒烟校验内容指纹，失败立即软链回退——回滚成本是"一条命令"。

```bash
# 发布原子性：软链切换 + 原子 rename
RELEASES=/data/web/releases
NEW=$RELEASES/1.42.0
OLD=$(readlink /data/web/current)          # 记录当前版本，供冒烟失败快速回退

# 1. 前置校验：新版本目录完整就位（产物校验 + 冒烟标记文件）
[ -f "$NEW/index.html" ] && [ -f "$NEW/.release-ok" ] \
  || { echo "artifact incomplete" >&2; exit 1; }

# 2. 原子切换：ln -sfn 一步改指向，读侧只会看到旧或新，无中间态
ln -sfn "$NEW" /data/web/current
nginx -s reload                             # 使 open_file_cache 的 stat 缓存失效（OPS-102）

# 3. 禁止覆盖式发布：rsync/cp 直接写 current 存在半新半旧窗口，且失败难回退

# 4. 单文件配置用原子 rename：写临时文件后 mv（同分区 rename 原子）
#    echo '{}' > gray-rule.json.tmp && mv gray-rule.json.tmp gray-rule.json

# 5. 切换后冒烟，失败秒级回退
curl -fsS https://www.example.com/ | grep -q '__BUILD_VERSION__' \
  || { echo "smoke failed, rollback"; ln -sfn "$OLD" /data/web/current; nginx -s reload; exit 1; }
```
