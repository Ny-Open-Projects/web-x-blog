# 26-Ceph集群使用-Ceph与项目的集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们开始学习Safe和项目的集成使用

上一讲咱们讲解了客户端采用Ledos方式指点

进行对Safe进行的操作

那么Safe在这里怎么和项目进行一个集成

要做哪些配置

如何去调用呢

好

那么我们就带着大家手把手来操作一遍

首先打开我们的支流股

服务工程

在下面的话我们创建一个服务模块

这种模块呢

就专门用于Safe的测试

然后点击Next

Safe

Demo

然后点击Next

Finish

这样呢就创建了一个新的模块

叫Safe Demo

我们让它导入生效

然后在那个Mave项目当中

让它禁止忽略

因为之前的话已经是做过测试了

然后的话呢

我们就来看看

我们在POM当中加入必要的依赖

这依赖呢

我们来具体查看一下

主要加入哪些依赖呢

在这里首先是Spring Boot的依赖

这个呢是基础性的

然后呢是LeadOS Java API的依赖

因为的话呢

我们最终还是要通过什么LeadOS来进行Safe的相关操作

然后下面的话呢

是Safe FS的文件系统

这块的话呢

相当就是通过Java API的文件系统

然后下面的话呢

就是Java的形式做了一个封装

对不对

那我们呢就来看一下

在Java这块怎么去实现它的一个调用呢

接着的话呢

咱们再去创建了它的一个运行测试内

我们就直接创建一个包吧

New Package

这个Package叫com.idcast.save.demo

我们在

创建完成之后呢

再创建两个指幕

目录Open in Terminal

Make

dir

一个的话呢

是专门负责Safe的接口操作实现

另外的一个目录呢

就是我们的启动内目录

好

创建完成之后刷新

在下面的话呢

已经看到两个目录

我们再去创建它的启动内

New Class

然后是Save Demo Application

这个呢

是我们Safe的一个启动配置内

在上面呢

就要加上对应的诸简

Spring Boot Application

作为Spring Boot服务启动

然后呢

Compand Skin基础的扫描

对不对

然后Base Package

在这里呢

就扫描我们的基础包

com.idcast

然后呢

给它一个启动方法

VM

然后呢

Spring Application.run

Save Demo Application.Cast

然后呢

Args参数

好

接着的话呢

我们要去提供它对应的实现

对不对

这个实现的话呢

咱们先不着急去调用

先要去封装对应Safe的API操作接口

对不对

你必须要把这个封装好

才能进行调用

那么咱们再去创建一个内

这个内的话呢

就是Save Operator

Operator

专门去负责对Safe进行的操作

在这里我们该怎么去实现

一个是Safe Operator

一个正常的文件操作呢

要包括它的下载

还有它的上传

还可能有目录的一些操作

比如说我要创建一个目录

修改目录

删除目录等等

对不对

这样的话呢

就会涉及到很多的文件操作接口

那这样

我们在这里面的话呢

直接将对代码拖过来

然后呢

再做一个详细讲解

咱们呢

就把

这个Safe Operator

直接引用到工程当中

因为手动敲起来的话

会很花时间啊

咱们来看一下

在这里呢

我们可以看到

它已经全部自动导入完成

没有报错

那么看它具体是什么意思呢

在上面的话呢

是Safe的配置信息

这些的话呢

就是Safe连接配置信息

我们要给它赋予User Name

对不对

还有它的一个Mount

这个Mount的话呢

是Safe的一个操作对象

它呢

会去加载你对应的用户信息

然后的话呢

在Mount里面的话呢

还要去设置它对应的配置

有哪些配置的话呢

以后呢

有哪些配置

比如说有Mount Host

就是你的Mount的连接节点

这个呢

就是Safe的连接IP和端口

然后下面的话呢

就是它的User Key

你用户的连接密钥

这个呢

就在构造的时候

会进行一个初始发

来

构造方法

初始发Safe的配置

再往下面的话呢

咱们可以看到

有查看目录的接口

对不对

查看目录怎么做呢

因为我们

在上面做了一个初始发

对不对

做了初始发之后呢

它就会去初始发这个Mount对象

拿到Mount对象之后呢

咱们就可以进行一个目录的查询

比如说我要查询某个Path下面的

它有哪些文件

对不对

就可以了

经过这个方法来进行调用

比如说我要新建一个目录

这个新建目录怎么做呢

同样通过Mount对象进行一个操作

然后Make DIRS

这个呢

都比较直观对不对

创建目录的意思

然后呢

这个是什么意思呢

这个是代表它的一个权限

就是你的一个模式

权限的一个模式

然后的话呢

删除目录

这个删除目录的话

要指定它的一个Path路径

对不对

这边是从命名

这个是删除文件

