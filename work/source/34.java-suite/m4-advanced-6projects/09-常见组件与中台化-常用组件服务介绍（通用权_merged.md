# 09-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个通用权限系统的介绍。

刚才呢,我们是说到这个重点代码,对吧?

那么我们刚才主要看的是这个网关服务里边,这三个主要的过滤器。

那接下来呢,我们来看一下权限服务。

权限服务里边呢,比较重要的呢,就是我们这些控制器。

当然了,为了能够支撑这些控制器呢,后边是不是还有一些这个service,包括我们的DAO等等这些。

好,然后呢,我们现在呢,可以打开权限服务呢,来看一下。

权限服务呢,是在我们这个PDApps,对吧?

然后PDOS,它这儿呢,对应的就是这个,PDOS Server。

然后这里边呢,主要的就是我们这些权限相关的这些controller。

那么你可以看到,我们这个地方呢,其实是分成了这么三个包,对吧?

一个是car,这个是核心包,核心包。

然后呢,在核心包里边呢,主要有这么两个控制器。

一个是org,这个是组织。

然后还有一个station,这个指的是岗位。

因为呢,我们一般这种后台的办公系统呢,它肯定都有相应的这些概念,对吧?

组织,其实对应的就是我们这个组织结构啊,一般就是一个竖形的结构,对吧?

然后呢,还有岗位。

咱们可以来看一下,这个呢,就是对组织来进行什么呢,一些增伤改善操作,对吧?

你看,这是分页查询。

对吧?

这个也是分页查询,只不过就是传的条件不一样。

然后呢,这个是根据ID来查,对吧?

这个是新增组织。

然后呢,这个是更新,对吧?

修改,也就是还有delete,删除。

然后呢,这个是查询它这个组织数,是一个竖形的结构来返回。

然后这个也是查询的。

这个是根据什么呢?

根据条件,对吧?

来查询。

然后还有station,这个就是岗位。

其实也是针对岗位的。

这个是根据这个组织来进行增伤改查。

这些代码呢,我们大概看一下就可以了。

然后在common这个包下边呢,对应的是什么呢?

这个area,这个其实是区域,对吧?

对区域数据,也就是行政区域来进行维护的。

然后还有这个是什么呢?

这是首页,主要是做一些统计性的,统计性的,比方说这个系统访问记录,对吧?

当然这是从我们这个日志记录表里面去查询的。

然后J2CAT这个不用看了,这个是做测试的。

然后这个是统计性的,这个是做测试的。

这是测试我们这个缓存的,实际运行的时候呢,没有什么意义。

然后呢,还有一个login log,这是登录日志,对吧?

登录日志,那么比如说这个是日志的,登录日志的这个查询,对吧?

日志呢,基本上都是查询,还有就是什么呢?

save,新增日志,然后删除日志。

然后这个是操作日志,也就是我们这个系统里边的,这个日志呢,是分成这么两类啊。

一个是登录日志,还有就是系统的这个操作日志。

这是对日志呢,进行增上改查操作。

然后在auth里边呢,就是跟我们这个权限相关的,比如说这个什么呢?

user,这是不是用户的管理,对吧?

对用户数据增上改查。

然后row,这是不是就是角色,角色,这是对角色,应该这是查询,对吧?

然后这个也是查询,是根据ID来查。

然后呢,row authority,这个其实是什么呢?

是针对我们角色的资源,对吧?

其实这相当于是操作的是我们那个角色跟这个资源权限相关的这个,其实是关系表。

然后呢,还有resource,resource对应的就是我们的资源。

然后还有这个menu,menu是不是就是菜单,针对菜单来进行数据维护。

你看这是删除菜单。

还有login,这是不是就是处理我们这个登录的啊,用户登录,对吧?

你看登录的时候调这个方法就可以了。

然后这个是测试的方法。

这个是验证图,

这个是boken的。

然后呢,这个是对我们这个验证码,因为我们页面呢是需要有验证码的。

好,对验证码进行校验的。

好,这个是用来这个生成验证码的。

好,生成验证码。

OK。

简单的,这就是咱们这些control了。

但是下边呢,你看他是不是都调用了相应的service,service在哪呢?

在我们这个BIZ,然后service这里边。

好,你看,都是这样的。

好,这是一个一个的service类。

好。

好。

但这个auth manager呢,

是处理什么呢?

处理我们这个用户的,对吧?

用户权限的。

你像这个什么简单登录,对吧?

