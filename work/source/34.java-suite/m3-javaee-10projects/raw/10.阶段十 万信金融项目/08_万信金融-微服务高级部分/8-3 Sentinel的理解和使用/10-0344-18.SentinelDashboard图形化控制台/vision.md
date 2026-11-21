# 画面线理解：18.SentinelDashboard图形化控制台

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\18.SentinelDashboard图形化控制台_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:16, 01:37, 02:07, 02:32, 03:02, 03:34, 04:14, 04:48, 05:07, 05:28, 06:00, 06:36, 06:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:15:36

1) 这一组画面整体在讲如何配置并使用 Spring Cloud Alibaba Sentinel 控制台进行流量控制和监控。

2) 按时间顺序列出每张画面的要点：
画面1：浏览器访问 http://localhost:5000/sentinel/hello，页面显示“系统繁忙，请稍候”。
画面2：文件资源管理器显示包含 sentinel-dashboard.jar 文件的目录，文件名和大小信息可见。
画面3：PDF 文档页面显示“2.2 Sentinel-Dashboard图形化控制台”，并给出启动命令：java -Dserver.port=9999 -jar sentinel-dashboard.jar，同时提示默认用户名和密码均为 sentinel。
画面4：浏览器访问 http://localhost:5000/sentinel/hello，页面显示“系统繁忙，请稍候”。
画面5：浏览器打开 Sentinel Dashboard 登录页面，用户名和密码输入框已填入“sentinel”。
画面6：浏览器登录页面，鼠标光标在“登录”按钮附近。
画面7：IDEA 编辑器中显示 application.properties 文件内容，其中包含配置：spring.application.name=SentinelDemo、server.port=5000、server.servlet.context-path=/sentinel，以及 spring.cloud.sentinel.transport.dashboard=localhost:9999。
画面8：IDEA 控制台显示 Spring Boot 应用启动日志，包括初始化 DispatcherServlet 和完成初始化。
画面9：Sentinel 控制台页面显示“SentinelDemo”，左侧菜单栏包含“首页”、“实时监控”、“数据埋点”、“流控规则”、“降级规则”、“热点规则”、“系统规则”、“授权规则”、“机器列表”等选项。
画面10：Sentinel 控制台页面显示“SentinelDemo”的实时监控数据，包含“hello”资源的 QPS、拒绝 QPS、响应时间图表和数据表格。
画面11：IDEA 编辑器中显示 TestService.java 代码，其中使用 @SentinelResource 注解配置资源名“hello”和异常处理器“exceptionHandler”。
画面12：浏览器访问 http://localhost:5000/sentinel/hello，页面显示“Hello Sentinel”。
画面13：IDEA 编辑器中显示 TestController.java 代码，其中使用 @GetMapping 注解映射“/hello”路径，调用 TestService 的 hello 方法。
画面14：PDF 文档页面显示“2.3 限流规则详解”，并列出限流规则参数：1. resource：资源名，2. grade：限流类型（QPS 或并发线程数），3. count：限流阈值。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
java -Dserver.port=9999 -jar sentinel-dashboard.jar
注意：需要 JDK 版本为 1.8 及以上版本
然后通过浏览器打开 http://localhost:9999 即可访问 Dashboard，默认用户名和密码都是 sentinel

画面7：
spring.application.name=SentinelDemo
server.port=5000
server.servlet.context-path=/sentinel
# 设置 dashboard 的地址
spring.cloud.sentinel.transport.dashboard=localhost:9999

画面11：
@SentinelResource(value = "hello", blockHandler = "exceptionHandler")
public String hello() {
    return "Hello Sentinel";
}

public String exceptionHandler(FlowException e) {
    e.printStackTrace();
    return "系统繁忙，请稍候";
}

画面13：
@Target
public class TestController {
    @Autowired
    private TestService testService;

    @GetMapping("hello")
    public String hello() {
        return testService.hello();
    }
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面3：PPT 标题为“2.2 Sentinel-Dashboard图形化控制台”，内容包含启动命令和登录信息。
画面14：PPT 标题为“2.3 限流规则详解”，内容包含限流规则参数列表。
画面9：Sentinel 控制台左侧菜单栏包含“首页”、“实时监控”、“数据埋点”、“流控规则”、“降级规则”、“热点规则”、“系统规则”、“授权规则”、“机器列表”等选项。
画面10：Sentinel 控制台页面显示“SentinelDemo”的实时监控数据，包含“hello”资源的 QPS、拒绝 QPS、响应时间图表和数据表格。

5) 无。
