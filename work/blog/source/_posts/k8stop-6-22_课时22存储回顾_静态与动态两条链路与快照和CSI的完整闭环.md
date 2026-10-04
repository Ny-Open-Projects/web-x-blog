---
disableNunjucks: true
title: "Kubernetes 集群部署: 存储回顾（静态与动态两条链路、快照的完整闭环，以及为什么 CSI 会成为主流）"
date: 2026-10-03 23:28:00
categories: [k8stop, Kubernetes, 存储]
tags: [静态存储, 动态存储, StorageClass, PVC, VolumeSnapshot, CSI, FlexVolume, in-tree, 回顾]
---

# Kubernetes 集群部署: 存储回顾（静态与动态两条链路、快照的完整闭环，以及为什么 CSI 会成为主流）

存储这一块比较杂，这一節把它串成一条线：**静态存储与动态存储两条链路各自的走法**、**快照在整条链路上处在哪一环**，以及**为什么 CSI 会成为未来最主流的存储方式**。

结论先摆：

1. **存储分两类**：**静态存储** = 管理员手动建 PV、建 PVC，再挂到 Deployment / StatefulSet 上；**动态存储** = 靠 StorageClass 自动生成；
2. **生产环境建议后端存储放在集群之外**，不要放在 K8s 集群内部；
3. **Pod 的 volume 可以直连后端存储**（GFS / NFS 都行），但**灵活性不高、配置不简单，实际用得不多**；主流的写法是 **volume → PVC →（StorageClass）→ PV**；
4. **没有 StorageClass 就得手动建 PV** —— 这就是静态与动态的分水岭；
5. **快照的设计理念和 StorageClass 完全一样**：`VolumeSnapshotClass` 是模板、`VolumeSnapshot` 是请求，后端存储对 PVC 绑定的那个 PV 打备份；
6. **恢复时新建 PVC 并在 `dataSource` 里指定快照名**，后端根据快照重建一份 PV；
7. **CSI 会成为主流**：以前那种「PVC/PV 直连后端」是 **in-tree** 方式，K8s 开发者得为每一种存储都写一遍连接代码；**FlexVolume 要每台宿主机装插件，太复杂**；**CSI 由存储厂商自己维护**，K8s 只需对接 CSI。

## 纲要

- 两大类：静态存储与动态存储
- 后端存储该放哪：生产建议放集群之外
- 链路一：动态存储怎么走通
- 链路二：静态存储怎么走通
- volume 直连后端存储：能行但不好用
- 两者的分水岭：有没有 StorageClass
- 快照：设计理念与 StorageClass 一致
- 打快照这一步发生了什么
- 恢复：dataSource 指向快照
- CSI 为什么是趋势
- in-tree 方式的痛点
- FlexVolume 的痛点
- 一张完整的链路图

## 两大类：静态存储与动态存储

```mermaid
flowchart TD
    A["K8s 存储的两大类"] --> B1["**静态存储**"]
    A --> B2["**动态存储**（Rook/Ceph 就是这类）"]
    B1 --> C1["管理员**手动**创建 PV"]
    C1 --> D1["再创建 PVC"]
    D1 --> E1["把 PVC 挂到资源文件上（Deployment / StatefulSet）"]
    B2 --> C2["**StorageClass** 自动生成 PV"]
    style B2 fill:#e6ffe6
```

| 类别 | 谁来创建 PV | 典型后端 |
| --- | --- | --- |
| 静态存储 | **管理员手动** | NFS 等 |
| **动态存储** | **StorageClass + 底层驱动自动创建** | **Rook/Ceph（云原生存储）** |

> 作者对 Rook 的评价：**「Rook 这个东西，对我们管理员来讲，就是把存储封装得比较好，用起来也比较简单」**。

## 后端存储该放哪：生产建议放集群之外

```mermaid
flowchart TD
    A["后端存储的位置"] --> B1["放在 **K8s 集群之内**（演示这么做）"]
    A --> B2["放在 **集群之外**"]
    B2 --> C["**生产环境建议这么做**"]
    style C fill:#e6ffe6
```

> 后端存储可以是 Ceph、GlusterFS、NFS，或者其它各种形态 —— 但**在生产环境，建议这个存储不要放在集群之内**。

## 链路一：动态存储怎么走通

