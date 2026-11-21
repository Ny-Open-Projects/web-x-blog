# 07-Ceph Swift Api实践-Swift Api封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习SWIFT API的集成调用

以及对整个功能进行测试和验证

首先咱们要去修改SWIFT demo工程

这个在之前做了讲解和实现

之前的话咱们是通过Leados Java主线实现了SWIFT调用

在这里咱们来看一下

如何去通过SWIFT的方式做个集成和调用

首先咱们去增加SWIFT Operate的接口

在这里要实现什么功能

主要去实现SWIFT连接初始化

然后文件上传的功能

下载的功能处理

以及去获取下面的所有容器信息

这个在之前讲SWIFT存储结构的时候

给大家做了介绍

用户下面对应的是有不同的桶

这个桶也就是容器

通过这个功能接口就能够查询到用户下面

到底有多少个容器

好

这一块就是SWIFT API的一个封装

咱们就来从代码方面做具体实现

找到咱们的SWIFT Demo工程

在Service下面去创建一个新的类

这个类我们就叫SWIFT Operator

创建完成之后

我们就来做代码的具体实现

首先我们加上入解Compand

作为Compand

作为一个页面

然后再加上Logbook的注解

Log4接

打印日志

然后我们首先去实现它的初始化连接配置

那么我们要定义它相关的属性

Street username

这个是它的用户名称

用户名称咱们还记不记得

在我们上个章节当中

对SWIFT的API服务端做了一个配置

那么创建了对应的用户名称

对不对

这个用户咱们也将主用户和只用户的信息都设置进去

那么咱们copy放到username当中

这个加上对应的说明

是用户的连接名称

格式的话是主用户名

再加上只用户名

下面咱们再去配置它的用户密码

这个密码和咱们创建的用户密码

这个密码和咱们创建的用户密码

是一致的

这个是用户连接的密码信息

那么我们还给它一个访问地址

这个就是SWIFT

接口访问地址

shrimp

ausurl

10.10

这是我们虚拟机地址

关口默认780

aus

采用1.0的协议

加个注释

是接口的访问地址

下面咱们再创建了

它默认的容器名称

before

container name

我们名称就给它叫用户信息

专门去存储用户相关的资料文件

好

这个是默认存储的容器名称

基本属性定义完成之后

咱们还要去定义

SWIFT账户配置信息account

然后再配置一个SWIFT的容器操作对象

我们将包导入进来

第一个加上对应的注释

这个是账户的操作对象

下面这个是SWIFT的容器操作对象

这些定义完成之后

咱们就可以进行连接的初始发配制

通过构造方法去做对应操作

又采用默认的构造方法

那么构造方法怎么去实现呢

第一步要去设置SWIFT的账户连接信息

好

我们先定义一个account

configure

接着的话去设置它的用户连接信息

usname password

接口的认证连接地址

往上来cache method

认证连接方法

上面这个报错

我们把这个方法写错了

重新修正一下

好

这个认证方法就采用基础的认证方式

Basic

然后咱们就可以创建账户配置对象

account

从它的工厂当中传递config

然后创建一个新的账户操作对象

好

下面要去获取容器信息

获取容器的操作对象

怎么去实现呢

首先咱们去定义一个container

通过account去获取它的容器

我们要传递它默认的名称

然后我们要做一个判断

判断这个容器它是否存在

如果是它不存在

我们就要去新增一个容器

要用create方法

然后将日志打印一下

这样的话

咱们就知道它新建了一个容器

便于我们的跟踪和排查

将名称打印出来

如果是它已经存在了

那我们就简单的直接将它赋予到咱们的容器操作对象当中

这样就完成了save的连接处理复制

下面咱们再去实现save的文件上传处理的接口

如何去通过save实现文件上传

其实也很简单

因为swift的API已经帮我们做了很好的封装

咱们直接拿回来使用就可以

去remote name

去定义它的远程save的文件操作对象当中

然后将去指定咱们要上传的文件信息

这个就是本地的文件路径

咱们看一下它的实现步骤

第一步是从容器当中

获取远程存储对象信息

start object

通过容器去获取一个对象

然后咱们要指定它的lim信息

就是它的唯一文件标识

接着咱们就可以执行文件的上传处理

那么怎么去调用

直接通过swift的API就能实现文件的上传

upload object

然后指定你要上传的本地文件路径

file path

将file保留进来

这样就实现了文件的上传处理

整个过程来讲也是非常简单的

只要两步通过swift的API

就能快速帮助咱们去实现

咱们给它加上一个注释

它是文件上传的处理接口

接下来咱们去实现文件的下载处理接口

同样我们要传递两个参数

一个是远程的文件对象名称

另外一个就是咱们要下载的本地路径

咱们看一下整体实现步骤是怎样

第一步咱们从

容器当中去获取远程对象信息

通过stored object

进行对应的操作

然后从容器当中去拿到对应的对象

传递了object name

这个咱们要改成小写

按照同封命名处理

第二步咱们要执行文件的下载方法

将它保存在本地路径

这样咱们就实现了文件的下载处理功能

咱们给它加上一个注释

文件的下载处理接口

最后咱们还要实现

获取用户下面的所有容器信息接口

如何去获取用户下面的所有容器信息呢

咱们仍然去通过swiftapi

去做对应的调用和实现

将list的选项连接到wavp.com

将list导入进来

定义一个list对象

这个的话就用于去记录容器信息

定义一个containers

将账户下面的所有容器列出来

然后做便利循环处理

将容器放到咱们list当中

咱们只是获取它的名称

这里拿到容器名称就可以

然后我们将日志打印出来

打印你当前所具备的容器信息

这里打印的就是容器的名称

最后将list的最终结果返回出去

