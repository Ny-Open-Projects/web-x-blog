# day01-18-SpringBoot集成Swagger

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-18-SpringBoot集成Swagger_【海量资源尽在 666java.com】.mp4
- 时长 10分9秒（音频 609s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们是不是给大家介绍了一款神器SWAG对吧那它到底有没有这么神呢那咱接下来就得用一用检验检验看它到底有没有那么神那我们接下来就需要在Spring Boot当中集成SWAG然后去使用一下SWAG怎么集成呢我们也是有一个固定的步骤而且这个步骤呢跟你平时用其他的这个框架这个套路差不多第一步呢就是在破文件当中对已经有相关的依赖有哪个依赖呢我们刚才说了这个Spring是不是已经把SWAG
[00:31] 给引进来了而且起个名字叫springfox就引这个依赖整个呢是两块啊大家看这个简历就行这是一块叫springfox-swagger2还有一个叫springfox-Swagger-ui引这两个依赖就行给它引到碰碰键当中那我们一会呢测试到时候我们准备拿着这个consumer这个微幅工程进行Swagger测试所以说呢我们接下来就要打开它的碰碰键我们看这里边有没有引入
[01:01] 死白个相关的依赖对不对我们搜一下应该是没有是不是没有的话有些人说那老师我们把这个站过来是不是就可以了哎咱先不要着急啊为啥不要着急呢大家要看看看这个图以前的这个图这个图蓝色部分啊蓝色部分那我们刚才发现了卡修莫这个微服工程当中呢的确是没有引死白个依赖但是他会不会把依赖放到API工程或者放到恐怕工程里面
[01:35] 对我们要考虑这种可能性因为从这张图上来看我们前面讲过了就说如果他把SWAG的依赖放到API或者放到Coreman工程里边之后我们的其他微服务工程比如Customer还需要再引一遍吗不需要吧是不是这个关系咱以前说过那咱既然就去Coreman工程里边找一找看他里边到底有没有引入这个SWAG的依赖就在这呢上来就是对不对你看是不是咱刚才说那两个对不对那我们现在发现呢
[02:06] 火曼工程里边已经引入了sweag的UI那我问大家一个问题consumer还需要也不需要不需要了吗我们的consumer依赖了API而API工程就依赖了谁啊 恐慢所以说consumer不用演了啊不用演这需要大家注意的一个细节这是第几步啊这是第一步就是在碰面当中啊引入sweag相关的依赖那么依赖有了之后呢接下来第二步就是搞配置我们说了它跟你集成别的框架差不多这个配置呢也分成两块一块就是
[02:37] swing boot 的配置我念就这个application.properties还有一个配置呢是一个配置类啊两块配置呃那咱先找到这个配置我念吧application.properties打开那这里边呢跟swag相关的配置就这一行对就这一行很简单这行配置呢我们表面上看它的功能就是开启这个什么呀swag这个功能处是不是但是实际上这行配置呢也没那么简单啊这个值呢并不是你想象啊给个处
[03:10] 这个功能就开起来给个fos这个功能关闭也没那么简单啊他呢跟一会我们要讲一个配置类他跟配置类上的某一块这个配置是有关系的啊是有关系的呃当然了这个我们前面讲过Apollo了这个配置将来我们会放到什么Apollo上但是你不管放到哪这个配置这个代码还是这么写的啊他就这么写这是一块配置还有一块配置我们说了是不是一个配置类是不是这配置类呢我们放到configure这个包里边
[03:42] 大家看就是他叫swag configuration那这个配置类里边这个代码大家过一遍能看懂就行了不需要大家编写啊以后呢呃哪个微服工程你需要用到swag呢这一套东西啊或者这个配置类你直接粘过去就行了那这里边都有啥呢咱过一遍吧首先配置类上面是不是一定有at configuration这个注解啊我就不再说了然后呢接下来这样配置咱留到最后先跳去然后我们看这
[04:11] 这呢有一个注解这个注解呢是开启Swag的注解支持或者呢你可以认为这个注解是将来要扫描其他的Swag注解啥意思呢一会儿呢我们再讲这个Swag具体怎么用的时候呢你会发现Swag本身带有很多注解而且这些注解呢是要写到Controller里边写到Controller里边而他就负责扫描那些注解他通过扫描那些注解里边的内容从而生成文档生成我们想要的文档
[04:41] 然后呢这里边的话大家看一下这里边是不是还配了一个b对吧Dockit那这里边都干啥了你看直线6这一代法基本上固定写法然后这里边呢啊大家需要关心的一个是这个地方就是包上面这个包的一个一个基本的一个路径你看我是写到哪一层了啊你看cn.itcast.onecp2p啊是这cn.itcast.onecp2p啊你看我这个是特别基础的一个路径那为什么要写到这一层呢
[05:12] 你可以看看另外一个微服工厂Dataway网关你看它的包CN.EDCAS.1P2P然后从它再往后这一集它们的名字就干什么呀不一样你看这是第二consumer这是第二什么呀Dataway所以说呢我这个扫描就扫描到这个路径写到这一集是不是它包含的这个范围就非常大凡是CN.EDCAS.1P2P下面所有的包以及它的子宝里面的东西都能被扫描我们刚才说扫描什么呀
[05:41] 就扫描sweig的一些一些注解里边的内容扫描里边内容来生成文档但是你得告诉他一个路径基本的一个路径其他这些代表你就不用管主要是这个路径然后下边这些呢就是我们生成文档里边的一个基本的一些内容比如说我们这个文档得用一个标题对你这个文档你看我们这里边有没有标题我这边其实也有标题
[06:11] 哪个算是标题呢这个不是特别明显是不是其实我觉得你像这个这种东西就是标题这是一个string类对不对那我们这里边其实也有标题你看我这就是一个固定的一个标题啊咱生成的文档不就是咱咱这个p2p平台的这个API文档是不是这是一个描述信息这些你可以自己随便改然后这是什么呀什么联系人或者你可以认为是作者啊这谁生成了这个文档啊或者说是出租于哪个公司对不对
[06:42] 这个你可以写公司的名字都可以这是一个版本号自己给一个版本号就行这是配置类吧再次给大家强调一下一个是这个包的这个路径一个就是这些文档的基本信息可以给一下然后还没完我们还剩最后一个注解需要给大家讲就这个地方这个地方他非常关键其实这儿呢才是真正的这个开启sweg这个功能的一个开关而且我们刚才说了这个地方
[07:12] 他跟这儿是不是有关系是不是这关系呢有什么关系呢你看一眼你看这儿你看这个prefix这个值是sweagervalue里边值是enabre哎你也没有发现这两个值正好是跟这儿的两个这个单词是一样的这是凑巧了吗这么巧对不对那可不是啊可不是凑巧应该严格意见来说这儿两个地方的值应该是这儿这儿超过去就是要跟他保持一致
[07:43] 那这块代码到底是什么意思呢大家注意听了啊这一块配置的作用就是从application.properties这个配用件里面获取这个值获取这个值那获取这个值干嘛呢原来是获取这个值那就是来决定开启不开启此二个功能如果我获取到值之处我就开启如果不是处我就把它关掉也没那么简单它是这么设计啊你看这它后边是不是还给了一个值啊你看它是这么判断
[08:14] 他通过前面这块东西是不是可以取到配有链里边的这个值然后他拿着这个值呢跟这儿的值进行相等判断如果这两个值一样了就表示开启SWAG这个功能如果不一样了哈这个功能就没有开启什么意思呢看好啊我这儿给他值是出吧这儿给他值也是出吧他俩一样吗一样那现在SWAG的功能就表示开启那如果说我这儿给一个什么呀False注意我给成False了啊
[08:43] 如果给人fos但是这儿是什么呀处你他俩是一样吗不一样不一样这个功能就没开启明白什么意思吧哎他其实内部是这么子来来判断的啊之后给大家提一下当然了我们没有必要这个去去动这个东西我们一般都是开启什么呀死板功能但是但是大家注意了啊我们有的情况下也需要把死板功能关掉关掉
[09:10] 那原来就有点疑惑了这么神的一个东西你不想把它关掉对不对神奇我们要拿着去用那这有一个细节我要跟大家说一说Spagger这个东西我们一般是在开发过程当中要用它所起的作用我们前面已经说过但是一旦你这个项目上线了这个功能要关了一般都要关为什么因为它生成的文档里边包含有我们整个项目所有的这个接口或者所有的扛出来的一些这个访问路径各种访问这个信息对不对
[09:40] 这个很容易这个暴露出去就产生一些安全隐患所以我们开发完之后一旦上线了这个功能我们就要关了啊开发阶段我们是开着你看什么意思吧哎所以他这相当于是设计了一个开关啊这块呢啊这个代码我要给大家说一说说这就是整个吧我们要想使用swag我们得知道啊在spinbook当中怎么去集成swag其实很简单引用依赖搞一些配置就搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Swagger2 以实现 API 文档自动生成。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示项目结构，包含 `wanningzp-common` 和 `wanningzp-consumer-Service` 模块，IDEA 界面展示 Maven 项目依赖和目录结构。
画面 2: PPT 页面标题为“2.1.2 Spring Boot集成Swagger”，内容讲解引入 Swagger 依赖，展示 Maven 依赖配置代码。
画面 3: IDE 中打开 `wanningzp-consumer-Service` 的 `pom.xml` 文件，显示项目依赖，包括 `spring-cloud-starter-netflix-Eureka-client` 和 `spring-boot-starter-web`。
画面 4: IDE 中 `wanningzp-common` 的 `pom.xml` 文件，高亮显示 `springfox-swagger2` 和 `springfox-Swagger-ui` 依赖。
画面 5: IDE 中 `wanningzp-common` 的 `pom.xml` 文件，高亮显示 `springfox-swagger2` 和 `springfox-Swagger-ui` 依赖。
画面 6: IDE 中 `wanningzp-consumer-Service` 的 `application.properties` 文件，配置 Swagger 启动开关 `Swagger.enable=true`。
画面 7: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解和 `@EnableSwagger2` 注解。
画面 8: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `paths(PathSelectors.any())` 方法。
画面 9: JavaDoc 界面，显示 `String` 类的文档，解释其不可变性。
画面 10: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `ApiInfo` 的 `title` 和 `description` 字段。
画面 11: IDE 中 `application.properties` 文件，显示 `Swagger.enable=true` 配置。
画面 12: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解。
画面 13: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解。
画面 14: PPT 页面，标题为“2.1.2 Spring Boot集成Swagger”，内容讲解引入依赖和配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-Swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>com.netflix.hystrix</groupId>
    <artifactId>hystrix-javanica</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-Swagger-ui</artifactId>
