# 08-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个通用权限系统的介绍。刚才呢,我们是说了一下它的应用场景,然后这个小节呢,我们来看一下重点代码介绍。前面我们也提到了,咱们对于这个通用权限系统啊,并不是真的带着大家去开发这个服务,对吧,而是直接把这个服务给大家,然后呢,我们在后边的课程当中啊,如果还需要进行这个权限相关的管理,对吧,那么我们就直接使用通用权限系统。

来帮我们进行权限的认证健全就可以了。

所以这块呢,重点还是在使用,就是我们会使用它。

那么对于代码这块呢,咱们就把重点的代码给大家介绍一下。

你知道哪些是我们这个权限,这个重点代码。

然后呢,我们先来看这个网关服务啊,网关服务里面最重要的呢,其实是三个过滤器,分别是什么呢,叫做base filter。

就是这个基础网关过滤器,这其实是一个副类,对吧,然后后边我们这两个过滤器呢,都是继承了这个base filter。

然后在这个基础的网关过滤器里边呢,它其实就是定义了一些公共的方法,然后子类呢,就可以去调用这些方法。

而这个token contact filter呢,它是用来解析我们这个token中的用户信息的。

因为我们这块呢,底层呢,其实是基于我们这个JWT令牌,也就是用户认证通过之后啊,

我们会给它响应回去一个令牌,然后呢,前端呢,每一次在请求的时候呢,都需要带着令牌过来,然后在我们这个过滤器这儿呢,统一去进行解析,校验。

然后教育完了之后呢,我们是不是就能够拿到这个用户相关的信息。

然后呢,再到这个access filter这儿,统一进行什么呢,权限的验证,对吧。

在这儿呢,来进行,说白了就是健全,看看你当前用户有没有相应的权限。

没有权限呢,就直接返回了。

这是关于我们这个网关过滤器。

然后一会儿呢,我们再看,这是我网关服务里面最重要的这三个过滤器。

一会儿呢,我们再来看权限服务里面这些。

好,咱们可以打开代码呢,来简单看一下。

找到我们这个gateway,对吧。

然后呢,这里边有一个filter包,对吧。

这里边呢,对应的就是我们这三个过滤器。

首先呢,我们看base filter,对吧。

base filter呢,这里边。

这个是基础网关过滤器。

那么前面我们也提到啊,咱们这个网关组件呢,底层使用的是zo,zo网关。

所以我们这个过滤器呢,必须要继承这么一个叫做zo filter。

而这个类呢,就不是我们自己写的了。

你看,它是我们这个,是我们导入的这个zo-call这个加包里边所提供的啊。

所以必须要继承它。

所有的过滤器呢,都必须要继承它。

好,然后呢,我们在这里边呢,有一些这个属性,对吧。

当然这些属性呢,是来自于哪呢?

是不是从我们这个配置文件去读取的。

这个是什么,前缀,对吧。

说白了就是,什么样的请求,带有什么样的前缀,会经过我们这个网关这个过滤器来处理。

包括这个什么profiles,它读取的是什么呢?

是这个属性。

当然如果读取不到,它默认就是deevee,也就是开发模式。

还有一个什么route locator,这个是做路由的。

你看这里边,这是一些公共的方法,对吧。

这是路由,然后呢,获得URI。

这个请求对象里面是不是来获得,最终呢,来处理字符串。

然后呢,这是什么呢?

忽略应用级token。

因为有一些这个请求呢,其实是不需要处理的,对吧。

那么有没有token都可以。

包括我们请求的某些资源,对吧。

是不是需要忽略。

因为我们并不是所有请求都需要去进行检查,去校验,对吧。

去查它的token到底正不正确。

比如说我在某一个登录页面上,对吧。

我展示的一个图片。

那么我请求图片这个资源,那其实就应该直接放行,对吧。

你不应该给我校验,也不用去解析token等等这些。

然后呢,这个是什么呢?

通过路由这种方式来忽略什么呢?

应用级的resource,校验。

你看都是什么判断它是否需要进行忽略,对吧。

这个是get token from request的。

你看这个名字也能看出来啊,是不是从我们request的对象里面来获得token。

也就是说前面我介绍的。

我们在前端系统,对吧。

认证通过之后,以后你发每一个请求的时候呢,都需要在请求头里面来把这个token给带过来。

