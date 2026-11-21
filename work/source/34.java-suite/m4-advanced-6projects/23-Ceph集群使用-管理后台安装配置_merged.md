# 23-Ceph集群使用-管理后台安装配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢,咱们来讲解Safe管理后台的安装和配置。

那怎么去实现呢?

首先,我们要开启Dashboard的模块。

其实在这里呢,它是以模块的方式进行了安装。

通过SafeMGR Model Enable Dashboard开启对应的模块就可以了,

在组件链上面进行执行。

我们可以看一下。

在这里呢,它说我们已经开启了,

因为在这之前呢,我已经做了测试和验证。

好,下面的话呢,就要生成它对应的签名。

通过这个命令去做一个执行,

它就会创建对应的签名密钥的信息。

然后呢,我们也创建一个目录。

这个目录的话呢,会去生成对应的密钥对的一个信息。

我们可以看一下。

CD,然后呢,进入我们的SafeCluster。

SafeCDMGRDashboard。

好,这个呢,是专门用于MGR Dashboard模块的一个目录。

在下面呢,我们要去什么?

创建它对应的密钥对。

怎么去创建呢?

我们可以copy一下命令。

它在这里呢,就会创建对应的这个key文件。

好,这个话呢,因为Dashboard,

比如说你要ATTPS的一个链接的话呢,

它要去,还有那个安全性的一个传输。

那在这一块的话呢,

它要去开启对应的一个密钥。

密钥认证信息。

好,那么通过以下指定的SSL的一个方式,

我们去创建对应的一个密钥证书就可以了。

那如果是大家内网测试的时候呢,

我们也可以不需要去通过ATTPS的方式进行访问。

通过ATTB访问也是可以。

好,这个呢,是密钥队的一个配置。

当然,如果是通过ATTPS的话呢,

密钥队是一定要生成的。

下面的话呢,我们就要启动Dashboard。

怎么启动呢?

其实就是模块化的开启和关闭就可以了。

通过这个命令呢,

Enable就是关闭,

Enable呢,就是开启。

这样呢,它就会启动Dashboard的服务。

我们可以看一下。

当中我们已经是启动完成,对不对?

好,然后呢,我们要设置它对应的IP和端口,

然后关闭ATTPS。

建议内网的情况下,我们关闭ATTPS,

以防出现一些不必要访问的一些连接安全信息。

那么我们再去查看服务的一个盖友信息。

我们来看一下Safe Manager Service。

在下面呢,

它会显示出我们Dashboard的访问端口、IP等具体信息。

好,这个呢,是设置它的一个管理用户和密码。

那我如果是你想指定其他的一个用户名或者密码的话呢,

就可以在这里做调整和修改。

默认的话呢,是admin进行一个访问。

那咱们呢,就来访问看一下。

咱们呢,打开浏览器,然后呢,输入它的IP和端口。

这个呢,就是在这里面显示出来的连接信息。

好,然后呢,它可以进行一个访问。

在这里呢,我们默认就采用admin。

然后我们登录进去看一下。

好,这个时候呢,就是我们的Dashboard管理后台。

管理后台呢,它会显示一些盖友信息。

比如说在这里面,monitor它的一些监控节点信息、OSD的一个信息。

然后呢,整个的使用的情况,一些对象存储的信息。

然后Pool它的一些连接时管理的一个信息。

在下面的话呢,还有File,就是文件系统管理。

然后的话,Object,Gateway,用户的一些管理。

这些的话呢,都是能够很直观的、很方便的,帮助我们进行SIM的一个管理。

好,这个呢,就是Dashboard。

那Dashboard的一个安装和配置呢,就已经实现完成。