</dependency>
```

画面 6:
```properties
# 应用程序名称
spring.application.name=consumer-Service
# 需要服务访问路径
server.servlet.context-path=/consumer
# 开启Swagger
Swagger.enable=true
# 日志配置
logging.config=classpath:log4j2-dev.xml
# spring 全局异常处理
spring.mvc.throw-exception-if-no-handler-found=true
# 中文乱码处理
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
# springCloud Eureka
Eureka.client.serviceUrl.defaultZone=http://localhost:53000/Eureka/
```

画面 7:
```java
@ConditionalOnProperty(prefix = "Swagger", value = "enable", havingValue = "true")
@EnableSwagger2 // 开启Swagger支持
public class SwaggerConfiguration {
```

画面 8:
```java
.paths(PathSelectors.any())
```

画面 10:
```java
.title("万信金融P2P平台-用户服务API文档")
.description("包含用户服务api")
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2: PPT 标题为“2.1.2 Spring Boot集成Swagger”，内容包括“1. 引入依赖”和“2. 在wanningzp_consumer工程的application.properties中配置Swagger的启动开关”。
画面 14: PPT 标题为“2.1.2 Spring Boot集成Swagger”，内容包括“1. 引入依赖”和“2. 在wanningzp_consumer工程的application.properties中配置Swagger的启动开关”。

5) 无。

