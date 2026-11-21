# day01-20-Swagger生成文档

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-20-Swagger生成文档_【海量资源尽在 666java.com】.mp4
- 时长 8分16秒（音频 497s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们在consumer这个微服务当中的Controller类里边已经把Swagger相关的这些注解是已经加进来了是不是你看这些都是那有了这些注解之后呢Swagger能不能生成我们想要的那个文档呢对不对那个文档长什么样呢那咱接下来就要试一试啊怎么试我们需要启动一下consumer这个微服务工程大家看consumer啊我启动一下
[00:29] 其实在微服启动的过程当中啊Swagger就已经开始工作了只不过我们目前是看不到效果我们可以关起来控制台看看有没有什么错误出来没有是吧你看端口号是53050没有问题那这个文档在哪呢已经生成了吗我怎么去看一看访问一下那这就需要通过谁啊浏览器啊为什么听过浏览器呢来稍等啊look host然后呢我们的端口号要改成
[01:04] 53050没错吧这是consumer的这个端口号然后敲consumer这个基本访问路径con sumer对吧没敲错吧然后后边再敲的这个东西是固定写法大家注意了怎么写呢Swagger-ui.html注意了Swagger-ui.html这个呢是固定写法那到现在大家才发现
[01:34] 原来我们之前说的这个文档它是一个网页吗不是word文档这时候你要注意了我们前面所说的它生成的这个文档其实是一个网页或者说是一个html文档我们敲回这大家看一下这就是我们千呼万唤使出来的什么呀对文档sweger生成的文档大概长这个样子其实就是一个网页那你看这里边像这些东西
[02:07] 你还有印象吗他是从哪来的这些东西这些东西从哪来的这个我不知道你有没有印象咱前面是不是讲过一个配置类你还有印象吧Spark配置类你看这里边是这些东西对不对你看就在这就是你看1.0.0版本号这些文字其实都是Spark扫描注解扫描出来然后生成生成到这个什么对HMW网页当中那然后呢这个
[02:37] 我们重点关心的不是这一块对吧我们重点关心的是控制了以边这些方法他的一些什么呀描述信息这信息在哪呢哎别着急大家看这consumer用户服务一片这个东西从哪来的用户服务一片是不是你看用户服务一片看到了吗哎他已经扫描到了这个什么呀类上面的这个注解的这个内容啊那方法上面我们配置的这些注解内容能扫到吗一脑大家看
[03:07] 这一点是能点出来两个方法能看出来吗其实这就是两个方法你看上去好像是两个路径对吧其实都是对应两个方法一个哈喽一个嗨你看是不是一个哈喽一个嗨然后你再看这写的是get post你应该能猜出来一个是get请求一个是什么呀post请求是不是为啥一个get一个post你看你这这是get mapping这是什么呀post mapping对这些注解斯坦克都认识然后你再看后边-哈喽-嗨-哈喽-嗨不就是
[03:36] 这俩地方的值吗对不对他都扫描到了然后后边什么测试哈喽测试看你看是不是这个珠节里边的这个值对不对你看他都扫描到了而且不仅如此啊你随便点进去一个你看比如说我们这个哈喽吧你看你点一下点进来之后呢这里边其实还有参数的信息啊当然咱这个哈喽是不是没有参数了这个方法没有参数还有啊你看这里边你看parameter是不是参数那边对吧你看name啊string啊
[04:07] 这个什么是required的这些东西包括这个姓名啊你看是不是都是扫描这些东西扫到对你看required的一处证明它是B填项你看这有这么一个标记红色的这个标记是不是你看这个姓名啊姓名不就是这个东西啊这个值啊是不是所以它就是通过扫描咱注解里边的这些内容扫描到之后呢它会帮我们生成这么一个网页出来这就是我们说的文档那大家看有了这个文档
[04:35] 那你看咱一开始讨论的那些痛点解决了吗我们前面说过哪些痛点比如说我要往control发个请求我得知道发什么请求get a repost我在知道往哪发请求请求路径是啥我得知道这个他有没有参数有没有反弹值有几个参数参数什么类型你看看你用不用打开这个什么这个工程一点一点再找找到这个代码然后在这翻翻翻用不用你只需要访问这个路径就行只需要访问这个路径就行
[05:06] 就打开了而且这个东西其实对于前端人员来说相对来说也是比较友好的你觉得前端人员看这个容易还是看这种东西容易是不是所以说这对前端人员相对来说也是比较友好所以说它是完全能够解决我们一开始说的那些痛点不仅如此不仅如Swagger还能做别的事什么事它还可以进行功能测试大家看这你看这有个按钮叫Try it out这什么意思
[05:37] 叫试一试对吧我一般就是说踹他一下是不是啊踹他一下踹他干嘛你点击一下试试呗然后你看这哎他说你你往这发请求的时候呢这有个参数你需要给个值这个值什么意思了性命那我们就根据这个意思给一个吧给一个什么呀小黑对不对随便写一个然后呢你再看下面有个按钮叫is cute什么意思啊执行运行其实当你点按钮的时候呢swegg就会往这发请求然后呢会把这个参数
[06:07] 给捎带过去其实说白了不就是往这发请求吗是不是就往这个地方发请求啊那看这个情形能发出去吗咱走走完了你往下走你看response是不是响应回来的内容啊你看这有个状态码200表什么意思啊200表成功吧然后这就是返回的内容返回的是这玩意儿吗嗨逗号小黑是吗当然是你看咱这个方案就是这么写的嗨逗号刚才传过来是不是小黑你看什么意思吧所以你会发现呢它不仅是
[06:36] 可以把我们想要的那些信息给你展示出来他还可以进行测试就是你可以通过他在这发请求进行功能上的一些测试所以我们看到这儿我们觉得这个他真的是很贴心的一个什么呀神器是不是这是我们把他到底是怎么用的是不是他这个文档到底长什么样这个文档里边都有啥内容怎么用我们整体给大家说了最后呢我们再
[07:04] 简单给大家提一提这个slug它大概的一个工作原理有的同学说老师我还是很好奇对吧它是在这个网页它是咋生成的其实这个很简单啊我们前面在讲的时候给大家说过当我们在启动这个微服工程的时候大家知道Spring它会扫描到这个配置类吧因为这个配置类上面是不是写的有这个configuration这个注解对不对它能扫描到这个配置类扫描到配置类它就能扫描到配置类里边的这个很多东西了对吧
[07:33] 包括开启这个注解支持啊这个开关也开着来对不对包括扫描这些东西那他扫描到这些东西之后你看这咱们配的是不是有一个路径他就会扫描这个路径下面比如说这个control对不对这扛着在不在这个这个包的路径下面在不在在吧那他就能扫描这个扛着扫描了扛着之后就能扫描到control里边的这些注解从而拿到这里边的这些值拿到这些值之后呢他就能帮我们把这些值生成到一个什么呀
[08:03] 网页里边然后在这呢我们就可以打开来浏览其实它大概就是这么一个过程这就是我们给大家讲的一个神器叫flag我们就给大家说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Swagger2 生成并测试 RESTful API 文档。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- IDE 界面显示 `ConsumerController.java` 文件，其中定义了两个 API 接口：`@GetMapping("/hello")` 和 `@PostMapping("/hi")`。
- `@ApiImplicitParam` 注解为 POST 接口的 `name` 参数添加了描述和必填约束。
- 项目结构中可见 `SwaggerConfiguration.java` 文件。