这个方法就是

获取用户下面的所有容器信息

这样咱们就实现了swiftapi的封装

实现了文件的上传和下载的主要功能

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程旨在演示如何在 Java 应用程序中集成并调用 Ceph Swift API，以实现文件的上传和下载功能。讲师通过一个名为 `ceph-demo` 的 Spring Boot 项目，逐步展示了如何配置 Ceph 客户端、创建操作对象、并实现核心的上传和下载方法。视频内容覆盖了从环境检查、代码编写到关键 API 调用的完整流程，重点在于实践操作和代码细节。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 中展示课程大纲，当前章节为“3.6 Ceph Swift Api 调用验证”。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，展示 `ceph-demo` 项目的目录结构，并聚焦于 `SwiftOperator` 类。
*   **00:00:15 - 00:00:30**: 讲师在 `SwiftOperator` 类中编写代码，定义了用于连接 Ceph Swift 服务的私有变量，包括用户名、密码、认证地址和默认容器名。
*   **00:00:30 - 00:00:45**: 讲师演示如何导入 `org.javaswift.joss.model.Container` 类，并在构造函数中初始化 `AccountConfig` 对象，设置用户名和密码。
*   **00:00:45 - 00:01:00**: 讲师调用 `AccountFactory.createAccount(config)` 方法创建 `Account` 对象，并通过 `account.getContainer()` 方法获取容器操作对象。
*   **00:01:00 - 00:01:15**: 讲师编写 `createObject` 方法，用于上传文件。该方法首先通过 `container.getObject(remoteName)` 获取存储对象，然后调用 `object.uploadObject(new File(filePath))` 方法完成上传。
*   **00:01:15 - 00:01:30**: 讲师编写 `retrieveObject` 方法，用于下载文件。该方法通过 `container.getObject(objectName)` 获取存储对象，然后调用 `object.downloadObject(new File(outPath))` 方法完成下载。
*   **00:01:30 - 00:01:45**: 讲师在 `SwiftOperator` 类中添加了 `listContainers` 方法，用于获取用户下的所有容器信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.6 Ceph Swift Api 调用验证”。
    *   **章节标题**: “3.5 Ceph Swift Api 服务端的配置”。
    *   **服务端配置命令**: `ceph -s`，用于检查 Ceph 集群状态。
    *   **集群状态输出**: 显示了集群 ID、健康状态（`HEALTH_OK`）、服务（mon, mgr, mds, osd, rgw）和数据池（pools）信息。

*   **代码关键内容**:
    *   **`SwiftOperator` 类构造函数**:
        ```java
        @Component
        @Log4j2
        public class SwiftOperator {
            private String username = "admin";
            private String password = "654321";
            private String authUrl = "http://10.10.20.11:7480/auth/1.0";
            private String defaultContainerName = "user_datainfo";
            private Account account = null;
            private Container container;

            public SwiftOperator() {
                // 设置Ceph的账户配置信息
                AccountConfig config = new AccountConfig();
                config.setUsername(username);
                config.setPassword(password);
                config.setAuthUrl(authUrl);
                config.setAuthenticationMethod(AuthenticationMethod.BASTO);
                account = new AccountFactory(config).createAccount();
                container = account.getContainer(defaultContainerName);
            }
        }
        ```
    *   **`createObject` 方法**:
        ```java
        public void createObject(String remoteName, String filePath) {
            StoredObject object = container.getObject(remoteName);
            object.uploadObject(new File(filePath));
        }
        ```
    *   **`retrieveObject` 方法**:
        ```java
        public void retrieveObject(String objectName, String outPath) {
            StoredObject object = container.getObject(objectName);
            object.downloadObject(new File(outPath));
        }
        ```
    *   **`listContainers` 方法**:
        ```java
        public List<Container> listContainers() {
            return account.listContainers();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境检查与项目结构展示** (00:00:00 - 00:00:15)
    *   讲师首先在 Typora 中展示课程大纲，明确当前学习目标。
    *   随后切换到 IntelliJ IDEA，展示 `ceph-demo` 项目的目录结构，重点突出 `src/main/java/com.itcast.ceph.demo/service/SwiftOperator.java` 文件，为后续代码编写做准备。

*   **场景二：创建 SwiftOperator 类并初始化配置** (00:00:15 - 00:00:45)
    *   讲师在 `SwiftOperator` 类中定义了连接 Ceph Swift 服务所需的私有变量。
    *   讲师通过 `AccountConfig` 对象设置用户名、密码和认证地址。
    *   讲师调用 `AccountFactory.createAccount(config)` 方法创建 `Account` 对象，并通过 `account.getContainer(defaultContainerName)` 获取容器操作对象。

*   **场景三：实现文件上传功能** (00:00:45 - 00:01:15)
    *   讲师编写 `createObject` 方法。
    *   该方法首先通过 `container.getObject(remoteName)` 获取存储对象。
    *   然后调用 `object.uploadObject(new File(filePath))` 方法，将本地文件上传到远程容器中。

*   **场景四：实现文件下载功能** (00:01:15 - 00:01:30)
    *   讲师编写 `retrieveObject` 方法。
    *   该方法通过 `container.getObject(objectName)` 获取存储对象。
    *   然后调用 `object.downloadObject(new File(outPath))` 方法，将远程文件下载到本地。

*   **场景五：实现容器列表功能** (00:01:30 - 00:01:45)
    *   讲师在 `SwiftOperator` 类中添加 `listContainers` 方法。
    *   该方法调用 `account.listContainers()`，返回用户下所有容器的列表，便于管理。

通过以上步骤，讲师完整地演示了如何在 Java 应用中集成 Ceph Swift API，实现文件的上传、下载和容器管理功能。
