# 29-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经把我们这个upload file,就是文件上传的这个方法呢,已经编写完了。

那么需要注意的有一点呢,这个地方呢,我们来看一下,刚才呢,我们是在拼接这个URL地址的时候,对吧?

就是文件上传完成之后啊,来拼接这个URL地址,然后呢,我们这个前缀呢,是这样用的,就是get URI prefix。

而这个方法呢,我们其实调用的是咱们这个抽象的附类里边给我们提供的这个方法。

那么对于我们当前这个阿里云存储呢,我们需要把这个方法来覆盖一下,也就是在我们当前这个子类里面来覆盖一下。

那么为什么?就是因为我们这个阿里云这块呢,它这个访问呢,有可能并不是这种http的,有可能使用的是这种什么呢,安全协议,也就是https,对不对?

所以说呢,我们。

这块呢,需要在咱们这个子类里面去覆盖一下,然后呢,动态的去判断。

也就是说,我们在这一块,咱们先把这个方法来复制过来,复制到我们当前这个子类,也就是阿里云,这里面来。

然后呢,我们来看一下,咱们就放在这个位置就可以了。

你看,StreetUtils呢,我们需要来这个导入一下。

好,咱们来看一下,这个方法名呢,还叫做get URI prefix。

这样的话呢,它是不是就会把附类里面这个给覆盖掉了。

然后呢,我们现在这个地方调用的这个get URI prefix这个方法呢,其实调用的就是我们自己子类里面这个方法。

然后呢,这个方法呢,同样,前面这句是一样的,先来判断啊,URI prefix,对吧,是否配置了。

如果配置了的话呢,我们就直接用它。

其实对于我们当前这个来说呢,咱们是不是没有配置了。

那么如果没有配置的话呢,它肯定就要走else了,对不对?

else的时候呢,它就会通过。

通过这个properties.get and point,咱们弄成一行啊,get and point。

这个得到的是谁呢?

得到的其实应该就是我们这个,这段,我选中的这段,对不对?

然后呢,它根据这段呢,来判断一下是否包含https,对不对?

是否包含https。

那么如果是https的话呢,最后它的取值是不是就是这段。

这就是我们这个prefix。

否则的话呢,取值就是这段。

也就是说它会动态的去选择这么一个协议,对不对?

到底是普通的http还是这个安全的https加密的这种协议。

然后呢,我们再把这个前缀,也就是说不管是这段还是这段,对吧?

把它这个拼接起来,然后前缀加上什么呢?

加上我们这个bucket name,对吧?

加上bucket name。

bucket name呢,是不是应该就是我们这个这段,对吧?

就是这段。

然后呢,再加上一个点。

然后呢,再来拼接什么呢?

拼接我们这个endpoint呢。

然后呢,把前面这段呢,给它替换掉,就可以了。

最终呢,它其实就是做了一个字符串的这么一个拼接啊。

这个呢,是针对我们阿里云这个配置它的特点呢。

所以我们在这个地方呢,又重新覆盖了一下

附类里面的这个get ui prefix这个方法。

那么一会儿呢,我们后边就可以启动环境啊,

来测试了。

好,那么我们测到这个地方的时候呢,

再具体可以加段点来跟一下。

好,然后呢,就是把这个方法给覆盖掉。

那么再往下呢,就是关于我们这个阿里云,对吧?

存储它的删除文件的方法。

删除文件的话呢,我们刚才也看到了,

在它这个示例代码这儿,对吧?

删除文件,它其实调用的是这么一个叫做delete object啊,

这么一个方法。

好,然后呢,咱们直接啊,

把我们讲义上的这个删除的方法拿过来,

就可以了。

好,直接考到这儿来。

那来看一下,首先呢,我们还是build client,对吧?

来构建这么一个OSS客户端对象。

然后呢,通过properties get bucket name,对吧?

然后这样的话,就可以把我们这个bucket name,

把这个值给取到了。

这是其实是一个空间名,对吧?

空间名称。

然后呢,我们就可以调用这个delete object的方法,

把它删除掉。

除了要指定我们从这个空间里面去删,对吧?

然后呢,还要指定这个文件,