咱们重点来看一下上传和下载

这个呢

是它的一个上传对不对

上传的话呢

我们看一下这块是怎么实现的呢

首先的话呢

它会去判断这个Mount对象是否初始发成功

对不对

如果都没初始发成功

那接下来这些事情

就不用再干了

就直接返回

那再往下面看的就是文件的一个定义

文件定义的话呢

比如说你要上传一个具体的文件

对不对

你要给它这个文件的

比如说文件名称

文件长度

上传的大小

等等

接下来的话

就要给它一个IO流的一个操作

那在下面呢

就要去获取本地的文件信息

看到没有

去读取

对吧

那读取到文件信息之后的话呢

会把它转换成为一个File Import Stream

文件流

那拿到文件流之后的话呢

会做对应的一个判断

判断这个目录

判断这个文件的它是否存在

对不对

然后呢

在这里面的话可以看到

它做了一个便利

对吧

然后做了这个文件的对比

好

如果说文件不存在

那我们怎么做呢

这个呢

是文件存在

文件不存在了

那很显然我们呢

就要去新增一个文件

对不对

怎么去新增呢

同样是通过这个Mount对象

可以看到这个Mount的话呢

是一个非常重要的对象

对不对

所有的这些API操作呢

都是通过这个Mount去实现的

那么的话呢

会去标识

你是要做一个什么指令

就是创建

然后呢

要给它一个授权

对不对

是只读呢

还是只写

等等

这些呢

都可以做一个灵活的配置

接下来的话呢

就开始进行传输

开始使它的全传输

开始进行传输

那传输的时候呢

咱们可以看到

它就是通过

自截流的方式呢

进行一个读取和操作

然后呢

去传递

传递的话呢

缓冲区大小是

1024

那么就不断的去上传

对不对

会有一个进度条

会跟踪它的一个进度

百分比

然后会输出呢

它目前的上传的一个进度

在这里面的话呢

你输不输出都没关系

不过说

要更人性化一点

交互更好一点的话呢

输出起来

就是稍微会

相对来讲

更直观一点

那么我们最后呢

上传完成之后

它呢

就会退出整个循环

对吧

然后呢

是输出一个日子

说明了

我现在是在

在这个日子中呢

这条文件传输成功

最后呢

然后会去修改

它的一个权限

当然这个权限的话呢

根据咱们需要

去做对应的配置

到底是只读呢

还是只写

还是读写都可以

最后呢

不要忘记了

要对这个monitor呢

对象呢

做一个close

close什么呢

close fd这个对象

fd这个对象是什么呢

因为打开的是一个文件

对不对

我们在文件操作的时候呢

为了防止这种

出现的内存泄露

等相关的问题

或者说一些流

没有关闭

导致呢

fd文件描述服的

这种占用

然后呢

进而去占用

更多系统资源的问题呢

那么我们一般

要对它的资源

进行一个释放

看到没有

fis也要进行close释放

那下面的话呢

就是文件存在

那文件存在的话呢

怎么说呢

它去获取你的文件长度

因为你已经存在了嘛

对不对

肯定会有一个文件的

长度大小

那么拿到这个长度大小呢

接着的话呢

它又去开始传输

在这里呢

它有个特点

就是可以支持什么

可以支持断点续传嘛

也就是说

在这里面

如果你想支持断点续传的话呢

你必须要拿到

你之前所传递的一个大小

对不对

比如说你之前的话呢

上传的一个文件

那么你传到60%的时候呢

突然这个话呢

就终止了

那么终止的时候的话呢

它的长度

就其实是已经传了多少

60%了

对吧

那么你拿到这个position大小

比如说总共是100个字元

那么60%呢

就是第60个字前

长度呢也是60

对不对

那么你就从60开始

进行一个上传

好

接着的话呢

还是流逝的一个

输出

输出的一个输出

对不对

进行一个上传

那么上传的话呢

也会输出它的一个百分比

当然

在这里

你不进行一个断点续传

那么就是重新覆盖

重新的进行一个上传

多次上传的话呢

如果是进行这样断点续传的话呢

它就会

实现文件的一个最佳

文件的一个最佳传输更新

那么的话呢

最后会去修改它的一个权限

最后呢

不要忘记了

要释放文件的这种操作资源

这个呢

就是文件的一个

上传处理的流程

那咱们再来看一下文件的下载呢

对不对

文件下载呢

是通过download file bypass

这个呢

其实跟文件上传呢

都是比较类似的

只不过呢

它是要根据指定路径

去save集群上面下载一个文件

对不对

好

那它下载的一个流程的话呢

同样要去指定你的一个文件信息

咱们来看一下

它主要的参数是什么

它的参数呢

一个是failpass

一个是failname

对不对

也就是说要下载文件到我们的指定路径

