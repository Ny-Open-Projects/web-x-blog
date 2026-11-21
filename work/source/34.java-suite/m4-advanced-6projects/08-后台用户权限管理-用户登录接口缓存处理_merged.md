# 08-后台用户权限管理-用户登录接口缓存处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢去实现用户登录接口的处理逻辑

那上一讲呢咱们是实现了用户最大角色权限的获取

那拿到用户最大权限角色之后呢

咱们也将它呢放置在Aux里U者对象里面

这样的客户端它就能够拿到呢

咱们服务端处理之后的最大角色权限信息

再往下面呢咱们就来实现了第五个步骤

获取呢用户的角色菜单操作权限信息

然后将它呢存入款程当中

那首先呢咱们要获取用户的菜单操作信息

这个呢是一个集合

然后呢咱们通过它的数据层接口

调用了Funderby Low ID的方法

之前呢咱们已经拿到了角色ID

然后做一个围攻判断

如果是OBT

这里面的话呢

有菜单操作权限

信息咱们呢就继续下面的逻辑

将它呢存入款程当中

咱们在这里呢

要对菜单操作权限做一个分组

因为在这里我们采用的是

PageOS的接口

PageOS呢

它有一个重要的特征

就是根据它的一个操作类型

做对应的处理

比如说有Post

有Get对不对

还会有那个Put

这个呢是更新

还会有Delete

好

有不同的操作类型呢

它们调用的地址的都是一样的

这个呢是HeadOS的一个规范

那么咱们要做到操作级别的权限控制呢

这个时候就要给它做一个分组

因为用户呢

它有可能具备了Post的权限

没有Delete的权限

对不对

也有可能有Delete的

没有Post的权限

所以我们并不知道这个URL

这个用户呢

到底是具备哪种操作权限

那么呢

我们就要给它做一个

分组权限

分组汇总

通过URL结合呢

你的操作类型

来判断呢

用户是否具备了真正的操作权限

好

咱们呢就来做一个具体的实现

这个呢是根据

请求接口的

请求类型

做分组汇总处理

转换为Map结构

比如说

具体格式呢

就是Post

然后呢

我们就要做一个具体的实现

这里会跟着一个集合

这个集合的话呢

就可能是

不同的路径有Add

也会有Update

这样呢

就作为一条记录

存储在Map里面

好

我们就来做一个处理

String

这里面因为是一个集合

对不对

有多个例子

好

通过流逝方式呢

做对应的处理

这里面呢

是Collector

Grouping

GroupingBy

然后呢

Post类型

Menu

Operation

这里面要取它的属性

Operation

Icon

这个注意一下

呃

它的实际存储的词呢

就是咱们的

其接口请求类型

比如说Post

Foot

Delete

因为原本这个属性呢

它是存取操作的图标

但是操作图标呢

在这里咱们没有去做具体的运用

所以呢

咱们就采用这个字段

来存储了它的接口请求类型

这一点呢

大家要理解清楚啊

接着换的是Mapping

MenuOperation

获取它的URL

例子

然后呢

咱们要将它转换成为一个集合

ToSet

这个可以不用保存顺序

所以采用Set

效率呢

会更高一些

接下来咱们如何去存取到款存当中呢

咱们呢

给大家画一下整个处理流程

在这里的Map结构呢

它其实呢

请求类型已经呢

URL组成了

这个呢

咱们逆举一下

Post了

这个呢

是它的一个Key

然后呢

这边是它的Value

Value在这里呢

就会是一个Set集合

Set集合下面呢

会存储多个路径

比如说Add路径

还有Update的接口

然后呢

Delete

比如说这里面的话呢

又是一个Set集合

然后的话呢

它可能会有UserDelete

或者还会有OrderDelete等等

好

这个呢

是咱们的Map里面的存储结构

那么咱们要转换成为Ladies的存储结构

该怎么去处理呢

那比如在这里呢

是一个Ladies

那Ladies的话呢

它的存储也是一个Key

然后呢

是它的一个Value

在这里它的Key的格式呢

就是UserID

然后呢

再去拼接

我们呢

一个注线做分割

然后再去拼接呢

它的操作类型

比如说是Post

接着的话呢

就是存取它的值

