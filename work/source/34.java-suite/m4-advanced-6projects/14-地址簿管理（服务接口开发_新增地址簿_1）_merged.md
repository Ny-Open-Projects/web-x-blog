# 14-地址簿管理（服务接口开发_新增地址簿_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才呢 我们这个实体呢 已经导入成功了

接下来呢 就是我们这个服务接口的开发

这块呢 我们一共要涉及到的是五个接口

包括什么呢 新增地址部接口 对吧

然后呢 还有根据ID查询地址部信息

然后呢 分页查询地址部 更新地址部 还有删除地址部

其实呢 就是对我们地址部这个表呢 进行一些增删改查操作

当然是在这个基础之上啊 还加入了一些缓存的操作

因为地址部信息呢 大家可以想一下

它的变动频率是不是非常低 对吧

一般呢 我们录入完成之后呢 很少去修改这个地址部的信息

所以说这块呢 是比较适合使用缓存的

所以说呢 这就是在我们纯增删改查基础之上啊

加入了我们这个J2Cache缓存的操作

整体来说还是比较简单的

所以我们在这块呢 就不再去手敲这个代码了

而是直接从我们讲义上 把这个代码复制过去

然后呢 能够运行成功就可以了

好 那么接下来呢 我们先把这个包呢 先来创建一下

首先呢 我们创建一个controller包

在品达这个下边 我们来创建这么一个包

然后呢 我们需要来创建controller 对吧

这个controller呢 就叫做addressbookcontroller

好 操作我们地址部的

咱们现在呢 要新增地址部 对吧

所以说我们需要在这里边呢 来添加一个叫做save方法

对吧 save方法

整个代码呢 我就直接复制了

复制过来之后呢

咱们大概来读一下这个代码就可以了

复制到这边来看

但是现在呢 他肯定是有报错的地方

是因为我们这儿是不是有一个这个接口

addressbookservice 对吧

这个service接口呢 还没有

我们下一步呢 再来创建它

咱们现在先来看一下

这是日志 对吧

然后呢 restcontroller

然后呢 requestmapping

这些都不用解释了

然后呢 注入service

然后呢 注入这个cachechannel

咱们使用这图cache呢

然后呢 这个save的方法呢

就是把我们的地址部信息呢

我们把我们的地址部信息呢

我们把我们的地址部信息呢

保存在某个区域里面去

这个区域呢 叫做addressbook

而这个区域呢 我们在前面这个配置文件上

是不是也已经定义过了

对吧 addressbook

然后呢 我们在这儿是不是提供了一个叫做save的方法

这就是新增地址部

新增地址部

好

咱们来看一下这个方法

大概读一下就可以了

因为这个代码比较简单

所以我们就不再手敲了

你看save方法

它是不是给我们传过来这么一个对象

就叫做addressbook

这就是通过我们前端 对吧

前端 你看

咱们来看一下我们这个原型吧

对吧

然后呢 在我们这个新增页面

我们是不是录入了这么多的

跟地址部相关的信息

比如这个

这个其实是一个复远框

是一个单选 对吧

这么一个按钮

然后呢 这个是设为地

是否是默认地址

如果是的话

就选中它就可以了

对吧 有姓名 电话

还有这个什么省市区 对吧

还有详细地址等等这些

好

好

好

好

好

, 把这些信息提交过来

它就会封装成这么一个对象

对吧

叫做addressbook

好

然后呢 我们来看啊

首先呢 它来了一个判断

if1等于anted.isdefault

这个isdefault是什么意思呢

注意看

isdefault呢

它其实对应的是这个

是否是默认的

也就是对于我们同一个用户来说

它可能留了很多这个地址信息

对吧

不止一个 有多个

但是呢

默认地址

对吧

信息只能有一个

is default

那么1呢表示默认

1表示默认

所以说呢

我们如果来判断

当前他提交过来的这个

这个is default等于1

这就说明他当前录入的这条

这个地址部信息

应该是作为这个用户

默认的地址部信息

那么有可能他原先

是不是已经存在了

有一些地址部信息

那这个时候呢

我们就需要把他

其他的那些地址部信息

他这个什么呢

is default的这个字段呢

给他改成什么呢

给他改成0

因为我刚才已经解释过了

对于同一个用户来说

他这么多的地址部信息

但是只能有一条是默认的

对吧

不能说好多都是默认的

所以只能有一个是默认的

那这个既然你现在

录入的这个是默认的

那其他的就必须改成非默认的

那么怎么改呢

咱们是不是就调用这个方法

调用这个方法

把这个什么呢

is default的字段

给他改成什么呢

给他改成0

改成0

那么这句话呢

其实就是在做这个事

但是条件是什么呢

是只能改当前用户

对吧

你不能改其他用户的

所以这个条件需要去给他设置好

这是先做一个更新操作

然后接下来呢

我们再正常是不是把它save掉

save掉

然后呢

save掉之后呢

返回值

如果是true的话呢

表示这个录入成功了

录入成功之后呢

我们是不是把它载入缓存就可以了

然后呢

存到这个区域

就是我们这个address book

这个区域

那么具体的key呢

我们这个key的话

