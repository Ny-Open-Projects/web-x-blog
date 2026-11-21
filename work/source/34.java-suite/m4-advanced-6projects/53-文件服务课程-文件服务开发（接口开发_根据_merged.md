# 53-文件服务课程-文件服务开发（接口开发_根据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们是已经实现了

我们根据文件ID打包下载

所有的代码开发 对吧

那接下来我们就可以来测试一下了

首先我们可以来测试一下

我们如果是使用的是这种阿里云存储 对吧

那么你看当前我们使用的就是阿里云存储

这种策略 咱们进行文件下载

好 Nux

咱们这个地方其实都已经启动过了

这个配置中心

并且我们配置的策略是阿里云存储

其实如果是阿里云存储的话

我们这个Nux其实是不需要的

什么时候才需要Nux呢

就是我们如果使用的是本地策略 对吧

本地策略的话

我们就需要借助这个Nux来对外提供HTTP

访问我们上传的文件服务 对吧

所以说如果是阿里云的话

这个Nux其实不启动也是没有关系的

好 接下来我们来启动一下咱们这个文件服务

需要重新启动

因为我们刚才是新开发了一些代码

好 咱们重新来启动一下

先来观察一下

我们现在这个表里边是没有数据的 对吧

所以说我们要下载的话

咱们需要来重新上传

而且咱们这个地方要测得完整一点

就是什么呢

因为我们刚才提到咱们这个文件下载的功能

可以一次性下载多个文件 对吧

所以说我们可以多传几个文件上去

而且

我们也可以在传文件的时候

传这种相同的文件名

这样的话

它是不是就会把我们这个同名的文件

进行一个文件名的处理

也就是说我们都要测到位

好 那么这个服务已经启动成功了

接下来咱们就来进行一个文件上传

咱们先来复件上传

这个随便填一下就可以了

咱们可以传一下这个

Nux.config 对吧

这个Nux.config 对吧

这个Nux.config 对吧

好 传上这个文件

然后这些我就不提交了

直接发送

稍等一下

好 你看它是不是已经传成功了

然后我们把这个表里面来刷新一下

接下来我们可以再来完成一个文件上传

把它关了

重新来提交一下

然后这个文件的话

我们还选这个文件

目的我就是想测一下

如果是同名文件 对吧

咱们再进行下载会有什么问题

好 这又传上去了

传上去之后

再来看一下我们这边

你看是不是两条数据

原始的文件名都是这个Nux.config 对吧

这个配置文件

然后我们来看一下他们这个访问地址

对吧

访问地址

这是第一个文件所对应的访问地址

现在因为已经传成功了

所以我们肯定是能够下载到

你看

然后我们从这边再来访问一下

应该也是可以下载到的

好 大家其实可以看一下

你看我们使用这个浏览器进行下载的问题是什么呢?

好 大家其实可以看一下你看我们使用这个浏览器进行下载的问题是什么呢?

我们使用这个浏览器进行下载的问题是什么呢?

它对于这种相同文件名

你看它是不是自动就在后面加了括号1

对吧

因为我们刚才已经下载了一个Nux.config

所以现在再下载

它自动就给我们区分开了

它会加一个括号1

而我们现在其实也是想做这么一个效果

只不过

现在咱们下载的话

就不直接通过这个UL地址

通过浏览器去下载了

而是什么呢?

通过我们这个接口去下载

你看这个地方

我们是不是已经有根据文件ID打包下载

好

好

这样的话

我们需要把它的ID传过来

这是第一个ID

然后用逗号给它分隔开就可以了

这个是第二个ID

好

咱们直接点发送

好

你看它是已经返回来了

这么一个链接对吧

然后我们直接点击这个链接

大家来看

你看它是不是下载的文件名

就叫做Nux.zip

对吧

好

我们可以把它打开

好

来看一下

你看这里边是不是就是我们这两个文件名

但是第一个叫做Nux.config

对吧

然后你再看这第二个

它是不是就给我们加上这个括号1

对吧

然后进行一个区分

就是因为它这个地方有这两个文件名是重复了

好

这是我们测试了一下

咱们是不是同时下载多个文件

对吧

比如说我现在就想下载一个文件

那么我把这第二个这个ID

把它设置出来

好

好

我现在就把它删掉

对吧

把它删掉

然后我们重新发送一下

然后再来点击下载

你看现在它是不是下载的就是原始的

现在之所以是因为它加了个括号2

是由于我们刚才已经下载过了

对吧

这是浏览器自动给我们加上的

咱们现在我们可以重新再来测一下

重新发送一下

然后再来点击下载

应该前面还有

对吧

还有

这个我们知道这个问题就可以了

也就是说浏览器呢

它会给我们自动的去加上这个括号

对吧

然后呢

防止我们这个文件名重复

好

这个呢是下载的是一个文件

刚才我们测了一下是下载多个文件

