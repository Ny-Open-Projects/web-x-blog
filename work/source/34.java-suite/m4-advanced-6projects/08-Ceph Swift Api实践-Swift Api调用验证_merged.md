# 08-Ceph Swift Api实践-Swift Api调用验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们继续实现save Swift API的封装调用

那么咱们去修改save demo application的启动类

在这里我们要增加一个方法实现对Swift API的调用

在下面我们添加对应的方法

将异常抛出来

那咱们来看一下怎么去实现Swift API的调用验证

首先第一步

咱们要列出打印列出用户的所有容器信息

第二步咱们就来上传指定的文件

验证文件上传接口

咱们就从save去下载刚才所上传的文件

保存在指定的路径下面

这个就是save的一个调用验证处理流程

我们就来做具体实现

通过Spring的

application context去获取它的上下文

传递当前的内容

拿到上下文之后

咱们就来获取Swift的操作对象

这是咱们之前所封装的Swift operator

通过上下文去获取

传递了Swift operator class

好

那么咱们就可以将它的对象的用户下面的所有容器

全部列出来ist container

在这个方法里面它会进行打印

接着咱们就来实现了文件的上传

首先去定义一个object name

这个是在save上面的文件名称标识

我们叫test save

然后我们就通过封装的class的对象

进行文件的上传

这里我们要传递一个路径

这个路径的话

大家可以根据

这个路径的话

自己本地的目录去指定对应的路径

我们就放在Swift

放在D盘下面

文件名称就叫test-swift-save-txt文件

然后我们再去实现文件的下载功能

同样通过Swift operator封装的对象

然后调用下载的接口功能

传递了object name

相当的保存在D盘下面

名称就叫test-txt

最后我们再输出一个日志

提示处理完成

好

这个就是整体的测试验证流程

加上对应的注释

通过Swift的方式去操作Swift集群

接着咱们就来看一下

具体的测试验证思路是怎样的

我们会在D盘上面去做一个测试

去创建一个文件

并让它上传到save系统当中

然后我们再从save系统当中去下载

将这个文件下载到指定路径下面

这里咱们要注意一下

我们默认的容器配置的名称是叫

usedatainfo

看一下

找到swift operator

在这里面搜索

我们默认的容器存储名称

就是叫usedatainfo

从save系统上传和下载的文件名称上去

进行的要保持一致

这个容器也是要一致的

之后会通过打印complete

如果执行到这里

说明了没有异常

代表了就是执行成功

最后我们还会去验证了这个文件信息是否正确

这里我们就来做一个演示

我们修改启动列

在这里我们将启动的方法改成了Swift API

这个流程

刚才我们做了讲解

我们要在第一盘上面去创建一个test-swift-txt的文本

我们给他创建一些内容

在第一盘下面

test-swift-save-txt

我们给他编辑下

内容我们随便给他输入一些

123 test

再输入两行abc test

好保存

然后我们去验证一下

上传功能和下载功能

是否能够正常运行

连接信息

这个要注意

不要填写错误

确保连接处处划是正常的

那咱们呢

启动服务做个测试验证

我们可以看到的结果已经运行完成

输出了complete的提示信息

对吧

咱们可以看到最后面的咱们是输出complete

那么我们来验证一下数据这块呢

是否正常了

我们打开一盘

因为目标呢

是放在一盘下面

txtxt文件

对不对

可以看到生成了一个testtxt文件

那咱们来看一下它的内容呢

是否我们刚才所输入的内容是一致呢

我们点击查看

可以看到这个内容的话呢

都是一模一样的

对不对

也就是说我们通过save对文件进行上传和下载呢

都能够正常实现

在这里呢

就是

