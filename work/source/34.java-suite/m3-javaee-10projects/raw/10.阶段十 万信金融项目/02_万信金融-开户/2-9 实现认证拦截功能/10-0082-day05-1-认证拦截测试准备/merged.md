# day05-1-认证拦截测试准备

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day05-1-认证拦截测试准备_【海量资源尽在 666java.com】.mp4
- 时长 5分43秒（音频 344s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 大家注意一下目前呢咱们这个认证拦截功能呢就已经实现了实现了吧这已经实现了啊你看这里边你像这个接入方的权限拦截啊包括那个令牌的校验这俩功能其实是由框架自动帮我们搞定的你把那一堆那个什么呀配置类粘到你的工程里边就OK了你就不用管那我们其实刚才主要做的事是不是就这个事对吧解析到用户的信息然后转发给什么呀
[00:31] 微服务这块代码是不是主要在这个过滤器里边实现那总之吧目前咱们这个认证拦截功能就已经实现了对应的是不是就是这个图当中的什么呀567是不是这三个路兆那咱接下来跟以前一样我们接下来要进行功能测试那在进行功能测试之前呢我们还要做一个准备工作或者要注意一个细节啊什么细节呢大家看这
[01:02] 看这个地方这个代码咱当时讲的时候说了这儿是不是用来配置接入方它的这个权限的一个一个拦截或者一个校验呢对不对我们说了我们每个这个微服务它的这个请求路径是不是都可以分成这几种这个你应该还有印象吧那么其中这个MY和M大头的这两种请求是不是受保护的对不对是受保护的也就是说呢你必须具备相应的什么呀权限
[01:33] 然后网关才能教研通过然后干什么呀放行是不是所以为了让我们的这个测试效果能够充分的体现出来那你一会儿再用postman进行测试的时候呢要挑这种请求路径带有这种就是MY或者说M的这种请求去进行测试所以这个系列一定要注意那我们这次呢就挑这个M开头M开头M开头的它其实是B端用户无论是要不要挑这个呢
[02:03] 是因为咱表里边现有的这个数据啊它就是B端啊就是这个不是它啊在account里边看这就这个othermean用户啊咱现在登录就是用它登的就是这个1537879911嘛你有印象吗它那是谁啊B端B端而这个这个M开头这个其实就是给谁去用啊B端用户去用啊所以说我们根据咱表里边的数据吧我们挑这个M开头的这种请求进行测试
[02:35] 那咱现有的这个代码里面有没有M打头的这种请求或者这种方法呢那有没有我们得找一找我们得找找谁啊consumer找到他的Controller咱看咱以前写的代码hello hiconsumer就没了对不对那这里边有没有M打头的请求啊没有没有那没有呢咱为了测试咱自己定义一个好吧就为了测试定义一个这个说保护的我们做这么一个准备工作
[03:05] 咱讲义当中其实也提到这个事你看这是吧他说你在consumer工程当中当然你拿着别的工程做测试也是可以的我们这是以consumer为例你找到consumer自己新定义一个受保护的资源方法那其实就是M打头的这里边你啥事都不用做你只需要去接收并这个返回什么呀返回这个网关转发过来的那个数据就行了咱刚才是不是在这个什么呀
[03:38] 过滤器里面是不是做这个事了吗咱在这个过滤器里面是不是把那个用户信息拿到手然后是不是转发给这个微服了对不对那微服务呢这边就可以得到这个什么呀这个信息不是在这得到我们单独要写一个方法就在这在这就可以得到得到完之后你给他解析一下嘛解析一下然后响应一下就行了我们在pulseman里边测试的时候是可以看到这个信息的所以我们接下来的话就在
[04:09] consumer Controller里面呢加这么一个方法这个方法我就不再从头敲了啊因为这个代码非常简单我就直接粘过来粘到下面我们整体看一下啊这个逗号呢你需要处理一下呃这里边你一定要注意这是M大头的这个是受保护的啊如果你的客户端这个或者接入方对不对没有通过校验或者不具备相关的权限的话那会被网关拒绝就这你是测试不通过了那这里边这个代码是干嘛的那给大家说一下
[04:48] 这个JSON token其实就是看图吧就这JSON token呢其实就是网关是不是要给微服务往这边转发请求吗转发请求的时候他会带过来那个用户信息就是刚才咱们在过滤区里边实现的有功能那么这个信息呢其实在这被接收了接收到之后呢我们这块代码是干嘛的呢这块代码实实际上是在进行解码或者在解密都行为啥呢因为你看在这
[05:17] 网关过滤器里边在转发请求的时候是不是进行了编码或者进行了加密嘛对不对所以你这边呢自然要做一个相反的操作就是解码或者叫解密都行然后我们就可以拿到那个原始的那个明文数据了然后进行响应就OK了我这个代码比较简单那这个搞定了之后呢咱接下来是不是就可以通过postman是不是就可以过网关往这发请求了对不对进行测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
            .antMatchers("/consumer/my/**").access("#OAuth2.hasScope('read') and #OAuth2.clientHasRole('ROLE_CONSUMER')")
            .antMatchers("/consumer/m/**").access("#OAuth2.hasScope('read') and #OAuth2.clientHasRole('ROLE_ADMIN')")
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
package cn.itecast.wanxing2p.consumer.Controller;

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
1. 在wanning2p-consumer-Service工程的ConsumerController类中新定义一个受保护的资源方法用来测试：
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
1. 在wanning2p-consumer-Service工程的ConsumerController类中新定义一个受保护的资源方法用来测试：
   @ApiOperation("过网关受保护资源，进行认证拦截测试")
   @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
   @GetMapping(value = "/m/consumers/test")
   public RestResponse testResources(String jsonToken) {
       return RestResponse.success(EncryptUtil.decodeUTF8StringBase