简单登录,然后这个普通登录,然后获得token,然后获得用户信息。

好。

OK,这个是教验token,对吧?

OK,那么这就是咱们这个pdauth server,也就是这是我们的权限服务的一些主要的代码。

主要的呢,我们是看的这些控制器,它其实就是对我们权限啊,角色呀,

什么菜单呀,用户啊等等,这些数据来进行维护的。

那么有了这些数据呢,我们是不是就可以在用户登录的时候呢,登录完成之后,我们就知道它的角色了。

因为我们已经维护好了这些数据,对吧?

然后根据角色呢,就能查到它的权限。

等等啊,这些呢,都是对这个角色,就是权限相关数据的一些这个管理维护。

那么是在我们这个权限服务里面来完成。

然后呢,在网关服务里面呢,来实现什么呢?

健全操作。

OK,这是针对我们这个通用权限系统里边一些重点代码。

我们就大概来了解一下。

那么如果大家感兴趣呢,也可以自己来看一下。

包括我们这边是不是还有一些API,对吧?

那么这其实定义的是一些FIN接口,是一些FIN接口。

OK,然后还有就是什么呢?

我们Entity,这是不是就是我们所涉及到的这些什么实体,实体,权限实体。

当然我们也都是按照这个包,你看有Common,有Curl。

还有什么呢?

Auth,给它划分开的。

OK,这是关于我们重点代码,先说到这儿。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于“品达通用权限系统”的技术课程，主要讲解了该系统的核心代码结构和关键功能实现。讲师通过 IntelliJ IDEA 开发环境，逐个展示并讲解了系统中各个控制器（Controller）的代码，包括登录、组织、岗位、角色、资源、日志等模块。视频旨在帮助开发者理解如何在现有项目中集成此权限系统，并通过一个“商品服务”的案例来演示其在新业务开发中的应用。整个讲解过程以代码演示为主，辅以PPT大纲，内容聚焦于后端Java服务端的实现细节。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开场，展示PPT大纲，介绍本节内容为“重点代码介绍”。
*   **00:00:05 - 00:00:15**: 讲师在PPT上列出“网关服务”和“权限服务”的主要组件，包括 `BaseFilter`, `TokenContextFilter`, `AccessFilter` 等过滤器，以及 `LoginController`, `MenuController`, `ResourceController` 等控制器。
*   **00:00:15 - 00:00:30**: 讲师切换到IDEA，展示 `OrgController.java` 文件，讲解“查询组织”功能的实现。
*   **00:00:30 - 00:00:45**: 讲师展示 `StationController.java` 文件，讲解“分页查询岗位”功能的实现。
*   **00:00:45 - 00:01:00**: 讲师展示 `AreaController.java` 文件，讲解“查询区域”功能的实现。
*   **00:01:00 - 00:01:15**: 讲师展示 `DashboardController.java` 文件，讲解“生成ID”和“查询登录日志”功能的实现。
*   **00:01:15 - 00:01:30**: 讲师展示 `LoginController.java` 文件，讲解“新增登录日志”功能的实现。
*   **00:01:30 - 00:01:45**: 讲师展示 `OptLogController.java` 文件，讲解“删除系统日志”功能的实现。
*   **00:01:45 - 00:02:00**: 讲师展示 `RoleAuthorityController.java` 文件，讲解“查询角色关联的菜单和资源”功能的实现。
*   **00:02:00 - 00:02:15**: 讲师展示 `LoginController.java` 文件，讲解“登录”和“验证验证码”功能的实现。
*   **00:02:15 - 00:02:30**: 讲师展示 `LoginController.java` 文件，讲解“验证码”功能的实现。
*   **00:02:30 - 00:02:45**: 讲师展示 `AuthManager.java` 文件，讲解“简单登录”功能的实现。
*   **00:02:45 - 00:03:00**: 讲师展示 `OrgApi.java` 文件，讲解“组织服务”的远程调用接口定义。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “2.1.3 重点代码介绍”。
    *   **网关服务**: `BaseFilter` (基础网关过滤器), `TokenContextFilter` (解析token中的用户信息过滤器), `AccessFilter` (权限验证过滤器)。
    *   **权限服务**: `LoginController` (登录控制器), `MenuController` (菜单管理控制器), `ResourceController` (资源管理控制器), `RoleController` (角色管理控制器), `UserController` (用户管理控制器), `OrgController` (组织管理控制器), `StationController` (岗位管理控制器)。
    *   **2.1.4 使用说明**: “如果是新项目开发，可以在品达通用权限系统的基础上进行相关的业务开发，其实就是将通用权限系统当做开发手架在此基础之上快速开展业务开发。”

