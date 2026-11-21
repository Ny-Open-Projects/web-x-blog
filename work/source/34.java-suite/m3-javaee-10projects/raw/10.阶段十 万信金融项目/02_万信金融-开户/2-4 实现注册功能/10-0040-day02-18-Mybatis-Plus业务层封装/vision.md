# 画面线理解：day02-18-Mybatis-Plus业务层封装

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-18-Mybatis-Plus业务层封装_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 02:35, 03:40, 04:18, 05:09, 05:50, 06:32, 06:52, 07:33, 07:55, 08:22, 08:46, 09:07, 09:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:26:12

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 框架实现用户服务层的接口定义、实现类编写及单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了项目结构目录，包含 service、mapper、pojo 等包。
- 代码编辑器中显示了 UserServiceImpl 类的片段，包含 @Autowired 注解和 save() 方法。
- 代码片段：public class UserServiceImpl { @Autowired private UserMapper usermapper; public void save() { usermapper.insert(...); } }

画面2：
- PPT 页面内容，讲解 MyBatis-Plus 的 Service 接口实现。
- 代码片段：public interface UserService extends IService<User> { }

画面3：
- IDE 中显示 UserService 接口定义，位于 cn.itcast.mp.service 包下。
- 代码片段：public interface UserService extends IService<User> { }

画面4：
- IDE 中显示 ServiceImpl 类的源码，展示其继承结构和方法。
- 代码片段：public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService { }

画面5：
- IDE 中显示 UserServiceImpl 类的继承结构，包含 ServiceImpl、UserMapper 和 UserService。
- 代码片段：public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService { }

画面6：
- PPT 页面内容，讲解测试类的编写。
- 代码片段：@RunWith(SpringRunner.class) @SpringBootTest public class TestUserService { @Autowired private UserService userService; @Test public void testInsert() { User user = new User(); user.setEmail("123@itcast.cn"); user.setAge(301); user.setUserName("cacao1"); user.setPassword("123456"); } }

画面7：
- IDE 中显示 TestUserService 类的代码，包含 @Transactional 注解。
- 代码片段：@Transactional @Test public void testInsert() { }

画面8：
- IDE 中显示 TestUserService 类的完整代码，包含 import 语句和测试方法。
- 代码片段：import cn.itcast.mp.service.UserService; import org.junit.runner.RunWith; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.boot.test.context.SpringBootTest; import org.springframework.test.context.junit4.SpringRunner; @RunWith(SpringRunner.class) @SpringBootTest public class TestUserService { @Autowired private UserService userService; @Test public void testInsert() { } }

画面9：
- IDE 中显示 TestUserService 类的测试方法，调用 userService.save()。
- 代码片段：public void testInsert() { userService.save(); }

画面10：
- IDE 中显示测试结果，测试失败，日志显示 HikariPool-1 关闭连接。
- 日志片段：HikariPool-1 - Closing connection with mysql.jdbc... Process finished with exit code -1

画面11：
- IDE 中显示测试失败的原因，提示 UserService 类未被 Spring 容器管理。
- 错误信息：Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'cn.itcast.mp.service.UserService' available: expected at least 1 bean which qualifies as autowire candidate

画面12：
- IDE 中显示测试通过，日志显示 Spring 测试上下文缓存统计和 HikariPool-1 关闭连接。
- 日志片段：Spring test ApplicationContext cache statistics: DefaultContextCache#ff6a76d size - 1, maxSize - 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
