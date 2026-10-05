# Go PaaS 平台开发: K8s 通过 CSI 方式添加外部 Ceph 系统（上）

## 纲要

- 为何选择 CSI 模式：官方推荐、稳定，取代老旧的 in-tree 方式
- 在 Ceph 中创建专用 pool 与用户，并初始化 RBD
- 部署 ceph-csi（v3.6.2）前的集群信息准备：fsid 与 monitor 地址
- 创建 ConfigMap（ceph-csi-config / ceph-config / encryption-kms-config）与 Secret（csi-rbd-secret）
- 配置 RBAC 与 PodSecurityPolicy

## 为什么用 CSI

把已安装好的 Ceph 集群接入 K8s，用于为平台中的应用动态提供云盘。当前官方推荐且最稳定的方式是 **CSI（Container Storage Interface）**，旧的直接对接方式已不再使用。CSI 模式支持按需动态创建存储卷，这正是 Go PaaS 平台自动化管理存储所需要的。

## 在 Ceph 侧创建 pool 与用户

登录 Ceph 集群的 master 节点，创建一个专供 K8s 使用的 pool 与用户：

```bash
# 创建 pool（PG 与 PGP 均为 16）
ceph osd pool create kubernetes 16 16

# 创建 client.kubernetes 用户并授权 rbd 相关 profile
ceph auth get-or-create client.kubernetes \
  mon 'profile rbd' \
  osd 'profile rbd pool=kubernetes' \
  mgr 'profile rbd pool=kubernetes'

# 初始化该 pool 的 RBD 元信息
rbd pool init kubernetes

# 查看 pool 是否创建成功
ceph osd pool ls
rados lspools
```

执行后会输出该用户的 key，例如：

```text
[client.kubernetes]
        key = AQC2Q/ZiecM/MBAA2nwfDPKgfReHxz/o4kQV3A==
```

这个 key 在后续创建 Secret 时会用到。若遗忘，可随时获取：

```bash
ceph auth get client.kubernetes
```

## 准备 Ceph 集群信息

在 K8s master 上部署 ceph-csi 前，先记录集群的 `fsid`（cluster ID）与 monitor 地址：

```bash
ceph mon dump
```

典型输出：

```text
fsid c32ff766-19f6-11ed-aa17-00163e005933
min_mon_release 16 (pacific)
0: [v2:172.31.96.70:3300/0,v1:172.31.96.70:6789/0] mon.ceph01
1: [v2:172.31.96.71:3300/0,v1:172.31.96.71:6789/0] mon.ceph02
2: [v2:172.31.96.72:3300/0,v1:172.31.96.72:6789/0] mon.ceph03
```

注意两点：

- **fsid**：即 Ceph 集群 ID，后续 ConfigMap 与 StorageClass 都会引用。
- **monitor 地址**：目前 ceph-csi 仅支持 **v1** 协议，因此只能取 `v1` 的 IP 与端口（如 `172.31.96.70:6789`）。

## 拉取 ceph-csi 并创建 ConfigMap

在 K8s master 节点上拉取指定 release 分支（v3.6.2）：

```bash
git clone --depth 1 --branch v3.6.2 https://github.com/ceph/ceph-csi
cd ceph-csi/deploy/rbd/kubernetes
ls -l ./
```

该目录下包含：`csi-config-map.yaml`、`csidriver.yaml`、`csi-nodeplugin-psp.yaml`、`csi-nodeplugin-rbac.yaml`、`csi-provisioner-psp.yaml`、`csi-provisioner-rbac.yaml`、`csi-rbdplugin-provisioner.yaml`、`csi-rbdplugin.yaml`。

### ceph-csi-config

将前面获取的 fsid 与 monitor 地址写入 `csi-config-map.yaml`：

```yaml
apiVersion: v1
kind: ConfigMap
data:
  config.json: |-
    [
      {
        "clusterID": "c32ff766-19f6-11ed-aa17-00163e005933",
        "monitors": [
          "172.31.96.70:6789",
          "172.31.96.71:6789",
          "172.31.96.72:6789"
        ]
      }
    ]
metadata:
  name: ceph-csi-config
```

部署到集群：

```bash
kubectl apply -f csi-config-map.yaml
```

### ceph-config 与 encryption-kms-config

创建 ceph-config（注意 keyring 必须为空值）：

```bash
cat <<EOF > ceph-config-map.yaml
---
apiVersion: v1
kind: ConfigMap
data:
  ceph.conf: |
    [global]
    auth_cluster_required = cephx
    auth_service_required = cephx
    auth_client_required = cephx
  # keyring is a required key and its value should be empty
  keyring: |
metadata:
  name: ceph-config
EOF
kubectl apply -f ceph-config-map.yaml
```

创建 encryption-kms-config（默认值 `{}`）：

```bash
cat <<EOF > csi-kms-config-map.yaml
---
apiVersion: v1
kind: ConfigMap
data:
  config.json: |-
    {}
metadata:
  name: ceph-csi-encryption-kms-config
EOF
kubectl apply -f csi-kms-config-map.yaml
```

## 创建 Secret

使用前面创建的 `client.kubernetes` 用户与 key 生成 Secret，**注意 `userID` 与 `userKey` 的值需替换为自己的集群信息**：

```bash
cat <<EOF > csi-rbd-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: csi-rbd-secret
  namespace: default
stringData:
  userID: kubernetes
  userKey: AQC2Q/ZiecM/MBAA2nwfDPKgfReHxz/o4kQV3A==
EOF
kubectl apply -f csi-rbd-secret.yaml
```

## RBAC 与 PodSecurityPolicy

创建所需的 ServiceAccount 与 RBAC 资源，以及 PodSecurityPolicy：

```bash
kubectl create -f csi-provisioner-rbac.yaml
kubectl create -f csi-nodeplugin-rbac.yaml
kubectl create -f csi-provisioner-psp.yaml
kubectl create -f csi-nodeplugin-psp.yaml
```

## 编辑部署清单（资源受限时的调优）

在 OSD 较少、节点较少的资源受限环境下，需要对 `csi-rbdplugin-provisioner.yaml` 与 `csi-rbdplugin.yaml` 做两处调整：

1. **注释掉 kms 配置**：将 `ceph-csi-encryption-kms-config` 相关的 volumeMount 与 configMap 引用注释掉（否则未创建对应配置会报错）。
2. **注释掉亲和性 / 改为单副本**：默认 `affinity.podAntiAffinity` 要求多节点分散，节点不足时 Pod 无法调度；同时把 `replicas` 由 3 改为 1。

示例（在 `csi-rbdplugin-provisioner.yaml` 中）：

```yaml
#      affinity:
#        podAntiAffinity:
#          requiredDuringSchedulingIgnoredDuringExecution:
#            - labelSelector:
#                matchExpressions:
#                  - key: app
#                    operator: In
#                    values:
#                      - csi-rbdplugin-provisioner
#              topologyKey: "kubernetes.io/hostname"
spec:
  replicas: 1
```

下一节将正式部署 CSI sidecar 与 RBD driver，并创建 StorageClass 与 PVC 完成验证。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/ceph/2.k8s 使用 CSI 添加 ceph 为存储.md`
- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：94%。是否需要继续：[是]。代码是否可运行：[是]。
