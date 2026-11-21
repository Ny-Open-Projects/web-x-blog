# 28.万信金融P2P项目实现服务熔断

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-6 万信金融P2P项目实现服务熔断
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-6 万信金融P2P项目实现服务熔断\28.万信金融P2P项目实现服务熔断_【海量资源尽在 666java.com】.mp4
- 时长 10分14秒（音频 614s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好 截止到目前呢我们就把Histrix服务熔断相关的内容呢就全部说完了接下来呢咱回到万信金融P2P项目当中咱这个项目应该也有很多地方都需要通过Histrix加入这个什么呀熔断机制当然呢我在这呢就不再一个一个演示了我只以登录为例给你演示一下啊怎么把这个什么呀对Histrix熔断机制
[00:30] 集成到咱们万信金融P2P项目当中那咱们这个登录功能的话大家看一下都跟哪些微服务有关了这个咱得先清楚是不是登录的话你看这17 18 19 20对不对这块是搞登录的跟谁有关啊跟UA和什么呀统一账户就是ArkCount只跟这两个服务有关我们说登录登录是不是那我们的目标就确定了我们将来要搞配置啊或者要写加了代码啊
[01:00] 是不是就是跟这两个微服务有关系对不对那具体怎么做呢咱看看首先是不是要先引入这个Histrix这个什么呀依赖在什么呀统一账户还有什么UA这两个微服务里边呢把这个Histrix这个依赖呢都要引进来那你自己需要检查检查啊看看咱之前的这个碰文件里边有没有引入这个依赖一个是谁啊一个是Account对不对你检查一下
[01:27] 你看我这是不是引过了啊你的里边有没有你自己要检查这是谁啊UAA里面哎这也引过了这第一步导入依赖第二步是不是就搞一个配置吧咱相关的配置其实就这一个对不对就是启用这个什么呀对Heads Tricks这个熔断功能就行了呃但是呢我们刚才说了在咱们外星金融P2P项目当中是不是应该有很多地方都会用这个
[01:53] 这个熔断对不对那我们最好呢是把这个配置给他放到哪个项目当中啊对放到Apollo的这个Corman template这个项目当中这是一个一个我们的通用配置模板嘛你这边你可以新建一个名称空间吧Fin-什么Hitrix然后把这个配置加上去就行我这边呢都已经操作过了啊咱一起看一个Corman template然后呢你是不是应该点这儿对吧新建一下就这个名字
[02:23] 然后呢把这唯一的一个page放进去就行了加完之后呢你别忘了啊我们的这个谁啊我们其他的这些项目是不是应该去关联这个什么呀对刚才那个名称空间啊比如说在这个account里边你是不是应该点击这个添加然后在这儿是不是要关联关联谁啊对关联我们新建的这个feet-heat tricks这个名称空间啊关联完之后呢你在这儿是不是就有了
[02:54] 对吧啊其他的这个微服务啊或者其他项目里边策划都一样啊我就不再一个一个展示另外还有一个细节需要大家特别特别注意也是大家最容易忘了就Apollo整个这一块全部搞定了之后我们本地微服务的这个配置念当中是不是应该要把这个名称物件给引进来啊给加上去是不是这个很容易忘啊嗯那我们相关的两个微服务啊跟登录相关的一个是UAA对吧我们要加进去
[03:26] 你就继续往后排呗读号诶英文状态下的你说吧嗯然后呢就是这个谁啊还有一个account也是加到最后这步千万不要忘了啊把这个名称中间的名字得加进来那配置这一块是不是全部搞定了对不对那么我们这个熔断相关的配置其实就这一个啊就是一个这就搞完搞完之后我们接下来还差一块东西什么东西是不是要进行这个
[04:03] 服务降级就是降级回退嘛是不是呃那咱看看这个这个图我们当时实验登录功能的时候你看看啊看这个图大家应该还有印象这个登录功能应该是你看前端发请求是不是直接就到哪到ua了是不是然后ua又发请求或者调用这个谁啊调用同一账户就是account那么这个调应该是通过飞啊应该是通过飞那咱可以找一找以前的代码
[04:31] 找找以前的代码UA去调用Account应该有个非印代理是不是有吧你看是不是一个非印代理一个接口吗登录是不是这是传过去的数据封装成这个DTO对象了吗然后这是这个什么呀这是Account那边的这个路径吧防路径你可以去找一找吧找找他的Controller找找他的Controller应该就是这个Controller是不是
[05:05] 他这是什么呀L开头的对不对我可抗此sessionsession我们找一找啊L开头的啊这有注释的用户登录应该就是这个啊抗此session对吧没错吧你看这是不调用业务从实现登录功能哎就是他啊就是他那我们前面讲过这个飞应跟这个谁啊Hitschicks集成的时候啊呃他的这个服务降级是怎么实现的他的服务降级我们看这个讲义吧是不是应该是
[05:35] 在这个飞带的这个地方对不对你看这儿你还应该还有印象吧在这个注解里边是不是要增加一个什么呀对降级回退的一个什么工厂类对不对在这个工厂类当中我们是不是要实现这个fallback factory这个接口然后呢重写它的credit方法在这个credit方法里边我们是不是实现这个什么呀降级回退啊我们这里边就是记录了一个日志然后返回了一个什么呀一个一个提示信息吧
[06:05] 就这么多啊非常简单那咱接下来把这块代码呢给编写一下嗯那应该就是这儿吧是不是这儿应该要加一个属性叫fallback factory但是呢咱这个类什么还没创建啊没创建的话咱就在下边给他创建一下呗嗯class咱跟讲义保持一致讲义里边叫account啊fallback factory因为咱是往account那边发的这个请求
[06:36] 这个类呢不是一般的类他需要实现这个什么呀fallback factory这个接口需要设置这个什么呀这个范形范形呢就是这个什么呀这个接口这咱们在入门案里边讲过啊然后呢咱们把这个相关的注解给他加上咱是不是还要用这个什么呀日志是不是那这个报错是因为咱是不是得重写
[07:05] 这个接口里边的一个方法什么叫create方法你先把它生成出来卡了一下啊然后呢咱先不着急先把这给补充一下对吧然后咱接下来就开始重写这个create方法这边都要写写什么代码写什么代码的话大家应该还有印象我们是不是还是要new一个什么呀这个接口的一个什么呀现在也创建了一个匿名内部类对象对不对
[07:38] 然后还是要在这里边重新login方法只不过这一次呢我们是进行服务降级了并不是真正的实现什么呀登录因为你往这走的话一定是之前发生什么发生熔断了对不对我们把这块代码写一下吧那就是直接就return new是不是还是new这个接口的一个实现类对象小伙号我们是不是可以他可以生成吧我记得acc对我们让他生成一下比较方便那在
[08:12] 这个方法里面是不是具体实现这个什么呀对降级回退啊就是服务降级大家看一下我们就是记录了一下日志这个我要跟讲义保持一致然后呢我们是不是要给前端返回一个提示信息吗对不对那我们往前端返回提示信息大家应该有印象我们整个P2P项目是不是做了一个响应数据的一个封装是不是叫Rest Response对不对那我们直接Nill一下把它返回就得了降级回退嘛
[08:46] 那这里边我们要给他封装什么信息我们得说一说这是跟什么跟登录有关的吧跟登录有关的话我们以前这个错误提醒其实是有一个类对吧封装好的叫Corma error code我们从这里边找一找Corma error code看看找一个合适的我们这里边应该有没有你看这里这一堆容乱相关的我们是不是
[09:16] 我们是OAuth康的统一账户对吧那应该就是选它第二get什么呀有一个code呢是不是还有一个那个什么DESC嘛一个描述信息嘛就这俩getDESC哎这其实就搞定了啊这少一个分号来大家看一下这个降级回退的这一块的这个代码呢咱就编写完了跟那个入门案例是不是差不多对不对
[09:49] 那整体其实整体上来说可以说是两块第一大块呢其实就是主要是搞这个配置我直播咱搞到Apollo里边的相对来说会复杂一些第二大块呢就是你要写写代码就在这个飞行代理这个地方了实现这个什么呀降级回退的逻辑这个代码基本上就编写完了编写完之后咱是不是就可以启动相关的这个微服务来进行这个什么测试了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面5：展示PPT中的操作步骤，包括在`account-Service`和`uaa`服务中引入依赖、在Apollo中新建`micro_service.feign-hystrix`命名空间并配置`feign.hystrix.enabled = true`。
画面6：展示PPT中的操作步骤，继续说明在相关服务的`application.yml`中引入命名空间，并修改UAAServer中的Feign代理。
画面7：展示PPT中的服务调用流程图，标注了多个步骤，如“11. 本注册”、“12. 发起注册请求”等。
画面8：在IntelliJ IDEA中展示`AccountApiAgent.java`文件，其中定义了Feign客户端接口。
画面9：展示PPT中的操作步骤，再次强调在`account-Service`和`uaa`服务中引入依赖。
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
@FeignClient(value = "account-Service", fallbackFactory = AccountFallbackFactory.class)
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
1. 在统一账户(account-Service)和UAA微服务中引入依赖
2. 在Apollo的common-template项目中新建micro_service.feign-hystrix名称空间，并增加如下配置：
   feign.hystrix.enabled = true
3. 在Apollo的其他项目中(例如：account-Service, uaa...)去关联micro_service.feign-hystrix名称空间
4. 在相关微服务的application.yml中引入micro_service.feign-hystrix名称空间
5. 修改UAA微服务中的Feign代理(AccountApiAgent.java)
画面6：继续列出操作步骤，与画面5相同。
画面7：展示服务调用流程图，包含“调用端/App”、“用户中心服务”、“UAA认证服务”、“统一账户”、“验证码服务”五个服务模块，箭头表示调用关系。
画面9：展示操作步骤，与画面5相同。
画面11：展示代码，定义了`AccountFallbackFactory`类，实现`FallbackFactory<AccountApiAgent>`接口，并重写了`create`和`login`方法。
画面14：展示代码，`AccountFallbackFactory`类中`login`方法的实现，包括记录错误原因、降级返回和构造错误响应。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