比如在这里面的它的值呢

是有多个UI路径

那这里呢

就存入它的Set的UI路径进行

这里面的话呢

就可能会有多个地址

Update等等

好

这个呢

就是Ladies的一个存储

上面的话呢

是咱们的一个Map

的存储

这个结构呢

咱们要理解清楚

差别的话呢

是咱们要在Ladies上面附带它的User信息

对不对

后面做权限控制的时候呢

咱们才知道哪个用户

它具备了哪些权限

好

那咱们呢

又来对代码做具体实现

首先做一个判断

这个呢

Size要大于0

然后呢

我们要拿到缓存对象

通过CacheManage

GetCache

这个是小写

GlobalConsistence

给它一个值

这个值呢

就叫Oscillate

然后是MenuKey

接着呢

咱们再对这个Size的结构呢

做一个编辑处理

ForEach

一个是它的Key

一个是它的GD

URL信息

咱们呢

给它加上对应的故事说明

将Map的菜单操作信息

淪入至Ladies网站当中

格式呢

就是user

key呢

就等于userID

然后再加上书线

再加上ObligType操作类型

它的Value呢

就是set URI信息

这个呢

咱们Ladies当中呢

就不采用set

这样呢不便于处理

咱们采用的呢

就是这种上的拼接

URI1

然后呢

URI2

将这个set的结构呢

转化成为一个通过逗号拼接

拼接而成的支付串

接下来呢

咱们就来对set里面的URI数据呢

做一个编辑处理

对URI

结合呢

做编辑处理

将权限菜单信息

按指定格式

淪入至Ladies当中

这里要注意一下

set里面的数据呢

是可以支持多个URI记录

那么在这里呢

咱们要将它呢

转换到set里面

然后呢

存置Ladies当中

因为Ladies里面的话呢

它的值其实呢

就是一个set的对象

需转换至set的结合当中

也就是要做一个拆分处理

那咱们呢

从代码上面做一个具体实现

这个呢

就可以支持多个URI路径的一个配置

我们通过流逝方式进行处理

那我们看一下该怎么去转换呢

通过flat map方法

然后呢

拿到它具体的值

将它值里面的话呢

如果是存在逗号的记录呢

要做分割处理

map

share

并且呢

去除对应的空格

然后呢

咱们将它呢转换成为一个set的结合对象

也就是呢

咱们在这里呢

这里存出了set集合对象的这里面的set信息

它会有多条记录

对不对

比如说有add方法

然后下面的话呢

有delete方法

那在这里呢

也有可能会有一个update

然后呢

一个modify

咱们这段代码的意思呢

就是将这个update

modify这条记录呢

将它的逗号做分割处理

最终的话呢

它会转换成为几条记录呢

这个数据呢

就会转换成为四条数据

对不对

之前呢是三条

这个结合是三条

通过这个转换之后呢

就会存在四条记录

就是说做了完全的分割处理

好

最后呢

咱们将它

存入到Ladies款中

这个ID

按照咱们约定的格式

Global Consistency

这里要是Pride

再加上Opplate

操作类型

然后呢

就存入刚才转换的UIL结合

这样呢

咱们就完成了

这个菜单全线信息的处理

那么在最后我们也将

Opplate

U者对象的返回出去

那么呢

咱们就完成了

用户登录接口的具体处理逻辑

好

接下来呢

咱们再回到讲义当中做一个回顾

用户登录接口呢

貌似看起来比较简单

但是呢

里面还是有较多的处理逻辑

刚才呢

也带着大家做了具体实现

咱们呢

再来回顾分析一下

首先呢

要根据传递的账号来查找用户呢

是否存在

不存在呢

要保持异常

没法继续下面逻辑的处理

密码呢

它是在数据过程中

密码它在数据过程中呢

是密吻

要加密呢

去判断密码呢

是否正确

错误呢

我们同样要给出一个提示信息

接着话呢

咱们要记录用户的登录信息

比如说它的登录时间啊

登录IP

然后保存菜单全线信息到款存当中

为什么是要放在款存里面呢

放在款存当中的作用呢

第一是可以实现服务的无状态化

第二呢

可以提升处理性能

最后呢

菜单和操作

它是分开存储的

