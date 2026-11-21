# 2.13 网关鉴权拦截

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.13 网关鉴权拦截_【海量资源尽在 666java.com】.mp4
- 时长 12分24秒（音频 744s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面呢我们来看一看我们的网关服务它是如何做API健全的那首先呢我们需要明白API健全是什么意思那么我们所有的前端服务都通过API网关来访问我们后台的服务那么每一次请求因为一个应用的话它可能包含很多很多的API那么如果每一次请求我都需要做一个数据库的一个验证验证你的带着你的用户名密码
[00:28] 这种情况其实是不可取的对吧那我们在现实生活中是如何来做的呢举个例子我们在现实生活中去一个大厦而这个大厦里边有很多的房间那么我们需要做的是什么我们需要做的是在它的保安处或者说在它某一个门卫那个地方然后呢我登记一下
[00:47] 登记我的身份证登记我的姓名然后留下我的电话这个时候保安会给我一个临时的公牌这个临时的公牌我就能进去了我拿到我的临时公牌就能进到各个房间里面去了那在这种情况下其实和我们API的一个健全方式是比较类似的那么某一个应用它在调用我们后台请求的时候最开始它其实是并没有权限的
[01:14] 所以我们开始的时候需要给他做一下用户名密码的一个认证那你认证用户名密码成功之后我们的服务会给他一个token而这个token就和我们刚才举的例子中的这个公牌比较类似那前端的应用他拿着这个公牌也就是说拿着这个token到了我们的每一个门每个门其实都有一些这个人或者说某一个机器来验证你的公牌是不是准确的那么
[01:42] 如果是正确的情况下那我允许你进去不正确的情况下那你对不起你就进不去了那么这个情况其实就是我们在API层面做认证做网关的做网关认证的或者网关健全的一个主要的一个机制因为如果我们在每一个门每一个房间的地方做一个验证那么所有的房间里边房间门口都需要加一个保安或者是都加一个
[02:11] 装置来验证你的用户名和密码对吧所以我们在统一的一个地方这就是在我们的网关层来做的一个验证那么我们来看一看我们如何来开发我们的这个API健全的这个问题那我们原来的代码里边其实已经有了我们的这个网关那么网关层呢它现在只是一个普通的一个Splitboard的应用那下一步的话我要添加一些我们的一些类
[02:40] 而这个类呢我们可以先添加一个什么先添加一个包我们package的话我们叫comment或者util都可以那我需要添加几个类我需要添加两个类第一个类的话我们要添加一个config也就是说是getaway的一个config这样的一个java的一个类这个java类的主要作用呢我们是让我们的整个的
[03:10] 工程变成一个或者这个类变成实际上是一个config configuration这样的一个注解我要添加这个注解这个注解里边我要在我们的Spring Boot刚启动的时候我要执行一个bin而这个bin就是我的一个过滤区这个过滤区我需要开发一个过滤区的一个程序一个Java的Java的过滤器叫tokenfiltertokenfilter这个过滤区这个过滤区的作用
[03:40] 就是来检查我们的token记不记得我们在用户服务里边我们用户服务新创建的时候或者说登录的时候我们会给他创建了我们用户的一个token就在这我们在登录接口里边如果是用户名密码正确的时候我们会给他新生成的一个token而这个token呢我们现在是保存在数据库里边那么我们在我们的网关层面
[04:09] 就需要对这个token做一下验证那这个token的话是一个filter这个类似的filterfilter的话它要实现一些接口这些接口比如说这样叫global filter另外一个就是叫order的这两个接口那么实现这两个接口主要是实现两个接口的一个方法一个叫filter方法一个叫getorder方法那么我们点开generator然后override
[04:40] 一个呢叫做filter方法一个叫做getter方法OK我们在filter方法里边我们getter这个order方法里边我们可以给它设置成我们一个比如说直接返回100这是错误的一个代码我们认为它返回的是错误的那么我们主要是在我们的这个我们的filter里边就开发我们的代码
[05:09] 那么Fiat里边我们开发代码是这样的一个过程那么我首先呢我要判断你的token如果你的token的请求的地址是什么呢是我们的这个login的因为你不可能把所有的接口全部都过滤掉如果全部都过滤掉至少有一个接口是有问题的就是我们的登录接口登录接口此时它没有任何权限了所以在这个时候我们不需要来给它做验证我们需要把我们的
[05:40] 这个登录接口给它过滤掉也就是说如果我的exchange我们要获取我们的request然后得到我们的pass如果这个pass的什么呢pass的value如果等于等于我们的登录接口而这个登录接口是什么code斜杠sys斜杠u字斜杠login也就是说
[06:11] 如果它不等于的时候我们要对它进行一个验证token而这个token我们是前台是放到我们的header里边所以说我们在我们的后台里边我们要拿到我们token就是从header里边来拿这个header里边怎么拿呢exchange的getter request然后从这里边我们要获得header那么header里边我们要获取我们第一个header的
[06:42] 这个是我们从后台拿从前端提交过来请求里边拿到的hider我们下一步的话我们就把我们的这个token做一下验证如果这个token呢等于空或者是或者是什么呢或者我们的token等于那对吧等于空等于那这些其实都是复辈于一起的it's empty
[07:18] 那么如果这样的时候我们可以输出一个什么token为空那么如果是我们的token我们request response我们直接把它设置status code等于http status的anost那么我们认为如果他没有拿到一个token
[07:59] 我们认为他是an aus的否则情况下我们要给他返回response.set completeOK也就是说如果你的token是错误的你的token是没有拿得过来token的时候我们这个时候就让你直接返回了返回错误的那么此时我们要return一个什么呢return一个filterfilter就是exchange这是我们
[08:32] 添加了我们的一个圈子添加了我们的一个配置而这个这个配置的话是此为人呃改的为的一个配置这个配置我们实际上是要添加一个病这个里边的话就是我们的一个token filtertoken filter的在这里边我们要返回newtoken filterok也就是说我们在我们的容器启动的时候我们就把token filter给他添加进去那么
[09:03] 所有的服务通过了网关的所有的服务其实都会验证你是否带了一个token那么在这个地方其实是并不完全的我们现在只是验证了是否唯控那其实还应该验证什么呢我们还需要验证什么呢还需要验证这个token是否在我们的mycego数据库里面因为我们把token存在mycego数据库里面了对不对
[09:41] 我们现在只是验证了是否围空所以我们在这个地方可以再开发额外的一个代码就是我们要验证它是否在我们MySQL数据库里面存储的那么更复杂的一个一些操作包括什么呢我们还可以验证这个时间上是否过期了或者我们把它这个token放到redis里边那么redis设置过期时间这些都是额外的一些我们正常的要开发的一个功能
[10:12] 但是在我们现在的这个程序里边我们只是给大家演示了一下我们如何来在我们的网关层做一些做一些服务的一个验证OK那么我们来开发完了之后下面的话我们就把我们的这个网关给它重启一下那么重启一下之后因为我们前面的所有的这个请求那么请求的时候我们到了我们8080这个这个地方
[10:40] 我们到8080的时候呢我们其实调用请求的原来时候调用请求的时候它是会返回正常的一个返回结果的那么我们现在点击再调用一次那它应该是给我返回一个是错误的对了对吧那此时它给我返回的token为空后台里边返回是token为空的那我们就在前台它就拿不到我们的这个数据了这是我们在网关层做了一个
[11:10] token的一个验证的工作但是这个验证工作现在只是验证了一部分我们只是验证是否为空的我们还需要来开发验证是否在mycircle里面那么验证是否在mycircle里面比较简单我们直接查询mycircle我们需要在我们的hider里面添加我们的token那么这个token的值呢我们随便输入一个因为我们没做这个准确性验证我们只是做有无的一个验证对吧那么我们再点击一下我们看一看这个返回结果
[11:39] OK此时就返回就成功了对吧如果我没有这个token的时候他给我返回的是唯空的那么如果我加了这个token之后他就给我返回正确的一个结果了那么我们实现了我们在我们的网关层面对于token的一个验证而这个Header是怎么怎么添加呢这个Header的话如果是前台的话前台的开发人员前端开发人员会把我们的token的值放到了我们的Header里边去
[12:08] 放到我们的cookie里面去那么cookie下一次每次调用请求的时候他都把我当前的那个token发送给我们后台这是我们针对于网关层做验证的给大家做的一个讲解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Cloud Gateway 中实现一个全局过滤器（TokenFilter），用于拦截并验证用户登录请求。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程目录结构，当前位于“6.2 常用API网关”章节，右侧是API网关技术选型图，包含 Nginx、Zuul/Zuul2、Spring Cloud Gateway 和 Kong。
画面2: 展示项目结构，选中了 GatewayApplication.java，这是网关服务的主类。
画面3: 在项目中右键点击，准备新建一个类文件。
画面4: 新建并选中 TokenFilter.java 文件，准备编写过滤器代码。
画面5: 在 TokenFilter.java 中编写实现 GlobalFilter 和 Ordered 接口的类骨架。
画面6: 在 TokenFilter.java 中编写 filter 方法，准备处理请求。
画面7: 在 TokenFilter.java 中编写获取请求路径和 token 的逻辑。
画面8: 在 TokenFilter.java 中使用 exchange.getRequest().getHeaders() 获取请求头。
画面9: 在 TokenFilter.java 中使用 exchange.getRequest().getHeaders().getFirst("token") 获取 token。
画面10: 在 TokenFilter.java 中编写 GatewayConfig 类的骨架。
画面11: 在 TokenFilter.java 中编写判断路径和 token 的逻辑，并设置响应状态码。
画面12: 在 TokenFilter.java 中编写设置响应状态码和返回链的逻辑。
画面13: 在终端中启动网关服务，同时显示 Postman 和 Typora 等工具窗口。
画面14: 在 TokenFilter.java 中编写完整的过滤器逻辑，包括获取 token、判断路径、设置响应状态码和返回链。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.ithema.cold_gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }
}
```

画面4:
```java
package com.ithema.cold_gateway.common;

import org.springframework.cloud.gateway.filter.GlobalFilter;

public class TokenFilter implements GlobalFilter {
}
```

画面5:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面6:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面7:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        if (!exchange.getRequest().getURI().getPath().equals("/tools/user/login")) {
            String token = exchange.getRequest().getHeaders().getFirst("token");
            if (token == null || token.isEmpty()) {
                System.out.println("token为空");
                exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
                return exchange.getResponse().setComplete();
            }
        }
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面11:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        if (!exchange.getRequest().getURI().getPath().equals("/tools/user/login")) {
            String token = exchange.getRequest().getHeaders().getFirst("token");
            if (token == null || token.isEmpty()) {
                System.out.println("token为空");
                exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
                return exchange.getResponse().setComplete();
            }
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: PPT标题为“6.2 常用API网关”，架构图中“API网关”指向“Nginx”、“Zuul/Zuul2”、“Spring Cloud Gateway”和“Kong”。

5) 不要评价画面美观，不要输出与课程无关的内容。

