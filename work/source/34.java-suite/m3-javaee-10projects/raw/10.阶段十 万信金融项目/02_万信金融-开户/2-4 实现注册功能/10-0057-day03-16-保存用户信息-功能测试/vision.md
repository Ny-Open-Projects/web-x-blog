# 画面线理解：day03-16-保存用户信息-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-16-保存用户信息-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:16, 03:29, 05:25, 06:49, 07:58, 09:20, 10:22, 11:22, 11:57, 12:56, 13:35, 14:21, 14:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:38:43

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Postman 发起 HTTP 请求，结合 Spring Boot 服务和数据库操作，完成用户注册功能的前后端集成测试，并处理业务异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“4.7 前后端集成测试”章节，内容包含启动服务的注解配置和功能测试说明。
画面2：展示课程视频文件夹，列出 day03 相关视频文件。
画面3：展示开发环境，包含多个服务窗口（如 Postman、SQLyog、Redis Desktop Manager、ApolloPortal 等）。
画面4：在 Postman 中创建一个 POST 请求，目标地址为 http://localhost:33030/consumer/consumers。
画面5：在 SQLyog 中查看数据库表结构，当前未查询到数据。
画面6：在 SQLyog 中执行 SQL 查询语句，但未显示结果。
画面7：在 IDEA 中查看 ConsumerServiceImp.java 代码，展示用户注册逻辑。
画面8：在 IDEA 中查看控制台日志，显示服务启动过程。
画面9：在 IDEA 中查看控制台日志，显示服务启动后连接失败。
画面10：在 IDEA 中查看控制台日志，显示服务启动后抛出异常。
画面11：展示项目文件夹，包含多个 Java 文件。
画面12：在 IDEA 中查看 GlobalExceptionHandler.java 代码，展示异常处理逻辑。
画面13：在 IDEA 中查看控制台日志，显示服务启动后抛出异常。
画面14：在 Postman 中发送 POST 请求，请求体为 {"mobile": "1597801913"}，响应状态为 200 OK。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Bean
@CopyProperties(value = ConsumerRegisterDTO.class)
RestResponse<AccountDTO> restResponse = accountApiAgent
    .register(accountRegisterDTO);
if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getErrorCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
```
画面7：
```java
throw new BusinessException(ConsumerErrorCode.E_140107);
Consumer consumer = new Consumer();
BeanUtils.copyProperties(consumerRegisterDTO, consumer);
consumer.setUserName(consumerRegisterDTO.getUserName());
consumer.setMobile(consumerRegisterDTO.getMobile());
consumer.setIsCard(0);
save(consumer);
```
画面8：
```text
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Starting protocol handler [http://mic-33030]
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Client: account-service instantiated
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Server: account-service started
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Server status: Server: 32.306.2.15:33030
```
画面12：
```java
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;
```
画面13：
```text
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
