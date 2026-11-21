# 画面线理解：22_app文章详情_关注接口_关注操作_接口编写及代码改造

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\22_app文章详情_关注接口_关注操作_接口编写及代码改造【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:35, 02:46, 03:28, 04:45, 05:31, 06:32, 07:54, 08:38, 09:37, 10:18, 11:08, 12:29, 13:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:22:22

1) 这一组画面整体在讲什么（一句话）：
演示用户关注功能的控制器测试、服务层实现及数据库操作，并通过测试验证功能正确性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA项目结构视图，显示 `heima-leadnews` 项目下的 `heima-leadnews-user` 模块，测试失败提示。
画面2：打开 `UserRelationController.java`，展示控制器类的包声明和导入语句，光标在 `@RestController` 注解处。
画面3：在 `UserRelationController.java` 中，光标位于 `@PostMapping("/user_follow")` 方法的 `return` 语句处。
画面4：打开 `UserRelationControllerTest.java`，光标在 `@Autowired` 注解的 `ObjectMapper mapper` 声明处，弹出 `ObjectMapper` 的导入建议。
画面5：在 `UserRelationControllerTest.java` 中，光标位于 `dto.setOperation(short);` 语句处，下方有测试方法 `testFollowAdd`。
画面6：测试失败，控制台显示异常堆栈，错误发生在 `UserRelationService` 的 `follow` 方法。
画面7：控制台输出日志，显示 ZooKeeper 会话建立成功。
画面8：测试通过，控制台显示 `Tests passed: 1 of 1`。
画面9：Navicat for MySQL 界面，显示 `ap_user_follow` 表，无数据。
画面10：打开 `AppUserRelationServiceImpl.java`，光标在 `apUserFan` 对象的初始化代码处。
画面11：打开 `ThreadPoolConfig.java`，光标在 `ThreadPoolTaskExecutor` 的 `setRejectedExecutionHandler` 方法处。
画面12：打开 `AppFollowBehaviorServiceImpl.java`，光标在 `saveFollowBehavior` 方法中，`apBehaviorEntryMapper.selectById` 语句处。
画面13：在 `AppFollowBehaviorServiceImpl.java` 中，光标位于 `appFollowBehaviorService.saveFollowBehavior` 方法调用处。
画面14：Navicat for MySQL 界面，显示 `ap_user_follow` 表中有两条记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.heima.user.controller.v1;

import com.heima.model.common.dto.ResponseResult;
import com.heima.user.apis.UserRelationControllerApi;
```

画面3：
```java
@RestController
@RequestMapping("/api/v1/user")
public class UserRelationControllerApi {

    @Autowired
    private AppUserRelationService appUserRelationService;

    @PostMapping("/user_follow")
    public ResponseResult follow(@RequestBody UserRelationDto dto) {
        return appUserRelationService.follow(dto);
    }
}
```

画面4：
```java
@Autowired
private ObjectMapper mapper;
```

画面5：
```java
public void testFollowAdd() throws Exception {
    UserRelationDto dto = new UserRelationDto();
    dto.setOperation(short);
    dto.setArticleId(1);
    dto.setAuthorId(1);
    MockMvcRequestBuilder builder = MockMvcRequestBuilders.post(urltemplate + "/api/v1/user/user_follow");
    builder.contentType(MediaType.APPLICATION_JSON_VALUE);
    content(mapper.writeValueAsString(dto));
    mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
    Thread.sleep(millis: 10000);
}
```

画面6：
```java
at org.mybatis.spring.MyBatisExceptionTranslator.translateExceptionIfPossible(MyBatisExceptionTranslator.java:73)
at org.mybatis.spring.SqlSessionTemplate.doExecute(SqlSessionTemplate.java:146)
at org.mybatis.spring.SqlSessionTemplate.execute(SqlSessionTemplate.java:228)
at org.apache.ibatis.binding.MapperMethod.execute(MapperMethod.java:6)
at org.apache.ibatis.binding.MapperProxy.invoke(MapperProxy.java:59)
at com.heima.user.service.impl.AppUserRelationServiceImpl.follow(AppUserRelationServiceImpl.java:114)
at com.heima.user.controller.v1.UserRelationController.follow(UserRelationController.java:57)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(Native Method)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:498)
at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:138)
at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:105)
at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:891)
at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:797)
at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:981)
at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:925)
at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:974)
at org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:874)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:661)
at org.springframework.web.servlet.FrameworkServlet.service(HttpServlet.java:849)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:742)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:231)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:166)
at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:198)
at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:96)
at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:496)
at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:140)
at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:81)
at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:651)
at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:87)
at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:342)
at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:799)
at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:66)
at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:868)
at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1455)
at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
at java.lang.Thread.run(Thread.java:748)
```

画面7：
```log
2019-09-17 19:38:24,191  INFO [main-SendThread(192.168.220.145:2181)] [org.apache.zookeeper.ClientCnxn] [Opening socket connection to 192.168.220.145:2181]
2019-09-17 19:38:24,249  INFO [main-SendThread(192.168.220.145:2181)] [org.apache.zookeeper.ClientCnxn] [Socket connection established to 192.168.220.145:2181]
2019-09-17 19:38:24,266  INFO [main-SendThread(192.168.220.145:2181)] [org.apache.zookeeper.ClientCnxn] [Session establishment complete]
2019-09-17 19:38:24,281  INFO [main-SendThread(192.168.220.145:2181)] [org.apache.zookeeper.ClientCnxn] [process: Negotiated session timeout: 30000]
2019-09-17 19:38:24,301  INFO [main-EventThread] [org.apache.curator.ConnectionState] [State change: CONNECTED]
2019-09-17 19:38:24,301  INFO [main-EventThread] [org.apache.curator.ConnectionState] [State change: CONNECTED]
2019-09-17 19:38:
