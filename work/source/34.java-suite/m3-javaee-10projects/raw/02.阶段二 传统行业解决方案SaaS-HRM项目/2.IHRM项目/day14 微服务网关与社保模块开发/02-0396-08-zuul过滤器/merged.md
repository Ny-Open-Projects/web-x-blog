# 08-zuul过滤器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\08-zuul过滤器_【海量资源尽在 ubkz.com】.mp4
- 时长 12分12秒（音频 733s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们刚才呢一起简单的看过了作为网关这一层来说它的一个配置和使用的方式那其实对于这种API网关来说呢除了能够对请求进行转发之外呢还有一个最大的好处呢就是它可以做全线方面的一个校验那它这个做全线方面的校验呢主要就是借助ZOO网关内部的这一个一个的过滤器来进行实现的
[00:29] 那接下来呢我们共同来学习一下ZOO网关的一个过滤器咱们应该如何去玩那回到我们的讲义简单的来看一下那这个Spring Cloud ZOO呢里面包含了很多的这种过滤器啊当然了这边也说过了ZOO呢它主要就是两个核心功能一个就是路由我们玩过了还有一个就是过滤器那路由呢负责把请求转发到具体的微服务上
[00:56] 而过滤器其实说白了就是对你的请求呢在路由在我们的网关这一层对请求进行干预对请求进行拦截对请求进行校验实现了我们这边的权限的等等的一些功能那对于这个做网关的实现起来或者玩起来呢相对来说比较简单我们可以在我们的代码当中任意去定义一个类那这个类的需要去定义需要去哎
[01:25] 继承它这个顶层负类叫做租filter就可以了那好了我们接下来呢可以一起来玩一下这个租filter看一下它应该怎样去做那回到我们这边的代码当中找到我们的网关层代码好了那接下来呢在这里面的合适的位置我们就可以自己去定义我们自己的一个filter出来好了那在这边呢右键我去OK在这个包啊选中
[01:57] 右键定一个class我把它放到filter这个包下起一个名字呢我们就叫做loginfilter好了那对于这个loginfilter呢点击ok那我们刚才说过了要想玩一个过于要想咱们去玩一个这个过滤器需要一个tense来继承它的副类这个副类呢在里面有就叫做zoofilterok我这个不写了直接拷过来引一下包ok
[02:30] 那注意需要去重写里面的这几个方法或者实现里面这几个方法OK好了这个就是我们自定义过滤器过滤器那对于这个自定义过滤器咱们写好了这个类之后呢立马各位就发现这里面呢有四个方法那这个四个方法呢简单的和各位做一个小小的介绍首先呢第一个方法叫做filter tabOK这个方法呢叫做filter tab
[03:03] 那对于这个方法呢首先呢简单的说一下它有一个返回值是一个死菌类型的类型的叫做返回值那对于这个方法它的主要目的就是用来定义定义过滤器类型的那对于这个ZOO filter当中呢过滤器类型呢一共有四种第一个叫做PRE好了接着第二个呢叫做Routing好了接着第三个POST第四个EROR
[03:32] 那注意这个代表的是啊这个代表的是咱们声明一下我们写的这个过滤器它的类型究竟是什么样子如果你这边返回的比如说来一个字符串PRE那这样一来也就意味着你这个过滤器啊其实是在被路由之前执行那这个看起来或者说起来不太直观什么意思呢如果你的过滤器写的是一个PRE那也就意味着在进行请求转发之前
[04:02] 也就在上面这一层我就去执行里面的具体内容好了这个叫做pro好那这个pro呢简单写一下它指的是在执行我们的路由路由请求之前执行好那接着还有一个叫做routing那这个routing呢就是在在路由请求时调用也就是真正的你发起请求的时候我才会进行调用
[04:35] 接着还有一个PostPost就是在Routing和Error过滤器之后执行这个是一个执行的顺序接着这边还有一个ErrorError指的什么呢就是处理请求出现异常的时候执行其实这个主要是说明一下你这个过滤器要在什么时间节点什么时间范围节点之内执行
[05:08] 那我们想说了,咱们比如说举一个例子,想要去完成一个全线校验的这么一个过滤器,那全线过滤器你觉得是在发送请求之后呢,还是抛出异常之后呢,还是在路由之后呢?
[05:23] 这几个都不是,是不是就是应该在进行请求之前,我们在上方这一层,就让它能够把我们的全线全部都校验清楚啊,所以我们这边用什么,各位应该就知道了,我们用的是Pool。
[05:38] 就可以了OK好了那第一个方法呢我们做了一个介绍那接下来呢继续再来看还有第二个方法第二个方法呢叫做filter order好了这边也写一下那这个filter order它有一个叫做返回值是一个int类型的返回值那对于这个方法究竟是在做什么这边简单的说一下这个是在去定义我们这个过滤器
[06:10] 的优先级好了那这个定义过滤器的优先级这边有一个小小的需要各位注意的事项就是数字越小优先级就越高越小优先级它就越高那这个什么意思啊是这样的是这样的比如说呢我这边可以写一个叫做5好了回到这张图举一个例子是这样的我们的破过滤器呢比如你写了两
[06:43] 这两个过滤器究竟谁先执行谁后执行它有一个执行的顺序也就是执行的优先级你要想让它优先执行那你就需要把这个方法的返回值给它搞的小一点因为我们说过了这边的数字越小是不是优先级越高如果你有俩你又想让我这个login filter先执行是不是这边给它搞的小一点写一个1写一个2另一个大于2是不是就可以了OK好了这个就是
[07:11] 它的一个过滤器的优先级那接下来呢还有一个叫做shoot filter好那这个shoot filter是什么呢这个有一个返回值啊也是通过返回值前来说它是一个补力类型的返回值那这个方法它的主要目的是是这样的就是判断判断过滤器是否需要执行那这边呢如果你返回到
[07:39] 举个例子比如说这边你返回一个Pulse啥意思就是说过滤器不管无论如何其实它都不执行了这个其实就是起到一个控制的作用接着有朋友说了这个Shoot Filter有什么有这个方法有什么用呢咱们可以在里面进行判断比如说这边你想对某些某些请求进行过滤也就是
[08:09] 也就是不执行过滤器我们可以在这边进行判断判断一下当前提供的URL如果这个URL你不想让它执行过滤器那怎么办我们这边是不是给它return一个truereturn一个false代表的就是不执行懂我意思吧OK好了这边我们要做测试的所以我这边写一个true它就会执行我们过滤器了接着还有最后一个最后一个叫做run
[08:37] 那这个run是啥呢注意这个run是我们这个过滤器最最核心的方法run方法run方法它主要目的就是我们过滤器中的过滤器中负责的负责的具体的业务逻辑OK那这样一来呢咱们就已经把这个过滤器呢怎么去玩说清楚了里面有四个方法filter tabfilter order
[09:06] should filter当然还有一个runrun里面主要负责它的核心的一些有逻辑那在我这个案例当中呢我配置的是pull在进行发之前它会执行它会执行那接下来呢这边给了一个order好了这边呢永远返回处是不是代表永远都会执行我们当前这个过滤器的方法好了这边
[09:29] 我们这个过滤器里面的业务逻辑究竟是什么咱们可以一起来试一下啊我就可以system out.print好了我们这边写的画就是执行了执行了login filter的run方法OK那这样一来我们这个过滤器呢就已经给它定义好了那过滤器定义好了之后我们可以重新启动一下我们这个网关微服OK重新启动
[10:06] 好了这边呢让它去重新启动回到我们这边的Postman咱们可以一起来试一下那注意啊现在呢我在这边已经Rio L还在这保留着我一请求会执行到我们的网关那对于我们来说我们自己的在网关当中配这个过滤器这边永远返回的是不是都是触啊所以它永远都会执行里面这个run方法把这句话给我打印出来那回到Postman咱们执行一下来看一下效果来走
[10:36] 好了首先呢这边已经得到了返回结果数据是有的回到我们的控台一起来看一下好像并没有对应的旅居输出啊我们来检查一下当前这个代码OK各位忘了上边呢需要把这个我们创建的这个对象呢需要交给SRN所以component啊加一注解抱歉少了一个注解我这边呢还需要再来重新启动一下
[11:18] 好了这边耐心等待它重新启动成功我们再来发送一个请求好了这边已经启动成功了我们清空一下控制台回到Postman再来发一个请求来走好了各位发现数据已经有了回到我们的控制台一起再来看一下各位来看执行了我们login filter里面的run方法没错了OK所以我想说在做网关当中定义filter很简单随便写一类
[11:53] 继承租filter那里面呢这四个方法我们需要自己override重新写一下好了里面的四个方法filter type它指的是过滤器的这个类型好了接着有一个它的优先级还有一个是否执行过滤器那接着run里面执行的是我们的过滤器的业务逻辑OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何基于Zuul实现统一鉴权，通过自定义ZuulFilter来拦截请求并进行权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- PPT标题：2 基于Zuul的统一鉴权
- 子标题：2.1 Zuul的过滤器
- 代码片段：public abstract ZuulFilter implements IZuulFilter{
  abstract public string filterType();
  abstract public int filterOrder();
  boolean shouldFilter(); // 求自IZuulFilter
  object run() throws ZuulException; // IZuulFilter
}

