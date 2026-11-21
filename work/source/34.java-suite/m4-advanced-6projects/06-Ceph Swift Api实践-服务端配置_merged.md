# 06-Ceph Swift Api实践-服务端配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接下来咱们开始学习Safe Swift API的服务端配置

首先咱们要确保Safe集群正常安装并启动成功

之前对Safe的集群咱们做了讲解

那么我们将虚拟机上的Safe集群正常启动

启动成功之后我们去检查Safe的状态

这个是我们之前所搭建的三台Safe节点

我们进入它的主节点10.10.20.11

在下面查看Safe的整个运行状态

它的状态目前是Health OK

这个一定要确保它是正常运行的状态

接着咱们去验证网关是否能够正常访问

因为Safe Swift API它其实要通过RGW去做对应实现

所以我们要确保Safe的RGW组件能够正常运行

那么咱们去

转为访问7480的端口

好我们刷信下

这个时候咱们可以看到Safe的网关转文是正常

并且也有响应内容

接下来咱们就要创建Safe的用户

用于接口的请求和认证

在这里我已经事先创建好了

那么我这边就不再执行

主要给大家讲解一下这个命令的主要作用

这个命令咱们可以看到

它是通过Ledos GW的命令

进行用户的创建

这个参数它是指定你的子用户

如果咱们需要用到子用户

这个也要把它创建并且记录下来

接着是我们的UID

也就是用户的名称

然后是显示的名称

这个是Key Type类型

因为我们是要创建Swift的用户

在这里配置Swift

Squid是它的密钥

Access是所有权限都可以进行访问

好

这个就是整个命令的讲解说明

通过这个命令创建完成之后

它能够返回对应的结果

在我们主节点上面去执行

在这里就不重复执行了

因为咱们已经创建了对应的用户

重新执行了

它也不能创建成功

好

那么我们看一下它的返回结果是怎样的

它的返回结果

首先是它的UID

也就是咱们所传递过去的UID

然后是Displace Name

可以做一个返回结果

然后是它的检查

下面就是它的Subuser用户的信息

Permission是你对应的权限

为了便于我们的测试和验证

咱们可以将它的所有权限

全部赋予这个用户

接下来的话就是它的Key

这个Key的话大家一定要记住

因为咱们在应用服务当中

要去调用访问的话

都要传递对应的Squid密钥

下面的话就是一些其他信息

大家的话也可以去了解下

最主要咱们要记住

SwiftKey下面的User以及SquidKey信息

也就是这一部分

因为在代码当中是需要使用到的

好

接着的话

咱们就要去激活管理后台的对象存储模块

咱们可以进入管理后台

看一下整个的存储模块是否已经激活

这个是File System

我们创建一个FSTest

在这里挂载了它的Data

以及Metadata信息

那么存储模块的话

它是正常在运作的

这个在咱们之前对Safe基群发现的时候

也做了讲解和介绍

下面就要创建一个管理用户

这个管理用户的创建命令是怎样的

同样是通过Ledos GW的MIM

然后这里去创建一个用户名称

然后显示名称

这个是你的类型

这个类型就是System

如果创建成功之后

下面会返回对应的结果信息

在这里大家要记住它的Access Key

Secret Key

因为下面当中咱们要去使用

这个Access Key跟Secret Key具体是什么作用呢

咱们来看一下

拿到这两个Key之后

我们要去通过Safe的Dashboard的模块

也就是管理后台

去将对应的Key设置进去

这样咱们就可以看到

我们刚才所创建的

两个用户

如果你在Dashboard上面

没有设置对应的Key

那么它就没有权限去访问咱们所创建的管理用户

看到没有

也就没法去访问Safe的用户

所以咱们要在Dashboard上面

去将管理员的密钥信息嵌入进去

这样通过Dashboard

我们就能够管理Safe的相关的操作用户

这个明白吧

好

那咱们就来进入管理界面来看一下

咱们去刷新一下管理后台

这个管理用户在哪里呢

在Object Gateway下面有个User

看到没有

所以的话呢

如果你没有去将它的管理用户的Key设置进去

在这个模块下面

你是没法看到咱们所创建的网关相关的用户账号

这点要明白清楚

好

那么

在这里呢

我们就能够统一管理了相关的用户信息

刚才的话呢

咱们去创建了Safe Test

对不对

还有Manage User

Safe Test呢

就是咱们API调用时候呢

所需要用到的用户信息

那么咱们可以点击这条记录

查看了它的详细信息

在这里呢

它都会列出来

它相关的一些设置信息

好

这个呢

是没有对应的权限限制

好

再往下面呢

咱们就可以呢

通过Safe

Safe API进行一个调用验证

咱们呢

就将Safe

Safe的呢

服务端的配置呢

都已经实现完成

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“交易平台 - Day 9”系列课程中关于 **Ceph Swift API 服务端配置与调用验证** 的实操教学。课程主要演示了如何在 Ceph 集群中配置并验证 Swift 对象存储服务，包括：
- 确认 Ceph 集群健康状态。
- 验证 Swift 网关服务是否正常运行。
- 使用 `radosgw-admin` 工具创建主用户（`uid`）和子用户（`subuser`）。
- 为用户分配权限并配置存储配额。
- 通过 Ceph Dashboard 管理界面验证用户创建结果。
- 最后，演示如何修改 Java 工程 `ceph-demo` 以调用 Swift API。

