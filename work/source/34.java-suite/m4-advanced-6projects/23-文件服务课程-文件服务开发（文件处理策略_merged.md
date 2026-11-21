# 23-文件服务课程-文件服务开发（文件处理策略 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经完成了我们这个本地文件处理策略的第一个方法,也就是这个upload file,文件上传的这个方法。

好,那么接下来呢,我们就需要来完成下一个,就是我们这个文件删除的这个方法。

那么要删除文件的话呢,我们可以来看到,这个方法呢,给我们传进来了这么一个参数啊。

那么这其实就是这么一个预模型对象,对吧,file delete do。

那么要删除文件的话呢,我们传进来这么多参数。

好,那么具体到这个地方呢,咱们是要从本地磁盘,也就是我们这个服务器上的一个本地磁盘,来删除我们这个文件。

所以首先呢,我们需要来获得什么呢,或者来这个拼接啊,拼接我们这个要删除的这个文件的这个什么呢,绝对路径,对吧,绝对磁盘路径啊,磁盘路径。

好,然后呢,再把它分析。

然后呢,把它封装成一个file对象,对吧,然后进行删除。

好,这个绝对磁盘路径具体应该如何拼接呢?

哎,咱们前面呢,在做文件上传的时候呢,其实也已经提到过了,我们这个文件当时是如何存储的呀?

首先呢,我们是不是先从咱们这个配置文件里面来读取什么呢?

咱们来看啊,这个PDFileServer,来读取到我们这么一个,叫做endpoint,对吧,endpoint。

这个呢,就是相当于把我们所有的要上传的文件放在这个地盘upload files,我们配置的这个目录下边,对吧。

当然了,在这个目录下边呢,我们又通过这个bucket name是不是又封装了一层目录,对吧,也就是说又分割了一层目录。

然后在这层目录下边,再按照我们的年跟月是不是来划分两层目录。

最终呢,我们这个文件呢,是放在了我们这个月份所对应的目录里边。

哎,所以说呢,我们现在要删除了这个目录。

哎,所以说呢,我们现在要删除了这个目录。

删除的话呢,肯定也是由这几部分来构成的。

所以我们来看,首先呢,我们需要来获得什么呢?

通过我们这个properties,properties.get什么呢?

叫做endpoint,endpoint,就是刚才我们看到的这个,对吧。

这样的话,我是不是就能拿到后边配置的这个磁盘路径了,对吧。

这是这个,然后呢,刚才我们提到还有一部分就是这个什么呢?

咱们先给它结束一下,properties.get什么呢?

叫做8.

bucket name,对吧,bucket name。

好,然后呢,这个对应的就是我们刚才看到的,

哎,上面这个配置,bucket name。

它其实也是一个目录结构,好。

然后呢,再往下呢,是不是应该就是我们的年跟月,对吧。

年跟月的话呢,这个应该如何获取呢?

哎,注意啊,这个通过我们properties这个就获取不到了。

你看我们是不是在这里边并没有去配置什么年月。

因为它是,我们不可能在这儿去配置死。

它应该是在我们这个程序当中,

我们的这个动态来获取,对吧。

那这个地方呢,它其实是通过这个对象呢,给我们传进来的。

好,叫get什么呢?

呃,叫做相对路径,对吧。

叫relative path。

好,那么这个路径呢,是因为我们当时啊,在这个地方是不是已经给它这个设置好了,对吧。

已经设置好了。

而这个related path呢,其实对应的,大家来看一下,就是我们当时的这个日期目录,对吧。

哎,年月。

好。

所以说现在呢,我们,哎,翻过头来给它取出来。

取出来。

然后最后呢,再追加上我们这个文件名,对吧。

文件名的话呢,也是通过我们传进来这个对象啊,给进来的。

所以我们在这儿直接get什么呢?

filename就可以啊。

filename。

呃,需要注意的是什么呢?

这个filename呢,实际上是我们通过UUID生成的那个随机的文件名。

而不是它原始上传的文件名。

好。

其实我们把这四部分给它拼接到一块呢,就构成了我们要删除的这个文件,它的绝对的磁盘路径。

好。

呃,但是这个拼接的话呢,

我们就不建议自己去拼接了。

咱们直接什么呢?

直接还是使用我们这个pass啊。

前面我们已经用过多次了,对吧。

pass。

好,对象。

然后点什么呢?

get。

然后呢,把这四部分啊,全都放进去。

