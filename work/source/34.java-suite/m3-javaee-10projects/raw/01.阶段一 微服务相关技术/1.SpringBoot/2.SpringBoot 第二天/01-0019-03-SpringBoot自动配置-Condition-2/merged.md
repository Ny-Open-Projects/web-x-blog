# 03-SpringBoot自动配置-Condition-2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\03-SpringBoot自动配置-Condition-2_【海量资源尽在 ubkz.com】.mp4
- 时长 18分10秒（音频 1091s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 简单的了解完condition并且呢我们做完了第一个需求之后呢我们来分析一下当前这个代码写的有没有问题啊我们发现我们写了这么一个类啊写一个条件类这个条件类呢只能判断你环境里边得有Jadis的坐标或者说得有Jadis这个类那么能不能写成一种动态的方式就是将来这个class condition啊它可以判断任意的你所指定的类
[00:30] 是否存在于你当前的环境中我把它搞成动态的那么这个是不是更加通用一些所以呢我们来看第二个第二个需求第二个需求呢就是将这个类的判断为定义为动态的也就是说你判断哪个字节码文件是可以动态指定的那么动态指定我们打开这个idea来看你在哪个地方指定呢OK那么接下来我们就可以这样做
[00:59] 我们这个地方呢可以来定义一个对应的注解定义一个注解这个注解呢我们就写名为condition on classcondition on class这个注解要能完成跟刚才这个注解一模一样的功能那么现在呢我们就可以不使用这个注解了OK那么我们使用我们自己定义的注解condition on class
[01:29] unclass完事了之后呢我们在里边可以指定指定谁呢我们比如说还是Jadis的话我们就在这个地方呢把Jadis这个复制过来这个字符串复制过来复制过来我放在这个地方OK那么将来我这样指定了之后这个玩意儿是不是相当于动态呢那么这个注解要和我们系统提供的conditional这个注解完成一样的功能非常简单你只需要把这个注解给它放到你自定义的注解上就可以了好
[01:58] 这样呢这两个注解完成功能就是一模一样的了而你自定义的这个注解呢又需要来配置属性刚才这个配置属性你看我什么都没写对吧为了方便其间我们给它定义一个叫做value的属性好stringvalue那么将来可以指定很多个类所以呢我们就加个数组就可以了这样写完之后写完之后我们再来看这个地方来看哎这个地方呢还是在报错是吧
[02:28] OK那么这个地方我们来看我们写错了我们写错了conditioncondition on classcondition这个名写错了condition多写个n对吧好重新来renew file一下renew file一下之后呢我们把这个重新来引一下condition on class没问题吧好现在你看这个condition on class是不是就是我们自己定义的这玩意儿了OK吧com at 黑马下的OK
[02:56] 那么这样弄完了之后呢接下来我们来说现在呢这个注解能不能生效呢还差最后一点点哈我们需要把这里边的原注解给它复制过来我们就找到这个注解里边这有三个原注解这三个原注解呢我们也给它复制到我们自己定义的注解上边OK三个原注解分别解释一下targettarget表示了你可以这个注解可以加到哪个范围上类上边
[03:24] 和方法上面第二个retention表示了你这个注解生效的时机是remit time第三个第三个表示了documented表示了生成java doc的文档好嘞那么这样我们这个注解写完了写完了之后呢接下来我们也把这个注解呢也加到了我们创建这个bin的上面了来看一下能不能生效能不能生效呢其实呢还是可以的因为我们这个最终的条件就是我们的条件
[03:52] 这里边是没有改的什么都没改还是写死的对吧好那么现在看它是报错的报错的原因呢是因为我们没有去指定我们Jadis的坐标好我们把这个坐标呢给它打开打开之后呢我们再来看它如果可以成功的创建这个病证明我们自定义注解的方式是可以行得通的哎来看一下这个地方呢它还是报错那么报错的原因呢可能是因为我们的一些缓存的一些信息哈
[04:21] 就是代码的缓存我们把这个地方呢随便敲两个敲一下敲一下之后呢让它重新编译一下然后我们重新的运行一下现在看user是不是就获取到了获取到了之后呢你把这个jallies呢再来你把它给它注释掉注释掉之后呢你会发现它现在呢可能就获取不到了是吧报错了它说没有这个user那么这个时候呢我们做完了第一步第一步呢我们自定义了一个书解
[05:00] 自定义完注解之后呢我们在这个地方呢使用我们自己定义的注解来指定对应的你要判断的那个类是否存在那么将来呢我们是不是就可以获取这个自己定义的这个字符串或者说自己定义的这个类文件是否存在了而不用在这个里边把这个玩意写死了吧对吧那么如何来获取你这个注解上定义的值呢我们这个时候呢就要聊一聊match这个方法的两个材数了
[05:27] 这两个参数我们来写个注释第一个参数叫做context这个参数是一个上下文对象它可以用于获取一些比如说环境IOC容器还有classloaderLOAD对象我们可以来看一下context
[05:57] 我们在这个地方用不到所以我们就没有去说dear get是不是获取环境environment你获取环境对象的话你可以来获取配置文件里边配置的属性值了我们之前讲过environment可以来获取property的属性值对吧获取对应的配置的属性通过get property方法这个我们待会再来看那么第二个metadata就是我们的注解的原对象注解的原对象
[06:26] 原对象那么这个原对象呢可以用于获取注解定义的属性值那么这刚才我们配置的那个属性值就可以通过这个metadata来获取了好嘞那么我们把这个呢代码呢我们给它注释掉注释掉之后呢我们再来做这个事好我们把它呢重新呢复制一份复制一份之后好接下来我们需求换了
[06:57] 第二个需求还是要导入Jadis坐标不是导入Jadis坐标了导入指定的坐标指定的坐标通过什么指定的呢通过注解属性值value来指定的这个坐标然后呢才能创建这个病对吧好嘞那么接下来这个里边这个名字是不是就不能写死了那么我们应该先去来判断思路就删掉了我们就应该来判断来去
[07:27] 判断我们的或者说第一个就是获取啊获取我们的注解属性值那个注解的属性的名字叫做value那么值呢获取一下通过怎么获取呢metadata.get有一个方法叫做annotation attributes那么里边传入你那个注解的名称我们那个注解的名称叫做condition on classcondition on class好dear class.get name
[07:54] 这样这个名字就有了是包名 内名 全路径名那么这样就获取一个map集合ok吧那个map集合有了之后我们把map打印一下看一下先看一下map好看完了之后我们再来说其他的事重新运行一下来看这个map集合返回的是一个value这个value就是我们的属性的键的名称然后值是一个数组因为我们定义的就是一个数组
[08:29] 你看我们这个地方定义的是不是就是数组OKvalue是固定的这个数组里边的值呢是可以变化的对吧所以呢我们在这个地方呢map即可给你了你来获取对应的值是不是非常简单的事OK那么在这个地方我们把这个打印呢就注释掉注释掉之后呢我们通过map.get方法k呢是固定的就是value它返回一个值呢是四不穿的数组四不穿的数组
[08:56] 那么数组有了之后我们现在呢只需要来去判断或者说我们在这个地方呢数组有了对吧我们只需要来便利这个数组it12便利这个数组便利这个数组呢就是class name了每一个就是一个类名然后呢我们把这个class name呢全部去寻找一遍是不是就可以了有任何一个不在是不是就说明你当前的环境里边没有对应的一个jar 包或者坐标啊OK
[09:25] 那么这样我们就做完了做完了之后呢接下来我们再来去运行一下看一下效果现在呢我们当前环境里边有有没有Jadis呀没有对吧我把它打开OK吧有Jadis吧有Jadis了之后呢我们配置的时候呢也指定的是你需要去有Jadis那么接下来我们来运行一下现在呢这个BIN就可以被创建出来了是这样的吗
[09:55] 那么如果我们配置的时候我们没有去指定没有指定对吧没有指定你就创建不出来将来就会报错的那么除了Jadis之外其实你想指定啥就指定啥现在你提供了一个B对吧这个B是User功能非常非常的强大但是你的条件是你要使用我这个BOK我可以让你用但是你必须给我加载一个坐标进来加个什么坐标呢
[10:25] 你说了算对吧你说了算那么这个地方呢比如说我们可以再演示一下你加载一个其他的坐标我们看一下这里边还有什么其他的比如说我们加载一个好我们导一个坐标导一个比如说fast json吧好fast json json转换器这么一个坐标那么现在呢你必须来我们来看用的时候你必须在这个地方呢
[10:52] 给我去导入一个其他坐标这个坐标呢叫做我们看一下这里边这个Jason的一个类名叫啥Jason就这个类这个玩意呢我们把这个全路径名给它复制到这个地方放在这放在这之后呢接下来我说你用我的user对象你必须导入fastjason的坐标如果你不导入我就不让你用现在呢你看是不是指定了指定了之后呢并且并且注意看
[11:19] 并且呢这个地方呢已经给我导入了fastjson了是吧导入了之后呢我们运行现在这个user就可以被创建出来现在就是一种动态的方式你想指定什么就可以指定什么是吧那么我把fastjson呢给它注释掉注释掉之后呢我们再来启动你看是不是就创建不出来这个bin了那么这个功能有什么用啊我们再回过头来来看看我们刚才那个刚才这个地方的一个思考
[11:55] 那么Spring Boot是如何知道要创建Redis Template的呢它其实就是使用condition来去判断判断你当前环境里边有没有导入Redis的stutter如果导入了它就帮你创建Redis的template那么其实在Spring Boot里边它给我们提供了非常多的这种condition on什么什么的东西那么在哪看呢我们可以来这里边看一下来看一下
[12:25] 这里边有一个jar 包稍等一下这个jar 包这个jar 包呢叫做Spring Boot Auto Configure这么一个包这个包我们点开看这是Spring Boot的自动配置包这里边呢有很多代码我们来找一个condition的这个包condition包里边你注意看有一大堆号是吧比如说condition on class这个玩意呢condition on class很熟悉吧其实就是刚才我们写的那玩意点进去看一下你看它里边定义了一个注解
[12:55] 这个注解里边上面加了一个condition这个condition有一个onClassCondition干啥呢就是在判断你是否有对应的字解码文件除了这个之外还有什么呢比如说conditionOnBean第一个conditionOnBean也就是说当你的环境IoC容器里边有这个Bean的时候我才去创建这个BeanOK那么再来看一个比较常用的conditionOnProperty
[13:25] 就是当你的配置文件里面去配置了指定的属性才去创建某一个bin,待会我们都会来演示一下那么还有,比如condition on missingbin就是说,当你的IOC容器里面没有那个bin的时候我们才去初始化对应的一个你指定的那个bin那么有这些东西之后呢,我们再来看再来看一个就是redis的对应的东西redis呢,它有一个叫做data包
[13:53] 这个Data包里边有一个叫做RedisRedis有一个配置类叫做Redis的Auto Configuration来看一下Redis的Auto Configuration那么来看Redis的Auto Configuration这个类上面这个就是一个配置类对吧它有很多的bin很多的bin它在初始化什么呢Redis的template那么这个Redis的template要想被初始化出来它有很多条件要满足第一个条件你看condition on class就是说
[14:19] 我们必须在当前环境里有这么一个字节码文件存在然后才能去初始化这个register template加到内上面的下边所有的都需要满足那么加到这个方法上还加了一个condition on missing bin哪个missing bin呢就是说register template这个bin在你当前的IOC容器里面不存在它才会去创建这个register template如果存在那就证明你自己定义了register template
[14:49] 用你自己定义的呗OK那么这么几个呢我们可以来简单的看一看演示一下比如说演示一个我们在这个地方呢来写一个就用这个user configure好user configure里边呢我们在这个地方呢我们把这个呢就注释掉了注释掉之后呢我们再写一个bin还是叫这个user吧我们比如说user2在这个地方呢我们at bin
[15:18] 就是刚才我们讲的所有的condition的动作都不用我们自己定义了我们直接可以用人家提供好的condition你看是不是一大堆对吧condition比如说unproperty我们来定义一个这个这个玩意儿呢就是只有当你某一个属性和对应的值存在它才会去加在这个bin那么比如说我们指定一下它的namename呢比如说叫做itcast好然后它有一个属性值叫做
[15:47] HandValue叫做比如说指定为IT黑码换句话说就是当你配置文件里边有一个键叫ITCast值呢对应的是IT黑码的时候才会去加载对应的这个bin好现在呢我们看获取user2来能不能获取到呢我们来试一下user2走现在是获取不到的因为我们的配置文件里边没有对应的那个对吧没有吧你看是不是user2获取不到
[16:17] 那么我们可以来配置一下配置一下呢我们就配itcast等于it黑码对吧那么定义好了配置文件那边有这个建制对了我们再来获取就可以获取到了OK吧好嘞这样呢就说完了对应的condition条件相关的这个功能那么最后呢我们来做一个小结小结呢首先呢我们要可以自定义条件自定义条件呢还有呢我们说了Spring Boot提供的常用的一些条件注解
[16:51] 那么先来说自定义的条件自定义的条件呢首先我们定义一个条件类这个条件类呢就是我们实现这个condition的接口重写max方法这个方法呢我们要进行一个不耳直的判断对吧那么这个方法其实有两个参数这个参数呢一个是context上下文对象可以来获取一些类加载器啊获取一些属性值属性值要用environment或者是bin factory就是我们的IOC容器等等这些第二个呢metadata
[17:20] 原数据对象这个原数据呢是来获取注解的属性值的这个我们自定义说完了第二个呢条件判断那么条件判断呢这个地方呢我们就需要使用conditional这个注解把我们的条件类放里边去它来满足对应的matches这个方法会被自动调用那么当然我们基本上一般我们都不用自己定义的因为Spring Boot给我们提供了很多常用的比如说condition on property
[17:50] 可以来判断配置文件里面是否有对应的属性值才初始化对应的bincondition on class判断环境里面是否有字节码文件才初始化对应的bincondition on missing bin就是判断你IOC容器里面没有这个bin才初始化对应的一个bin好嘞那么对于condition这个功能我们就介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Boot 自动配置中的条件化 Bean 创建机制，通过 @ConditionalOnClass 等注解实现根据类存在与否动态创建 Bean。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 项目结构显示 `src/main/java/com.ithema.springbootcondition/config/UserConfig.java`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition.config;
  import com.ithema.springbootcondition.condition.ClassCondition;
  import com.ithema.springbootcondition.condition.domain.User;
  import org.springframework.context.annotation.Conditional;
  import org.springframework.context.annotation.Configuration;
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      public User user() {
          return new User();
      }
  }
  ```

画面 2:
- 项目结构中选中 `UserConfig`。
- 代码内容：
  ```java
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("redis.clients.jedis.Jedis")
      public User user() {
          return new User();
      }
  }
  ```

画面 3:
- 项目结构中选中 `SpringbootConditionApplication`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition;
  import ...
  @SpringBootApplication
  public class SpringbootConditionApplication {
      public static void main(String[] args) {
          // 可以看到注释掉的代码
          // @Bean redisTemplate
          // Object redisTemplate = context.getBean("redisTemplate");
          // System.out.println(redisTemplate);
          ConfigurableApplicationContext context = SpringApplication.run(SpringbootConditionApplication.class, args);
          Object user = context.getBean("user");
          System.out.println(user);
      }
  }
  ```

