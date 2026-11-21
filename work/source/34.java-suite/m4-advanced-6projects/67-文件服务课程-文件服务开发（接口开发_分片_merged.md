# 67-文件服务课程-文件服务开发（接口开发_分片 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢咱们是测试了一下

我们这个前端呢

跟后端是完全可以配合起来的

前端呢可以对我们这个文件进行分割

对吧 分多次啊

将一片一片的文件呢

把它上传到我们这个方法

对吧 提交到我们这个方法

然后在这个方法这儿呢

我们就可以继续来写了

那么当然这个地方呢

我们首先肯定还是先来判断一下什么呢

有没有这种特殊情况

比如说这个multipartfile对吧

它是空 对吧

那这种情况呢我们就不用处理了

所以我们一般呢

都是先来判断一些这种非正常情况

比如说这个multipartfile对吧

它如果等于空

或者是什么呢

或者是这个空对吧

multipartfile.什么呢

isempty

那么如果是空的话呢

我们其实就没有必要再去进行处理了

所以直接就返回就可以了

直接return什么呢

this.file

就是什么呢

这个分片上传

就是分片上传

上传

上传

上传

这个的这个分片文件对吧

为空

好

然后呢直接返回这么一个错误提示

就可以了

这个呢是一个非正常的情况了

所以我们尽量还是写的这个

这个完善一点

对吧

就是各种情况都考虑到

好

然后呢我们也可以在这儿使用这个log.error

对吧

来记录一下

好

这是这种情况啊

那么如果一复不成立

那就说明我们上传的这个文件

不为空对吧

那么不为空的话

我们应该怎么处理

所以这个地方呢

我们需要来说明一下

就是说

它这个前端对吧

把这个文件提交到我们这边来

是不是一定会进行分片

其实这个呢不一定

比如说它上传的是一个1k的小文件对吧

而我们在这个地方规定的是什么呢

每片是10兆

所以说呢

它还不足以分为两片对吧

或者多片

那这个时候呢

它其实

相当于只有一片

如果是一片的话呢

我们是不是就把它作为什么呢

普通的文件上传来处理

所以我们在这个地方呢

需要来看一下

来这个判断啊

当前这个上传的文件是否

是分片对吧

也有可能它上传的是一个完整的文件

比如说我们在这个地方呢

可以这样来测一下

咱们把控制台清理一下

然后呢

把我们这边来刷新一下

我现在呢

来传一个小文件

我们先来看

我来传一个小点的文件

比如说呢

我来传一个docs

对吧

然后呢

这儿有个circle

对吧

这个文件呢

很小对吧

只有50多k

然后呢

我们来传一下

然后呢

你可以看到

它是不是只上传了一次

但是它这个地方的显示有问题啊

其实只是上传了一次

咱们可以来看一下

你看这个

是不是接收到分片啊

是不是只提示了这么一次

对吧

只提示了一次

然后呢

我们可以看到

这个分片

这个分片的文件

这个信息

重点看的是后边这个

大家可以来看一下

size

name

这些都没问题

然后呢

这个trunks等于null

trunk等于null

为什么都是空呢

就是因为我们当前上传的这个文件呢

很小对吧

它根本就没有分片

如果没有分片的话呢

这个trunks

还有trunk是不是都是空

都是空

所以啊

我们这个地方呢

需要来判断一下

它是否是分片

还是说就是一个大的

一个完整的文件

对吧

一个完整的文件

所以我们在这呢

如何来判断呢

其实非常简单

刚才也看到了

如果没有分片

这两个属性trunk

还有trunks

是不是都是空啊

所以我们在这呢

就可以来判断一下什么呢

通过这个dto啊

它是封装到我们dto里面来了

对吧

如果这个dto.get什么呢

trunks

这是这个总的分片数

对吧

如果它等于空

对吧

如果等于空

等于null

如果是这种情况

或者

对吧

或者是什么呢

这个

这个.gettrunks啊

它小于等于零

对吧

这就写的完善一点

其实一般情况下呢

我们就写前面这个条件

其实也就足够了

后边这个呢

就是为了能让我们的程序

是不是更保险一些

好

那么如果是这种情况的话呢

这就说明啊

我们当前是不是

当前这个上传呢

是不是没有

没有分片

对吧

没有分片

那这个时候呢

我们就按照什么呢

就按照我们的

普通文件

上传是不是来处理就可以了

好

这是这种情况

然后是else呢

如果是else的话

那是不是在这边就是

当前这个上传属于什么呢

属于分片上传