```mermaid
flowchart TD
    A["namespace 内创建一个 PVC"] --> B["PVC 里写 **storageClassName**"]
    B --> C["SC 绑定着后端存储"]
    C --> D["SC 向后端存储**申请一块 PV**"]
    D --> E["PV 与 PVC **绑定**"]
    E --> F["Deployment 的 **volume 写上这个 PVC 的名字**"]
    F --> G["容器就能读写这块存储了"]
    style G fill:#e6ffe6
```

```text
动态存储链路:

Deployment.spec.template.spec.volumes
   └── persistentVolumeClaim.claimName: <PVC 名>
             │
             ▼
          PVC  ← storageClassName
             │
             ▼
       StorageClass  ← 绑定后端存储
             │
             ▼
          PV（**自动创建**）
```

## 链路二：静态存储怎么走通

```mermaid
flowchart TD
    A["没有 StorageClass"] --> B["**管理员手动创建 PV**"]
    B --> C["PV 连接到后端存储"]
    C --> D["再创建 PVC, PVC 写这个 PV 的 storageClassName"]
    D --> E["PVC 与 PV **绑定**"]
    E --> F["Deployment 的 volume 写 PVC 的名字"]
    style B fill:#fff6e6
```

```text
静态存储链路:

管理员手动建 PV（连到后端存储）
        │
        ▼
      PVC（写 PV 对应的 storageClassName）
        │
        ▼
   两者绑定
        │
        ▼
Deployment volume 引用 PVC
```

## volume 直连后端存储：能行但不好用

```mermaid
flowchart TD
    A["volume 模式"] --> B1["**直连后端存储**（GFS / NFS 等）"]
    A --> B2["经过 PVC（主流）"]
    B1 --> C1["**可以, 但灵活性不高**"]
    C1 --> C2["有些配置也不简单"]
    C2 --> D["连个 NFS 还行, 连别的就不太灵活 → **实际用得不多**"]
    style D fill:#ffe6e6
    style B2 fill:#e6ffe6
```

> 课程原话：**「这种其实用的不是很多，你连个 NFS 其实是可以的，但是你连其他的可能不是很灵活，我们一般都不是这么写」**。

## 两者的分水岭：有没有 StorageClass

```mermaid
flowchart TD
    A{"集群里有 StorageClass 吗?"}
    A -->|"有"| B["**动态**: PVC 写 SC 名 → 自动出 PV"]
    A -->|"没有"| C["**静态**: 手动建 PV → PVC 与之绑定"]
    style B fill:#e6ffe6
```

| 条件 | 结果 |
| --- | --- |
| **有 StorageClass** | PVC 通过它自动申请 PV（动态） |
| **没有 StorageClass** | 必须手动建 PV（静态） |

> 一句话总结两者的区别：**「如果没有 storageClass，就需要自己手动去创建一个 PV」**。

## 快照：设计理念与 StorageClass 一致

```mermaid
flowchart TD
    A["**VolumeSnapshotClass**"] --> B["相当于 StorageClass 的角色"]
    B --> C["一个**模板**"]
    C --> D["我们创建 VolumeSnapshot = 发一个**快照请求**"]
    D --> E["请求通过 VolumeSnapshotClass 发给后端存储"]
    style B fill:#e6ffe6
```

| 概念 | 类比 |
| --- | --- |
| `VolumeSnapshotClass` | 相当于 `StorageClass`（模板） |
| `VolumeSnapshot` | 相当于 `PVC`（请求） |
| 实际的快照数据 | 相当于 `PV`（底层实体） |

## 打快照这一步发生了什么

```mermaid
flowchart TD
    A["VolumeSnapshot 里写明: 对**哪个 PVC** 打快照"] --> B["通过 VolumeSnapshotClass 请求后端存储"]
    B --> C["后端存储找到该 PVC 绑定的 **PV**"]
    C --> D["**对这个 PV 里的数据做一份备份**"]
    D --> E["这就是快照"]
    style D fill:#e6ffe6
```

> 课程表述：**「他通过这个 snapshotClass 去对这个后端存储发了一个请求，告诉后端存储我要对某个 PVC 进行一次快照……也就是说他对这个 PV 里面的数据进行了一个备份」**。

在 **Ceph 的 dashboard** 里也能直接看到这些快照对象。

## 恢复：dataSource 指向快照

