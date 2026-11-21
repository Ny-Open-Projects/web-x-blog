# 12-权限业务接口-保存角色权限接口外层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习

权限核心逻辑接口的实现

这一小节比较重要

大家要好好掌握

针对于比较复杂的权限逻辑

通过Split Data List是不便于处理

因为咱们还加很多逻辑的判断

这个时候咱们就需要再包装一层

通过Split Boot Control去提供对应接口

然后再调用Service处理具体逻辑

首先咱们来看一下保存角色权限接口

角色它是由不同的权限组合形成的

每个角色都拥有自己的菜单

以及相应的操作权限

在这里通过后台进行管理和配置

那么咱们就来做一个具体实现

这个接口就是实现角色和菜单

操作权限信息的关联处理

咱们回到工程当中

在这里我们去创建一个Service

这个Service名称

我们就叫做Ausolated Locked Service

这个是它的实现类加上Employment

接下来我们就来实现保存角色指定的权限信息接口

这个它也可以支持批量的操作

多个角色可以同时保存

那么只要咱们实现一个角色的关联保存

多个角色只要在外层再一个循环处理就可以了

咱们就来看一下它具体是如何实现的

在这里咱们定义一个方法

Public

这个是用来保存角色权限

它的参数是Aus

然后要传递需要保存关联的角色ID信息

外层拷数对应的一场Business

将业务一场的拷数

首先咱们打印一个日志

加上Logbook的主页Logbook的截图

我们打一个提示信息

说明了它已经进行了批量了

进入到网络当中

将它的参数打印出来

这个是Logos的参数

然后再打印Logid的参数

咱们来看一下这个参数里面具体是怎样的格式呢

Logos它其实包括菜单的信息以及操作的信息

那么菜单跟操作都通过这个参数传递过来

如何去区分与标识呢

那我们在这里会约定M开头代表是菜单

那菜单后面

比如它的ID

是1001

那么O开头的话呢

代表的是操作

它的ID呢

比如说20001

这样的话呢

他们通过逗号进行拼接

然后呢

组成一个支付算

说明了Logos参数

那么Logids呢

在这里呢

它的参数呢

那就比较简单

比如说一个JSID呢

它是1001

另外一个JSID呢

它是10002

这样呢

它是以数组的形式呢

传递进来的

拿到这个Logids呢

咱们就可以进行了多个

角色的权限分配

这个是他们的一个参数格式

咱们呢

要了解清楚

那接下来呢

咱们先写下整体的业务处理流程

第一步呢

我们要保存多个角色的权限信息

支持呢

批量方式处理

这个批量方式呢

参数是由前端进行交易

也就是说

你传递过来的参数

一定要符合刚才咱们的规范

对不对

在这里我们后台就不做

过多的参数校验

减少一些代码量

那我们专注于核心逻辑的处理实现

外层的话呢

是一个过循环

是去

Logid

将传递过来的Logids输出呢

做个编例

然后第二步呢

咱们是要

将Logid信息呢

转换

并且呢

校验角色

信息呢

是否存在

那我们呢

先将它转换为Login

Logid

Log

然后Log.Bidigob

Logid

然后我们就来做一个校验

Epinion

这里面的话呢

OSLO

然后要从数据层当中呢

获取对应的数据

咱们将数据层接口呢

注入进来

这个呢

是用户角色的数据层接口

好呢

根据角色ID查找对应数据

下面呢

咱们就要做一个判断

如果是这个呢

不存在

那么呢

咱们要抛出一个异常

就没必要进行下面逻辑的处理

Application

UserNode

UserNodeNodeFound的异常错误提示

好

最后呢

咱们就要保存角色

角色与权限的外联关系

咱们呢

先给它写上一个空的方法

后面呢

咱们再做一个具体实现

将参数呢

传递进去

我们再将这个方法呢

完善一下

这里呢

咱们要给它加上助剪

开启事物功能

go back for

如果抛出异常的时候呢

要进行事物的回滚

这个呢

就标示为所有异常

然后呢

我们再给它加上方法的

故事说明

这个方法呢

是保存角色指定的权限信息

可以支持呢

提亮方式

多个角色可以呢

同时保存

好

在这里呢

就是对角色和权限的外层处理逻辑

那内层的话呢

具体的实现

咱们下个章节呢

