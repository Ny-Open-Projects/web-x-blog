# 88-文件服务课程-文件服务开发（接口开发_分片 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么阿里云这种方式呢

我们已经写完了

接下来呢 我们可以测试一下

但是这个地方呢

我们发现少写了一个service注解

对吧 把这个service注解来加一下

好 那接下来呢

我们就可以来测试一下

因为这块呢

代码相对来说比较繁琐

所以说我们可以在这加一个断点

咱们可以跟一下

看看它这个过程

首先呢 我们需要把咱们这个

配置文件呢 改一下

把我们这个策略呢

改成什么呢 阿里

好 type等于阿里

好 发布

然后呢 我们就可以直接来启动了

这次呢 我们再进行这个分片上传

对吧 最终呢

我们这个文件呢

会上传到我们阿里云的平台

好 那么现在呢

咱们这个服务呢 已经启动完了

启动完之后呢

我们现在呢 就可以直接来测试了

还是使用我们这个页面 对吧

重新把这个页面刷新一下

现在呢 我们再来

随便来传一个文件

看这个文件

是20多兆 对吧

好 稍等一下

好 那么现在呢 你看

它已经到我们这个分片的合并方法了

这个时候呢 我们来看一下

因为我们还没有真正合并

所以说呢 我们这些临时文件呢

也就是我们本地的这些分片文件

应该还存在

咱们来看一下

地盘trunks2020

然后呢 这个

你看现在是不是还是存在的

刚才呢 我们看到那个文件呢

应该是20多兆啊

所以说呢 它一共是分成了20多兆的文件

它分装了这么三片

三片文件

接下来呢 就到这个地方

在这个地方呢

我们就要进行分片的合并了

看 传进来这个files里边

封装的是这么三个文件

对吧 分别是0 1 2

然后filename呢

就是这个

然后呢 这是我们的

DTO对象

DTO对象

在这里边

这里边属性了 封装的也都没有问题

也都没问题 三片

那接下来呢 我们继续往下走

把这个client对象是不是创建一下

好 稍等一下啊

因为这个地方呢

它是需要连接网络的

所以稍微有一点点慢

好 client对象是不是已经创建出来了

你看这是我们的endpoint对吧

还有什么呢

其他的一些属性啊

最重要的就是它

还有这个bucket的什么operation等等这些

然后呢 我们继续往下走

把这个bucket name是不是给它取出来

好 这个也没问题

然后呢 这是日期目录对吧

日期目录

好

这2020-05

这个也没问题

然后呢 这是整个路径的一个拼接

你看它这是2020-05

然后呢 是我们把这个文件名拼到一块

其实就这三部分拼起来了

然后呢 接下来是这个原信息的保存

对吧

这个封装

好

然后呢 我们处置化

这边一个result

稍等一下

好

然后呢 现在我们来看啊

它会给我们产生一个upload id对吧

看这个upload id是多少呢

其实是非常长的这么一串对吧

哎呀 几十位长度的这么一个串

好 是一个唯一的

然后接下来呢 是不是要进行分片上传

分别在我们4星环里面呢

来进行分片上传

先把第一片取出来

其实就是一个文件对吧

就是我们编号是0的这个文件

好

然后呢 把它封装成一个流

然后呢 这个对象封装 封装

好

真正上传呢 其实是调用这个方法

upload path

这个呢 就传过去了

好

稍等一下

这个过程稍微有一点点慢

好

然后呢 我们add一下

这儿的话是不是又继续

它一共会便利几次呢

很显然我们是三片文件对吧

所以它肯定是便利三次啊

好 咱们直接啊

快一点

然后呢 再传上其余片

你看一到这个方法

它是不是就会稍微卡一下啊

就是因为它这个地方呢

是通过网络上传

然后这是第三回

你看现在这个爱是不是等于二

这是第三次便利

好

稍等一下

好

OK 那么现在呢

是不是就已经

我们已经分片

其实已经上传完成了

对吧

发新环便利了三次

分片已经上传完成了

然后接下来呢

我们对这些

通过这个分片编号呢

进行一个排序

然后呢

我们是不是再调用这个complete

multiply的upload

这个呢来完成什么呢

其实调用这个方法

就是让阿里云呢

