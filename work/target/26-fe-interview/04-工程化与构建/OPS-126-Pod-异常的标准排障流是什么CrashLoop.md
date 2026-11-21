---
title: [OPS-126] Pod 异常的标准排障流是什么？CrashLoopBackOff/ImagePullBackOff 各查什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-126：Pod 异常的标准排障流是什么？CrashLoopBackOff/ImagePullBackOff 各查什么？
**答**：
- 先看全景分类：Pending（调度不上：资源/亲和性/PVC）、ImagePullBackOff（镜像不存在/凭证错）、CrashLoopBackOff（启动即崩）、Running 但不就绪（探针/依赖）。
- describe 看 Events 能解决 80% 问题；CrashLoopBackOff 必须 kubectl logs -p 看上一次崩溃日志。
- OOMKilled 看 lastState.terminated.exitCode=137；CPU throttle 表现为延迟高但不崩，用 top pod 与 throttling 指标查。
- exec 进容器验证 DNS/网络/本地端口，区分"进程内问题"与"网络问题"。
- 排障的最后兜底永远是 rollout undo/回滚（OPS-140），先恢复再细查。

```bash
# Pod 排障标准流
NS=web-prod; APP=web-frontend
POD=$(kubectl get pod -n $NS -l app=$APP -o name | head -1 | cut -d/ -f2)

# 1. 全景分类：状态一眼定位方向
kubectl get pods -n $NS -l app=$APP -o wide

# 2. Events 先行：调度失败/镜像拉取失败/探针失败都写在 Events 里
kubectl describe pod -n $NS -l app=$APP | sed -n '/Events:/,$p'

# 3. 日志：当前 + 上一次崩溃（CrashLoopBackOff 关键是 -p）
kubectl logs -n $NS -l app=$APP --tail=100 --prefix
kubectl logs -n $NS $POD -p --tail=50

# 4. 终止原因：137 = OOMKilled
kubectl get pod $POD -n $NS \
  -o jsonpath='{.status.containerStatuses[0].lastState.terminated}'; echo

# 5. 容器内验证网络/DNS/本地端口
kubectl exec -it -n $NS $POD -- sh -c \
  'wget -qO- localhost:3000/healthz; nslookup web-stable-svc; exit'

# 6. 资源水位与回滚兜底
kubectl top pod -n $NS --sort-by=memory
kubectl rollout history deploy/$APP -n $NS
kubectl rollout undo deploy/$APP -n $NS --to-revision=41
kubectl rollout status deploy/$APP -n $NS --timeout=120s
```

---

## 十四、可观测性深入（OPS-127 ~ OPS-136）

第八章解决"有监控告警"，本章解决"看得全、追得到、算得准"：三大支柱全景、OpenTelemetry 接入、traceId 全链路、错误聚类、会话回放、采样、SLO/错误预算、容量、压测与报告自动化。
