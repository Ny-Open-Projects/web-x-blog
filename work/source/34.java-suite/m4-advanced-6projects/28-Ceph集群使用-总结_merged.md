# 28-Ceph集群使用-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对第三章Safe的集群使用做个回顾和总结

首先咱们看一下本章的学习目标

在这里我们要了解Safe的基本用法

着重掌握Safe和项目的集成使用

必须要了解它相关的API操作

因为Safe它是作为集群模式去运用的

所以我们不能通过单节点方式运作

必须要把集群搭建好

但是这一块配置来讲会比较复杂

刚才也带着大家做了一个详细讲解

本章的话可以不要求掌握Safe集群

可以作为额外的一个知识点

大家有能力或者有兴趣的话

可以再去掌握Safe的一个搭建和安装

那么我们侧重点是在于Safe的一个使用

必须要掌握好Safe的基本的API接口操作

以及跟我们项目的集成配置

好这一块是我们本章所要学习的重点

那咱们来回顾一下整个的学习讲解步骤

首先的话咱们介绍了部署的一个结构

规划了三个虚拟机节点11 12 13

去实现了Safe集群的创建

那11的话既可以作为子节点又作为管理节点

这个就是我们的主要操作节点

然后我们在安装集群之前

首先做了系统的一个配置

那么我们先来看一下

那么系统配置的准备工作要做哪些呢

要去修改它的主题名称

还有它的样母源

以及它的NTP时间同步工具

这一块要确保安装好

接着的话咱们实现了免密码的SSH登录方式

因为Safe它有很多个节点

对不对

它们内部之间的话要进行一个通讯

所以我们要把它免密码SSH登录方式配置好

接着的话咱们讲解了Safe具体如何去

搭建

它在这里面集群搭建有哪些过程和步骤

这个大家可以详细看讲义去做研究和学习

再往下面就是Safe的管理后台的安装

在这个管理后台

它是一个模块

这个模块来讲

就是通过对应的命令就能实现它的安装和管理

那我们可以看到它配置一些密钥信息

对不对

然后怎么去启动呢

直接Enable对应的模块

就可以了

接着的话

就是它的一个管理后台的配置信息

比如像IPR Port

ATTPS等等

接着的话

咱们创建了一个Safe FS对不对

因为集群创建完成之后

它并没有一个完整的文件系统

所以咱们必须要创建一个Safe FS

它才能够支持我们对外部的调用

这样才能存储客户端所发送传递过来的文件信息

这个是Safe FS文件系统的一个作用

咱们通过客户端进行了连接验证

这个是采用直连的方式

Redos进行了一个操作

在我们之前讲解Safe整体设计的时候

给大家讲解了

对不对

像Safe有可以支持应用的直接访问

这个就是直接操作Redos对象

还可以支持Swift的API网关

通过Redos GW进行这样一个访问操作

在这一块

我们后面项目的实际运用当中

还会做深入的学习和讲解

回到这里

再往下面

咱们就进行了Safe的项目集成的搭建和使用

在这一块

咱们是提供了Safe的Operate API接口

实现了像Safe的集群常用的一些文件操作功能

比如说文件的上传下载目录的查看等等

最后

咱们就对整个项目做了一个启动和验证

最主要的话

就是去验证整个集群的文件上传和下载功能是否正常

对不对

那么通过我们的演示

大家的话也是可以看到整个集群的这种操作和使用

都是能够OK正常运行的

这个就是我们本章内容的一个回顾

最后咱们再总结一下

在这一章当中

咱们最主要是要掌握Safe的用法

以及和项目的集成使用

因为Safe集群安装配置比较复杂

如果不能掌握

这个也没有关系

可以作为额外的一些拓展的知识点去作为学习

那么我们如果是后面有时间

可以做一个专题去专门讲解这个更详细的搭建

比如说针对于Dock

它怎么去实现这一块的集群搭建和配置

这里我们只要掌握Safe的集成和使用就可以了

给后面项目运用去做好一个基础的铺垫

因为在后面课程当中

我们还会对其使用做一个详细的介绍

这个时候就会融入我们的项目业务

去做具体功能的实现

我们就不再通过这种方式去做一个简单的验证了

而是通过Safe的API来进行一个操作使用

后面章节当中会做深入的讲解和介绍

那就是讲解了

Safe Swift API的操作使用

在项目当中该怎么去集成和配置

好

