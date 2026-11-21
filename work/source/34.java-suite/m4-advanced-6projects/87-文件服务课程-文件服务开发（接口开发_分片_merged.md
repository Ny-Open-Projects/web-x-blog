# 87-文件服务课程-文件服务开发（接口开发_分片 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才我们已经实现了FastDFS Trunk Service IMPL

这个service是当我们文件的处理策略

为FastDFS的时候

我们如何进行分片的合并

那么接下来我们来看最后一个

就是阿里云的这个

叫做Ali Trunk Service IMPL

那么我们需要把这个实现类

把它创建出来

同样也是放在我们相应的配置类当中

这些我们暂时先关上

打开咱们阿里云的这个配置类

找到我们这个storage

这个是阿里云OSS

Public Class

这是类名

然后extends abstract

abstract

这个

咱们来实现这个merge这个方法

这个我们加一个注释

咱们这个service是什么呢

是处理这种阿里云

阿里云OSS

分片

文件

策略

这么一个处理类

然后我们来实现这个

来加一个注释

这是我们的分片的合并方法

那么要使用我们这个阿里云

进行分片的合并

咱们需要使用到

它给我们提供的一个客户端

这个客户端

其实在上面这个地方

我们也写过了

咱们直接把它拿过来

把这个方法拷过来

然后在我们当前这个service里边

也会用到它

来看一下

好

但是这个变量名

我们定义的是不一样的

对吧

这个我们可以来找一下

它起的名字叫做file server properties

然后我们get阿里

这个对应的是谁

这个对应的应该是

咱们这儿没有定义

没有定义的话

我们可以给它来定义一下

再来接受一下

properties

这个是我们的

好

就是get阿里

拿到的其实就是我们配置的

阿里云这段配置

对吧

拿到的其实就是这些配置

把这些配置

封装到我们这个property对象里面去

好

这是关于咱们阿里云的这段配置

然后我们到这边来

那么读取到它之后

我们是不是要创建这么一个

叫做OSS的

这么一个客户端对象

对吧

通过这个对象来进行什么

我们这个文件的操作

文件的操作

好

你看需要传进来的是什么

是咱们配置文件中

当中配置的endpoint

还有什么access key id

还有access key secret

好

最终就会给我们返回这么一个OSS对象

那么在这儿的话

咱们就可以直接去调用我们这个什么

build client的方法

对吧

然后返回我们这个client的对象

好

返回client的对象之后

我们如何来进行分片的合并

这个地方

其实它也是给我们

进行了一个封装

就跟咱们前面实现这个

Fast的DFS是类似的

这个地方呢

其实严格来说

我们这个地方虽然

这个方法我们强调

它是分片合并

对吧

而实际上这个地方呢

我们其实调用的是

它的这个分片上传的方法

是这个client对象的

分片上传的方法

那么我们

为什么说是分片合并

这个地方呢

又改成分片上传了呢

是因为啊

这个阿里云呢

OSS

是这个

已经给我们进行了封装

我们只需要把这些分片

咱们这些分片呢

是不是全封装到这个集合里面了

把它上传到我们的阿里云平台

然后呢

它会根据我们提供的一些API呢

来去自动完成分片的合并

所以我们要做的呢

就是把这些分片的文件呢

传到阿里云平台上面去

然后呢

它会根据要求呢

来帮我们来完成合并

大家明白这个意思吧

所以说这块呢

我们实际上调用它的API呢

是文件上传的

分片上传的API

最终呢

是由阿里云

它已经封装了

然后呢

它帮我们去完成这个分片的合并

当然了

它这个地方的封装的

其实代码写起来还是比较繁琐的

咱们可以来看一下

这个地方呢

我们这是阿里云

他给我们提供的这么一个页面

对吧

阿里云

然后呢

这有一个分片上传

我们直接来找到分片上传

大家可以看到

这是他给我们提供的这个例子里面的页面

这个例子程序

实际上呢

我们讲义上呢

也是照着他这个例子程序呢

进行的改造啊

改造之后的

咱们来看一下大概这个示例

它的实现的步骤啊

首先endpoint

access key id

access key secret

这些呢

咱们是不是通过我们的配置文件

都可以读取到

对吧

然后还有bucket name

也可以读取到

然后呢

这是我们对象的名字

对吧

就是最终呢

它是这么一个类似于这样的这么一个路径

好

然后呢

我们是不是把这个对象

创建出来

刚才咱们已经创建过了

创建过之后呢