要把这两部分数据的UI呢

统一记录下

通过呢

set集合

咱们呢

就可以做一个去从处理

对不对

我们采用了

servincage加ladies呢

去存储对应的数据

刚才也讲解了

它的一个存储

结构

那么它的一些存储格式呢

咱们要了解清楚

后面做权限控制的时候呢

是需要使用到的

最后呢

咱们就来对controller层

做一个实现

那快速起见呢

咱们在这里

就将它的登录方法

拷贝进去

好

这个呢

是用户的登录方法

这个service呢

咱们已经注入进去了

好

这注释呢

咱们就不添加了

因为这里呢

已经有SWOG的注释说明

这个配置的话呢

大家要了解一下

就是

SWOG2的

它的属性注释

该怎么去配置

之前呢

也做了讲解

然后呢

是参数相关的教研规则

比如说

账号的长度教研

这个呢

可以根据实际需要

采用了不同的一些教研约束

接着的话呢

就是用户登录的具体处理逻辑

咱们呢

通过service

去做对应的实现

那么这个接口呢

还没有抽取出来

咱们回到user service里面

在这里呢

我们通过

reflect

forman bus app

将user

这个users

login这个方法呢

抽取出来

reflect

抽取完成之后呢

在这里就没有包错了

用户登录处理完成之后呢

不要忘记了

咱们要将用户登录的信息呢

保存在sha里面

后面的时候呢

一些业务操作都会用到呢

当前登录的用户信息

比如之前章节当中呢

咱们所讲的新建用户接口

对不对

它在这里呢

就要去获取当前登录用户的信息

这一块呢

就是

conclude成接口的具体处理

好

那在这里呢

咱们就实现了

后台用户登录接口的处理

这讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个后台管理系统（`bulls-stock-admin`）的用户登录与权限控制模块的开发演示。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了 `AuthorityUserService` 服务层中用户登录逻辑的实现细节，重点包括：

*   **用户登录校验**：检查密码是否匹配。
*   **角色权限获取**：从数据库查询用户关联的角色列表。
*   **角色优先级处理**：通过 `getPriorityAuthorityUserRole` 方法获取具有最高优先级的角色ID。
*   **菜单操作权限获取**：根据角色ID查询该角色对应的菜单操作权限，并将其转换为 `Map<String, Set<String>>` 结构，便于后续的权限控制。
*   **数据缓存**：将用户ID和其权限信息存入缓存（`cache.put`），以提高后续访问效率。
*   **代码优化与调试**：演示了如何使用 Java 8 的 Stream API 对权限数据进行分组和转换，并处理了编译时的类型错误。
*   **控制器层**：简要展示了 `AuthorityUserController` 控制器类的结构，包括 `@ApiImplicitParam` 注解用于 Swagger 文档和参数校验。

整个过程体现了典型的 Spring Boot + Spring Security 应用中，服务层如何处理业务逻辑、数据查询、权限管理和缓存策略。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示 `AuthorityUserService` 类中 `userLogin` 方法的代码，主要逻辑是校验密码并保存登录信息。
*   **00:00:05 - 00:00:15**：讲师开始讲解获取用户角色权限的逻辑，调用 `authorityUserRoleRepository.findByUserId` 方法。
*   **00:00:15 - 00:00:25**：讲解 `getPriorityAuthorityUserRole` 方法，用于从角色列表中获取最高优先级的角色ID。
*   **00:00:25 - 00:00:35**：讲解获取角色菜单操作权限，调用 `authorityMenuOperationRepository.findByRoleId` 方法。
*   **00:00:35 - 00:00:45**：讲师开始使用 Stream API 对权限数据进行处理，将 `List<AuthorityMenuOperation>` 转换为 `Map<String, Set<String>>`。
*   **00:00:45 - 00:00:55**：演示 Stream API 的 `collect` 方法，使用 `Collectors.groupingBy` 和 `Collectors.mapping` 进行分组和映射。
*   **00:00:55 - 00:01:05**：讲师在代码中添加了 `cache.put` 语句，将用户ID和权限信息存入缓存。
*   **00:01:05 - 00:01:15**：讲师切换到 PPT 页面，展示 `AuthorityUserController` 的代码结构。
*   **00:01:15 - 00:01:25**：在 PPT 中讲解控制器层的注解，如 `@ApiImplicitParam` 用于 Swagger 文档和参数校验。
*   **00:01:25 - 00:01:35**：讲师在 PPT 中讲解密码重置接口的实现思路。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **控制器层**：`AuthorityUserController` 类的代码，包含 `@ApiImplicitParam` 注解。
    *   **密码重置接口**：标题为“1.6 密码重置接口”，描述了其功能。
    *   **服务层**：标题为“1.6 密码重置接口”，并提示“这里提供密码重置功能”。

