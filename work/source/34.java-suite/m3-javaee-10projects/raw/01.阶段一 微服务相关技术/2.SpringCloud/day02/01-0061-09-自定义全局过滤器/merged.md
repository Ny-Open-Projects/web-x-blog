# 09-自定义全局过滤器

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\09-自定义全局过滤器_【海量资源尽在 ubkz.com】.mp4
- 时长 7分28秒（音频 448s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 自定义全局过滤器在这一小节中我们的主要目标是定义一个全局过滤器检查请求中是否携带有token参数那具体我们的需求就是编写全局过滤器在过滤器中检查请求地址是否携带token参数如果token参数的值
[00:33] 存在也就是非空的话则放行如果token的参数值为空或者不存在这个token参数则设置返回的状态码为未授权也不再执行下去了其实这个就相当于做了一个权限的鉴定
[01:07] 当如果你带了我们指定的一些参数的话呢就可以正常的去执行请求如果没有带那么就说明没有授权那么就不再执行下去那具体我们的这个做法应该如何做实现的步骤来分析一你要去编写一个全局过滤器之后再去测试就可以了全局过滤器不需要去配置好所以我们现在打开IDA去编写一个全局的过滤器
[01:40] 编写一个类my比如说global filter实现接口global filter然后让我们的这个过滤器呢有先后顺序的话你可以去实现一个再实现一个接口叫older的control o这个是我们的过滤器逻辑的处理方法这个是我们的过滤器执行顺序的一个方法那么它有个这个特点就是值越小
[02:24] 月先执行当如果有多个过滤器的时候这个值呢谁哪一个过滤器的小那么就会先执行OK我们改一个1的来然后在这边的处理逻辑呢我们就是去判断这个参数是否存在包括我们这个过滤器它也是一个组件所以我们加一个component注解加了以后呢在这里面去编写出具体的处理逻辑我们先输出一句话这是一个全局的过滤器my global filter
[03:00] 接着我们再去判断它的请求参数那就是exchange.getRequest.get请求参数中得到一个叫做token而且我们得到是就因为我们token只有一个我们要得到它的值那就直接获取值getFirst就是在这个列表里面去获取第一个值这个参数对应的第一个值那我们现在呢因为一般也只是传一个所以就获取到就可以了获取以后
[03:35] 去判断它是否存在那个ifStringUtilsComments的包isBlain如果是空的话那么我们的处理就是设置一个未授权的状态好就是设置响应状态码为未授权好所以我们来设置Exchange.get响应的respond.
[04:13] set状态他状态码unauthorized再返回一个直接返回不再执行下去了点set complete就已经完成的意思不再执行后面的一些过滤请求如果是正常情况下那我们还是让他继续的往后执行ok所以chain点filter exchange这就是我们那个全局的过滤器
[04:49] 内容已经全部编写完成我们现在马上来进行测试启动启动以后呢我们成功的标准就是当一会我们访问一个路径的时候携带了token跟不携带了token的这个地址呢是不一样的表现的我们现在打开浏览器来去查看验证现在地址呢是没有携带token那按照我们的这个过滤器的作用就是会返回不是正常的一个数据结果也就是被
[05:26] 设置为未授权就是空的了应该打开F12来查看它的一个响应状态码刷新好无法正常运行接下来我们再看它的一个请求好像现在没有列出来我们再来刷一次好就是出现一个响应状态码是401其实这个401呢就已经是我们的叫做未授权其实如果你用我们的一个任何REST CLAN的工具那我这边安装了一个工具REST CLAN
[06:05] 或者是postman这些都可以打开后呢接着我们去输入一个地址这个地址的话呢就是我们刚才这个地址看一下它的一个情况好接着我们执行get方法点击发送它就显示了401就是未授权好所以就是我们当时设置的状态码只是没有任何数据但如果这时候我们去加一个请求地址的话那在这边也行在这边也都一样可以因为我们是正常请求了你加了一个token的话来个token等于abc
[06:36] 回车正常获取到数据那这时候呢我们的状态码就应该是正常的200好再发送这就是加了一个全局过滤器的一个作用那这个工具呢在今天的资料中大家如果要安装的话也可以去安装也就是它你解压以后里面有安装说明文档包括它安装的内容全部在这里边你去安装也行你用postman也是可以的OK这就是我们一个全局过滤器的一个应用我们回到开发工具中
[07:06] 我们把这段记录起来再回到我们的笔记记录这个全局过滤器的使用这是我们的全局过滤器它不需要去配置只要去编写实现这个接口然后再去编写你的过滤逻辑就可以了这是我们自定义全局过滤器的所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud Gateway 中自定义一个全局过滤器，用于检查请求中是否携带 token 参数，若无则返回 401 未授权状态码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“9. 自定义全局过滤器”的目标和需求分析，明确要实现的功能。
画面 2: 在 IDEA 中打开 `MyGlobalFilter.java` 文件，准备编写过滤器代码。
画面 3: 为 `MyGlobalFilter` 类选择实现 `GlobalFilter` 和 `Ordered` 接口。
画面 4: 编写 `MyGlobalFilter` 类的 `filter` 方法，打印日志并获取请求参数。
画面 5: 在 `filter` 方法中添加注释，说明后续要检查 token。
画面 6: 在 `filter` 方法中添加代码，获取请求参数中的 token。
画面 7: 在 `filter` 方法中添加代码，如果 token 为空则设置响应状态码为 401。
画面 8: 在 `filter` 方法中添加代码，设置响应状态码为 401 并完成响应。
画面 9: 在浏览器中访问 `http://127.0.0.1:10010/api/user/8`，页面显示 404 错误。
画面 10: 在浏览器中访问 `http://127.0.0.1:10010/api/user/8`，页面显示 404 错误。
画面 11: 使用 Advanced REST Client 发起 GET 请求到 `http://127.0.0.1:10010/api/user/8`，返回状态码 401 Unauthorized。
画面 12: 展示文件资源管理器中 `day02` 目录下的文件结构。
画面 13: 展示课程文档中“9. 自定义全局过滤器”的目标和需求分析，明确要实现的功能。
画面 14: 展示课程文档中“9. 自定义全局过滤器”的实现步骤，包括编写过滤器和测试。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ithema.gateway.filter;
```

画面 3:
```java
public class MyGlobalFilter implements GlobalFilter, Ordered {
```

画面 4:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        exchange.getRequest().getHeaders().forEach((k, v) -> {
            System.out.println(k + " : " + v);
        });
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
```

画面 5:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        exchange.getRequest().getHeaders().forEach((k, v) -> {
            System.out.println(k + " : " + v);
        });
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 6:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 7:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 8:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

