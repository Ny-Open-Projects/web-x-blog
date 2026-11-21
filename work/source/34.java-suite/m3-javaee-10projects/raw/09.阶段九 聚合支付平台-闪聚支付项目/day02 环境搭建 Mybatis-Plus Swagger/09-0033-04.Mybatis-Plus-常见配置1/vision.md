# 画面线理解：04.Mybatis-Plus-常见配置1

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\04.Mybatis-Plus-常见配置1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:40, 02:20, 03:12, 04:13, 04:50, 05:52, 06:49, 07:32, 08:16, 08:46, 09:21, 10:06, 11:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:36:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 MyBatis，包括配置文件位置、Mapper 接口与 XML 映射文件的编写，以及测试方法的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 课程内容：讲解 MyBatis 的配置，指出 MyBatis Plus 的配置详情在 https://mybatis.plus/config。
- 代码示例：在 resources 下创建 mybatis-config.xml。
- XML 配置文件内容：
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
  <configuration>
  <!--plugins-->
  </configuration>

画面 2：
- 画面内容：在 IDEA 中右键点击项目，选择“New”菜单。
- 代码内容：application.properties 文件中配置了数据源和 MyBatis 配置。
  spring.application.name=itcast-ap-springboot
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/ap?useUnicode=true&characterEncoding=UTF-8
  spring.datasource.username=root
  spring.datasource.password=mysql
  #配置mybatis-config.xml的位置
  mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml

画面 3：
- 画面内容：在 application.properties 文件中，修改了 MyBatis 配置文件路径。
- 代码内容：
  spring.application.name=itcast-ap-springboot
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/ap?useUnicode=true&characterEncoding=UTF-8
  spring.datasource.username=root
  spring.datasource.password=mysql
  #配置mybatis-config.xml的位置
  mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
  # Logger Config
  logging.level.root: debug

画面 4：
- 画面内容：在 mybatis-config.xml 文件中，配置了插件。
- XML 配置文件内容：
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
  <configuration>
  <!--plugins-->
  <!--plugin interceptor="com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor"-->
  </configuration>

画面 5：
- 画面内容：在项目结构中，选中了 mybatis-config.xml 文件。
- 画面内容：测试失败，提示“Tests failed: 1 of 1 test”。

画面 6：
- 画面内容：讲解如何创建 UserMapper.xml 文件。
- 代码内容：
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.mp.mapper.UserMapper">
  <select id="findById" resultType="cn.itcast.mp.pojo.User" parameterType="java.lang.Long">
  select * from tb_user where id = #{id}
  </select>
  </mapper>

画面 7：
- 画面内容：在 UserMapperTest 测试类中，编写测试方法。
- 代码内容：
  public class UserMapperTest {
  @Autowired
  private UserMapper userMapper;
  @Test
  public void testSelect() {
  List<User> users = userMapper.selectList(null);
  System.out.println(users);
  }
  }

画面 8：
- 画面内容：在 UserMapperTest 测试类中，编写测试方法。
- 代码内容：
  public void testFindById() {
  //查询用户
  User user = userMapper.findById(1L);
  System.out.println(user);
  }

画面 9：
- 画面内容：在 UserMapperTest 测试类中，编写测试方法。
- 代码内容：
  @SpringBootTest
  @MapperScan("cn.itcast.mp.mapper")
  @Configuration
  public class UserMapperTest {
  @Autowired
  private UserMapper userMapper;
  @Test
  public void testFindById() {
  User user = userMapper.findById(1L);
  System.out.println(user);
  }
  }

画面 10：
- 画面内容：在 User 类中，编写属性和方法。
- 代码内容：
  private String password;
  private String name;
  private Integer age;
  private String email;
  private LocalDate birthday;

画面 11：
- 画面内容：在 User 类中，编写属性和方法。
- 代码内容：
  private String password;
  private String name;
  private Integer age;
  private String email;
  private LocalDate birthday;

画面 12：
- 画面内容：在 IDEA 中右键点击项目，选择“New”菜单。
- 画面内容：测试失败，提示“Tests failed: 1 of 1 test”。

画面 13：
- 画面内容：在 application.properties 文件中，修改了 MyBatis 配置文件路径。
- 代码内容：
  spring.application.name=itcast-ap-springboot
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/ap?useUnicode=true&characterEncoding=UTF-8
  spring.datasource.username=root
  spring.datasource.password=mysql
  #配置mybatis-config.xml的位置
  mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
  # Logger Config
  logging.level.root: debug

画面 14：
- 画面内容：课程 PPT 页面，标题为“3.2 mapperLocations”。
- 画面内容：PPT 内容包括“我们的愿景是成为 MyBatis 最好的搭档，就像 魂斗罗 中的 1P 2P，基友搭配，效率翻倍。”