为了防止这个冲突

对吧

因为每一个

用户是不是都要缓存自己的

这个地址部信息

所以说呢

我们使用用户的id啊

使用用户的id作为key

这样防止冲突

然后这个值呢

就是整个entity对象

就是这个address book对象

OK

那么这就是咱们这个save方法

整体来说呢

还是非常简单的

那么现在它报错了

就刚才我们说的

有一个service接口

我们是不是需要去定义

所以接下来呢

我们需要把这个service接口呢

来定义出来

到这边来

定义这个接口

咱们先来创建

这个包啊

service包

在这个包下边

我们再来创建这个接口

对吧

接口的名字呢

就叫做

iaddress book service

注意是接口interface

然后在这个接口里边呢

是不是需要来继承啊

咱们整个把这块

复制一下就可以了

你看

我们当前这个接口呢

是不是继承了

这个mybattiesplus

给咱们提供的

iservice接口

好

那这样的话

你看它这边

是不是就不再报错了

好

包括这个什么lambda update

其实也是从这个接口

接口这儿继承过来的

好

这是接口就定义好了

接下来呢

再来提供实现类

实现类呢

是在这个impl包下边来定义

在service下边

再来创建一个包

一个子包impl

对吧

然后呢

我们把这个实现类呢

来创建一下

好

这些代码呢

我们就直接复制了

基本上没什么难度

整个复制过来

大概读一下代码就可以了

好

然后呢

它现在报错呢

是因为还差一个mapper

对吧

所以下一步呢

我们就需要把这个address book

mapper呢

给它创建出来

放在哪了

是不是就放在咱们这个mapper包下边

所以在品达下边

再来创建一个mapper包

然后呢

我们把这个

这其实是个接口

对吧

把这个接口名字啊

给它复制过来

interface

咱们这个接口的话呢

需要继承什么呢

继承mybattiesplus

给我们提供的这个base mapper

同时呢

加一个什么

这个mapper注解

好

代码呢

我就

从这儿来复制一下

粘到这儿

好

然后呢

还有什么呢

还有就是我们这个

对应的插码

应设文件

对吧

这个呢

也是放在resource下边的mapper

resource下边

来创建一层

公路

叫做mapper

对吧

然后呢

在这下边呢

来创建这个应设文件

当然了

我们这个应设文件呢

你可以看到

它其实是个空的

对吧

因为现在呢

我们调用的这些

通用的增生改查方法

由这个mybattiesplus

其实就搞定了

如果你有一些特殊的

特殊的这个circle

那么框架没法提供的话

需要自己在这儿来书写

所以我们把它

这个空文件

也给它提供在这儿

就可以了

那么到这儿的话呢

我们整个

这个新增

对吧

从我们的这个control

到service

到mapper

最终到我们这个应设文件

整个这一套呢

就都提供好了

代码非常简单

那么一会儿呢

我们来测试一下

这个接口

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”系列教程的第3章“用户服务开发”中的第4节“地址簿管理”下的“4.4 服务接口开发”部分。讲师通过 IntelliJ IDEA 开发环境，演示了如何为地址簿功能创建一个完整的 Spring Boot RESTful API。该过程遵循分层架构，依次创建了控制器（Controller）、服务接口（Service Interface）、服务实现类（Service Implementation）和 MyBatis Mapper 接口及对应的 XML 映射文件。核心内容包括使用 `@RestController`、`@PostMapping`、`@Autowired` 等 Spring 注解，以及 MyBatis 的 `@Mapper` 注解和 XML 映射文件来实现数据持久化和缓存操作。整个演示旨在展示如何在实际项目中构建可维护、可扩展的后端服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示 IntelliJ IDEA 项目结构，项目名为 `pinda-tms-java`，当前选中的是 `pd-user` 模块。
*   **00:00:05 - 00:00:15**: 讲师在 Typora 文档中定位到当前章节“4.4 服务接口开发”，并开始讲解“4.4.1 新增地址簿”。
*   **00:00:15 - 00:00:30**: 讲师在 IDEA 中创建 `AddressBookController` 类，并编写其 `save` 方法的框架，包括 `@RestController`、`@RequestMapping` 和 `@Autowired` 注解。
*   **00:00:30 - 00:00:45**: 讲师在 `save` 方法中编写了核心逻辑：判断实体是否为默认状态，调用 `addressBookService.save(entity)` 保存数据，并根据结果设置缓存。
*   **00:00:45 - 00:00:55**: 讲师切换到 Typora 文档，讲解“第二步：创建 `IAddressBookService` 接口”。
*   **00:00:55 - 00:01:10**: 讲师在 IDEA 中创建 `IAddressBookService` 接口，并展示其继承自 `IService<AddressBook>`。
*   **00:01:10 - 00:01:25**: 讲师切换到 Typora 文档，讲解“第三步：创建上面服务接口的实现类 `AddressBookServiceImpl`”。
*   **00:01:25 - 00:01:40**: 讲师在 IDEA 中创建 `AddressBookServiceImpl` 类，并展示其继承自 `ServiceImpl<AddressBookMapper, AddressBook>` 并实现了 `IAddressBookService` 接口。
*   **00:01:40 - 00:01:55**: 讲师切换到 Typora 文档，讲解“第四步：创建 `AddressBookMapper` 接口”。
*   **00:01:55 - 00:02:10**: 讲师在 IDEA 中创建 `AddressBookMapper` 接口，并展示其继承自 `BaseMapper<AddressBook>`。
*   **00:02:10 - 00:02:25**: 讲师切换到 Typora 文档，讲解“第五步：创建上面 Mapper 接口对应的 xml 映射文件”，并展示文件路径 `/resources/mapper/AddressBookMapper.xml`。
*   **00:02:25 - 00:02:40**: 讲师在 IDEA 中打开并展示 `AddressBookMapper.xml` 文件，其中包含 MyBatis 的 XML 命名空间定义。
*   **00:02:40 - 00:02:55**: 讲师切换到 Typora 文档，讲解“4.4.2 根据 id 查询地址簿详情”，并展示在控制器中创建 `detail` 方法的代码框架。
*   **00:02:55 - 00:03:00**: 视频结束。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **文档标题**: `TMS项目讲义_第1章.md`
    *   **章节大纲**: `品达物流TMS项目 > 第3章 用户服务开发(pd-user) > 4. 地址簿管理 > 4.4 服务接口开发`
    *   **关键小节**: `4.4.1 新增地址簿`, `4.4.2 根据id查询地址簿详情`
    *   **技术栈提示**: 文档中多次出现 `jcache多级缓存`、`用户服务数据模型` 等关键词。

