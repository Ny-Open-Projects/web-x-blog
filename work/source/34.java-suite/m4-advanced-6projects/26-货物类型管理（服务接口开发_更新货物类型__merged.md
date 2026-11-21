# 26-货物类型管理（服务接口开发_更新货物类型_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们这个代码都已经写完了

并且呢现在服务呢我也已经跑起来了

那接下来呢我们就来测试一下这个更新方法

把这边重新刷一下

那先找到我们这些请求应该是这个put方式请求对吧

更新户类型信息

然后呢我们来看一下try it out对吧

来执行

大家来看啊

那么我们在这呢要传的

要传的是不是这么两部分

一个是什么呢

一个是咱们这个DTO对吧

一个是DTO

你看它是不是JSON形式的

JSON形式的

然后呢我们可以在这来改

然后呢还有一个就是我们这个ID对吧

这个ID呢也是必须的

从这能看出来required

从这也能看到这边application-json对吧

是JSON形式的这个DTO

最终这个JSON呢就会封装成我们这个DTO对象

这个ID注意我们不能随便写对吧

它肯定是一个存在的ID啊才有意义

那么我们可以来找一个

咱们从这里边呢来找一个ID

PD base

好

打开我们这个表啊

从这里边来找一个货物类型的ID

往下拽

咱们就使用

还使用咱们这个就可以了

来复制一下

然后呢

把这个ID是不是放到这儿来

然后呢根据这个ID来改

那么具体改成什么值呢

具体改成什么值呢

这个呢比如我改成个10对吧

这个呢也改成个10

然后呢

这块这个ID呢

其实它应该是跟我们这个ID是一致的

那么我们也可以把它去掉

不要这个

好

Daddy

然后呢

name

这个name的话呢

我们就来一个test吧

test

好

remark呢

remark

表示我在这来一个5

好

状态状态的话我们改成一啊

这是一

然后呢传个type ID

这个呢其实你可以传也可以不传对吧

咱们都来测一下

比如说这次呢

我先不传

我把它去掉

好把他去掉

然后呢

我们现在来改一下

大家来看这个效果

直接执行

好

这就直接更新完了

好

呃

从这呢

也看不出什么效果来

那么他又把这个DTO

是不是给我们反过来了

然后呢

我们直接来看

咱们这个数据库啊

看他的基本信息

刷新一下

注意看

这块他是不是已经改回来了

已经改回来了

好

然后呢

这两个值是不是

还有这个值

这些都已经改对了

这是基本信息

呃

现在呢

是没有涉及到关联关系

对吧

因为我们刚才没有传

然后呢

我们接下来呢

重新再来

这个改一下啊

把这个重新刷新一下

好

然后呢

重新再来

哎

不是这个啊

应该是铺的方式

这个

好

传一套的

这次呢

我们还改这个数据啊

还改这个ID

复制

然后呢

把ID是不是放在这个位置

然后呢

这个地方呢

呃

比如说我们改成20吧

好

改成20

但这个ID呢

还是不要他

这个没用

好

前端传的时候呢

他也不会给我们传这个

然后这个NAME呢

我还改回去啊

这个3C

好

然后呢

这个REMARK呢

咱们这个地方呢

改成个TEST的

好

然后呢

这个STATUS改成1

然后关联关系

对吧

这个ID啊

传个TYPE

IDs呢

我们可以来看一下

咱们先查一下

先查一下

到这呢

我们先来写个CIRCLE

就不用写CIRCLE了

直接

从这儿来看

但这里边数据呢

还是比较多的吧

那还是来

写一个CIRCLE

查一去

看一下

要不然这里面看起来呢

可能不太方便啊

然后呢

我们在这里边来

SELECT

SEARCH FROM

我们这个表名呢

叫做什么呢

叫做PD什么

CHANK TYPE

然后呢

是GOOSE TYPE

对吧

好

这是所有的啊

然后呢

我们再来一个WHERE条件

对吧

好

WHERE

那么我们传过来的

应该是这个什么呢

是这个GOOSE TYPE ID

对吧

货物类型ID

GOOSE TYPE ID