它所在的这个什么呢?

相对路径,以及什么呢?

以及它这个,其实就一个相对路径就可以了。

这个相对路径呢,它是怎么拼接成的呢?

它是,这样啊,我们给它整理一下。

这块呢,因为我们前面在进行文件上传之后呢,

是不是都已经给它这个保存到数据库了,对不对?

那么最终呢,是这么一个related path。

所以现在呢,我们就可以翻过头来,

然后呢,把它拼接过来。

但是这个地方为什么会报错呢?

就是因为,

这个地方命名不一样啊。

好,把这儿改过来就可以了。

file.getrelatedpath,这个呢,其实是一个相对路径。

然后呢,加上什么呢?

加上我们这个,这其实是一个斜线。

然后呢,再加上我们这个文件名,对不对?

filename,好,这样来删除。

咱们可以来看一下它这个事例代码,你看。

它在进行删除的时候呢,

它是封装成这么一个对象,对吧?

叫做object name。

而这个object name呢,

其实它是我们这个文件,

文件后缀在内的,包含文件后缀在内的完整的路径名,

就类似于这样,你看,它给我们这么一个东西。

所以说呢,我们现在给它传进来的呢,

就是在拼这么一个串。

这个路径,然后加上斜线,加上文件名。

跟它提供的这个例子呢,其实是一回事啊。

这么一个效果。

好,那么到这儿的话呢,我们就已经把这个文件给删除掉了。

删除完之后呢,别忘了,

把这个客户端对象是不是给它关闭掉,就可以了。

好。

那么到这儿的话呢,我们整个这个阿里云存储相关的这个文件策略的处理类呢,

就已经编写完成了。

那么对应的呢,是需要咱们这个配置文件啊,这样来配合使用的。

那么关于这个阿里云文件策略呢,我们先说到这儿。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个基于 Spring Boot 的文件服务模块，主要讲解如何集成阿里云对象存储服务（OSS）来实现文件的上传与删除功能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了核心代码的编写过程，包括：
- **文件上传**：创建 `PutObjectRequest` 对象，设置对象元数据（如文件名、类型），并调用 `client.putObject()` 方法上传文件。
- **文件删除**：通过 `client.deleteObject()` 方法删除指定路径的文件。
- **URL 生成与处理**：在文件上传后，生成可访问的文件 URL，并将其信息写入数据库实体对象中。
- **配置管理**：讲解了如何在配置文件（如 `panda.yml`）中配置阿里云 OSS 的访问凭证和端点信息。
- **代码结构**：展示了采用策略模式（Strategy Pattern）设计的文件服务，包括抽象策略接口 `AbstractFileStrategy` 和具体实现类 `AliServiceImpl`。

整个课程旨在教授开发者如何在实际项目中，利用阿里云 OSS 服务进行文件管理，并通过代码实现业务逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于截图中未提供明确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程开场，介绍文件服务的整体架构和本次课程的目标。
*   **00:30 - 01:00**：讲解文件上传的核心代码逻辑，包括生成文件名、构建 `PutObjectRequest`、设置元数据和执行上传。
*   **01:00 - 01:30**：演示文件上传后的 URL 生成过程，以及如何将 URL 和文件信息写入数据库实体。
*   **01:30 - 02:00**：讲解文件删除的代码实现，包括构建 OSS 客户端和调用 `deleteObject` 方法。
*   **02:00 - 02:30**：展示如何在配置文件中配置阿里云 OSS 的访问信息。
*   **02:30 - 03:00**：总结代码结构，强调策略模式的应用，并展示 `AbstractFileStrategy` 和 `AliServiceImpl` 的关系。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文件服务架构图**：在 Typera 文档中，展示了文件服务的目录结构，包括 `FileStrategy`、`AbstractFileStrategy`、`LocalServiceImpl`、`FastDsServiceImpl` 和 `AliServiceImpl` 等模块。
*   **配置文件示例**：在 `panda.yml` 文件中，展示了如何配置数据库、Nginx 和阿里云 OSS 的信息，例如：
    ```yaml
    panda:
      database: pd_files
      nginx:
        ip: ${spring.cloud.client.ip-address}
        port: 10000
    file:
      type: ALI
      ali:
        bucket-name: bladex-loan
        endpoint: http://oss-cn-qingdao.aliyuncs.com
        access-key-id: LTAI4fhtm...GJ5J1uI
        access-key-secret: SSUJ5QapP...Gy92Fnc
    ```

