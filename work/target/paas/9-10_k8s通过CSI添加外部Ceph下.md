# Go PaaS 平台开发: K8s 通过 CSI 方式添加外部 Ceph 系统（下）

## 纲要

- 部署 CSI sidecar（csi-rbdplugin-provisioner，含 6 个 sidecar 容器）与 RBD CSI driver
- 创建 StorageClass（provisioner 指向 `rbd.csi.ceph.com`），关键参数说明
- 验证：创建 PVC 与测试 Pod，在 Pod 内读写数据并核验 RBD image
- 强调：clusterID / fsid 必须替换为自己的集群值

## 部署 CSI 插件

在 `ceph-csi/deploy/rbd/kubernetes` 目录下，先部署 provisioner（其中包含 external-provisioner、external-attacher、csi-resizer、csi-rbdplugin 等共 6 个 sidecar 容器）：

```bash
kubectl create -f csi-rbdplugin-provisioner.yaml
```

再部署 RBD CSI driver（Pod 内含 `csi-node-driver-registrar` 与 `csi-rbdplugin` 两个容器）：

```bash
kubectl create -f csi-rbdplugin.yaml
```

部署后观察：

```bash
kubectl get pods -n default | grep csi
```

应看到 provisioner（含 7 个容器）与 node 插件（3 个容器）均处于 `Running`。若容器未启动成功，PV 挂载会失败，务必先排查 Pod 状态。

## 创建 StorageClass

StorageClass 决定 PVC 动态申请 PV 时使用哪个 provisioner。定义如下（**clusterID 必须替换为你自己集群的 fsid**）：

```bash
cat <<EOF > storageclass.yaml
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: csi-rbd-sc
provisioner: rbd.csi.ceph.com
parameters:
   clusterID: c32ff766-19f6-11ed-aa17-00163e005933
   pool: kubernetes
   imageFeatures: layering
   csi.storage.k8s.io/provisioner-secret-name: csi-rbd-secret
   csi.storage.k8s.io/provisioner-secret-namespace: default
   csi.storage.k8s.io/controller-expand-secret-name: csi-rbd-secret
   csi.storage.k8s.io/controller-expand-secret-namespace: default
   csi.storage.k8s.io/node-stage-secret-name: csi-rbd-secret
   csi.storage.k8s.io/node-stage-secret-namespace: default
   csi.storage.k8s.io/fstype: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
mountOptions:
   - discard
EOF
kubectl apply -f storageclass.yaml
```

参数要点：

- **clusterID**：对应前文 Ceph 的 fsid；每台集群此值都不同，不能直接复制课程示例。
- **pool**：前文创建的 `kubernetes` 池。
- **imageFeatures**：限制创建的 RBD image 特征为 `layering`。若不指定，内核可能不支持全部特征导致挂载失败。
- **secret 系列参数**：让 provisioner / node 在不同阶段使用 `csi-rbd-secret` 访问 Ceph。

创建后查看：

```bash
kubectl get sc
```

应能看到 `csi-rbd-sc`，后续 Go 代码创建 PV/PVC 时即引用该 StorageClass（通过其 clusterID 与 secret 关联到具体 Ceph 集群）。

## 验证与使用

进入 ceph-csi 官方示例目录 `example/rbd`，直接创建 PVC：

```bash
kubectl apply -f pvc.yaml
kubectl get pvc
kubectl get pv
```

典型输出：

```text
NAME      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
rbd-pvc   Bound    pvc-44b89f0e-4efd-4396-9316-10a04d289d7f   1Gi        RWO            csi-rbd-sc     8m21s

NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                STORAGECLASS   AGE
pvc-44b89f0e-4efd-4396-9316-10a04d289d7f   1Gi        RWO            Delete           Bound    default/rbd-pvc      csi-rbd-sc    8m18s
```

PVC 已自动绑定到动态生成的 PV（1Gi，RWO）。再创建示例 Pod 把该卷挂载到容器内目录并读写测试：

```bash
kubectl apply -f pod.yaml
kubectl exec -it csi-rbd-demo-pod bash
root@csi-rbd-demo-pod:/# cd /var/lib/www/
root@csi-rbd-demo-pod:/var/lib/www# echo "hello from paas" > caplost.txt
root@csi-rbd-demo-pod:/var/lib/www# cat caplost.txt
hello from paas
```

在 Ceph 侧核验实际写入的 RBD image：

```bash
rbd ls -p kubernetes
# 输出：csi-vol-fe40eb16-1a4e-11ed-bb7c-0eb2f382cefd

rbd info csi-vol-fe40eb16-1a4e-11ed-bb7c-0eb2f382cefd -p kubernetes
# size 1 GiB in 256 objects
# format: 2
# features: layering
```

到此，K8s 通过 CSI 接入外部 Ceph 存储的配置全部完成。后续章节将用 Go 代码把「创建云盘」这一能力封装为平台的后端服务，实现自动化开通。

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