这个就是对第三章内容的回顾和总结

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程主要讲解了如何在项目中集成和使用 Ceph 分布式存储系统，特别是通过 Java 语言（Rados Java API）进行操作。课程内容分为两大部分：第一部分是 Ceph 集群的部署与配置，包括系统环境准备、SSH 免密登录、安装管理后台（Dashboard）等；第二部分是 Ceph 与项目的集成，演示了如何在 Spring Boot 项目中使用 Rados Java API 实现文件的上传和下载功能。课程强调，对于初学者，可以先掌握 Ceph 的集成使用，后续再深入学习其底层架构和更复杂的配置。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，显示课程大纲，当前章节为“第3章 Ceph集群使用”。
*   **00:00:05 - 00:00:15**：讲解“3.1 部署结构”，展示了一个包含管理节点（node1）和子节点（osd.1）的虚拟机部署拓扑图。
*   **00:00:15 - 00:00:30**：讲解“3.2 系统配置”，包括修改主机名和编辑 `/etc/hosts` 文件。
*   **00:00:30 - 00:00:45**：讲解“3.3 免密码SSH登陆”，演示创建 `ceph_user` 用户并配置 sudo 权限。
*   **00:00:45 - 00:01:00**：讲解“3.5 安装管理后台”，演示启用 dashboard 模块、生成自签名证书、创建目录和设置 IP/PORT。
*   **00:01:00 - 00:01:15**：讲解“3.4 Ceph整体设计”，展示一个包含 Rados、RADOSGW、LIBRBD、MDS 等组件的架构图。
*   **00:01:15 - 00:01:30**：讲解“3.8 Ceph与项目集成使用”，展示一个 Spring Boot 项目的目录结构。
*   **00:01:30 - 00:01:45**：展示 `CephDemoApplication` 启动类的 Java 代码。
*   **00:01:45 - 00:02:00**：展示 `CephOperator` 类中的文件操作方法，如 `delDir`, `renameDir`, `delFile`。
*   **00:02:00 - 00:02:15**：展示 `pom.xml` 文件中的 Maven 依赖，包括 Spring Boot、Rados Java API 和 Cephfs 文件系统依赖。
*   **00:02:15 - 00:02:30**：演示文件上传和下载的命令行操作。
*   **00:02:30 - 00:02:45**：展示 Maven 依赖的部署命令，用于将 Rados Java API 上传到 Maven 仓库。
*   **00:02:45 - 00:03:00**：视频结尾，显示“4. 总结”部分，回顾课程重点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   **部署结构图**：展示了一个由管理节点（node1）和子节点（osd.1）组成的 Ceph 集群拓扑。
    *   **Ceph整体设计图**：一个流程图，展示了应用通过不同接口（RADOS、S3、librbd、MDS）与 Ceph 存储系统交互的架构。
*   **代码**：
    *   **Java 代码**：
        ```java
        @SpringBootApplication
        public class CephDemoApplication {
            public static void main(String[] args) {
                // 启动应用
            }
        }
        ```
        ```java
        public void delDir(String path) throws IOException {
            mount.rmdir(path);
        }
        public void renamedir(String oldName, String newName) throws IOException {
            mount.rename(oldName, newName);
        }
        public void delFile(String path) throws IOException {
            mount.unlink(path);
        }
        ```
    *   **Shell 命令**：
        ```bash
        # 修改主机名
        [root@CENTOS7-1 ~]# vi /etc/hostname
        # 编辑 hosts 文件
        10.10.20.11 CENTOS7-1
        10.10.20.12 CENTOS7-2
        # 创建用户并设置密码
        useradd -d /home/ceph_user -m ceph_user
        passwd ceph_user
        # 设置 sudo 权限
        echo "ceph_user ALL = (root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers
        # 启用 dashboard 模块
        ceph mgr module enable dashboard
        # 生成自签名证书
        openssl req -new -nodes -x509 -subj "/O=IT/CN=ceph-mgr-dashboard" -days 3650 -keyout dashboard.key -out dashboard.crt -extensions v3_ca
        # 设置 IP 和 PORT
        ceph config set mgr mgr/dashboard/server_addr 10.10.20.11
        ceph config set mgr mgr/dashboard/server_port 18843
        # 上传文件
        [root@CENTOS7-1 sources]# java -jar ceph-demo.jar upload upload.txt
        # 下载文件
        [root@CENTOS7-1 sources]# java -jar ceph-demo.jar download upload.txt
        ```
    *   **Maven 依赖 (POM.xml)**：
        ```xml
        <dependencies>
            <!-- Spring Boot 依赖 -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
            <!-- Rados Java API 依赖 -->
            <dependency>
                <groupId>com.ceph</groupId>
                <artifactId>rados</artifactId>
                <version>0.6.0</version>
            </dependency>
            <!-- Cephfs 文件系统依赖 -->
            <dependency>
                <groupId>com.ceph</groupId>
                <artifactId>cephfs</artifactId>
                <version>0.6.0</version>
            </dependency>
        </dependencies>
        ```
    *   **Maven 部署命令**：
        ```bash
        mvn deploy:deploy-file -DgroupId=com.ceph -DartifactId=rados -Dversion=2.0.1 -Dpackaging=jar -Dfile=d:/TestCode/rados-0.6.0-SNAPSHOT.jar -url=http://192.168.19.102:8082/repository/maven-releases/ -DrepositoryId=nexus-releases
        ```

---

### 4) 关键场景与演示描述

*   **场景一：部署结构演示** (00:00:05)
    *   讲师在屏幕上展示了一个简单的 Ceph 集群拓扑图，其中包含一个管理节点 `node1` 和一个子节点 `osd.1`。这为后续的安装和配置工作提供了物理环境的参考。
*   **场景二：系统配置演示** (00:00:15)
    *   讲师演示了如何在三台虚拟机上进行系统配置，包括修改主机名和编辑 `/etc/hosts` 文件，以确保节点间能够通过 IP 地址和主机名互相访问。
*   **场景三：免密码 SSH 登录配置** (00:00:30)
    *   讲师演示了如何创建一个名为 `ceph_user` 的专用用户，并配置其 sudo 权限，以便后续的安装和管理操作可以通过 SSH 无密码执行。
*   **场景四：安装管理后台** (00:00:45)
    *   讲师演示了如何启用 Ceph 的管理后台（Dashboard）模块，生成自签名证书，创建必要的目录，并设置监听的 IP 地址和端口（18843），以便通过浏览器访问。
*   **场景五：Ceph 整体设计图解** (00:01:00)
    *   讲师展示了一张 Ceph 的整体架构图，清晰地说明了应用如何通过不同的接口（RADOS、S3、librbd、MDS）与 Ceph 存储系统进行交互，帮助理解 Ceph 的核心组件和数据流向。
*   **场景六：项目集成演示** (00:01:30)
    *   讲师展示了如何在 Spring Boot 项目中集成