那么需要按照什么呢

按照我们这个分片

分片上传进行处理

也就是说分片上传

跟这种普通上传的处理方式

肯定是不一样的

按照普通上传处理的

普通文件上传处理

其实这个呢

我们前面都已经写过了

对吧

都已经写过了

好

所以我们这个地方呢

就简单了

咱们直接来注入什么呢

我们那个file strategy就可以了

private

咱们是不是前面定义了

这么一个

接口对吧

顶层接口

file strategy

然后呢

直接out to where的

把它注入进来

那么如果是

if成立了

这就说明是普通上传

普通上传的话呢

我们直接调用什么呢

调用那个

iTunes的

upload的方法对吧

把咱们这个multiple的file

传进去

然后呢

它会给我们返回

这么一个file对象对吧

返回一个file对象

好

然后呢

我们把这个file对象

是不是给它保存了

就可以

好

要保存的话呢

咱们是不是导进来了一个

这个file service啊

但是这块代码呢

咱们没有写

因为我们课上呢

主要写的是附件的

对吧

而这个呢

是针对我们那个网盘服务的

咱们导入了

这么一个service接口

前面已经导入过了

就是这个file service

对吧

所以我们在

在这呢

来把它注进来

file service接口

servc

这个file service接口

把它来注入一下

然后呢

我们这个是按照

普通文件上传

传完之后呢

调用这个什么呢

file service对吧

file service点什么呢

它这里边是不是

给我们提供了一个save方法

然后呢

咱们把这个file对象保存

这个呢

其实就是数据库操作了

就是把这个文件信息

把它插入到数据库

然后呢

我们直接呢

直接return就可以了

直接return什么呢

this.success

然后这里边来传个空就可以

你说为什么要传空呢

因为呢

我们分片上传呢

正常来说应该传的是这个

叫做file tracks merge DTO

因为分片上传完之后啊

下一步

紧接着就是进行合并

对不对

进行合并

你看这些属性呢

都是跟我们后边

进行文件合并相关的

而现在呢

我们走的是义父这个分支

义父分支呢

它其实不是分片上传

所以呢

所以我们在这给个空就可以了

好

咱们就不再去封装这个什么

merge的DTO了

merge其实就是合并的意思

好

这样的话呢

我们这块就写完了

当然了

这个地方呢

还有一个

这里边我们需要在保存之前呢

有一个属性需要来设置一下

就是什么呢

这个文件的MD5值

因为呢

我们这个upload的方法

执行完之后呢

这个file只是封装了

其中的一部分属性

没有封装它的MD5值

所以我们在这个地方呢

需要来设置一下

这个什么呢

set MD5

file MD5

对吧

有人说这个MD5从哪获得呢

MD5呢

从我们这个DTO里面就能获得

这个其实最初呢

是从我们这个

它这个发送请求

你看

发送的这个请求里边

其实就有

咱们可以来看一下

请求的这个参数

这边呢

可能看起来不太方便啊

然后呢

我们从这个控制台来看吧

你看

这边它是不是有这个

MD5

对吧

这第一个MD5

这是我们前端呢

JS给我们提交过来的

所以我们在这呢

直接从DTO里面

就可以把它获取出来

从我们这个file upload DTO

点get什么呢

MD5

然后呢

我们把这个属性给它设置上

再保存就可以了

这是比较简单的一种情况

对吧

就是我们如果上传的是一个小文件

前端呢

因为这个文件很小

对吧

不足以进行切分

所以它就把整个原始大

原始整个文件

对吧

整个文件就已经一次性提交过来了

没有分片

那么如果没有分片

我们就按照普通的这种

这个文件上传来处理

好

那么咱们是先把这个分支呢

写完

写完之后呢

我们一会儿来测试一下这个分支

这个分支测试没有问题

我们继续来写

就是什么呢