在服务端帮我们啊

把那三片文件合并成一个文件

调用这个方法

好

然后呢我们看这个时候呢

这个result啊

看这个result里边封装的是什么东西

好

你看这个key啊

还有location

你看这是完整的路径啊

最终呢

我们通过这个路径

应该就可以访问到我们

在合并之后的那个文件

好

一会呢

我们可以测试一下

好

然后呢

这个呢

就是我们自己封装的吧

url地址

然后呢

把它拼到一块

拼到一块

你看这个url地址

好

这个其实就是我们想要的这个地址

通过这个地址呢

应该就可以访问到我们

合并之后的那个文件

然后呢

把这个file对象

是不是呢

创建出来

相应的属性一个一个来设置

这个呢

我们就不用跟了

直接啊

放行

好

那么到这之后呢

我们来看咱们这些分片文件

这些临时的是不是都没有了

对吧

这个时候呢

我们再到控制台来看一下

应该

它给我们发出了一个insert语句

然后呢

我们到这个数据库里面来看一下

刷新一下

大家看

它是不是又传上来了

就是这条

然后呢

通过这个url地址呢

大家能看到

这是我们那个文件

对吧

对吧

它的url地址

咱们直接复制一下

然后呢

我们直接啊

这样来访问一下

来访问一下

你看

它是不是能够下载到

好

但是它这儿就存在一个乱码

那么我们如果通过这个

这个地方呢

我们来测试一下

通过我们的接口文档

对吧

这样的话

我们要下载的话呢

是需要它的id的

需要它的id

文件的id

咱们直接来copy

然后呢

我们重新来加载一下

下载文件

然后呢

通过id来下载

把id放在这儿

直接发送

稍等一下

好

然后点击下载文件

你看

现在呢

它是不是开始下载了

这个用的就是我们这个原始的文件名

进行下载

这个大小呢

也是22.2兆

没有问题

那么这是关于咱们阿里云这种方式啊

进行分片的合并

对吧

测试呢

是已经通过了

完全没有问题

好

关于这个测试呢

我们先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一段关于如何在 Java 应用中使用阿里云 OSS（对象存储服务）进行文件分片上传的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何实现一个 `merge` 方法，该方法负责将一个文件拆分成多个部分（分片），并利用阿里云 OSS 的分片上传功能，将这些分片合并成一个完整的文件。视频重点讲解了 `AliChunkServiceImpl` 类中的核心逻辑，包括构建 OSS 客户端、计算文件路径、创建并上传分片、收集 PartETag、以及最终完成合并上传并返回文件对象。最后，讲师通过 Swagger UI 展示了上传后的文件在 OSS 服务端的存储状态。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示项目结构和 `AliOSSAutoConfigure.java` 文件。
*   **00:03 - 00:07**: 讲师定位到 `AliChunkServiceImpl` 类，并开始讲解 `merge` 方法的实现。
*   **00:07 - 00:12**: 讲师演示如何构建 OSS 客户端，并获取配置信息，如存储桶名称。
*   **00:12 - 00:16**: 讲师讲解如何根据当前日期和文件名生成文件在 OSS 中的相对路径。
*   **00:16 - 00:21**: 讲师开始编写分片上传的核心循环，创建 `UploadPartRequest` 对象。
*   **00:21 - 00:26**: 讲师设置分片的大小、编号和输入流，并将每个分片上传，同时收集返回的 `PartETag`。
*   **00:26 - 00:31**: 讲师演示如何调用 `completeMultipartUpload` 方法，将所有分片合并成一个完整文件。
*   **00:31 - 00:36**: 讲师构建最终的文件对象 `FilePo`，并关闭 OSS 客户端。
*   **00:36 - 00:40**: 讲师切换到浏览器，展示 Swagger UI 中的文件下载接口，验证文件已成功上传。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **构建 OSS 客户端**:
        ```java
        private OSS buildClient() {
            properties = fileServerProperties.getAli();
            return OSSClientBuilder.build(properties);
        }
        ```
    *   **获取文件路径**:
        ```java
        String relativePath = LocalDate.now().format(DateTimeFormatter.ofPattern(DEFAULT_MONTH_FORMAT_SLASH));
        String relativeFileName = relativePath + StrPool.SLASH + fileName;
        ```
    *   **分片上传循环**:
        ```java
        List<PartETag> partTags = new ArrayList<PartETag>();
        for (int i = 0; i < files.size(); i++) {
            FileInputStream in = FileUtils.openInputStream(file);
            UploadPartRequest uploadPartRequest = new UploadPartRequest();
            uploadPartRequest.setBucketName(bucketName);
            uploadPartRequest.setKey(relativeFileName);
            uploadPartRequest.setUploadId(uploadId);
            uploadPartRequest.setInputStream(in);
            uploadPartRequest.setPartNumber(i + 1);
            uploadPartRequest.setPartSize(file.length());
            PartETag partETag = client.uploadPart(uploadPartRequest);
            partTags.add(partETag);
        }
        ```
    *   **完成合并上传**:
        ```java
        CompleteMultipartUploadRequest completeMultipartUploadRequest = new CompleteMultipartUploadRequest(bucketName, relativeFileName, uploadId, partTags);
        CompleteMultipartUploadResult uploadResult = client.completeMultipartUpload(completeMultipartUploadRequest);
        ```
    *   **构建返回的文件对象**:
        ```java
        File filePo = File.builder()
            .relativePath(relativePath)
            .group(uploadResult.getETag())
            .path(uploadResult.getRequestId())
            .url(StringUtils.replace(url, searchString, StrPool.SLASH))
            .build();
        ```

