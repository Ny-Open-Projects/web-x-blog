# 45-文件服务课程-文件服务开发（接口开发_根据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢

咱们是对我们这个业务接口的这个文档

对吧 接口文档进行了一个说明

那接下来呢

我们就来进行代码的实现

这个代码实现呢

相对来说啊

也是比较简单的

跟我们刚才开发的这个是一样的

是类似的

所以说呢

我们这块呢

对于类似的功能呢

就不再去手写了

咱们直接啊

把我们的代码从讲义上抄过来

然后呢

大概来读一下这个代码就可以了

那么我们现在呢

要根据业务类型

或者业务ID来删除

对吧

所以在我们的controller里边

我们肯定要创建这么一个方法

对吧

叫做removeByBizID

andBizType

好

这个方法名呢

是比较明确的

并且呢

返回值是R

里边呢

是一个不二类型的

这个没什么好说的

然后呢

我们这个请求参数呢

需要封装成这么一个DTO对象啊

叫做AttachmentRemoveDTO

好

咱们呢

其实从这个地方也能看到

你看我们这个数据类型

对吧

AttachmentRemoveDTO

对吧

然后咱们可以来看一下

我们可以打开这个DTO来搜一下

叫做AttachmentRemoveDTO

然后在这里边呢

其实就封装了这么两个属性

对吧

分别是我们的业务类型

还有业务ID

好

所以我们现在呢

回到我们的controller里边来

咱们现在呢

把这个讲义上这个代码呢

直接复制过来就可以了

好

然后呢

同样我们肯定也是要在

service里面呢

去这个扩展这么一个方法

根据业务类型

业务ID呢

来进行这个复建的删除

咱们整个把这个controller方法复制过来

然后呢

把它放在这个位置

好

这个地方报错呢

是因为我们这个service里边

目前还没有这个方法

我们先加一个注释啊

这个是根据业务类型

或者是我们的业务ID

对吧

来删除复建

好

那么它这个地方报错呢

我们就可以怎么做呢

给它来这个扩展一下

加一个public吧

其实不加public也没有关系啊

因为在接口里边默认是吧

如果不加这个修饰符

默认其实就是public的

这个是根据业务类型

或者是这个业务ID

对吧

删除复建

上面这个呢

是根据什么呢

根据IDs

对吧

删除复建

好

那么我们这个方法呢

就已经扩展好了

其他的这些呢

我们暂时先给它关闭掉

然后接下来呢

我们是不是就需要来实现啊

在咱们实现类里面来实现这个方法

所以我们需要来打开实现类

实现我们这个remove by bizid and biztype

这个方法

加个注释

或者是

或者是这个业务ID来删除复建

好

这个代码的话呢

咱们也是直接从我们讲义上抄过来就可以了

很显然这个地方

我们是不是需要根据业务类型

业务类型业务ID

是不是来这个查询我们数据库里面的数据啊

对吧

你看这是扩展

然后呢

在这个地方

我们需要根据业务类型业务ID呢

把咱们这个数据库里面的这个例子集合

给它查上来

好

查上来之后呢

先来判断一下

如果它是空

对吧

是空的话就没有必要再往下走了

好

所以直接return了

如果不是空呢

不是空的话呢

就会把咱们这个例子的集合呢

重新加工一下

封装成什么呢

封装成一个

例子的里边装的是IDs

IDs就是浪形的ID数组

为什么呢

因为我们前面是不是已经提供了一个

根据ID删除的方法

其实就是

上面的这个方法

对吧

remove这个方法

所以说呢

我们在这个方法里边呢

把咱们这个数据查上来

把它封装成

这么一个类型的对象

然后呢

再调用remove方法

那么又走到我们当时根据ID删除的

这个方法里面来了就

所以它是这么一个思路

那么我们整个把这块拷过来

大家来看一下

直接全都复制过来就可以了

这些代码呢

我们就不再手敲了

咱们大概来读一下

你看

那么这个呢

我们是不是还是修补点list

调用我们这个

MyBitPlus这个service

给我们提供的这个list方法

对吧

然后在这呢

我们构造一个条件对象

根据什么条件呢

一个是我们的BizID

还有一个是BizType

来进行一个查询

对吧

最终呢

返回一个list的集合

然后我们判断

list集合如果等于空

后边就不用执行了

直接return了

如果不等于空呢

不等于空

我们就把这个list集合

通过stream流

对吧

然后呢

把它转成一个浪形的

转成一个浪形的

然后这个浪形的取哪个字段呢

取的是ID

这个属性

因为它是个浪形的

所以要调用boxed

对吧

然后呢

再给它转成一个数组

转成一个数组

好

转成数组之后呢

再调用remove方法

而这个remove方法

就是我们刚才已经实现的

这个remove方法

在这呢

来实现我们真正的

这个删除操作

好

大概呢

就是这么一个思路啊

咱们把这个代码呢

读一下就可以了

好

到这儿的话呢

我们这个

根据业务类型

业务ID啊

删除附件

代码开发呢

都已经实现了

一会儿呢

我们来测试一下就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个文件服务（Attachment Service）的开发教程，主要讲解如何实现一个根据“业务类型”和“业务ID”删除附件的接口。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从控制器（Controller）层到服务（Service）层的代码实现过程。核心内容包括：
- 在 `AttachmentController` 中定义一个接收 `AttachmentRemoveDTO` 对象的删除接口。
- 在 `AttachmentService` 接口中声明对应的抽象方法。
- 在 `AttachmentServiceImpl` 中实现该方法，包括查询数据库、转换数据格式、调用 OSS（对象存储服务）删除文件等步骤。
- 整个过程遵循了分层架构的设计思想，体现了接口与实现分离的原则。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节划分是根据画面内容和逻辑顺序进行的：

