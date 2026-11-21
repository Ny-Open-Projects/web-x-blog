# 20_app文章列表_业务层实现类代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\20_app文章列表_业务层实现类代码完成【海量资源尽在 666java.com】.mp4
- 时长 17分32秒（音频 1052s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们继续啊把当前的这个实现类给写完啊那这个类里边到底该怎么去写呢那咱们呢重新的再打开当前这个需求的这个图啊那说啊咱们现在用户啊分两种情况一个是未登录一个是登录那登录的时候呢咱们就去加载推荐的文章那不未登录呢咱们就加载这种默认的文章就可以所以说呢咱们在这儿啊去写的时候呢首先的是要干嘛
[00:27] 叫获取用户的什么信息然后第二个呢这就是判断啊用户是否存在然后呢就是存在怎么办存在就是登录是吧登录然后是加载什么加载推荐的文章OK然后下面呢是不存在不存在的话说明就是未登录呗是吧
[01:01] 未登录未登录那就是加载什么默认的文这个呢其实就是大概的一个思路那咱们说到之前呢咱们还要再去为了程序的严谨性啊需要去把这个参数啊做一个校验参数校验首先第一个校验呢咱们要去判断那谁呢判断当前的DTO是吧如果说DTO
[01:34] 没没弄怎么办呢咱们就给他new一个出来好吧就一个空的出来你你有一个什么article保证他不会报错就可以好吧下面呢咱们还要再去做教验啊要去做一个什么教验咱们可以打开这个tto来看一眼这里面有什么参数呢这三个参数啊其实咱们无所谓我们到后期咱们到map文件中也可以做教验主要呢咱们是把这些做教验就可以好吧
[02:05] 那咱们可以把这个时间先多一个校验打开当前的Service时间校验其实有两个时间一个是最大值一个是最大时间一个是最小时间是吧好那咱们来看一下如果说cto里边的什么setmax这个时间最大时间等于等于什么呢等于等于空等于none怎么办呢我们就把它设置为前时间cto.set
[02:40] 重新设置啊然后new一个什么get出来它不就完事了吗同样啊这个最小时间也是一样如果说它没有时间的话咱们把它设置为刚前时间就可以了啊这是getmin是吧就是一小时间把它拷贝一下不是拷贝是吧set什么这样的话咱们就算是设置完了啊
[03:07] 这个参数校验完之后咱们还有哪些参数需要校验呢还可以打开这个里面再去看一眼啊那就行啊里面的是还有啥呢还有一个分页那咱们把这个分页也给做一下校验啊分页参数的什么叫页首先呢咱们拿到当前这个分页参数啊比如说dto.setSize好拿到这个size之后呢咱们首先做个分段看这个size是否为空是吧
[03:42] size等于空或者是啥呢或者是size小于等于0的时候呢给它设一个什么呢都市值或者默认值是20在这就定于20啊那下面还有一种另外一种情况比如说啊用户传了一个size过来但是呢它这个参数太大那咱们的页面里边有可能是加载不了
[04:10] 那这时候呢咱们可以做一些优化怎么优化呢咱们呢咱们呢可以把这个值啊给它设立一个固定值什么固定值就是说当它大于50的时候呢咱们就让它去加载50条那这个怎么做呢这个咱们可以借助一个数学的函数叫massmass点什么咱们取个小值给谁对比呢当前这个size给这写个50那这句话的意思呢就是说当前啊
[04:41] 当前这个size如果说大于50的话咱们就取50这个值如果说小于50咱们就取当前size这个值那这样的话就能保证它绝对不会大于50好吧行那这个size设置完之后呢咱们把它的重新设置到哪设置到当前的TO中设size好那这样完了啊那这里面还有个问题啊那这个50啊我也不想写死到这
[05:08] 咱们可以呢在当前类上去定义一个什么常量好privates static 是吧然后是final它是一个short的型啊咱们就进小一点啊50其实已经够了啊然后定义成啥呢叫max page好sizesize等于50好吧行那把它呢就直接
[05:39] 这个50给替换了就可以了啊这样的话就算设置完了那这个分页参数咱们也教练完了下面咱们再继续教验另外一个参数啊就是哪个参数呢就是一个文章频道的参数啊文章频道参数教验好这里边啊我们首先再去判断一下当前这个参数是否为空pto.get如果说它是为空的话呢咱们呢可以给它设一个
[06:10] 这个啊,咱们就这么判断啊咱们用当前一个工具类吧stu94.2如果说它不得是微空的话呢咱们就再给它重新复制啊重新复制一个什么值呢9.7的tog咱们就设置一个当前的档杠那这个呢,咱们就做一个标识
[06:33] 为了方便后边mypool进行处理好吧那这个我也不想写死那怎么办呢其实呢在咱们常量类里边啊已经定义了这么一个东西所以说呢你只需要去用当前的常量去引入就可以了点什么呢一个defun那这个文章文章频道参数啊我们也说到这然后下面还有一个啊就是我们有一个种类型参数啊类型参数的教研那这个参数可以看一下啊
[07:07] 如果说他为空或者说他一般不为空那他是cos他不等于谁呢不等于loadMode不等于loadNew的时候呢咱们就给他一个初始值是让他等于loadMode这样可以吧那这个怎么判断呢还是他啊当然什么loadMode而且呢他呢还不等于loadNew咱们试一个等号啊好那这个呢
[07:44] 我还跑呢抓不着了是吧好放到这啊它是load这时候呢如果说它都不等于的话呢咱们就给它设置一个都是值那就是type等于谁呀等于当前的load木就可以了目前的话这些参数呢就算是全部交易完了啊然后下面咱继续往下看啊咱们就写咱们具体的业务了啊首先咱们要获取用户信息那用户信息怎么获取呢
[08:13] 其实这是咱们在后台能够获取在当前现场当时咱们在介绍工具类的时候大家不知道还有没有印象在这个工具类里边有一个叫这样的工具类SredLocal里边有一个AppSredLocalUtils这里边就可以去拿到当前APP的用户你可以设置用户你也可以获取用户那咱们现在就直接获取用户就可以了叫APP
[08:43] stribe local utils.getuser它呢就能去拿到当前AP用户的一个运行器OK那咱们就判断呗如果说呢当前用户不等于那不等于那的话就说明它是已存在的咱们可以去干嘛呢去加载它推荐的文章否则呢否则啊OK那这时候呢就是否则就是未登录咱们要去加载默认的文章
[09:20] 那咱们之前分析过啊加载默认的文章的不是加载那个推荐的文章的咱们是通过当前的用户ID就可以去查询当前的一个表哪个表啊就是当前的一个这个表啊就是当前的哎就是打开这个表啊这个表那这个表呢就是里边有一个user ID并且呢有对应的一个文章ID也就是说咱们需要去通过当前的用户去查到当前对应的文章ID那这个呢咱们就可以在这去写一下啊
[09:49] 那怎么写呢咱们在这可以定一个方法定一方法咱们就叫做setUserArticle这个时候咱们就可以去设置一些参数这个参数有哪些呢咱们的参数就过了User信息还有什么呢DTO信息还有什么呢好那最终的反回的是一个啥呢反回的它反回的咱们一会再说它应该是反回一个list
[10:22] 那这list里边装的呀应该就是articleAP article叫article好吧那这个方法没有啊咱们就创建出来那这个方法主要干嘛呢这个方法呢主要就是先从哪啊先从用户叫什么推荐小钟干嘛呢查找文章查找文章信息
[11:09] 然后呢如果没有的话呢再从哪啊再从这种默认的文章信息获取获取数据这是一种方式啊那行如果说那这不存在的话呢咱们就也可以去加一个也可以去写一个私有的方法啊说get什么be foundbe found article好
[11:43] 这时候他传的参数就没有 user应该是 DTO 一个什么呢就是 type他返回的也是目前的某个东西这样咱们就简单点直接去 return 就可以了好吧咱们先去方法创建出来创建出来之后呢就在这直接 return 就可以21return 还不行是吧他需要把这个方法呢去装到 response 中或者把这个返回值装到 response 中response 中那这时候怎么办呢
[12:21] 我们可以这样啊同样的他也是还让他去返回好吧这时候咱们就叫articles好吧嗯等于最终呢咱们可以在这去new一个什么response就直接return就可以了return一个response result打什么ok result就可以把VP article result的例子进去哎就完事了啊下面是一样的啊好这里边装的是
[12:53] 那这个就是写的写起来就比较简单了
[13:23] 首先呢咱们在这呢可以直接从这个什么article的表中直接获取数据就可以了咱们一会儿再来说这个方法好吧那这个方法啊首先呢你看这里边是有一个DTO有一个type咱们可以作为参数进行查询所以说呢咱们首先呢要去注入一个mypr进来那这mypr呢咱们可以在这定义啊比如private叫什么AP articlemypr好mypr没有没有事啊咱们一会儿再去创建
[13:55] 他这里边呢是应该会有一个方法叫啥呢load什么咱们就起个名字咱们跟一张宝石一致好吧打开当前的啊叫什么呢叫load article by location是吧叫他然后呢这是dto然后是啥呢是type作为参数就可以了啊最终是返回可以好那这个方法啊
[14:24] 这个MIPR一会儿再创建咱们先写到这咱们再把下面的方法再去补全刚才说了啊这个是要先从用户推荐表中查找文章信息然后最终的是再从如果说没有的话咱们再去获取文章信息数据就可以了啊那这个怎么写呢好那这么写啊咱们也要去把当前的这种方法名给拷贝过来啊这一块首先呢咱们要去注入当前的一个MIPR比如说呢你在这啊咱去注入这个MIPR
[14:54] private叫啥呢叫tongue我们把这个ar好就叫tongue把这个注入进来那注入进来之后呢这里边是有一个方法的那方法先去叫load什么咱们也考过来这个方法名load article idistab user那这个参数就比较多了这个参数就有一个user参数还有什么dto的参数还有什么还有type那最终它返回的是啥呢
[15:28] 反回的是一个当前的推荐文章列表当前的这个类这个对象,所以说咱们怎么写呢应该是叫AP userAP user article list,就它咱们可以写一个名字叫list,反回下面就来去判断判断啥呢判断当前里面到底没有值如果说list反而什么
[15:59] 如果它是空它不是空的话咱们就写个非如果它不是空怎么办呢好如果它不是空的话咱们就问出来就是去再去哪去查呢再去咱们当前的这个表中当前的这个表中再去查那根据什么查呢根据查到的list的集合去查就可以了啊OK那咱们在这再把这个方法给考过来点它然后参数呢
[16:31] 其实呢就是当前的list返回的应该就是当前的所需要的这种list叫articles好这个算是一种情况还有第二种情况啊不说他没有在你的推荐里面的话没有找到文章应该干嘛呢应该再去查询当前的这个方法这个方法呢需要两个参数第一个是BTO然后第二个是这个返回的呢
[17:06] 也是它直接累称就可以了啊咱们上面也直接累称一下啊这样的话就不用再去定义这个变量了好那这个就算是定义完了啊咱们说的逻辑呢算是都都写到这那这个类呢还没有那咱们下一个这种视频咱们再定义

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个文章推荐系统中，根据用户登录状态和请求参数（如时间范围、分页大小）加载不同文章列表的逻辑，涉及控制器、服务层、线程局部变量和数据映射器的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个用户文章加载的流程图，包含“未登录”、“登录”、“用户设置的频道”三种状态，以及“上拉刷新”、“下拉刷新”、“隐藏需求”等交互说明。
画面2：展示IDEA中ArticleHomeDto类的定义，包含provinceId、cityId、countyId、maxBehotTime、minBehotTime、size、tag等字段。
画面3：展示ArticleHomeService类中load方法的参数校验逻辑，包括对dto参数和时间参数的非空判断。
画面4：展示ArticleHomeService类中对分页参数size的校验逻辑，包括设置默认值20。
画面5：展示对type参数的校验逻辑，包括判断是否为0。
画面6：展示AppThreadLocalUtils类中设置当前线程用户信息的代码。
画面7：展示ArticleHomeService类中获取用户信息并根据用户状态决定加载推荐文章或默认文章的逻辑。
画面8：展示ArticleHomeService类中根据用户是否存在决定加载推荐文章或默认文章的逻辑。
画面9：展示ArticleHomeService类中获取默认文章列表的逻辑。
画面10：展示ArticleHomeService类中获取默认文章列表的逻辑，包含返回ResponseResult。
画面11：展示ArticleHomeService类中获取默认文章列表的逻辑，包含使用apArticleMapper。
画面12：展示ArticleHomeService类中获取默认文章列表的逻辑，包含使用apUserArticleListMapper。
画面13：展示ArticleHomeService类中获取用户文章列表的逻辑，包含判断列表是否为空。
画面14：展示ArticleHomeService类中获取用户文章列表的逻辑，包含根据列表是否为空返回不同结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
// 省
Integer provinceId;
// 市
Integer cityId;
// 县
Integer countyId;
// 最大时间
Date maxBehotTime;
// 最小时间
Date minBehotTime;
// 分页大小
Integer size;
// 每页范围，比如频道 20
String tag;
```

画面3：
```java
@Override
public ResponseResult load(ArticleHomeDto dto, Short type) {
    // 参数校验
    if(dto == null) {
        dto = new ArticleHomeDto();
    }
    // 时间校验
    if(dto.getMaxBehotTime() == null) {
        dto.setMaxBehotTime(new Date());
    }
    if(dto.getMinBehotTime() == null) {
        dto.setMinBehotTime(new Date());
    }
    // 分页参数的校验
    Integer size = dto.getSize();
    if(size == null || size <= 0) {
        size = 20;
    }
    dto.setSize(size);
    // 获取用户的信息
    // 判断用户是否存在
```

画面4：
```java
// 类型参数校验
if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_MORE)) {
    type = ArticleConstants.LOADTYPE_LOAD_MORE;
}
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面6：
```java
package com.heima.utils.threadlocal;

import com.heima.modal.user.pojos.ApUser;

public class AppThreadLocalUtils {
    private final static ThreadLocal<ApUser> userThreadLocal = new ThreadLocal<>();

    // 设置当前线程中的用户
    public static void set(User user) {
        userThreadLocal.set(user);
    }

    // 获取线程中的用户
    public static ApUser getUser() {
        return userThreadLocal.get();
    }
}
```

