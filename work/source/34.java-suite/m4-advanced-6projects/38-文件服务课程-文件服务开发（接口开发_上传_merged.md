# 38-文件服务课程-文件服务开发（接口开发_上传 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们再来测试一下,我们把这个文件的处理策略呢,改成阿里云的,咱们来测试一下。

那么我们首先呢,还是来修改配置文件,对吧?

把我们这个文件的存储策略,这个类型改成什么呢?阿里。

改成阿里,好,然后呢,我们重新来发布一下。

重新发布一下,确定。

好,那么发布完之后呢,别忘了,我们这个服务呢,需要重新来启动一下。

重启一下咱们这个文件服务。

好,然后启动完之后呢,我们这次呢,就是把我们这个文件策略修改成了阿里云。

那这样的话呢,我们上传的文件呢,最终是上传到哪儿呢?

就是上传到我们指定的,注意看啊,看阿里云这段配置,对不对?

应该是这段配置,阿里的这段配置。

也就是上传到了我们当前指定的这个,这其实是一个空间的名字,对不对?

然后呢,这是我们这个,相当于是一个前缀啊。

endpoint。

好,咱们来观察一下啊。

呃,看一下我们控制台呢,好像是报错了,对吧?

来看一下是有什么问题啊。

这个地方有一个问题。

attachment service。

创建它的时候呢,attachment service mpr。

哦,这个文件策略对象呢,应该是没有注入进来,对吧?

没有注入进来。

我们来看一下。

文件策略对象没有注入进来。

那说明是阿里这种方式呢,我们当时写的肯定是有问题的。

它其实是在创建我们这个controller的时候,对吧?

创建controller的时候。

好,就是这个地方。

在这里边呢,它是不是想注入一个这个service。

这个service其实是没有问题的啊,因为咱们前面其实都已经测试过了。

应该是什么呢?

在创建这个service对象的时候,这儿是不是要注入一个file,file strategy。

而现在呢,我们希望啊。

它给我们注入的是这个阿里云的这个service,对吧?

应该是这个。

哦,看见没有?

这个地方呢,我们是不是当时少写了一个什么呢?

少加了一个注解,对吧?

也就是这个service注解。

好,如果你不加这个注解的话呢,那这个service是不是就实力化不出来?

其他的service呢,因为我们指定的这个属性它匹配不上,对吧?

所以那些service呢,也没有去这个创建。

好,这是我们当时编写这个阿里云service mpr,对吧?

这个的时候呢,忘了加这么一个service注解。

所以现在呢,启动的时候,它其实就报错了,对吧?

好,那么我们改完之后呢,咱们重新再来启动一下。

那么我们重启一下,来看一下咱们这个控制台。

所以大家启动的时候呢,一定要注意观察这个启动日志啊。

这就是因为我们当时啊,编写这个service类的时候呢,忘了加这个service注解了。

好,现在呢,它正在启动。

然后呢,通过这儿呢,也能看到它加载到的这个从我们这个配置中心呢,

加载到的配置文件,它会输出到我们这个控制台。

方便呢,我们去查看啊。

然后呢,我们可以来看一下当前我们指定的这个file type,对吧?

已经指定成阿里了。

好,但是这个启动过程呢,稍微有一点点慢啊。

好,现在是已经正常启动起来了。

这是我们这个swagger文档的地址。

咱们这边呢,其实已经打开过了。

然后呢,我们可以重新来刷新一下。

好,还是我们这一个接口,对吧?

现在呢,我们来测试一下。

只不过呢,这一次呢,我们就会将这个文件呢,把它上传到我们的阿里云。

好,然后呢,咱们这个bizid呢,随便来一个啊。

比如说我来一个101,对吧?

好,这个呢,我来一个test的。

这个地方呢,我们可以来随便选一个文件来传上去。

嗯,我就还选这个sql文件吧。

咱们其实传什么样的文件都可以。

同样的id跟这个azsingle呢,这两个呢,我都不提交了。

好,然后呢,我们直接点发送。

好,那么这个数据呢,已经返回回来了,对吧?

通过这个地方呢,我们能看到咱们这个状态码是0,对吧?

这就表示我们这个上传是成功的。

然后呢,你看这儿是不是有一个URL地址。

但是这个地址呢,也会保存到我们的数据库里面去啊。

其实我们通过这个地址呢,就可以访问到咱们上传的这个文件。

大家仔细来看这个地址呢,它其实是阿里云给我们提供的这么一个地址,对吧?

阿里云给我们提供的这么一个地址。

好,然后呢,我们可以直接来复制。

下来。

在这儿呢,来访问一下。

哎,你看,通过这个地址,我们是不是就能够加载到这个文件,对吧?

它现在呢,其实是在下载这个文件啊。

