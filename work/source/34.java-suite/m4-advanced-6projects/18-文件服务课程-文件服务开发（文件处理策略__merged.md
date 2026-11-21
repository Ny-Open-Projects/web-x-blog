# 18-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们这个抽象的文件策略处理类呢

我们是已经都写好了

那么主要是写了两个方法对吧

一个是这个文件上传upload的方法

还有一个是文件删除也就是这个delete的方法

那么实际上呢我们这个类里边呢

还有另外两个属性呢我们可以来完善一下

虽然说当前呢咱们当前写的这些代码里面没有用到

因为后边呢我们是不是马上要开发这个类的相关的子类对吧

比如说什么呢

比如说这个local service impr

还有fast dfs service impr

还有ali service impr

在这些子类里边呢会用到副类的一些属性

所以说呢我们这个地方呢直接把它这个完善一下

那么也就是说我们当前呢

把这个类呢所用到的这些属性还有方法都提供好

那么后边的子类就直接可以拿过来用了

那么咱们这儿呢还差这么两个属性啊

我就不再手写了

直接把它拷过来

大家来看一下

这个是什么呢

一个是注入了一个这个配置属性类对吧

大家还记得吧

配置属性类叫做file server properties

好

那么对应的呢

这个配置属性类在哪呢

就是在我们这个properties啊

这个包下边就是这个file server properties

然后这里边定义的这些属性呢

跟我们的配置文件都是一一对应的

所以最终呢我们项目在启动的时候呢

就会把我们这些配置对吧

加载进来

最终封装成这么一个对象

封装成这么一个对象

file properties对象

然后咱们加了一个outware的注解对吧

就可以给我们注进来了

好

那这样的话呢

我们当前这个类的子类呢

就可以直接啊

通过这个file properties这个对象

来获得我们相关的一些配置信息了

好

然后呢我们还引入了这么一个

而这个的话并没有注入对吧

哎现在相当于只是声明

哎为什么呢

因为大家来看一下

它是在我们这个properties呢

是什么呢

是我们当前这个类里面的一个内部类对吧

好

好

oli

然后呢

这里边大家可以看到

我们是不是提供了这么多

properties类型的

那么

分别每一个代表的就是一种什么呢

文件的这个存储方案

对吧

处理策略

好

所以说呢

这个地方具体我们用的是哪一个呢

是不是只有程序运行的时候才能知道

所以说呢

我们这个地方呢

哎

这个properties对应的

到底是这个loco

还是a11

还是minio

对吧

还是七牛

还是腾讯

那么具体是哪一个

这个只有程序运行期间才能够知道

所以这个地方呢

我们是不是只是把它声明出来

然后呢

在我们具体的某个子类里面

才才能去确定它

所以说这个地方呢

只是封装一下

只是声明一下这个属性

那么这个定义好

然后接下来呢

还有一个方法呢

在我们当前这里边没有用到

那么一会儿呢

它的子类里边呢

会使用到

所以我们呢

提前也给它定义好

就是这个方法

get uri prefix

这个是获取我们下载地址前缀

咱们直接把这个方法考过来

这个我就不再手敲了

然后呢

我们可以来简单读一下这个代码

这个string utils呢

需要来导一下

咱们来看一下

那么这个是获得

首先判断一下什么呢

is not empty

对吧

properties.get uri prefix

而这个properties呢

就是我们

刚才声明的这个

对吧

那么具体它是谁

具体它是谁

是我们这个local

还是阿里

还是minio

是不是这个是需要根据我们这个配置文件

我们配置的策略去确定

那么咱们可以回到我们的配置文件来看一下

在我们配置中心里边

咱们是不是已经导入了这个pdfile server

这个配置文件

对吧

这是我们这个文件服务啊

读取的一个主要的配置文件

就是它

然后呢

大家可以看到

我们在这呢

定义了这么一个

分析文件

我们可以看到这个pdfile.type

对吧

这么一个属性

这个代表的就是我们当前这个文件服务

所使用的这个存储的类型

到底是哪些

比如说我这是不是指定的是fast.dfs

但是我们可选的有很多啊

比如还有local

对吧

还有阿里

还有minio

但是这个minio呢

我们并没有去实现啊

我们如果实现的话呢

也可以使用它

咱们课上呢

只是实现其中的三种

一个是local

一个是阿里

还有一个是fast.dfs

前面我们课程当中也提到了

如果有其他的

这个存储方案呢

你自己去实现

都是可以扩展的啊

所以呢

在这个type这个地方呢

我们定义的就是表示

我们当前这个文件服务啊

所使用的这个存储类型

到底是哪种类型

比如我这个地方

配置的是fast.dfs

当然我也可以配置local

对吧

也可以配置阿里

这都是可以的啊

那么在这个配置文件里边

比如说我们当前使用的是local

本地存储

对吧

那么这个时候呢

咱们这个地方

这个properties呢

这个地方

这个properties

最终呢

确定下来的应该就是这个对象