现在我们使用的这个文件的存储策略呢

是这个阿里云

对吧

一会儿呢

我们来测试一下

使用本地这种情况

来进行文件下载

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程演示了一个基于 Spring Boot 的文件服务（`pd-file-server`）的完整开发与部署流程。课程内容涵盖了从项目配置、数据库设计、文件上传接口开发、文件下载接口开发，到通过 Nacos 配置中心进行配置管理的全过程。核心演示包括：
- **文件上传**：通过 Swagger UI 调用 `POST /attachment/upload` 接口上传文件，并在数据库中记录文件元数据。
- **文件下载**：通过 Swagger UI 调用 `GET /attachment/download` 接口根据 ID 下载文件。
- **配置管理**：在 Nacos 中配置文件服务的存储路径和 OSS 对象存储的访问凭证。
- **数据库操作**：使用 Navicat 连接 MySQL 数据库，执行 SQL 语句进行数据增删改查。

整个过程旨在展示一个典型的、可扩展的文件服务在微服务架构下的实现方式。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **章节 0: 开发环境与项目初始化 (0:00 - 0:30)**
  - 展示了项目结构，包括 `pd-auth`、`pd-file` 等模块。
  - 在 IntelliJ IDEA 中打开项目，展示 `AttachmentController.java` 和 `AttachmentServiceImpl.java` 的代码。

- **章节 1: 数据库设计与配置 (0:30 - 1:30)**
  - 使用 Navicat 连接 MySQL 数据库，展示 `pd_attachment` 表结构。
  - 在 IDEA 中编辑 `application.yml` 文件，配置数据库连接信息，包括 `driver-class-name`、`url`、`username` 和 `password`。

- **章节 2: 文件上传接口开发与测试 (1:30 - 3:00)**
  - 在 Swagger UI 中查看 `POST /attachment/upload` 接口的文档。
  - 在 Swagger UI 中配置请求参数（`bizId`, `bizType`, `file`, `isSingle`），并上传一个名为 `nginx.conf` 的文件。
  - 展示上传成功后的响应数据，包含文件的 `id`、`url`、`filename` 等信息。
  - 在 Navicat 中查询 `pd_attachment` 表，验证数据已成功插入。

- **章节 3: 文件下载接口开发与测试 (3:00 - 4:00)**
  - 在 Swagger UI 中查看 `GET /attachment/download` 接口的文档。
  - 在 Swagger UI 中配置请求参数 `id`，并发起下载请求。
  - 展示 Chrome 浏览器的下载页面，确认文件已成功下载。

- **章节 4: 配置中心管理 (4:00 - 5:00)**
  - 登录 Nacos 控制台，进入配置管理页面。
  - 编辑 `pd-file-server.yml` 配置文件，配置文件存储类型为 `LOCAL`，并设置 `local` 存储路径为 `D:/uploadFiles`。
  - 配置 OSS 对象存储的 `bucket-name`、`endpoint`、`access-key-id` 和 `access-key-secret`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT / 图表**：
  - **Swagger UI 界面截图**：展示了文件上传和下载接口的详细文档，包括请求方法、请求参数、响应数据等。
  - **Navicat 数据库界面截图**：展示了 `pd_attachment` 表的结构和数据。
  - **Nacos 配置中心界面截图**：展示了配置文件的编辑界面，包括 `file.type`、`file.local`、`oss.bucket-name` 等配置项。

- **代码**：
  - **数据库配置文件 (`application.yml`)**：
    ```yaml
    spring:
      datasource:
        driver-class-name: com.p6spy.engine.P6SpyDriver
        url: jdbc:p6spy:mysql://$[pinda.mysql.ip]:$[pinda.mysql.port]/$[pinda.mysql.database]?serverTimezone=UTC
        username: root
        password: 123456
    ```
  - **文件上传接口代码 (`AttachmentController.java`)**：
    ```java
    @PostMapping("/attachment/upload")
    public Result upload(@RequestParam("file") MultipartFile file,
                         @RequestParam("bizId") Integer bizId,
                         @RequestParam("bizType") Integer bizType,
                         @RequestParam("isSingle") Boolean isSingle) {
        // 业务逻辑
    }
    ```
  - **文件下载接口代码 (`AttachmentController.java`)**：
    ```java
    @GetMapping("/attachment/download")
    public void download(@RequestParam("id") Integer id, HttpServletResponse response) {
        // 业务逻辑
    }
    ```
  - **Nacos 配置文件 (`pd-file-server.yml`)**：
    ```yaml
    file:
      type: LOCAL
      local:
        path: D:/uploadFiles
    oss:
      bucket-name: oss-file-service
      endpoint: http://oss-cn-qingdao.aliyuncs.com
      access-key-id: LTAI4Fm1nIaF6l61G51u4i
      access-key-secret: 50u1SgPwPyg7sQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQc
