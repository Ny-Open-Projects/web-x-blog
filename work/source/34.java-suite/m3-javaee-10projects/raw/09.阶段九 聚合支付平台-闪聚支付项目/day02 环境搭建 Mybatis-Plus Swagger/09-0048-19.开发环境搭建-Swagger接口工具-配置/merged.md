# 19.开发环境搭建-Swagger接口工具-配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\19.开发环境搭建-Swagger接口工具-配置【海量资源尽在 666java.com】.mp4
- 时长 15分32秒（音频 932s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来讲一个工具啊接口开发相关的工具各位现在我们思考一个问题啊就是说我们现在把微服务开发完成啊比如说我们暴露给前端的微服务就是application应用的这个服务呢给他对吧然后呢我们说前端这个时候呢前端要调用我们的接口注意啊就是我们这个整个项目我们一直谈论接口接口的大家一定脑子里面清楚到底是哪些接口对不对
[00:29] 我们知道我们暴露给前端的接口一定是一个RESTful的接口就是应用这个工程application里边去暴露的所以以后我再说这个application大家都知道是暴露的给前端的这些RESTful的接口我们又说了另外一道接口就是double服务的接口我们再说就是微服务的接口就是double服务的接口我们指的就是刚才我们写的三户服务这套接口
[00:59] 对吧好那现在我们说问题来了前端要调我们的接口前端说你给我吧把你们的接口文档给我吧为啥要接口文档因为前端要知道他怎么调你你比如说刚才我们去测试我们说你给我传商户的ID你就按照这样的URL给我传然后呢我给你返回这个商户的信息那我问你前端他是不是得要你的文档呀对吧什么是文档就是你得给我写清楚呀你让我
[01:29] 怎么调你的接口你不能光口头说所以这个时候呢我们就需要一个什么对接口文档了前后端分离开发最重要的就是这个接口文档因为大家都依据这个接口文档来进行开发这就是前后端开发的规范对吧这个时候呢我们说那文档谁来写呢对不对那前端说你看服务端你的接口写好了那你来写呀
[01:56] 那服务端说你看我开发完了之后对吧我就是定义了一个Controller接口我还得写文档这挺麻烦的所以这个时候呢我们就需要一个工具来帮助我们生成这些接口文档给前端开发人员去用这个工具呢就是叫Swagger那Swagger呢它就是一个可以自动的生成RESTful接口的这么一个开发工具
[02:24] 这是他的官网大家回头可以看一下那么有了这个文档各位前后端分离开发他们的团队协作是不是就效率就提高了前端是不是就可以依据你给他的文档来进行开发了好那现在我们看吧有人说老师那咋生成量因为我们说既然是工具肯定是好用的也就是你只管写你的Controller你写完Controller之后这个工具它就帮你生成文档了对那怎么做看好
[02:52] 这个SWAG跟着这个怎么样我们是不是用的Spring Boot这个架构对它基于Spring Boot这个框架它可以你只要把这个依赖包加进去它就帮你生成什么文档了看好我们在这加就是你现在要生成的接口文档是不是基于Ctrl生成的我们暴露给前端的这些Restful接口的文档所以你要在Application当中来把这个依赖加进去
[03:21] 那这个依赖呢各位我们往下翻别我们加重了因为当初我们这个依赖当中看好啊没有啊没有我就考进去了OK吧这是SWIGER的依赖SWIGER依赖注意它是怎么样生成接口文档呢我要跟你说一下它的原理啊它会扫描你的这个control这个包下边你建立的这些control类
[03:45] 里边各位你是不是都标记了一个叫rest Controller的注解那他就扫描到这个注解扫描到这个注解他就扫描到你里边的方法甚至你方法上面的get mapping这些注解从而就拿到你的URL以及你的参数各位这就是他的工作原理啥意思就是扫描你的Controller类然后解析你的类名类路径URL路径等等然后帮你生成文档所以
[04:14] 你肯定要配置一下吧你肯定告诉Swagger你扫描我哪个包吧对所以我们如果要在哪个工程生成Swagger文档你就需要在哪个application工程当中来配置一下Swagger知道了吧这个好像弄错了配置的话我们统一都是加一个config然后在这个里边我们写一个配置类对吧
[04:44] 这个配置类各位不需要大家去手写因为这个配置类就跟我们当初配插描一样它就是一个配置对不对所以我给大家说它这里边有哪些东西就行了注意看这里边我们来看一下它需要引入哪个东西它是运错了现在我们把这个配置就加进去了然后注意看这里边
[05:15] 大家需要注意的点就是它你看我现在是不是在merchant的这个application工程当中来生成结构文档是吧所以它要扫描这个包下边的然后呢control这个包下边的什么所有的control类所以你这个包路径你得注意是吧然后你还需要注意更改哪个东西呢你比如说它
[05:41] 你看见吗这就是一个title就是你这个文档上面就跟你写一个word文档上面有一个标题一样这是你的标题这标题叫闪具支付商户应用API文档看见吗对所以这个呢可能你也需要改将来你给人家前端会给他一个标题对不对其他的比如说开发者或者啥这就是小case了不用管了所以其他的各位都不用管主要是包路径和标题你写好
[06:06] 然后这时候呢有人说老师那还要怎么弄啊还要注意一个配置啊这个注意这个配置你也需要改就是这个Sweiger所生成的这个文档可以通过http来访问就是直接访问你这个Machine的Application工程某一个URL那它这个URL呢其实你比如说它呢是有一定路径的就这个Sweiger生成的URL你比如说是Sweiger-uihtml但是我们将来可能会加一些什么
[06:34] 认证授权之类的拦截器这时候呢你把人家拦住了这个文档是不是就不能访问了所以啊你需要给他创建一个针对这个什么呀可以访问你Swagger这些URL的一个指定这个具体的一个什么配置类这个配置类呢注意我们也不需要去掌握你只要知道怎么配就行了来看一下啊很简单大家来看
[07:02] 那这个配置类呢就是告诉我们的啊Machine的application啊凡是访问这个URL的看见了吗哎统一location到这儿统一到这个地址来访问哎所以其实这也是基于我们说的这个SWAG啊他给我们提供的这些URL呢我们根据自己工程的特点让他指定到具体的地方哎说这个配置类呢我们也配好了好那么我们把这些配置类配好了之后呢这个时候我们就可以重启
[07:32] 看好重启完了之后我们接下来就能访问我们Swagger给我们生成的文档了看好老师咋访问呢看好他前面的路径不用动这是他的什么content pass然后后边就是他的Swagger-ui.html这时候就拿到了看拿到了这时候拿到了是不是就是我们说的这是一个标题对不对有时候老师他没有好像
[08:05] 出来了你看有个get你看见了吗这就是我们的一个他扫描到我们的这个马尔信的Controller里边的某一个方法了你看他这个方法他这个方法是不是就是一个叫-marxist下边是传一个三货ID看见了吗这就是一个接口文档有人说老师这个接口文档除了这个标题我看的是中文好像没有几个中文对吧
[08:30] 那其实中文不中文不重要重要的是你对这个接口的描述到底清晰不清晰你比如说这个接口到底是个啥意思嘞所以你是不是得告诉前端人员呀对不对所以这个时候我们说那怎么实现SWAG给我们提供了一些注解就是你啊只要把这些注解定义到我们的control内以及方法上它就能够
[08:53] 更加详细的来描述我们这个方法它的是实现了什么功能以及参数实现了什么你举个例子你比如说这个这个组件它可以修饰整个我们的这个Controller接口Controller内那你啥意思啊看好啊我在这加了看好我就在这加这是不是就是swegg你看我加完了之后你干嘛这里头有啥呀我们瞧一瞧它这里头有啥你看有value啊有text啊还有一个什么
[09:23] 有一个discretion是吧好那我随便加一个东西其实有时候我们搞技术开发有很多东西不是说非得是我知道它是啥意思了我才去写其实有时候我们可以尝试着去写一下你比如说我们就这个叫商户的什么商户平台应用的借口对吧然后看好我就把它重启了我就看一下它的效果你懂
[09:53] 老师的意思吧就是你要敢于去尝试不要非得去知道他们每一个注解的意思你要敢于去尝试OK那么弄完了之后呢我们刷新来看这时候呢我们来看有人说老师好像没有效果呀对不对对没有效果但是你别忘了他这里头好像好多注解了呀好多属性了是不是啊那我们是不是就可以三户平台应用的借口那边还有一个叫discretion看到吗看到吗对吧
[10:25] 我尝试嘛我现在我也不知道他很多诸解他是啥意思呀对不对我要看一下他能不能去描述他这个接口啊能不能更加详细的去说明这个接口啊好那你这时候写完了之后呢我们刷新一下哦出来了三户平台应用接口大家看懂吗
[10:46] 好像大家看到点门道了是不是没错也就是说Swagger给我们提供了很多注解这些注解其实就是足以能够来详细的说明我们的这个接口你比如刚才我在这个类上面写了一个叫API的注解然后我指定了valuetag字包括这个怎么样discretion描述的它的一个相关的详细信息那么你会发现这儿它就能够
[11:12] 显示出来这个中文其实显示中文的目的就是为了详细的来描述这个接口对不对那说老师那这个方法这是商务平台应用的接口我想针对这个方法描述咋描述呢其实他也有你看他有一个接口叫有一个注解叫operation是吗operation是吗那其实我们也可以去这么去尝试也就是说啥意思他有很多注解我们根据老师给你提供的这些讲义
[11:42] 然后上面说明了这些注解的作用我们就完全可以在这里头去写了对不对你比如说它有一个对不对那我们就写这叫什么这叫根据ID查询商户信息我是不是写完了写完了之后来重启这样的话我们是不是就慢慢就会学习这个注解的使用其实我们在写这个
[12:09] 接口这个方法的时候你会发现其实我们就可以把这些注解写上去了你刷新我们来看你会发现哇有了根据ID查询商户信息是不是啊这就是我们说的这个Swagger注解的使用它的注解还有好多你看这些注解还有好多那后边我们用到哪个注解呢我们会给大家说那个注解其实这个东西我还是建议大家去尝试去首先去网上查资料其次
[12:38] 在你这呢去尝试自己去测试自己去看这个注解的作用不要等着老师给你一个一个的讲完你明白我的意思吧好那现在呢我们把这个注解大概呢我们就什么呀演示出来了吧虽然演示了两个简单的注解但是Swagger文档绝不是这么简单你现在看到的这个文档是不是就可以很清楚的知道你这个平台提供了哪些这个接口啊
[13:05] 那比如说你看我们讲义上我们随便又测又列了几个测试看好啊我把它复制过去也就是说这里边你看我们是不是只有一个方法比如这里边我考进去两个方法这个方法很简单你看就是个hello是吧测试的这里边也是swag的一个组结对吧还有这个是啥呢这个是hi是吧hi啥呀这是给你测试了吗让你看看它到底生成的这个
[13:28] 很多的这个方法的时候呢你看看这个Sweiger文档他呢都会把这些方法的描述呢在Sweiger文档当中给你显示出来你看好啊很有意思来刷新这种发现哎发现发现啥了发现都出来了所以也就是你control里边的方法是不是在这里边他都会给你都会给你生成他的描述包括这个注解
[13:56] 我在刚才是不是没有讲过那其实你就可以看一下他是他是他是啥意思呀对原来呀这个注解刚才你看到的是啥对姓名你看针对我们方法的参数他也可以定义他的详细描述是不是很强悍呀对这就是Swagger文档Swagger文档好那么刚才我们是不是就针对Swagger文档这块我们简单去
[14:23] 配置去测试了一下它生成的这个文档呀那具体的方法其实很简单只需要各位就在我们的依赖当中把SWAG的依赖加进去然后呢在configure里边把SWAG的这个configuration配上去看到吗然后呢配置configuration的时候注意这里头它的这个什么Controller包的路径要注意包括它的标题的说明还有就是我们要把这个web mvc configure这个也要考上去
[14:52] 这个注意啊后边每一个微服务工程这个webmvcconfigure基本上你都可以去重复用了但这个swaggerconfiguration这个你要注意包名的修改然后呢就是在Controller内当中首先在内上面用API这个注解来标识整个Controller到底是哪个方面的这个接口的信息描述写清楚第二就是每个方法上面也要写Swagger的注解这样我们就可以把整个的这个Controller内以及
[15:21] 方法所有的描述信息就描述清楚了好Swagger的文档这块呢我们先这个配置这一块就讲完后边呢我们来进行一个什么测试啊好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Swagger 以自动生成和展示 API 文档。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了项目结构，焦点在 `MerchantController.java` 中的 `@GetMapping("/merchants/{id}")` 方法，用于查询商户信息。
画面 2: 代码编辑器中高亮显示了 `@GetMapping("/merchants/{id}")` 方法，右侧显示了 Maven 依赖。
画面 3: 展示了 `pom.xml` 文件中添加的 Spring Boot 启动器依赖项。
画面 4: 代码编辑器中高亮显示了 `@GetMapping("/merchants/{id}")` 方法，右侧显示了 Maven 依赖。
画面 5: 展示了 `SwaggerConfiguration.java` 文件，其中配置了 Swagger 扫描的包路径。
画面 6: 展示了 `WebMvcConfig.java` 文件，其中配置了静态资源路径。
画面 7: 展示了浏览器中访问的 Swagger UI 页面，显示了 API 文档。
画面 8: 展示了 `SwaggerConfiguration.java` 文件，其中配置了 Swagger 扫描的包路径。
画面 9: 展示了 Swagger UI 页面，显示了 `GET /merchants/{id}` 接口的详细信息。
画面 10: 展示了 `MerchantController.java` 文件，其中定义了 `@GetMapping("/merchants/{id}")` 方法。
画面 11: 展示了 Swagger 文档中关于 `@ApiImplicitParam` 注解的说明。
画面 12: 展示了 `MerchantController.java` 文件，其中定义了 `@GetMapping("/hello")` 和 `@GetMapping("/hi")` 方法。
画面 13: 展示了 `pom.xml` 文件中添加的 Swagger 依赖项。
画面 14: 展示了 `SwaggerConfiguration.java` 文件，其中定义了 `buildApiInfo` 方法。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 1:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 2:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 3:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

画面 4:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 5:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.Controller"))
                .paths(PathSelectors.any())
                .build();
    }
}
```

画面 6:
```java
@Component
public class WebMvcConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/**").addResourceLocations("classpath:/");
        registry.addResourceHandler("/Swagger-ui.html").addResourceLocations("classpath:/META-INF/resources/");
        registry.addResourceHandler("/webjars/**").addResourceLocations("classpath:/META-INF/resources/webjars/");
    }
}
```

画面 7:
```html
GET /merchants/{id} queryMerchantById
```

画面 8:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.Controller"))
                .paths(PathSelectors.any())
                .build();
    }
}
```

画面 9:
```html
GET /merchants/{id} queryMerchantById
```

画面 10:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 11:
```text
@ApiImplicitParam属性：
属性      取值     作用
paramType  path    以地址的形式提交数据
```

画面 12:
```java
@GetMapping("/hello")
public String hello() {
    return "hello";
}

@GetMapping("/hi")
public String hi(String name) {
    return "hi " + name;
}
```

画面 13:
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

画面 14:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.Controller"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo buildApiInfo() {
        Contact contact = new Contact("开发者", "", "");
        return new ApiInfoBuilder()
                .title("商户平台API")
                .contact(contact)
                .version("1.0.0")
                .build();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 6:
标题: 1.7.2 配置 MyBatis-Plus
表格数据:
1.7.2.1 配置连接池 Druid
1.7.2.2 配置 MyBatis-Plus

画面 11:
标题: 2.1.3 Swagger常用注解
表格数据:
属性      取值     作用
paramType  path    以地址的形式提交数据

5) 不要评价画面美观，不要输出与课程无关的内容。