名字叫local的这个对象

当然我们需要给它复制啊

这个后边我们需要通过程序的方式

去体现出来啊

所以我们真正这个地方

使用到的这个properties

其实就是这个local

就是这个local

而这个local

它封装的是什么呢

大家来看

封装的是uri

uri什么prefix

还有endpoint

什么access key id

什么secret

还有prefix

还有bucket name

这个对应的是谁呢

其实对应的就是我们local这块

这块配置

你看

urprefix

对吧

还有同的名称

还有endpoint

endpoint对应的就是我们这个本地嘛

本地的话

我是不是需要指定一个盘符

对吧

我们的文件需要上传到什么位置

比如说我们如果用的是阿里云存储呢

那么他走的就是下面这段配置

你看他bucket name是不是就这个

然后呢

endpoint

这是阿里云给我们提供的一个网址

当然了

你需要去阿里云去注册成功的话呢

去注册账号对吧

去注册账号

然后呢

去申请这个空间

然后呢

我们访问阿里云的时候呢

他是需要健全的

所以我们需要有这么一对啊

一个是key的id

还有一个secret的

这相当于是密码

那么申请完阿里云之后呢

这些呢都是有的

所以说如果用的是阿里云存储

那么他读取的就是这段配置

最终呢

他就会封装到我们这个properties里面去

这些都封装好了就

然后我们刚才考下来这个方法呢

其实就是获得

什么

获得我们下载地址的前缀

你看首先我们判断一下

properties.get ui prefix

如果它不是空对吧

不是空的话就直接使用这个ui prefix

咱们可以对照我们那个阿里云来看一下

这里边呢

我们是不是没有去配置这个什么ui prefix

那么没有配置呢

他就会走这个else

走else的话

他获取的是谁呢

就是properties的endpoint这个属性

endpoint

你看其实对应的就是这个属性

所以他取到的值呢

就是这个

自负传

那么假设我们使用的是本地存储

对吧

本地存储

你看我们是不是配置了这个ui prefix

所以说呢

他取到的就是这段这个值

因为这是不同的存储方案呢

它的特点不一样

它特点不一样

所以我们在这呢

先判断一下

如果有这个ui prefix

先取它的值

没有呢

就取这个endpoint的这个值

这个呢

这个前缀其实是干什么用的呢

是为我们后边下载准备的

你看下载地址的一个前缀

这个方法呢

我们当前的没有用到

因为呢

这是给它的子类来使用的

在我们当前这个类里面没有使用到

我们先提前把它提供好

后边呢

我们在它的子类里面呢

直接拿过来使用就可以了

好

那么到这儿的话呢

咱们整个这个抽象的文件策略处理类呢

就已经编写完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频为一个关于“文件服务”模块的开发教程，核心内容是实现一个基于**策略模式（Strategy Pattern）**的文件上传与删除服务。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何设计一个抽象的文件策略类 `AbstractFileStrategy`，并定义了具体的实现类（如本地、阿里云、FastDFS 等）。同时，视频也展示了如何通过 Spring Boot 的 `@ConfigurationProperties` 注解来管理不同存储类型的配置，并利用 Nacos 作为配置中心进行动态配置管理。整个设计旨在实现文件服务的高内聚、低耦合，便于后期扩展和维护。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 介绍课程主题“文件服务”，并展示项目结构，重点讲解 `strategy` 包下的 `AbstractFileStrategy.java`。
*   **00:15 - 00:30**: 展示 `AbstractFileStrategy` 抽象类的代码，定义了 `upload` 和 `delete` 两个抽象方法，用于规范所有具体实现类的行为。
*   **00:30 - 00:45**: 讲解 `FileServerProperties.java` 配置类，定义了 `FileStorageType` 枚举和 `uriPrefix`、`innerUriPrefix` 等属性，用于区分不同存储类型。
*   **00:45 - 01:00**: 展示 `Properties` 内部类，用于封装不同存储服务（如 `minio`、`aliyun`、`tencent`）的详细配置信息（如 endpoint、accessKey、secretKey）。
*   **01:00 - 01:15**: 讲解 `getUriPrefix()` 方法的实现，该方法根据配置决定返回内网地址还是外网地址，体现了配置的灵活性。
*   **01:15 - 01:30**: 展示 `AbstractFileStrategy` 中的 `@Autowired` 注解，用于注入 `FileServerProperties`，以便在具体实现类中获取配置信息。
*   **01:30 - 01:45**: 切换到 Nacos 配置中心界面，展示如何为 `pd-file-server` 服务配置不同的存储策略（如 `LOCAL`、`FAST_DFS`、`ALIYUN`）。
*   **01:45 - 02:00**: 回到代码，讲解 `AbstractFileStrategy` 中的 `upload` 方法，演示如何通过 `multipartFile` 获取文件信息并构建 `File` 对象。
*   **02:00 - 02:15**: 展示 `delete` 方法的抽象定义，以及如何通过 `FileDeleteDO` 对象传递要删除的文件信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 大纲**:
    *   文件服务
        *   1. 需求背景
        *   2. 核心功能
        *   3. 存储策略
        *   4. 技术设计
        *   5. 文件服务开发
            *   5.1 环境搭建
            *   5.2 文件处理策略
                *   5.2.1 FileStrategy
                *   5.2.2 AbstractFileStrategy
                *   5.2.3 LocalServiceImpl
                *   5.2.4 FastDfsServiceImpl
                *   5.2.5 AliServiceImpl
            *   5.3 接口开发-上传附件
            *   5.4 接口开发-根据业务id下载附件
            *   5.5 接口开发-根据业务类型/业务id下载附件
            *   5.6 接口开发-根据业务类型/业务id打包