等于什么值呢

这不应该就是咱们刚才考的这个值

好

也就是说我们现在先看一下什么

它原有的这些关联关系对吧

原有的关联关系是这个样子的

好

关联的是这两个啊

这是不是代表的是车辆类型对吧

然后呢

现在我们给它改造一下

给它改一下

改成其他的对吧

随便挑两个啊

其实改成什么都可以

车辆类型

比如说我现在呢

把这个ID

考一下

这个代表的是一个车辆类型ID对吧

然后呢

给它放在这里吧

放到

这个地方

好

有多个呢

有多个呢

你加个逗号

然后再来呗

中间分隔就可以了

好

是这样的

比如我们可以再来考一个啊

好

我考一个这个

好

复制

然后呢

把它贴这儿

咱们就整这两个就可以了

然后呢

我们接下来执行一下

大家来看

执行

好

已经执行完了

对吧

从这儿呢

看着不太明显

然后呢

我们还是看这边

刚才查询的是这么一个结果

现在呢

我们再次查询

再次查询

哎

你注意看

这块是不是就已经发生了变化

说明什么呀

它把原先的这两个是不是给清理掉

然后重新添加的这两个关系

当然它的基本信息呢

应该也已经改过来了

咱们重新刷新一下

好

你看

这是改成3C对吧

这些都已经改成功了

好

那么这个测试是没有什么问题的

那么到这儿的话呢

我们这个更新货物类型就已经完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段演示了如何使用 Swagger UI 工具对一个名为“品达物流管理”的后端系统进行 API 测试，具体操作是通过 `PUT` 方法更新“货物类型”数据。演示过程包括：
- 通过 Swagger UI 查看并调用 `GET /base/goodsType/{id}` 接口，获取目标货物类型的详细信息。
- 在 Swagger UI 中配置 `PUT /base/goodsType/{id}` 接口，设置请求体（`dto`）和路径参数（`id`）。
- 执行更新请求，并观察返回的响应结果。
- 为验证数据更新，切换到 Navicat Premium 数据库客户端，查询数据库表 `pd_truck_type_goods_type`，确认 `goods_type_id` 字段的值已成功更新。
- 最后，展示了在项目源码（Typora 文档）中，`GoodsTypeController` 类中 `update` 方法的实现逻辑，该方法负责处理前端传入的更新请求，并调用服务层进行数据持久化。

整个过程旨在展示前后端协作、API 测试以及数据库变更的完整工作流。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节按画面出现的逻辑顺序排列：

- **章节 1: 查看并测试 GET 接口 (00:00:00 - 00:00:05)**
  - 展示 Swagger UI 界面，执行 `GET /base/goodsType/{id}` 接口。
  - 成功获取到一个 JSON 格式的响应体，包含 `id`、`name`、`defaultVolume`、`defaultWeight`、`remark`、`status` 和 `truckTypeId` 等字段。

- **章节 2: 配置 PUT 接口 (00:00:05 - 00:00:10)**
  - 切换到 `PUT /base/goodsType/{id}` 接口的编辑页面。
  - 设置路径参数 `id` 为 `1236865284496138246`。
  - 设置请求体 `dto` 的 JSON 格式，包含 `defaultVolume`、`defaultWeight`、`name`、`remark`、`status` 和 `truckTypeId` 等字段。

- **章节 3: 执行 PUT 请求并查看响应 (00:00:10 - 00:00:15)**
  - 点击“Execute”按钮，执行更新请求。
  - 展示响应结果，状态码为 `200`，响应体显示 `status: 1`，表示更新成功。

- **章节 4: 验证数据库变更 (00:00:15 - 00:00:20)**
  - 切换到 Navicat Premium 数据库客户端。
  - 执行 SQL 查询语句：`SELECT * FROM pd_truck_type_goods_type WHERE goods_type_id = 889255497728;`。
  - 查询结果显示，`goods_type_id` 字段的值已更新为 `889255497728`，验证了 API 更新操作的有效性。

