# 30-文件服务课程-文件服务开发（接口开发_上传 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们是针对我们不同的文件存储方式啊,我们一共编写了是三种文件策略处理,对吧,分别是本地的,还有FastDFS的,还有阿里云存储的,这么三种策略处理。

好,这些策略处理类呢,写完之后呢,我们就可以啊,来编写我们第一个接口,就是我们这个文件上传,对吧,也就是上传附件,这个接口。

好,首先呢,我们先来明确一下,我们这个上传文件啊,这个接口文档到底是什么样子的。

咱们这个上传附件接口呢,主要完成的呢,有这么两个操作,一个呢,就是将我们客户端提交的文件呢,把它上传到我们指定的存储位置。

那么指定的存储位置呢,是不是可以由我们这个配置文件啊,在这儿来指定,对吧。

咱们这个配置文件在这儿来指定啊,通过我们这个type,是保存在这个fastdfs上面呢,还是这个。

这个local啊,本地啊,还是阿里云呢,对吧。

也就是说我们根据这个配置啊,这样的话呢,就可以把这个文件把它上传到我们指定的存储位置了。

这个是由我们配置文件,是不是配置的策略来确定的。

然后呢,把它存储好之后呢,我们还需要将这个上传的文件信息把它保存到我们的数据库。

具体呢,就是我们这个pd,attachment,就是附件,这张表里面去。

所以说呢,我们当前要开发的这个接口啊,主要要完成的这么两个操作,对吧。

简单来说,一个就是把文件。

文件存好。

第二个呢,就是把这个信息寄入到数据库。

那么具体呢,这个接口文档,它的形式是什么样子的呢?

大家来看啊。

首先呢,我们客户端需要发送的是一个post的方式的请求。

然后呢,请求的地址呢,是这个attachment-upload,对吧。

因为呢,是一个文件上传啊,所以它请求的数据类型呢,是这种multipad form data。

这个大家应该就比较熟悉了。

接口描述呢,就是附件上传。

然后呢,请求参数。

咱们来看啊,有这么几个参数,大家来看一下。

这个file呢,就是我们上传的这个文件,对吧。

其实就是一个附件。

那么请求的这个数据类型呢,就是这个form data。

然后接下来呢,还有什么呢?

为了,因为我们当前提供的这个文件服务啊,它是一个什么呢,相当于是一个文件服务平台。

那么各个业务系统呢,都可以去调我们这个接口来进行文件上传。

那么为了能够区分不同的这个业务,对吧。

那么,我们呢,我们可以去调我们这个接口来进行文件上传。

我们在这个地方呢,提供了这么两个属性啊,这么两个参数。

一个叫做BIZID,这个是业务ID,对吧。

还有一个是业务类型。

这个呢,其实就是用来区分不同的业务的,区分不同的业务。

因为我们传上来这个文件,对吧。

到底这是哪一个系统里面的文件,对吧。

然后呢,这个文件,它代表什么含义。

那么需要通过这两个字段来去进行区分。

然后呢,还有一个是文件的ID,还有一个是文件的ID。

通常情况下,这个文件的ID我们不用去传。

如果传的话呢,就表示是一个修改操作了。

然后呢,最后一个参数呢,就是is single,就是是否是单文件。

因为我们上传的时候呢,可能同时要上传多个文件,对吧。

所以通过这个字段来判断啊,是否是单一的某一个文件。

还是说,我们当前这个业务下边对应的有多个文件。

那么这是我们请求参数啊,需要提交过来的。

然后响应的话呢,

如果我们给客户端啊,这个状态码响应的是这个,响应的是200,对吧。

200,这表示成功。

然后下边这种4001啊,4002啊,03啊等等,这些呢,都是相当于是有问题的。

你看这个4001,就是绘画超时了,对吧。

然后呢,这个0003呢,是缺少token参数等等。

这呢,就是定义的一些这个响应的状态。

这是先把我们这个,先把我们这个接口呢,定义好。

然后呢,还需要注意什么呢?

我们需要给客户端呢,返回的啊,除了有这种状态码之外呢,大家来看。

它其实是封装到了一个R对象里边。

这个R呢,代表的就是return,对不对。

