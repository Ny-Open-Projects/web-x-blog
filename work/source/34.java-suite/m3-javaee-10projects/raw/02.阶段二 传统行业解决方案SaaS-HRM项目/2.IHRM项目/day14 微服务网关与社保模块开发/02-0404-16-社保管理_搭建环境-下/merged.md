# 16-社保管理：搭建环境-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\16-社保管理：搭建环境-下_【海量资源尽在 ubkz.com】.mp4
- 时长 5分27秒（音频 328s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们刚才简单的搭建了一个环境并且写了一个测试的一个control的方法那接下来呢我们就可以把这个工程呢给它启动起来一起来试一下好了这边呢找到我们的启动类ok找到们方法来执行走好了这个启动呢稍微有一点点慢各位耐心等待一下那这边让它启动我呢打开postman和各位简单的看一下
[00:31] 那首先是这样的就是为了让这个测试呢更加完整我首先先去登录接着我再去访问一下当前这个登录用户他的企业这个设置的一些情况好了我们这边先去登录一下127.0.0.1这是我们请求的好了我们可以请求直接就是9090代表的是我们的网关Sys-login是我们的请求的路径
[00:58] 好了那接下来呢请求我们用的是Post的方式那这边呢可以给他提供一些我们请求的数据啊OK改成Jason我们请求数据呢这个比较简单各位应该还记得我们是根据mobilemobile来结合password来完成的password来完成的好了我们这边的mobile呢就是可以随便起了当了我可以从这边呢简单的来看一下好了就是这个138
[01:35] 好了我们的密码抱歉我密码已经有点忘了我这边上面登录一下我们来看一下好了123456没问题123456123456OK那接着我开始登录好了登录成功的这边就有我们对应的token数据那接下来我再去访问一下我们刚刚设置好的这个请求路径Ctrl C这边拿过来Ctrl V注意现在改了我们要去访问
[02:04] 咱们刚刚创建好的这个社保模块里面的这么一个settings路径那我这边就可以杠好了社保模块好了接着杠settings切换过来settings好了那接下来呢咱们现在呢由于没有配置服务网关所以我这边只能请求的是9004刚才设置好了那这边呢给他加一个我们的请求加一个我们对应的应该是一个请求头吧好了请求头呢我们叫做
[02:37] 好了抱歉啊这个有点忘了我们可以从页面这边靠一段请求头呢就是要做also recent好了贴过来好了那接着是bill冒号开头那接来里面的这个数据就是刚刚登录返回的这个dataOK那这样一来咱们已经准备好了那准备好了之后我开始点击send走各位发现现在呢请求
[03:14] 能够得到对应的数据操作成功没有问题但是呢我们这边呢咱们说过了由于有了网关的加入所以我们全部请求的是不是都应该是9090给尼森的没错吧但是网关现在还没有进行配置所以我们需要打开网关把网关和我们这边社保模块这个映射关系给它配置上去OK好了那接下来呢找到我们的网关工程找到网关工程叫做Gate好了接着
[03:45] 做我们最后一个操作找到配置文件好了从这边呢直接来一块哎下来那这边呢我们配置的就是我们的设设保对应的这个模块那么请求的路径中间是以这个匹配的那我们对应的微服务呢刚才咱们也设置过名字啊哎就是这个微服名称好了这个ID呢我也改一下改成跟我们微服名称保持一致OK那这样一来我们网关的配置
[04:24] 也已经改好了改好了之后重新启动一下我们的网关OK耐心等待网关启动成功好了如果网关呢启动成功之后那我们这边呢请求只需要请求9090是不是就可以把我们对应的这些请求转发到我们的社保模块啊好了回来看一下这边呢应该是已经启动成功了那接着我们一起演一下试一下走
[05:00] 好了各位发现这回请求网关还有和我们请求单独为服务就是一样的那这样一来我们整个工程搭建已经搭建好了那我们其实就是创建了一个模块在里面呢添加了箱的配置以及copy过去一大堆我们生成好的代码最终各位千万别忘了由于有了网关的加入我们需要添加网关对于我们社网模块的地址影射

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Postman 调用 Spring Boot 服务的登录接口和获取企业设置接口，并展示相关代码和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA 编辑器中显示 SocialSecurityApplication.java 的 main 方法，其中包含 @Bean 注解定义的 IdWorker、JwtUtils 和 OpenEntityManagerInViewFilter。
画面2：浏览器开发者工具 Network 面板显示登录请求的 Request Payload，包含 mobile 和 password 字段。
画面3：桌面多窗口视图，展示多个开发工具和文档窗口。
画面4：浏览器开发者工具 Network 面板显示登录请求的 Response Headers，状态码为 200。
画面5：Postman 中配置了登录请求的 Body，包含 mobile 和 password 字段。
画面6：IDEA 编辑器中显示 SocialSecurityController.java 的 settings 方法，用于查询企业设置。
画面7：Postman 中登录请求的响应结果，显示错误信息。
画面8：Postman 中准备发送 GET 请求以获取企业设置。
画面9：Postman 中 GET 请求的响应结果，显示成功获取企业设置的 JSON 数据。
画面10：IDEA 编辑器中显示项目结构，包含 SocialSecurityController.java 和 settings/Result 等类。
画面11：IDEA 编辑器中显示 ihm_gate 模块的 application.yml 配置文件，包含多个服务的路径和敏感头配置。
画面12：IDEA 控制台显示 Spring Boot 启动日志，包含 Eureka 服务注册和 Ribbon 负载均衡信息。
画面13：IDEA 控制台显示 Spring Boot 启动日志，包含服务注册成功和 Eureka 服务发现信息。
画面14：IDEA 编辑器中显示 ihm_gate 模块的 application.yml 配置文件，包含 ihm-social-security 服务的路径和敏感头配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public static void main(String[] args) {
    SpringApplication.run(SocialSecurityApplication.class, args);
}
@Bean
public IdWorker idWorker() { return new IdWorker(); }
@Bean
public JwtUtils jwtUtils() { return new JwtUtils(); }
//解决no session
@Bean
public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
```

画面2：
```json
{
  "mobile": "1280000002",
  "password": "123456"
}
```

画面5：
```json
{
  "mobile": "1280000002",
  "password": "123456"
}
```

画面6：
```java
package com.ihrm.social.Controller;
import ...
@RestController("/social/security")
public class SocialSecurityController extends BaseController {
    @Autowired
    private CompanySettingsService companySettingsService;
    /**
     * 查询企业是否设置过社保
     */
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result settings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }
}
```

画面11：
```yaml
uri: http://127.0.0.1:9001 # 时路径对应的实际服务的url路径
serviceId: ihm-company # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
path: /sys/ # 指定请求URL的请求规则
serviceId: ihm-system # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
path: /employee/ # 指定请求URL的请求规则
serviceId: ihm-employee # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
```

画面14：
```yaml
uri: http://127.0.0.1:9001 # 时路径对应的实际服务的url路径
serviceId: ihm-social-security # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