*   **代码关键内容**：

    *   **用户登录核心逻辑**：
        ```java
        if (authorityUser.getUserPassword().equals(encryptPassword)) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ACCOUNT_PROBLEM);
        }
        authorityUser.setLastLoginTime(new Date());
        authorityUser.setLastLoginIp(clientIp);
        authorityUserRepository.save(authorityUser);
        ```

    *   **获取角色权限**：
        ```java
        List<AuthorityUserRole> roleList = authorityUserRoleRepository.findByUserId(authorityUser.getId());
        if (null == roleList || roleList.size() < 1) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_NOT_ASSIGN_ROLES);
        }
        Long roleId = getPriorityAuthorityUserRole(roleList).getRoleId();
        authorityUser.setRoleId(roleId);
        ```

    *   **获取菜单操作权限**：
        ```java
        List<AuthorityMenuOperation> optList = authorityMenuOperationRepository.findByRoleId(roleId);
        if (null != optList) {
            Map<String, Set<String>> optUrlSets = optList.stream()
                .collect(Collectors.groupingBy(AuthorityMenuOperation::getOperationUri,
                    Collectors.mapping(AuthorityMenuOperation::getOperationId, Collectors.toSet())));
        }
        ```

    *   **缓存数据**：
        ```java
        cache.put(authorityUser.getId() + GlobalConstants.SPLIT + optList, optUrlSets);
        ```

    *   **Stream API 代码**：
        ```java
        optList.stream()
            .collect(Collectors.groupingBy(AuthorityMenuOperation::getOperationUri,
                Collectors.mapping(AuthorityMenuOperation::getOperationId, Collectors.toSet())));
        ```

---

### 4) 关键场景与演示描述

*   **场景一：用户登录校验与角色权限获取**
    *   讲师在 `AuthorityUserService` 中，首先检查用户输入的密码是否与数据库中加密后的密码匹配。如果匹配，则继续执行后续逻辑。
    *   接着，讲师调用 `authorityUserRoleRepository.findByUserId` 方法，查询该用户的所有角色信息。
    *   通过 `getPriorityAuthorityUserRole` 方法，从角色列表中获取具有最高优先级的角色ID，并将其设置到 `authorityUser` 对象中。

*   **场景二：菜单操作权限处理与缓存**
    *   讲师调用 `authorityMenuOperationRepository.findByRoleId` 方法，根据角色ID查询该角色对应的菜单操作权限。
    *   使用 Java 8 的 Stream API，将 `List<AuthorityMenuOperation>` 转换为 `Map<String, Set<String>>`，其中键是操作URI，值是该URI对应的操作ID集合。
    *   讲师在代码中添加了 `cache.put` 语句，将用户ID和权限信息存入缓存，以便后续请求可以直接从缓存中获取，提高性能。

*   **场景三：代码调试与优化**
    *   讲师在编写 Stream API 代码时，遇到了编译错误，提示 `cannot resolve symbol 'set'`。
    *   讲师通过查看 IDE 的自动补全建议，选择了 `Collectors.toSet()` 方法，成功解决了问题。
    *   讲师还演示了如何使用 `Arrays.stream(str.split(regex)).map(String::trim)` 来处理字符串数组。

*   **场景四：控制器层介绍**
    *   讲师切换到 PPT 页面，介绍了 `AuthorityUserController` 类。
    *   讲师解释了 `@ApiImplicitParam` 注解的作用，即用于 Swagger 文档生成和参数校验。
    *   讲师还提到，在参数上加上 `@Validated` 注解，可以配合类上的 `@Validated` 注解一起使用，实现更严格的参数校验。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解这段技术课程的内容。
