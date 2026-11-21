# 19_app文章列表_接口代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\19_app文章列表_接口代码编写【海量资源尽在 666java.com】.mp4
- 时长 12分13秒（音频 734s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们继续往下讲啊下面呢咱们就来去定义一些接口那定义接口之前呢咱们把这个环境虽然是搭完了但这里边还少一步咱们把这一步给补全也就是说咱们在当前微服务加载的时候应该是要去查询数据库的所以说呢咱们在这儿去加一个什么呢mycircle的什么配置类这个怎么写呢它呢是一个配置类所以说一个configuration然后呢再次去加一个什么compound scan
[00:30] 然后就在这去直接扫描就可以了那扫描哪个呢大家还有印象啊当时咱们去封装买circle的时候有一个配置是吧咱们主要是扫描当前这个包就可以打开拷贝一下好直接复制它就可以啊这里边没有内容吧对没有内容没有问题当我们去这个启动项目的时候啊你可以看一下
[00:59] 当我们启动项目的时候这块呢是有一个叫引导类引导类呢它就会去默认去加载什么当前包及其此包的一些扫描对吧OK那这时候呢它这个啊就会被加载那行啊那这个呢咱们算是补完了下面呢咱们就来去定义咱们的这种服务应该说是定义咱们的接口啊那定义接口之前呢咱们首先呢是来定义一个DTO
[01:26] 那这DTO啊其实已经在当前的model项目中已经提供了啊大家呢可以打开来看一眼好当前的是article下面有一个DTOS有一个article home DTO那这个呢就是用来咱们去查询文章列表的时候的一些参数那这参数是有那么多啊咱们一块来分析一下啊刚才呢咱们去分析当
[01:52] 当前的需求的时候说了啊有可能呢咱们需要去根据当前的时间最大时间和最小时间还有有可能会分页还有用户去点击了某一个频道他可以去切换频道那这上面这三个呢咱们刚才没有说那咱们再简单说一下啊那这个呢其实呢就是根据当前用户的这种省市还有区限进行去加载当用户呢去没有去选择任何用户的时候呢
[02:21] 咱们可以基于当前的地区进行作为条件进行去加载数据好那这个咱们就把这个给说完了咱们这个算是定义完了下面咱们就来去定义具体的接口那咱们再回忆一下咱们需要定义哪些接口呢目前咱们只说啥呢只说这种文章加载的接口首先第一个是不是有一个当进入首页的这种接口还有上拉和下拉刷新的接口对不对
[02:50] 好那咱们呢定义接口的话咱们定义啊之前说过是吧咱们需要在哪啊在当前的APIS里边去定义咱们通用的什么暴露的接口在这去创建一个包那这个包叫啥呢叫com.kma.articleAPIS好下面呢咱们就来去创建一个什么对这里叫啥好articlehomecontrollerAPI
[03:25] 所有的pull借口都以api结尾它是一个接口好那这借口咱们就创建完了那里边里边有哪些方法呢刚才说了三个是吧三个呀一个是public的什么load是吧load里边有什么参数呢参数就是刚才咱们说这个dtoarticlehomedto好dto那返回值是啥呢那返回值的话咱们
[03:55] 之前讲这种接口规范的时候目前咱们统一都反馈什么呢叫resonanceresult里边呢可以装入咱们的数据列表好那这是第一个接口叫什么呢叫加载加载首页文章我们再来去定义第二个接口叫public还是resonanceresult然后是叫load什么mood那loadmood是什么意思呢
[04:33] 它的参数是一样的啊是加载更多的吧这个呢咱们来去解释一下啊这个呢就是加载更多还有一个是吧哪个哎好啊叫public race without然后是load new这里边啊它参数也是一样的也是article home
[05:04] 好那这个呢是咱们是什么发载什么发载最新对吧发载最新的文章好这个接口啊咱们算是定义完了下面呢咱们就来去把这接口给实现一下那实现在哪实现呢哎在咱们具体的微服务上面是吧这有一个controllerok那咱们去创建一个类这个类叫啥呢
[05:31] 这个类跟咱们这个接口是一样的只是它没有后缀API好是article home Controller让它实现当前咱们刚才定义的接口article home Controller API好,ctrl i直接去实现这三个方法好,那这呢去加一个诸解叫request restrest Controller
[06:06] 好啊这个control加完之后呢咱们还有一个叫request mapping请求映射咱们需要去加一下呀那这个咱们去怎么定义呢咱们可以看一下讲义啊讲义里边呢咱们就按照这个讲义回饭一块去锁好这里边啊咱们就算是这三个方法就算是按完了那加完之后呢咱们需要去是不是要去调用一个Service啊好那咱们把这个Service给说一下叫ppp articleservice好吧
[06:40] 这个接口没有没事啊咱们就来创建出来好创建一个不对啊咱们应该是创建一个接口啊不得加回车然后是创建一个接口在哪个包下边呢咱们可以选择一下包这个包的话就是Service好okok那这时候这个Service就算是创建完了啊行那这个有了那这里边分别应该是加在哪个东西呢咱们之前分析过啊
[07:11] 它呢是跟咱们之前的这个load的接口啊应该是一样的啊比如说你load的接口加载咱们是有这么个条件那load墨和load new呢它呢也是需要有这么些条件并且呢它是有一个时间的控制对吧所以说呢咱们在Service中啊只需要定义一个方法就可以只要去参照不同的参数传不同的参数让它去加载不同的东西就可以比如说你在这啊去创建一个load什么
[07:40] load好咱们就创建个load咱们需要传什么参数呢首先传的一个参数叫BTO第二个呢咱们应该有一个type那type是谁呢哎这个type呀就是咱们要去定义的当前的什么你到底是load more呀还是load new啊那关于这个load more和load new呢咱们可以这样啊咱们可以干嘛呢可以是load more跟load呢其实应该是一个道理
[08:09] 只是呢一个传了参数一个传了时间参数另外一个是没有传当前漏的是没有传时间参数这个漏的末呢是传了一个时间参数是吧所以说咱们统一呢都叫漏的末就可以了那这个参数呢咱们是可以去写写词比如说都叫一只要是一的不是漏的末所以说这两个应该是一样的那第二个呢TOTO写错了是吗TOTO
[08:42] 好那这个呢这个呢其实也是一样啊只是呢目前传的时候不是1咱们可以给它定义一下呢定义一个目前的话咱们这个就算是定义完了当然这里边还有一些代码需要补全比如说咱们具体要访问哪一个呢比如说咱们有一个getmypn是吧这里边干嘛呢需要去设置一个load的接口还有下面是
[09:12] 分别是loadMod和loadNode好按上loadMod好这个是loadNode好这个咱们就算是s是Node咱们最好是跟笔记是一致这个好像是小写的我看一下笔记上都是小写的所以说咱们在这也定义成小写好指Node等到这个定义完之后这个Service的方法还没有创建出来咱们就直接按
[09:46] out加回车去创建就可以了啊那创建之前呢咱们再来说一下当前这个参数啊这个参数啊咱们不应该这么写不应该写死咱们应该怎么着呢在通常的开发的时候呢咱们都要去定义一个这种常量那常量在哪定义呢OK那常量呢咱们通常呢是都在common下边去定义所以说咱们在这啊再去创建一个常量类
[10:10] 哦那就成量类已经有了啊有的话呢咱们就直接定义就可以了它是一个short类型哎一就代表load more二呢就代表load new如果说你那没有的话就把这两个也定义出来就可以了这个非常简单啊行那这个呢咱们就可以在这传一下怎么传呢叫articleconstance是吧什么load more这个下面这个是一样的好这个呢应该是load new改一下
[10:46] 那这创建完之后呢咱们就可以在这去out加回车直接让他创建方法就可以好吧好那这个方法呀创建完了下面呢就来去实现这个方法那咱们定义实现之前呢咱们把这个注释啊也顺便给写一下啊这个是有两个参数就是short当前这个type啊把这个type改一下啊改成type也是type但是type呢是就是啊呢就是加载什么更多二呢就是
[11:20] 加载更新好咱们来一块来实现一下当前的这个方法首先呢咱们还是在当前的这个类下吧去创建一个包这个包呢就是ampl好ampl.什么ppp article好servicem 车首先呢这个类呢咱们需要去实现当前的接口是吧这是app Service
[11:55] ServiceCtrl I实现这个方法然后呢让它去加到Spring容器中是吧加一个Service注解然后呢咱们主要是来编写当前这个接口就完事了啊当前这个什么实现类就可以了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，如何定义文章首页 DTO、Controller 接口、Service 接口及其实现类，构建文章加载功能的分页和加载更多逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，选中 `heima-leadnews-article` 模块，准备进行开发。
画面 2：打开 `MysqlConfig.java`，展示 Spring Boot 的配置类，使用 `@Configuration` 和 `@ComponentScan` 注解。
画面 3：切换到 PPT 页面，标题为“7.3 article服务功能开发”，并展示 `ArticleHomeDto` 的定义。
画面 4：在 `ArticleHomeDto.java` 中，展示 DTO 类的字段定义，包括 `provinceId`、`cityId`、`countyId`、`maxBehotTime`、`minBehotTime`、`size`、`tag` 等。
画面 5：右键点击 `ArticleHomeDto.java`，弹出菜单，选择“Run All Features in java”等选项。
画面 6：在 `ArticleHomeControllerApi.java` 中，定义了三个方法：`load`、`loadMore`、`loadNew`，并标注了注释。
画面 7：在 `ArticleHomeControllerApi.java` 中，对 `load` 方法的参数和返回值进行注释说明。
画面 8：在 `ArticleHomeController.java` 中，实现 `ArticleHomeControllerApi` 接口，三个方法均返回 `null`。
画面 9：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@RequestMapping("/api/v1/article")` 注解。
画面 10：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@Autowired` 注解，注入 `AppArticleService`。
画面 11：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@RequestMapping("/load")` 注解。
画面 12：在 `ArticleHomeController.java` 中，为 `loadMore` 和 `loadNew` 方法添加 `@RequestMapping("/loadmore")` 和 `@RequestMapping("/loadnew")` 注解。
画面 13：在 `AppArticleService.java` 中，定义了 `load` 方法，参数为 `ArticleHomeDto` 和 `Short type`。
画面 14：在 `AppArticleServiceImpl.java` 中，实现 `load` 方法，返回 `null`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
package com.heima.article.config;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.heima.common.mysql.core")
public class MysqlConfig {
}
```

