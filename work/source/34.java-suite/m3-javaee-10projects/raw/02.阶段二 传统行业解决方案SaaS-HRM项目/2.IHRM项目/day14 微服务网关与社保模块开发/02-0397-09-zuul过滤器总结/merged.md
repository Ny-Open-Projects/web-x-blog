# 09-zuul过滤器总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\09-zuul过滤器总结_【海量资源尽在 ubkz.com】.mp4
- 时长 4分35秒（音频 276s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 我们自己定义了一个ZOO里面的过滤器其实还是比较简单的那对于这个过滤器呢它有很多种类型它究竟是怎么执行的在咱们讲义上有一张图形和各位做一个简单的说明好了这个是ZOO官网提供的这么一个请求的一个生命周期的一张图里面清晰的表达了就是ZOO里面的过滤器它的一个职责还有它执行的这么一个顺序
[00:31] 那我们都知道过滤器呢一共有四个PRERoutingPost还有Arrow那我们的一个请求过来之后呢首先进入的就是Port Filter那进入到Port Filter之后那再去执行我们Routing Filter那Routing Filter执行完成之后去调用我们对应的微服务那微服务有对应的返回那接着执行到Post Filter那有的朋友就疑问了不是有四个吗
[00:59] 这边还有一个叫做error没错吧那这个error什么时候生效呢是这样的在我们整个的执行过程当中不管在执行的是filter方法还是我们这边调的是远程微幅当中的方法一旦出现异常它就会立马进入到error filter那error filter代表的是出现异常之后进入到的过滤器那error filter执行完成之后还是要去执行poster
[01:27] filter最终完成我们整个调用过程当然了讲义上也有我们这些文字的一些描述这个我就不再啰嗦了好了当然了在这个ZOO filter里面呢在ZOO网关当中它自己呢也实现了很多filter这边呢咱们讲义上也给各位罗列出来了有兴趣啊咱们可以参照相关资料简单的做些了解其实就可以了那刚才我们说过了这个ZOO
[01:55] 网关涉及到的最核心的第二块功能就是这个过滤器那对于过滤器它究竟可以实现什么样的效果用过滤器究竟能够完成什么样的功能呢简单的说一下其实呢对于使用过滤器啊一般它能做到的事情呢有这么三项首先呢第一项啊第一项借助这个过滤器注意就以这张图我们来做说明借助这个过滤器
[02:25] 那我们在请求的过程当中可能请求的是系统为服务企业为服务或者是员工为服务任一个那这几个里面都有可能会抛出异常那我们是不是就可以借助做网关当中的我们叫做Aero过滤器处理统一处理异常没错了好了这是他可以做的一个事情那除了这个事情之外接下来
[02:55] 那对于我们进行一个请求过来之后呢比如说请求过来进入到网关接着网关调用系统微服务那系统微服务是不是要做出响应得到一些最终的响应数据那这边呢咱们也可以去统计我们请求的这个时间那你请求这个微服务究竟用了多长时间我们是不是可以在这边来进行统计啊我们可以在PoFilter当中记录一下
[03:26] 你开始请求的这个时间那接着在我们这个Post filter当中是不是可以给它记录一下我们结束请求的时间那这样一来是不是就可以统计你一个微服务发送请求它究竟用了多长时间没错了OK那除了这个作用之外呢还有最后一个功能这个功能呢极其普遍叫做什么呢就是健全健全其实就是
[03:56] 校验一下用户的一些权限放到这边那对于这个健全而言呢只要用网关我们一般就把权限校验放到网关层来进行统一处理那注意我们之前是怎么做到的咱们课程介绍的时候说过我们之前是不是每一个都放到了各个的微服务当中这种方式写起来代码太啰嗦并且不好维护那么可以把
[04:25] 校验权益这一块放到网关层来做也可以当然了进入什么来实现的就是它里面的这些过滤器

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解Zuul过滤器的生命周期、执行流程、内置过滤器列表及其使用场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中LoginFilter.java代码，定义了ZuulFilter并重写了filterType()和filter()方法，返回“pre”类型。
画面2：PPT页面标题为“2.1.3 过滤器执行生命周期”，展示Zuul过滤器生命周期图，包含“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”。
画面3：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程。
画面4：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程。
画面5：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面6：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面7：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面8：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面9：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面10：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面11：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面12：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面13：PPT页面展示Zuul过滤器生命周期图，图中“pre filters”、“routing filters”、“post filters”、“error filters”和“Origin Server”构成完整流程，下方文字说明“正常流程”和“异常流程”。
画面14：展示架构图，包含“Vue”、“zull, spring cloud gateway”、“aureka”、“企业微服务”、“员工微服务”、“金税微服务”等节点，以及“API网关权限校验”、“路由”、“负载均衡”等连接关系。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import com.netflix.zuul.exception.ZuulException;
import org.springframework.stereotype.Component;

@Component
public class LoginFilter extends ZuulFilter {

    @Override
    public String filterType() {
        return "pre";
    }

    @Override
    public int filterOrder() {
        return 0;
    }
```

画面2：
```java
@Override
public Object run() throws ZuulException {
    System.out.println("zuul过滤器...");
    return null;
}
```

画面6：
```java
// 所有内置过滤器列表：
[ ZullFilter (com.netflix.zuul)
  SendResponseFilter (org.springframework.cloud.netflix.zuul.filters.post)
  TestZuulFilter in TestUnit in ZuulFilter (com.netflix.zuul)
  TestZuulFilter in TestUnit in ZuulFilter (com.netflix.zuul)
  StaticResponseFilter (com.netflix.zuul.filters)
  SimpleHostRoutingFilter (org.springframework.cloud.netflix.zuul.filters.route)
  SendForwardFilter (org.springframework.cloud.netflix.zuul.filters.route)
  SurgicalDebugFilter (com.netflix.zuul.filters)
  FormBodyWrapperFilter (org.springframework.cloud.netflix.zuul.filters.pre)
  DebugFilter (org.springframework.cloud.netflix.zuul.filters.pre)
  ServletDetectionFilter (org.springframework.cloud.netflix.zuul.filters.pre)
  TestZuulFilter in FilterLoader (com.netflix.zuul)
  Servlet30WrapperFilter (org.springframework.cloud.netflix.zuul.filters.pre)
  LocationRewriteFilter (org.springframework.cloud.netflix.zuul.filters.post)
  PreDecorationFilter (org.springframework.cloud.netflix.zuul.filters.route)
  RibbonRoutingFilter (org.springframework.cloud.netflix.zuul.filters.route)
  SendErrorFilter (org.springframework.cloud.netflix.zuul.filters.post)
  StaticResponseFilter (com.netflix.zuul.filters)
  SurgicalDebugFilter (com.netflix.zuul.filters)
]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：标题“2.1.3 过滤器执行生命周期”，图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面3：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面4：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面5：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面6：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面7：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面8：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面9：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面10：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面11：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面12：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面13：图中“HTTP Request”指向“pre filters”，“pre filters”指向“routing filters”，“routing filters”指向“post filters”，“post filters”指向“error filters”，“error filters”指向“Origin Server”，“Origin Server”指向“HTTP Response”。
画面14：架构图中“Vue”指向“zull, spring cloud gateway”，“zull, spring cloud gateway”指向“aureka”，“aureka”指向“企业微服务

