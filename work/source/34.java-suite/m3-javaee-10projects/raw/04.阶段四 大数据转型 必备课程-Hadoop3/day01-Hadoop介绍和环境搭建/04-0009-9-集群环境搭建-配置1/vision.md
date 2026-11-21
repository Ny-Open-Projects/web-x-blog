# 画面线理解：9-集群环境搭建-配置1

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\9-集群环境搭建-配置1【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:48, 01:19, 01:44, 04:18, 05:00, 08:58, 09:56, 10:23, 10:45, 11:26, 12:13, 12:52, 13:57, 14:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:20:11

1) 这一组画面整体在讲什么（一句话）：
在三台 Linux 服务器上配置防火墙、关闭 SELinux，并设置 SSH 免密登录，为后续 Hadoop 部署做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 内容：在 Typora 中查看“5.1: 三台虚拟机关防火墙”章节，弹出“使用 Google 搜索”菜单。
- 代码/命令：无直接命令，但显示了“service iptables stop”和“chkconfig iptables off”等命令的上下文。

画面 2:
- 内容：在 SecureCRT 中，node03 服务器终端执行“service iptables stop”命令，成功停止防火墙服务。

画面 3:
- 内容：在 SecureCRT 中，node01 服务器终端执行“service iptables stop”和“chkconfig iptables off”命令，成功停止并禁用防火墙服务。

画面 4:
- 内容：在 SecureCRT 中，node02 服务器终端执行“service iptables stop”和“chkconfig iptables off”命令，成功停止并禁用防火墙服务。

画面 5:
- 内容：在 Typora 中查看“5.3 三台机器免密登录”章节，显示 SELinux 配置文件内容。
- SELinux 配置文件内容：
  ```
  # This file controls the state of SELinux on the system.
  # SELinux can take one of these three values:
  #     enforcing - SELinux security policy is enforced.
  #     permissive - SELinux prints warnings instead of enforcing.
  #     disabled - No SELinux policy is loaded.
  SELINUX=enforcing
  ```
- 画面中高亮显示“SELINUX=disabled”并提示“修改此行配置”。

画面 6:
- 内容：在 Typora 中查看“5.3 三台机器免密登录”章节，展示 SSH 免密登录原理的流程图（A节点指向B节点）和文字说明。

画面 7:
- 内容：在 Typora 中查看“5.3 三台机器免密登录”章节，展示“第一步：三台机器生成公钥与私钥”的命令。
- 命令：
  ```
  ssh-keygen -t rsa
  ```
- 画面中显示在 node01 执行命令后，终端提示“Generating public/private rsa key pair.”。

画面 8:
- 内容：在 SecureCRT 中，node01 服务器终端执行“ssh-keygen -t rsa”命令后，终端提示“Enter file in which to save the key (/root/.ssh/id_rsa):”，并提示“Overwrite (y/n)?”。

画面 9:
- 内容：在 Typora 中查看“5.3 三台机器免密登录”章节，展示在 node01 服务器上执行“ssh-keygen -t rsa”命令后，终端提示“Overwrite (y/n)?”。

画面 10:
- 内容：在 SecureCRT 中，node01 服务器终端执行“ssh-keygen -t rsa”命令后，终端提示“Overwrite (y/n)?”，用户输入“y”后，命令继续执行。
- 画面中显示终端输出“Generating public/private rsa key pair.”。

画面 11:
- 内容：在 SecureCRT 中，node01 服务器终端执行“ssh-keygen -t rsa”命令后，终端提示“Overwrite (y/n)?”，用户输入“y”后，命令继续执行。
- 画面中显示终端输出“Generating public/private rsa key pair.”。

画面 12:
- 内容：在 SecureCRT 中，node02 服务器终端执行“ssh-keygen -t rsa”命令后，终端提示“Enter file in which to save the key (/root/.ssh/id_rsa):”，并提示“Overwrite (y/n)?”。
- 画面中显示终端输出“Generating public/private rsa key pair.”。

画面 13:
- 内容：在 SecureCRT 中，node02 服务器终端执行“ssh-copy-id node01”命令，成功将公钥复制到 node01。
- 命令：
  ```
  ssh-copy-id node01
  ```
- 画面中显示终端输出“Now try logging into the machine, with 'ssh 'node01', and check in: .ssh/authorized_keys”。

画面 14:
- 内容：在 Typora 中查看“5.4 三台机器时钟同步”章节，展示“第三步：复制第一台机器的认证到其他机器”的命令。
- 命令：
  ```
  scp /root/.ssh/authorized_keys node02:/root/.ssh
  scp /root/.ssh/authorized_keys node03:/root/.ssh
  ```
- 画面中显示终端执行命令后，提示“Password:”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```
# This file controls the state of SELinux on the system.
# SELinux can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=enforcing
```

画面 7:
```
ssh-keygen -t rsa
```

画面 13:
```
ssh-copy-id node01
```

画面 14:
```
scp /root/.ssh/authorized_keys node02:/root/.ssh
scp /root/.ssh/authorized_keys node03:/root/.ssh
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
- 标题：“5.3 三台机器免密登录”
- 流程图：A节点 → B节点
- 文字说明：
  - 为什么免密登录：
    - Hadoop 节点众多，所以一般在主节点启动从节点，这个时候就需要频繁地从主节点登录到从节点中，如果不能免密登录每次都要输入密码，非常麻烦。
  - 免密 SSH 登录的原理：
    1. 需要先在 B 节点配置 A 节点的公钥。
    2. A 节点请求 B 节点要求登录。
    3. B 节点使用 A 节点的公钥，加密一段随机文本。
    4. A 节点使用私钥解密，并发回 B 节点。
    5. B 节点验证文本是否正确。

画面 6:
- 标题：“5.3 三台机器免密登录”
- 流程图：A节点 → B节点
- 文字说明：
  - 为什么免密登录：
    - Hadoop 节点众多，所以一般在主节点启动从节点，这个时候就需要频繁地从主节点登录到从节点中，如果不能免密登录每次都要输入密码，非常麻烦。
  - 免密 SSH 登录的原理：
    1. 需要先在 B 节点配置 A 节点的公钥。
    2. A 节点请求 B 节点要求登录。
    3. B 节点使用 A 节点的公钥，加密一段随机文本。
    4. A 节点使用私钥解密，并发回 B 节点。
    5. B 节点验证文本是否正确。

画面 14:
- 标题：“5.4 三台机器时钟同步”
- 文字说明：
  - 为什么需要时间同步：
    - 因为很多分布式系统有状态的，比如说存储一个数据，A 节点记录的时间是 1，B 节点记录的时间是 2，就会出问题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