```mermaid
flowchart TD
    A["新建一个 PVC"] --> B["dataSource 指定**快照的名字**"]
    B --> C["通过快照找到它对应的 PVC / PV"]
    C --> D["后端存储**重建一份 PV**, 数据照快照恢复"]
    D --> E["这个新 PVC 挂上就能看到快照时刻的数据"]
    style D fill:#e6ffe6
```

```text
恢复链路:

新 PVC（dataSource: VolumeSnapshot）
    │
    ▼
快照 → 找到当时的 PVC → 找到当时的 PV
    │
    ▼
重建一个 PV（数据是快照里那份）
```

## CSI 为什么是趋势

```mermaid
flowchart TD
    A["K8s 里的存储接口演进"] --> B1["**in-tree**（PVC/PV 直连后端）"]
    A --> B2["**FlexVolume**"]
    A --> B3["**CSI**"]
    B1 --> C1["K8s 开发者要自己为**每一种**后端存储写连接代码"]
    B2 --> C2["**比较复杂**: 每个宿主机都要装插件"]
    B3 --> C3["**由存储厂商 / 维护者提供驱动**, K8s 只对接 CSI"]
    C3 --> D["⇒ **CSI 将会是未来最主流的存储方式**"]
    style D fill:#e6ffe6
```

| 方式 | 谁写驱动 | 部署负担 | 评价 |
| --- | --- | --- | --- |
| **in-tree** | **K8s 开发者** | 随 K8s 走 | 每加一种存储就要改 K8s 本体 |
| FlexVolume | 第三方 | **每台宿主机都要装插件** | 复杂 |
| **CSI** | **存储官方 / 维护者** | 集群内部署即可 | **主流方向** |

> 课程原话：**「像这种 PVC 或者是 PV 直连的话，在 K8s 里面被称为一种 in-tree 的开发方式，就是 K8s 的管理者、K8s 开发者必须要自己去手动实现连接每一个后端存储的代码……为了减少 K8s 开发者的工作量，他们提出了很多概念，PVC 是一种，CSI 又是一种，还有一个 FlexVolume 也是一种，但是 FlexVolume 比较复杂，它需要安装插件，每个宿主机都要安装；CSI 是由存储的官方去提供一个 CSI，或者其他的维护者提供一个 CSI」**。

## in-tree 方式的痛点

```mermaid
flowchart TD
    A["后端存储的类型有很多"] --> B["每一种都要在 K8s 里实现一遍连接代码"]
    B --> C["K8s 开发者工作量巨大"]
    C --> D["新增存储类型要等 K8s 本体支持"]
    style D fill:#ffe6e6
```

## FlexVolume 的痛点

```mermaid
flowchart TD
    A["FlexVolume"] --> B["需要安装**插件**"]
    B --> C["**每个宿主机都要安装**"]
    C --> D["运维成本高 → 用起来复杂"]
    style D fill:#ffe6e6
```

## 一张完整的链路图

```text
静态 vs 动态 vs 快照 —— 完整关系:

【动态存储】
Deployment volume
└── PVC（storageClassName: xxx）
    └── StorageClass
        └── 后端存储 → **自动生成 PV**

【静态存储】
Deployment volume
└── PVC
    └── **管理员手动创建的 PV** → 后端存储

【快照】
PVC ──打快照──> VolumeSnapshot（通过 VolumeSnapshotClass）
   │                  │
   │                  └── 后端存储对 PV 数据做备份
   │
新建 PVC（dataSource: 快照名）──> 重建 PV（数据来自快照）

【接口层】
PVC / PV ──> **CSI**（由存储厂商提供）──> 后端存储
```

## API 速览

| 能力 | 做法 | 关键点 |
| --- | --- | --- |
| 看有哪些 SC | `kubectl get sc` | 集群级，无 ns |
| 看 PVC 绑定了哪个 PV | `kubectl get pvc -o jsonpath='{.spec.volumeName}'` | — |
| 看 PV 属于哪个 SC | `kubectl get pv -o yaml` | 看 `storageClassName` |
| 看快照 class | `kubectl get volumesnapshotclass` | 与 SC 同设计 |
| 看快照 | `kubectl get volumesnapshot -n <NS>` | namespace 级 |
| 从快照恢复 | 新 PVC 写 `dataSource` | 容量 ≥ 快照 |
| 看 CSI 驱动 | `kubectl get csidrivers` / `kubectl get csinodes` | CSI 时代的排查入口 |
| Ceph 侧观察 | dashboard 或 toolbox | 看池 / image / 快照 |