把这四部分,哎,这是第一部分。

按照顺序啊,不要放错了。

然后呢,第二部分就是我们这个bucket name。

好。

然后呢,第三部分呢,就是咱们这个相对目录,对吧。

相对目录呢,我们使用的是年月来进行分割的。

最后呢,

是我们这个文件名称。

哎,文件名称。

把这四部分啊,把它拼接到一块。

然后呢,就构成了我们这个文件它的一个什么呢?

呃,绝对的磁盘路径,对吧。

咱们就叫file path吧。

呃,当然了,这个地方呢,我们需要给它转成字符串啊。

所以说呢,还得来toString一下。

好,最后呢,忘了一个toString,对吧。

好,这样的话呢,就构成了我们这个要删除的这个文件,它的绝对的磁盘路径。

好,那接下来呢,我们是不是就可以啊,把这个file path这个磁盘路径呢,给它封装一下。

封装成一个什么呢?

呃,file对象,对吧。

file对象。

好,注意这个file不要导错了啊。

应该是我们这个java.io的这个file,对吧。

好,等于什么呢?

直接new一个file就可以了。

当然,这也需要是java.io.file,对吧。

好,然后呢,把我们这个路径呢,给它放进去。

叫做file path吧。

好,这样的话,我们这个文件呢,是不是就已经构造好了。

接下来是不是把这个文件给删了就可以了。

好,咱们其实可以调用file.delete,对吧。

那么我们这个地方呢,也可以使用什么呢?

file utils,就是这个工具类,对吧。

file utils,工具类啊,它这里边呢,就有一个delete方法。

好,叫做delete.query,然后呢,把我们这个file传进去。

好,这样呢,使用工具类啊,给我们提供的这个删除方法。

将当前这个文件呢,把它删除掉,就可以了。

好,那么这就是我们这个进行文件删除啊,这个地方。

那么需要注意的是什么呢?

大家可以来看一下,我们这个本地啊,策略处理类。

这里边这个删除方法,还有文件上传方法。

他们呢,就是关注于我们真正的这个文件上传删除。

而关于我们前面提到过的啊,我上传之后是不是要保存数据。

然后呢,我这个地方删除完文件之后呢,

可能也需要去操作数据库,对吧?

那么对于这些数据库操作,不应该出现在我们当前这个类里面。

哎,那么这个呢,那些呢,进行数据库操作的呢,

应该是属于我们业务层的代码的封装,对吧?

而我们当前这个类呢,只是专注于我们这些文件的处理。

比如说文件的删除,文件的上传。

好,这是我们当前这个类啊,最核心的这两个功能。

好,那么关于咱们这个本地的啊,这个文件策略处理类呢,

我们就已经全都开发完成了。

好,那我们就先来看看这个文件吧。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于 Java 文件服务（File Server）的实战开发教程，重点演示了如何实现文件的上传和删除功能。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了如何在本地文件系统中操作文件，并结合配置中心（Nacos）管理配置。视频内容涵盖了文件实体类（`FileDeleteDO`）的设计、配置属性的读取、文件路径的拼接、以及使用 `java.io.File` 和 `FileUtils` 工具类进行文件操作。整个过程旨在展示一个典型的、可扩展的文件服务模块的实现方式。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的时间点，以下章节是根据画面内容和逻辑顺序进行的划分：

*   **章节 1: 项目环境与配置中心 (Nacos)**
    *   **内容**: 展示了 Nacos 配置中心的界面，用于管理文件服务的配置信息（如端点、存储桶名等）。
    *   **画面**: Nacos 网页界面，显示“配置详情”页面，正在加载。

*   **章节 2: 文件删除功能实现**
    *   **内容**: 讲解如何在 `LocalAutoConfigure.java` 中实现文件删除功能。
    *   **画面**: IDE 中 `LocalAutoConfigure.java` 文件，光标位于 `delete(FileDeleteDO fileDeleteDO)` 方法内。
    *   **关键步骤**:
        *   通过 `properties.getEndpoint()` 和 `properties.getBucketName()` 获取配置。
        *   通过 `fileDeleteDO.getRelativePath()` 获取文件相对路径。
        *   使用 `Paths.get(...)` 拼接出文件的绝对路径。
        *   使用 `new java.io.File(...)` 创建文件对象。
        *   调用 `FileUtils.deleteQuietly(...)` 方法删除文件。

