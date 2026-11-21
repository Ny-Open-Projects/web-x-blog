# 54-文件服务课程-文件服务开发（接口开发_根据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是测试了一下我们这个文件存储策略啊,使用的是阿里云,这种存储策略的时候,根据ID呢,打包下载附件。

那接下来呢,我们来测试一下,如果说我们使用的是本地存储策略,对吧,然后呢,我们这个文件下载是否还是可以的。

首先呢,我们肯定还是到我们这个配置中心呢,把咱们这个file type对吧,给它改成local,也就是我们使用的是本地策略。

好,发布。

发布完之后呢,需要保证我们的Andex呢,是启动状态,这个呢,我提前都已经启动过了。

接下来呢,我们需要把咱们这个文件服务呢,重新启动一下。

好,那么我们需要重新来启动一下咱们的文件服务。

好,那么到这儿的话,我们文件服务呢,已经启动成功了。

咱们可以来看一下我们这个控制台的这个日志信息,确认一下我们当前这个文件的存储策略是不是已经改成了local,

也就是本地。

好,那接下来呢,咱们来上传一下啊。

先把咱们的文件呢,上传到本地。

最后刷新一下这个页面。

好,调用咱们这个附件上传的接口,把文件传上来。

咱们还是传这个文件吧,andex.config,对吧。

好,这两个参数还是把它勾掉啊,发送。

好,这样上来了一个。

好,可以通过我们这个表来查看一下,你看是不是又多了这条记录。

这个呢,从哪能看出来它是存在我们本地的呢?

其实通过这个URL地址就能够看到,大家可以看到这个地方,对吧。

你看它是基于我们本地的这个andex服务啊,来访问我们当前上传的这个文件。

咱们呢,再来上传一个啊,再来发送一下。

好,应该是又上传上来了一个,刷新一下。

你看现在是不是四条数据。

好,当然我们可以通过我们这个andex啊,来访问。

好,现在我们可以通过我们这个andex啊,来访问。

好,现在我们可以通过我们这个andex啊,来访问。

好,现在我们可以通过我们这个andex啊,来访问。

来访问到我们上传上来的这个页面,这个文件,对吧。

你看,是不是就可以下载到它。

但是这个下载的话呢,是下载它这个原始文件名,对吧。

因为我们是直接通过这个URL地址啊,这种方式去访问它。

所以下载到的是它这个UID啊,所命名的这个。

而我们现在呢,要测试的是什么呢?

根据我们这个文件ID打包下来,对吧。

好,那么咱们需要把这两个ID呢,把它拿过来。

通过我们的接口来进行下载。

一个是这个。

然后呢,别忘了加个逗号,对吧。

然后呢,再把这个ID拷过来。

好,然后我们点发送。

点击下载文件。

你看,这是不是又变成了andex.zip。

这是因为它加了个括号1啊,就是因为我们刚才在测试这个阿里云的时候呢,是不是已经下载过这么一个文件了。

这是由浏览器啊,给我们加上的这个括号1。

你可以看到啊。

我们这里边这两个文件,是不是啊,也都有。

好。

如果说我们只是下载一个文件的话呢,我把前面这个ID去掉,对吧。

只下载这个,点击发送。

然后呢,点击下载。

你看现在呢,它是不是下载的就是直接这个原始文件。

好,这是我们测试了一下咱们这个文件策略,对吧。

文件存储策略呢,改成本地。

那么这个下载呢,也是没有问题的。

好,那么关于咱们这个。

根据文件ID啊,打包下载呢,我们就先测试到这。

好,那我们就测试到这里吧。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频演示了一个基于 **Nacos 配置中心** 和 **FastDFS 文件服务** 的文件上传与下载系统。核心内容包括：
- **配置管理**：通过 Nacos 管理 FastDFS 的配置文件（`pd-file-server.yml`），实现配置的动态化和集中化。
- **文件上传**：通过 HTTP POST 接口，将文件上传至 FastDFS 服务，并将文件信息（如 ID、URL）存入 MySQL 数据库。
- **文件下载**：通过 HTTP GET 接口，根据文件 ID 从数据库获取文件 URL 并进行下载。
- **技术栈**：Java Spring Boot、Nacos、FastDFS、MySQL、Nginx、Swagger。

整个演示流程清晰，展示了如何将配置管理、文件服务和数据库操作整合到一个微服务架构中。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的时间点，以下章节按画面内容和逻辑顺序排列：