我们需要来创建啊

这么一个对象

你看到没有

它这个类名呢

非常长啊

叫做initialize multi-part upload request

对吧

哎

然后呢

需要把它创建出来

然后呢

把这两部分数据啊

把这些参数给它传进去

好

这后边呢

它显示不太全

你看

把这两个参数传进去

一个是我们的一个bucket name

其实对应的是空间名对吧

然后呢

还有一个就是object name

好

它这有个滚动条啊

我们给它划回来

咱们来先大概读一下它这个代码

你看它给我们提供的例子呢

其实这个代码非常繁琐

然后呢

它需要创建什么呢

这个metadata对吧

哎

其实是一些原数据啊

原数据封装

然后呢

初始化分片

你看没有

初始化分片

怎么初始化分片呢

其实就是调用我们这个client对象的这个方法

叫做initialize对吧

multipart upload

然后呢

把前面咱们封装的这个request对象

把这个对象是不是给它传进去

好

然后呢

就得到了这么一个upup result对吧

注意啊

现在呢

还没有真正进行分片的上传

只是初始化了一下

初始化分片对吧

然后呢

我们需要通过这个对象呢

get一个upload id

其实就是一个什么呢

上传的id

它是分片上传事件的唯一的一个标识

那么我们可以啊

根据这个标识来发起什么相关的操作啊

比如说什么呢

取消分片上传呢

查询分片上传等等啊

所以我们需要拿到这么一个id

到这儿的话呢

还没有进行真正的分片上传

真正分片上传其实是在哪呢

你看这块呢

这其实是在计算我们有多少个分片对吧

分片大小等等这些

好

然后呢

真正分片上传其实是这个负荷循环里面

因为我们有多片对吧

所以它一定要便利

好

便利

便利出来之后呢

这其实就是其中的一个分片对吧

然后呢

把它封装成一个什么input stream对吧

封装成这么一个流

然后呢

我们继续来进行封装这么一个啊

叫做up part request

part其实就是部分对吧

也就因为它是一个分片

它其实是我们整个文件的一部分

所以它封装了这么一个对象

叫做up part request

然后呢

把我们的这个什么呢

空间名

这个name

还有返回的这个什么呢

上传的id对吧

还有我们当前这一片文件啊

所封装成的这个流对象对吧

全都封装进去

包括这个文件的大小对吧

大小

然后呢

这个分片的

分片的一个

编号对吧

你看设置分片号

就是每一个分片的都有唯一的这么一个编号

啊

啊

这些呢

都设置好之后

我们就可以调用这个client对象的这个upload part方法

然后呢

把我们这个对象给传上去

对吧

其实最终它达到的效果就是什么呢

把我们当前这一片文件是不是传上去啊

然后呢

每次传完之后呢

还有

还有把这个tag呢

把它记录到我们这个tags里面去

因为什么呢

现在我们只是把这些分片啊

一个一个给它传上去了

现在还没有进行合并

对不对

我们最终呢

是希望把传上去的这些分片文件

最终是要把它合并到一块

那么合并的话呢

就需要来调用下边这个代码

你看使用它给我们提供的这么一个类啊

叫做complete multipart upload request对象

这个呢

就是我们执行完上传之后呢

就可以啊

来调用这个

调用它给我们提供的这个方法来实现什么呢

实现分片的合并

啊

那么合并的话呢

需要封装这么一个对象呢

对吧

然后呢

把这些参数相应的都封装进去

然后呢

我们来调用这个叫做complete multipart upload result

一定要用这个方法呢

它就是什么呢

就会把我们传上去的那些分片进行一个合并

最终呢

给我们返回这么一个result对象

所以大家可以看一下

整个代码写起来呢

其实是非常繁琐的

其实对于这种代码呢

我们一般情况下也没有必要自己去手写

即使你背下来其实也没有多大意义

对吧

因为都是它

给我们提供的一些API

所以我们只要抓住什么呢

关键的环节

能看懂它的步骤

并且呢

把这个代码呢

能够拿到我们这边来

然后呢

相应的进行修改

最终呢

实现我们想要的效果就可以了

所以说呢

我们这一块呢

就直接从咱们这个讲义上

把它抄过来就可以了

我们讲义上这个代码

其实也是从它官方给的这个例子这呢

直接进行的一个改造啊

然后呢

我们直接抄过来

抄过来之后呢

我们整个再来分析一遍

好

整个这个代码

大家可以看到是很多的

差这一句对吧

client

从这一句

