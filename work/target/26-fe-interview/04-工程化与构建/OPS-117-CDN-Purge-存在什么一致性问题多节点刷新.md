---
title: [OPS-117] CDN Purge 存在什么一致性问题？多节点刷新延迟怎么应对？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-117：CDN Purge 存在什么一致性问题？多节点刷新延迟怎么应对？
**答**：
- 刷新不是原子操作：请求要下发到多边缘节点、多层级（L1 边缘→L2 中间层→源），存在分钟级不一致窗口，部分节点新部分旧。
- 刷新任务化并轮询状态到 Complete，而不是 fire-and-forget；批量刷新分段提交便于跟踪。
- 架构上规避不一致：发布用"版本目录 + 入口切换"（OPS-005/140），真正需要刷的只有入口文件，且入口本身短 TTL，刷新失败影响也小。
- 刷新后多地拨测验证内容版本指纹；把"刷新完成"作为放量前置条件写进发布流水线。
- 全量刷新（Purge everything）视为高危操作：权限收紧、二次确认，且优先用基于目录/URL 的精确刷新。

```bash
# Purge 任务化跟踪与多地验证
# 1. 待刷 URL 列表（入口文件优先，杜绝全量刷新）
FILE=urls_$(date +%Y%m%d_%H%M).txt
echo "https://www.example.com/index.html" > "$FILE"

# 2. 提交刷新任务并记录 ID（阿里云示例）
aliyun cdn RefreshObjectCaches --ObjectPath "$(paste -sd, "$FILE")" --ObjectType File > refresh_job.json
TASK_ID=$(jq -r '.RefreshTaskId' refresh_job.json)
echo "refresh task: $TASK_ID"

# 3. 轮询到全部节点 Complete（多边缘逐级收敛需要时间）
while :; do
  if aliyun cdn DescribeRefreshTasks --TaskId "$TASK_ID" \
     | jq -e 'any(.Tasks.CDNTask[]; .Status != "Complete")' > /dev/null; then
    sleep 10
  else
    echo "refresh complete"; break
  fi
done

# 4. 多地拨测验证版本指纹一致（发布平台把本步作为放量前置条件）
for probe in beijing shanghai guangzhou; do
  curl -s -H "X-Probe: $probe" "https://www.example.com/index.html" \
    | grep -o 'window.__BUILD__ = "[^"]*"'
done
```
