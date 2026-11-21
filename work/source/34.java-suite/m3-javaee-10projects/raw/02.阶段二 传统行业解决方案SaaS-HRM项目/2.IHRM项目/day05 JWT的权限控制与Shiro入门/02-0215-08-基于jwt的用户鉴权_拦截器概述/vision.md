# 画面线理解：08-基于jwt的用户鉴权：拦截器概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\08-基于jwt的用户鉴权：拦截器概述_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:36, 00:45, 01:39, 02:46, 03:07, 04:04, 04:13, 04:52, 05:17, 06:43, 07:25, 07:38, 09:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:12:35

1) 这一组画面整体在讲如何通过自定义 Spring 拦截器来实现基于 JWT 的 API 权限控制，包括在登录接口中提取 token 并进行权限校验。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 页面，标题为“3.1 基于拦截器的token与鉴权”，内容介绍 Spring 中拦截器的作用和三个方法（preHandle、postHandle、afterCompletion）。
画面 2: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块。
画面 3: 在 IntelliJ IDEA 中，项目结构显示选中了“ihrm_system”模块下的“controller”包。
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
