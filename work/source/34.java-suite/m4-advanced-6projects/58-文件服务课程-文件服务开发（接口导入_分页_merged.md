# 58-文件服务课程-文件服务开发（接口导入_分页 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们文件服务的开发

这个小节我们是导入其他接口代码

因为我们这个课程重点讲解的其实是文件的上传下载

还有文件处理策略这些实现

这些咱们前面都已经实现过了

还有一些纯数据库的操作

比如说一些分页查询

根据各种条件查询等等

这些不再作为我们课程的重点

所以说我们对于这一类的纯数据库操作的这些代码

咱们直接导入到我们这个项目里面来就可以了

首先我们导入的是什么呢

分页查询复建

也就是说我们来查询一下

看看我们当前复建表里面一共有多少条数据

然后分页进行一个展示

所以说我们对于这种纯数据库操作的

数据库操作增伸改查的

那么直接把这个代码直接导到我们项目里面来就可以了

首先是我们controller里面的代码

那么有这么一个叫做page

这么一个方法

一看是不是就是进行分页查询的

然后咱们直接把这个方法

把它拷到我们项目里面来

找到controller

咱们需要把这个类来导入一下

但这个地方的报错

是因为我们现在接口里面还没有这个方法

咱们可以大概来看一下

这是我们这个分页查询复建

重新加一下

这个是我们分页查询复建

然后我们传过来的参数是什么

传过来的参数其实是这个

叫做file page request dto

都是跟我们查询条件相关的

查询条件相关的

但是有些人可能比较奇怪

就是什么呢

我们这里边好像这个

没有跟我们这个分页条件相关的

比如说我们的页码查询多少条

为什么没有

这个地方其实我们是通过

什么

是通过这个get page来获得的

而这个是进行了封装

这个get page是在哪呢

是在我们这个base controller当中

大家可以看到base controller当中

然后它在这里边

有这么一个get page方法

然后在这边

你看是不是进行的这个分页数据的封装

所以说它是统一抽取了

抽取到我们base controller当中

来进行这个封装

因为这里边它其实是注入了什么呢

注入了我们的这个

你看request对吧

还有response

对象对吧

所以说呢

它是在base controller当中

把我们这个分页相关的数据呢

把它收集到

所以并不是在我们当前

这个controller当中收集的

它是在复利里边

这样是为了

让我们可能多个地方都需要进行分页

所以说呢

直接继承base controller

这些重复的代码呢

就不用再写了

这个简单看一下就可以了

然后接下来呢

我们是不是需要在咱们这个

attachment service接口里边

来提供这个方法呢

来提供这个方法呢

直接把我们这个方法

拷过来

然后呢

找到我们这个接口

这是分页查询的对吧

分页查询的

这个呢

我们需要来导入一下

好

你看controller这边呢

就没有问题了

对吧

然后接下来呢

我们是不是需要来

这个到它的实现类里边呢

来实现这个方法

这个方法呢

咱们也是直接拷过来就可以了

好

这些呢

其实都是一些纯数据混合的

这个方法呢

我们可以直接去

把这个方法呢

用到这个库子操作

这个地方呢

它是不是要用到一个dozer对象

这个地方呢

它是不是要用到一个dozer对象

所以我们需要给它

咱们这个已经注进来了

对吧

只不过起名的不一样

叫做dozer utils

然后呢

我们把这儿给它改造一下

就可以了

改成dozer utils

好

那么整个这个代码呢

我们就都

我们就都

这个拷过来了

对吧

然后呢

它只不过这个地方呢

这个查询的条件呢

全都是like查询啊

like查询对吧

根据什么呢

根据原始文件名

根据BIZ type

BIZ ID对吧

还有Data type等等

这些

这些各种各样的查询条件

最终呢

就要用我们base mapper的

这个分页查询方法

来进行一个分页查询

好

这是关于我们复建的分页查询

然后导入完之后呢

咱们简单来测试一下就可以了

简单来测试一下

把我们这个服务呢

重新来启动一下

好

咱们这个服务呢

已经启动成功了

然后接下来呢

我们刷新一下

咱们这个接口文档

然后呢

我们看这里边呢

应该有一个什么呢

分页查询复建对吧

多出来这么一个接口

然后呢

我们可以直接来查询一下

比如说我们这个current

我们查询第一页对吧

然后这个type呢

咱们就不填了