#### 代码关键内容

*   **文件上传核心代码**：
    ```java
    // 创建对象元数据
    ObjectMetadata metadata = new ObjectMetadata();
    metadata.setContentDisposition("attachment;filename=" + file.getSubmittedFileName());
    metadata.setContentType(file.getContextType());

    // 构建上传请求
    PutObjectRequest request = new PutObjectRequest(bucketName, relativeFileName, multipartFile.getInputStream(), metadata);

    // 执行上传
    PutObjectResult result = client.putObject(request);

    // 生成文件 URL
    String url = getUriPrefix() + StrPool.SLASH + relativeFileName;
    url = StrUtil.replace(url, searchStr: "\\\\", StrPool.SLASH);
    url = StrUtil.replace(url, searchStr: "\\", StrPool.SLASH);

    // 写入文件表
    file.setUrl(url);
    file.setFilename(fileName);
    file.setRelativePath(relativePath);
    file.setGroup(result.getETag());
    file.setPath(result.getRequestId());

    // 关闭 OSS 客户端
    client.shutdown();
    ```

*   **文件删除核心代码**：
    ```java
    // 删除文件
    OSS client = buildClient();
    String bucketName = properties.getBucketName();
    client.deleteObject(bucketName, file.getRelativePath() + StrPool.SLASH + file.getFileName());
    ```

*   **URL 前缀生成方法**：
    ```java
    protected String getUriPrefix() {
        if (StringUtils.isNotEmpty(properties.getUriPrefix())) {
            return properties.getUriPrefix();
        } else {
            String prefix = properties.getEndpoint().contains("https://") ? "https://" : "http://";
            return prefix + properties.getBucketName() + "." + properties.getEndpoint().replaceFirst(prefix, "");
        }
    }
    ```

*   **OSS 客户端构建方法**：
    ```java
    return new OSSClientBuilder()
        .build(properties.getEndpoint(),
               properties.getAccessKeyId(),
               properties.getAccessKeySecret());
    ```

---

### 4) 关键场景与演示描述

*   **场景一：文件上传流程演示**
    讲师在 IntelliJ IDEA 中，逐行展示如何构建 `PutObjectRequest` 对象。他首先创建 `ObjectMetadata` 并设置文件名和类型，然后使用 `bucketName`、`relativeFileName` 和文件输入流构建请求对象，最后调用 `client.putObject()` 方法完成上传。上传成功后，他演示了如何从 `PutObjectResult` 中获取文件的 ETag 和请求 ID，并生成最终的访问 URL。

*   **场景二：文件删除流程演示**
    讲师展示了如何在 `delete` 方法中构建 OSS 客户端，并调用 `deleteObject` 方法删除指定路径的文件。他强调了删除操作需要传入正确的存储空间名称和文件路径。

*   **场景三：配置文件讲解**
    讲师切换到 Typera 文档，展示了 `panda.yml` 配置文件的内容，重点讲解了如何配置阿里云 OSS 的 `endpoint`、`access-key-id` 和 `access-key-secret`。他提醒观众在正式环境中需要使用正确的配置信息。

*   **场景四：代码结构与策略模式**
    讲师在 IDE 中展示了 `AbstractFileStrategy` 接口和 `AliServiceImpl` 类的代码，解释了策略模式如何让系统能够灵活地支持不同的文件存储服务（如本地存储、阿里云 OSS 等）。他通过高亮代码，强调了 `getUriPrefix()` 方法在不同实现类中的作用。

*   **场景五：阿里云 OSS 官方文档参考**
    讲师在浏览器中打开了阿里云 OSS 的官方文档，展示了删除文件的示例代码，以验证自己实现的正确性。他指出，官方文档中的代码与自己实现的逻辑是一致的。

---

以上是根据视频画面截图整理出的结构化信息，希望能帮助您更好地理解这段技术课程的内容。
