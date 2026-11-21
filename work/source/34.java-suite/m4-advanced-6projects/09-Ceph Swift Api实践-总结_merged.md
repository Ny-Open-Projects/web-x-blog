# 09-Ceph Swift Api实践-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们对第一章内容做个回顾和总结

我们首先看一下本章的学习目标

在这里我们要掌握两点

第一要掌握SWIFT API的特点

以及它底层的存储结构

这点要理解清楚

这个跟我们传统的路径式存储

是有较大的区别

第二点咱们要掌握SWIFT API的配置与使用

完成了文件的上传和下载接口的封装

被下面的项目集成使用去做好预热和铺垫

那我们回顾一下本章的讲解主要内容有哪些呢

首先我们对SWIFT API做了一个说明

讲解了它的一个特点

以及为什么要采用SWIFT API去实现文件的存储管理

因为采用LightDos的方式

这种本地化操作不便于服务的接入和使用

下面咱们去讲解了SWIFT API的具体特点

SWIFT它是由LightSpace开发的

用来为云计算提供的可货的存储项目

那么我们做了一个对比

通过我们SWIFT RGW的网关去试试兼容了SWIFT API

这样它就有较强的扩展性

能够更加灵活

功能上来讲也更为丰富了

下面我们对SWIFT RGW做了具体介绍

SWIFT的话可以提供快文件和对象的三种存储形态

那么RGW它的主要作用是干嘛

我们在这里可以看到

它能够去适配兼容AWS S3的接口

以及OpenStack SWIFT API接口

也就是本章咱们要重点学习的SWIFT API的接口

再往下面咱们对SWIFT的存储结构

做了一个讲解介绍

这个和咱们传统的路径式存储有很大的区别

这个要理解清楚

用户下面对应的是桶

桶下面的话可以对应N个文件

在文件下面就没有具体的层级

这些的话都是作为一个评级存放的

然后咱们讲解了SWIFT API服务端的具体配置

怎么去实现

在我们实现SWIFT API接口调用之前

要做哪些对应的配置

咱们要去看一看

我们要确保创建了SWIFT的用户

对不对

要用于接口的请求和认证

再往下面咱们就对SWIFT API做了一个集成封装

然后也做了一个调用和验证

封装的时候

咱们最主要去实现了SWIFT的初始化配置

然后上传的功能

下载的功能

以及列出用户下面的所有容积信息

那么最后我们启动和验证的时候

是调用SWIFT API

然后再进行一个测试

整个测试流程是怎样的

我们是进行了一个文件的上传

首先我们是进行了一个文件的创建和上传

对不对

然后再将上传的文件下载到指定的路径下面

这里可以看到整个结果的话

也是操作正常的

在这里就实现了SWIFT API的集成封装

以及整体功能的调用和验证

咱们再来总结一下

SWIFT它提供了多种的API调用方式

这里我们采用了兼容性较强的SWIFT API进行调用

了解SWIFT RGW的功能作用

在API调用之前

我们必须要做好对应的服务配置

从本章的案例当中

对SWIFT API的使用

我们要有一定的了解

接下来我们就会在项目当中去做具体的集成和使用

好

这一块也是为咱们下面的项目的学习和应用做好一个铺垫

同时加深大家对SWIFT API的一个理解和运用

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程为“交易平台 - Day 9”的一部分，主要讲解如何在 Spring Boot 项目中实践 Ceph Swift API。课程目标是掌握 Ceph Swift API 的特点与存储结构，完成文件的上传与下载接口，并为后续项目集成做准备。课程内容从 Ceph Swift API 的基本概念、Ceph RGW 介绍、存储结构，到服务端配置，最后演示了如何在 Java 项目中调用 API 进行文件上传和下载验证。课程强调了 Ceph Swift API 的兼容性、最终一致性，以及与传统文件系统（如 fs）和 RBD 的区别。

---

### 2) 按时间顺序的章节（带时间点）

由于截图未提供具体时间戳，以下章节结构基于画面内容按逻辑顺序排列：