- **00:00 - 00:05**: 视频开场，展示课程目录，定位到“5.5 接口开发-根据业务类型/业务id删除附件”章节。
- **00:05 - 00:15**: 展示接口文档（PPT），说明接口的请求示例、参数（bizId, bizType）和响应状态码。
- **00:15 - 00:30**: 在 `AttachmentController` 中编写接口代码，定义 `@ApiOperation` 和 `@DeleteMapping` 注解，并接收 `AttachmentRemoveDTO`。
- **00:30 - 00:45**: 在 `AttachmentService` 接口中声明 `removeByBizIdAndBizType` 方法。
- **00:45 - 01:00**: 在 `AttachmentServiceImpl` 中实现 `removeByBizIdAndBizType` 方法，包括数据库查询和 OSS 删除逻辑。
- **01:00 - 01:15**: 展示 `AttachmentService` 接口文档，预览后续测试章节。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **接口文档**：
  - **请求示例**：
    ```json
    {
      "bizId": "123",
      "bizType": "user"
    }
    ```
  - **请求参数**：
    | 参数名 | 参数说明 | 必填 | 数据类型 | schema |
    | :--- | :--- | :--- | :--- | :--- |
    | bizId | 业务id | false | string | |
    | bizType | 业务类型 | false | string | |
  - **响应状态码**：
    | 状态码 | 说明 |
    | :--- | :--- |
    | 200 | 成功 |
    | 40001 | 会话超时，重新登录 |
    | 40003 | 缺少Token参数 |
    | -1 | 系统繁忙 |

#### 代码关键内容

- **控制器层 (`AttachmentController.java`)**
  ```java
  @ApiOperation(value = "根据业务类型或业务id删除文件",
      notes = "根据业务类型或业务id删除文件")
  @DeleteMapping(value = "/biz")
  public R<Boolean> removeByBizIdAndBizType(
      @RequestBody AttachmentRemoveDTO dto) {
      attachmentService.removeByBizIdAndBizType(dto.getBizId(),
          dto.getBizType());
      return success(true);
  }
  ```

- **服务接口层 (`AttachmentService.java`)**
  ```java
  /**
   * 根据业务id/业务类型删除附件
   * @param bizId
   * @param bizType
   */
  void removeByBizIdAndBizType(String bizId, String bizType);
  ```

- **服务实现层 (`AttachmentServiceImpl.java`)**
  ```java
  @Override
  public void removeByBizIdAndBizType(String bizId, String bizType) {
      // 根据业务类和业务id查询数据库
      List<Attachment> list = super.list(
          Wraps.<Attachment>lbQ()
              .eq(Attachment::getBizId, bizId)
              .eq(Attachment::getBizType, bizType));
      if (list.isEmpty()) {
          return;
      }

      // 根据id删除文件
      remove(list.stream().mapToLong(
          Attachment::getId).boxed().toArray(Long[]::new));
  }
  ```

  **其中 `remove` 方法的实现（用于删除数据库记录和 OSS 文件）**：
  ```java
  @Override
  public void remove(Long[] ids) {
      if (ArrayUtils.isEmpty(ids)) {
          return;
      }

      // 查询数据库，用于删除文件信息封装
      List<Attachment> list = super.list(Wraps.<Attachment>lambdaQuery()
          .in(Attachment::getId, ids));

      // 从数据库中删除文件信息记录
      super.removeByIds(Arrays.asList(ids));

      // 对象格式转换处理
      List<FileDeleteDO> fileDeleteDOList = list.stream().map(fi ->
          FileDeleteDO.builder()
              .relativePath(fi.getRelativePath())
              .fileName(fi.getFilename())
              .group(fi.getGroup())
              .path(fi.getPath())
              .build()
      ).collect(Collectors.toList());

      // 调用 OSS 删除文件
      ossClient.deleteObject(bucketName, fileDeleteDOList);
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：接口定义与文档展示**
  - 讲师首先在 PPT 上展示了接口的详细文档，包括请求参数、响应状态码等，为后续代码开发提供规范。
  - 展示了 `AttachmentRemoveDTO` 的结构，用于接收前端传来的业务ID和业务类型。

- **场景二：控制器层代码编写**
  - 讲师在 `AttachmentController` 中编写了 `removeByBizIdAndBizType` 方法。
  - 使用 `@ApiOperation` 和 `@DeleteMapping` 注解定义接口。
  - 通过 `@RequestBody` 注解接收 `AttachmentRemoveDTO` 对象，并调用服务层方法。

- **场景三：服务接口与实现**
  - 讲师在 `AttachmentService` 接口中声明了 `removeByBizIdAndBizType` 方法。
  - 在 `AttachmentServiceImpl` 中，讲师通过 `super.list` 查询数据库，根据 `bizId` 和 `bizType` 条件获取附件列表。
  - 使用 `list.stream().mapToLong(...).boxed().toArray(...)` 将附件ID列表转换为 `Long[]` 数组，以便调用 `remove` 方法。
  - 最终调用 `ossClient.deleteObject` 方法删除 OSS 中的文件。

- **场景四：代码调试与优化**
  - 讲师在代码中添加了 `if (list.isEmpty()) return;` 的判断，以避免空指针异常。
  - 使用 `Wraps.<Attachment>lbQ()` 进行条件查询，体现了 MyBatis-Plus 的便捷性。
  - 通过 `Arrays.asList(ids)` 将 `Long[]` 转换为 `List<Long>`，以便调用 `removeByIds` 方法。

---

以上是根据视频画面进行的结构化技术分析报告。