字段速查：

| 字段 | 作用 |
| --- | --- |
| `PVC.spec.storageClassName` | 指向哪个 SC（**为空就是静态路线**） |
| `PV.spec.storageClassName` | 手动建的 PV 也要写，供 PVC 匹配 |
| `Pod.spec.volumes[].persistentVolumeClaim.claimName` | Pod 侧引用 PVC |
| `VolumeSnapshot.spec.source.name` | 对哪个 PVC 打快照 |
| `PVC.spec.dataSource` | 从哪个快照恢复 |
| `VolumeSnapshotClass.snapshotter` | 由哪个 CSI 处理快照 |

## Demo 示例

```bash
# 1. 看集群里有哪些 StorageClass（有没有它决定走动态还是静态）
kubectl get sc

# 2. 走动态路线: 建 PVC 并看它自动绑定了哪个 PV
NS=default
kubectl apply -f pvc-dynamic.yaml -n "$NS"
kubectl get pvc -n "$NS"
kubectl get pvc -n "$NS" -o jsonpath='{.items[0].spec.volumeName}'; echo
kubectl get pv

# 3. 走静态路线: 手动建 PV, 再让 PVC 与之绑定
kubectl apply -f pv-static.yaml
kubectl apply -f pvc-static.yaml -n "$NS"
kubectl get pvc -n "$NS"

# 4. 快照与恢复
kubectl get volumesnapshotclass
kubectl apply -f snapshot.yaml -n "$NS"
kubectl get volumesnapshot -n "$NS"
kubectl apply -f pvc-restore.yaml -n "$NS"
kubectl get pvc,pv -n "$NS"

# 5. 看 CSI 相关对象（CSI 时代的必备排查项）
kubectl get csidrivers
kubectl get csinodes

# 6. 在 Deployment 里引用 PVC
#    volumes[].persistentVolumeClaim.claimName
```

```yaml
# pvc-dynamic.yaml —— 动态路线：指定 SC，PV 自动来
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-dynamic
  namespace: default
spec:
  storageClassName: rook-ceph-block
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

```yaml
# pv-static.yaml —— 静态路线：管理员手动建 PV
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-static
spec:
  storageClassName: manual
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.1.100
    path: /data/nfs
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-static
  namespace: default
spec:
  storageClassName: manual        # ← 与 PV 的 storageClassName 对应
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

```text
存储演进的一张表:

方式          驱动谁维护              部署负担          现状
──────────────────────────────────────────────────────────
in-tree       K8s 开发者              随 K8s 发布       逐渐被替代
FlexVolume    第三方                  **每台机器装插件**  复杂, 少用
**CSI**       **存储厂商/维护者**      集群内即可         **未来主流**
```

### 总结

- **存储分静态与动态两类**：静态是**管理员手动建 PV + PVC 再挂到 Deployment / StatefulSet**，动态是**靠 StorageClass 自动生成 PV**（Rook/Ceph 就是这套，作者评价它「封装得比较好、用起来简单」）；
- **生产环境建议后端存储放在集群之外**；**volume 虽然能直连后端存储（NFS 可以），但灵活性不高、配置不简单，实际用得不多**，主流写法是 **volume → PVC →（StorageClass）→ PV**；
- **两者的分水岭就是有没有 StorageClass** —— 有就走动态（PVC 写 `storageClassName` 自动出 PV），没有就只能手动建 PV 再让 PVC 与之绑定；
- **快照的设计理念和 StorageClass 如出一辙**：`VolumeSnapshotClass` 是模板、`VolumeSnapshot` 是请求，**后端存储会对该 PVC 绑定的 PV 里的数据做一份备份**（Ceph dashboard 里能直接看到）；
- **恢复的做法是新建一个 PVC 并在 `dataSource` 里指定快照名**，后端据此重建一份 PV，数据照快照恢复；
- **CSI 会成为未来最主流的存储方式**：in-tree 要求 K8s 开发者为每种后端存储都写一遍连接代码，**FlexVolume 要在每台宿主机上装插件太复杂**，而 **CSI 由存储厂商自己维护驱动**，K8s 只需对接 CSI —— 存储这一章也就此告一段落，接下来是中间件与工具。

