# day02-7-测试统一账户微服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-7-测试统一账户微服务_【海量资源尽在 666java.com】.mp4
- 时长 10分59秒（音频 659s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才咱是不是把统一账户这个微服务工程给创建出来本地的一些配置咱也搞定了阿卜罗上的配置呢咱也搞定了啊大家看一下这是我阿卜罗上统一账户服务里边相关的一些配置我就不再展开让大家看了啊这个过程就是需要大家非常非常细心的一个过程要不然一会就要出错那咱这个最基本的环境全部整完之后是不是也应该向基础
[00:32] 工程一样咱搞一个测试啊是不是写个Controller看看这个刚才这个环境到底能跑起来不能能跑起来了我们接下来是不是才动手去实现注册功能对吧应该是这么一个逻辑或者一个流程那咱看一下吧我们接下来需要写一个Controller然后大家看一下咱consumer当中应该会有一堆这个基础的包吧是不是你看一堆基础的包
[01:02] 咱这个account里边应该还没这一包那这个包一个一个创建似乎有些麻烦咱干脆直接复制过来得了反正它里边基本上也都是空的嘛对进来之后呢你看啊从这儿到这儿control呢你可以先不要一会咱单独创建剩下这些基本上是空包你control stay然后呢去这个什么地方呀account里边直接给它粘过去省了一个一个在那儿创建在这儿对吧粘过来
[01:42] 然后这边我们看一下它应该就能刷出来的是不是刷出来刷出来之后你要注意一个细节这个Swag的这个配置类你还有印象吗咱前面给大家讲过Swag它这里边是不是涉及到一个配置你最好打开看一看有没有哪些地方需要修改的这个报错了就是需要你修改的地方ACCONT对吧包名得换了然后还有哪你过一遍看这里边这些东西都不需要改对不对这儿是不是得需要改一改
[02:15] 咱这就不是用户服务而是什么呀统一账户服务统一账户服务一片这就完事了然后接下来的话咱就做这个环境测试了咱需要建一个包controllerc-o-n-t-r-o-l-l-e-r然后在这里边呢咱就新建一个Controller来进行环境测试那我们起名字就
[02:50] 这样起ACCOU ACC OUNT对吧C-O-N-T-R-O-L-LYeahAucon的consumer不是Aucon的Controller这些的话咱就先删掉吧那既然是Controller咱首先想到是要加一个注解叫rest什么呀对Controller先给它加上加上之后的话咱这里边也就写一个哈喽方法吧跟当时consumer一样
[03:23] public string hello咱就是测环境的啊直接return hello是不是就搞定了对吧咱们前面讲个swag咱顺便把swag相关的注解也往上面加一加吧看大家还有印象没有啊用于这个描述类的是叫什么名字这个注解at应该是什么at api吧是不是这个注解这里边都有哪些属性需要写的
[03:56] 有一个什么呀value它有提示啊value呢一般就是描述整个这个类就是这个control是干嘛的那我们就写一个统一账户服务服务的什么呀API然后其他的其实你写不写都行我们就不写了啊就这一个属性了我们当然是不是还要描述这个方法当然咱这个方法比较简单
[04:24] 没有啥参数是不是没有参数那我们就先加一个描述这个方法了叫at APIoperation对不对就是它那这里边呢你只需要描述一下这个方法的功能就行了那就是测试呗反正就是做测试还需要加什么东西还需要一个东西千万别忘了咱是不是得有一个防路径呀我们就get请求吧这个路径咱就是hello吧
[04:57] 搞定了吧对不对这就是很简单的一个Controller一个方法那整完之后咱接下来就要做测试了我需要开始启动这个微服务了Apollo大家看我是不是已经启动过了那我们既然就是启动微服务启动微服务呢我们首先是不是要启动这个服务注册是不是服务注册有发现先把它给启一下启完之后呢我们要启什么呀启这个启网关网关咱是不是
[05:34] 好点东西没有配置了对吧一会再说吧咱就直接起这个谁啊阿康的啊看到旁边去我看到在这那么这个啊啊康的你在起的时候你要注意了啊不知道大家有没有印象咱当时是把这配启动参数啊哎这个你千万不要忘了啊咱找到找到这个谁啊卡西莫把这个启动参数直接给他复制过去这是咱耳抗他对不对下到这
[06:00] 当然这个端口号可不是53050了前面你可以不用修改但这可不是53050了那这个端口号是多少呢这个端口号不要自己乱写我们在资料文件夹里边大家看有一个pdf文件这里边已经规定好了我们一个微幅的他这个端口号大家要按照这个去设置不能自己随便乱设置统一账号应该是什么53030好这要改成530
[06:31] 30OK然后呢我们就启动这个Arkana这个微服务启动过程当中呢我们看有没有什么问题没有问题的话咱就通过什么呀通过浏览器进行这个访问看咱刚才这个Hello能不能正常访问如果能正常访问的话证明咱整个这个环境这一块就没问题了好现在正在启动我们注意观察一下控制台就行了目前是不是没有报任何错误对吧
[07:09] 应该也启动完毕了我们看它占用的端口号是在哪呢53030没错吧好我们接下来通过浏览器访问一下啊lookhost多少53030是吧斜杠接下来这个访问路径就是ACC OUNT然后再接下来就是什么呀hello敲回声好我们已经正常的
[07:35] 导到了这个响应的这个结果那证明我们目前整个这一套环境是可以正常的干什么呀工作的那有的学员说老师那之前技术工程是不是还要通过网关进行测试对不对那你要想通过网关进行测试大家注意了你这个网关里边还需要做一些修改我们打开这个Gateway这个微服务哪个地方需要做修改这里边吗还是说这里边吗配置类有吗
[08:06] 感觉好像也没有说哪些地方需要修改了对不对你别忘了咱们现在这个微服当中的好多配置都在什么地方Apollo里边对吧那你得去Apollo里边瞅一瞅看有没有什么地方需要改的我们找一下Apollo找到Gateway是吧进来之后呢我们找谁呢你先大概过一遍吧Application这里边你看一下我点击文本你看一下这块你觉得有没有
[08:39] 需要我们增加点东西还是修改点东西呢需不需要需要吧看这儿是不是这都是需要的啊需要的啊如果你不增加相关这个配置的话我们如果通过网关去访问看它那是过不去的啊过不去的所以说我们点击这个修改怎么修改呢你仿照着修改就行了需要这儿你看这儿是不是就是跟consumer相关的那个配置对不对Ctrl CCtrl V
[09:11] 当然这儿你要改成ACC OUNT是吧这儿也得改ACC OUNT这儿也得改咱刚才这个访问路径你看到是不是可看它是不是说这儿也得改成ACC OUNTACC OUNT这个一定要细心整完之后自己要检查检查应该没了吧对吧应该就没了好点击
[09:39] 起交修改还没完还要干什么呀对发布它才能生效好OK了之后呢接下来你这边需要启动这个谁呀启动咱的网关呢对不对把它给启动起来稍等片刻啊启动完之后呢我们就可以通过什么呀网关去访问我们的可看看看看那个哈喽能不能正常的进行访问后边套路都一样啊你每次
[10:08] 新创建一个微服务工程之后都要在Apollo当中进行配置还要在网关里边加入那个基本的配置就是放行就是放行那个配置固定套路了基本上好启动没有报错接下来是这样Ctrl C单独打开一个窗口Ctrl V这要改成530多少啊哎网关那个端口号你要是忘了的话没有关系啊哎这就有对不对或者说你就看这个启动参数里边嘛网关53多少啊
[10:40] 010嘛这就改成53010然后敲回车也没有问题吧对吧好那至此呢咱们关于这个统一账户规服务整个相关的这套环境我们就测试通过

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apollo 配置中心为微服务项目（account-Service 和 gateway-server）配置并管理运行时参数，包括在 IDE 中编写代码、配置文件、启动服务并验证配置生效。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Apollo 配置中心界面，展示 account-Service 项目下多个配置项（如 micro_service.spring-boot-http, micro_service.spring-Eureka 等），当前环境为 DEV。
画面 2: 显示 IntelliJ IDEA 项目结构，选中 consumer-Service 模块，展示其目录结构。
画面 3: 显示 IntelliJ IDEA 项目结构，选中 account-Service 模块，展示其 resources 目录下的配置文件（apollo-env.properties, application.yml, log4j2-dev.xml）。
画面 4: 显示 SwaggerConfiguration.java 代码，其中定义了 Swagger API 文档的配置，包括 title 和 description。
画面 5: 显示 AccountController.java 文件，光标位于 @author 注释行。
画面 6: 显示 AccountController.java 文件，光标位于 @Api 注解行，准备添加或修改注解。
画面 7: 显示 AccountController.java 文件，添加了 @Api 和 @GetMapping 注解，并定义了 hello 方法。
画面 8: 显示 Run/Debug Configurations 界面，配置了 Wanning2pAccountServiceApplication 的启动参数，包括环境变量 -Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=8080。
画面 9: 显示控制台日志，显示服务启动成功，包括 Tomcat 初始化和 Spring Boot 启动信息。
画面 10: 显示浏览器地址栏，输入 localhost:8070 并访问 Apollo 配置中心。
画面 11: 显示浏览器访问 http://localhost:8080/account/hello，页面内容模糊，但可见部分文本。
画面 12: 显示 IntelliJ IDEA 中 gateway-server 项目的 application.yml 配置文件，内容包括 app、apollo、spring 等配置。
画面 13: 显示 Apollo 配置中心界面，展示 gateway-server 项目下的 application 配置项，包括 zuul.routes.* 等配置。
画面 14: 显示 IntelliJ IDEA 中 gateway-server 项目的 application.yml 配置文件，内容与画面 12 相同，但下方显示了控制台日志，包含服务器启动和路由信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 4:
```java
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("cn.itcast.wanning2p"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo buildApiInfo() {
        Contact contact = new Contact(name: "黑马程序员", url: "", email: "");
        return new ApiInfoBuilder()
                .title("万信金融P2P平台-用户服务API文档")
                .description("包含...服务api")
                .contact(contact)
                .version("1.0.0")
                .build();
    }
}
```

