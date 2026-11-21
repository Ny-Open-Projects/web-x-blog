# 12-全局权限控制-目标与学习步骤 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做个回顾和总结

首先咱们来明确本章的学习目标

在这里咱们要掌握两点

第一点要完成后台的创建用户接口

密码重置接口

以及产品相关的接口

产品管理接口

产品分类管理接口

第二点咱们要掌握SplintCache的使用

还有SplintSessionLadies

分布式绘画的集成和运用

咱们来回顾一下本章的具体讲解内容

首先咱们对整体的实现做了一个讲解

为什么要去完成对应的登录接口

用户接口

以及产品相关的接口

这个是为咱们后续核心功能的实现

做好对应的铺垫

因为这些都是一些基础核心的数据

接着咱们就去实现了

后台创建用户的接口

后台用户创建的话

其实逻辑来讲并不复杂

咱们的话按照JPA的规范

去实现了用户的数据层操作接口

在这里咱们最主要是要掌握

JPA的动态的查询实现

咱们是通过一个数据层的查询

根据用户账号编号去获取了用户对象

在这里如果是有需要

咱们还可以扩展

我们可以扩展

更多的条件去实现了JPA的动态查询

这个它都是可以支持的

还可以支持多种操作服的查询

比如说Like

JPA的实现它也比较丰富

并不只是仅仅局限于Lipocytol

这个标准化的接口

下面咱们就讲解了Splint Session

Ladies的实现

通过这个组件可以帮助咱们在微服群当中

实现多种的查询

统一的绘画管理

可以保障用户的绘画数据

不会造成丢失的问题

它整个的配置实现来讲

也是比较简便

没有太强的轻度性

咱们只要做好相应的配置

在代码当中开启对应的注解就可以了

Session的处理还是按照之前的方式去做对应的实现

不需要做任何调整与修改

接着的话

咱们就讲解了获取客户端的真实有效IP

获取客户端真实IP的话

这个方法有很多种

但是咱们要根据实际的需要去做对应的改进

来获取有效真实的用户IP

如果是咱们的服务前置采用的是NGGS

那么它的优先级在这里面

就要改成NGGS的头部信息

也就是X6 IP

在用户采用的多层代理的情况下面

比如说它经过了多个VPN进行的转发

那么如果还想获取它的真实IP

就需要采用一些逆向追踪的方法

比如GS杀监或者其他方案

最终目的都是从用户的源头上面去附带用户的IP信息

然后再传递到服务端

只不过这种获取的方式来讲

有通过GS的或者是通过第三方服务器的等等不同方式

再往下面

咱们就讲解了ServinCache的集成使用

咱们在之前实现OS2认证的时候

也做了一个运用

但是还没有去深入讲解

在这里

咱们就详细讲解了ServinCache所提供的一些功能

以及这些功能的具体作用

再往下面

咱们就是实现了后台用户的登录接口

后台用户登录接口是比较核心的一个功能

在这里面会涉及到很多的流程

需要去做对应的处理

比如说咱们的一个用户信息的记录

然后用户的菜单全线缓存记录的处理

这些咱们要理解好

我们在权限控制当中是采用怎样的数据格式规范

就能理解了为什么代码当中要这么去做对应的处理

再往下面

就是对密码重置接口的实现

这个并非核心功能

但是这个是比较实用的一个功能

咱们也将它做对应的实现

下面的是产品管理和分类接口的具体实现

这两个接口是通过ServinDataRest做的实现

提供了HitOS规范的接口可以呢快速盘换接口的实现

提供了HitOS规范的接口可以呢快速盘换接口的实现

帮助咱们去实现这两个对象的增伤改差操作

同时呢也可以去实现自定义的一些接口

比如说根据股票编号获取股票对象等等

最后咱们再来总结一下

本章的话呢

是完成了用户的创建密码重置产品和分类管理相关的接口

在这里的设计的基础点也比较多

咱们要掌握好ServinCache

ServinSessionLadies的集成和运用

了解和掌握真实有效的IP的获取方法

这个IP的获取呢

因为实际的场景来讲也是比较错综复杂

所以咱们要根据具体的业务场景需要采用合适的方案做对应处理

在这里呢就是对本章内容的回顾和总结

那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是“交易平台 - Day 11”的一部分，主要讲解后台用户权限管理功能的实现。核心内容包括：创建用户接口、实现 Spring Session Redis 分布式会话、获取客户端真实 IP、集成 Spring Cache、实现后台用户登录接口以及密码重置接口。课程通过代码演示和 PPT 讲解，重点介绍了如何在 Spring Boot 项目中集成这些技术，并强调了在具体业务场景中选择合适方案的重要性。

---

### 2) 按时间顺序的章节（带时间点）

由于截图未提供精确的时间戳，以下章节结构基于画面内容进行逻辑划分：

*   **第 1 节：学习目标与实现概览 (00:00 - 00:30)**
    *   介绍本章目标：完成后台用户权限管理功能，包括创建用户、登录、密码重置、产品管理等接口。
    *   概述实现步骤：从创建用户接口开始，到实现 Spring Session Redis、获取真实 IP、Spring Cache 集成，最后实现登录和密码重置接口。