下载文件到指定路径呢

因为这个save

它是一个用户和桶的方式进行的一个存储

也就是说这个save

比如说这是一个用户

对不对

然后呢

它下面要去存放一个文件

怎么去存放呢

它要去找到它的bucket

bucket

相当于就是一个桶啊

一个容器

那么呢

拿到这个容器之后呢

它再去存储对应的文件

那这个文件的话呢

就是file id

就是文件的唯一标识

如果说我有多个文件怎么办呢

就是会有多个的方式进行一个存储

那它的桶的话呢

会有多个桶

一个用户下面它会有多个桶

那大家的话呢

就可以明白

之前的话呢

咱们都是在Linux下面

比如说我要去存储一个文件

会给它一个路径

对不对

user

local

然后呢

再是我们的一个file

名称

比如说是一个文本

它就会指定的路径进行一个保存

在这里呢

它是指定你是在哪个用户

然后呢

连接的是哪个bucket

最后的话呢

就是存储在这下面

这个呢

是save的一个存储结构

那咱们再来看一下

就是针对于下载这一块呢

因为我们是要把文件下载到本地

对不对

所以呢

你要给一个file的pass

file pass呢

咱们可以看到

跟file name进行了一个组合

就是拼接

最终呢

组成了一个完整的路径

那完整路径呢

就开始进行save的一个下载

那么话呢

它要去获取呢

它对应的一些状态信息

状态统计信息

对不对

接着的话呢

就要去判断这个file name

同样它也可以支持锻炼去传

只要咱们呢

去做对应处理就可以了

要去做对应的那个标记

那么下载文件的话呢

也是采用这种流的方式进行一个传输

那么传输的时候的话呢

通过这种file out

other put stream

一个文件流进行一个输出

输出的时候的话

会做对应的记录

它也是通过这个字节流方式

做了一个传输记录

那这里的话呢

就是它的一些处理的细节

就比如说你这边download

是不是download完成了

对不对

如果说没有download

没有download完成

那么它会输出对应的进度条

最后的话呢

就是对整个文件资源的一个示范

这个呢

就是整体的一个配置

整体那个save API的

它的接口的封装

以及呢

它对应的一些连接信息的配置

save operator

那咱们来看一下save

demo application

它怎么去调用呢

在下面咱们去将save demo application

做一个代码的引用实现

这个呢是在上面

我们将这个代码呢copy一下

然后呢在这里替换

那咱们来看一下

整个流程

这个流程来讲呢

也比较简单

它怎么做呢

你的连接配置信息

对不对

接着的话呢

就是开始进行save operator的一个调用

那么我们就主要是通过两个指令

一个指令呢

upload代表呢

就是要进行文件上传

另外一个指令呢

download就代表进行下载

好

这个呢

就是它的一个启动内的实现逻辑

好

接下来呢

咱们就可以呢

根据这个工程的代码实现

