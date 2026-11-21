# 13.Mybatis-Plus-代码生成器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\13.Mybatis-Plus-代码生成器【海量资源尽在 666java.com】.mp4
- 时长 8分23秒（音频 503s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来看一下MyBatis-Plus给我们提供的代码生成器什么是代码生成器呢从字面意义上可以理解就是自动生成代码生成什么代码呢比如说我们在写Maple的时候大家知道这个Maple呢其实通常就是根据什么呀我们的表来生成的就是一张表对应一个Maple对不对包括这个什么POG的类这些其实我觉得都可以通过某种规则来生成
[00:30] 所以呢MyBitX Plus呢就给我们提供了一个代码生成器可以按照某些规则自动的生成我们要的Mapper呀包括这个模型类型啊甚至包括Service Control等这些类它都能生成那我们来看它是怎么用的首先你要加入MyBitX Plus的这个Generator的这个依赖然后呢官方提供的例子我们简单看一下啊比如说这里边呢你看它指定
[00:57] 比如说指定你这个要生成哪张表是不是啊然后呢他的思路其实很简单就是首先要连上你的数据库对吧连上你的数据库然后呢根据你配置的表然后呢他取出表的他的这个字段然后呢他呢其实是根据有一种模板引擎的技术我相信大家早期是不是学过GSP啊
[01:20] GSP呢其实你要知道它是根据动态的标签来生成HTML网页是吧它其实也是它是根据模板引擎然后提前呢你可以设置一些模板的页面然后呢根据模板生成你的类有时候老师呢这能不能测试一下嘛注意这个是官方给的例子啊就是我们项目其实在资料文件夹当中我给大家提供了一个Generator的工程
[01:45] 这个工程里边其实就是把官方给的这个例子呢简单的稍Vue化改造了一下然后呢我们这么弄我们把这个generator工程给它解压开然后呢我们把它拷贝到我们这个代码目录里头然后呢我们用idea呢把它打开然后现在我们针对这个工程我给大家讲一下基本的使用方法其实这里边呢主要是大家第一理解它的原理第二
[02:11] 能够去使用这个generator工程去生成我们要的代码就OK了好那现在呢我们是不是就打开了打开了之后呢大家可以看一下它的依赖里边我们该把该加的都加了myptisplus的包括数据库的驱动因为它要连数据库嘛这个就是我们说的模板引擎free marker就是说free marker呢它呢提供什么呀它是基于模板它可以生成
[02:40] 一些文件那你也知道我们其实那些什么加码类它都是文件嘛那我们就可以基于这个模板让它生成我们最重要的这个什么类文件对吧你看这里边package这是不是就报名啊导入什么什么你看这些是不是都是在我们的FreeMark模板里边设置好了好那么来我们来看有时候老师我没学过FreeMark其实这个模板不用你管
[03:05] 不用你改后期我们学过学到free marker的时候呢你就能看懂这些模板了如果当前这个时刻你没有学过free marker你也不要着急就是这些模板是他的这个generator工程给你提供的你要知道原理啊原理就是类似于free marker就类似于gsp就是将来呢这些标签都是动态标签传入一些数据哎他能
[03:28] 自动拼装成一个什么我们要的类文件的内容就跟JSP最终生成一个HTML网页是一个意思好那现在呢我们来看这个就是它的生成的一个组类那这个生成的组类它的使用方式呢很简单注意看首先呢控制台它要输入一个东西啊输入一个什么模块的名称注意看啊这个代码呢这个代码大家只要能看得懂就行了这是代码生成的组类然后呢里面有一些全局的配置
[03:56] 这个全局的配置呢最后呢我们最终会让它在一个目录里边把我们要的文件生成然后呢我们注意看我先给大家演示一下啊要配置哪些东西第一我们要配数据库连接假如我们现在呢连接MP就是我们现在的这个MP的数据库我们准备把TBU的这个类型呢把里面这个根据这个表生成我们要的代码行不行可以啊这是数据库的连接参数
[04:23] 这个是我们说的包名将来生成代码都在这个包下面可以吧好那现在呢我准备运行了看好运行一运行啊这个时候呢大家看就会在控制台啊就输入模块名这个输入模块名这一块大家注意啊你看它这个表明前缀是不是有一个叫TB它是不是有一个TB这个TB你如果输入TB的话注意啊
[04:51] 很关键TB这时候一旦回车它就会把什么它就会找到这个表这个表如果有TB的它就会把生成的这个类名会把TB这两个字母给它干嘛去掉啥意思回车看好现在我们生成了一对代码你也知道你生成的这个TB下滑线user所对应的模型类这个名称我觉得最好叫user
[05:20] 你不要叫TB吗所以他就会干嘛呀根据TB找到这个就是找到这些表发现这个表有前缀TB的他就把这个TB呢给他替换掉这样就得到一个user这个名称你懂我的意思吧然后呢还有这个TB呢还是一个什么还是一个包的名称对这他的规则你会发现你看他生成的这个什么类型
[05:48] 是不是就是把我们字段里边的这些属性是不是就罗列进去了然后还有Mapper是不是也给我们生成了包括Service也生成了就是它都给你生成了你想用你就用就是我们项目当中将来我们只用什么mapperentity是吧control也有很强悍这就是我们说的代码生成工具其实在实际的企业开发当中很多情况下这种通用的这种按照某种规则固定的这种代码都会
[06:18] 按照使用工具来生成好那现在呢我们是不是就生成了了生成完了之后有人说老师那能用吗当然能用你把这个user和user Mapper考到我们的工程当中是不是就可以用了对不对就和我们之前我们自己去写的这个user你看是不是都差不多呀这个就是我们说的什么代码生成器代码生成器所以其实代码生成器的它的原理呢就是首先连接你的数据库
[06:48] 找到里边有多少表然后呢把每张表然后呢根据Framark模板来生成我们要的类文件好那这个测试我刚才是不是给大家测试过了然后测试完了之后呢你是不是就可以把这个文件拷贝到我们工程去用就可以了当然如果你学习过Framark的话你说我准备把这个我能不能把这个类里边的一些什么信息改一下或者说我想自定义这个模板让你学过这个Framark你就可以去改
[07:18] 对吧那其实我们在项目开发当中一般来说你就直接拿来用我们直接去生成就可以了好如果你生成完了之后你要把这个删掉对吧你可以再运行是不是就可以再生成比如这时候我输入我随便输入模块名对吧输一下所以你看它照样是要找到你所有的表只不过你输入这个模模块名是不是叫XXX是吧这个三个X是不是并不是你表的前缀
[07:46] 所以这个时候呢它就会把怎么样把你这个表tbuser作为一个完整的名称作为你的这个类名你看叫tbuser变成驼峰的这种方式大家理解吗对所以大家去输入这个模块名的时候如果是表名的前缀它就会把这个前缀给它覆盖掉去掉然后呢把后边的作为一个类的名称好了那么以上呢就是我们说的什么这个
[08:15] 代码生成器在项目当中啊是最常用的一个武器啊好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 MyBatis-Plus 的代码生成器（AutoGenerator）自动生成项目中的实体类、Mapper 接口、Service 和 Controller 层代码。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 展示了 IntelliJ IDEA 中一个 Spring Boot 项目的结构，包含 `src/main/java` 下的 `com.itcast` 包，以及 `test` 包下的 `UserMapperTest` 测试类。
- `UserMapperTest.java` 中的代码：
  ```java
  wrapper.likeRight("name", val: "张");
  wrapper.select("id", "name");
  List<User> users = this.userMapper.selectList(wrapper);
  for (User user : users) {
      System.out.println(user);
  }
  ```