画面 2:
- 控制台日志显示服务已启动，端口为 53050，Eureka 服务注册成功。

画面 3:
- 控制台日志显示服务初始化完成，Spring Dispatcher 初始化成功。

画面 4:
- IDE 界面显示 `SwaggerConfiguration.java` 文件，其中 `private ApiInfo buildApiInfo()` 方法用于构建 API 文档信息。
- `ApiInfoBuilder` 设置了文档标题、描述、联系人和版本号。

画面 5:
- 浏览器显示 Swagger UI 页面，标题为“万信金融P2P平台-用户服务API文档”，包含 GET `/hello` 和 POST `/hi` 两个接口。

画面 6:
- IDE 界面显示多个窗口，包括 Swagger UI 页面和项目结构，表明正在演示 Swagger 文档的访问。

画面 7:
- 浏览器显示 Swagger UI 页面，展示 GET `/hello` 接口的详细信息，包括响应状态码 200。

画面 8:
- 浏览器显示 Swagger UI 页面，展示 POST `/hi` 接口的详细信息，包括参数 `name` 和响应示例。

画面 9:
- IDE 界面显示 `ConsumerController.java` 文件，高亮显示 `@ApiImplicitParam` 注解，用于定义 POST 接口的参数。

画面 10:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的“Execute”按钮被点击，准备发送请求。

画面 11:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的“Execute”按钮正在执行，页面显示“LOADING”状态。

画面 12:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的响应结果，包括 Curl 命令和请求 URL。

画面 13:
- IDE 界面显示 `SwaggerConfiguration.java` 文件，其中 `@ConditionalOnProperty` 注解用于控制 Swagger 是否启用。

画面 14:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的参数输入框中已填写“小明”，准备执行请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.springframework.web.bind.annotation.RestController;

@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() {
        return "hello";
    }

    @ApiOperation("测试hi")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
    @PostMapping(value = "/hi")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

画面 4:
```java
private ApiInfo buildApiInfo() {
    Contact contact = new Contact(name: "黑马程序员", url: "", email: "");
    return new ApiInfoBuilder()
        .title("万信金融P2P平台-用户服务API文档")
        .description("包含用户服务api")
        .contact(contact)
        .version("1.0.0")
        .build();
}
```

画面 13:
```java
@Configuration
@ConditionalOnProperty(prefix = "Swagger", value = "enable", havingValue = "true")
@EnableSwagger2 // 开启Swagger注解
public class SwaggerConfiguration {
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
            .apiInfo(buildApiInfo())
            .select()
            .apis(ScanHandlerSelectors.basePackage("cn.itcast.wanxing2p"))
            .paths(PathSelectors.any())
            .build();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