那么这里边呢,返回的是一个叫做,它封装的啊,这个范形是一个什么呢?

attachment DTO。

咱们可以来看一下,叫做attachment DTO。

而这个DTO对象呢,咱们来看。

就在我们这个entity里边。

就这个。

它这边呢,DTO。

当我们来这个进行这个文件上传成功之后,对吧。

需要给我们的客户端呢,返回这么一个对象。

而这个对象里面封装的是什么呢?

哎,你说这里边没有东西啊。

哎,它继承了这个类。

就是我们这个附件类。

所以说呢,需要把这些信息全都返回给我们这个客户端页面。

好,看到了这些。

OK,这是先把我们这个接口文档呢,先来明确一下。

一会儿呢,我们就需要按照我们定义好的这个接口规范。

来开发我们的这个文档。

来开发我们真正的这个接口实现。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段属于一个关于“文件服务”开发的技术课程，主要聚焦于**文件上传接口**的设计与实现。讲师通过文档、代码和配置管理工具，系统地讲解了如何定义一个用于上传附件的RESTful API，包括接口文档规范、数据传输对象（DTO）的设计、以及如何将文件存储到不同的存储服务（如阿里云OSS）中。课程内容覆盖了从接口定义、数据模型设计到具体代码实现的完整流程，旨在指导开发者构建一个健壮、可扩展的文件上传功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:10**: **课程引入与接口文档概览**。讲师在文档编辑器中展示了“5.3 接口开发-上传附件”章节，并重点讲解了“5.3.1 接口文档”部分，明确了上传接口需要完成的两个核心操作：文件上传和元数据存储。
*   **00:10 - 00:25**: **接口参数与响应定义**。讲师详细解读了接口文档中的“请求参数”表格，包括 `file`、`bizId`、`bizType`、`isSingle` 等参数的含义、类型和是否必填。同时，也展示了“响应状态”部分，说明了不同HTTP状态码的含义。
*   **00:25 - 00:45**: **数据传输对象（DTO）设计**。讲师切换到IDE，展示了 `AttachmentDTO` 类的代码。重点讲解了如何使用 `@ApiModel`、`@ApiModelProperty`、`@TableField` 等注解来定义DTO的字段、业务含义和数据库映射关系。
*   **00:45 - 01:00**: **数据模型字段详解**。讲师逐行讲解了 `AttachmentDTO` 中的关键字段，如 `bizId` (业务ID)、`bizType` (业务类型)、`relativePath` (相对路径)、`url` (访问链接)、`icon` (图标)、`createMonth` (创建年月) 等，并说明了每个字段的约束条件（如长度限制）和业务含义。
*   **01:00 - 01:15**: **存储策略与配置管理**。讲师切换到 Nacos 配置中心，展示了 `pd-file-server.yml` 配置文件的内容。该配置文件定义了文件存储的策略，包括使用 `FAST_DFS` 或 `LOCAL` 两种模式，并配置了具体的存储服务地址（如阿里云OSS的 `bucket-name` 和 `access-key-secret`）。
*   **01:15 - 01:30**: **代码实现与存储逻辑**。讲师展示了 `AliServiceImpl` 类中的 `delete` 方法，演示了如何通过 `OSSClient` 对象调用阿里云OSS的 `deleteObject` 方法来删除文件。这暗示了上传文件后，系统会将文件元数据存储到数据库，并将文件本身存储到配置的存储服务中。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **接口文档**: `POST /attachment/upload`，请求类型为 `multipart/form-data`。
    *   **请求参数表**:
        | 参数名称 | 参数说明 | 请求类型 | 是否必填 | 数据类型 | schema |
        | :--- | :--- | :--- | :--- | :--- | :--- |
        | file | 附件 | formData | true | array | MultipartFile |
        | bizId | 业务id | query | false | integer(m64) | |
        | bizType | 业务类型 | query | false | integer(m64) | |
        | isSingle | 是否单文件 | query | false | boolean | |
    *   **响应状态表**:
        | 状态码 | 说明 | schema |
        | :--- | :--- | :--- |
        | 200 | OK | R<AttachmentDTO> |
        | 40001 | 会话超时，需重新登录 | |
        | 40003 | 缺少token参数 | |
        | -1 | 系统繁忙 | |
        | -2 | 服务超时 | |

