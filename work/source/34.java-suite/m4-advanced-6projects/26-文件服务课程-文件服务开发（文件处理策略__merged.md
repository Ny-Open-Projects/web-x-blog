# 26-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经啊,把我们这个fastdfs啊,所对应的这个文件上传的这个方法呢,已经编辑好了。

那么接下来呢,我们来实现另外一个呢,就是这个删除文件的方法。

但是删除文件这个方法呢,也是比较简单的。

咱们直接调用什么呢,我们注进来的这个客户端对象就可以了。

好,直接调用这个什么呢,叫做storage client,对吧。

它这里边呢,给我们封装了这么一个方法,就叫做delete file。

delete file。

然后呢,我们根据什么来删呢?

注意,我们当时呢,在进行文件上传的时候,咱们是不是设置了一个叫做group还有一个pass啊。

并且呢,我们还把这两个属性最终是不是保存到数据库啊。

那么这儿的话呢,我们删除的时候,翻过来就需要使用它了。

就是什么呢,delete file,然后把我们这个group name还有pass传进去,就可以了。

而这个group name呢,怎么获得呢?

通过我们传进来这个对象呢,就可以获得啊。

好,点get什么呢?

呃,group吧,对吧。

然后呢,file delete,del.get什么?pass。

好,这就是调用我们这个客户端对象啊。

调用我们fast dfs的客户端对象啊。

客户端对象实现什么呢?文件的这个删除。

所以这个删除的话呢,就非常简单了。

直接调用这个方法,把它需要的这两个参数给它传进去,就可以了。

好,这个呢,是关于我们这个fast dfs文件删除。

好,这个呢,是关于我们这个fast dfs文件删除。

然后呢,我们可以使用这个方法,把这个方法传进去。

好,我们来看一下咱们这个讲义啊。

跟咱们讲义是保持一致的。

然后呢,咱们再对照一下我们的这个什么呢,呃,配置文件,对吧。

因为我们要编写我们的这个客户端代码的话呢,是需要我们配置文件啊,进行支持的。

如果你配置文件配置不正确啊,我们这个Java代码运行的时候呢,就会出现问题。

比如说什么呢?

比如说我们这个地方,我想使用这个storage client,对吧。

就是我们这个客户端对象。

那么之所以我们。

我们现在能够这么编写,能够使用,就是因为在咱们这个配置文件里边呢,我们是不是配置了咱们这个fast dfs。

好,那么这样的话呢,它能够连接到我们这个服务器,对吧。

然后呢,进行相关的操作。

好,所以说这块呢,我们需要注意啊。

还有一个就是什么呢?

我们需要把这个file,它的type设置成什么呢?

fast dfs。

然后呢,还有一个ui prefix,对吧。

这么一个前缀。

而这个前缀其实对应的是什么呢?

这个其实使用的是我们的这个。

呃。

使用的是我们的nginx服务。

使用的是nginx服务。

但是这个服务器呢,是远程的服务器啊。

我们提前都已经搭建好了。

好,然后呢,通过这个前缀呢,最终就能访问到我们fast dfs。

它这个。

它这里边给我们传上去的这些文件。

好。

因为呢,我们这个fast dfs呢,它是需要结合我们nginx提供的http能力来访问我们fast dfs。

这个分布式文件存储系统里边的这些文件呢。

好。

所以说呢,需要这么一个ui prefix。

好。

到这儿的话呢,我们fast dfs呢,这种文件策略的处理类呢,就已经全都实现完成了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个 Java 项目中文件服务模块的开发教学，重点讲解如何使用 FastDFS（一个开源的分布式文件系统）来实现文件的上传和删除功能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了在 `FastDfsServiceImpl` 类中编写 `uploadFile` 和 `deleteFile` 方法的代码逻辑。核心内容包括：如何注入 FastDFS 客户端对象 `FastFileStorageClient`，如何调用其方法完成文件操作，并如何将操作结果（如文件路径、分组等）封装到一个 `File` 对象中，以便后续存储到数据库。视频还展示了如何通过配置文件（如 `application.yml`）来配置 FastDFS 的连接参数。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节是根据画面内容和逻辑顺序进行的划分：

