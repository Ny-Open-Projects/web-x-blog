# Go PaaS 平台开发: 集群外创建 kubeconfig 并用 kubectl 操作 K8s（上）

## 纲要

- 在开发机上安装 `kubectl`，它是 K8s 官方命令行客户端，用于从集群外操作集群。
- 把 Master 节点上的 `~/.kube/config` 拷贝到本地 `~/.kube/config`，其中包含访问集群的证书与 API Server 地址。
- config 中的 `server` 地址必须指向 API Server 的公网 IP；本地可用 hosts 文件做域名解析。
- 用 `kubectl get nodes` 验证集群连通性。
- 在 Go 中以"集群外"模式创建 K8s 客户端（`client-go`），核心是先校验 config 文件存在，再用 `BuildConfigFromFlags` 构建 `rest.Config`，最后生成 `kubernetes.Clientset`。
- 区分集群外与集群内两种客户端创建方式。

## 在开发机安装 kubectl

`kubectl` 是 Kubernetes 官方提供的命令行工具，运行在集群之外，专门用来操作集群。开发机上的 Go 程序也正是通过它（以及 `client-go` 库）来完成对集群的调用。

安装步骤（以 macOS 为例，Windows 同理）：

1. 从官网下载对应操作系统的 `kubectl` 二进制。
2. 赋予可执行权限：`chmod +x kubectl`。
3. 移动到系统 PATH 目录，例如 macOS 的 `/usr/local/bin`。
4. 终端执行 `kubectl version --client` 验证安装。
5. 把 Master 节点上的 config 文件拷贝到本机。

## 拷贝 kubeconfig

在 Master 节点安装完成后，会在 `/etc/kubernetes/admin.conf` 生成配置文件。把它拷贝到本机家目录的 `.kube` 下：

```bash
# 在 Master 节点
mkdir -p /root/.kube
cp -i /etc/kubernetes/admin.conf /root/.kube/config

# 在开发机（本地）
mkdir -p ~/.kube
# 将 Master 上的 config 内容整体拷贝到本地 ~/.kube/config
```

config 文件里包含与集群通信所需的证书，以及最重要的 `server` 字段——它是与集群内部通信的 API Server 地址：

```yaml
apiVersion: v1
kind: Config
clusters:
- name: kubernetes
  cluster:
    server: https://<APIServer公网IP>:6443
    certificate-authority-data: <base64 证书>
users:
- name: kubernetes-admin
  user:
    client-certificate-data: <base64 客户端证书>
    client-key-data: <base64 客户端私钥>
```

要点：

- `server` 必须指向 API Server 的**公网 IP**，否则本地无法解析与访问。
- 若没有购买域名，可在本地 `hosts` 文件（Windows 下也在另一目录）把域名强制指向 Master 公网 IP，效果等价。生产环境仍建议做正式解析。
- 客户端证书配合 `kubectl` 工具，才能在集群外经由 kubectl 操作 K8s。

## 验证集群

```bash
kubectl get nodes
```

若能列出集群节点且状态为 `Ready`，说明 config 下载与配置正确，可以进入代码开发。若返回异常，需要先回头修正 `kubectl` 配置。

## 在 Go 中创建 K8s 客户端（集群外模式）

平台程序运行在集群之外，因此使用"集群外"方式创建客户端。核心是先判断 config 文件是否存在，再构建 `rest.Config`，最后生成 `Clientset`：

```go
package k8s

import (
    "fmt"
    "os"

    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/rest"
    "k8s.io/client-go/tools/clientcmd"
)

// 集群外创建 K8s 客户端
func NewClientOutOfCluster() (*kubernetes.Clientset, error) {
    // 1. 指定 kubeconfig 路径（通常为 ~/.kube/config）
    kubeConfig := os.Getenv("HOME") + "/.kube/config"

    // 2. 判断 config 文件是否存在
    if _, err := os.Stat(kubeConfig); os.IsNotExist(err) {
        return nil, fmt.Errorf("kubeconfig 不存在: %v", err)
    }

    // 3. 集群外：用 BuildConfigFromFlags 读取本地 config
    config, err := clientcmd.BuildConfigFromFlags("", kubeConfig)
    if err != nil {
        return nil, err
    }

    // 4. 生成 Clientset
    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        return nil, err
    }
    return clientset, nil
}
```

`Clientset` 创建成功后，即可用它操作集群资源（如创建 Deployment、Pod、Service 等）。一般地，我们会把这个 clientset 传入 Repository/Service 层，由数据访问层调用它来真正操作 K8s。

## 集群内模式对比

若程序运行在 Pod 内部，则无需读取本地 config 文件，直接使用 `InClusterConfig`：

```go
// 集群内创建 K8s 客户端
func NewClientInCluster() (*kubernetes.Clientset, error) {
    config, err := rest.InClusterConfig()
    if err != nil {
        return nil, err
    }
    return kubernetes.NewForConfig(config)
}
```

两种方式的差异只在于 `rest.Config` 的来源：集群外用 `clientcmd` 读取本地文件，集群内用 `rest.InClusterConfig()` 读取挂载的 ServiceAccount 信息。

## 衔接

本篇完成了"集群外 kubeconfig + Go 客户端"的搭建与连通性验证。下一篇将基于这个 clientset，编写初始化逻辑并把客户端挂入微服务，同时补上数据库表的自动初始化。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/k8s-install/check_host.sh`
- `code/课件/common/config.go`
- `code/课件/middleware/domain/model/middle_config.go`
- `code/课件/k8s-install/install_master.sh`
- `code/课件/go-paas-html/pages-404.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
