# 画面线理解：16-shiro认证与授权：基于ini的用户认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\16-shiro认证与授权：基于ini的用户认证_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 01:18, 01:50, 02:33, 03:31, 05:55, 06:44, 09:44, 10:34, 11:31, 12:48, 13:50, 15:00, 15:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:17:21

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中使用Shiro框架进行用户认证，包括创建项目、配置依赖、编写测试代码和处理认证失败。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，标题为“4.4 Shiro的入门”，子标题“4.4.1 搭建基于ini的运行环境”，并显示了Maven依赖配置代码。
画面2：在IntelliJ IDEA中创建新项目，选择“Empty Project”。
画面3：IntelliJ IDEA项目创建完成后的初始界面。
画面4：显示了项目中的pom.xml文件内容，包含Shiro和JUnit的依赖配置。
画面5：黑屏，可能是视频切换或暂停。
画面6：展示课程PPT，标题为“4.4.1 用户认证”，并显示了ini配置文件内容。
画面7：展示多个窗口，包括PDF文档、IDEA项目、SQL日志等，用于说明Shiro的认证流程。
画面8：在IntelliJ IDEA中编写ShiroTest01.java测试类，导入Shiro相关包。
画面9：IDEA提示“不兼容的类型”，建议将变量类型改为InSecurityManagerFactory。
画面10：在ShiroTest01.java中，将SecurityManager设置到当前运行环境。
画面11：运行测试时出现异常，提示“UnknownError”。
画面12：在ShiroTest01.java中，创建UsernamePasswordToken对象并调用subject.login方法。
画面13：在IDEA中，使用Ctrl+Alt+Shift+L格式化代码。
画面14：测试失败，显示“SLF4J: Failed to load class 'org.slf4j.impl.StaticLoggerBinder'”和“org.apache.shiro.authc.IncorrectCredentialsException”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<dependencies>
    <dependency>
        <groupId>org.apache.shiro</groupId>
        <artifactId>shiro-core</artifactId>
        <version>1.3.2</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
        <scope>test</scope>
    </dependency>
</dependencies>

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>shiro_demo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面6：
[users]
#模拟从数据库查询的用户
#数据格式：用户名-密码
zhangsan=123456
lisi=654321

画面8：
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.junit.Test;
public class ShiroTest01 {

画面9：
Factory<SecurityManager> factory = new IniSecurityManagerFactory( inResourcePath: "classpath:shiro-test-1.ini");

画面10：
SecurityManager securityManager = factory.getInstance();
SecurityUtils.setSecurityManager(securityManager);

画面12：
String username = "zhangsan";
String password = "123456";
UsernamePasswordToken token = new UsernamePasswordToken(username,password);
subject.login(token);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题“4.4 Shiro的入门”，子标题“4.4.1 搭建基于ini的运行环境”。
画面6：标题“4.4.1 用户认证”，内容包括“认证：身份认证/登录，验证用户是不是拥有相应的身份”。
画面7：展示多个窗口，包括PDF文档、IDEA项目、SQL日志等，用于说明Shiro的认证流程。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
