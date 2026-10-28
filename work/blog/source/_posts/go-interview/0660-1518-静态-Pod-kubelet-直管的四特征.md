---
disableNunjucks: true
title: "1518 静态 Pod：kubelet 直管的四特征"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：K8s / Pod 进阶 | 难度：L1~L2 | 题型：概念题 | 频率：中 | 关键词：**静态 Pod**/**kubelet**/**manifests 目录**/**节点绑定**/**mirror pod**

> 原文锚点：第 1~19 段「不由 apiserver 管理…kubelet 监视静态文件…绑定节点不调度…删除原地复活…四大用途」

## 一句话总述
静态 Pod = 由节点上的 **kubelet 直接监视 manifest 文件目录**创建并管理的 Pod，**不经过 apiserver 创建流程、不参与调度**，永远绑死所在节点。三句口诀：**文件生、节点死、删不掉**——配置文件在就反复复活，删文件才真死。典型用途是 kubeadm 用它拉起 etcd/apiserver 等控制面组件。

## 面试官视角
- 意图：是否理解 Pod 创建有「apiserver 派发」之外的第二条路，以及自举（bootstrap）问题——控制面自己怎么跑起来。
- 分档：P5 知定义与 kubelet 管理；P6 说清四特征（无调度/仅查询/原地复活/节点绑定）与用途；P7 能讲 kubeadm 自举、mirror pod 机制、静态 Pod vs 普通 Pod 自愈差异。
- 红旗答案：以为 kubectl delete 能删掉静态 Pod；以为静态 Pod 可被 scheduler 调度到别的节点。
- 惊艳点：能报出 manifest 目录路径（标准 `/etc/kubernetes/manifests`）+ 静态 Pod 命名规则 `<名>-<节点名>` + 「删 manifest 才是真删」 [经验]。

## 主问答
**Q（面试官原话）：** K8s 中什么是静态 Pod？

**A：**
1. **定义**：kubelet 直接监视节点上的 manifest 目录（标准为 `/etc/kubernetes/manifests`），发现 YAML 就在本节点拉起 Pod——**不经 apiserver 创建、不经 scheduler 调度**；apiserver 侧只能查询，不能通过 API 更新删除。
2. **四特征**：① 绑定节点，永不漂移；② 生命周期全归 kubelet；③ 删不掉——kubectl delete 后立即原地复活；④ 自愈在原节点，普通 Pod 被删则由控制器**换节点**重建。
3. **真删方式**：删除/移走 manifest 文件，Pod 随之消失——「文件生、节点死、删不掉」。
4. **四大用途**：① 控制面自举（kubeadm 拉起 etcd/apiserver/controller-manager，天然防误删）；② 基础设施服务（日志/监控代理，不等 apiserver 就绪）；③ 独立应用；④ 节点级系统进程。
5. **识别**：静态 Pod 名自动带节点后缀（`<名>-<节点名>`）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 什么是静态 Pod？ | 说不清 kubelet 直管 |
| L2 | 和普通 Pod 创建路径差异？ | 讲不出绕过 apiserver 创建 |
| L3 | 怎么删掉一个静态 Pod？ | 答不出删 manifest |
| L4 | 控制面组件怎么部署的？ | 不知道 kubeadm 静态 Pod 自举 |
| L5 | mirror pod 是什么？ | 说不出 apiserver 侧镜像对象 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| kubelet 静态 Pod 机制 | 无（1.x 全系稳定） | manifest 目录路径各发行版可配置（kubeadm 默认 /etc/kubernetes/manifests，k3s 为 /var/lib/rancher/k3s/agent/pod-manifests） |

## 关键代码
[实测] k3d（k3s）集群四步：① 把 Pod manifest 放入 `/var/lib/rancher/k3s/agent/pod-manifests/` → kubelet 约 10s 自动拉起（无需 kubectl create）；② Pod 名自动改写为 `wave-static-k3d-wave158-server-0`（`<名>-<节点名>`），Running 1/1、nodeName 固定本节点；③ `kubectl delete --wait=false` → 约 8s 后原地复活（Pending 重启）；④ 删除 manifest 文件 → `NotFound`，真死。k3s 侧 mirror pod 的 ownerReferences 指向 Node（kind=Node, controller=true）。

```python
# 静态 Pod 识别器：按 <名>-<节点名> 命名规则从 API 视角找 mirror pod
import json, subprocess

def kjson(*args):
    return json.loads(subprocess.run(
        ["kubectl", *args, "-o", "json"], capture_output=True, text=True).stdout)

nodes = {n["metadata"]["name"] for n in kjson("get", "nodes")["items"]}

for p in kjson("get", "pods", "-A")["items"]:
    name = p["metadata"]["name"]
    for node in nodes:
        if name.endswith("-" + node):          # 名字以 -<节点名> 结尾 → 静态 Pod
            print(f"static? {p['metadata']['namespace']}/{name} node={node}")
            break
```

[实测] 输出：`static? default/wave-static-k3d-wave158-server-0 node=k3d-wave158-server-0`。

## 总结与追问预判
核心：**「文件生、节点死、删不掉」九字答定义，四特征收尾，kubeadm 自举是加分题**。追问常接普通 Pod 创建链路对比见 1516 与排查分流 `1516-pod-flow-detail.deep`；集群架构中 kubelet 角色见 1515；误删防护与升级场景可引 `1515-k8s-advantages`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 kubelet 音转为多个崩坏串、K8s 音转为「k 八 s」、Pending 音转为「喷景」，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 原文「静态 Pod 的自愈可能会在一个新的节点上创建副本，而静态 Pod 在原节点原地复活」措辞混乱——「换节点重建」说的是**普通 Pod**（控制器在新节点拉起新副本）；静态 Pod 永远原节点原地重启，二者对比正是考点。
3. 事实核校： [经验] 原文「只能通过 K8s 的 API 进行查询」正确补充——apiserver 侧存在 mirror pod 只读镜像，对其的更新/删除请求不影响真实生命周期。