*   **第 2 节：后台创建用户接口实现 (00:30 - 01:15)**
    *   **1.1 后台创建用户接口实现**：定义 `AuthorityUserRepository` 接口，使用 `@Repository` 和 `JpaSpecificationExecutor` 进行自定义查询。
    *   **1.2 Spring Session Redis 实现分布式会话**：讲解在微服务架构下如何通过 Spring Session Redis 解决会话数据丢失问题，展示 `pom.xml` 中的依赖配置。
    *   **1.3 获取客户端真实有效 IP**：演示如何在 `BaseController` 中通过 `HttpServletRequest` 获取客户端 IP，处理代理和 VPN 场景。
    *   **1.4 Spring Cache 集成使用**：介绍 Spring Cache 的核心接口 `Cache` 和 `CacheManager`，并说明其与 Redis 的关系。

*   **第 3 节：后台用户登录接口实现 (01:15 - 02:00)**
    *   **1.5 后台用户登陆接口实现**：展示 `AuthorityUserServiceImpl` 中的登录逻辑，包括密码加密校验、记录登录信息、保存菜单权限至 Redis。
    *   **1.6 密码重置接口**：讲解如何通过 `@ApiImplicitParam` 和 `@Validated` 注解来定义和校验密码重置接口。

*   **第 4 节：总结 (02:00 - 02:30)**
    *   总结本章内容，强调完成的接口功能和掌握的核心技术：Spring Cache、Spring Session Redis 的集成使用，以及获取真实有效 IP 的方法。
    *   提醒学员根据具体业务场景选择合适的方案。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **学习目标**：明确列出本章要完成的接口功能。
    *   **章节大纲**：详细列出从“1.1 后台创建用户接口实现”到“1.6 密码重置接口”的所有子章节。
    *   **核心概念说明**：如 Spring Session Redis 的作用、Spring Cache 的核心接口、获取真实 IP 的方法等。

*   **代码关键内容**：

    *   **创建用户接口**：
        ```java
        @Repository
        public interface AuthorityUserRepository extends PagingAndSortingRepository<AuthorityUser, Long>, JpaSpecificationExecutor<AuthorityUser> {
        }
        ```

    *   **用户密码加密处理**：
        ```java
        user.setUserPassword(EncryptUtil.encryptSigned(user.getUserPassword()));
        ```

    *   **获取客户端真实 IP**：
        ```java
        protected static String getClientIP() {
            HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
            // 先从头部获取
        }
        ```

    *   **Spring Session Redis 依赖**：
        ```xml
        <dependency>
            <groupId>org.springframework.session</groupId>
            <artifactId>spring-session-data-redis</artifactId>
        </dependency>
        ```

    *   **登录接口核心逻辑**：
        ```java
        String encryptPassword = EncryptUtil.encryptsigned(password);
        if (!authorityUser.getUserPassword().equals(encryptPassword)) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ACCOUNT_PWD_ERROR);
        }
        authorityUser.setLastLoginTime(new Date());
        authorityUser.setLastLoginIp(clientIp);
        authorityUserRepository.save(authorityUser);
        ```

    *   **保存菜单权限至 Redis**：
        ```java
        List<AuthorityUserRole> roleList = authorityUserRoleRepository.findByUserId(authorityUser.getId());
        if (null == roleList || roleList.size() < 1) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ROLE_NOT_EXIST);
        }
        ```

    *   **Swagger 文档注解**：
        ```java
        @ApiImplicitParams({
            @ApiImplicitParam(value = "股票编号", name = "code", dataType = "string", required = true)
        })
        TradeStock findByCode(@Param("code") String code);
        ```

*   **图表**：
    *   **Redis 数据结构图**：展示 `authority_menu` 键的结构，说明其存储的是菜单权限信息。

---

### 4) 关键场景与演示描述

*   **场景一：创建用户接口实现**
    *   **演示**：讲师在 Typora 中展示 `AuthorityUserRepository` 接口的代码，解释其继承自 `PagingAndSortingRepository` 和 `JpaSpecificationExecutor`，用于支持分页、排序和自定义查询。

*   **场景二：Spring Session Redis 集成**
    *   **演示**：讲师在 PPT 上展示 `pom.xml` 文件，添加 Spring Session Redis 的依赖，并解释其在微服务架构中用于解决会话数据丢失问题。

*   **场景三：获取客户端真实 IP**
    *   **演示**：讲师在 Typora 中展示 `BaseController` 中的 `getClientIP()` 方法代码，解释如何通过 `HttpServletRequest` 获取 IP，并说明处理代理和 VPN 场景的方法。

*   **场景四：登录接口实现**
    *   **演示**：讲师在 Typora 中展示 `AuthorityUserServiceImpl` 中的登录逻辑代码，详细讲解密码加密校验、登录信息记录、菜单权限保存等步骤。

*   **场景五：Redis 数据操作**
    *   **演示**：讲师在 Typora 中展示 Redis 的图形界面，操作 `authority_menu` 键，演示如何将菜单权限信息存储到 Redis 中。

*   **场景六：Swagger 文档注解**
    *   **演示**：讲师在 Typora 中展示 Swagger 注解的代码，解释如何使用 `@ApiImplicitParams` 和 `@ApiImplicitParam` 注解来定义和校验接口参数。

---

以上是根据视频画面截图整理出的结构化信息，希望能帮助您更好地理解这段技术课程的内容。
