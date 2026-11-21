# day04-14-认证(登录)功能实现-Feign代理

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-14-认证(登录)功能实现-Feign代理_【海量资源尽在 666java.com】.mp4
- 时长 6分3秒（音频 363s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们已经把UAA服务给集成到咱们P2P项目里边了是不是而且我们也进行了基本的环境的一些搭建和配置最后呢还启动了一下能正常启动没有问题那咱接下来就该动动小手开始实现什么呀认证功能其实就是我们说的什么呀登录功能那大家还记得我们以前说的这个注册登录的这个流程吗
[00:28] 如果你不记得了没有关系我们这不是有这个图吗对不对这个时序图吗有印象吗大家看一下前面咱是不是把这个注册呀等着这一块的功能是不是都已经实现过了对不对那咱接下来就该实现这个登录功能大家看这整体的流程是这样子的当你注册成功之后接下来就该发起一个请求就是前端发起一个登录请求这个请求是直接就到哪来呀到咱的UAA的因为我们刚才说了嘛
[00:57] 这个UA就是作为统一认证中心来存在所以你既然是登录嘛你就提交请求到这儿但是呢我们说了UA呢他是不是在这儿要检验你的账号和密码是否正确对不对所以他需要远程去调用谁啊统一账户中心因为统一账户这边是不是他负责这个用户的什么账号密码这套东西对不对所以你需要发起远程调用到这儿来进行校验校验成功之后
[01:26] 这边会返回一个结果对吧成功之后呢那么UA就要生成什么呀令牌然后返回到前端一面那这就表示什么呀登录成功了那如果这儿校验就没通过他也不会生成令牌对不对那登录就算是什么呀失败所以说这就是整个这个什么呀流程那咱接下来先实现什么功能呢先走哪一步呢对不对我们准备先走这一步就做一个准备工作嘛
[01:57] 因为我们刚才说了UA是不是要远程调用什么啊我可看他远程调用还是通过什么呀飞那咱前面是不是在这个注册那一块是不是就用过一次这个飞发起远程调用了对不对那么具体的调是不是我们主要是写一个代理就行了很简单是不是那咱这呢要把这个准备工作做一做那就是说呢咱需要在UA工厂里面你得分清楚谁调谁啊是UA去调用什么呀
[02:24] 统一账户这边啊所以我们应该在ua 这边这个工程里面哎添加一个什么呀一个代理一个接口啊然后把这个准备工作做一下然后我们再去实现登录功能那咱就找到 uaa 对就是他然后呢他下面应该有一个包叫啊进就是代理的意思嘛对不对然后呢我们在这个包里边呢新建一个接口那我们起一个名字叫啥呢
[02:51] 因为我们是不是要调用那边对吧所以说咱这样起名字ACC OUNT然后就是APIAGENT然后它是一个接口这大家应该还有印象我们只需要定义接口了由框架帮我们生成代理类以及代理对象对不对这个接口这块怎么写对首先你需要在接口上面要加一个注解叫非因什么clant没错
[03:24] 这个注解是用来设置你要远程访问哪个服务对吧我们要访问的服务是不是account对不对ACC OUNT写上他的服务名S E R V I C E对那你光指定访问哪个服务还不够那服务里边controllercontroller里边方法都有很多对不对那我们是不是要具体告诉他那个访问入境这个也是通过一个注解来设置的对不对
[03:51] 那我们这样子吧我们就跟以前一样找到这个我们要访问的这个Controller以及他里面这个方法把那块东西粘过来就行了哎是这个吗对啊大家应该还有印象我们当时在看到当中是不是有这么一个login吗对不对他呢就是实现这个这个登录功能的那我们把这一块呢粘哪一块了其实这一块粘过来我们改造一下就行
[04:24] 我们将来远程调呢就是他嘛所以我把它粘过来改造一下啊这个就不用要哎大家看下是这么写的吗这应该加一个什么呀分号对你可以把它那边的这个方法啊连同这个路径对吧原封不动的给它粘过来基本上不用改了但是有一个细节需要注意有个地方需要改就这这呢你直接写这么路一个路径不像
[04:53] 前面需要把这个微服务的基本访问路径也加上就是AACC OUNT因为这是一个远程调用你需要把这个服务名或者说这个不是服务名应该是这个服务的基本访问路径就是那个context path对不对把这个也给他加上这个才可以这才可以这是我们加上这么一个代理就OK了然后代理类代理对象由Support帮我们搞定就行
[05:23] 另外呢还要注意你一旦使用了飞应啊你一定要检查这个启动类上的不是这个启动类了啊不是这个启动类是咱们UA这个启动类上的有没有加这个注解这个大家应该还有印象吗他是不是扫描咱这个包的对不对扫描到这个接口嘛然后他会帮我们生成对代理类代理对象这是我们做的一个准备工作吧有了这个东西的话将来这步是不是就打通了吗
[05:54] 就是UA远程调什么统一账户这不就打通了那咱后边就该实现什么功能呀对就是登录功能了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Cloud 的 Feign 客户端实现微服务间的远程调用，具体演示了在 UAA 服务中定义接口、在账户服务中实现接口、以及在 UAA 服务中启动 Feign 客户端以调用账户服务的流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了“4. 认证(登录)功能实现”的需求分析流程图，图中包含“网关API”、“用户中心服务”、“OAM认证服务”、“账户服务”等模块，以及它们之间的调用关系，如“网关API”调用“用户中心服务”，“用户中心服务”调用“OAM认证服务”和“账户服务”等。
画面 2: 在 IDEA 中显示了项目结构，选中了“wanningzp-uaa-Service”模块。
画面 3: 在 IDEA 中显示了“wanningzp-uaa-Service”模块的资源目录，其中包含“pom.xml”、“wanningzp-uaa-Service.iml”等文件。
画面 4: 在 IDEA 中右键点击“wanningzp-uaa-Service”模块，弹出菜单，选中“New” -> “Interface”。
画面 5: 在 IDEA 中打开“AccountApiAgent.java”文件，显示了接口定义的初始状态。
画面 6: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于接口定义处。
画面 7: 在 IDEA 中切换到“wanningzp-account-Service”模块，选中“agent”包。
画面 8: 在 IDEA 中显示“AccountController.java”文件，其中包含“register”和“login”两个方法的定义。
画面 9: 在 IDEA 中“AccountController.java”文件中，光标位于“login”方法的注解上。
画面 10: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于“@FeignClient”注解的值上。
画面 11: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于“@PostMapping”注解的值上。
画面 12: 在 IDEA 中显示“Warning2pAccountServiceApplication.java”文件，其中包含“@SpringBootApplication”、“@EnableDiscoveryClient”、“@MapperScan”等注解。
画面 13: 在 IDEA 中显示“UAAService.java”文件，其中包含“@SpringBootApplication”、“@EnableDiscoveryClient”、“@EnableFeignClients(basePackages = “cn.itcast.wanningzp.uaa.agent”)”等注解。
画面 14: 在 IDEA 中“UAAService.java”文件中，光标位于“@EnableFeignClients”注解的值上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7:
```java
package cn.itcast.wanningzp.account;
import org.springframework.cloud.openfeign.FeignClient;
@FeignClient(value = "account-Service")
public interface AccountApiAgent {
}
```