画面 4:
- 项目结构中选中 `SpringbootConditionApplication`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition;
  import ...
  @SpringBootApplication
  public class SpringbootConditionApplication {
      public static void main(String[] args) {
          ConfigurableApplicationContext context = SpringApplication.run(SpringbootConditionApplication.class, args);
          Object user = context.getBean("user");
          System.out.println(user);
      }
  }
  ```

画面 5:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName("redis.clients.jedis.Jedis");
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 6:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName("redis.clients.jedis.Jedis");
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 7:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 获取注解属性值
          Map<String, Object> map = metadata.getAnnotationAttributes(ConditionalOnClass.class.getName());
          String value = map.get("value");
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName(value);
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 8:
- 项目结构中选中 `UserConfig.java`。
- 代码内容：
  ```java
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("redis.clients.jedis.Jedis")
      public User user() {
          return new User();
      }
  }
  ```

画面 9:
- 项目结构中选中 `pom.xml`。
- 代码内容：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
  </dependency>
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-redis</artifactId>
      </dependency>
  </dependencies>
  ```

画面 10:
- 项目结构中选中 `pom.xml`。
- 代码内容：
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-redis</artifactId>
          <version>2.1.8.RELEASE</version>
      </dependency>
  </dependencies>
  ```

画面 11:
- 项目结构中选中 `ConditionalOnClass.java`。
- 代码内容：
  ```java
  @Target({ElementType.TYPE, ElementType.METHOD})
  @Retention(RetentionPolicy.RUNTIME)
  @Documented
  @Conditional(OnClassCondition.class)
  public @interface ConditionalOnClass {
      Class<?>[] value() default {};
  }
  ```

画面 12:
- 项目结构中选中 `RedisAutoConfiguration.java`。
- 代码内容：
  ```java
  @Configuration
  @ConditionalOnClass(RedisOperations.class)
  @ConditionalOnBean(RedisConnectionFactory.class)
  @Import({LettuceConnectionConfiguration.class, JedisAutoConfiguration.class})
  public class RedisAutoConfiguration {
      @Bean
      @ConditionalOnMissingBean
      public RedisTemplate string(RedisConnectionFactory redisConnectionFactory) throws UnknownHostException {
          StringRedisTemplate template = new StringRedisTemplate();
          template.setConnectionFactory(redisConnectionFactory);
          return template;
      }
  }
  ```

画面 13:
- 项目结构中选中 `UserConfig.java`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition.config;
  import com.ithema.springbootcondition.condition.ClassCondition;
  import com.ithema.springbootcondition.condition.domain.User;
  import org.springframework.context.annotation.Conditional;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.Bean;
  import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("com.alibaba.fastjson.JSON")
      public User user() {
          return new User();
      }
      @Bean
      public User user2() {
          return new User();
      }
  }
  ```

画面 14:
- PPT 标题：Spring Boot 自动配置。
- PPT 内容：
  - Condition
  - Condition 是在 Spring 4.0 增加的条件判断功能，通过这个功能可以实现选择性的创建 Bean 操作。
  - 思考
  - Spring Boot 是如何知道要创建哪个 Bean 的？比如 Spring Boot 是如何知道要创建 RedisTemplate 的？