- **章节 5: 查看后端代码实现 (00:00:20 - 00:00:25)**
  - 切换到 Typora 文档，展示 `GoodsTypeController` 类中的 `update` 方法。
  - 方法接收 `@PathVariable` 的 `id` 和 `@RequestBody` 的 `dto`。
  - 方法内部通过 `BeanUtils.copyProperties` 将 DTO 数据复制到实体对象 `PdGoodsType`。
  - 调用 `truckTypeGoodsTypeService.batchSave` 方法，将更新后的 `truckTypeId` 批量保存到关联表中。
  - 最终返回更新后的 `truckTypeGoodsType` 对象。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **Swagger UI 界面截图**：
  - **GET 接口响应体**：
    ```json
    {
      "id": "1236865284496138246",
      "name": "2222",
      "defaultWeight": 22,
      "defaultVolume": 22,
      "remark": "2222",
      "truckTypeId": "123680787604142236",
      "status": "118805260119159194"
    }
    ```
  - **PUT 接口请求体**：
    ```json
    {
      "defaultVolume": 0,
      "defaultWeight": 0,
      "id": "string",
      "name": "string",
      "remark": "string",
      "status": 0,
      "truckTypeId": ["string"]
    }
    ```
  - **PUT 接口响应体**：
    ```json
    {
      "id": "889255497728",
      "name": "TEST1",
      "defaultWeight": 10,
      "defaultVolume": 10,
      "remark": "无",
      "truckTypeId": null,
      "status": 1
    }
    ```

- **Navicat Premium 数据库查询语句**：
  ```sql
  SELECT * FROM pd_truck_type_goods_type WHERE goods_type_id = 889255497728;
  ```

- **后端 Java 代码（Typora 文档）**：
  ```java
  @PutMapping(value = "更新货物类型信息")
  public GoodsTypeDto update(@PathVariable(name = "id") String id, @RequestBody GoodsTypeDto dto) {
      dto.setId(id);
      PdGoodsType pdGoodsType = new PdGoodsType();
      BeanUtils.copyProperties(dto, pdGoodsType);
      truckTypeGoodsTypeService.batchSave(dto.getTruckTypeIds()).stream().map(truckTypeId -> {
          PdTruckTypeGoodsType pdTruckTypeGoodsType = new PdTruckTypeGoodsType();
          pdTruckTypeGoodsType.setTruckTypeId(truckTypeId);
          pdTruckTypeGoodsType.setGoodsTypeId(id);
          return pdTruckTypeGoodsType;
      }).collect(Collectors.toList());
  }
  ```

---

### 4) 关键场景与演示描述

- **场景 1: GET 接口数据获取**
  - 演示者在 Swagger UI 中输入一个特定的 `id`，并点击“Execute”按钮。
  - 系统返回一个包含货物类型详细信息的 JSON 对象，其中 `status` 字段为 `118805260119159194`，表明数据存在且有效。

- **场景 2: PUT 接口数据更新**
  - 演示者将 `id` 参数设置为 `1236865284496138246`，并配置了新的 `name` 为 `"TEST1"`，`defaultVolume` 和 `defaultWeight` 均为 `10`，`remark` 为 `"无"`。
  - 点击“Execute”按钮后，系统返回 `status: 1`，表示更新操作成功。

- **场景 3: 数据库验证**
  - 演示者切换到 Navicat Premium，执行 SQL 查询，验证 `pd_truck_type_goods_type` 表中 `goods_type_id` 字段的值。
  - 查询结果确认 `goods_type_id` 已更新为 `889255497728`，与 Swagger UI 中的 `id` 参数值一致，证明了前后端数据同步成功。

- **场景 4: 后端代码逻辑展示**
  - 演示者展示 `GoodsTypeController` 中的 `update` 方法。
  - 该方法接收前端传入的 `id` 和 `dto` 数据，通过 `BeanUtils.copyProperties` 将 DTO 数据复制到实体对象。
  - 通过 `truckTypeGoodsTypeService.batchSave` 方法，将更新后的 `truckTypeId` 批量保存到关联表中，实现了数据的持久化。

整个演示过程清晰地展示了从 API 调用、数据更新到数据库验证的完整闭环，体现了前后端协作开发的典型工作流程。