一直复制到最后啊

我们一直到这个方法的结束啊

但是这一句呢

就没有用了

这是由于我们这个变量名是不是不一样

properties

这应该用的是properties

来找一下看

这是应该我们是不是需要把它定义成一个全局的就好使了

所以我们在这呢稍微改造一下

咱们把这个properties呢给它拿到外边来

要不然的话

我们是不是出了这个方法出了它作用域了

等于呢

然后在这个地方呢

我们直接给它

这样改造一下

对吧

这样的话

我们这边是不是就没有问题了

好

这是build client

然后呢

这个地方呢

是由于我们这个名称呢

这个命名啊不一样

对吧

这其实是我们的DTO对象

把这个改造一下

好

咱们呢

再对着我们当前这个代码呢

来大概读一下

首先这是创建我们的客户端对象

这个应该没什么问题

然后呢

这是从我们这个配置文件里面是不是把我们的bucket name给读取出来

对吧

bucket name呢

其实对应的就是我们在这个地方配置的

这个地方好像有点问题啊

这个地方我们配置的这个bucket name

就是把这个值给取出来了

然后呢

接下来

这是我们日期文件夹

对吧

日期文件夹

拿到的其实就是类似于这样的2020对吧

然后-05就是类似于这样的

日期文件夹

然后呢

这个呢

是把整个路径给拼起来

这就是我们这个日期文件夹加上一个斜线

再加上一个什么呢

file name

这个file name呢

就是我们这传进来的

好

然后接下来呢

这是我们说的这个metadata的吧

原信息啊

这是我们文件

文件

上传原信息

原信息

然后呢

我们这里边封装的是什么呢

是这个content disposition对吧

然后指定file name

file name呢

从DTO里面来获得就可以了

然后呢

设置我们的content type也是从DTO里面去获得

这些呢

都是一些常规的配置

然后接下来呢

就是初始化一个分片上传的事件

其实就是咱们前面也看到了

对应的就是这边

就是这个对吧

叫做initialize multipath upload request

这个类名呢

是非常长的

然后呢

把我们的相关的这些参数对吧

bucket name

related file path

还有metadata

三个参数传进去

接下来呢

我们是不是就初始化这个

初始化这个事件

初始化这个事件

然后呢

他会给我们一个result

通过这个result呢

我们就拿到了这个文件上传的一个ID

那么到这儿的话呢

只是只是说明我们要进行文件上传

对不对

但是呢

还没有真正进行文件上传

那么真正进行文件上传的是在这个复号循环里边

对吧

复号循环里边

最核心的呢

其实就是这个client.upload path

这你看通过这个名字也能看到

我们传上去的是不是只是一部分文件

一部分文件

其实就是一个分片文件

当然了

因为他要封装这个参数啊

要封装这个参数

所以在这儿呢

就要把它创建出来

然后呢

设置一系列的这些属性

一系列的属性

而这个地方呢

最重要的是这个in

这个in是一个输入流

对不对

而这个输入流呢

是通过我们这个file创建出来的

而这个file呢

就是通过我们这个files get出来的

这个files呢

是不是就是我们所有的这个分片

对吧

全都封装到这个集合里面去了

所以我们这样呢

把它取出来

封装成这么一个输入流

然后呢

这个输入流呢

又封装到这个对象里面去了

所以你可以看到

他这个对象的封装呢

其实还是挺麻烦的

非常多

然后呢

设置这个部分文件的大小

对吧

咱们呢

其实是10兆啊

咱们是10兆一片

这是由于我们前端呢

是这样设置的

然后呢

设置我们分片号

包括这个注释的

你看跟他跟我们提供的例子呢

都是一样的

好

然后呢

我们调用这个upload part

这个呢

就是把我们当前这一片文件

把它传上去了

传上去之后呢

这个地方其实就是做了一个记号

因为我们后边还要做什么呢

做分片的合并

所以接下来呢

我们是不是排序啊

把这个顺序排一下

根据分片号

然后呢

排一下

然后呢

我们是不是就调用了这个

叫做

complete

完成什么multiple upload

然后这个呢

其实一定要用这个方法

其实就是什么呢

哎

在阿里云

哎

服务端来实现什么呢

服务端啊

来实现分片的合并

好

所以说呢

我们直接调用这个方法就可以了

但是他需要传进来这么一个request对象

而这个request对象呢

对应的就是这么一个类啊

叫做complete

multiple

multiple upload request

然后呢

把这些参数啊

空间名对吧

