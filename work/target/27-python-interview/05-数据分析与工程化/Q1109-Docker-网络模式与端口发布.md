---
title: [Q1109] Docker 网络模式与端口发布
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1109 · Docker 网络模式与端口发布

> 难度:★★★☆ | 标签:Docker, 网络

**问**:bridge 和 host 网络有什么区别?容器之间怎么互访?

**答**:bridge 是默认模式:容器接在 docker0 网桥,经 NAT 访问外网,外部访问要 `-p 8080:80` 做端口映射;host 模式共享宿主机网络栈,无 NAT 性能最好但端口冲突且隔离弱;none 只有 loopback,适合离线批任务。容器互访的正确姿势:自定义网络内置 DNS,服务名即主机名(`web`、`db` 直接互连),不要用已被废弃的容器 link。排查顺序:进容器 ping/nc 服务名、检查 compose 网络是否同一张、再查端口映射。

```python
# file: code/05_数据分析与工程化/q1109_docker_network.py
import shutil
import subprocess

def sh(cmd):
    print("$", cmd)
    if shutil.which("docker"):
        try:
            out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            print((out.stdout or out.stderr).strip()[:400])
        except Exception as e:
            print("docker 调用失败:", e)
    else:
        print("本机未安装 docker,仅演示命令")

if __name__ == "__main__":
    sh("docker network create app-net")
    sh("docker run -d --name web --network app-net -p 8080:80 nginx")
    sh("docker network inspect app-net")
    print("""
模式对比:
  bridge 默认 经 docker0 与 NAT 外部访问需 -p 端口映射
  host    共享宿主机网络栈 无 NAT 隔离弱
  none    仅 loopback 适合离线任务
  自定义网络内置 DNS 服务名互访
""")
```

**追问**:
- 追问 1:-p 8080:80 数据怎么走?—— 宿主机 iptables/nftables DNAT 把 8080 转到容器 80,回程 SNAT 自动完成。
- 追问 2:k8s 里还用 -p 吗?—— 不用,Pod 有独立 IP,Service/Ingress 负责暴露,端口映射是单机 Docker 的概念。