因为我们现在的数据很少

对吧

数据很少

一共就这么几条吧

六条数据对吧

六条数据

所以说呢

我们这些过滤条件呢

这些呢

就都不写了

然后呢

我们查询这个十个

查询十个

然后呢

我们再来查询这个

这个这个

这些呢

参数都不提交过去

只提交最简单的一个current

还有一个size

然后呢

我们直接点发送

看一下数据

它其实已经反复回来了

对吧

然后呢

我们可以看到

这个地方这不是recourse吗

这些是我们当前这一页

要展示的对吧

因为一共就六个

所以只是分成了一页

然后呢

我们来看它统计的total

是不是六个对吧

size是十

当前的是第一页

others这些都没有

pages

然后呢

一共也是分成了一页

好

比如说我现在呢

改一下

我们这个size呢

来个2对吧

也就是说

这些呢

它都又给我反复来了

然后呢

把这些还都去掉

因为我们数据很少

所以这些就不要了

然后呢

我们查第一页

然后呢

每页是不是展示两条数据

直接点发送

它又重新查了

你看

稍等一下

发送

size是2对吧

然后呢

当前呢

是一共是分成了一页

对吧

一共是分成了什么呢

一共是分成了这个3页对吧

一共分成了3页

然后呢

总的这个数据量呢

是6条对吧

好

然后呢

你可以看到一共

这是应该是三条数据啊

整个到这儿

这是一条数据对吧

然后呢

这是一条数据

这是两条数据

然后呢

因为我们的size等于2嘛

一共是6条

然后呢

分成了3页

好

这个简单验证一下就可以了

因为这是一个附件啊

针对我们附件这个表里边的数据

进行复建啊

进行一个分页查询

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个“文件服务”模块的开发教学，重点讲解如何实现“分页查询附件”功能。讲师通过 IntelliJ IDEA 开发环境，演示了从控制器（Controller）到服务层（Service）的完整代码实现。核心内容包括：
- **接口定义**：在 `AttachmentController` 中定义了 `/page` 接口，用于分页查询附件。
- **请求参数封装**：使用 `FilePageReqDTO` 类封装分页查询所需的参数，如当前页、每页条数、文件夹ID、文件类型、创建时间范围等。
- **服务层实现**：在 `AttachmentServiceImpl` 中，通过 `LqWrapper` 构建动态查询条件，使用 MyBatis-Plus 的 `page` 方法执行分页查询，并将数据库结果映射为 DTO 返回。
- **演示与验证**：通过 Swagger UI 发起 HTTP 请求，验证接口功能，并在数据库管理工具中查看查询结果，确认数据正确性。

整个过程体现了典型的 Spring Boot + MyBatis-Plus 开发模式，强调了分页查询、条件构造和前后端数据交互。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取实际的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:30**: 课程引入与目标说明。讲师在文档中指出本节将重点讲解“导入分页查询附件”的代码，强调数据库操作不是本节重点。
- **00:30 - 01:00**: 展示 `AttachmentController` 的代码。重点讲解 `@ApiImplicitParams` 注解定义的两个查询参数：`current`（当前页）和 `size`（每页条数）。
- **01:00 - 01:30**: 展示 `FilePageReqDTO` 类的定义。详细说明其包含的字段，如 `folderId`、`submittedFileName`、`dataType`、`startCreateTime` 和 `endCreateTime`，并解释其作用。
- **01:30 - 02:00**: 展示 `BaseController` 中定义的常量。说明 `CURRENT`、`SIZE`、`PAGE_ASCS` 和 `PAGE_DESCS` 等常量用于统一管理分页和排序相关的参数。
- **02:00 - 02:30**: 展示 `AttachmentServiceImpl` 中的 `page` 方法实现。重点讲解如何使用 `LqWrapper` 构建查询条件，包括文件名、类型、业务ID、数据类型和排序。
- **02:30 - 03:00**: 演示接口调用。在 Swagger UI 中配置请求参数并发送 GET 请求，验证分页查询功能。
- **03:00 - 03:30**: 数据库验证。在数据库管理工具中执行查询语句，确认返回的数据与接口返回结果一致。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`5.8 导入其他接口代码`
- **子章节标题**：`5.8.1 接口导入-分页查询附件`
- **接口文档**：展示了 `AttachmentController` 的接口文档，包括 `@ApiOperation` 和 `@ApiImplicitParam` 注解。
- **数据表结构**：展示了 `pd_files` 表的字段结构，包括 `id`、`submittedFileName`、`folderId`、`dataType`、`createTime` 等。