*   **关键注释**:
    *   `// 日期文件夹 2020/05`
    *   `// web服务器存放的相对路径`
    *   `// 文件上传信息`
    *   `// 每个分片不需要按顺序上传，OSS会按照分片号排序组成完整的文件`
    *   `// 每次上传分片之后，OSS的返回结果会包含一个PartETag，PartETag将被保存到partETags中。`
    *   `// 关闭OSSClient`

---

### 4) 关键场景与演示描述

*   **场景一：环境与项目结构展示 (00:00-00:03)**
    *   讲师首先展示了 IntelliJ IDEA 的项目结构，包括 `pom.xml`、`application.yml` 等配置文件，以及 `AliOSSAutoConfigure.java` 和 `AliChunkServiceImpl.java` 等核心 Java 文件。这为观众提供了项目的整体概览。

*   **场景二：分片上传逻辑实现 (00:03-00:36)**
    *   讲师在 `AliChunkServiceImpl.java` 文件中，逐步演示了 `merge` 方法的实现。
    *   **步骤一：构建客户端** (00:07-00:12)：讲师调用 `buildClient()` 方法，从配置中获取阿里云 OSS 的访问凭证，并创建 `OSSClient` 实例。
    *   **步骤二：生成文件路径** (00:12-00:16)：讲师使用 `LocalDate.now()` 和 `DateTimeFormatter` 根据当前日期生成文件夹名（如 `2020/05`），并拼接文件名，形成完整的 OSS 存储路径。
    *   **步骤三：分片上传循环** (00:16-00:26)：讲师使用 `for` 循环遍历文件列表，为每个文件创建 `UploadPartRequest` 对象，并设置分片号、大小和输入流。然后调用 `client.uploadPart()` 方法上传分片，并将返回的 `PartETag` 收集到列表中。
    *   **步骤四：合并上传** (00:26-00:31)：讲师创建 `CompleteMultipartUploadRequest` 对象，将存储桶名、文件名、上传 ID 和所有 PartETag 传入。然后调用 `client.completeMultipartUpload()` 方法，将所有分片合并成一个完整文件。
    *   **步骤五：构建返回对象** (00:31-00:36)：讲师根据上传结果构建一个 `FilePo` 对象，包含文件的相对路径、ETag、请求 ID 和访问 URL，并关闭 OSS 客户端，最后返回 `R.success(filePo)`。

*   **场景三：结果验证 (00:36-00:40)**
    *   讲师切换到浏览器，打开 Swagger UI 的文件下载接口。
    *   他点击“下载”按钮，系统弹出一个确认对话框，提示“翻译此页？”。
    *   通过这个操作，讲师验证了文件已成功上传到 OSS 服务端，并且可以通过 API 访问和下载。

---

以上是根据视频画面进行的结构化分析。