画面2：
- PPT内容：ZuulFilter是过滤器的顶级类。在这里我们看一下其中定义的4个最重要的方法：
- 代码片段：public abstract ZuulFilter implements IZuulFilter{
  abstract public string filterType();
  abstract public int filterOrder();
  boolean shouldFilter(); // 求自IZuulFilter
  object run() throws ZuulException; // IZuulFilter
}

画面3：
- IDE界面：IntelliJ IDEA
- 项目结构：ihrm_parent > ihrm_gate > src > main > java > com.ihrm.gate > filter > LoginFilter.java
- 代码：package com.ihrm.gate.filter;
public class LoginFilter {

}

画面4：
- IDE界面：IntelliJ IDEA
- 代码：public class LoginFilter extends ZuulFilter {
  /*
  自定义过滤器
  定义过滤器类型
  */
  public String filterType() {
    return "pre";
  }
  @Override
  public int filterOrder() {
    return 0;
  }
  @Override
  public boolean shouldFilter() {
    return false;
  }

画面5：
- PPT内容：架构图
- 图中文字：
  1. 系统需要维护多个url
  2. 路由
  3. 权限校验
  - 网关配置：/sys/user /company/list
  - 服务发现：Eureka
  - 服务地址：
    - ihrm-company 127.0.0.1:9002
    - ihrm-system 127.0.0.1:9001
    - 员工微服务 127.0.0.1:9003
    - 企业微服务 127.0.0.1:9002
    - 业绩微服务 127.0.0.1:9003
  - 过滤器：API网关、权限校验
  - 服务注册与发现：Eureka

画面6：
- IDE界面：IntelliJ IDEA
- 代码：public String filterType() {
  return "pre";
}
@Override
public int filterOrder() {
  return 0;
}
@Override
public boolean shouldFilter() {
  return false;
}
@Override
public Object run() throws ZuulException {
  return null;
}

画面7：
- IDE界面：IntelliJ IDEA
- 代码：public int filterOrder() {
  return 2;
}
@Override
public boolean shouldFilter() {
  return true;
}

画面8：
- IDE界面：IntelliJ IDEA
- 代码：public boolean shouldFilter() {
  return true;
}
@Override
public Object run() throws ZuulException {
  System.out.println("执行了LoginFilter的run方法");
  return null;
}

画面9：
- IDE界面：IntelliJ IDEA
- 控制台日志：
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.a.c.c.[Tomcat].[localhost].[/] : Initializing Spring FrameworkServlet 'dispatcherServlet'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:52.527 INFO 32628 --- [nio-9090-exec-1] o.s.w.s.handler.SimpleUrlHandlerMapping : Mapped URL path [/**] onto handler 'defaultServletHandler'
  2019-08-26 17:26:5