好,然后呢,我们可以看一下咱们这个表里边,对吧?

刷新一下,你看,是不是我们这条阿里云的这条保存的这个数据呢,也就查进来了。

好,这个呢,我们通过控制台呢,再来看一下,我们肯定是执行了一条circle语句,对吧?

insert语句。

好,那么通过这儿呢,我们就已经测试过了。

咱们基于阿里云。

这种文件处理方式呢,也是没有问题的。

好,那么关于这个阿里云的测试呢,我们先说到这儿。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频演示了一个基于 Spring Boot 的文件服务（`pd-file-server`）如何集成阿里云 OSS（对象存储服务）进行文件上传。核心流程包括：
1.  **配置中心集成**：使用 Nacos 作为配置中心，动态管理文件服务的配置，包括 OSS 的访问密钥、端点、桶名等。
2.  **服务启动与异常排查**：演示了服务启动失败的场景，通过查看控制台日志定位到 `AttachmentController` 依赖的 `fileStrategy` Bean 未被正确注入。
3.  **策略实现**：通过自定义 `AliOssAutoConfigure` 配置类，实现 `AliServiceImpl`，该类继承自 `AbstractFileStrategy`，用于处理阿里云 OSS 的文件上传逻辑。
4.  **配置注入与动态化**：在 `AliOssAutoConfigure` 中，通过 `@ConditionalOnProperty` 注解，根据配置文件中的 `pinda.file.type` 属性值（如 `ALI`）来决定是否启用阿里云 OSS 策略。
5.  **前端上传测试**：最后，通过 Swagger UI 发起一个 POST 请求，上传文件，验证整个流程的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 Nacos 配置中心界面，编辑名为 `pd-file-server.yml` 的配置文件，其中包含 `file` 配置块，用于定义文件服务的存储类型和相关参数。
*   **00:05 - 00:10**: 切换到 IntelliJ IDEA，展示项目结构，启动 `FileServerApplication`，但控制台报错，提示 `AttachmentController` 依赖的 `fileStrategy` Bean 未找到。
*   **00:10 - 00:15**: 在 IDEA 中查看 `AttachmentServiceImpl.java` 代码，确认其依赖了 `@Autowired FileStrategy fileStrategy;`。
*   **00:15 - 00:20**: 查看 `AliOssAutoConfigure.java` 代码，该类用于配置阿里云 OSS 策略，其中包含 `buildClient` 方法用于构建 OSS 客户端。
*   **00:20 - 00:25**: 在 Nacos 配置中心中，修改 `pd-file-server.yml` 文件，将 `file.type` 设置为 `ALI`，并配置了阿里云 OSS 的 `bucket-name`、`access-key-id`、`access-key-secret` 等参数。
*   **00:25 - 00:30**: 重新启动服务，控制台日志显示成功连接到 Nacos，并加载了配置。
*   **00:30 - 00:35**: 在 IDEA 中，查看 `AliOssAutoConfigure` 代码，确认 `@ConditionalOnProperty` 注解的条件是 `pinda.file.type` 等于 `ALI`。
*   **00:35 - 00:40**: 在 Nacos 配置中心中，再次确认 `pd-file-server.yml` 的配置内容，确保 `file.type` 为 `ALI`。
*   **00:40 - 00:45**: 切换到 Swagger UI，展示文件上传的接口 `/attachment/upload`，并准备上传文件。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：
    *   **`AttachmentServiceImpl.java`**:
        ```java
        @Autowired
        private FileStrategy fileStrategy;
        ```
    *   **`AliOssAutoConfigure.java`**:
        ```java
        @Configuration
        @ConditionalOnProperty(name = "pinda.file.type", havingValue = "ALI")
        public class AliOssAutoConfigure {
            @Service
            public class AliServiceImpl extends AbstractFileStrategy {
                private OSS buildClient() {
                    properties = fileProperties.getAli();
                    return new OSSClientBuilder()
                        .build(properties.getEndpoint(),
                               properties.getAccessKeyId(),
                               properties.getAccessKeySecret());
                }
            }
        }
        ```
    *   **Nacos 配置文件 `pd-file-server.yml`**:
        ```yaml
        file:
          type: ALI # LOCAL ALI MINIO FAST_DFS
          uriPrefix: http://$pinda.nginx.ip:$pinda.nginx.port
          local:
            uriPrefix: http://$pinda.nginx.ip:$pinda.nginx.port
            bucket-name: oss-file-service
            endpoint: D:\uploadFiles
            ali:
              bucket-name: bladex-loan
              access-key-id: LKX4K4HIM4F4E4F4E4F4E4F4E4F4E4F4E
              access-key-secret: SsU1SqPwP1F5h0WcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQcQc
