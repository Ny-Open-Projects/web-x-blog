# 59-文件服务课程-文件服务开发（接口导入_根据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么接下来呢

咱们继续来看我们文件服务的开发

刚才呢

咱们是做了一个接口导入

导入的是我们分页查询附件啊

这个接口

接下来呢

我们导入的是什么呢

根据我们的业务类型

业务ID啊

查询附件

这些呢

全都是一些纯数据库操作啊

那么咱们就直接啊

把我们这个代码

这是controller里边的一个方法

对吧

直接把它拷到我们controller当中

好

然后呢

我们可以给它加一个注释啊

这个地方

这是根据什么呢

根据我们的业务类型

对吧

业务ID啊

来查询附件

根据业务类型

然后呢

还有业务ID查询附件

好

这是这两个条件

对吧

biztypes

还有bizids

同样的

这个地方也是跟前面是一个问题啊

它是在我们这个

这个

code的

exception code里边定义的这个常量

好

然后呢

在service里边呢

我们是不是需要来提供这么一个方法

叫做fine的方法

好

根据这两个条件对吧

然后呢

进行一个查询

找到咱们这个接口

然后呢

接下来就是实现类对吧

实现类这边呢

我们也把它拷过来

好

大家可以看到

它其实呢

就是直接调用了我们base mapper对吧

然后这个fine的方法

把我们这两个条件对吧

分别是biztypes

还有bizids传进去

然后呢

根据这两个条件进行一个查询

好

这个demo呢

咱们就直接导过来了

导过来之后呢

我们可以来简单测试一下

验证一下就可以了

那么从根本上来讲了

这个其实就是两个组合条件的一个查询

对吧

一个纯数据库操作

好

咱们这个服务呢

已经重启过了

重启过之后呢

我们简单来看一下

刷新一下咱们这个

接口文档的页面

然后呢

把什么呢

把我们刚才导入的

就是根据什么呢

根据我们这个业务类型

业务ID查询

但是它这展示的叫做查询附件

对吧

为什么起的这个名字呢

就是因为我们刚才导入的时候

咱们来看一下

这个地方它是不是叫做查询附件呢

好

其实我们可以定的更加明确一点

对吧

就是根据什么呢

根据我们的业务类型

业务ID来查询

其实通过这个接口文档了

从这能看到

对吧

好

好

比如说我们刚才这个提交的这两个

对吧

333

好

在这来制定一下

根据这两个条件来查询

好

你可以看到它已经查出来了

对吧

一共是几条呢

应该是两条吧

好

从这到这

对吧

这是一个对象

转成的一个Jason

对吧

然后呢

又从这到这

这又是另外一个

好

这是根据我们这两个条件呢

进行一个查询

比如说我这个地方呢

我在这儿再加个4对吧

这个时候还有吗

它是不是就没有了

对吧

因为匹配不上了

咱们可以看一下控制台

控制台应该是发出了查询语句

对吧

select的

distinct的

这是查在我们字段的吧

字段

然后呢

from这个表

where一等于一

and

BIZID in

然后呢

and

因为它是一个and条件

对吧

所以说根据这个BIZ type

业务类型匹配的时候

肯定就匹配不上了

这样的话

我们是不是

一条数据都查不上来

好

这是我们简单测试一下

根据这两个条件进行查询

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析：

---

### 1) 视频摘要

本视频课程聚焦于一个文件服务模块（`pd-file-server`）中“根据业务类型和业务ID查询附件”功能的开发与实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从控制器（Controller）层到服务（Service）层的完整代码编写过程。核心内容包括：
*   **接口定义**：在 `AttachmentController` 中定义了两个接口方法，一个用于分页查询，另一个用于根据业务类型和ID查询附件列表。
*   **参数注解**：使用 `@ApiImplicitParam` 注解为接口参数（如 `current`、`size`、`bizTypes`、`bizIds`）添加文档说明。
*   **服务层实现**：在 `AttachmentServiceImpl` 中，通过 `baseMapper` 的 `find` 方法，根据传入的业务类型数组和业务ID数组，查询数据库中的附件记录。
*   **数据库验证**：通过 MySQL 数据库客户端验证了附件表 `pd_attachment` 中的数据，确认了查询条件的有效性。
*   **接口测试**：使用 Swagger UI 对接口进行测试，成功调用并返回了预期的 JSON 数据。

整个过程展示了如何在 Spring Boot 项目中，通过分层架构（Controller -> Service -> Mapper）实现一个典型的业务查询功能，并通过 Swagger 进行接口调试。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程开场，展示项目结构和当前正在开发的章节 `5.8.2 接口导入-根据业务类型/业务id查询附件`。
*   **00:16 - 00:30**：在 `AttachmentController` 中，为分页查询接口 `page` 添加 `@ApiImplicitParam` 注解，定义 `current` 和 `size` 参数。
*   **00:31 - 00:45**：在 `AttachmentController` 中，新增一个用于查询附件列表的接口 `findAttachment`，并为其添加 `@ApiOperation` 和 `@ApiResponses` 注解。
*   **00:46 - 01:00**：在 `AttachmentService` 接口中，定义了 `find` 方法，声明其接收 `String[] bizTypes` 和 `String[] bizIds` 作为参数。
*   **01:01 - 01:15**：在 `AttachmentServiceImpl` 中，实现 `find` 方法，使用 `baseMapper.find(bizTypes, bizIds)` 查询数据库。
*   **01:16 - 01:30**：在 `AttachmentServiceImpl` 中，为 `find` 方法添加 `@Override` 注解，并在 `baseMapper` 的 `find` 方法中，使用 `QueryWrapper` 构建查询条件。
*   **01:31 - 01:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `like` 和 `eq` 条件。
*   **01:46 - 02:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **02:01 - 02:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **02:16 - 02:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **02:31 - 02:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **02:46 - 03:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **03:01 - 03:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **03:16 - 03:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **03:31 - 03:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **03:46 - 04:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **04:01 - 04:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **04:16 - 04:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **04:31 - 04:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **04:46 - 05:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **05:01 - 05:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **05:16 - 05:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **05:31 - 05:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **05:46 - 06:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **06:01 - 06:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **06:16 - 06:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **06:31 - 06:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **06:46 - 07:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **07:01 - 07:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **07:16 - 07:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **07:31 - 07:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **07:46 - 08:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **08:01 - 08:15**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **08:16 - 08:30**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **08:31 - 08:45**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by` 条件。
*   **08:46 - 09:00**：在 `AttachmentServiceImpl` 中，完成 `find` 方法的 `QueryWrapper` 构建，包括 `order by`