整个过程旨在帮助学员掌握 Ceph Swift 服务端的配置、用户管理及 API 调用基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**: **章节 3.5 Ceph Swift Api 服务端的配置** - 开始讲解服务端配置。
- **00:05 - 00:10**: **步骤 1. 确保集群正常安装并启动** - 通过 `ceph -s` 命令检查集群健康状态。
- **00:10 - 00:15**: **步骤 2. 验证网关是否正常** - 访问 `http://10.10.20.11:7480` 验证 Swift 网关。
- **00:15 - 00:20**: **步骤 3. 创建一个管理用户** - 使用 `radosgw-admin user create` 命令创建主用户 `cephtester`。
- **00:20 - 00:25**: **步骤 4. 激活管理后台的对象存储模块** - 通过 `ceph dashboard set-rgw-api-access-key` 和 `ceph dashboard set-rgw-api-secret-key` 命令配置 Dashboard。
- **00:25 - 00:30**: **步骤 5. 创建一个管理用户** - 创建子用户 `mgruser`。
- **00:30 - 00:35**: **步骤 6. Ceph Swift Api 调用验证** - 切换到 `ceph-demo` 工程，准备进行 API 调用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **标题**: `3.5 Ceph Swift Api 服务端的配置`
- **学习目标**: 1. 目标 2. 步骤 3. 实现
- **章节导航**: 包含 `3.1 Ceph Swift Api 实践说明` 至 `3.6 Ceph Swift Api 调用验证` 等子章节。

#### 代码与命令

- **检查集群状态**:
  ```bash
  [root@CENTOS7-1 ceph-cluster]# ceph -s
  ```

- **验证网关**:
  - 访问地址: `http://10.10.20.11:7480`
  - 返回提示: `This XML file does not appear to have any style information associated with it.`

- **创建主用户**:
  ```bash
  radosgw-admin user create --uid=cephtester --display-name=cephtester --key-type=swift --secret=654321 --access=full
  ```

- **创建子用户**:
  ```bash
  radosgw-admin user create --uid=mgruser --display-name=mgruser --system
  ```

- **配置 Dashboard API 密钥**:
  ```bash
  ceph dashboard set-rgw-api-access-key XZDC4YOAORE01NMYU3VV
  ceph dashboard set-rgw-api-secret-key meO280HLvctkzzBs74ufXS0wi947NBe6wpj3MxKP
  ```

#### JSON 配置结构

- **用户创建返回的 JSON 结构**:
  ```json
  {
    "user_id": "cephtester",
    "display_name": "cephtester",
    "email": "",
    "suspended": 0,
    "max_buckets": 1000,
    "subusers": [
      {
        "id": "cephtester:subtester",
        "permissions": "full-control"
      }
    ],
    "secret_key": "654321"
  }
  ```

- **用户权限配置 (部分)**:
  ```json
  "caps": [],
  "op_mask": "read, write, delete",
  "default_placement": "",
  "bucket_quota": {
    "enabled": false,
    "check_on_raw": false,
    "max_size": -1,
    "max_size_kb": 0,
    "max_objects": -1
  },
  "user_quota": {
    "enabled": false,
    "check_on_raw": false,
    "max_size": -1,
    "max_size_kb": 0,
    "max_objects": -1
  },
  "temp_url_keys": [],
  "type": "rgw",
  "mfa_ids": []
  ```

---

### 4) 关键场景与演示描述

- **场景 1: 集群健康检查**
  - 演示者在终端中执行 `ceph -s` 命令，屏幕显示集群健康状态为 `HEALTH_OK`，并列出 `mon`, `mgr`, `mds`, `osd`, `rgw` 等服务的运行情况，确认集群已正常启动。

- **场景 2: 网关服务验证**
  - 演示者在浏览器中访问 `http://10.10.20.11:7480`，页面返回 XML 格式的响应，表明 Swift 网关服务已成功启动并对外提供服务。

- **场景 3: 创建管理用户**
  - 在终端中执行 `radosgw-admin user create` 命令，创建主用户 `cephtester` 和子用户 `mgruser`，并展示返回的 JSON 结构，包含用户 ID、显示名、密钥等信息。

- **场景 4: 配置 Dashboard**
  - 演示者通过 `ceph dashboard set-rgw-api-access-key` 和 `ceph dashboard set-rgw-api-secret-key` 命令，将生成的 API 密钥配置到 Ceph Dashboard。
  - 随后，演示者打开浏览器访问 `http://10.10.20.11:18843`，进入 Ceph Dashboard 管理界面，展示已创建的两个用户 `cephtester` 和 `mgruser`。

- **场景 5: API 调用准备**
  - 屏幕切换到 `ceph-demo` 工程的目录结构，演示者准备修改 Java 代码，以使用之前配置的 Swift API 密钥进行对象存储操作。

---