你看我们在这呢,就request的get header,是不是就是从这个请求的头信息里面,对吧。

来获得token。

但是如果获得不到,对吧。

也可以通过什么呢?

get parameter,通过参数这种方式把token带过来。

但是我们还是建议啊,你这个token呢,这个令牌是通过什么呢?

头信息这种方式带过来。

然后这是网关抛异常的时候是不是?

执行这个代码。

其实就是什么呢?

就是不放行。

怎么告诉他不放行啊?

最重要的就是调这句。

就send to response等于false。

其实就是不对其进行路由。

说白了就是不放行。

直接响应回我们这个客户端了。

而响应的内容呢?

我们在这是不是send什么response body,对吧。

设置的就是这个内容。

然后呢,这是error response,对吧。

这个响应错误。

怎么处理啊?

这是咱们这个base filter。

这其实就是一个负过滤器。

然后呢,真正起作用的其实是它这两个子过滤器。

你看我这个负过滤器上面是不是没有加那个component的注解。

也就是说它不会实力化。

它主要是提供这些公共方法。

然后让子类来继承它。

你看我这个子类的话,上面是不是就有component的注解。

这样的话呢,表示我们当前这个过滤器是不是才会真正的去生效,对吧。

真正去处理。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

对吧。

你看它继承了base filter。

然后这里面是不是注入了什么呢?

auth client properties,这个属性对象,对吧。

这里面其实对应的就是我们配置文件的配置项。

是吧。

header name,还有什么,这个public key,对吧。

然后呢,这个是一个工具类。

这个工具类是做什么呢?

就是做我们这个JWT它的解析的,这个工具类。

你看,主要的逻辑呢,

其实是在这个JWT的解析的这个工具类。

在run方法里边,就是我们所有的请求过来,对吧。

必须经过run方法在这儿来进行处理。

具体怎么处理呢?

大概来看一下,是不是先获得这个什么contact对象,

其实是它包装的一个上响文对象,

通过它呢,能获得我们这个http serverlet request,对吧。

request对象。

然后呢,我们先来判断一下什么呢?

当前这次请求是否需要这个忽略token,对吧。

如果反回,如果忽略token,

这就说明这次请求呢,不用处理,对吧。

不用处理,直接return到。

注意,return到表示的就是放行。

return到表示的就是放行。

那后边都不用处理了。

如果不忽略,对吧。

不忽略的话呢,还需要进行解析,解析token。

你看,这不是get token from request的,

是不是获得我们这个token。

然后呢,接下来呢,这个token拿过来之后呢,

需要真正去解析。

这个呢,只是从request里边把它取出来。

真正解析呢,其实是在这个地方。

你看,通过我们这个youtube,对吧。

然后呢,把这个token拿进去。

然后呢,

解析完之后,如果能够解析成功,对吧。

它就会返回user info。

user info里边封装的就是什么呢?

就是我们当前这个什么账号的ID,对吧。

还有这个账号名,然后姓名,单位,

还有这个什么岗位ID等等这些。

是不是就是我们当前登录用户的一系列的个人信息,对吧。

在这儿去解析,通过这个工具类来解析。

解析完了之后呢,还要把它放到什么呢?

放到我们zoo的这个header里边。

把这些信息,

包括它这个什么呢?

账号,对吧。

user ID,还有什么key name,什么这是组织ID,岗位ID等等这些。

放到我们这个zoo网关的这个token里面去。

然后return null。

注意,return null就是放行。

具体怎么放到header里面呢?

你看我们这个add header其实是调用的这个方法,在这儿封装的,对吧。

就是这样。

ctx什么addzoo request header,放到它的token里面去。

这样的话呢,我们在下一个过滤器呢,就可以从这个zoo的这个header里面去,

在这个zoo网关它的请求的投信器里面,把这些数据是不是给它取过来。

然后呢,真正进行健全,

其实是在access filter。

刚才我们说token这边呢,token这个contact filter主要是做这个什么呢?

token解析的,对不对?jwt-token解析。

然后呢,这边呢是真正健全的。你看,全线验证过滤器。

在这个地方,

来验证当前用户是否具有访问权限,对吧。

那么在这儿呢,

统一来进行健全。

那么如果健全通过的话呢,就会return null。

return null其实就是放行了。

如果健全不通过呢,

它就会提示什么呢?权限不足。

这块代码比较多,我们就不再展开去一句一句去解读了。

