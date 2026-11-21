# 15-地址簿管理（服务接口开发_新增地址簿_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们这个新增地址部这个接口啊

从我们的这个controller到service对吧

然后呢一直到我们这个实体类对吧

都已经导入过了

但是这个地方要注意啊

这个实体类呢是需要去实现一个什么呢

虚拙化接口的

我们在这来实现一下

implements

然后呢实现完这个虚拙化接口之后啊

咱们就来启动一下

启动一下我们这个服务

然后呢我们来测试一下

这是我们这个服务启动类的吧

好然后呢我们在这来执行一下

好咱们这个服务呢也已经启动完了

那么接下来呢

我们就来测试一下咱们这个接口

好我们服务的地址呢是8189

对吧这个地址

这个地址

然后呢我们来测试一下这个接口

localhost的

然后端口号是8189

就这个地址

好swagui

好那么能够看到我们这个接口

对吧

这是我们新增的这个接口

首先呢我们先来解释一下

大家可以看啊

我们当前的这个controller

其实并没有去加什么呢

并没有去加我们这个swag相关的注解

你看我们那个什么API注解

包括方法上加的那个API operation注解

它并没有加对吧

没有加的话呢

它其实只要能扫描到我们当前这个controller

就可以生成默认的

你看默认的其实就是什么呢

使用这个

使用这个

也就是它其实是对我们这个类名

进行驼封命名法的一个拆分对不对

然后呢

然后呢

中间呢是用空格隔开

用这个横线隔开

address book control

好

然后呢我们这个方法呢

其实这个地方这个说明save呢

对应的就是我们这个方法名对不对

好

也就是它是默认的

这是一套生成规则

好

好那接下来呢我们就来测试一下

咱们来测试一下

直接点try it out

对吧

然后呢我们来检查一下address

address

比如说我在这来一个什么呢

来一个北京

好

然后呢cityid

的话呢

比如就等于10吧

好

这个地方呢我们需要来解释一下

这个cityid啊

这个id是怎么来的

注意

咱们当前这个项目当中并没有我们的省市区

对吧

这些数据

它其实是来自于什么呢

是来自于我们那个通用权限系统所带的一套表结构

所以这个呢

也是一个逻辑意义上的一个外建

叫做逻辑外建

好

然后呢还有company name

比如说我们就叫传制播客

对吧

传制播客

好

然后呢这个countryid

比方说等于50

然后呢create time

这个time的话呢

我们其实可以给它删掉

删掉

让它自动生成

然后呢这个number呢

我们就随便写一个001

然后呢这个id不用给对吧

id它是会自动生成的

所以不用给它传

is default是否是默认的对吧

如果是1的话

表示当前我们录入的这个地址

不是信息是默认的

然后呢name

name

比方说是小名

好

然后for number

咱们随便写一个

随便写一个

这个手机号

对吧

然后呢这个profit wins id

这个也是啊

刚才已经解释过了

省市区

这个呢这都是逻辑外建

那么我们真正的省市区的

这些基础数据呢

是在通用权益系统

那边保存的

好

然后呢我们在这呢

随便给它传一个值就可以了

好

然后呢这个是user id对吧

这个user id呢

它其实是

相当于也是一个

逻辑外建

也是一个逻辑外建

来看一下

地址不

这个应该就不是逻辑外建了

这个是真正的外建关系

当然了我们这个系统里面

其实并没有真的

把这个外建约束

把它这个创建出来

那么它对应的是什么呢

它对应的是咱们这个

也就是在我们这个address book

这个表里面是不是有个user id

而这个user id呢

它其实指向的是什么呢

指向的是我们这个member表的id

这个字段

但是这个外建的字段呢

这个外建约束呢

没有去创建出来

它保存的就是这个值

所以说呢

是具体是哪个用户的呢

我们可以随便来选一个

随便来选一个

因为我们现在呢

没有去写这个开发

没有去写登录功能

对不对

所以说呢并没有登录

所以说呢

我们这个地方呢随便来一个

比如说就是这个用户的

这个代表的是个用户id

然后呢我们给它直接抄过来就可以了