然后这个filename

还有上传的ID

还有我们记录的这些

啊

tags对吧

然后呢

把它传进去

好

封装的非常深

到这的话呢

其实就已经这个完成合并了

然后完成合并之后呢

我们接下来封装的这些呢

这其实就是在

封装我们这个file对象对吧

哎

需要给我们这个上一层

其实就是我们的这个controller那层了

来进行返回

然后最后呢

把这个client对象呢

给他关闭掉就可以了

大概呢

就是这么一个套路啊

这块呢

代码整体写起来呢

其实还是非常繁琐的

所以对于这一类的代码呢

我们一般呢

都是直接参考他给我们提供的例子程序

对吧

然后呢

进行一个相应的改造就可以了

好

那么到这的话呢

咱们这个阿里云呢

基于他这种阿里云策略了实现分片合并了

我们就已经搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程聚焦于一个文件上传服务的“分片合并”功能实现，具体是为阿里云OSS（对象存储服务）设计的分片上传策略。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个具体的策略类 `AliChunkServiceImpl`，该类继承自抽象策略类 `AbstractFileChunkStrategy`。课程内容涵盖了如何初始化 OSS 客户端、初始化分片上传、上传每个分片、排序并完成合并上传，以及最终返回文件的访问 URL。整个过程体现了面向接口编程和策略模式在实际项目中的应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和当前正在编辑的 `AliChunkServiceImpl.java` 文件。
*   **00:05 - 00:15**: 讲师介绍 `AliChunkServiceImpl` 类的作用，即处理阿里云 OSS 的分片文件合并操作。
*   **00:15 - 00:25**: 展示抽象策略类 `AbstractFileChunkStrategy` 的定义，说明其作为所有分片策略的基类。
*   **00:25 - 00:35**: 讲师讲解 `merge` 方法的参数和返回值，该方法是核心业务逻辑。
*   **00:35 - 00:45**: 代码演示：在 `AliChunkServiceImpl` 中调用 `buildClient()` 方法来初始化 OSS 客户端。
*   **00:45 - 00:55**: 展示 `buildClient()` 方法的实现，通过 `FileServerProperties` 获取阿里云配置信息并构建 `OSSClient`。
*   **00:55 - 01:05**: 讲师讲解如何获取文件的存储路径和文件名，用于构建最终的 URL。
*   **01:05 - 01:15**: 代码演示：初始化分片上传，创建 `InitiateMultipartUploadRequest` 对象并调用 `initiateMultipartUpload` 方法。
*   **01:15 - 01:25**: 讲师讲解如何为每个分片创建 `UploadPartRequest`，并上传文件内容。
*   **01:25 - 01:35**: 代码演示：将每个分片的上传结果 `PartETag` 收集到一个列表中。
*   **01:35 - 01:45**: 讲师讲解如何对 `PartETag` 列表进行排序，以便后续合并。
*   **01:45 - 01:55**: 代码演示：创建 `CompleteMultipartUploadRequest` 对象并调用 `completeMultipartUpload` 方法完成合并。
*   **01:55 - 02:05**: 讲师讲解如何构建最终的文件访问 URL，并返回 `R.success(filePo)`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   在 `AliChunkServiceImpl` 类的注释中，明确标注了其功能：“阿里云OSS分片文件处理策略类”。
    *   在 `AbstractFileChunkStrategy` 类的注释中，说明其为“文件分片处理 抽象策略类”。
    *   在 `AliChunkServiceImpl` 的 `merge` 方法注释中，列出了参数和返回值。
    *   在 `buildClient()` 方法注释中，说明了其作用：“构建阿里云OSS客户端”。