你只要知道当前这个过滤器,

它起一个什么样的作用就可以了。

当然如果大家对这个代码呢,

比较感兴趣呢,也可以自己来大概读一下。

这是我们这个

网关服务里面最重要的这么三个过滤器。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个名为“品达”的通用权限与认证系统（`pinda-authority`）的源码分析，特别是其网关服务（`pd-gateway`）中的核心过滤器实现。讲师通过 IntelliJ IDEA 开发环境，逐步剖析了 `BaseFilter`、`TokenContextFilter` 和 `AccessFilter` 三个关键过滤器的代码逻辑。课程旨在帮助开发者理解如何在 Spring Cloud Gateway 中实现统一的权限校验、JWT Token 解析与用户信息上下文注入，从而为微服务架构提供安全的访问控制。视频内容结合了代码演示与 PPT 讲解，重点在于过滤器的执行顺序、条件判断、异常处理和上下文信息传递。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开场，展示 IntelliJ IDEA 的项目结构，项目名为 `pinda-authority`，并定位到 `pd-gateway` 模块。
*   **00:00:05 - 00:00:15**：进入 `BaseFilter.java` 文件，讲解其作为基础过滤器的作用，主要负责获取路由信息和判断是否需要跳过权限校验。
*   **00:00:15 - 00:00:30**：继续分析 `BaseFilter`，重点讲解 `isIgnoreResource()` 和 `isIgnoreResourceByRoute()` 方法，用于判断是否忽略资源或路由的权限校验。
*   **00:00:30 - 00:00:45**：讲解 `getTokenFromRequest()` 方法，用于从请求头中提取 JWT Token。
*   **00:00:45 - 00:01:00**：分析 `setFailedRequest()` 方法，用于设置错误响应，包括设置状态码和响应体。
*   **00:01:00 - 00:01:15**：切换到 `TokenContextFilter.java` 文件，讲解其 `filterOrder()` 方法，用于设置过滤器的执行顺序。
*   **00:01:15 - 00:01:30**：讲解 `shouldFilter()` 方法，用于判断该过滤器是否需要执行。
*   **00:01:30 - 00:01:45**：分析 `run()` 方法的核心逻辑，包括获取客户端 IP、判断是否需要跳过过滤器、以及解析 JWT Token。
*   **00:01:45 - 00:02:00**：详细演示 `TokenContextFilter` 中的 Token 解析逻辑，包括对测试环境特殊 Token 的处理。
*   **00:02:00 - 00:02:15**：讲解如何将解析出的用户信息（`JwtUserInfo`）添加到请求上下文（`RequestContext`）的 Header 中。
*   **00:02:15 - 00:02:30**：切换到 `AccessFilter.java` 文件，讲解其作为权限校验过滤器的作用。
*   **00:02:30 - 00:02:45**：分析 `AccessFilter` 中的 `isIgnoreToken()`、`isIgnoreResourceByRoute()` 和 `isIgnoreResource()` 方法，用于判断是否跳过权限校验。
*   **00:02:45 - 00:03:00**：讲解 `AccessFilter` 中的权限校验逻辑，包括获取所有角色、获取当前请求资源、并进行权限匹配。
*   **00:03:00 - 00:03:15**：展示 PPT 页面，介绍该权限系统的组件结构，包括网关服务和权限服务，并说明其在新项目开发中的应用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**：
    *   **章节标题**：`2.1.3 重点代码介绍`。
    *   **网关服务**：
        *   `BaseFilter`: 基础网关过滤器。
        *   `TokenContextFilter`: 解析 token 中的用户信息过滤器。
        *   `AccessFilter`: 权限验证过滤器。
    *   **权限服务**：
        *   `LoginController`: 登录控制器。
        *   `MenuController`: 菜单管理控制器。
        *   `RoleController`: 角色管理控制器。
        *   `ResourceController`: 资源管理控制器。
        *   `UserController`: 用户管理控制器。
        *   `OrgController`: 组织管理控制器。
        *   `StationController`: 岗位管理控制器。
    *   **使用说明**：
        *   `2.1.4 使用说明`。
        *   `2.1.4.1 新项目开发`：强调可以基于该系统快速开发新业务。