真正的这个生产环境下呢

这个user id呢

它其实是能够获取到的对吧

就是我们当前登录用户的

它的id

因为我们现在呢

没有开发这个登录功能

所以在这呢

user id我们随便给它造一个就可以了

好

那接下来呢

我们就来这个执行一下

但是在执行之前呢

咱们先来看一下我们这个pdadressbook这个表

因为呢新增的话

它会向这个表里面插入一条数据

现在呢

大家能看到一共是什么呢

一共是58条数据对吧

当前是58条数据

然后呢

它在新增成功之后呢

是不是还需要把我们这个数据呢

把它缓存起来对吧

缓存起来

那么它同时呢

会在这个redis当中啊

给我们缓存一份

所以说呢

我们现在呢来看一下咱们这个redis

好

你看现在里边是没有东西的对吧

里边没有东西

然后呢我们执行一下

点execute

好

执行完了对吧

应该success

已经执行成功

执行成功之后呢

咱们先来看一下redis

重新加载一下

大家看address book

然后下边呢

这个其实是使用的什么呢

我们当前用户的ID啊

作为什么呢

作为这个key对吧

然后呢

这里边只存的其实是我们那个对象

entity对象

好

然后呢

到这边来刷新一下

刚才看是58条数据对吧

然后我们刷新一下

变成59条了对吧

应该就是最后这一条啊

就最后这条

来找一下是不是最后这条

但是它这个不一定是最后这条啊

因为它并不是按

根据我们这个ID牌的序啊

所以说这里边呢

我们就不再具体去找它了

因为这个数据稍微有点乱

那么能看到那条数据已经插入成功了

就可以了

好

那么这是咱们这个新增

地址部这个接口

那么我们简单测试一下就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程演示了一个基于 Spring Boot 的地址簿服务的开发与测试流程。主要内容包括：

*   **服务端开发**：在 IntelliJ IDEA 中编写 `AddressBookController` 控制器，处理 `POST /addressBook/save` 请求，将数据保存到数据库。
*   **数据模型设计**：定义 `AddressBook` 实体类，使用 `@Data`、`@TableName`、`@TableId` 等注解，并实现 `Serializable` 接口以支持序列化。
*   **数据库操作**：通过 MyBatis 框架，使用 `AddressBookMapper` 接口和对应的 XML 映射文件进行数据持久化。
*   **接口文档**：使用 Swagger 生成并展示 API 文档，方便前端调用和测试。
*   **数据验证与测试**：通过 Swagger UI 发送 HTTP 请求，验证后端服务的正确性，并通过 Navicat 数据库工具验证数据是否成功写入数据库。