*   **关键代码片段**:

    **1. `AliChunkServiceImpl` 类定义**:
    ```java
    public class AliChunkServiceImpl extends AbstractFileChunkStrategy {
        // ... 其他代码 ...
    }
    ```

    **2. `AbstractFileChunkStrategy` 抽象类定义**:
    ```java
    public abstract class AbstractFileChunkStrategy implements FileChunkStrategy {
        @Autowired
        private FileService fileService;
        @Autowired
        protected FileServerProperties fileServerProperties;
        // ... 其他代码 ...
    }
    ```

    **3. `merge` 方法实现**:
    ```java
    @Override
    protected R<File> merge(List<java.io.File> files, String fileName, FileChunksMergeDTO fileChunksMergeDTO) throws Exception {
        OSS client = buildClient();
        String bucketName = properties.getBucketName();
        String relativePath = LocalDate.now().format(DateTimeFormatter.ofPattern(DEFAULT_MONTH_FORMAT_SLASH));
        String relativeFileName = relativePath + StrPool.SLASH + fileName;

        ObjectMetadata metadata = new ObjectMetadata();
        metadata.setContentDisposition("attachment;filename=" + fileChunksMergeDTO.getSubmittedFileName());
        metadata.setContentType(fileChunksMergeDTO.getContextType());

        // 初始化分片上传
        InitiateMultipartUploadRequest request = new InitiateMultipartUploadRequest(bucketName, relativeFileName, metadata);
        InitiateMultipartUploadResult result = client.initiateMultipartUpload(request);
        String uploadId = result.getUploadId();

        // 上传分片
        List<PartETag> partTags = new ArrayList<>();
        for (int i = 0; i < files.size(); i++) {
            java.io.File file = files.get(i);
            FileInputStream in = FileUtils.openInputStream(file);

            UploadPartRequest uploadPartRequest = new UploadPartRequest();
            uploadPartRequest.setBucketName(bucketName);
            uploadPartRequest.setObjectKey(relativeFileName);
            uploadPartRequest.setUploadId(uploadId);
            uploadPartRequest.setInputStream(in);
            uploadPartRequest.setPartSize(file.length());

            UploadPartResult uploadPartResult = client.uploadPart(uploadPartRequest);
            partTags.add(uploadPartResult.getPartETag());
        }

        // 排序
        partTags.sort(Comparator.comparingInt(PartETag::getPartNumber));

        // 完成合并
        CompleteMultipartUploadRequest completeMultipartUploadRequest = new CompleteMultipartUploadRequest(bucketName, relativeFileName, uploadId, partTags);
        CompleteMultipartUploadResult uploadResult = client.completeMultipartUpload(completeMultipartUploadRequest);

        // 构建URL
        String url = new StringBuilder(properties.getUriPrefix())
                .append(relativePath)
                .append(StrPool.SLASH)
                .append(fileName)
                .build();

        // 关闭客户端
        client.shutdown();

        return R.success(filePo);
    }
    ```

    **4. `buildClient()` 方法实现**:
    ```java
    private OSS buildClient() {
        properties = fileServerProperties.getAli();
        return new OSSClientBuilder().build(properties.getEndpoint(),
                properties.getAccessKeyId(),
                properties.getAccessKeySecret());
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：策略模式的引入 (00:05-00:15)**
    讲师首先展示了 `AliChunkServiceImpl` 类，并强调它是一个具体的策略类，用于处理阿里云OSS的分片合并。他指出，通过继承抽象策略类 `AbstractFileChunkStrategy`，可以轻松地为其他云服务（如腾讯云、华为云）添加新的策略，体现了策略模式的灵活性。

*   **场景二：客户端初始化 (00:35-00:45)**
    讲师在 `AliChunkServiceImpl` 中调用 `buildClient()` 方法。他通过 `FileServerProperties` 获取阿里云的配置信息（Endpoint、AccessKeyId、AccessKeySecret），并使用 `OSSClientBuilder` 构建了一个 `OSSClient` 实例。这个客户端是后续所有 OSS 操作的基础。

*   **场景三：分片上传流程 (01:05-01:25)**
    讲师演示了分片上传的核心步骤：
    1.  **初始化**：创建 `InitiateMultipartUploadRequest` 对象并调用 `initiateMultipartUpload` 方法，获取一个唯一的 `uploadId`。
    2.  **上传分片**：遍历文件列表，为每个文件创建 `UploadPartRequest`，并调用 `uploadPart` 方法上传分片内容。每次上传成功后，会返回一个 `PartETag`，它包含了分片号和校验码。
    3.  **收集结果**：将所有 `PartETag` 收集到一个 `List<PartETag>` 中。

*   **场景四：合并与URL生成 (01:35-01:55)**
    讲师演示了如何完成合并：
    1.  **排序**：对 `PartETag` 列表按分片号进行排序，确保上传顺序正确。
    2.  **完成合并**：创建 `CompleteMultipartUploadRequest` 对象，将 `uploadId` 和排序后的 `partTags` 传入，并调用 `completeMultipartUpload` 方法。
    3.  **生成URL**：根据 `properties.getUriPrefix()` 和文件路径，构建最终的文件访问 URL。
    4.  **关闭资源**：调用 `client.shutdown()` 关闭 OSS 客户端，释放资源。

*   **场景五
