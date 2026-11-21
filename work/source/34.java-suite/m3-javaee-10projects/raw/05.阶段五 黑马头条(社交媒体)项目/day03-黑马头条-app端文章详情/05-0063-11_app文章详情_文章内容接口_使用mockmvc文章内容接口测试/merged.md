# 11_app文章详情_文章内容接口_使用mockmvc文章内容接口测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\11_app文章详情_文章内容接口_使用mockmvc文章内容接口测试【海量资源尽在 666java.com】.mp4
- 时长 12分6秒（音频 726s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那咱们下面就来去测试一下那咱们该怎么去测试呢咱们第一天的时候其实是用的是单元测试直接测试的是Service那我现在想去用另外一种方式去测试我想去测试当前这个接口到底能不能用那这个测试其实有很多是吧就在咱们之前学过的比如说咱们用Postman用Swagger其实都能测今天咱们再介绍另外一种方式叫MOOC MVC
[00:28] 让它去测试这个呢是通过编写代码的方式去测试咱们的接口到底是否能通好那咱们就还是在单元测试里边去定义啊还来看一下怎么定义在这去创建一个类放个点黑码点什么叫什么呀然后是Controller我们直接去测试controllerV1点什么叫articleA-R-T-I-Z-R-V是吧info Controller
[01:10] 好test好吧好这个类是创建出来的创建之后咱们需要去把这环境给继承一下首先是Spring Boot test这东西是少不了的好第一个是class然后是article然后是然后是什么runways是吧写的很多了叫spring runner class
[01:45] 好咱们下面刚才说了使用一个什么来着使用MOOC MVC测试那是谁提供的呢是Sprint框架提供的所以说首先要想去使用的话你首先得开启MOOC测试那开启怎么开启呢这有个诸解叫什么Auto Configuration MOOC MVC它就是Sprintboot提供的好那这个
[02:14] 拉进来之后呢那下面就可以去注入一些东西那注入啥呢注入Service吗不是咱们需要去注入一个moke好看一下啊他自动的他已经帮你维护了啊moke就是这个啊好moke好吧等一会用他呢去进行测试还有一个啊嗯咱们一会再说吧好吧public
[02:40] 直接 void 然后是 testload什么的articleinfo好吧行就这么写然后呢然后咱们就可以直接去调用了那调用该怎么调用呢其实里边有一个静态方法就是叫mokemvcrequestloader这里边呢其实有很多方法比如说host还有什么delete还有什么get
[03:13] 好咱们看一下咱们的控制了是啥啊这一块是个pulse是吧刚才我好像我没有定义是吧我后加后加的啊这是一个pulseok注意啊刚才没有写是一个pulse mapping我这边是一个pulse请求所以说你再去写测试的时候应该写哪个呀很显然是什么pulse吧pulse啊那这里边呢就是你的url这个url是啥呢看一下啊就是dpi d article然后是load article infook
[03:45] 直接放到这然后是load article最终咱们可以去在一个点里边咱们可以再去设置一些参数类型哪些类型你看首先有一个content type这个其实就是你如果你要从前台去往后台去传数据的时候是不是要指定类型的
[04:13] 在这咱们也可以指定咱们的请求的类型咱们的类型都可以用MediaType里边有一个什么PPApplicationJsonValue就用这种方式你看它的其实你可以看一下它的其实就是Application-Value好了这里边还没有完最终咱们请求方式你是不是还有参数参数的话你可以继续玩是有一个档
[04:43] 这个参数呢你可以去传一个content传的格式是啥呢格式就是json的所以说啊咱们现在需要再去传一个参数那这个参数的话咱们还还还需要看一下目前是不是article info dto啊可以说啊你在这创建一个类叫dto然后设置一个参数啊咱们就设置一个叫什么来着article id好吧就设置为1啊因为目前的话呢在你们的数据里边呢有一个数据
[05:17] 这个1的数据呢content里边content啊找一下content里边呢是有一条数据是1那这个1呢是测试数据一般是不会删除的啊就咱们就一般测的时候就测1就可以了啊好那这个设置完之后呢咱们在这儿就可以直接去把它放进去放进去之后呢你会发现还是不错是吧因为啊这种内容呢它需要去接受有什么什么参数啊是一个string或者是一个字节数组
[05:47] 那这时候咱们需要去转换一下把当前对象转成JSON怎么转这个很简单我们可以用当前的JSON去做用object-mypro我们可以用它好mypro好吧直接注入就可以了因为咱们在项目中已经集成了它所以说直接mypro-rate-value-as-metas就可以了dtook那这样就结束了它可以去返回一个builder
[06:22] 好这不是还报错吗报错需要去抛出一场一场给抛了抛一个大的好吧省得再报错那抛完之后呢咱们现在就可以去发请求了这时候还没有发请求你需要去用一个mvc什么呢而里边有一个叫perform好这时候这里边你就可以去装一个boot然后咱们就可以去再往后去设置一些参数那这个参数的话其实都是一些返回参数了
[06:54] 反复的参数咱们可以去看一下笔记这个就是比较固定的了啊就是不会说用其他的因为咱们最终是拿到当前这个参数啊这个这个反回的状态之后呢最终把这个把这个数据给打印一下就完事了啊好我把最后一句话都考过来到了啊最后一句话基本上不用不会改啊要改的话有可能是在你以后再去测试的话有可能你的
[07:23] 路径不一样你的参数有可能不同所以说你要改的地儿就是当前参数或者说你的当前的一个请求的URL路径好吧行那咱们下面的就来可以去测试一下好我们可以走一下看看能不能行咱们写的当前的Controller也可以在这打转点看看能不能过来好走稍等好来了来了之后咱们可以看一下当前的DTO有没有拿到数据是吧这个DTO没有拿到数据是吧
[08:15] 没有拿到数据的话这个呢咱们还是少一个参数啊咱们先把它停了啊然后这块呢是需要去加一个什么request body是吧因为咱们接收的是啥数据啊是json你需要把json转换为do是吧这个老旺是吧行咱们再来测一下啊好再去加一个再去debug执行一下看看看看效果好正在运行稍等好来了看看这个参数有没有拿到啊
[08:59] 当前参数1是不是拿到了好咱们直接放行啊直接放行看看这个效果就可以了啊放行然后看看当前有没有拿到请求到数据啊这个数据的话来往下看往下走往下走往下走啊你看这块是不是他请求的是response是一个200啊是不是这里边是不是操作成功最终咱们数据是不是拿到了这个content是不是拿到了啊啊content id是个1然后下面是有一个这个content的内容好像是当前的一个
[09:29] 编码之后的东西是吧那这个呢咱们需要去把它解码啊需要解码那解码的话呢这个因为呢是现在你们的数据啊存的时候呢都已经编完码了是有一个64位的编码啊这个编码之后呢效果呢就是在爬虫爬数据的时候啊咱们后期会去学会去用啊所以说呢在这个内容呢我给你们的数据里边呢都是一些编码之后的内容所以说你这会儿你要想去在前台正常显示的话呢这个代码还要再去微调一下这样调呢
[09:59] 就是在当前装入content之前呢咱们需要把这个content这个内容呢去稍微调一下调的话呢其实很简单就是这里边啊在当前的有一个叫做youtube包下边youtube这个工程下边有一个工具类就是有一个ZIPyoutube里边是有一个压缩的一个命令还有一个啥呢还有一个是解压的一个方法好那咱们就去直接调用解压这个方法就可以了啊
[10:29] 好在这去加一下叫ZIPQtusR就是这个这是解压解压谁呢解压当前里边的content对解压就是content啊解压完content之后呢咱们需要再重新装入当前的什么东西重新装入当前的对象里边是吧所以说呢咱们在这啊再去设置一下set content那就是content这样这样解压之后呢
[11:02] 我们再来看一下效果看看行不行啊好咱们再来去左一边走执行看看最终能不能拿到当前文章的内容稍等不出意外的话啊应该是能够打印出来当前文章的一些文字信息好把这个断点放掉啊直接放行就可以了啊好成功了是吧好看一下啊操作成功没有问题往下走你看这块你看这个汉字是不是就已经编码之后的汉字啊
[11:44] 这时候这个内容就已经拿到了OK那这个咱们测试就算是做完了这里边主要是讲了一个内容就是当前的哪个当前的一个MOOC MVC大家应该熟悉这种写法最主要的就是这块内容你怎么去设置你的URL怎么去传参好吧行那这个咱们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何为 Spring Boot 项目中的 ArticleInfoController 编写并执行单元测试，重点演示了使用 MockMvc 模拟 HTTP 请求并验证服务层逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 ArticleInfoController.java 中的 @PostMapping("/load_article_info") 方法，用于加载文章信息。
画面 2: 展示 ArticleInfoControllerTest.java 的测试类，使用 @SpringBootTest(classes = ArticleJarApplication.class) 和 @RunWith(SpringRunner.class) 注解。
画面 3: 展示测试类中使用 @AutoConfigureMockMvc 注解，用于配置 MockMvc。
画面 4: 展示测试类中导入 MockMvc 和 MockMvcRequestBuilder 等类。
画面 5: 展示测试方法 testLoadArticleInfo() 中创建 ArticleInfoDto 对象并设置 articleId。
画面 6: 展示测试方法中使用 MockMvcRequestBuilders.post() 构建 POST 请求。
画面 7: 展示测试方法中使用 .content(Mapper.writeValueAsBytes(dto)) 设置请求体。
画面 8: 展示测试方法中使用 mvc.perform(builder) 执行请求。
画面 9: 展示调试器中 ArticleInfoController 的方法执行过程，参数 dto 和 appArticleInfoService 被赋值。
画面 10: 展示测试执行后的控制台日志，包含 Hibernate 初始化信息。
画面 11: 展示测试执行成功后的控制台输出，显示响应状态码 200 和响应体。
画面 12: 展示 AppArticleInfoService.java 中的逻辑，根据 articleId 查询配置信息。
画面 13: 展示测试执行后的控制台日志，包含 Hibernate 初始化信息。
画面 14: 展示测试方法中设置请求体的代码，使用 .content(Mapper.writeValueAsBytes(dto))。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
@RestController
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {

    @Autowired
    private AppArticleInfoService appArticleInfoService;

    @PostMapping("/load_article_info")
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

画面 2:
```java
package com.heima.article.Controller.v1;

import com.heima.article.ArticleJarApplication;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
@SpringBootTest(classes = ArticleJarApplication.class)
public class ArticleInfoControllerTest {

}
```

画面 3:
```java
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = ArticleJarApplication.class)
@AutoConfigureMockMvc
public class ArticleInfoControllerTest {

}
```

画面 4:
```java
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
```

画面 5:
```java
public void testLoadArticleInfo() {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 6:
```java
public void testLoadArticleInfo() {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 7:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 8:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 9:
```java
public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
    return appArticleInfoService.getArticleInfo(dto.getArticleId());
}
```

画面 10:
```java
2019-09-19 19:23:37,833 | INFO  | main | org.hibernate.jpa.internal.util.LogHelper | logPersistenceUnitInformation | HHH000224: Processing PersistenceUnitInformation
name: default
```

画面 11:
```java
Attributes - null
MockHttpServletResponse:
Status - 200
Error message - null
Headers - {Content-Type=[application/json;charset=UTF-8]}
Body - {"host":"null","code":"0","errorMessage":"操作成功","data":{"id":1,"articleId":1,"isComment":true,"isForward":true,"isDown":false}}
Redirected URL - null
Cookies - []
```

画面 12:
```java
//根据文章id查询配置信息
ArticleConfig apArticleConfig = apArticleConfigMapper.selectByArticleId(articleId);
if (apArticleConfig == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
} else if (apArticleConfig.getDelete()) {
    ArticleContent apArticleContent = apArticleContentMapper.selectByArticleId(articleId);
    String content = ZipUtils.gunzip(apArticleContent.getContent());
    data.put("config", apArticleConfig);
    data.put("content", content);
    return ResponseResult.okResult(data);
}
```

画面 13:
```java
2019-09-19 19:25:49,814 | INFO  | main | org.hibernate.Version | logVersion | HHH000012: Hibernate Core (3.3.10.Final)
```

画面 14:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