*   **00:00 - 00:05**: 开场，展示项目结构和 `FastDfsServiceImpl` 类的代码，介绍本节将实现文件上传和删除功能。
*   **00:05 - 00:15**: 讲解 `uploadFile` 方法。演示如何注入 `FastFileStorageClient`，并调用其 `uploadFile` 方法上传文件流，获取返回的 `StorePath` 对象。
*   **00:15 - 00:25**: 讲解如何将上传成功的文件信息（如 URL、分组、路径）设置到 `File` 对象中，以便保存到数据库。
*   **00:25 - 00:35**: 讲解 `deleteFile` 方法。演示如何通过 `FileDeleteDO` 对象获取文件的分组和路径，并调用 `FastFileStorageClient` 的 `deleteFile` 方法进行删除。
*   **00:35 - 00:45**: 展示 `FastFileStorageClient` 的 API 文档，说明其 `deleteFile` 方法的参数要求。
*   **00:45 - 00:55**: 讲解如何在配置文件中配置 FastDFS 的连接参数，如 `ip`、`port`、`uriPrefix` 等。
*   **00:55 - 01:05**: 展示 `AliServiceImpl` 的相关配置和代码，作为后续内容的预告。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **文件服务模块结构**：
        *   5.1 环境搭建
        *   5.2 文件处理策略 (包含 5.2.1 FileStrategy, 5.2.2 AbstractFileStrategy, 5.2.3 LocalServiceImpl, 5.2.4 FastDfsServiceImpl, 5.2.5 AliServiceImpl)
        *   5.3 接口开发 - 上传附件
        *   5.4 接口开发 - 根据业务类型/业务id删除附件
        *   5.5 接口开发 - 根据文件id打包下载
    *   **FastDFS 配置说明**:
        *   `pinda:`
            *   `mysql: database: pd_files`
            *   `nginx: ip: ${spring.cloud.client.ip-address}, port: 10000`
            *   `file: type: FAST_DFS, uriPrefix: http://172.17.0.115:8188/`
        *   `#FAST_DFS配置`
            *   `soTimeout: 1500`
            *   `connectTimeout: 600`
            *   `thumb-image: width: 150, height: 150`
            *   `tracker-list: 172.17.0.115:22122`
            *   `pool: max-total: 153, max-wait-millis: 102, jmx-name-base: 1, jmx-name-prefix: 1`

*   **代码关键内容**:

    **`FastDfsServiceImpl.java` - `uploadFile` 方法**
    ```java
    @Override
    public void uploadFile(File file, MultipartFile multipartFile) throws Exception {
        StorePath storePath = storageClient.uploadFile(multipartFile.getInputStream(), multipartFile.getSize(), multipartFile.getOriginalFilename());
        file.setUrl(fileProperties.getUriPrefix() + storePath.getFullPath()); // 设置文件访问URL
        file.setGroup(storePath.getGroup()); // 设置文件分组
        file.setPath(storePath.getPath()); // 设置文件路径
    }
    ```

    **`FastDfsServiceImpl.java` - `deleteFile` 方法**
    ```java
    @Override
    public void delete(FileDeleteDO fileDeleteDO) {
        storageClient.deleteFile(fileDeleteDO.getGroup(), fileDeleteDO.getPath());
    }
    ```

    **`FastFileStorageClient` API 文档 (部分)**:
    *   `deleteFile(String groupName, String path)`
    *   `uploadFile(InputStream inputStream, long fileSize, String fileExtName, Set<MetaData> metaDataSet)`
    *   `deleteFile(String groupName, String path)`
    *   `uploadImage(FastImage fastImageFile)`
    *   `uploadImageAndCrtThumbImage(InputStream inputStream, long fileSize, String fileExtName, Set<MetaData> metaDataSet)`

---

### 4) 关键场景与演示描述

*   **场景一：上传文件逻辑演示**
    *   讲师在 `FastDfsServiceImpl` 类中，通过 `@Autowired` 注入 `FastFileStorageClient` 对象。
    *   在 `uploadFile` 方法中，调用 `storageClient.uploadFile(...)` 方法，传入文件流、文件大小和文件名，获取返回的 `StorePath` 对象。
    *   随后，讲师将 `StorePath` 对象中的 `getFullPath()`、`getGroup()` 和 `getPath()` 方法的返回值，分别设置到 `File` 对象的 `setUrl()`、`setGroup()` 和 `setPath()` 方法中，完成文件信息的封装。

*   **场景二：删除文件逻辑演示**
    *   讲师在 `deleteFile` 方法中，首先通过 `fileDeleteDO.getGroup()` 获取文件分组。
    *   然后通过 `fileDeleteDO.getPath()` 获取文件路径。
    *   最后调用 `storageClient.deleteFile(group, path)` 方法，完成文件的删除操作。

*   **场景三：配置文件讲解**
    *   讲师切换到 PPT，展示 `application.yml` 文件中 `pinda` 和 `file` 配置块。
    *   重点讲解 `file.type: FAST_DFS` 和 `file.uriPrefix` 的配置，说明这是为了使用 FastDFS 作为文件存储服务。
    *   展示 `#FAST_DFS配置` 下的 `soTimeout`、`connectTimeout`、`tracker-list` 等参数，说明它们是 FastDFS 客户端连接的必要配置。

*   **场景四：API 文档查阅**
    *   讲师在代码中点击 `storageClient.deleteFile(...)` 方法，弹出其 API 文档。
    *   通过文档确认 `deleteFile` 方法需要传入 `groupName` 和 `path` 两个参数，与代码中的逻辑一致。

*   **场景五：错误提示与修正**
    *   在编写 `deleteFile` 方法时，IDE 提示 `FastFileStorageClient` 不能应用于 `FileDeleteDO` 类型。
    *   讲师通过查看 `FileDeleteDO` 类的结构，确认其包含 `getGroup()` 和 `getPath()` 方法，从而修正了代码，确保类型安全。