对save的API的集成和调用验证

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个关于 **Ceph Swift API 调用与集成** 的实践教学。讲师通过 IntelliJ IDEA 开发环境，演示了一个名为 `CephDemoApplication` 的 Spring Boot 项目，该应用旨在实现对 Ceph 存储系统的文件上传与下载功能。课程内容聚焦于如何在 Java 项目中集成 Ceph Swift API，包括配置认证信息、创建容器、上传文件和下载文件等核心操作。讲师通过代码演示和注释说明，清晰地展示了 API 的使用方法和关键步骤。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 文档中展示课程大纲，明确本节内容为“Ceph Swift Api 调用验证”。
*   **00:00:05 - 00:00:15**：讲师切换到 IntelliJ IDEA，展示项目结构和 `CephDemoApplication` 启动类的代码，介绍项目整体框架。
*   **00:00:15 - 00:00:30**：讲师在 `CephDemoApplication` 类中，通过 `SpringApplication.run()` 方法启动 Spring 应用，并获取 `SwiftOperator` 实例。
*   **00:00:30 - 00:00:45**：讲师在 `swiftApi` 方法中，调用 `swiftOperator.listContainer()` 列出容器，演示了如何获取容器列表。
*   **00:00:45 - 00:01:00**：讲师演示文件上传功能，调用 `swiftOperator.createObject()` 方法，将本地文件上传到 Ceph。
*   **00:01:00 - 00:01:15**：讲师演示文件下载功能，调用 `swiftOperator.retrieveObject()` 方法，将 Ceph 中的文件下载到本地。
*   **00:01:15 - 00:01:30**：讲师切换到 Sublime Text，展示本地文件 `test_swift_ceph.txt`，并说明该文件是上传后下载的文件，内容与本地文件一致，证明操作成功。
*   **00:01:30 - 00:01:45**：讲师回到 Typora 文档，总结本节内容，强调 Ceph Swift API 的调用方式，并预告后续将讲解如何在项目中集成使用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **课程大纲**：包含“目标”、“步骤”、“实现”、“总结”等部分，其中“实现”部分详细列出了“Ceph Swift Api 实践说明”、“Ceph Swift Api 特点”、“Ceph RGW 介绍”、“Ceph 存储结构”、“Ceph Swift Api 服务端的配置”和“Ceph Swift Api 调用验证”等子章节。
    *   **总结页**：明确指出 Ceph 提供了多种 API 调用方式，本案例采用了兼容性较强的 Ceph Swift API，并强调在 API 调用前必须做好服务端配置。

*   **代码关键内容**：
    *   **`CephDemoApplication.java` 启动类**：
        ```java
        @SpringBootApplication
        @ComponentScan(basePackages = "com.itcast")
        public class CephDemoApplication {
            public static void main(String[] args) throws Exception {
                swiftApi();
            }
        }
        ```
    *   **`swiftApi` 方法**：
        ```java
        public static void swiftApi() throws Exception {
            // 1. 打印列出用户的所有容器信息
            ConfigurableApplicationContext appContext = SpringApplication.run(CephDemoApplication.class);
            SwiftOperator swiftOperator = appContext.getBean(SwiftOperator.class);
            swiftOperator.listContainer();

            // 2. 上传指定的文件
            String objName = "test_ceph";
            swiftOperator.createObject(objName, filePath: "d:/test_swift_ceph.txt");

            // 3. 从Ceph下载文件到指定的路径下面
            swiftOperator.retrieveObject(objName, outputPath: "e:/test.txt");
        }
        ```
    *   **`SwiftOperator` 类的配置**：
        ```java
        private String authUrl = "http://10.10.20.11:7480/auth/1.0";
        private String defaultContainerName = "user_datainfo";
        private Account account = null;
        private Container container;
        ```
    *   **`CephOperator` 类的初始化**：
        ```java
        public static void radosApi(String[] args) throws Exception {
            System.out.println("start...");
            String username = "admin";
            String monIp = "10.10.20.11:6789";
            String userKey = "AQEB..."; // 省略部分密钥
            String mountPath = "/";
            CephOperator cephOperate = new CephOperator(username, userKey, monIp, mountPath);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目启动与依赖注入**（00:00:15 - 00:00:30）
    *   讲师在 `CephDemoApplication` 的 `main` 方法中调用 `SpringApplication.run()` 启动 Spring Boot 应用。
    *   通过 `appContext.getBean(SwiftOperator.class)` 从 Spring 容器中获取 `SwiftOperator` 实例，这是后续所有操作的基础。

*   **场景二：容器列表与文件操作**（00:00:30 - 00:01:15）
    *   讲师调用 `swiftOperator.listContainer()` 方法，演示了如何列出 Ceph 中的容器。
    *   接着，讲师调用 `swiftOperator.createObject()` 方法，将本地文件 `d:/test_swift_ceph.txt` 上传到 Ceph。
    *   最后，讲师调用 `swiftOperator.retrieveObject()` 方法，将 Ceph 中的文件 `test_ceph` 下载到本地路径 `e:/test.txt`。

*   **场景三：结果验证**（00:01:15 - 00:01:30）
    *   讲师切换到 Sublime Text 编辑器，打开本地文件 `D:/test_swift_ceph.txt`。
    *   展示文件内容，确认其与上传前的文件内容一致，从而验证了上传和下载功能的成功执行。

*   **场景四：课程总结**（00:01:30 - 00:01:45）
    *   讲师回到 Typora 文档，总结本节内容，强调 Ceph Swift API 的调用方式和必要配置。
    *   预告后续课程将讲解如何在项目中集成使用 Ceph Swift API。

---

以上是根据视频画面进行的结构化技术课程分析。