*   **代码关键内容**:
    *   **`OrgController.java`**:
        ```java
        @GetMapping("/pageLike")
        public R<Page<Org>> pageLike(String keyword, Long cityId, String latitude, String longitude) {
            // ... 业务逻辑 ...
            return this.success(page);
        }
        ```
    *   **`StationController.java`**:
        ```java
        @GetMapping("/page")
        public R<Page<Station>> page(StationPageDTO data) {
            // ... 业务逻辑 ...
            return success(page);
        }
        ```
    *   **`DashboardController.java`**:
        ```java
        @GetMapping("/generate")
        public R<Long> generate() {
            return success(idGenerate.generate());
        }
        ```
    *   **`LoginController.java`**:
        ```java
        @PostMapping("/login")
        public R<LoginDTO> login(@Validated @RequestBody LoginDTO login) throws BizException {
            // ... 验证验证码、登录逻辑 ...
            return this.success(data);
        }
        ```
    *   **`AuthManager.java`**:
        ```java
        private R<LoginDTO> simpleLogin(String account, String password) {
            // 1. 验证登录
            R<User> result = this.getUser(account, password);
            if (result.getErrorCode() != 0) {
                return R.fail(result.getErrorCode(), result.getMsg());
            }
            // 2. 获取用户信息
            User user = result.getData();
            // 3. 生成token
            Token token = this.getToken(user);
            // 4. 获取资源列表和权限列表
            List<Resource> resourceList = this.resourceService.findVisibleResource(Resource.class, user);
            List<String> permissionsList = resourceList.stream().filter(item -> item != null).map(item -> item.getPermission()).collect(Collectors.toList());
            // 5. 返回登录结果
            return R.success(LoginDTO.builder().user(this.dozer.map(user, UserDTO.class)).permissions(permissionsList).build());
        }
        ```
    *   **`OrgApi.java`**:
        ```java
        @FeignClient(name = "${pinda.feign.authority-server:pd-auth-server}", fallback = OrgApiFallback.class)
        public interface OrgApi {
            @GetMapping("/get/{id}")
            R<Org> get(@PathVariable Long id);
            @GetMapping("/page")
            R<Page<Org>> page(@RequestParam Map<String, Object> params);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：系统架构总览 (00:00:00)**
    *   讲师首先在PPT上展示课程大纲，明确本节将讲解“重点代码介绍”，并列出“网关服务”和“权限服务”两大模块及其包含的控制器，为后续代码演示做铺垫。

*   **场景二：组织管理功能演示 (00:00:15)**
    *   讲师在IDEA中打开 `OrgController.java` 文件，高亮显示 `@GetMapping("/pageLike")` 方法，演示如何通过 `keyword`, `cityId`, `latitude`, `longitude` 等参数进行模糊查询和分页，最终调用 `orgService.pageLike` 方法获取数据并返回。

*   **场景三：岗位管理功能演示 (00:00:30)**
    *   讲师切换到 `StationController.java` 文件，高亮显示 `@GetMapping("/page")` 方法，演示如何通过 `StationPageDTO` 对象接收分页和查询条件，调用 `stationService.findStationPage` 方法进行数据查询和转换，最终返回分页结果。

*   **场景四：登录功能演示 (00:02:00)**
    *   讲师在 `LoginController.java` 文件中，演示了“登录”接口的完整流程。首先验证用户输入的验证码，然后调用 `authManager.login` 方法进行登录，如果成功则返回 `LoginDTO` 对象，包含用户信息和权限列表。

*   **场景五：权限管理核心逻辑演示 (00:02:30)**
    *   讲师展示 `AuthManager.java` 文件，重点演示 `simpleLogin` 方法。该方法首先通过 `getUser` 方法验证用户凭证，然后调用 `getToken` 方法生成用户令牌，接着通过 `resourceService.findVisibleResource` 方法获取用户可访问的资源列表，并将其转换为权限字符串列表，最终返回包含用户信息和权限列表的 `LoginDTO` 对象。

*   **场景六：服务接口定义 (00:02:45)**
    *   讲师展示 `OrgApi.java` 文件，演示了如何使用 Feign 客户端定义一个远程调用接口。该接口通过 `@FeignClient` 注
