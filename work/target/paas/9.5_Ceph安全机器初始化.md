# Go PaaS 平台开发: Ceph 安全机器初始化

## 纲要

- 三台机器分别安装必要依赖，重点必须安装时间同步服务（chrony）
- 关闭防火墙（firewalld）并禁用 SELinux，减少安装干扰
- 设置主机名（如 ceph01 / ceph02 / ceph03），主机名中不要带点号
- 配置 `/etc/hosts`，把节点内网 IP 与主机名一一对应写入三台机器
- 主机名与内网 IP 顺序建议和云厂商标记保持一致，避免后续添加节点出错

## 安装前置依赖

登录三台服务器后，逐台执行安装命令（远程连接可能较慢，每台约两分钟）：

```bash
# 在三台节点分别安装基础依赖
# 以 CentOS 8.3 为例
dnf -y install chrony vim wget
systemctl enable --now chronyd
```

> **时间同步务必安装**：Ceph 是分布式系统，节点间依赖时间一致。若未安装时间同步服务，添加主机时会报错，安装过程中也会提示时间不同步。

## 关闭防火墙与 SELinux

为减少安装期的网络与权限干扰，关闭防火墙并禁用 SELinux：

```bash
# 关闭并禁用 firewalld
systemctl stop firewalld
systemctl disable firewalld

# 临时关闭 SELinux（重启后失效）
setenforce 0

# 永久禁用：修改 /etc/selinux/config
sed -i 's/^SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
```

## 设置主机名

三台机器按 1/2/3 顺序分别设置主机名，主机名中**不要带点号**，否则添加节点时会报错：

```bash
# 节点一
hostnamectl set-hostname ceph01
# 节点二
hostnamectl set-hostname ceph02
# 节点三
hostnamectl set-hostname ceph03
```

## 配置 /etc/hosts

Ceph 节点之间走内网 IP 通信。将三台机的内网 IP（如 `.73 / .74 / .75`）与主机名一一对应写入每台机器的 `/etc/hosts`：

```bash
# 在三台机器上均追加如下内容（以实际内网 IP 为准）
cat >> /etc/hosts <<'EOF'
192.168.1.73 ceph01
192.168.1.74 ceph02
192.168.1.75 ceph03
EOF
```

建议主机名与云厂商控制台标记的实例名称一致（ceph01 对应 `.73`，以此类推），后续添加节点、编写安装说明时不会混淆。

## 初始化完成检查

完成以上步骤即完成安装前初始化：

- 时间同步服务运行正常
- 防火墙已关闭、SELinux 已禁用
- 三台主机名设置完毕且无点号
- `/etc/hosts` 中内网 IP 与主机名映射正确

下一节将基于这些初始化好的节点，使用 cephadm 引导安装集群。

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