这一讲呢,咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **Ceph 分布式存储系统** 的实战部署教程，具体聚焦于 **安装和配置 Ceph 的 Web 管理后台（Dashboard）**。讲师通过在 CentOS 7 虚拟机上操作，演示了从启用 Dashboard 模块、生成自签名 SSL 证书、创建必要的目录、生成密钥对，到最终配置并访问 Dashboard 的完整流程。整个过程旨在让学习者掌握如何为 Ceph 集群搭建一个可视化的管理界面，以便于监控和管理集群状态。视频中还展示了 Ceph Dashboard 的最终访问效果，界面清晰地显示了集群的健康状况、存储池（Pools）信息等核心数据。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，讲师在 Typora 文档中定位到“3.5 安装管理后台”章节。
*   **00:00:05 - 00:00:15**：讲师切换到 SecureCRT 会话，展示 Ceph 集群的健康状态和 OSD 信息。
*   **00:00:15 - 00:00:30**：讲师在 Typora 中展示“3.5 安装管理后台”的步骤列表，包括“1. 开启dashboard模块”、“2. 生成签名”、“3. 创建目录”、“4. 生成密钥对”、“5. 启动dashboard”等。
*   **00:00:30 - 00:00:45**：讲师在终端中执行 `ceph mgr module enable dashboard` 命令，确认模块已启用。
*   **00:00:45 - 00:01:00**：讲师执行 `ceph dashboard create-self-signed-cert` 命令，生成自签名证书。
*   **00:01:00 - 00:01:15**：讲师创建目录 `mkdir mgr-dashboard`，并切换到该目录。
*   **00:01:15 - 00:01:30**：讲师使用 `openssl req -new -nodes -x509 -subj ...` 命令生成密钥对 `dashboard.key` 和 `dashboard.crt`。
*   **00:01:30 - 00:01:45**：讲师在 Typora 中展示“7. 关闭HTTPS”和“8. 查看服务信息”的步骤。
*   **00:01:45 - 00:02:00**：讲师执行 `ceph config set mgr mgr/dashboard/server_addr 10.10.20.11` 和 `ceph config set mgr mgr/dashboard/server_port 18843` 命令，配置 Dashboard 的 IP 和端口。
*   **00:02:00 - 00:02:15**：讲师执行 `ceph config set mgr mgr/dashboard/ssl false` 命令，关闭 HTTPS。
*   **00:02:15 - 00:02:30**：讲师执行 `ceph mgr services` 命令，查看服务信息。
*   **00:02:30 - 00:02:45**：讲师执行 `ceph dashboard set-login-credentials admin admin` 命令，设置登录用户名和密码。
*   **00:02:45 - 00:03:00**：讲师在浏览器中访问 `https://10.10.20.11:8443/`，成功打开 Ceph Dashboard 界面。
*   **00:03:00 - 00:03:15**：讲师在 Dashboard 界面中展示集群的健康状态、存储池信息等。
*   **00:03:15 - 00:03:30**：讲师在 Typora 中切换到“3.6 创建Cephfs”章节，准备讲解下一步。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **Typora 文档**：显示了课程大纲，包括“3.5 安装管理后台”、“3.6 创建Cephfs”等章节。
    *   **章节标题**：如“3.5 安装管理后台”、“3.6 创建Cephfs”、“10. 访问”。
    *   **步骤列表**：如“1. 开启dashboard模块”、“2. 生成签名”、“3. 创建目录”、“4. 生成密钥对”、“5. 启动dashboard”、“7. 关闭HTTPS”、“8. 查看服务信息”、“9. 设置管理用户与密码”、“10. 访问”。

*   **命令行代码**：
    *   `ceph mgr module enable dashboard`
    *   `ceph dashboard create-self-signed-cert`
    *   `mkdir mgr-dashboard`
    *   `cd /usr/local/ceph-cluster/mgr-dashboard`
    *   `openssl req -new -nodes -x509 -subj "O=IT/CN=ceph-mgr-dashboard" -days 3650 -keyout dashboard.key -out dashboard.crt -extensions v3_ca`
    *   `ceph config set mgr mgr/dashboard/server_addr 10.10.20.11`
    *   `ceph config set mgr mgr/dashboard/server_port 18843`
    *   `ceph config set mgr mgr/dashboard/ssl false`
    *   `ceph mgr services`
    *   `ceph dashboard set-login-credentials admin admin`

*   **图表 / 界面截图**：
    *   **Ceph Dashboard 界面**：显示了集群的健康状态（`HEALTH_OK`）、存储池（Pools）列表、对象数量、容量使用率等信息。
    *   **终端界面**：展示了执行命令后的输出结果，如 `health: HEALTH_OK`、`services` 信息、文件列表等。

---

### 4) 关键场景与演示描述

*   **场景一：启用 Dashboard 模块**
    *   **描述**：讲师在终端中执行 `ceph mgr module enable dashboard` 命令，系统返回 `module dashboard is already enabled`，表明模块已成功启用。

*   **场景二：生成自签名证书**
    *   **描述**：讲师执行 `ceph dashboard create-self-signed-cert` 命令，系统生成了证书文件，为后续的 HTTPS 服务做准备。

*   **场景三：创建目录与生成密钥对**
    *   **描述**：讲师创建了 `mgr-dashboard` 目录，并使用 `openssl` 命令生成了 `dashboard.key` 和 `dashboard.crt` 两个文件，用于配置 Dashboard 的安全连接。

*   **场景四：配置 Dashboard 服务**
    *   **描述**：讲师通过 `ceph config set` 命令，将 Dashboard 的服务地址设置为 `10.10.20.11`，端口设置为 `18843`，并关闭了 HTTPS 服务（`ssl false`），以便于访问。

*   **场景五：设置登录凭据**
    *   **描述**：讲师执行 `ceph dashboard set-login-credentials admin admin` 命令，为 Dashboard 设置了默认的用户名和密码。

*   **场景六：访问 Dashboard**
    *   **描述**：讲师在浏览器中输入 `https://10.10.20.11:8443/`，成功打开了 Ceph Dashboard 界面。界面显示了集群的健康状态为 `HEALTH_OK`，并列出了多个存储池（如 `rbd.root`, `default.rgw.control` 等）及其使用情况，证明了管理后台已成功部署并可以正常工作。

---
