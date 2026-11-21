# 27-货物类型管理（服务接口开发_删除货物类 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来看我们货物类型管理这块的服务接口开发

那么我们还有最后一个

就是这个删除货物类型

需要注意的是什么呢

我们这个地方的删除货物类型

这个删除操作其实是一个逻辑删除

也就是说它其实本质上是一个什么呢

是一个更新操作

那也就意味着什么呢

我们这个地方呢

要想把某个货物类型删掉

其实就是把它那个状态位啊

给它改成什么呢

给它改成0就可以了

改成0就可以了

所以说呢

它其实最终掉的service呢

还是掉的我们这个update by id这个方法

所以说呢

我们这块呢

就不再手敲了

咱们只要在这个controller当中啊

提供这么一个方法

然后呢

就可以完成这个逻辑删除

我们直接把这个代码呢

复制过来啊

咱们大概读一下这个代码就可以了

因为这个呢

是最简单的一个方法

删除货物类型对吧

注意是逻辑删除

好

那么我们在这来写一下逻辑删除

好

其实就是

将我们这个状态位

对吧

这个status啊

把它的这个值呢

改成0就可以了

当然我们在这呢

没有直接去写0对吧

我们是使用了一个常量啊

好

你看

在我们这个constants

这个类里面定义了这么一个常量

0

所有的状态禁用的对吧

我们统一都写成0

所以说呢

我们使用这个

有什么好处呢

就是到时候我们如果这个状态位对吧

比如说我使用1表示什么禁用对吧

那这个时候呢

我直接在这改就可以了

好

所以我们可以来看一下

这个删除的话呢

它其实是什么呢

是这样来传过来的

把这个ID是不是给我们传过来

是吧

ID传过来

把这个ID接收到

然后呢

我们是不是把这个对象啊

重新这个

new一下

然后set ID

这就相当于它的这个删除条件

对吧

然后呢

把这个状态位更新成什么呢

我们是不是来设置一下

然后直接调用update的方法

这样就可以更新了

好

更新完之后呢

最后我们返回一个result对象

好

这个result对象呢

这个result对象呢

这个result对象呢

这个result对象呢

这个result对象呢

这个result对象里边呢

其实就是封装的什么呢

这个装填码

对吧

封装的装填码

好

以及这个信息

好

整个代码呢

写进来还是非常简单的

那接下来呢

我们把这个服务啊

启动一下

咱们来简单测试一下

就可以了

好

那么我们启动一下这个程序

好

咱们这个服务呢

已经启动完了

那接下来呢

我们回到这边

刷新一下

这个页面

然后呢

找到我们这个删除的方法

对吧

但是你注意看

它这是put的页面

这是put的请求

对吧

因为我们刚才已经说过了

它其实本质上是一个什么呢

是一个更新操作

虽然叫做删除

对吧

实际上是一个更新操作

好

然后呢

我们直接啊

在这儿来

try it out

把这个ID是不是给传过去啊

把这个ID给传过去

咱们可以随便来一个

比如说就还拿我们这个来说

我们直接复制

好

然后呢

把它拷过来

直接贴到这儿

对吧

然后执行

好

看反位值

反位值就这么两个

对吧

message是success

然后code是0

这表示成功

好

然后呢

我们从这边刷新一下

你会看到这条数据是不是还在

还在

但是呢

它的这个slitters

是不是已经改成0了

已经改成0了

这就表示啊

把它删除了

这就是一个逻辑删除

好

但是我们这块呢

大家也看到了

因为它是一个逻辑删除

并没有真的把这条数据删掉

所以我们那个关联关系呢

其实还在

对吧

并没有去操作这个关联关系这张表

好

那么到这儿的话呢

我们这个

这个删除货物类型呢

就已经测试通过了

