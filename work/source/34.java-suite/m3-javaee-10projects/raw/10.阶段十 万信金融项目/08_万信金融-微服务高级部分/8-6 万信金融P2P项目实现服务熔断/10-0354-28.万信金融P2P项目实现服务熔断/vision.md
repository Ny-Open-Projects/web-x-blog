# 画面线理解：28.万信金融P2P项目实现服务熔断

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-6 万信金融P2P项目实现服务熔断
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-6 万信金融P2P项目实现服务熔断\28.万信金融P2P项目实现服务熔断_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 01:27, 01:54, 02:28, 03:02, 03:53, 04:18, 04:55, 05:34, 06:41, 07:31, 08:41, 09:37, 10:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:21:34

1) 这一组画面整体在讲什么（一句话）：
在万信金融P2P项目中，演示如何通过Hystrix为登录功能添加熔断机制，包括引入依赖、配置Apollo、定义Feign客户端和实现Fallback工厂。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT标题页，内容为“4万信金融P2P项目服务熔断”，并说明演示将以登录功能为例。
画面2：在IntelliJ IDEA中展示`pom.xml`文件，其中添加了Hystrix依赖：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
    <version>1.0.2.RELEASE</version>
</dependency>
```
画面3：再次展示PPT中的服务调用流程图，强调登录功能涉及多个服务。
画面4：展示Apollo配置中心的登录页面，地址为`localhost:8070`。
画面5：展示PPT中的操作步骤，包括在`account-service`和`uaa`服务中引入依赖、在Apollo中新建`micro_service.feign-hystrix`命名空间并配置`feign.hystrix.enabled = true`。
画面6：展示PPT中的操作步骤，继续说明在相关服务的`application.yml`中引入命名空间，并修改UAAServer中的Feign代理。
画面7：展示PPT中的服务调用流程图，标注了多个步骤，如“11. 本注册”、“12. 发起注册请求”等。
画面8：在IntelliJ IDEA中展示`AccountApiAgent.java`文件，其中定义了Feign客户端接口。
画面9：展示PPT中的操作步骤，再次强调在`account-service`和`uaa`服务中引入依赖。
画面10：在IntelliJ IDEA中展示`AccountApiAgent.java`文件，光标位于`@FeignClient`注解的`fallbackFactory`属性上。
画面11：展示PPT中的代码，定义了`AccountFallbackFactory`类，实现`FallbackFactory<AccountApiAgent>`接口，并重写了`create`和`login`方法。
画面12：在IntelliJ IDEA中展示`AccountFallbackFactory`类，光标位于`login`方法的`return`语句上。
画面13：在IntelliJ IDEA中展示`AccountFallbackFactory`类，光标位于`return`语句后的`}`。
画面14：展示PPT中的代码，`AccountFallbackFactory`类中`login`方法的实现，包括记录错误原因、降级返回和构造错误响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
    <version>1.0.2.RELEASE</version>
</dependency>
```
画面5：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```
```yaml
feign.hystrix.enabled = true
```
画面6：
```java
@FeignClient(value = "account-service", fallbackFactory = AccountFallbackFactory.class)
```
画面11：
```java
public interface AccountApiAgent {
    @PostMapping(value = "/account/1/accounts/session")
    RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO);
}

@Component
@Slf4j
class AccountFallbackFactory implements FallbackFactory<AccountApiAgent> {
    @Override
    public AccountApiAgent create(Throwable cause) {
        return new AccountApiAgent() {
            @Override
            public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
                //记录错误原因
                log.info("fallback; reason was:", cause);
                //降级返回
                return new RestResponse<>(CommonErrorCode.E_999995.getcode(), CommonErrorCode.E_999995.getDesc());
            }
        };
    }
}
```
画面12：
```java
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    //记录错误原因
    log.info("fallback; reason was:", cause);
    //降级返回
    return new RestResponse<>(CommonErrorCode.E_999995.getcode(), CommonErrorCode.E_999995.getDesc());
}
```
画面13：
```java
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    //记录错误原因
    log.info("fallback; reason was:", cause);
    //降级返回
    return new RestResponse<>(CommonErrorCode.E_999995.getcode(), CommonErrorCode.E_999995.getDesc());
}
```
画面14：
```java
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    //记录错误原因
    log.info("fallback; reason was:", cause);
    //降级返回
    return new RestResponse<>(CommonErrorCode.E_999995.getcode(), CommonErrorCode.E_999995.getDesc());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“4万信金融P2P项目服务熔断”，下方说明“在万信金融P2P项目中，会有很多地方都需要通过Hystrix加入熔断机制，这里只以登录功能为例进行演示。”
画面3：展示服务调用流程图，包含“调用端/App”、“用户中心服务”、“UAA认证服务”、“统一账户”、“验证码服务”五个服务模块，箭头表示调用关系。
画面5：列出操作步骤：
1. 在统一账户(account-service)和UAA微服务中引入依赖
2. 在Apollo的common-template项目中新建micro_service.feign-hystrix名称空间，并增加如下配置：
   feign.hystrix.enabled = true
3. 在Apollo的其他项目中(例如：account-service, uaa...)去关联micro_service.feign-hystrix名称空间
4. 在相关微服务的application.yml中引入micro_service.feign-hystrix名称空间
5. 修改UAA微服务中的Feign代理(AccountApiAgent.java)
画面6：继续列出操作步骤，与画面5相同。
画面7：展示服务调用流程图，包含“调用端/App”、“用户中心服务”、“UAA认证服务”、“统一账户”、“验证码服务”五个服务模块，箭头表示调用关系。
画面9：展示操作步骤，与画面5相同。
画面11：展示代码，定义了`AccountFallbackFactory`类，实现`FallbackFactory<AccountApiAgent>`接口，并重写了`create`和`login`方法。
画面14：展示代码，`AccountFallbackFactory`类中`login`方法的实现，包括记录错误原因、降级返回和构造错误响应。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
