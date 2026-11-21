# 画面线理解：day05-1-认证拦截测试准备

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day05-1-认证拦截测试准备_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 00:38, 00:50, 01:02, 02:11, 02:46, 02:56, 03:36, 03:43, 03:54, 04:28, 05:04, 05:15, 05:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:56:56

1) 这一组画面整体在讲什么（一句话）：
实现网关服务的认证拦截功能，包括定义受保护资源、配置OAuth2权限控制、以及在Controller中编写测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示AuthFilter.java中提取请求参数的代码，将jsonToken放入requestQueryParams。
画面2：PPT标题为“1.4 认证拦截功能实现”，子标题“1.4.1 需求分析”，说明网关服务现在负责令牌解析和权限拦截。
画面3：PPT内容“1.4.4 功能测试”，展示在ConsumerController中定义受保护资源的测试方法，以及Postman中发送请求的示例。
画面4：展示ResourceServerSecurityConfigurer配置类，定义了不同路径的访问权限，如consumer/my/**需要read和ROLE_CONSUMER，consumer/m/**需要read和ROLE_ADMIN。
画面5：展示SQL查询语句，查询用户表中的用户名和密码。
画面6：展示ConsumerController类中定义的测试方法“测试hello”和“测试hi”。
画面7：展示ConsumerController类中定义的“用户注册”方法，使用@RequestBody接收ConsumerRegisterDTO对象。
画面8：展示ConsumerController类中“用户注册”方法的完整代码。
画面9：展示AuthFilter.java中提取请求参数的代码，将jsonToken放入requestQueryParams。
画面10：PPT内容“1.4.4 功能测试”，展示在ConsumerController中定义受保护资源的测试方法，以及Postman中发送请求的示例。
画面11：展示ConsumerController类中定义的测试方法“测试”。
画面12：展示ConsumerController类中定义的“用户注册”方法，使用@RequestBody接收ConsumerRegisterDTO对象。
画面13：展示AuthFilter.java中提取请求参数的代码，将jsonToken放入requestQueryParams。
画面14：展示ConsumerController类中“用户注册”方法的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
Map<String, String> jsonToken = new HashMap<>();
//将jsonToken写入请求服务的请求中，这样服务端通过
RequestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParametersMap(); //关键步骤，一定要get一下，下面这行代码才能得到值
Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
requestQueryParams.put("jsonToken", arrayList);
ctx.setQueryParams(requestQueryParams);
return null;
```

画面4：
```java
@Override
public void configure(ResourceServerSecurityConfigurer resources)
        throws Exception {
    resources.tokenStore(tokenStore).resourceId(RESOURCE_ID)
            .stateless(true);
    resources.authenticationEntryPoint(point).accessDeniedHandler(handler);
}

@Override
public void configure(HttpSecurity http) throws Exception {
    http.sessionManagement()
            .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
            .and()
            .authorizeRequests()
            .antMatchers("/consumer/").denyAll()
            .antMatchers("/consumer/my/**").access("#oauth2.hasScope('read') and #oauth2.clientHasRole('ROLE_CONSUMER')")
            .antMatchers("/consumer/m/**").access("#oauth2.hasScope('read') and #oauth2.clientHasRole('ROLE_ADMIN')")
            .antMatchers("/consumer/**").permitAll();
}
```

画面5：
```sql
SELECT ID, USERNAME, PASSWORD, MOBILE, GATE, STATUS, DOMAIN
FROM p2p_account;
```

画面6：
```java
package cn.itecast.wanxing2p.consumer.controller;

import cn.itecast.wanxing2p.consumer.api.ConsumerAPI;
import org.springframework.web.bind.annotation.*;

@Controller
@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController implements ConsumerAPI {

    @Autowired
    private ConsumerService consumerService;

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() { return "hello"; }

    @ApiOperation("测试hi")
    @PostMapping(path = "/hi")
    @ApiImplicitParam(name = "姓名", value = "姓名", required = true, dataType = "String")
    public String hi(String name) { return "hi," + name; }
}
```

画面7：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}
```

画面9：
```java
Map<String, String> jsonToken = new HashMap<>();
//将jsonToken写入请求服务的请求中，这样服务端通过
RequestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParametersMap(); //关键步骤，一定要get一下，下面这行代码才能得到值
Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
requestQueryParams.put("jsonToken", arrayList);
ctx.setQueryParams(requestQueryParams);
return null;
```

画面11：
```java
@ApiOperation("测试")
@ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true,
        dataType = "String")
@GetMapping(value = "/m/consumers/test")
public RestResponse testResources(String jsonToken) {
    return RestResponse.success(EncryptUtil.decodeUTF8StringBase64(jsonToken));
}
```

画面12：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}
```

画面13：
```java
Map<String, String> jsonToken = new HashMap<>();
//将jsonToken写入请求服务的请求中，这样服务端通过
RequestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParametersMap(); //关键步骤，一定要get一下，下面这行代码才能得到值
Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
requestQueryParams.put("jsonToken", arrayList);
ctx.setQueryParams(requestQueryParams);
return null;
```

画面14：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
标题：1.4 认证拦截功能实现
子标题：1.4.1 需求分析
内容：
(1) 令牌解析并转发当前登录用户信息给微服务
(2) 作为OAuth2.0的资源服务角色，实现接入方权限拦截

画面3：
标题：1.4.4 功能测试
内容：
1. 在wanning2p-consumer-service工程的ConsumerController类中新定义一个受保护的资源方法用来测试：
   @ApiOperation("过网关受保护资源，进行认证拦截测试")
   @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
   @GetMapping(value = "/m/consumers/test")
   public RestResponse testResources(String jsonToken) {
       return RestResponse.success(EncryptUtil.decodeUTF8StringBase64(jsonToken));
   }
2. 启动相关服务后，在Postman中发起请求：
   GET http://localhost:53010/consumer/m/consumers/test?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

画面10：
标题：1.4.4 功能测试
内容：
1. 在wanning2p-consumer-service工程的ConsumerController类中新定义一个受保护的资源方法用来测试：
   @ApiOperation("过网关受保护资源，进行认证拦截测试")
   @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
   @GetMapping(value = "/m/consumers/test")
   public RestResponse testResources(String jsonToken) {
       return RestResponse.success(EncryptUtil.decodeUTF8StringBase