画面 2:
- 展示了 Typora 中的 PPT 内容，标题为“6 代码生成器”。
- 画面中显示了“2) 获取官方案例”的代码片段：
  ```java
  package cn.itcast.mp_generator;
  import com.baomidou.mybatisplus.core.exceptions.MybatisPlusException;
  import com.baomidou.mybatisplus.core.toolkit.StringPool;
  import com.baomidou.mybatisplus.generator.AutoGenerator;
  import com.baomidou.mybatisplus.generator.config.InjectionConfig;
  import com.baomidou.mybatisplus.generator.config.po.TableInfo;
  import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;
  import java.util.ArrayList;
  import java.util.List;
  import java.util.Scanner;
  ```

画面 3:
- 展示了 `MpGenerator` 类的代码，其中定义了表名数组：
  ```java
  private static final String[] TABLE_NAMES = new String[][]{
      "t_user",
      "c_user"
  };
  ```

画面 4:
- 展示了 Windows 资源管理器中的文件，包含 `shangjue.zip` 和 `generator.zip` 两个压缩文件。

画面 5:
- 展示了 IntelliJ IDEA 中名为 `generator` 的项目结构，其中 `src/main/java` 下的 `com.itcast` 包和 `generator` 包可见。

画面 6:
- 展示了 `Controller.java.ftl` 模板文件的内容，其中包含用于生成 Controller 类的 FreeMarker 模板代码：
  ```java
  @RestController
  @Controller
  @Api(value = "", tags = "", description="")
  class ${table.controllerName} {
  ```