*   **第1章 CEPH Swift Api 实践**
    *   **1.1 目标** (画面2)
        *   掌握 Ceph Swift Api 特点与存储结构。
        *   掌握 Ceph Swift Api 的配置与使用，完成文件的上传与下载接口，为下面的项目集成使用与封装做预热。
    *   **1.2 步骤** (画面2)
        *   Ceph Swift Api 实践说明。
        *   Ceph Swift Api 特点。
        *   Ceph RGW 介绍。
        *   Ceph 存储结构。
        *   Ceph Swift Api 服务端的配置。
        *   Ceph Swift Api 调用验证。
    *   **1.3 实现**
        *   **3.1 Ceph Swift Api 实践说明** (画面3)
            *   介绍 Ceph 与 Ceph Swift API 的背景，指出 fs 和 RBD 在互联网大规模场景下的不足，引出使用 Ceph Swift API 的必要性。
        *   **3.2 Ceph Swift Api 特点** (画面3)
            *   介绍 Swift 是由 Rackspace 开发的、用于云计算的开源对象存储系统。
            *   强调其 RESTful 风格 API 和最终一致性。
            *   对比 Ceph FS（POSIX 文件系统）和 RBD（块设备）。
            *   提及 Ceph RGW 作为对象存储的网关。
        *   **3.3 Ceph RGW 介绍** (画面4)
            *   解释 RGW 是提供对象存储的网关，本质上是一个 HTTP 服务器。
            *   说明其兼容 AWS S3 和 OpenStack Swift 的 API。
        *   **3.4 Ceph 存储结构** (画面5)
            *   介绍桶（Container）的概念，强调桶与对象的关系类似于文件夹与文件，但没有层级路径的概念。
            *   展示一个简单的存储结构图：用户 -> 桶1、桶2、桶n。
        *   **3.5 Ceph Swift Api 服务端的配置** (画面6)
            *   演示如何检查 Ceph 集群状态，使用 `ceph -s` 命令查看集群健康状况（`HEALTH_OK`）和各服务（mon, mgr, mds, osd）的运行情况。
        *   **3.6 Ceph Swift Api 调用验证** (画面7-11)
            *   **3.6.1 修改 ceph-demo 工程** (画面8)
                *   展示项目结构，重点是 `SwiftOperator` 类。
            *   **3.6.2 初始化配置** (画面9)
                *   代码示例：创建 `AccountConfig`，设置用户名、密码、认证 URL，并创建 `Account`。
                *   获取容器信息，如果容器不存在则创建。
            *   **3.6.3 调用验证** (画面10)
                *   在 `CephDemoApplication` 的 `main` 方法中调用 `swiftApi()` 方法。
            *   **3.6.4 测试验证** (画面11)
                *   描述测试思路：在 D 盘创建文件，上传到 Ceph，然后从 Ceph 下载。
                *   强调上传和下载的文件名称必须一致。
                *   展示 IDE 中的 `SwiftOperator` 类代码，其中包含 `upload` 和 `download` 方法。
                *   说明“无异常代表执行成功”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文本内容**:
    *   **目标**: 掌握 Ceph Swift API 特点与存储结构，完成文件上传下载接口。
    *   **步骤**: 列出了从实践说明到调用验证的六个步骤。
    *   **Ceph Swift API 特点**: 由 Rackspace 开发，RESTful 风格，最终一致性。
    *   **Ceph RGW 介绍**: 对象存储网关，兼容 AWS S3 和 OpenStack Swift API。
    *   **Ceph 存储结构**: 以桶（Container）和对象（Object）为核心，无层级路径。
    *   **总结**: Ceph 提供多种 API 调用方式，本课程采用兼容性较强的 Ceph Swift API，强调在调用前必须做好服务配置。

*   **图表**:
    *   **Ceph 存储结构图** (画面5): 一个简单的树状图，展示用户可以创建多个桶，每个桶下可以存储多个对象。

*   **代码**:
    *   **Ceph 集群状态检查命令** (画面6):
        ```bash
        [root@CENTOS7-1 ceph-cluster]# ceph -s
        cluster:
          id:    Oec99aa9-e97e-43d3-b35b-90eb21c4abff
          health: HEALTH_OK
        services:
          mon: 3 daemons, quorum CENTOS7-1,CENTOS7-2,CENTOS7-3
          mgr: fs_test-1/1 up {0=CENTOS7-1=up:active}
          mds: fs_test-1/1 up
          osd: 3 osds: 3 up, 3 in
        ```
    *   **创建 Swift 用户命令** (画面7):
        ```bash
        sudo radosgw-admin user create --subuser='cephtester:subtester' --uid='cephtester' --display-name='cephtester' --key-type=swift --secret='654321' --access=full
        ```
    *   **Java 代码 - SwiftOperator 初始化** (画面9):
        ```java
        public SwiftOperator() {
            // 1. Ceph的账户信息配置
            AccountConfig config = new AccountConfig();
            config.setUsername(username);
            config.setPassword(password);
            config.setAuthUrl(authUrl);
            config.setAuthenticationMethod(AuthenticationMethod.BASIC);
            account = new AccountFactory(config).createAccount();

            // 2. 获取容器信息
            Container newContainer = account.getContainer(defaultContainerName);
            if (!newContainer.exists()) {
                container = newContainer.create();
                log.info("container create === " + defaultContainerName);
            } else {
                container = newContainer;
            }
        }
        ```
    *   **Java 代码 - CephDemoApplication 主方法** (画面10):
        ```java
        @SpringBootApplication
        @ComponentScan(basePackages = {"com.itcast"})
        public class CephDemoApplication {
            public static void main(String[] args) throws Exception {
                // Swift Api接口调用验证
                swiftApi();
            }
        }
        ```
    *   **Java 代码 - SwiftOperator 上传/下载方法** (画面11):
        ```java
        // 伪代码，根据画面中的注释和逻辑推断
        public void upload(String filePath, String containerName, String objectName) {
            // 1. 获取容器
            Container container = account.getContainer(containerName);
            // 2. 上传文件
            container.upload(objectName, filePath);
        }

        public void download(String containerName, String objectName, String downloadPath) {
            // 1. 获取容器
            Container container = account.getContainer(containerName);
            // 2. 下载文件
            container.download(objectName, downloadPath);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：课程目标与步骤介绍** (画面2)
    *   讲师在 PPT 上清晰列出本章的学习目标和实现步骤，为后续内容做铺垫。

*   **场景二：Ceph 存储结构图解** (画面5)
    *   讲师展示了一个简单的示意图，用图形化的方式解释了 Ceph 对象存储的核心概念——桶和对象，以及它们之间的关系，帮助学员建立直观理解。

*   **场景三：Ceph 集群状态检查** (画面6)
    *   讲师在终端中执行 `ceph -s` 命令，向学员展示了一个健康状态为 `HEALTH_OK` 的 Ceph
