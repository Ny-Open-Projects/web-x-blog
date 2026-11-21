# 22-货物类型管理（服务接口开发_查询货物类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好刚才呢咱们这个control的这个方法呢已经写完了

接下来呢就是差我们这个service具体的实现了对吧

你看现在这个service这边是不是已经报错了

就是因为我们在这个接口里边声明了final这个方法

然后呢这里边还没有去实现它

那接下来呢我们来实现

先把这个注释呢来加一下

这个是查询货物货物类型列表

其实呢就是我们根据传过来的这个list的集合

这个集合里面其实封装的都是我们这个货物类型的ID对吧

根据多个ID来进行一个in关键字的查询

那么这个查的话呢其实也比较简单

咱们还是使用什么呢

mybetaplus给咱们提供的这个对象

就是这个lambda query viper吧

然后呢这个实体的话呢还是我们这个pdgoose type

然后呢我们把它来封装一下

把这个条件来封装一下

lambda query viper

那么条件呢是不是只有一个

就是根据

这个id来查询

但是这个id呢我们最好还是先来判断一下

这个id不等于空对吧

同时id.size大于零

这个时候呢我们再来动态添加条件啊

添加我们这个查询条件对吧

使用in关键字来进行查询

那么直接调用它的封装的

它这里边封装的一个方法是不是就叫做in呢

就叫做in

然后呢

使用哪个关键字进行in查询呢

是不是应该是根据id啊

所以我们这个地方呢就是pdgoose type

然后应该是getid对吧

然后呢具体的值呢

是不是就是我们传进了这个id

就这一个条件

那么这个封装好之后呢

是不是直接调用我们这个什么呢

base mapper啊

它这里边是不是有这个select list方法

然后呢把这个条件呢对象传进去就可以了

整个呢它这个已经封装好了

所以我们主要做的呢

就是把这个条件对象是不是给它封装好

然后呢把这些具体的条件一个一个添加进去

最后呢调用这个select list方法

这个select list方法呢

其实就不是我们自己定义的

而是在base mapper里边是不是已经有了

所以我们就把这个对象给它封装好

这个条件传进去就可以了

好那么到这儿的话呢

我们整个这个方法就已经写完了

一会儿呢我们整体来测试一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是一个关于 Spring Boot + MyBatis-Plus 框架的实战教学视频，主要演示如何在服务层（Service）中，通过 `LambdaQueryWrapper` 构建一个根据多个 ID 进行查询的条件，并最终调用 MyBatis-Plus 的 `selectList` 方法执行数据库查询。视频通过 IntelliJ IDEA 的代码编辑器进行演示，逐步展示了从控制器（Controller）接收参数，到服务层（Service）处理业务逻辑，再到使用 MyBatis-Plus 的 Lambda 查询方式构建 SQL 条件的完整过程。核心内容是 `LambdaQueryWrapper` 的 `in` 方法的使用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构和 `GoodTypeController` 中的 `@GetMapping` 注解方法，该方法接收一个 `ids` 参数列表，用于查询货物类型。
*   **00:05 - 00:10**: 切换到 `GoodTypeServiceImpl` 类，展示 `findALL` 方法的初始状态，该方法目前仅返回 `null`。
*   **00:10 - 00:15**: 在 `findALL` 方法中，开始编写业务逻辑，创建一个 `LambdaQueryWrapper` 实例。
*   **00:15 - 00:20**: 添加参数校验逻辑，判断 `ids` 是否为非空且长度大于0。
*   **00:20 - 00:25**: 在 `LambdaQueryWrapper` 中调用 `in` 方法，传入实体类的 `getId` 字段和 `ids` 列表，构建查询条件。
*   **00:25 - 00:30**: 调用 `baseMapper.selectList` 方法，传入构建好的 `LambdaQueryWrapper`，执行数据库查询并返回结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **控制器层 (`GoodTypeController.java`)**:
        ```java
        @GetMapping("...")
        @ApiOperation(value = "查询货物类型列表")
        public List<GoodsTypeDto> findAll(@RequestParam(name = "ids", required = false) List<String> ids) {
            return goodsTypeService.findAll(ids);
        }
        ```
    *   **服务层 (`GoodTypeServiceImpl.java`)**:
        ```java
        @Override
        public List<PdGoodsType> findAll(List<String> ids) {
            LambdaQueryWrapper<PdGoodsType> lambdaQueryWrapper = new LambdaQueryWrapper<>();
            if (ids != null && ids.size() > 0) {
                lambdaQueryWrapper.in(PdGoodsType::getId, ids);
                return baseMapper.selectList(lambdaQueryWrapper);
            }
            return null;
        }
        ```

*   **关键概念**:
    *   **`LambdaQueryWrapper`**: MyBatis-Plus 提供的用于构建动态 SQL 条件的工具类，支持 Lambda 表达式，可以避免硬编码字段名。
    *   **`in` 方法**: 用于构建 `IN` 查询条件，例如 `WHERE id IN (1, 2, 3)`。
    *   **`PdGoodsType::getId`**: Java 中的方法引用，用于指定查询条件的字段。
    *   **`baseMapper.selectList`**: MyBatis-Plus 的 Mapper 接口方法，用于根据条件查询列表。

---

### 4) 关键场景与演示描述

*   **场景一：从控制器接收参数**
    *   演示者首先在 `GoodTypeController` 中定义了一个 `@GetMapping` 方法，该方法接收一个名为 `ids` 的 `List<String>` 参数。这个参数用于前端传递多个货物类型的 ID。
*   **场景二：在服务层构建查询条件**
    *   演示者切换到 `GoodTypeServiceImpl` 类，定位到 `findAll` 方法。
    *   他创建了一个 `LambdaQueryWrapper<PdGoodsType>` 实例，用于构建查询条件。
    *   他添加了参数校验逻辑，确保 `ids` 不为空且包含有效元素。
*   **场景三：使用 LambdaQueryWrapper 构建 IN 条件**
    *   演示者调用 `lambdaQueryWrapper.in(PdGoodsType::getId, ids);` 方法。
    *   这行代码的作用是将 `ids` 列表中的所有值作为 `id` 字段的 `IN` 条件，生成 SQL 语句 `WHERE id IN ('id1', 'id2', 'id3')`。
*   **场景四：执行查询并返回结果**
    *   演示者调用 `baseMapper.selectList(lambdaQueryWrapper);` 方法。
    *   这行代码会根据构建好的条件执行数据库查询，并将结果集返回给调用方。
    *   最终，`findAll` 方法返回一个 `List<PdGoodsType>`，包含了所有匹配的货物类型数据。

整个演示过程清晰地展示了如何在 Spring Boot 项目中，利用 MyBatis-Plus 的 Lambda 查询功能，实现一个基于多个 ID 的高效、可维护的查询操作。