分片上传的这个分支

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的文件分片上传功能的开发过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `FileChunkController` 中实现一个 `@PostMapping("/upload")` 接口，用于处理前端传来的文件分片。核心逻辑包括：首先校验上传的分片文件是否为空，然后判断该上传是否为分片上传（通过 `FileUploadDTO` 中的 `chunks` 字段）。如果是普通文件上传，则直接调用 `fileStrategy.upload()` 保存文件并调用 `fileService.save()` 保存文件元数据；如果是分片上传，则需要后续处理。整个过程涉及控制器、DTO、服务层和策略模式的协作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示 `FileChunkController.java` 文件的初始状态，代码中 `uploadFile` 方法的末尾返回 `null`。
*   **00:03 - 00:07**: 开始编写分片上传的校验逻辑，添加 `if (multipartFile == null || multipartFile.isEmpty())` 判断，并调用 `this.fail()` 返回错误。
*   **00:07 - 00:11**: 继续添加逻辑，判断 `fileUploadDTO.getChunks()` 是否为 `null` 或小于等于 0，如果是普通文件上传，则调用 `fileStrategy.upload(multipartFile)`。
*   **00:11 - 00:15**: 在普通文件上传的逻辑中，调用 `fileService.save(file)` 保存文件元数据，并返回 `this.success(data: null)`。
*   **00:15 - 00:19**: 为分片上传的 `else` 分支添加 `return null;`，并展示 `FileUploadDTO` 的结构，其中包含 `name`, `md5`, `chunks` 等字段。
*   **00:19 - 00:23**: 在分片上传的 `else` 分支中，讲师准备编写后续的分片处理逻辑，但视频在此处结束。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **控制器方法**:
        ```java
        @PostMapping("/upload")
        public R<FileChunksMergeDTO> uploadFile(
            @RequestParam(value = "file") MultipartFile multipartFile,
            FileUploadDTO fileUploadDTO) {
            log.info("接收到分片：" + multipartFile + "分片信息：" + fileUploadDTO);
            if (multipartFile == null || multipartFile.isEmpty()) {
                log.error("分片上传的分片文件为空");
                return this.fail(msg, "分片上传的分片文件为空");
            }
            // 判断当前上传的文件是否是分片
            if (fileUploadDTO.getChunks() == null || fileUploadDTO.getChunks() <= 0) {
                // 当前上传没有分片，按照普通文件上传处理
                File file = fileStrategy.upload(multipartFile);
                fileService.save(file);
                return this.success(data: null);
            } else {
                // 当前上传属于分片上传，需要按照分片上传进行处理
                return null;
            }
        }
        ```
    *   **DTO 类 `FileChunksMergeDTO`**:
        ```java
        public class FileChunksMergeDTO {
            @ApiModelProperty(value = "文件唯一名 md5.js 生成的，与后端生成的一致")
            private String name;
            @ApiModelProperty(value = "原始文件名")
            private String submittedFileName;
            @ApiModelProperty(value = "md5", notes = "webuploader 自带的md5算法值，与后端生成的一致")
            private String md5;
            @ApiModelProperty(value = "分片总数")
            private Integer chunks;
            @ApiModelProperty(value = "后缀")
            private String ort;
        }
        ```
    *   **工具类 `BaseController` 中的 `fail` 和 `success` 方法**:
        ```java
        fail(String msg)
        fail(Throwable throwable)
        fail(int code, String msg)
        fail(String msg, Object... args)
        fail(BaseExceptionCode exceptionCode)
        success(T data)
        validFail(String msg)
        ```

---

### 4) 关键场景与演示描述

*   **场景一：初始化与校验** (00:00-00:07)
    讲师首先展示了 `FileChunkController` 中 `uploadFile` 方法的初始代码，其中返回 `null`。随后，他开始编写校验逻辑，通过 `if (multipartFile == null || multipartFile.isEmpty())` 判断上传的分片文件是否为空，并在条件成立时调用 `this.fail()` 返回错误信息，确保上传的合法性。

*   **场景二：分片与普通文件判断** (00:07-00:15)
    讲师接着添加了对 `FileUploadDTO` 中 `chunks` 字段的判断。如果 `getChunks()` 为 `null` 或小于等于 0，表示这是一个普通文件上传，此时调用 `fileStrategy.upload(multipartFile)` 将文件保存到磁盘，并通过 `fileService.save(file)` 保存文件的元数据（如文件名、MD5等），最后返回 `this.success(data: null)` 表示上传成功。

*   **场景三：分片上传处理** (00:15-00:23)
    讲师在 `else` 分支中准备处理分片上传的逻辑，但视频在此处结束。他展示了 `FileUploadDTO` 的结构，其中包含 `name`, `md5`, `chunks` 等关键字段，这些字段将用于后续的分片合并和校验。在 `else` 分支中，他设置了 `return null;`，这通常意味着需要后续的代码来处理分片上传的逻辑，例如将分片文件保存到临时目录，并记录分片信息。

---

**总结**: 本视频片段清晰地展示了如何在 Spring Boot 项目中实现文件分片上传的初步逻辑，包括文件校验、普通文件上传处理和分片上传的分支判断。讲师通过代码演示，逐步构建了文件上传服务的核心功能。
