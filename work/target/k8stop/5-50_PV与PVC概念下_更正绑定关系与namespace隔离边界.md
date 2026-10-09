---
disableNunjucks: true
title: "Kubernetes 存储: PV 与 PVC 概念（下）—— 更正绑定关系，以及 namespace 隔离边界"
date: 2026-10-10 07:15:00
categories: [Kubernetes, 存储]
tags: [PV, PVC, StorageClass, namespace隔离, claimName, 绑定关系, 勘误]
---

# Kubernetes 存储: PV 与 PVC 概念（下）—— 更正绑定关系，以及 namespace 隔离边界

上一节画的关系图有一处画得不对，这一节专门更正它。更正之后，PV / PVC / Pod 三者的落点关系才真正说得通——这也是面试和排查时最容易讲错的一环。

结论先摆：

1. **PVC 是写在 Pod 里面的**——准确说是写在 Pod 的 `spec.volumes[].persistentVolumeClaim.claimName`，**只写一个 PVC 的名字**；
2. **PVC 需要单独创建**：创建了 PV 之后，还要**再创建一个 PVC**，不是自动就有；
3. **PVC 通过 `storageClassName` 去连某"一类" PV**（比如连到 SSD 类型的 PV），连上之后 PVC 与 PV 就**绑定**在一起了；
4. **Pod 里的 PVC 名字要和创建出来的 PVC 名字对上**，对上就挂进去了；
5. **隔离边界不同**：**PVC 是 namespace 隔离的，PV 不是 namespace 隔离的**。

## 纲要

- 更正点一：PVC 写在 Pod 的 `volumes` 里，只写名字
- 更正点二：PV 创建完还要**单独**创建 PVC
- PVC 如何连到 PV：`storageClassName` 按"类型"匹配
- 名字对上才算挂上：`claimName` 与 PVC 的 `metadata.name`
- **namespace 隔离边界**：PVC 有、PV 没有
- 一张正确的落点关系图

## 更正一：PVC 是写在 Pod 的 volumes 里

上一节的图画得不对。正确的写法是：**在 Pod 的 `spec.volumes[].volume`（即 `volumes` 段）里写 PVC**，而这里写的**只是一个 PVC 的名称**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
  namespace: production
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - name: data          # 与下面 volumes[].name 对应
          mountPath: /data
  volumes:
    - name: data              # 卷名，容器内 mountPath 引用它
      persistentVolumeClaim:
        claimName: pvc-nfs    # ← 只写一个 PVC 的名字，不写 PV 名字
```

关键点：**Pod 从头到尾不出现 PV 的名字**。Pod 只说"我要这个叫 `pvc-nfs` 的 PVC"，剩下的由 K8s 去把 PVC 和 PV 对上。

## 更正二：创建 PV 之后，还要单独创建 PVC

这一点也容易含糊：**我们创建了 PV 之后，需要再创建一个 PVC**——PVC 不会自己冒出来。

```yaml
# ① 管理员先建 PV（连着后端真实存储）
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs-01            # 注意：PV 没有 namespace
spec:
  storageClassName: nfs
  capacity:
    storage: 5Gi
  accessModes: [ReadWriteMany]
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.0.204
    path: /data/nfs
---
# ② 使用方再建 PVC（只声明"我要什么"）
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-nfs              # ← Pod 里 claimName 写的就是它
  namespace: production      # ← PVC 有 namespace
spec:
  storageClassName: nfs      # ← 靠它去"连到某一类 PV"
  accessModes: [ReadWriteMany]
  resources:
    requests:
      storage: 1Gi
```

两者是**先后两步、两个对象**，不是一次创建出来的。

## PVC 怎么连到 PV：靠 storageClassName 按"类型"匹配

PVC 建好之后，**根据它的 `storageClassName`，可能会连到某一类 PV**。比如声明 `storageClassName: ssd`，就会去连 SSD 类型的 PV。

一旦匹配成功（class 一致 + 访问模式一致 + 容量足够），**这个 PVC 和那个 PV 就绑定在一起了**（状态变 `Bound`）。

```text
匹配三条件（缺一 PVC 就一直 Pending）
├── storageClassName 一致
├── accessModes 兼容
└── capacity 足够（PVC 要的 ≤ PV 有的）
```

> 动态存储下这一步由 StorageClass 自动创建 PV，使用方感知不到；静态存储（NFS）下则要管理员先手工把 PV 准备好。

## 名字对上，才算挂上

Pod 里写的 `claimName` 和创建出来的 PVC 的 `metadata.name` **必须是同一个名字**，对上之后 Pod 就挂到这个 PVC 上了。名字写错 → Pod 起不来，报 PVC 找不到。

## namespace 隔离边界：PVC 有，PV 没有

这是本节第二个要点，也是最常考的一条：

| 对象 | 是否 namespace 隔离 | 含义 |
| --- | --- | --- |
| **PVC** | ✅ 是 | `pvc-nfs` 属于某个 namespace，**别的 namespace 看不到也用不了** |
| **PV** | ❌ 否 | 集群级资源，**全集群可见**，任何 namespace 的 PVC 都能去绑定它 |

理解方式：PV 是**资源池**（集群共享的盘），PVC 是**申请单**（挂在某个业务 namespace 下）。一份 PV 被某个 namespace 的 PVC 绑定后，别人就用不了了——但**资源本身不属于任何 namespace**。

## 一张正确的落点关系图

```text
【集群级 · 无 namespace】
    PV: pv-nfs-01                (storageClassName=nfs, RWX, Retain)
     │   nfs.server = 192.168.0.204, path=/data/nfs
     │
     │   按 class + 访问模式 + 容量 匹配 → Bound
     ▼
【production 命名空间 · 有隔离】
    PVC: pvc-nfs                 (storageClassName=nfs, requests 1Gi)
     │
     │   Pod 的 volumes 里只写名字
     ▼
    Pod: app
     └── volumes[].persistentVolumeClaim.claimName = pvc-nfs
          └── containers[].volumeMounts.mountPath = /data
```

## 总结

- **Pod 不认识 PV，只认识 PVC**：`volumes` 里写 `persistentVolumeClaim.claimName`，值就是一个名字；
- **PV 和 PVC 是两个对象、两步创建**，PV 建完还要单独建 PVC；
- **绑定靠 `storageClassName` 匹配**（加上访问模式、容量），不是靠名字硬连；
- **名字必须对上**：Pod 的 `claimName` = PVC 的 `metadata.name`；
- **隔离边界要记牢：PVC 是 namespace 隔离的，PV 不是**——这是本节最容易说反的一条。
