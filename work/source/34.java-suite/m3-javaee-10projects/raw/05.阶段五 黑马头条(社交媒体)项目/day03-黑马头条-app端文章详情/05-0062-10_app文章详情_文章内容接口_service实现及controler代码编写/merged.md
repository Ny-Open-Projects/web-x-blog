# 10_app文章详情_文章内容接口_service实现及controler代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\10_app文章详情_文章内容接口_service实现及controler代码编写【海量资源尽在 666java.com】.mp4
- 时长 7分31秒（音频 451s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就把当前这个Service这个实现列给写一下啊刚才咱们已经分析了啊说是要走两步是吧第一步咱们要根据当前ID文章ID去查询config的信息如果说它没有被删除的话呢咱们就把config跟content都要返回就可以了啊那时候呢咱们首先呢应该第一步首先应该判断一下当前那个article id到底是否为空是吧我说它等于等于空
[00:29] 或者是啥呢或者说RTG ID小于1应该小于1吗自身的主件应该是没有小于1的所以说如果说一旦有的话咱们就直接去看一个破误信息就可以了raise without error找里边的咱们可以去写一些enumerpp里边有http code enumer里边咱们有一个参数错误就第一个好
[00:58] 说是一个参数错误就可以了然后这时候如果他没有问题的话咱们再去查询当前config的信息那Map文件呢咱们已经有了啊所以说在这儿去注入首先注入第一个就是当前的什么AP article有一个on tink map好这是一个啊还有第二个是吧第二个的话也是他AP articleon tink map好吧把它也给注入一下
[01:37] 这里边是不是黄线报警告啊这叫红线警告是吧警告的话之前咱们说过是吧在这去加一个COPER warning啊不舒服的话就加上好那这个就没有了啊然后这时候咱们就可以查询了啊首先是查询configslack的by article id就是根据当前的文章it去查询查询完之后呢这个config信息啊就有了
[02:04] 然后这时候咱们就可以去判断了那判断怎么判断呢首先咱们要去判断一下如果说它等于none如果说它等于等于none的时候咱们也会去返回一个错误信息就是当前的这个东西一模一样的然后如果说它不等于none但是它里边还有个什么东西要判断什么先文章是否删除是吧怎么判断的你可以去cp article config.at list delete
[02:38] 看它是否删除是没有删除是非然后这时候呢我们再去做操作我们操作呀就是把当前的content信息给查出来是吧content是不是用它呀好.slack还是它.id好是.ok那这时候我们的content信息就有了但是咱们进行介绍的时候说了啊这时候呢咱们应该返回两步的内容一个是content另外一个是config这时候咱们
[03:08] 应该上一个什么东西装下来让一个map去装这两个东西最终把map的信息给返回过去就可以了好吧所以说咱们在这再定一个mapmap里边呢是有一个script object这个导游包我们叫date好吧就一个hc map好那设完之后呢咱们在这就可以去加进去了date.pose好第一个是on turn然后
[03:39] 把当前的AP article content放进去就完事了当然了这块呢你还要再装一个叫date点什么把这个config信息也应该装进去AP OK就它这个装进去之后啊然后咱们最终再去返回一个response result.o然后是result然后是把当前的date装进去OK那这个Service我们就算是点完了好吧
[04:09] 那写完之后呢咱们下面呢就来去往下写咱们再去定义一下接口的Controller那接口在哪定义啊接口是不是统一咱们都会去在当前的APIS里边去做呀所以说啊还是在这去做啊咱们在这啊再去创建一个类这个类叫啥呢叫AP啊叫article infer好吧好嗯是个接口
[04:37] 咱们可以看笔记看看到底叫什么名叫ArticleInfoControlAPI是吧好把它拷过来OK创建完之后这里边是有什么方法吗是不是有一个方法一个方法就是去加载当前的什么首页的应该是不是首页应该是文章详情的信息对吧好往下看这时候咱们方法去写一个public然后下面是什么
[05:13] thisbouncewithout是吧咱们统一都会返回当前这个东西然后咱们起个名字叫loadarticle是info好吧条件是啥呢条件条件就是当前的articleinfo好dto因为这里边封装了当前的一个article id好那这个创建完之后咱们要去创建对应的Controller信息了这时候咱们首先是在当前的article里边去定义一个接口
[05:44] 叫Controller然后在这去创建一个Controller已经存在了吗我看看存在的话咱们就删了好吧我之前做测试好咱们再自己创建一下然后让它去实现当前的什么APIOK好那这个就做完了这里边咱们首先要去设立一个rest Controller然后是request mapping在mapping里边
[06:22] 该怎么去写呢这个呢其实呢你还要去看前的接口的定义这里边是不是有一个APIBI article其实还是他好粘过来然后这里边咱们需要去注入Service去调用就可以了然后是private然后怎么着是APIBI article.cre Service没有什么info没有吗我看这个什么名
[06:59] App是吧App articleinfo Service就它这时候你要去注入进来叫outware好然后是用一下要用的就是当前的只有一个方法叫get articleinfo然后传的是一个gto的什么article idok那这样的话咱们就算是把当前的Controller也给写完了行那这个写完之后咱们下面就来去测试一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现文章信息的查询服务，包括服务层的参数校验、配置与内容映射，以及控制器层的接口定义与调用。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 AppArticleInfoServiceImpl.java 中，对 articleId 参数进行初步校验，若为空或小于1则返回错误结果。
画面 2: 在 AppArticleInfoServiceImpl.java 中，添加了 articleId 的非空和小于1的校验逻辑。
画面 3: 在 AppArticleInfoServiceImpl.java 中，引入了 @Autowired 注解，并声明了 apArticleConfigMapper 和 apArticleContentMapper 两个私有成员变量。
画面 4: 在 AppArticleInfoServiceImpl.java 中，为两个 Mapper 接口变量添加了 @Autowired 注解。
画面 5: 在 AppArticleInfoServiceImpl.java 中，为 apArticleConfigMapper 变量添加了 @Autowired 注解。
画面 6: 在 AppArticleInfoServiceImpl.java 中，为 apArticleContentMapper 变量添加了 @Autowired 注解。
画面 7: 在 AppArticleInfoServiceImpl.java 中，声明了一个 Map<String, Object> 类型的 data 变量，并开始编写业务逻辑。
画面 8: 在 AppArticleInfoServiceImpl.java 中，完成对 apArticleConfigMapper 的赋值和校验逻辑。
画面 9: 在 AppArticleInfoServiceImpl.java 中，完成对 apArticleContentMapper 的赋值和校验逻辑。
画面 10: 在 IDEA 中，右键点击 com.heima.article 包，选择“Create New Class”创建新类。
画面 11: 在 IDEA 中，右键点击 com.heima.article.Controller.v1 包，选择“New” -> “Interface” 创建接口。
画面 12: 在 ArticleInfoControllerApi.java 中，定义了接口方法 loadArticleInfo。
画面 13: 在 ArticleInfoControllerApi.java 中，为 loadArticleInfo 方法添加了 @RequestMapping 注解。
画面 14: 在 ArticleInfoController.java 中，为 loadArticleInfo 方法添加了 @RequestMapping 注解，并调用 Service 层方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.heima.article.Service.impl;
import com.heima.article.Service.AppArticleInfoService;
import com.heima.model.common.dtos.ResponseResult;
import org.springframework.stereotype.Service;

@Service
public class AppArticleInfoServiceImpl implements AppArticleInfoService {
    @Override
    public ResponseResult getArticleInfo(Integer articleId) {
        //根据文章id查询config的信息
        //判断当前文章是否删除
        return null;
    }
}
```

画面 2:
```java
if(articleId == null || articleId < 1) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 3:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 4:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 5:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
```

画面 6:
```java
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 7:
```java
Map<String, Object> data = new HashMap<>();
```

画面 8:
```java
if(apArticleConfig == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 9:
```java
else if(!apArticleConfig.getIsDelete()) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 10:
```java
// Create New Class
Name: 
Kind: Interface
```

画面 11:
```java
public interface ArticleInfoControllerApi {
    public ResponseResult loadArticleInfo(ArticleInfoDto dto);
}
```

画面 12:
```java
public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
    return null;
}
```

画面 13:
```java
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {
    @Autowired
    private AppArticleInfoService appArticleInfoService;
    @Override
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

画面 14:
```java
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {
    @Autowired
    private AppArticleInfoService appArticleInfoService;
    @Override
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

