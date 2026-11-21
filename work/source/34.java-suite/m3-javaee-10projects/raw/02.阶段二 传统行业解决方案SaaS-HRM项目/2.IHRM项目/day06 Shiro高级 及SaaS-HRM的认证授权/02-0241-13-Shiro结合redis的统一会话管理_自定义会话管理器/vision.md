# 画面线理解：13-Shiro结合redis的统一会话管理：自定义会话管理器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\13-Shiro结合redis的统一会话管理：自定义会话管理器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:34, 02:32, 03:15, 04:20, 04:35, 05:53, 06:49, 07:57, 08:46, 09:42, 09:59, 10:55, 11:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:35:05

1) 这一组画面整体在讲如何通过自定义Shiro的SessionManager并结合Redis实现统一的会话管理。

2) 按时间顺序列出每张画面的要点：
画面1：展示Shiro结合Redis的统一会话管理架构图，说明身份认证、会话管理与Redis服务的关系。
画面2：展示项目目录，突出redis-server.exe文件，暗示Redis服务已准备就绪。
画面3：展示SessionManager与SessionDao的关系图，说明需要自定义SessionDao并配置Redis。
画面4：展示application.yml配置文件，包含数据库和Redis连接信息。
画面5：展示多个开发工具窗口，包括IDEA、Redis Desktop Manager、Postman等，用于演示环境。
画面6：展示CustomSessionManager类的创建，继承DefaultWebSessionManager。
画面7：展示CustomSessionManager类的初始代码结构。
画面8：展示DefaultWebSessionManager的源码，用于理解SessionId的生成逻辑。
画面9：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面10：展示Shiro的统一会话管理架构图，与画面1内容相同。
画面11：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面12：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面13：展示DefaultWebSessionManager的源码，用于理解SessionId的生成逻辑。
画面14：展示CustomSessionManager类中添加获取SessionId的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
<dependency>
    <groupId>org.crazycake</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>

画面4：
server:
  port: 8081
spring:
  application:
    name: ihm-company #指定服务名
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/shiro_db?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  redis:
    host: 127.0.0.1
    port: 6379

画面6：
package cn.itcast.shiro.session;
import org.apache.shiro.web.session.DefaultWebSessionManager;

画面11：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

画面12：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

画面14：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：标题“2.3 Shiro结合redis的统一会话管理”，架构图：前端请求 → 身份认证 → 认证中心 → 认证通过 → 会话管理 → 存储到redis；会话管理 → Redis服务。
画面3：标题“2.3.2 构建环境”，架构图：SessionManager → SessionDao → Redis。
画面10：标题“2.2 应用场景分析”，架构图：前端请求 → 身份认证 → 认证中心 → 认证通过 → 会话管理 → 存储到redis；会话管理 → Redis服务。

5) 不要评价画面美观，不要输出与课程无关的内容。