去做一个启动和验证

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `ceph-demo` 的 Java 项目，旨在演示如何在 Spring Boot 应用中集成 Ceph 文件系统。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目结构、Maven 依赖配置、核心业务逻辑（`CephOperator` 类）以及如何通过命令行参数实现文件的上传和下载功能。整个过程强调了如何利用 Ceph 的 Java SDK (`rados` 和 `libcephfs`) 来操作分布式存储，为后续的微服务架构（如与 Nacos 集成）打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目目录结构和 POM 文件。
*   **00:05 - 00:15**: 介绍项目 `ceph-demo` 的 Maven 依赖，包括 Spring Boot Web、Rados Java API 和 CephFS 文件系统依赖。
*   **00:15 - 00:25**: 展示 `CephDemoApplication` 主类，演示 Spring Boot 的启动方式。
*   **00:25 - 00:35**: 介绍核心业务类 `CephOperator`，展示其构造函数和初始化 CephMount 的逻辑。
*   **00:35 - 00:45**: 进入 `CephOperator` 类的 `uploadFile` 方法，演示如何读取本地文件并写入 Ceph。
*   **00:45 - 00:55**: 展示 `downloadFile` 方法，演示如何从 Ceph 读取文件并写入本地。
*   **00:55 - 01:05**: 回到 `CephDemoApplication` 的 `main` 方法，演示如何根据命令行参数调用 `upload` 或 `download` 功能。
*   **01:05 - 01:15**: 课程总结，强调了 Ceph 与 Spring Boot 集成的关键点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **POM 文件配置** (在多个时间点展示，如 00:05, 00:15, 00:25):
    ```xml
    <dependencies>
        <!-- Spring Boot 依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Rados Java Api 依赖 -->
        <dependency>
            <groupId>com.ceph</groupId>
            <artifactId>rados</artifactId>
            <version>0.6.0</version>
        </dependency>

        <!-- Cephfs 文件系统依赖 -->
        <dependency>
            <groupId>com.ceph</groupId>
            <artifactId>libcephfs</artifactId>
            <version>0.80.5</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

*   **`CephDemoApplication.java` 主类** (00:15, 01:05):
    ```java
    @SpringBootApplication(
        basePackages = "com.ictast"
    )
    public class CephDemoApplication {
        public static void main(String[] args) {
            SpringApplication.run(CephDemoApplication.class, args);
        }
    }
    ```

*   **`CephOperator.java` 核心类** (00:25, 00:35, 00:45, 00:55):
    *   **构造函数**:
        ```java
        public CephOperator(String username, String monIp, String userKey, String mountPath) {
            this.username = username;
            this.monIp = monIp;
            this.userKey = userKey;
            this.mount = new CephMount(username);
            this.mount.confSet(option: "mon host", monIp);
        }
        ```

    *   **`uploadFile` 方法** (00:35, 00:45):
        ```java
        // ... 获取文件信息 ...
        try {
            fis = new FileInputStream(file);
            // ... 检查目录是否存在 ...
            if (!fileExist) {
                // 创建目录
                this.mount.mkdir(dirName, CephMount.O_CREAT);
            }
            // 打开文件
            int fd = this.mount.open(fileName, CephMount.O_RDWR, mode: 0);
            // 读取并写入
            byte[] bytes = new byte[1024];
            while ((length = fis.read(bytes, 0, bytes.length)) != -1) {
                this.mount.write(fd, bytes, length, uploadedLength);
                uploadedLength += length;
            }
            // 计算并输出传输速率
            float rate = (float) uploadedLength * 100 / (float) fileLength;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        ```

    *   **`downloadFile` 方法** (00:45, 00:55):
        ```java
        // ... 获取文件信息 ...
        try {
            // 打开 Ceph 文件
            int fd = this.mount.open(fileName, CephMount.O_RDONLY, mode: 0);
            // 打开本地文件
            fos = new FileOutputStream(file);
            // 读取并写入
            while ((fileLength - downloadedLength) >= length && (this.mount.read(fd, bytes, length) != -1)) {
                fos.write(bytes, 0, length);
                fos.flush();
                downloadedLength += (long) length;
            }
            // 计算并输出传输速率
            rate = (int) rate * "%";
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        ```

*   **`main` 方法中的命令行参数处理** (01:05):
    ```java
    public static void main(String[] args) {
        System.out.println("start...");
        String username = "admin";
        String monIp = "10.20.11.6789:10.20.12.6789:10.20.13.6789";
        String userKey = "AQGByDmVhBRAA..."; // 省略部分
        String mountPath = "/";
        CephOperator cephOperator = null;
        try {
            String opt = (args == null || args.length < 1) ? args[0] : args[0];
            if ("upload".equals(opt)) {
                cephOperator.uploadFileByPath(filePath, "/temp_upload_fs", args[1]);
            } else if ("download".equals(opt)) {
                cephOperator.downloadFileByPath(filePath, "/temp_download_fs", args[1]);
            } else {
                System.out.println("Unrecognized Command! Usage: opt [upload|download]");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理 (00:05-00:15)**
    讲师首先展示了项目 `ceph-demo` 的目录结构，然后重点讲解了 `pom.xml` 文件中的依赖配置。他通过高亮显示的方式，逐一解释了 Spring Boot Web、Rados Java API 和 CephFS 文件系统依赖的作用，强调了这些依赖是项目能够与 Ceph 交互的基础。

*   **场景二：核心业务类 `CephOperator` 的实现 (00:25-00:45)**
    讲师切换到 `CephOperator.java` 文件，演示了如何创建一个 `CephOperator` 实例。他详细讲解了构造函数中如何初始化 `CephMount` 对象，并设置 Ceph 的监控节点地址（`monIp`）。随后，他展示了 `uploadFile` 方法的实现，重点讲解了如何使用 `CephMount` 的 `mkdir`、`open` 和 `write` 方法来完成文件上传操作。

*   **场景三：文件下载功能实现 (00:45-00:55)**
    讲师接着演示了 `downloadFile` 方法。他解释了如何使用 `CephMount` 的 `open` 方法打开 Ceph 上的文件，然后通过 `read` 方法读取数据，并写入到本地文件中。他特别强调了在读取过程中需要处理文件长度和传输速率的计算。

*   **场景四：命令行参数驱动的应用 (01:05)**
    讲师回到 `CephDemoApplication` 的 `main` 方法，演示了如何通过命令行参数来控制程序行为。他展示了如何根据传入的 `upload` 或 `download` 参数，调用相应的业务方法。这体现了程序的灵活性和可扩展性。

*   **场景五：代码调试与分析 (00:35-00