没什么问题

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段主要演示了一个基于 Spring Boot 的“品达物流”后台管理系统中“货物类型”功能的逻辑实现。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了如何在 `GoodsTypeController` 中实现“逻辑删除”功能。核心内容包括：
- **功能实现**：通过 `@PutMapping("/id/disable")` 映射，接收前端传入的 `id`，在数据库中不真正删除记录，而是通过设置状态字段（如 `DATA_DISABLE_STATUS`）来标记该记录为“已禁用”。
- **代码结构**：展示了控制器层（Controller）、常量定义（Constant）、统一返回结果类（Result）以及数据库表结构。
- **演示验证**：通过 Swagger UI 调用接口，并在 Navicat 数据库客户端中验证数据表中记录的状态变化，确认逻辑删除功能生效。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示 IntelliJ IDEA 中 `GoodsTypeController.java` 文件，聚焦于 `updateById` 方法，用于更新货物类型信息。
*   **00:00:06 - 00:00:15**：讲师讲解 `updateById` 方法的逻辑，包括复制请求体数据、更新主表信息、处理关联表（如 `truckTypeGoodsType`）的删除和重建。
*   **00:00:16 - 00:00:25**：讲师将光标移动到 `disable` 方法，准备讲解“逻辑删除”功能。
*   **00:00:26 - 00:00:35**：讲师切换到 `Constant.java` 文件，展示定义的状态常量，如 `DATA_DEFAULT_STATUS` (1) 和 `DATA_DISABLE_STATUS` (0)。
*   **00:00:36 - 00:00:45**：讲师切换到 `Result.java` 文件，展示统一的返回结果类，用于规范 API 的响应格式。
*   **00:00:46 - 00:00:55**：讲师回到 `GoodsTypeController.java`，聚焦于 `disable` 方法，讲解其核心逻辑：创建实体、设置 ID、设置状态为禁用、调用服务层更新。
*   **00:00:56 - 00:01:05**：讲师在代码中高亮 `pdGoodsType.setStatus(Constant.DATA_DISABLE_STATUS);`，强调状态更新是逻辑删除的关键。
*   **00:01:06 - 00:01:15**：讲师在代码中高亮 `goodsTypeService.updateById(pdGoodsType);`，说明数据更新操作。
*   **00:01:16 - 00:01:25**：讲师在代码中高亮 `return Result.ok();`，说明返回统一的成功响应。
*   **00:01:26 - 00:01:35**：讲师切换到浏览器，打开 Swagger UI，展示 `PUT /base/goodsType/{id}/disable` 接口。
*   **00:01:36 - 00:01:45**：讲师在 Swagger UI 中输入一个 `id`（如 `889255497728`），并点击“Execute”按钮调用接口。
*   **00:01:46 - 00:01:55**：讲师切换到 Navicat 数据库客户端，执行 SQL 查询 `SELECT * FROM pd_base.pd_goods_type LIMIT 1000;`，并高亮显示查询结果，展示 `status` 字段已更新为 `0`，确认逻辑删除成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.4.7 删除货物类型`。
    *   **关键注释**：`注意：此处删除货物类型为逻辑删除`。
    *   **代码示例**：在 PPT 中展示了 `disable` 方法的代码片段，与视频中展示的代码一致。

*   **代码关键内容**：
    *   **控制器方法 `disable`**：
        ```java
        @PutMapping("/id/disable")
        @ApiOperation(value = "删除货物类型")
        public Result disable(@PathVariable(name = "id") String id) {
            PdGoodsType pdGoodsType = new PdGoodsType();
            pdGoodsType.setId(id);
            pdGoodsType.setStatus(Constant.DATA_DISABLE_STATUS);
            goodsTypeService.updateById(pdGoodsType);
            return Result.ok();
        }
        ```
    *   **常量类 `Constant.java`**：
        ```java
        public static final Integer DATA_DEFAULT_STATUS = 1;
        public static final Integer DATA_DISABLE_STATUS = 0;
        ```
    *   **统一返回类 `Result.java`**：
        ```java
        public class Result extends HashMap<String, Object> implements Serializable {
            private static final long serialVersionUID = 1L;
            public static Result ok() {
                Result result = new Result();
                result.put("code", 0);
                result.put("msg", "success");
                return result;
            }
        }
        ```

*   **图表/界面**：
    *   **Swagger UI**：展示了 `Goods Type Controller` 的所有接口，包括 `PUT /base/goodsType/{id}/disable`。
    *   **Navicat 数据库界面**：展示了 `pd_goods_type` 表的结构和数据，用于验证逻辑删除后的状态。

---

### 4) 关键场景与演示描述

*   **场景一：逻辑删除功能实现** (00:00:46 - 00:01:15)
    *   **描述**：讲师在 `GoodsTypeController` 中编写了 `disable` 方法。该方法接收一个 `id` 参数，创建一个 `PdGoodsType` 实体，设置其 `id` 和 `status` 为禁用状态（`0`），然后调用 `goodsTypeService.updateById` 方法将状态更新到数据库。最后，返回一个标准的成功响应 `Result.ok()`。

*   **场景二：接口调用与验证** (00:01:26 - 00:01:55)
    *   **描述**：讲师在 Swagger UI 中调用 `PUT /base/goodsType/{id}/disable` 接口，传入一个具体的 `id`。接口成功执行后，讲师切换到 Navicat 数据库客户端，查询 `pd_goods_type` 表。在查询结果中，讲师高亮显示了目标记录的 `status` 字段，确认其值已从 `1`（正常）更新为 `0`（禁用），从而验证了逻辑删除功能的正确性。
