# 画面线理解：08-zuul过滤器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\08-zuul过滤器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:29, 02:09, 03:53, 05:19, 07:11, 09:08, 09:48, 10:22, 10:52, 11:04, 11:25, 11:50, 12:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:14:48

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
  - 服务发现：eureka
  - 服务地址：
    - ihrm-company 127.0.0.1:9002
    - ihrm-system 127.0.0.1:9001
    - 员工微服务 127.0.0.1:9003
    - 企业微服务 127.0.0.1:9002
    - 业绩微服务 127.0.0.1:9003
  - 过滤器：API网关、权限校验
  - 服务注册与发现：eureka

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