*   **章节 3: 文件上传功能实现**
    *   **内容**: 讲解如何在 `LocalServiceImpl.java` 中实现文件上传功能。
    *   **画面**: IDE 中 `LocalServiceImpl.java` 文件，光标位于 `uploadFile(File file, MultipartFile multipartFile)` 方法内。
    *   **关键步骤**:
        *   调用 `buildClient()` 方法初始化客户端。
        *   从配置中获取 `endpoint`、`bucketName` 和 `uriPrefix`。
        *   生成文件名（使用 UUID）。
        *   拼接文件的绝对路径。
        *   创建 `java.io.File` 对象。
        *   使用 `FileUtils.writeByteArrayToFile(...)` 将文件内容写入磁盘。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1: `FileDeleteDO` 实体类**
    ```java
    private String path; // fastdfs 的路径
    private String fileName; // 唯一文件名
    private String relativePath; // 文件在服务器的相对路径
    private Long id;
    private Boolean file; // 是否是云盘文件删除
    ```

*   **代码片段 2: `LocalAutoConfigure.java` 中的 `delete` 方法**
    ```java
    @Override
    public void delete(FileDeleteDO fileDeleteDO) {
        // 拼接要删除的文件的绝对磁盘路径
        String filePath = Paths.get(properties.getEndpoint(), properties.getBucketName(), fileDeleteDO.getRelativePath());
        java.io.File file = new java.io.File(filePath);
        FileUtils.deleteQuietly(file);
    }
    ```

*   **代码片段 3: `LocalServiceImpl.java` 中的 `uploadFile` 方法**
    ```java
    @Override
    public void uploadFile(File file, MultipartFile multipartFile) throws Exception {
        buildClient();
        String endpoint = properties.getEndpoint();
        String bucketName = properties.getBucketName();
        String uriPrefix = properties.getUriPrefix();

        // 使用UUID为文件生成新文件名
        String fileName = UUID.randomUUID().toString() + StrPool.DOT + file.getExt();

        // 日期目录
        String relativePath = Paths.get(LocalDate.now()).format(DateTimeFormatter.ofPattern(DateUtils.DEFAULT_MONTH));

        // 目标输出文件：D:\uploadFiles\oss-file-service\2020\05\xxx.doc
        String absolutePath = Paths.get(endpoint, bucketName, relativePath).toString();
        java.io.File outFile = new java.io.File(Paths.get(absolutePath, fileName).toString());
        FileUtils.writeByteArrayToFile(outFile, multipartFile.getBytes());
    }
    ```

*   **关键配置属性**:
    *   `endpoint`: 文件服务的端点。
    *   `bucketName`: 存储桶名称。
    *   `uriPrefix`: URI 前缀。
    *   `fileDeleteDO.getRelativePath()`: 文件的相对路径。

---

### 4) 关键场景与演示描述

*   **场景 1: 配置中心 (Nacos)**
    *   **描述**: 讲师首先展示了 Nacos 配置中心的界面，说明了如何将文件服务的配置（如端点、存储桶名等）集中管理。这为后续代码中读取配置提供了背景。

*   **场景 2: 文件删除功能开发**
    *   **描述**: 讲师在 IDE 中逐步编写 `delete` 方法。他首先获取配置信息，然后通过 `Paths.get(...)` 方法将配置信息和文件相对路径拼接成一个完整的文件路径。接着，他创建了一个 `java.io.File` 对象，并调用 `FileUtils.deleteQuietly(...)` 方法来删除文件。这个过程清晰地展示了如何在本地文件系统中执行文件删除操作。

*   **场景 3: 文件上传功能开发**
    *   **描述**: 讲师在 `LocalServiceImpl.java` 中编写 `uploadFile` 方法。他首先初始化客户端，然后获取配置信息。接着，他生成一个唯一的文件名（使用 UUID），并根据当前日期创建一个目录。最后，他拼接出文件的完整路径，并使用 `FileUtils.writeByteArrayToFile(...)` 方法将上传的文件内容写入到磁盘上。这个过程展示了如何实现文件的上传和存储。

*   **场景 4: 代码调试与运行**
    *   **描述**: 在 `main` 方法中，讲师通过 `Paths.get(...)` 拼接路径并打印出来，用于调试和验证路径拼接的正确性。这体现了在开发过程中对路径和文件操作的验证。

---

以上是根据您提供的视频画面进行的结构化分析。希望对您有所帮助。