*   **代码关键内容**:
    *   **`AttachmentDTO` 类定义**:
        ```java
        @Data
        @NoArgsConstructor
        @EqualsAndHashcode(callSuper = false)
        @ApiModel(value = "AttachmentDTO", description = "附件表")
        public class AttachmentDTO extends Attachment implements Serializable {
            // ... 其他字段和注解 ...
            @ApiModelProperty(value = "文件下载地址 根据url下载")
            private String downloadUrlByUrl;
            @ApiModelProperty(value = "文件下载地址 根据id下载")
            private String downloadUrlById;
            @ApiModelProperty(value = "文件下载地址 根据业务id下载")
            private String downloadUrlByBizId;
            @Length(max = 64, message = "文件ID长度不能超过64")
            @TableField("biz_id")
            private String bizId;
            @ApiModelProperty(value = "业务类型")
            @Length(max = 255, message = "业务类型长度不能超过255")
            @TableField("biz_type")
            private String bizType;
            @ApiModelProperty(value = "数据类型")
            @DataType(DIR=图像, VIDEO=视频, AUDIO=音频, DOC=文档, OTHER=其他)
            @TableField("data_type")
            private String dataType;
            @ApiModelProperty(value = "文件相对路径")
            @Length(max = 255, message = "文件相对路径长度不能超过255")
            @TableField("relative_path")
            private String relativePath;
            @ApiModelProperty(value = "文件访问链接")
            @Length(max = 255, message = "文件访问链接长度不能超过255")
            @TableField("url")
            private String url;
            @ApiModelProperty(value = "图标")
            @Length(max = 64, message = "图标长度不能超过64")
            @TableField("icon")
            private String icon;
            @ApiModelProperty(value = "创建年月")
            @Length(max = 10, message = "创建年月长度不能超过10")
            @TableField("create_month")
            private String createMonth;
        }
        ```
    *   **Nacos 配置文件 (`pd-file-server.yml`)**:
        ```yaml
        # FAST_DFS配置
        type: FAST_DFS # LOCAL_ALI_MINIO_FAST_DFS
        urlPref: http://172.17.7.115:8188/ # 存储桶地址
        local:
          urlPref: http://$(pinda.nginx-op):$(pinda.nginx.port)
          bucket-name: oss-file-service
          endpoint: D:/uploadFiles
        ali:
          # 重写可自定义阿里云存储配置
          bucket-name: pinda-bucket
          endpoint: https://oss-cn-beijing.aliyuncs.com/
          access-key-id: LTAI4HmPw1p1sXmQw0G0G0u192hc
          access-key-secret: 5u01GqPwp1p1sXmQw0G0G0u192hc
        ```

---

### 4) 关键场景与演示描述

*   **场景一：接口文档设计**。讲师在文档编辑器中，通过鼠标悬停和点击，引导观众理解接口的请求方法、路径、参数和响应状态。他特别强调了 `file` 参数是 `multipart/form-data` 类型，这是上传文件的标准方式。
*   **场景二：数据模型设计**。讲师在IDE中，通过滚动和高亮，详细解释了 `AttachmentDTO` 类中每个字段的业务含义和注解作用。例如，他解释了 `@ApiModelProperty` 用于描述字段的业务含义，`@TableField` 用于指定数据库字段名，`@Length` 用于设置字段长度限制。
*   **场景三：存储策略配置**。讲师切换到Nacos配置中心，展示了 `pd-file-server.yml` 文件。他通过高亮和滚动，解释了配置文件中 `type` 字段用于指定存储类型（如 `FAST_DFS` 或 `LOCAL`），并详细说明了 `ali` 配置块中 `bucket-name`、`endpoint`、`access-key-id` 和 `access-key-secret` 等参数的用途，用于连接阿里云OSS服务。
*   **场景四：代码实现演示**。讲师展示了 `AliServiceImpl` 类中的 `delete` 方法。他通过高亮和注释，解释了如何通过 `OSSClient` 对象调用 `deleteObject` 方法来删除文件，这体现了系统在文件上传后，如何管理文件的生命周期。