再做具体讲解

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的后台管理系统权限模块开发教程。讲师正在讲解如何实现“权限核心逻辑接口”，其核心目标是为系统中的“角色”（Role）保存“权限”（Privilege）信息。讲师通过在 `AuthorityLogicService` 服务层中编写代码，演示了如何接收前端传入的角色名和权限ID列表，然后通过数据访问层（Repository）进行数据库操作。视频重点展示了如何在服务层中进行数据校验（如校验角色是否存在），并调用自定义的 `saveRolePrivileges` 方法来建立角色与权限的关联关系。整个过程体现了典型的分层架构（Controller -> Service -> Repository）和面向接口编程的思想。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:06**: 视频开头，讲师在 Typora 文档中展示课程大纲，定位到“3.7 权限核心逻辑接口实现 (重要)”这一章节，说明本节内容的重要性。
*   **00:06 - 00:18**: 讲师切换到 IDE，展示项目结构，定位到 `StockAdminUserApplication` 启动类，准备进入服务层代码。
*   **00:18 - 00:35**: 讲师在 `AuthorityLogicServiceImpl` 类中编写 `savePrivileges` 方法的主体逻辑，包括日志记录、参数校验和角色存在性检查。
*   **00:35 - 00:48**: 讲师在代码中添加了 `@Autowired` 注解，注入 `AuthorityRoleRepository`，并开始编写角色存在性校验的 `if` 语句。
*   **00:48 - 00:55**: 讲师在 `if` 语句中抛出 `BusinessException`，并传入自定义的错误码 `ApplicationErrorCodeEnum.USER_ROLE_NOT_FOUND`，以处理角色不存在的异常情况。
*   **00:55 - 01:05**: 讲师在 `if` 语句后添加了注释“3. 保存角色与权限的关联关系”，并准备调用 `saveRolePrivileges` 方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.7 权限核心逻辑接口实现 (重要)`
    *   **核心概念**: “角色就是由不同权限组合形成，每个角色有自己的菜单与操作权限，通过后台进行管理配置。”
    *   **接口定义**: `业务层 AuthorityLogicService 接口`，并展示了其方法签名：
        ```java
        /**
         * 保存角色指定的权限信息（支持批量，多个角色同时保存）
         * @param roleAuth
         * @param roleIds
         */
        @Override
        @Transactional(rollbackFor = Exception.class)
        ```

*   **代码关键内容**:
    *   **服务层方法**: `AuthorityLogicServiceImpl` 中的 `savePrivileges` 方法。
    *   **方法签名**:
        ```java
        public void savePrivileges(String roleAuth, String... roleIds) throws BusinessException {
        ```
    *   **日志记录**:
        ```java
        log.info("Process in AuthorityLogicServiceImpl.savePrivileges method. params, roleAuth: " + roleAuth + ", roleIds: " + Arrays.toString(roleIds));
        ```
    *   **角色存在性校验**:
        ```java
        Long roleIdLong = Long.valueOf(roleId);
        Optional<AuthorityRole> authorityRole = authorityRoleRepository.findById(roleIdLong);
        if (authorityRole.isPresent()) {
            // 角色存在，继续处理
        } else {
            throw new BusinessException(ApplicationErrorCodeEnum.USER_ROLE_NOT_FOUND);
        }
        ```
    *   **待实现的关联关系保存**:
        ```java
        // 3. 保存角色与权限的关联关系
        saveRolePrivileges(roleIdLong, roleAuth);
        ```
    *   **IDE 中的错误提示**: 在调用 `saveRolePrivileges` 方法时，IDE 显示“Cannot resolve method 'saveRolePrivileges(java.lang.Long, java.lang.String)'”，表明该方法尚未在 `AuthorityLogicServiceImpl` 中实现，或在其他类中未定义。

---

### 4) 关键场景与演示描述

*   **场景一：课程定位与目标**
    *   **描述**: 讲师首先在 Typora 文档中展示课程大纲，明确指出本节的核心是“权限核心逻辑接口实现”，并强调其重要性。这为后续的代码开发设定了清晰的目标。

*   **场景二：服务层方法开发**
    *   **描述**: 讲师在 IDE 中打开 `AuthorityLogicServiceImpl` 类，开始编写 `savePrivileges` 方法。他首先添加了日志记录，用于追踪方法的执行过程和参数。接着，他通过一个 `for` 循环遍历所有传入的权限ID，并对每个权限ID进行转换和校验。

*   **场景三：角色存在性校验与异常处理**
    *   **描述**: 讲师在循环体内，使用 `authorityRoleRepository.findById(roleIdLong)` 查询数据库中是否存在该角色。如果查询结果为空（`!authorityRole.isPresent()`），则抛出一个 `BusinessException`，并传入自定义的错误码 `ApplicationErrorCodeEnum.USER_ROLE_NOT_FOUND`，以向调用方返回明确的错误信息。

*   **场景四：方法调用与错误提示**
    *   **描述**: 讲师在完成角色校验后，准备调用 `saveRolePrivileges` 方法来保存角色与权限的关联关系。此时，IDE 显示了“Cannot resolve method”的错误，这表明讲师正在演示一个“待完成”的步骤，即 `saveRolePrivileges` 方法的实现尚未完成，需要在后续的视频中进行讲解。

---