*   **关键代码片段**:

    **`AbstractFileStrategy.java` (抽象策略类)**

    ```java
    @Slf4j
    public abstract class AbstractFileStrategy implements FileStrategy {
        private static final String FILE_SPLIT = ".";
        // 上传文件
        @Override
        public File upload(MultipartFile multipartFile) { ... }
        // 文件上传抽象方法，需要由当前类的子类来实现
        public abstract File uploadFile(File file, MultipartFile multipartFile);
        // 文件删除
        @Override
        public boolean delete(List<FileDeleteDO> list) { ... }
        // 获取下载地址前缀
        protected String getUriPrefix() {
            if (StringUtils.isNotEmpty(properties.getUriPrefix())) {
                return properties.getUriPrefix();
            } else {
                return properties.getEndpoint();
            }
        }
    }
    ```

    **`FileServerProperties.java` (配置类)**

    ```java
    @Data
    @ConfigurationProperties(prefix = "pinda.file")
    @RefreshScope
    public class FileServerProperties {
        private FileStorageType type = FileStorageType.LOCAL;
        private String uriPrefix = "";
        private String innerUriPrefix = "";
        // 内网通道前缀 主要用于解决某些服务器的无法访问外网ip的问题

        public String getInnerUriPrefix() { return innerUriPrefix; }
        public String getUriPrefix() {
            if (uriPrefix.endsWith(StrPool.SLASH)) {
                uriPrefix += StrPool.SLASH;
            }
            return uriPrefix;
        }

        private Properties local;
        private Properties ali;
        private Properties minid;
        private Properties qiniu;
        private Properties tencent;

        @Data
        public static class Properties {
            private String uriPrefix;
            private String endpoint;
            private String accessKeyId;
            private String accessKeySecret;
            private String bucketName;
        }
    }
    ```

    **`getUriPrefix()` 方法逻辑**:
    该方法优先使用 `uriPrefix`，如果为空，则使用 `endpoint`。这允许开发者根据部署环境（如内网或外网）灵活配置下载地址。

---

### 4) 关键场景与演示描述

*   **场景一：策略模式设计** (00:00-00:30)
    讲师在 IDE 中打开 `AbstractFileStrategy.java`，通过高亮显示 `upload` 和 `delete` 方法，强调这是一个抽象类，其子类（如 `LocalServiceImpl`、`AliServiceImpl`）必须实现这些方法。这体现了策略模式的核心思想：将算法（文件上传/删除）的实现细节封装在不同的具体策略类中，使得主程序（如控制器）无需关心具体实现。

*   **场景二：配置管理** (00:30-01:15)
    讲师切换到 `FileServerProperties.java`，通过注释和代码展示了如何使用 `@ConfigurationProperties` 注解将配置文件中的属性绑定到 Java 类的字段上。他特别强调了 `Properties` 内部类的结构，用于封装不同存储服务（如 `ali`、`qiniu`）的详细配置，如 `endpoint`、`accessKeySecret` 等。这使得配置管理变得集中和可维护。

*   **场景三：Nacos 配置中心** (01:30-01:45)
    讲师切换到浏览器，打开 Nacos 配置中心，展示 `pd-file-server` 服务的配置详情。他演示了如何为不同存储类型（如 `LOCAL`、`FAST_DFS`、`ALIYUN`）设置不同的配置值，例如 `uriPrefix` 和 `endpoint`。这表明系统可以通过配置中心动态切换存储策略，无需重新编译或部署。

*   **场景四：文件上传逻辑** (01:45-02:00)
    讲师回到代码，展示 `AbstractFileStrategy` 中 `upload` 方法的实现。他通过 `File.builder()` 方法构建一个 `File` 对象，并设置其属性，如文件名、内容类型、大小等。这展示了如何将上传的 `MultipartFile` 转换为系统内部统一的 `File` 对象，为后续的存储操作做准备。

*   **场景五：下载地址生成** (01:00-01:15)
    讲师重点讲解 `getUriPrefix()` 方法。他通过代码演示，当 `uriPrefix` 配置不为空时，直接返回该值；否则，返回 `endpoint`。这体现了系统在不同部署环境下（如内网或外网）的灵活性，能够动态生成正确的下载地址。