*   **代码关键内容**:
    *   **控制器 (`AddressBookController.java`)**:
        ```java
        @RestController
        @RequestMapping("addressBook")
        public class AddressBookController {
            @Autowired
            private IAddressBookService addressBookService;
            private String region = "addressBook";

            @PostMapping("")
            public Result save(@RequestBody AddressBook entity) {
                if (1 == entity.getDefault()) {
                    addressBookService.lambdaUpdate().set(AddressBook::getDefault, 0).eq(AddressBook::getUserId, entity.getUserId()).update();
                }
                boolean result = addressBookService.save(entity);
                if (result) {
                    cacheChannel.set(region, entity.getId(), entity);
                    return Result.ok();
                }
                return Result.error();
            }
        }
        ```
    *   **服务接口 (`IAddressBookService.java`)**:
        ```java
        public interface IAddressBookService extends IService<AddressBook> {
        }
        ```
    *   **服务实现 (`AddressBookServiceImpl.java`)**:
        ```java
        @Service
        public class AddressBookServiceImpl extends ServiceImpl<AddressBookMapper, AddressBook> implements IAddressBookService {
        }
        ```
    *   **Mapper 接口 (`AddressBookMapper.java`)**:
        ```java
        @Mapper
        public interface AddressBookMapper extends BaseMapper<AddressBook> {
        }
        ```
    *   **XML 映射文件 (`AddressBookMapper.xml`)**:
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
            "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
        <mapper namespace="com.ithema.pinda.mapper.AddressBookMapper">
        </mapper>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建控制器**
    *   讲师在 IntelliJ IDEA 中，通过右键点击 `controller` 包，选择新建 Java 类，命名为 `AddressBookController`。
    *   讲师在类中添加了 `@RestController` 和 `@RequestMapping` 注解，并使用 `@Autowired` 注解注入了服务接口 `IAddressBookService`。
    *   讲师在类中定义了一个私有字符串变量 `region` 用于缓存。

*   **场景二：编写控制器方法**
    *   讲师在 `AddressBookController` 类中创建了 `save` 方法，并使用 `@PostMapping` 注解。
    *   讲师在方法中使用 `@RequestBody` 注解接收前端传来的 `AddressBook` 实体。
    *   讲师编写了业务逻辑：判断实体是否为默认状态，如果为默认状态，则使用 `lambdaUpdate` 方法更新数据库；然后调用 `save` 方法保存实体。
    *   讲师在保存成功后，使用 `cacheChannel.set` 方法将数据存入缓存，并返回 `Result.ok()`。

*   **场景三：创建服务接口与实现**
    *   讲师在 Typora 文档中切换到“第二步：创建 `IAddressBookService` 接口”。
    *   讲师在 IDEA 中创建了 `IAddressBookService` 接口，并使其继承自 `IService<AddressBook>`。
    *   讲师在 Typora 文档中切换到“第三步：创建上面服务接口的实现类 `AddressBookServiceImpl`”。
    *   讲师在 IDEA 中创建了 `AddressBookServiceImpl` 类，并使其继承自 `ServiceImpl<AddressBookMapper, AddressBook>` 并实现了 `IAddressBookService` 接口。

*   **场景四：创建 Mapper 接口与 XML 文件**
    *   讲师在 Typora 文档中切换到“第四步：创建 `AddressBookMapper` 接口”。
    *   讲师在 IDEA 中创建了 `AddressBookMapper` 接口，并使其继承自 `BaseMapper<AddressBook>`。
    *   讲师在 Typora 文档中切换到“第五步：创建上面 Mapper 接口对应的 xml 映射文件”。
    *   讲