- **00:00 - 00:15**：**环境准备与 Nacos 配置**。展示 Nacos 控制台，编辑 `pd-file-server.yml` 配置文件，设置 FastDFS 的 `endpoint`、`bucket-name` 等参数。
- **00:15 - 00:30**：**配置提交与生效**。在 Nacos 中点击“确认”按钮，保存配置。
- **00:30 - 00:45**：**Java 服务端代码**。展示 IntelliJ IDEA 中的 `AttachmentController.java` 和 `AttachmentServiceImpl.java` 代码，说明文件上传的业务逻辑。
- **00:45 - 01:00**：**文件上传接口测试**。在 Swagger UI 中发起 POST 请求，上传文件 `nginx.conf`，并查看返回的 JSON 数据。
- **01:00 - 01:15**：**数据库记录**。展示 Navicat Lite 中的 `pd_attachment` 表，查看上传文件的记录和 URL。
- **01:15 - 01:30**：**文件下载接口测试**。在 Swagger UI 中发起 GET 请求，根据文件 ID 下载文件。
- **01:30 - 01:45**：**文件下载结果**。展示下载的文件 `nginx.conf`，并打开文件内容。
- **01:45 - 02:00**：**接口文档与总结**。展示接口文档页面，总结整个文件服务的开发流程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 页面**：在视频末尾，展示了名为 `文件服务.md - Typora` 的文档，其中包含章节 `5.6.3 接口测试` 和 `5.7 接口开发-根据业务类型/业务id打包下载`。
- **接口文档**：在 `http://localhost:8765/doc.html` 页面，展示了文件服务的 API 文档，包括上传和下载接口的请求参数和响应格式。

#### 代码关键内容

- **Nacos 配置文件 (`pd-file-server.yml`)**：
  ```yaml
  file:
    type: ALI # LOCAL ALI MINIO FAST_DFS # 根据类型选择存储
    urlPrefix: http://127.0.0.1:8080 # 本地测试时使用
    local:
      urlPrefix: http://$(ip):$(nginx_port) # 用于 FastDFS 服务
      bucket-name: oss-file-service
      endpoint: D:\uploadFiles
    ali:
      # 请填写自己的阿里云存储配置
      bucket-name: bladex-loan
      endpoint: http://oss-cn-qingdao.aliyuncs.com
      access-key-id: LTAI4FhtmPAiZ6iLGJSiJui
      access-key-secret: SsU15qaPwpF1x5Mqwc0XzGuY92fnc
  ```

- **Java 服务端代码 (`AttachmentController.java`)**：
  ```java
  @PostMapping("/attachment/upload")
  public Result upload(@RequestParam("file") MultipartFile file, @RequestParam("bizId") String bizId, @RequestParam("bizType") Integer bizType) {
      // 业务逻辑：保存文件到 FastDFS，将信息存入数据库
      String fileId = fileService.upload(file, bizId, bizType);
      return Result.success(fileId);
  }
  ```

- **Java 服务端代码 (`AttachmentServiceImpl.java`)**：
  ```java
  public String upload(MultipartFile file, String bizId, Integer bizType) {
      // 1. 上传文件到 FastDFS
      String fileId = fastDfsService.upload(file);
      // 2. 将文件信息存入数据库
      pdAttachmentService.save(fileId, bizId, bizType);
      return fileId;
  }
  ```

#### 图表 / 数据库内容

- **数据库表 `pd_attachment`**：
  - `id`: 文件 ID。
  - `bizId`: 业务 ID。
  - `bizType`: 业务类型。
  - `fileId`: 文件在 FastDFS 中的 ID。
  - `url`: 文件在 FastDFS 中的访问 URL。
  - `createTime`: 创建时间。
  - `updateTime`: 更新时间。

---

### 4) 关键场景与演示描述

#### 场景一：Nacos 配置中心配置

- **描述**：在 Nacos 控制台中，用户编辑 `pd-file-server.yml` 文件，配置 FastDFS 的阿里云存储参数，包括 `bucket-name`、`endpoint`、`access-key-id` 和 `access-key-secret`。
- **关键操作**：点击“确认”按钮，将配置提交并生效。

#### 场景二：文件上传接口测试

- **描述**：在 Swagger UI 中，用户发起一个 POST 请求，上传文件 `nginx.conf`，并设置 `bizId` 和 `bizType` 参数。
- **关键操作**：点击“发送”按钮，查看返回的 JSON 数据，其中包含文件的 `id`、`url` 和 `code`。

#### 场景三：数据库记录查看

- **描述**：在 Navicat Lite 中，用户查询 `pd_attachment` 表，查看上传文件的记录和 URL。
- **关键操作**：在 Navicat 中执行 SQL 查询，查看文件的 `id`、`url` 和 `createTime`。

#### 场景四：文件下载接口测试

- **描述**：在 Swagger UI 中，用户发起一个 GET 请求，根据文件 ID 下载文件。
- **关键操作**：点击“发送”按钮，下载文件 `nginx.conf`，并打开文件内容。

#### 场景五：接口文档展示

- **描述**：在 `http://localhost:8765/doc.html` 页面，用户查看文件服务的 API 文档，包括上传和下载接口的请求参数和响应格式。
- **关键操作**：在文档页面中，查看接口的详细说明和示例。

---

以上是根据视频画面进行的结构化技术课程分析。
