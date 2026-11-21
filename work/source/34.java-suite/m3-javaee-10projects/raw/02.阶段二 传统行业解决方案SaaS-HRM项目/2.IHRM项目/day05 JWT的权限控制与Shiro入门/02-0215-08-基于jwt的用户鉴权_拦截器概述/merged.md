# 08-基于jwt的用户鉴权：拦截器概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\08-基于jwt的用户鉴权：拦截器概述_【海量资源尽在 ubkz.com】.mp4
- 时长 9分12秒（音频 552s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] OK好了我们看过了服务状态的这些内容那接下来就是我们用无状态服务模式去完成我们的权限API的一个管理好了呢对于这种无状态呢我们其实是基于JWT的方式完成API的一个健全的一个操作那对于这个JWT的API健全呢怎么去做呢其实很简单我们之前呢昨天写过一部分的代码
[00:29] 那这部分的代码在哪呢就是我们获取用户信息的这个代码那我们找到获取用户信息profile方法找到profile方法抱歉在我们的user Controller当中有一个profile那在这个profile方法里面呢首先呢咱们在讲健全之前啊先去声明这么一个问题是这样的就是说呢咱们这里面要想获取用户的信息的话那太麻烦了
[01:00] 你会发现我写的这个代码有一大串有一大堆都是去获取到请求头assistation然后呢从头里面获取到我们的bier获取到我们的token接着再从里面获取我们到我们存储的数据那这个太麻烦了那么应该如何去判断或者如何去做就能够统一的对所有的方法或者对你指定的一些方法进行统一的获取
[01:24] 并且除了统一获取内容之外我们还可以在访问这些所有的控制器方法之前所有的我们的接口之前是不是都可以统一的对你这个权限进行控制那我们用什么手段去做那这边我们可以借助Spring MVC提供的叫做拦截器的方式我们可以通过它的拦截器对我们的Token进行验证可以从我们的Token伺服券当中提取出内容
[01:51] 这是第一个第二个那在我们的拦截器当中统一的对你要查询的我们的API方法进行全线上面的一个教演那这个思路和各位做过一个说明所以接下来我们就是说怎么去使用拦截器对获取到我们的token数据对token进行解析以及怎么在拦截器当中我们完成我们token完成我们API的全线鉴定那首先呢
[02:20] 第一个就是跟各位来聊一下聊一下死不认拦截器究竟是什么那其实对于死不认拦截器而言这个玩意儿呢各位应该都不陌生也比较简单那这个拦截器呢它其实是一个就是Handle InterceptorDoppel的这个一个它有这么一个适配器那我们只需要去写一些代码去适配它其实就可以了那么要自己去写一个拦截器那如何去做呢各位
[02:47] 我们只需要在一个合适的位置去写自己的一个拦截器去实现错了去继承一个叫做HandlerInterceptorAdapter去继承它那我们就能去实现那继承了之后这个我们自定义拦截器当中会有三个方法这三个方法一个叫做PoreHandler好了那第二个方法叫做PostHandler还有一个叫做AfterCompilation那PoreHandler指的是你在进入到真正的你的API接口之前要做的事情
[03:18] 就是在进入API接口之前要干什么事那第二个呢是在Post HandlerPost Handler是执行了API方法之后要干的事那第三个就是After CompilationAfter Compilation一般指的是所有的请求都结束之后他做的事情好了一共有这么三个方法那我们接下来呢就可以自己去定一个拦截器自己去定一个拦截器那我们先来看一下在拦截器当中如何去对我们的用户信息做识别
[03:49] 好了那这边呢我去打开我的idea这些所有的内容呢就都关掉了好了那接下来那这个拦截器呢是要做用户健全并且要做到用户数据的应该是一个公共的一个拦截器所以这个呢我就写到common包下了那在我的common包下呢找一个合适的位置比如说呢我就在common下创建一个我自己的拦截器好了我把它放到enterceptorinterceptor
[04:20] 这个保持下我叫做 JWT InterceptorOK好了那这个是我们自定义的拦截器那自定义拦截器如何去做呢其实很简单它只需要我们继承一个副类Etense 继承一个副类那这个副类呢叫做什么呢叫做 Handler InterceptorHandler Interceptor
[04:54] adapter即可那是继承它的之后呢我们可以实现它们当中的一些方法OK实现方法呢可以实现它的pro handler方法post handler方法以及after compilationOK那这些方法呢都有什么作用咱们简单的提一下pro handler它是指进入到我们的控制器方法之前执行的内容
[05:32] 那也就是说你想进入到某一个API接口是不是先进入到我这个PostHandler那这是第一个第二个还有PostHandler那PostHandler是执行了我们的控制器方法之后执行的内容那对于这块啥意思呢就是说当你去执行了你的API接口开始返回那这个时候是不是要经过我们的PostHandler那还有一个叫做AfterCompletionAfterCompletion指的是我们响应结束
[06:02] 之前执行的我们叫做那种也就是说呢执行了破执行了post handle开始执行响应了那执行响应之前你比如说可以完成一些操作那当然了后面两个我们基本上用的比较少那但是执行这两个呢它有一个前提条件就是这个破handle必须有返回值那这破handle呢它执行的返回值是一个补利类型的那补利类型返回值触代表什么意思因为这破handle呢有对我们的一个
[06:31] 进入到控制器方法之前执行它有一个拦截的一个作用那触指的是可以继续执行执行我们的控制器方法好了还有一个False那False就是拦截了就是你不能再继续往下走了那这就是它的一些特点好了那这个我们看过了之后底下这两个方法我们就不用了我们只用Pull Handler在Pull Handler里面我们想方设法的去完成如下的这么几个操作
[07:04] 第一个操作我们想方设法的通过拦截器获取到我们的token数据因为我们刚才说过了我们写拦截器的主要目的呢一共就两个那在拦截器里面第一件事由于我们刚才以一个profile方法举例说明了一个事就是说如果你要从token里面获取数据的话
[07:31] 你这个代码写起来真的是有点太啰嗦或者有一点点太麻烦了我们再来看一下你发现他要解析他要获取to request那获取了request之后呢从request当中获取我们的我们的认证数据投信息拿到之后呢去进行判断去进行比较还有从里面获取到ID等等一系列操作这个有点麻烦那怎么去做更加方便那我们是不是可以再进入到我们的控制方法之日
[08:01] 当前之前我们在Interceptor里面就给你解析好你直接底下就可以用那这种方式是不是更简单呀所以第一种方式第一个我们在拦截器里面要做的事情就是做什么呢就是简化我们的获取Token数据的代码边线当然了在这个里面呢我们可以完成统一的用户权限交易当然了这个用户权限交易就是是否登录了
[08:35] 好了那接着第二件事我们就要在这个拦截器里面进行判断因为它有这么一个特性它有这么一个特性是因为它呢可以获取到你要执行的API接口的方法那我们别忘了还有一个就是说你这个用户访问的时候你有没有访问这个接口的一个权限是不是没错吧所以我们要做的第二件事判断用户是否具有当前访问接口的权限
[09:05] 所以这是我们要完成的两个内容那我们一个一个的来看

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过自定义 Spring 拦截器来实现基于 JWT 的 API 权限控制，包括在登录接口中提取 token 并进行权限校验。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 页面，标题为“3.1 基于拦截器的token与鉴权”，内容介绍 Spring 中拦截器的作用和三个方法（preHandle、postHandle、afterCompletion）。
画面 2: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块。
画面 3: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块下的“Controller”包。
画面 4: 展示课程 PPT 页面，标题为“3 基于JWT的API鉴权”，内容与画面 1 类似。
画面 5: 展示课程 PPT 页面，显示“3.2 签发用户API权限”部分，代码为登录接口的实现，包含注解 @RequestMapping 和获取 mobile、password 的逻辑。
画面 6: 展示课程 PPT 页面，内容与画面 1 类似，鼠标光标在“3.2 签发用户API权限”标题下。
画面 7: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块。
画面 8: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_common”模块，弹出“Create New Class”对话框。
画面 9: 在 IntelliJ IDEA 中，编辑器显示新建的拦截器类“JwtInterceptor.java”，代码为继承 HandlerInterceptorAdapter 并重写方法。
画面 10: 在 IntelliJ IDEA 中，编辑器显示“JwtInterceptor.java”类，代码为重写 preHandle、postHandle、afterCompletion 方法。
画面 11: 在 IntelliJ IDEA 中，编辑器显示“JwtInterceptor.java”类，代码为重写 preHandle、postHandle、afterCompletion 方法，注释说明各方法的作用。
画面 12: 在 IntelliJ IDEA 中，编辑器显示“JwtInterceptor.java”类，代码为重写 preHandle 方法，注释说明“1. 通过拦截器获取到token数据”。
画面 13: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块下的“UserController”。
画面 14: 在 IntelliJ IDEA 中，编辑器显示“JwtInterceptor.java”类，代码为重写 preHandle 方法，注释说明“1. 通过拦截器获取到token数据”和“2. 未在用户权限校验（是否登录）”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 5 代码：
```java
//用户名密码登录
@RequestMapping(value = "/login", method = RequestMethod.POST)
public Result add(@RequestBody Map<String,String> map) throws Exception {
    String mobile = map.get("mobile");
    String password = map.get("password");
    User user = userService.findMobileAndPassword(mobile, password);
    if (user == null) {
        throw new CommonException(ResultCode.SYS_ERROR_MOBILE_PASSWORD);
    }
}
```

画面 9 代码：
```java
package com.ihrm.common.interceptor;

/**
 * 自定义拦截器
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
```

画面 10 代码：
```java
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true, 可以继续执行拦截器方法
 * false, 拦截
 * postHandle: 执行控制器方法之后执行的内容
 * afterCompletion: 响应结束之前执行的内容
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        return super.preHandle(request, response, handler);
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        super.postHandle(request, response, handler, modelAndView);
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        super.afterCompletion(request, response, handler, ex);
    }
}
```

画面 14 代码：
```java
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true, 可以继续执行拦截器方法
 * false, 拦截
 * postHandle: 执行控制器方法之后执行的内容
 * afterCompletion: 响应结束之前执行的内容
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1. 通过拦截器获取到token数据
        // 2. 未在用户权限校验（是否登录）
        return super.preHandle(request, response, handler);
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        super.postHandle(request, response, handler, modelAndView);
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        super.afterCompletion(request, response, handler, ex);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1 标题：3.1 基于拦截器的token与鉴权
画面 4 标题：3 基于JWT的API鉴权
画面 5 标题：3.2 签发用户API权限
画面 6 标题：3.1 基于拦截器的token与鉴权
画面 14 标题：3.2 签发用户API权限

5) 无。

