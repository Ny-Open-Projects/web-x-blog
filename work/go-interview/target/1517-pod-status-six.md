# 1517 Pod 状态六件套与查看命令

> 分类：K8s / Pod 基础 | 难度：L1~L2 | 题型：概念题 | 频率：高 | 关键词：**Pending**/**Running**/**Succeeded**/**Failed**/**Unknown**/**kubectl describe**

> 原文锚点：第 1~18 段「pending/containercreating/running/succeed/field/unknown…kubectl get/describe/-o json/yaml」

## 一句话总述
Pod 的 **phase 只有五个**（Pending/Running/Succeeded/Failed/Unknown）+ 一个创建中间态（ContainerCreating，挂在 Pending 下）；`kubectl get` STATUS 列显示的 ImagePullBackOff、CrashLoopBackOff 等是**合成的展示态（reason）**，不是 phase。查看三板斧：`kubectl get pods`（列表）、`kubectl describe pod`（事件与条件详情）、`-o json/yaml`（结构化全量）。

## 面试官视角
- 意图：Pod 是最小部署单元，状态排查是日常——考的是「真排过障」还是背名词。
- 分档：P5 报全状态；P6 说清各状态成因与排查命令；P7 能讲 phase 与 reason 的层级差异、按状态分流的排查树。
- 红旗答案：把 ImagePullBackOff 说成 Pod 的 phase；说 Failed 是「部分容器失败」（全容器终止且至少一个失败才算）。
- 惊艳点：点破「STATUS 列 ≠ phase」——phase 就五个，其余全是 reason/condition；再用 describe 的 Events 讲排查顺序 [经验]。

## 主问答
**Q（面试官原话）：** K8s 中 Pod 的状态有哪些？怎么查看？

**A：**
1. **Pending**：已被 API 接受，尚未在节点上跑起来——等调度、等资源、拉镜像中（ContainerCreating 是此阶段内的展示态）。
2. **Running**：所有容器已创建且至少一个在运行。
3. **Succeeded**：所有容器成功退出且不重启（Job 完成态，终态）。
4. **Failed**：所有容器已终止，且至少一个以非零失败结束（终态）。
5. **Unknown**：状态拿不到，通常是 kubelet 与 apiserver 通信故障。
6. **查看**：`kubectl get pods`（全列表）、`get pod <id>`（单个）、`describe pod <id>`（镜像/存储卷/条件/Events——排障主力）、`-o json|yaml`（结构化输出，脚本友好）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 报一遍 Pod 状态 | 漏 Unknown/终态语义 |
| L2 | Pending 卡住查什么？ | 说不清调度/资源/镜像分流 |
| L3 | STATUS 列的 ImagePullBackOff 是 phase 吗？ | 混淆 phase 与 reason |
| L4 | describe 和 -o yaml 各看什么？ | 不知道 Events 是排障主力 |
| L5 |  Unknown 怎么发生？ | 说不清 kubelet 心跳断连 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| phase 枚举 1.x 稳定 | 无 | 五个 phase 是 API 规范；展示态（reason）随版本增减，答题以 phase 为准 |

## 关键代码
```python
# 用 jsonpath 级数据核对 phase 与展示态的区别（-o json 全量解析）
import json, subprocess

def pods():
    out = subprocess.run(["kubectl", "get", "pods", "-A", "-o", "json"],
                         capture_output=True, text=True).stdout
    return json.loads(out)["items"]

for p in pods():
    name = p["metadata"]["name"]
    phase = p["status"]["phase"]                       # API 真实 phase
    reasons = [c["state"].get("waiting", {}).get("reason", "Running")
               for c in p["status"].get("containerStatuses", [])]  # 展示态来源
    print(f"{name:<42} phase={phase:<9} reason={reasons}")
```

[实测] k3d 集群输出（节选）：`coredns-…-7kph5  phase=Pending  reason=['ImagePullBackOff']`；`demo-pod  phase=Running  reason=['Running']`——**STATUS 列显示 ImagePullBackOff 的 Pod，phase 实为 Pending**，两层级区分实证。

## 总结与追问预判
核心：**先报全状态，再主动点破「phase 五个、STATUS 列是展示态」，排查按 describe Events 走**。追问接创建链路：各状态在四棒接力中的位置见 `1516-pod-creation-flow`、Pending/ImagePullBackOff 分流排查见 `1516-pod-flow-detail.deep`、静态 Pod 生命周期特例见 `1518-static-pod`；集群组件角色见 `1515-k8s-architecture`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 kubectl 音转为「typeCTL」、Failed 音转为「field」、json/yaml 音转为「jason/压某/yeln」、node 音转为「load」，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 原文把 ContainerCreating 与五个 phase 并列为「状态」——它不是独立 phase，而是 Pod 处于 Pending 期间容器尚未启动时的展示态（reason）[实测]。
3. 事实核校： [经验] 原文「succeed 表示所有容器成功结束且不会被重启」正确补充限定——它要求**所有容器**终止；Running 只要求至少一个运行中即可。