画面7：
```java
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面8：
```java
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面9：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面10：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面11：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面12：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    apUserArticleListMapper.loadArticleListByUser(dto, type);
}
```

画面13：
```java
// 获取用户文章列表
private List<Article> getUserArticle(AppUser user, ArticleHomeDto dto, Short type) {
    List<Article> articleList = apUserArticleListMapper.loadArticleListByUser(user, dto, type);
    if(articleList.isEmpty()) {
        return apArticleMapper.loadArticleListByLocation(dto, type);
    } else {
        return getDefaultArticle(dto, type);
    }
}
```

画面14：
```java
// 获取用户文章列表
private List<Article> getUserArticle(AppUser user, ArticleHomeDto dto, Short type) {
    List<Article> articleList = apUserArticleListMapper.loadArticleListByUser(user, dto, type);
    if(articleList.isEmpty()) {
        return apArticleMapper.loadArticleListByLocation(dto, type);
    } else {
        return getDefaultArticle(dto, type);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：流程图结构：
- “用户”指向“未登录，加载默认的文章列表”
- “用户”指向“登录，加载推荐的文章列表”
- “用户”指向“用户设置的频道进行加载”
- “上拉刷新”指向“加载当前时间之前发布文章”
- “下拉刷新”指向“加载当前时间之后发布文章”
- “隐藏需求”指向“记录当前用户的行为”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

