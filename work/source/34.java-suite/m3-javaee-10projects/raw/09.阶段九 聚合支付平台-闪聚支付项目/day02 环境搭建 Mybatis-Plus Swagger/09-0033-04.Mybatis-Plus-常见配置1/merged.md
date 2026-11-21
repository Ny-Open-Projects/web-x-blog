# 04.Mybatis-Plus-常见配置1

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\04.Mybatis-Plus-常见配置1【海量资源尽在 666java.com】.mp4
- 时长 11分14秒（音频 675s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来看一下mybattlesplus的常见配置那么在之前我们学习mybattles课程的时候呢我们知道它呢可以配置很多的项对吧那在mybattlesplus我们来看它是怎么配置的首先第一个叫configure location这个配置呢是指定mybattles-configure这个配置文件这个配置文件大家应该还熟悉吧这是mybattles框架它指定的一个配置文件
[00:27] 虽然mybdxplus和sprintboot进行集成但是呢其实它也可以使用这个mybdx-configure这个配置文件好我们来看一下吧怎么做那首先呢我们是不是得把这个配置文件给它创建出来然后呢我们来看看它在mybdxplus这边它是怎么去指定这个配置文件的首先我们在resource这儿然后我们把这个配置文件创建出来然后这里边的内容呢其实我们可以暂时先写一个空的内容
[00:54] 这是一个空的内容然后呢这个配置文件你看我是不是就创建好了创建好了之后呢我们现在是不是需要去指定这个配置文件的位置啊那这时候在哪指定啊这需要在我们的这个Spring Boot给我们的这个配置文件里面叫application.properties这里面是吧然后我们指定一个key value串就可以了注意看它的配置方法很简单这个呢其实就是什么就是指定
[01:23] 指定我们说的这个mybatties-configure.tab它的位置对吧它的位置你看它是不是class pass这个resource是不是就是class pass下边的这个mybatties-configure.tab就这个位置那如果说这里边我再创建一个目录它叫什么呀mybatties那我问你这时候我把这个文件拖进去这时候这个位置应该怎么指定
[01:53] 它就变成mybatties杠大家看懂了吗这个目录要注意好那现在我们说它指定了到底有用吗其实我们可以运行一下刚才的测试因为你只要一运行它是不是就会加载配置文件对你会发现是不是就这个测试是不是正常跑了但是有人说老师那我怎么就知道配置文件有效果有用其实很简单你怎么做那你在这你把这个
[02:23] 你把这个路径改错它其实通过这个路径是不是找不到啊那找不到你看你看它会不会报错你看看一下各位它是不是就报错了对吧它说这个什么呀这个路径不存在对不对所以说明我们这个配置是不是起了作用了好这是配置mybattles-configure这个什么插门的位置啊那将来你看这个插门我们当初学习mybattles的时候这里边是不是可以配很多东西啊我们可以在这里边去配
[02:52] 好那么接下来我们再看一个配置叫Mapper Location刚才是Configure Location那是Mapper LocationMapper Location是干嘛的呀是不是就是配置Mapper XML它的映射文件的位置那么我们之前学习过MapTest如果我们不配Mapper XML那么我们知道就是Mapper XML映射文件的这个位置是和Mapper的这个什么文件的位置路径是一样的
[03:20] 但只不过呢这个映射文件是要放在resource下那比如说我给大家看我举个例子因为现在我们用的这个Mapper你看它是个接口因为我们默认是用它封装好的这些什么方法如果我们想自定义一个Mapper的一个方法的话那这时候我们就需要去新建映射文件了那新建映射文件映射文件建哪呢我们说如果你不指定Mapper映射文件的位置它和Mapper接口的位置一样就在resource下注意看
[03:49] 叫CNCN你看对应的是不是这个CN对CN然后下边是不是还有一个叫IDCAST注意你可不要这么写啊为啥因为在resolve下它是没有办法建包的啊你只能一层一层的建看好啊CN对吧IDCAST然后呢再MP看到吧然后呢再建一个叫MAP
[04:17] 那我问你现在这个Mapper是不是就对应这个Mapper你看它的路径是不是一样那最终都会打包到class的这下边的这个目录你看它的目录最终打进去的话这里边我建一个什么建一个映射文件你要注意它就和我们说的Mapper接口的这个文件它就在同一个目录了大家能理解吧
[04:41] 这当初我们学习myptest的知识是吧那好现在呢我们来建这么一个映射文件看好啊这个映射文件呢嗯这个映射文件我来拷贝一下因为这个比较简单啊大家可以看到是不是就是根据ID查询这个user你看对吧然后呢select然后where等于ID所以这个大家当初学过myptest嘛所以我就不再去敲了啊那么我们写完了之后我们的目的是什么呢
[05:07] 我们的目的是要看一下现在我们说这个MapperLocation怎么配对不对那现在我还没有配MapperLocation吗MapperLocation不用配的话它就是这个路径那我怎么测呢其实很简单我首先呢Mapper映射里边有一个这个slack的ID等于byfindByID的那我当然需要在这儿对不对也需要增加一个嘛增加一个和这个ID名字相同的这个方法名那么它呢就是
[05:37] 返回user它传入进去的是不是就是一个ID各位是不是就写好了你看这方法名是不是和这个Mapper里面的这个ID是保持一致好那现在呢我们是不是就可以在这测一下可以吧好来我们改一下这个方法名叫find by ID是吧然后呢它呢是不是就是find by ID那么我们随便找一个记录吧你看1吧
[06:10] 就输入一个2吧它是个浪形嘛是吧然后呢最后是不是返回一个user那现在我如果啊我把这个测试方法一执行发现能正常执行那是不是就说明我们这个映射文件我们写对了映射文件的位置就是按照我说的当没有配置Mapper位置的时候呢它和这个映射Mapper接口的位置是不是一样的这个路径对吧好
[06:40] 那我们来看那我们是不是就可以跑一下看一下看他对不对啊你看是不是就正常了对不对你看你看他跑完了之后你看他没有我想让他打印出这个user的信息但是他打印出了一个什么这个类的一个地址对象的地址是吧那怎么办呢我们需要在user里面加一个to stream方法可以吧
[07:10] user里边加toString的话按照我们之前的玩法是不是就会定义一个public然后呢toString对不对那现在呢我们不这么玩了因为在前面我说过有一个插件啊是不是叫做longbook对是不是就它那么这个longbook怎么用呢太简单了看好我们在这加一个注解叫data对加了这么一个注解的话我告诉你这个guideset的方法呢就自动就就OK了
[07:41] 就有了那有时候老师我想加一个to stream行不行可以你看这就自动加to stream有时候老师我还想加一个它的构造方法行不行构造方法它分有参构造和无参构造你看这就是自动生成无参构造这是有参构造有时候老师我不相信对吧不相信我们可以给你测一下你看好看好那这里边我们是不是就可以来我给你我给你看一下我给你测一下然后在user你看点你看set方法是不是都有了你看get方法
[08:15] 有吧对不对盖的方法是不是都有了包括它的什么呀to string你看自动是不是就生成了对所以其实就是我们说的long bulk是非常方便的long bulk非常方便就是通过这几个注解就搞定那其实我们为什么刚才说正在写这个测试方法我没有转到这个long bulk呢其实因为我们刚才一运行你没发现吗它打了一个对象的地址现在我们是不是要想让它打印出一些信息你看方便我们看吗
[08:44] 所以你来看一下你看这是不是就是走它的这个to stream了你看它是把这个信息都拿到了对好那现在呢各位我们说这个user Mapper它的位置就是和user Mapper接口的位置映射文件和接口是同一个位置都是cn你看cnitcast map
[09:07] 但我们现在学习的是这个配置啊它是叫做什么呀叫Mapper Location看见吗Mapper Location如果我们想指定另外一个位置比如说举个例子啊我在这儿我在这儿指定一个目录叫Mapper然后呢我把这个什么我把这个拖进去我问你现在这个Mapper映射文件的位置和这个
[09:31] 这个这个这个接口的位置还在一个路径吗不在了吧所以你在运行他肯定报错因为他找不到嘛找不到这个映射文件对不对他就报错了他报啥错呀他说这个这个statement就是映射文件里的这个select就找不到所以这时候我们怎么我们就需要在这个配置文件里面我们要干嘛我们要指定这个什么Mapper的位置
[09:58] 有时候老师你干嘛要指定啊那你就和这个接口位置保持一样就OK了吗你为啥要指定因为你没发现嘛它这个你看位置好长对不对写起来太麻烦然后呢我们就弄个短的路径好那我们来看吧这里边咋指定啊很简单啊我们往下翻那我们就需要使用这种方式来指定其实就是kvalue的一些配置啊都是以myptis-plus开头你看这个叫Mapper location
[10:27] 这个大家知道吗class pass星指的是什么呀class pass星是不是就指的是去找吗因为他要加载这个Mapper映射他就去他就去class pass下边所有的jar 包里边来找只要符合这个路径的这个映射文件的他都会把它加载进来那class pass下边是不是有mybattles这个目录我看见吗然后呢有Mapper这个目录对吧
[10:55] 那就找到了这个新点插描就找到user Mapper插描好我把这个配置一旦加上这时候呢我们再来运行这个测试方法你会发现它就正常看见吗它就正常了这就是我们学习的第二项配置叫做Mapper location对吧Mapper location

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  spring.application.name=itcast-ap-Spring Boot
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/ap?useUnicode=true&characterEncoding=UTF-8
  spring.datasource.username=root
  spring.datasource.password=mysql
  #配置mybatis-config.xml的位置
  mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml

画面 3：
- 画面内容：在 application.properties 文件中，修改了 MyBatis 配置文件路径。
- 代码内容：
  spring.application.name=itcast-ap-Spring Boot
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
  <!DOCTYPE Mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.mp.Mapper.UserMapper">
  <select id="findById" resultType="cn.itcast.mp.pojo.User" parameterType="java.lang.Long">
  select * from tb_user where id = #{id}
  </select>
  </Mapper>

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
  @MapperScan("cn.itcast.mp.Mapper")
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
  spring.application.name=itcast-ap-Spring Boot
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

