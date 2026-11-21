# 画面线理解：10-基于jwt的鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\10-基于jwt的鉴权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:58, 02:29, 03:17, 05:37, 06:22, 09:02, 09:36, 11:14, 12:12, 12:34, 13:12, 13:58, 15:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:16:34

1) 这一组画面整体在讲什么（一句话）：
讲解基于JWT的统一鉴权实现，通过Zuul网关拦截请求并验证token，实现无状态用户认证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”标志，鼠标悬停在“TIA-客户端”图标上。
画面2：PPT页面，标题为“2.2 统一鉴权”，子标题“2.2.1 基于JWT的统一鉴权”，展示Java代码片段：
@Component
public class AuthFilter extends ZuulFilter{
@Override
public String filterType() {
// 登录校验，肯定在前置拦截
}
}
画面3：流程图草稿，展示“浏览器”指向“zuul网关”，网关再分别指向“系统微服务”和“企业微服务”。
画面4：流程图，浏览器向zuul网关发送token，网关将token转发给“系统微服务”和“企业微服务”。
画面5：IDEA开发环境，展示LoginFilter.java文件内容，包含注释和部分代码：
import org.springframework.stereotype.Component;
@Component
public class LoginFilter extends ZuulFilter {
// 自定义过滤器
// 定义过滤器类型
// pre：在路由之前执行
// routing：在路由之后执行
// post：在路由错误之后执行
// error：处理请求出现异常的时候执行
public String filterType() {
return "pre";
}
public int filterOrder() {
// 过滤器的优先级，数字越小，优先级越高
return 2;
}
}
画面6：流程图，zuul网关中对token进行校验，标注“1. token需存在请求的header中，2. 校验token是否存在以及token中携带的权限信息是否合法”。
画面7：IDEA开发环境，LoginFilter.java文件，展示shouldFilter方法和run方法的代码片段：
public boolean shouldFilter() {
// 对某些请求过滤(不执行过滤器)
return true;
}
public Object run() throws ZuulException {
// System.out.println("执行 LoginFilter的run方法");
// 获取请求对象request
RequestContext rc = RequestContext.getCurrentContext();
// 从上下文对象获取request对象
HttpServletRequest request = rc.getRequest();
// 从request中获取Authorization的头信息
String token = request.getHeader("Authorization");
// 判断
if(token == null || "".equals(token)) {
// 没有传递token信息，需要登录，拦截
rc.setSendZuulResponse(false);
// 返回401状态码
}
return null;
}
画面8：IDEA开发环境，LoginFilter.java文件，展示获取request对象和获取Authorization头信息的代码：
RequestContext rc = RequestContext.getCurrentContext();
HttpServletRequest request = rc.getRequest();
String token = request.getHeader("Authorization");
画面9：IDEA开发环境，LoginFilter.java文件，展示判断token是否为空的代码：
if(token == null || "".equals(token)) {
// 没有传递token信息，需要登录，拦截
rc.setSendZuulResponse(false);
// 返回401状态码
}
画面10：IDEA开发环境，LoginFilter.java文件，展示设置返回状态码的代码：
rc.setResponseStatus(HttpStatus.UNAUTHORIZED);
画面11：IDEA开发环境，LoginFilter.java文件，展示filterOrder方法和shouldFilter方法的代码：
public int filterOrder() {
// 过滤器的优先级，数字越小，优先级越高
return 2;
}
public boolean shouldFilter() {
// 对某些请求过滤(不执行过滤器)
return true;
}
画面12：IDEA开发环境，控制台输出日志，显示Spring框架初始化过程，包括“initializing Spring frameworkServlet”、“FrameworkServlet 'dispatcherServlet'”、“Mapping URL path '/' onto handler”等信息。
画面13：IDEA开发环境，LoginFilter.java文件，展示设置返回状态码的代码：
rc.setResponseStatus(HttpStatus.UNAUTHORIZED);
画面14：IDEA开发环境，LoginFilter.java文件，展示设置返回状态码的代码：
rc.setResponseStatus(HttpStatus.UNAUTHORIZED);

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
@Component
public class AuthFilter extends ZuulFilter{
@Override
public String filterType() {
// 登录校验，肯定在前置拦截
}
}
画面5：
import org.springframework.stereotype.Component;
@Component
public class LoginFilter extends ZuulFilter {
// 自定义过滤器
// 定义过滤器类型
// pre：在路由之前执行
// routing：在路由之后执行
// post：在路由错误之后执行
// error：处理请求出现异常的时候执行
public String filterType() {
return "pre";
}
public int filterOrder() {
// 过滤器的优先级，数字越小，优先级越高
return 2;
}
}
画面7：
public boolean shouldFilter() {
// 对某些请求过滤(不执行过滤器)
return true;
}
public Object run() throws ZuulException {
// System.out.println("执行 LoginFilter的run方法");
// 获取请求对象request
RequestContext rc = RequestContext.getCurrentContext();
// 从上下文对象获取request对象
HttpServletRequest request = rc.getRequest();
// 从request中获取Authorization的头信息
String token = request.getHeader("Authorization");
// 判断
if(token == null || "".equals(token)) {
// 没有传递token信息，需要登录，拦截
rc.setSendZuulResponse(false);
// 返回401状态码
}
return null;
}
画面8：
RequestContext rc = RequestContext.getCurrentContext();
HttpServletRequest request = rc.getRequest();
String token = request.getHeader("Authorization");
画面9：
if(token == null || "".equals(token)) {
// 没有传递token信息，需要登录，拦截
rc.setSendZuulResponse(false);
// 返回401状态码
}
画面10：
rc.setResponseStatus(HttpStatus.UNAUTHORIZED);
画面11：
public int filterOrder() {
// 过滤器的优先级，数字越小，优先级越高
return 2;
}
public boolean shouldFilter() {
// 对某些请求过滤(不执行过滤器)
return true;
}
画面12：
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/] : Initializing Spring frameworkServlet 'dispatcherServlet'
2019-08-26 21:37:37.604 INFO 18936 --- [nio-9000-exec-1] o.a