画面 8:
```java
@ApiOperation("用户注册")
@ApiOperation("用户登录")
public RestResponse<AccountDTO> register(@RequestBody AccountRegisteredDTO accountRegisteredDTO) {
    return RestResponse.success(accountService.register(accountRegisteredDTO));
}

@ApiOperation("用户登录")
@ApiOperation("用户登录")
public RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO) {
    return RestResponse.success(accountService.login(accountLoginDTO));
}
```

画面 10:
```java
@FeignClient(value = "account-Service")
```

画面 11:
```java
@PostMapping(value = "/accounts/session")
```

画面 12:
```java
@SpringBootApplication
@EnableDiscoveryClient
@MapperScan("cn.itcast.wanningzp.account.Mapper")
public class Warning2pAccountServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(Warning2pAccountServiceApplication.class, args);
    }
}
```

画面 13:
```java
@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients(basePackages = "cn.itcast.wanningzp.uaa.agent")
public class UAAService {
    public static void main(String[] args) {
        SpringApplication.run(UAAService.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“4. 认证(登录)功能实现”，流程图中“网关API”指向“用户中心服务”，“用户中心服务”指向“OAM认证服务”和“账户服务”，“账户服务”指向“OAM认证服务”，“OAM认证服务”指向“网关API”。

5) 不要评价画面美观，不要输出与课程无关的内容。

