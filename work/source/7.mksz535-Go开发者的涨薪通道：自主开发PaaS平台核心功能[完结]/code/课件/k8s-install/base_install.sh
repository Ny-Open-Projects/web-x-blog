#!/bin/bash
# 在 master 节点和 node 节点都要执行
# 阿里云 docker hub 镜像
#export REGISTRY_MIRROR=https://registry.cn-hangzhou.aliyuncs.com

# 在 master 节点和 node 节点都要执行

# 安装 containerd
# 参考文档如下
# https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd

# cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
# overlay
# br_netfilter
# EOF

# sudo modprobe overlay
# sudo modprobe br_netfilter

# # Setup required sysctl params, these persist across reboots.
# cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
# net.bridge.bridge-nf-call-iptables  = 1
# net.ipv4.ip_forward                 = 1
# net.bridge.bridge-nf-call-ip6tables = 1
# EOF

# sysctl --system

# 卸载旧版本
# yum remove -y containerd.io

# 卸载旧版本
yum remove -y docker \
docker-client \
docker-client-latest \
docker-ce-cli \
docker-common \
docker-latest \
docker-latest-logrotate \
docker-logrotate \
docker-selinux \
docker-engine-selinux \
docker-engine

# 设置 yum repository
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo



# 安装并启动 docker
yum install -y docker-ce docker-ce-cli
# yum install -y containerd.io-1.4.3

mkdir /etc/docker || true

cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": ["${REGISTRY_MIRROR}"],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
EOF

mkdir -p /etc/systemd/system/docker.service.d

# Restart Docker
systemctl daemon-reload
systemctl enable docker
systemctl restart docker


# mkdir -p /etc/containerd
# containerd config default > /etc/containerd/config.toml

# sed -i "s#k8s.gcr.io#registry.aliyuncs.com/k8sxio#g"  /etc/containerd/config.toml
# sed -i '/containerd.runtimes.runc.options/a\ \ \ \ \ \ \ \ \ \ \ \ SystemdCgroup = true' /etc/containerd/config.toml
# sed -i "s#https://registry-1.docker.io#${REGISTRY_MIRROR}#g"  /etc/containerd/config.toml


# systemctl daemon-reload
# systemctl enable containerd
# systemctl restart containerd


# 安装 nfs-utils
# 必须先安装 nfs-utils 才能挂载 nfs 网络存储
yum install -y nfs-utils
yum install -y wget

# 关闭 防火墙
systemctl stop firewalld
systemctl disable firewalld

# 关闭 SeLinux
setenforce 0
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

# 关闭 swap
swapoff -a
yes | cp /etc/fstab /etc/fstab_bak
cat /etc/fstab_bak |grep -v swap > /etc/fstab

# 配置K8S的yum源
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
       http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

# 卸载旧版本
yum remove -y kubelet kubeadm kubectl

# 安装kubelet、kubeadm、kubectl
# 将 ${1} 替换为 kubernetes 版本号，例如 1.19.5
yum install -y kubelet-${1} kubeadm-${1} kubectl-${1}

# crictl config runtime-endpoint /run/containerd/containerd.sock

# 重启 docker，并启动 kubelet
systemctl daemon-reload
systemctl restart docker
systemctl enable kubelet && systemctl start kubelet

docker --version
kubelet --version
