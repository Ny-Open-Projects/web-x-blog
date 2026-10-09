# Go PaaS 平台开发: 使用 cephadm 引导安装 Ceph 基础集群

## 纲要

- 通过 GitHub 直接下载 `cephadm` 二进制，避免使用系统包管理器安装导致版本不兼容
- 使用 `cephadm add-repo --release quincy` 指定要安装的 Ceph release 并完成安装
- 通过 `cephadm bootstrap --mon-ip <内网IP>` 引导首个节点，自动创建 Monitor 与 Manager 守护进程
- bootstrap 产生的关键文件：集群最小配置、管理员密钥环、用于添加节点的 SSH 公钥、自动拉取的 Quincy 镜像
- Dashboard 默认通过 8443 端口访问，购买云服务器时需在安全组放行该端口

## 安装 cephadm 工具

在正式部署前，我们已经完成了每台机器的初始化（主机名、时间同步、`/etc/hosts` 等，详见本章「Ceph 安全机器初始化」一节）。下面安装 `cephadm` 引导工具。

课程建议**不要**通过系统的 `dnf`/`yum` 安装 `cephadm`：

```bash
# 不推荐：系统包管理器安装的 cephadm 可能对应最旧的版本，
# 而容器镜像却是最新的，二者不一致会导致兼容性故障
dnf -y install cephadm
```

原因是系统仓库里的 `cephadm` 版本往往偏旧，拉起的容器镜像却是新版，版本错配会引发各种异常。课程采用从 GitHub 下载指定 release 的方式，最稳妥。

```bash
# 从 GitHub 下载 cephadm 二进制（课程使用 Quincy / v16）
curl --silent --remote-name https://github.com/ceph/ceph/raw/quincy/src/cephadm/cephadm

# 下载后默认没有执行权限，需手动加上
chmod +x cephadm

# 指定要使用的 Ceph release（此处为 quincy）
./cephadm add-repo --release quincy

# 安装 cephadm 自身及必要依赖
./cephadm install
```

安装完成后，`cephadm` 即可直接使用；另一种可选方式是通过 `dnf` 安装，但如前所述不推荐。

## 引导首个集群节点

引导（bootstrap）操作只需在主节点上执行一次。它会创建 Monitor（MON）与 Manager（MGR）守护进程，并为集群生成 SSH 公钥，随后自动拉取 Quincy 版本的容器镜像。

```bash
# mon-ip 必须填写节点内网 IP，切勿填写公网 IP
./cephadm bootstrap --mon-ip 192.168.1.73
```

注意：`--mon-ip` 必须填**内网 IP**。在阿里云等云环境下填写公网 IP 会导致绑定失败，因为节点间通信走的是内网。课程中第一台节点的内网 IP 为 `192.168.1.73`，该节点默认即为主节点（mon + mgr）。

## 引导后的关键产物

bootstrap 命令执行过程中会生成并保存以下文件，后续所有配置与运维都围绕它们展开：

- `/etc/ceph/ceph.conf`：集群最小配置文件，集群的全部配置都在这里修改
- `/etc/ceph/ceph.client.admin.keyring`：管理员（admin）特权密钥环，保存在该文件中
- `/etc/ceph/ceph.pub`：自动生成的 SSH 公钥，后续添加新节点时需要把它拷贝到目标节点的 `authorized_keys` 中才能纳管
- FSID：集群唯一标识，添加到节点、运维排障时常会用到
- 自动拉取 Quincy 镜像并启动 Monitor、Manager，Manager 还会一并启动 Prometheus 与官方 Dashboard 等组件

引导成功后，日志中会打印 Dashboard 的访问地址（形如 `https://<mon-ip>:8443/`）。

## 访问 Dashboard

1. 在云厂商安全组中放行 `8443` 端口，否则无法访问 Dashboard
2. 在本机 `hosts` 中将 Dashboard 域名（一串主机标识）映射到节点公网 IP，即可通过浏览器访问
3. 浏览器会提示证书错误（证书为自动生成），忽略并继续访问即可
4. 使用 bootstrap 输出的初始用户名与密码登录，登录后按提示修改初始密码

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