#### 代码关键内容

- **控制器层 (`AttachmentController.java`)**
  ```java
  @ApiOperation(value = "分页查询附件", notes = "分页查询附件")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "current", value = "当前页", dataType = "long", paramType = "query", defaultValue = "1"),
      @ApiImplicitParam(name = "size", value = "每页显示几条", dataType = "long", paramType = "query", defaultValue = "10")
  })
  @GetMapping(value = "/page")
  public R<Page<Attachment>> page(FilePageReqDTO data) {
      Page<Attachment> page = getPage();
      attachmentService.page(page, data);
      return success(page);
  }
  ```

- **请求参数 DTO (`FilePageReqDTO.java`)**
  ```java
  @Data
  @ApiModel(value = "文件分页列表请求参数", description = "文件夹id")
  public class FilePageReqDTO implements Serializable {
      @ApiModelProperty(value = "文件夹id")
      private Long folderId;
      @ApiModelProperty(value = "原始文件名")
      private String submittedFileName;
      @ApiModelProperty(value = "数据类型 null和' '表示查询全部 图片：IMAGE 视频：VIDEO 音频：AUDIO 文档DOC 其他：OTHER")
      private DataType dataType;
      @ApiModelProperty(value = "开始时间")
      private LocalDateTime startCreateTime;
      @ApiModelProperty(value = "结束时间")
      private LocalDateTime endCreateTime;
  }
  ```

- **服务层 (`AttachmentServiceImpl.java`)**
  ```java
  public IPage<Attachment> page(Page<Attachment> page, FilePageReqDTO data) {
      Attachment attachment = dozerUtils.map(data, Attachment.class);
      LqWrapper<Attachment> wrapper = Wraps.Attachment.lq();
      wrapper.like(Attachment::getSubmittedFileName, attachment.getSubmittedFileName())
             .like(Attachment::getBizType, attachment.getBizType())
             .like(Attachment::getBizId, attachment.getBizId())
             .eq(Attachment::getDataType, attachment.getDataType())
             .orderByDesc(Attachment::getId);
      return baseMapper.page(page, wrapper);
  }
  ```

#### 图表/演示

- **Swagger UI 界面**：展示了如何配置分页查询的请求参数，包括 `current`、`size`、`folderId`、`dataType`、`startCreateTime` 和 `endCreateTime`。
- **数据库查询结果**：在数据库管理工具中，执行 `SELECT * FROM pd_attachment` 查询，返回了 6 条记录，验证了分页查询功能。

---

### 4) 关键场景与演示描述

- **场景一：接口定义与参数说明**
  - 讲师在 `AttachmentController` 中定义了 `/page` 接口，并使用 `@ApiImplicitParams` 注解说明了 `current` 和 `size` 两个参数。
  - 通过高亮显示代码，强调了参数的名称、值、数据类型和默认值。

- **场景二：请求参数 DTO 设计**
  - 讲师展示了 `FilePageReqDTO` 类的定义，详细说明了每个字段的作用。
  - 特别强调了 `dataType` 字段的取值范围，包括 `IMAGE`、`VIDEO`、`AUDIO`、`DOC` 和 `OTHER`。

- **场景三：服务层分页查询实现**
  - 讲师在 `AttachmentServiceImpl` 中，使用 `LqWrapper` 构建查询条件。
  - 通过 `like`、`eq` 和 `orderByDesc` 方法，动态构建了查询条件。
  - 最终调用 `baseMapper.page(page, wrapper)` 方法执行分页查询。

- **场景四：接口调用与结果验证**
  - 讲师在 Swagger UI 中配置了分页查询的请求参数。
  - 发送请求后，接口返回了分页查询结果。
  - 在数据库管理工具中，执行查询语句，确认返回的数据与接口返回结果一致。

- **场景五：代码逻辑与注释**
  - 讲师在 `AttachmentServiceImpl` 中，展示了 `download` 方法的实现，说明了如何根据 ID 下载附件。
  - 在 `save` 方法中，展示了如何根据业务类型和文件信息保存附件到数据库。

---

以上是根据视频画面进行的结构化技术分析，旨在帮助理解视频内容并掌握相关技术要点。
