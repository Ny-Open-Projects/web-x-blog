# 画面线理解：day04-22-认证拦截功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day04-22-认证拦截功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:39, 01:53, 03:57, 04:24, 05:52, 06:18, 06:49, 07:39, 08:35, 10:02, 10:38, 12:30, 12:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:56:02

1) 这一组画面整体在讲什么（一句话）：
讲解 Spring Cloud Gateway 网关服务如何实现 OAuth2.0 认证授权拦截，通过自定义过滤器提取并传递用户凭证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“1.4.1 需求分析”章节，说明网关服务需承担将用户登录信息转发给 P2P 认证授权体系、并作为 OAuth2.0 资源服务器角色实现接入权限拦截的职责。
画面2：展示文档“1.4.3 功能实现”章节，说明认证拦截功能由 Spring Security OAuth2 实现，需在过滤器中提取用户信息并转发。
画面3：展示 PPT 图片，图中架构图显示：接入方（WEB、移动端、第三方接入）→ 网关 → 认证服务（UAA）→ 微服务1/2/3/4，标注了网关的路由、权限控制、认证等作用。
画面4：展示 IDE 中 `AuthFilter.java` 文件代码，包含 `filterOrder()` 和 `run()` 方法，用于获取认证信息并处理。
画面5：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `filterType()` 方法，其返回值为 "pre"，表示该过滤器在请求路由前执行。
画面6：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `filterOrder()` 方法，其返回值为 0，表示该过滤器优先级最高。
画面7：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中获取 `Authentication` 对象的逻辑。
画面8：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中判断 `authentication` 是否为 `null` 或 `OAuth2Authentication` 类型的逻辑。
画面9：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中将当前登录用户及客户端信息放入 `Map` 的逻辑。
画面10：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中获取 `HttpServletRequest` 对象的逻辑。
画面11：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中将 `jsonToken` 编码为 `Base64` 并设置到 `request` 的 `queryParam` 中的逻辑。
画面12：展示 PPT 图片，图中架构图与画面3相同，再次强调网关在系统中的核心作用。
画面13：展示 IDE 中 `AuthFilter.java` 文件代码，聚焦于 `run()` 方法中 `if (requestQueryParams == null)` 的判断逻辑。
画面14：展示 PPT 图片，图中架构图与画面3、12相同，再次强调网关在系统中的核心作用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4代码：
```java
public int filterOrder() { return 0; }
@Override
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
    }
    //将当前登录的用户以及接入客户端的信息放入Map中
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Map<String, String> jsonToken = new HashMap<>();
    (oauthAuthentication.getAuthRequest().getRequestParameters());
    RequestContext ctx = RequestContext.getCurrentContext();
    HttpServletRequest request = ctx.getRequest();
    request.getParameterMap(); //关键步骤，一定要get一下，下面行代码才能获得值
    Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
    if (requestQueryParams == null) {
        requestQueryParams = new HashMap<>();
    }
    List<String> arrayList = new ArrayList<>();
    arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
    requestQueryParams.put("jsonToken", arrayList);
    ctx.setRequestQueryParams(requestQueryParams);
}
```

画面5代码：
```java
public String filterType() { return "pre"; } //前置过滤器，可以在请求路由之前调用
```

画面6代码：
```java
public int filterOrder() { return 0; }
```

画面7代码：
```java
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
    }
    //将当前登录的用户以及接入客户端的信息放入Map中
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Map<String, String> jsonToken = new HashMap<>();
    (oauthAuthentication.getAuthRequest().getRequestParameters());
    RequestContext ctx = RequestContext.getCurrentContext();
    HttpServletRequest request = ctx.getRequest();
    request.getParameterMap(); //关键步骤，一定要get一下，下面行代码才能获得值
    Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
    if (requestQueryParams == null) {
        requestQueryParams = new HashMap<>();
    }
    List<String> arrayList = new ArrayList<>();
    arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
    requestQueryParams.put("jsonToken", arrayList);
    ctx.setRequestQueryParams(requestQueryParams);
}
```

画面8代码：
```java
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
    }
    //将当前登录的用户以及接入客户端的信息放入Map中
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Map<String, String> jsonToken = new HashMap<>();
    (oauthAuthentication.getAuthRequest().getRequestParameters());
    RequestContext ctx = RequestContext.getCurrentContext();
    HttpServletRequest request = ctx.getRequest();
    request.getParameterMap(); //关键步骤，一定要get一下，下面行代码才能获得值
    Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
    if (requestQueryParams == null) {
        requestQueryParams = new HashMap<>();
    }
    List<String> arrayList = new ArrayList<>();
    arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
    requestQueryParams.put("jsonToken", arrayList);
    ctx.setRequestQueryParams(requestQueryParams);
}
```

画面9代码：
```java
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
    }
    //将当前登录的用户以及接入客户端的信息放入Map中
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Map<String, String> jsonToken = new HashMap<>();
    (oauthAuthentication.getAuthRequest().getRequestParameters());
    RequestContext ctx = RequestContext.getCurrentContext();
    HttpServletRequest request = ctx.getRequest();
    request.getParameterMap(); //关键步骤，一定要get一下，下面行代码才能获得值
    Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
    if (requestQueryParams == null) {
        requestQueryParams = new HashMap<>();
    }
    List<String> arrayList = new ArrayList<>();
    arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
    requestQueryParams.put("jsonToken", arrayList);
    ctx.setRequestQueryParams(requestQueryParams);
}
```

画面10代码：
```java
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
    }
    //将当前登录的用户以及接入客户端的信息放入Map中
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Authentication userAuthentication = oauthAuthentication.getAuthentication();
    Map<String, String> jsonToken = new HashMap<>();
    (oauthAuthentication.getAuthRequest().getRequestParameters());
    RequestContext ctx = RequestContext.getCurrentContext();
    HttpServletRequest request = ctx.getRequest();
    request.getParameterMap(); //关键步骤，一定要get一下，下面行代码才能获得值
    Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
    if (requestQueryParams == null) {
        requestQueryParams = new HashMap<>();
    }
    List<String> arrayList = new ArrayList<>();
    arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
    requestQueryParams.put("jsonToken", arrayList);
    ctx.setRequestQueryParams(requestQueryParams);
}
```

画面11代码：
```java
public Object run() {
    //获取Spring Security OAuth认证信息对象
    Authentication authentication = SecurityContextHolder.getContext()
            .getAuthentication();
    if (authentication == null || !(authentication instanceof OAuthAuthentication)) {
        return null; //无token则网关内空流，直接返回null