*   **代码关键内容**：

    *   **`BaseFilter.java`**:
        ```java
        protected String zullPrefix;
        protected String profiles;
        @Autowired
        protected RouteLocator routeLocator;

        protected boolean isDev() {
            return StrPool.PROD.equalsIgnoreCase(profiles);
        }

        protected Route route() {
            HttpServletRequest request = RequestContext.getCurrentContext().getRequest();
            String requestURI = URL_PATH_HELPER.getPathVariable(request);
            return routeLocator.getMatchingRoute(requestURI);
        }

        protected boolean isIgnoreResource() {
            return IgnoreResourceConfig.isIgnoreResource(getUri());
        }

        protected boolean isIgnoreResourceByRoute() {
            return IgnoreResourceConfig.isIgnoreResourceByRoute(route().getId());
        }

        protected String getTokenFromRequest(String headerName, HttpServletRequest request) {
            String token = request.getHeader(headerName);
            return token;
        }

        protected void setFailedRequest(String body, int code) {
            RequestContext ctx = RequestContext.getCurrentContext();
            ctx.setResponseStatusCode(code);
            ctx.addZuulResponseHeader("Content-Type", "application/json");
            if (ctx.getResponseBody() == null) {
                ctx.setResponseBody(body);
            }
            ctx.sendZuulResponse(false);
        }

        protected void errorResponse(String errMsg, int errCode, int httpStatusCode) {
            R tokenError = R.fail(errCode, errMsg);
            setFailedRequest(tokenError.toString(), httpStatusCode);
        }
        ```

    *   **`TokenContextFilter.java`**:
        ```java
        public int filterOrder() {
            return FilterConstants.PRE_DECORATION_FILTER_ORDER + 1;
        }

        @Override
        public boolean shouldFilter() {
            return true;
        }

        @Override
        public Object run() {
            RequestContext ctx = RequestContext.getCurrentContext();
            HttpServletRequest request = ctx.getRequest();
            String clientIP = ServletUtil.getClientIP(request);
            log.info("clientIP={}", clientIP);

            if (isIgnoreToken()) {
                log.debug("access filter not execute");
                return null;
            }

            // 获取 token，解析，然后将信息放入 header
            String userToken = getTokenFromRequest(authClientProperties.getUser().getHeaderName(), request);
            JwtUserInfo userInfo = null;

            if (isDev() && StrPool.TEST.equalsIgnoreCase(userToken)) {
                userInfo = new JwtUserInfo(userId: 1L, account: "pinda", name: "品达");
            } else if (isIgnoreToken() && userInfo == null) {
                userInfo = jwtTokenClientUtils.getUserInfo(userToken);
            }

            try {
                if (isIgnoreToken() && userInfo == null) {
                    userInfo = jwtTokenClientUtils.getUserInfo(userToken);
                }
            } catch (BizException e) {
                errorResponse(e.getMessage(), e.getCode(), httpStatusCode: 200);
                return null;
            } catch (Exception e) {
                errorResponse(errMsg: "验证 token 出错", R.FAIL_CODE, httpStatusCode: 200);
                return null;
            }

            if (userInfo != null) {
                addHeader(ctx, BaseContextConstants.JWT_KEY_ACCOUNT, userInfo.getAccount());
                addHeader(ctx, BaseContextConstants.JWT_KEY_USER_ID, userInfo.getUserId());
                addHeader(ctx, BaseContextConstants.JWT_KEY_NAME, userInfo.getName());
                addHeader(ctx, BaseContextConstants.JWT_KEY_ORG_ID, userInfo.getOrgId());
                addHeader(ctx, BaseContextConstants.JWT_KEY_INFO_ID, userInfo.getInfoId());
                log.info("userInfo={}", userInfo);
                return null;
            }

            private void addHeader(RequestContext ctx, String name, Object value) {
                if (StringUtils.isEmpty(value)) {
                    return;
                }
                ctx.addZuulResponseHeader(name, value.toString());
            }
        }
        ```

    *   **`AccessFilter.java`**:
        ```java
        if (isIgnoreToken()) {
            log.info("access filter not execute");
            return null;
        }

        if (isIgnoreResourceByRoute()) {
            log.info("access filter not execute by resource route");
            return null;
        }

        if (isIgnoreResource()) {
            log.info("access filter not execute by resource");
            return null;
        }

        HttpServletRequest request = ctx.getRequest();

        List<RoleDTO> allRoles = roleAuthService.getAllRoles();
        Set<Resource>