整个过程展示了从后端代码编写、数据库设计、接口文档生成到最终功能测试的完整闭环。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：课程开场，展示项目结构和 `AddressBookController.java` 文件，讲解 `@PostMapping` 注解用于处理 POST 请求。
*   **00:05 - 00:15**：讲解 `@RequestBody` 注解，用于接收前端传来的 JSON 数据，并演示如何在控制器中处理该数据。
*   **00:15 - 00:25**：展示 `AddressBook` 实体类的定义，重点讲解 `@Data`、`@TableName`、`@TableId` 注解的含义，以及 `implements Serializable` 的作用。
*   **00:25 - 00:35**：演示如何在 `AddressBook` 类中定义 `@TableId` 注解，指定主键字段 `id` 的类型为 `IdType.ASSIGN_UUID`，并展示 `@Accessors` 注解的使用。
*   **00:35 - 00:45**：讲解 MyBatis 的 Mapper 接口和 XML 映射文件，展示 `AddressBookMapper.xml` 文件的结构。
*   **00:45 - 00:55**：演示如何在 `AddressBookController` 中添加 `@GetMapping("/detail/{id}")` 方法，用于根据 ID 查询地址详情。
*   **00:55 - 01:05**：展示 Swagger UI 界面，讲解如何通过 Swagger 文档查看和测试 `POST /addressBook/save` 接口。
*   **01:05 - 01:15**：在 Swagger UI 中填写请求体，设置 `Content-Type` 为 `application/json`，并准备发送请求。
*   **01:15 - 01:25**：执行 POST 请求，查看响应结果，确认服务成功返回 `200 OK`。
*   **01:25 - 01:35**：切换到 Navicat 数据库工具，执行 SQL 查询 `SELECT * FROM pd_users.pd_address_book LIMIT 1,1000`，验证数据是否已成功写入数据库。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **文档标题**：`品达物流订单模块--Swagger文档`。
    *   **章节结构**：
        *   第五章：创建上面Mapper接口对应的xml映射文件。
        *   第五节：`4.4.2 根据id查询地址详情`。
    *   **代码片段**：
        *   **控制器代码**：
            ```java
            @PostMapping("/save")
            public Result save(@RequestBody AddressBook entity) {
                if (1 == entity.getIsDefault()) {
                    addressBookService.lambdaUpdate().set(AddressBook::getIsDefault, 0).eq(AddressBook::getId, entity.getId()).update();
                }
                boolean result = addressBookService.save(entity);
                if (result) {
                    cacheChannel.set(region, entity.getId(), entity);
                    return Result.ok();
                }
                return Result.error();
            }
            ```
        *   **实体类代码**：
            ```java
            @Data
            @EqualsAndHashCode(callSuper = false)
            @TableName("pd_address_book")
            public class AddressBook implements Serializable {
                @TableId(value = "id", type = IdType.ASSIGN_UUID)
                private String id;
                // 其他字段...
            }
            ```
        *   **Mapper 接口代码**：
            ```java
            @Mapper
            public interface AddressBookMapper extends BaseMapper<AddressBook> {
            }
            ```
        *   **XML 映射文件代码**：
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
                "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
            <mapper namespace="com.ithema.pinda.mapper.AddressBookMapper">
            </mapper>
            ```
        *   **Swagger 接口文档**：
            ```json
            {
                "address": "北京",
                "cityId": 10,
                "companyName": "中智",
                "countryId": 58,
                "createTime": "2020-08-18T01:28:05.152Z",
                "defaultId": 0,
                "phoneNumber": "13412345678",
                "provinceId": 18,
                "userIp": "string"
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：控制器方法开发**（00:00 - 00:15）
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `AddressBookController.java` 文件，演示如何使用 `@PostMapping` 注解定义一个保存地址簿的接口。他展示了如何通过 `@RequestBody` 注解接收前端传来的 JSON 数据，并在方法体内进行业务逻辑处理，例如判断是否为默认地址并更新数据库。

*   **场景二：实体类设计与注解**（00:15 - 00:35）
    *   **描述**：讲师切换到 `AddressBook.java` 文件，讲解 `@Data` 注解自动生成 getter/setter 方法，`@TableName` 注解指定数据库表名，`@TableId` 注解指定主键字段及其生成策略。他特别强调了 `implements Serializable` 接口的重要性，以确保对象在序列化和反序列化时能够正常工作。

*   **场景三：数据库操作与 MyBatis**（00:35 - 00:45）
    *   **描述**：讲师展示了 MyBatis 的 Mapper 接口 `AddressBookMapper`，并讲解了如何通过 XML 文件定义 SQL 映射。他强调了 `@Mapper` 注解的作用，以及如何通过 `BaseMapper` 继承来简化 CRUD 操作。

*   **场景四：Swagger 接口测试**（00:45 - 01:15）
    *   **描述**：讲师切换到浏览器，打开 Swagger UI 页面，演示如何查看 `POST /addressBook/save` 接口的详细信息。他指导观众如何填写请求体，设置 `Content-Type` 为 `application/json`，并点击“Execute”按钮发送请求。他展示了请求成功后返回的 JSON 响应体，确认服务正常工作。

*   **场景五：数据库验证**（01:15 - 01:35）
    *   **描述**：讲师切换到 Navicat 数据库工具，执行 SQL 查询语句 `SELECT * FROM pd_users.pd_address_book LIMIT 1,1000`，验证数据是否已成功写入数据库。他通过查询结果确认了数据的正确性，从而完成了整个功能的闭环验证。