画面 5:
```java
package cn.itcast.wanning2p.account.Controller;

/**
 * @author
 * @since 2019/7/20
 */
public class AccountController {

}
```

画面 6:
```java
package cn.itcast.wanning2p.account.Controller;

import io.Swagger.annotations.Api;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "统一账户服务的API")
public class AccountController {

}
```

画面 7:
```java
package cn.itcast.wanning2p.account.Controller;

import io.Swagger.annotations.Api;
import io.Swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "统一账户服务的API")
public class AccountController {

    @ApiOperation("测试")
    @GetMapping("/hello")
    public String hello() {
        return "hello";
    }
}
```

画面 8:
```
Name: Wanning2pAccountServiceApplication
Main class: cn.itcast.wanning2p.account.Wanning2pAccountServiceApplication
Environment: -Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=8080
```

画面 12:
```yaml
app:
  id: gateway-server
apollo:
  bootstrap:
    enabled: true
    namespaces: application,micro_service.spring-boot-http,micro_service.spring-Eureka,micro_service.spring-hystrix,micro_service.spring-ribbon,micro_service.spring-boot-druid
spring:
  application:
    name: gateway-server
logging:
  config: classpath:log4j2-dev.xml
```

画面 13:
| Key | Value | 备注 | 最后修改人 | 最后修改时间 |
| --- | --- | --- | --- | --- |
| zuul.routes.consumer-Service.stripPrefix | false |  | apollo | 2019-07-20 17:28:27 |
| zuul.routes.account-Service.stripPrefix | false |  | apollo | 2019-07-20 17:28:27 |
| zuul.routes.account-Service.path | /account/** |  | apollo | 2019-07-20 17:28:27 |
| zuul.add-host-header | true |  | apollo | 2019-07-20 17:28:27 |
| zuul.ignoredServices | * |  | apollo | 2019-07-20 17:28:27 |

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