画面 3：
```java
mysql初始化扫描配置类com.heima.article.config.MysqlConfig

@Configuration
@ComponentScan("con.heima.common.mysql.core")
public class MysqlConfig {
}
```

画面 3：
```java
public class ArticleHomeDto {
    // 省市
    Integer provinceId;
    // 市区
    Integer cityId;
    // 区县
    Integer countyId;
    // 最大时间
    Date maxBehotTime;
    // 最小时间
    Date minBehotTime;
    // 分页大小
    Integer size;
    // 搜索范围，比如频道
    String tag;
}
```

画面 6：
```java
public interface ArticleHomeApi {
    // 加载首页文章
    @Param dto
    @Return
    public ResponseResult load(ArticleHomeDto dto);

    // 加载更多
    @Param dto
    @Return
    public ResponseResult loadMore(ArticleHomeDto dto);

    // 加载最新的文章信息
    @Param dto
    @Return
    public ResponseResult loadNew(ArticleHomeDto dto);
}
```

画面 8：
```java
public class ArticleHomeController implements ArticleHomeControllerApi {
    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 9：
```java
@RequestMapping("/api/v1/article")
public class ArticleHomeController implements ArticleHomeControllerApi {
    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 10：
```java
@Autowired
private AppArticleService appArticleService;
```

画面 11：
```java
@RequestMapping("/load")
@Override
public ResponseResult load(ArticleHomeDto dto) {
    return appArticleService.load(dto, "1");
}
```

画面 12：
```java
@RequestMapping("/loadmore")
@Override
public ResponseResult loadMore(ArticleHomeDto dto) {
    return appArticleService.load(dto, "1");
}

@RequestMapping("/loadnew")
@Override
public ResponseResult loadNew(ArticleHomeDto dto) {
    return appArticleService.load(dto, "2");
}
```

画面 13：
```java
public interface AppArticleService {
    /**
     * type 1 加载更多 2 加载最新
     * @param dto
     * @param type
     * @return
     */
    ResponseResult load(ArticleHomeDto dto, Short type);
}
```

画面 14：
```java
public class AppArticleServiceImpl implements AppArticleService {
    @Override
    public ResponseResult load(ArticleHomeDto dto, Short type) {
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3：
PPT 标题：“7.3 article服务功能开发”
子标题：“(1) 定义dto”
内容：
- (1) load接口
- (2) load_more接口 & load_new接口
- (4) 行为接口
- (7.3.1) 在Konn文件中的校验注解
- (7.3.2) Article服务功能开发
- (7.3.3) 行为接口功能开发

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