画面 7:
- 展示了 `MyBatisPlusGenerator.java` 中的 `main` 方法，用于配置代码生成器：
  ```java
  public static void main(String[] args) {
      // 代码生成器
      AutoGenerator autoGenerator = new AutoGenerator();
      // 主要配置
      GlobalConfig globalConfig = new GlobalConfig();
      String projectPath = System.getProperty("user.dir");
      String projectName = "/generator";
      globalConfig.setOutputDir(projectPath + "/src/main/java");
      globalConfig.setAuthor("author");
      globalConfig.setOpen(false);
      globalConfig.setDbType(ID_WORKER);
      autoGenerator.setGlobalConfig(globalConfig);
  ```

画面 8:
- 展示了 `MyBatisPlusGenerator.java` 中的 `outputFile` 方法，用于自定义输出文件路径：
  ```java
  public String outputFile(TableInfo tableInfo) {
      return projectPath + "/src/main/resources/Mapper/" + packageConfig.getModule() + "/" + tableInfo.getEntityName() + "Mapper" + StringPool.XML;
  }
  ```

画面 9:
- 展示了控制台输出，显示 MyBatis-Plus 代码生成器成功连接到 MySQL 数据库并开始生成代码。

画面 10:
- 展示了 `User.java` 实体类的代码，包含 `username`、`password`、`name` 和 `age` 等字段。

画面 11:
- 展示了控制台输出，显示 MyBatis-Plus 代码生成器成功生成了文件。

画面 12:
- 展示了 Typora 中的 PPT 内容，标题为“策略配置”，其中包含设置命名策略和实体类属性的代码：
  ```java
  StrategyConfig strategy = new StrategyConfig();
  strategy.setNaming(NamingStrategy.underline_to_camel);
  strategy.setColumnNaming(NamingStrategy.underline_to_camel);
  strategy.setEntityLombokModel(true);
  strategy.setRestControllerStyle(true);
  strategy.setInclude(TABLE_NAMES);
  strategy.setTablePrefix("th_");
  strategy.setEntityBooleanColumnRemovePrefix(true);
  mpg.setStrategy(strategy);
  mpg.execute();
  ```

画面 13:
- 展示了 `entity.java.ftl` 模板文件的内容，其中包含用于生成实体类的 FreeMarker 模板代码：
  ```java
  import io.Swagger.annotations.ApiModel;
  import io.Swagger.annotations.ApiModelProperty;
  <!--#if entityLombokModel-->
  import lombok.Data;
  <!--#end-->
  import com.baomidou.mybatisplus.annotation.TableName;
  ```

画面 14:
- 展示了 Typora 中的 PPT 内容，标题为“6 代码生成器”，其中包含对 `AutoGenerator` 的介绍和在 `pom.xml` 中引入依赖的代码：
  ```xml
  <dependency>
      <groupId>com.baomidou</groupId>
      <artifactId>mybatis-plus-generator</artifactId>
      <version>3.1.8c</version>
  </dependency>
  ```

