# 10.圈子功能实现之动态信息评论（查询评论列表-APP服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\10.圈子功能实现之动态信息评论（查询评论列表-APP服务）_【海量资源尽在 666java.com】.mp4
- 时长 19分3秒（音频 1144s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来编写我们这个服务接口那么首先呢我们需要定义一个commons这样的一个对象用于去匹配我们的这个所需要的这个数据结构那么就是下面这个item这样的一个数据结构了好,那么我们就把这个来考虑过来然后呢丢到我们的这个server这个工程中的这个VO这个里面来
[00:27] 好这样的话呢我们就有了这个对象了大概呢有这么几个字段我们来看一下那么一个呢是ID啊这个是评论的ID然后呢还有头像昵称还有评论的内容评论的时间还有点赞数和是否点赞那要注意了这个点赞数啊它呢是我们对于评论的点赞而并不是对于我们动态的点赞啊这一点要分清楚那么其次呢我们再要说一下就是
[00:57] 那么我们对于评论的点赞那么实际上它也是一个评论只是它评论的目标不是动态信息而是什么呢某一个这个评论的这个内容去做一个点赞所以说呢我们对于评论的这个点赞呢依然是使用着我们的这个comment这样的一个对象去做一个存储这一点要注意一下那么还是使用之前这个逻辑啊那是一样的
[01:27] 好,那么接下来呢我们就实际的来操作一下那么下面呢我们就定义我们的这个方法对吧那么我们来看一下那么首先第一个呢就是去查询我们这个列表那么我们需要写一个这Commons的一个Controller那我们就在这个里面来写一个Controller对吧然后呢写一个叫Commons的一个ControllerControllerL
[01:55] 然后我们把它标记为这是一个rest Controller然后我们这样子就可以了那么我们再标记一个叫做什么叫做request mapping设置一个URL那么就是刚刚我们看到这个comments那么下面首先第一个我们需要查询它的是一个列表那我们就public返回值我们就写一个叫做
[02:24] PagerResult对象PagerResult然后呢我们去写一个叫做QueryCommonsCommonsList查询这个列表然后呢我们去写一个叫做GetMapping看一下是Get进去GetMapping这个参数呢大概有这么几个参数叫
[02:50] moment id还有一个page还有page sign这三个参数那我们就分别来获取一下那么首先第一个呢是我们需要通过一个request param来做一个获取这个呢其实就是我们的这个它是moment id那么所对应的其实就是我们的这个publish id然后去做一个查询了那么我们就来写一个这个street然后呢写一个publish id
[03:20] 好那么这是我们的第一个这个参数那么第二个这个参数呢写一个叫做什么呢就是看一下啊那么是pager然后呢我们是不是应该这样去写这个value等于它然后呢我们可以写一个default value等于什么呢就是默认的就是在什么查询第一页数据然后呢我们继续往下面去写
[03:48] 还有呢就叫request param还有就是value啊等于等于谁呢来看一下就是叫做pagesize那么我们来设置它的一个default value啊等于什么呢10然后呢我们再去设置一个我们这个pagesize这个改成大写啊pagesize好那么这样的话呢我们就已经啊把这个参数呢就接收到了那么接收到之后呢我们就要去写一个
[04:16] 这个common式的一个Service然后去做一个具体逻辑的一个编写和处理那么写一个Service好那我把它去写这个叫做什么呢Service好那么然后我们在我们这个Controller中就可以把它就注入进来了对吧叫common式Service然后去把它就注入进来那么注入之后我们就来编写这个里面的一些逻辑了
[04:45] 我们通过comment Service然后点然后做一个query的查询那么我们把这三个参数传递过去一个是public id一个是page一个是什么呢page size那么把这三个参数传递过去那么我们所期望它返回的是一个叫做page result对象好那等于它
[05:13] 然后我们来看一下在这个位置我们就需要去做判断了如果说如果说我们空等于它的话空等于它的话那我们就应该应该我们判断不等于当然这个位置我们还是应该去使用我们的responseresponse entity去拿一个page result如果不等于空的话那我们就return这个response entity点什么的ok
[05:43] 把这个PageResult传递进去下面呢走到这儿就return我们的response.http然后呢写一个叫做.internal.stable.然后呢设置一个build好那么这个control逻辑呢我们基本上呢就写好了那我们再来给它做一个try catch的一个处理那么简单来处理呢那就这样了好那么这个是查询什么呢
[06:11] 去查询我们的这个评论列表查询这个评论列表然后呢我们来看一下那么在在这个里面那么我们就需要去创建我们这个Service中的这个方法了那么这个方法创建出来之后呢那么我们肯定是需要把谁注入进来呢是我们肯定需要是把我们的这个圈子对吧圈子API是不是注入进来那么因为在这个里面呢是我们的这个
[06:40] double的服务对吧reference去获取它那么我们这个Warsen版本呢Warsen版本呢是1.0.0这样的一个这个操作了好那么通过它呢去做一个查询那么这么查询呢是不是就通过这个圈子这个API然后呢去写一个querycommentlist去做一个查询那么首先第一个呢是这个
[07:08] 我们的这个叫做啊public id那么第二个呢就是我们的这个pager对吧第三个呢就是一个pager size啊pager size去做一个啊这个查询那么他所拿到的就是我们这个pager info那么我们其实需要拿到的是pager info中的这个recall就是我们这个comment这个对象那我们去来获取一下
[07:37] 那么获取到之后呢接下来呢我们就需要按照我们所需要的这个结构去做一些数据的一些这个分装了那么就是这个comments这样的一个对象那么下面呢我们对它呢做一个判断啊如果说这个为空的话那我们就使用一个结合去做判断嘛connection utils.isempty那么如果它为空的话那我们就需要return了
[08:05] 当然了return呢我们是需要给它返回一个我这个空的一个对象当然这个空对象呢不是那是它的确是有值的对吧那我们就在上面吧我们最终定一个我们这个pager-resultnew一个pager-result然后呢我们来给它设置一些这个值点set这个pager那就是这个pager然后呢pager-result.set什么的pager-set那就是pager-set了
[08:35] 然后呢page result.set什么呢还有我们的这个counts那就设置为0然后呢page result.set什么呢pages也设置为0然后应该就没了吧result.set是不是都已经设置完了当然我们这个items我们现在肯定没有所以我们就不做设置了那我们直接returnreturn这个page result这样的
[09:04] 反复这个对象是不是就可以了那么如果不为空呢那么接下来呢我们来看一下那么就要去分装谁呢刚才我们所写的这个comments这个对象那么在这个里面呢它是需要有一些用户相关的一些这个信息的比如说这个用户的头像啊昵称呢这样的所以说呢在这个里面我们还需要去查询用户了那么我们又要去使用谁了呢是不是我们这个user infoservice
[09:33] 把这个UreinfoService注入进来好那么注进来然后呢在下面这个怎么操作呢我们肯定是通过这个list点UreinfoService点是不是queryUreinfoList那么需要一个queryWrap对象那我们就给它定一个什么呢queryWrap对象那么这个就叫Ureinfo好那么我们定一个这个queryWrap对象去new一个去
[10:00] 另外一个这个querywrap对象然后呢我们去给大家去我们应该去设置什么呢设置我们的这个条件条件对吧那么我们是不是应该去设置一个in就是我们这个url下滑线ID然后呢它呢是谁呢就是in缺少一个参数对吧然后呢in那么肯定是需要一个集合了那么上面是我们需要定义一个这个集合比如说我们叫
[10:29] list然后呢是一个none类型的这样的一些这个用户呢叫userids等于new一个revealist那我们就可以把这个userids传递过来然后这个呢就是它的一个查询条件了那我们就把条件传过去它就会得到一个叫做userinfo list那这个大家应该能看懂吧这个是我们之前写的代码
[10:55] 好那么接下来呢我们就需要把这个UIDs去做一个填充对不对那么我们怎么样去做填充呢我们去拿到一个这个就是recode那么应该是点按的去添加一个recode中的get什么的UID这样的话我们是不是拿到所需要去查询用户信息的这个UID了给它丢到这个里面来然后呢下面呢我们就对这个
[11:22] 我们这个集合去做不能对它便利啊那我们应该对谁便利呢就是我们呢还是去应该对我们的这个recode是去做一个便利然后呢再去做一些这个填充啊那么在上面呢我们还是需要定一个集合啊这个集合呢用于存储我们最终的一个comments这个对象啊叫comments list等于等于去new一个arrival list
[11:51] 那么最终呢注意啊最终我们返回的还是这个page-result对象还是我们上面这个对象那么这个page-result呢我们就需要给它去set一个叫做items把这个comment-list传递进去好那么这个传递进去之后呢我们接下来就需要对这个集合做填充啊就可以了那么每循环一次那肯定会生成一个comments的一个对象那我们就去new一个这个comments对象
[12:20] 然后呢我们去做一个填充那么就写个comments list.and去添加一个comments这样的一个对象好那么在这个中间呢对它做填充就可以了那我们来看一下.set比如说那么我们来看一下这个ID这个ID显然就是我们recall的ID然后呢就这个ID了然后呢我们再来设置.set什么呢就是leg count我们一会儿再处理那么关于用户的一会儿再处理
[12:49] 那么还有什么呢创建的这个时间啊那么创建这个时间呢我们还是需要给他去填充一下那么我们就按照这个年月日去做一个填充吧那我们去拗一个data啊data啊time对象啊然后呢呃注意这个不能去直接去拗啊那我们还要拿到这个recall的点get什么呢就是叫做created这样就得到一个对象了然后呢to啊street
[13:16] 那么这个怎么去写呢我们就按照年月日吧就是YYY应该去写个周创YYY然后呢年年MM然后呢月然后呢DD日啊空格然后呢就后面这个呢就写什么呢就是时间了啊那么应该写什么呢就叫H啊冒号M啊应该这个是要大写吧然后呢MM
[13:46] 这样写那么前面这个M要注意这个M也应该是大写这样才对我们来看一下讲义对不对别把这个格式搞错是在下面这个位置那么看一下这个YYY年月D没问题吧那么这个就是我们的一个需要格式化的一个时间那么我们再去set一下那么下面的是内容评论的内容那么通过recode来获取
[14:13] record.get一个contact的内容然后呢comments.set然后呢还需要有哪些呢那么还需要关于用户相关的对吧那么这个怎么办呢这个我们就需要去做一个便利了便利谁呢便利我们的这个user info list那么判断一下判断我们这个就是record.get user id.long value是不是等于
[14:43] 什么呢get user id点这个long value那么如果这两个相等那就说明找到了那么先写一个break跳出然后呢接下来呢我们在这个位置就需要拿到用户了去做填充了那么就写一个comments.set什么呢叫做neek name那么就写个user info点get什么neek name
[15:05] 然后呢comments然后呢再去设置他的一个什么头像对吧然后呢我们就通过userinfo.get什么logo去获取那么应该是没有了吧关于用户相关的那就没了那么接下来呢还有两个没做处理的那就是我们的这个点赞数对吧点赞数那么接下来我们来看一下这个点赞数应该怎么做处理那么我们来看一下comments.set这个叫做like count
[15:35] 和comments.set一个什么呢是否已经点赞那么这两个可以参考我们之前所写的我们这个服务就是Moments服务去使用是去写这个逻辑那么我们就把这个逻辑呢就拷贝过来那么它呢也会有这个类似的这样的一个逻辑好那我们来拷贝一下那么首先呢它是需要我们的这个就是
[16:01] ready是template那么我们同样呢把这个ready的template呢去注入进来那么ready的template然后呢死去啊然后呢是在写一个死去好那么这个就是一个ready的一个template啊把它呢注入进来那么注入进来之后呢我们来看一下它还需要什么那么它需要我们这个优的对象那么优的对象呢那我们就在就在最上面吧去拿到这个优的对象啊
[16:29] 那么这个优惠就是我们当前的这个用户把这个优惠呢我们导一下包那么就叫优惠等于叫优惠随 local.get来获取到这个优惠对象然后呢我们来看一下他还需要什么就是说这个呢是这个没有问题然后呢这个是我们的ID这个ID那我们就应该使用谁的呢就是使用这个comments ID了
[16:54] 就是我们这个评论的这个ID就说我们现在是对前面的一个评论是不是去做一个点赞呢对吧拿到他评论的一个ID然后呢下面呢我们再设置他一个是否这个喜欢是否点赞了然后呢下面的这个呢也是一样的对吧那么我们去拿到他的一个这个ID拿到他的一个ID
[17:21] 然后下面这个没有问题然后我们去设置它的一个reg count这样的话逻辑是不是就搞定了那么其实这个逻辑跟我们前面逻辑是一样的只是说我们这个ID会发生变更一下好那么这样的话其实我们这个查询也就搞定了好那么接下来我们来看一下我们的讲义看一下这个代码跟我们写的一样不一样然后在这个位置是不是去拿到一个UIDS
[17:49] 前面这个肯定我们刚才都已经确定没有问题对吧然后呢下面这个我们去写一个这个由来ids然后呢这个还我们去找一个判断其实我们是应该在这个位置应该判断一下这个逻辑我们之前也写过那是在哪里呢是不是在这那么如果有着这个ids中如果我们不包含取反
[18:16] 如果不包含我们这个ID的话那么再把它加进去这个逻辑应该去加一下其实这个可以算作是一个小小的一个优化了好那么然后呢下面呢去做这个查询查询到之后呢去做数据的填充那么填充完成之后呢去查询用户的信息填充用户的信息然后呢去设置这两个这个key对吧然后一个是点赞数一个呢就是我们这个是否点赞
[18:46] 最后呢就去把它加进去然后最后呢就返回回去了OK好那么这样的话呢我们其实已经就完成了一个查询我们这个评论的一个列表好那么关于这个查询评论列表的一个服务接口的提供呢那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Mock 服务中定义一个评论列表接口，并在后端 Java 代码中实现该接口的 Controller 和 Service 层逻辑，包括参数绑定、分页、用户信息关联和数据格式化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Mock 服务界面中，查看接口基本信息，接口路径为 /comments，请求方式为 GET，Mock 地址为 https://mock.boxuegu.com/mock/164/comments，请求头包含 Content-Type: application/json 和 Authorization: Bearer 令牌。
画面 2: 在 Mock 服务界面中，点击“评论列表”后，弹出一个包含多个开发环境截图的预览窗口，展示代码和界面。
画面 3: 在 IntelliJ IDEA 中，打开 CommentsController.java 文件，显示了 @RequestMapping 和 @RequestParam 注解的使用。
画面 4: 在 IntelliJ IDEA 中，展示 CommentsController.java 文件中 queryCommentsList 方法的完整代码，包括 @GetMapping 注解和参数绑定。
画面 5: 在 IntelliJ IDEA 中，打开 CommentsService.java 文件，显示了 @Service 注解和 @Autowired 注解的使用。
画面 6: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的开始部分，包括 PageResult 的声明和初始化。
画面 7: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 quanZiApi 的调用和 PageResult 的赋值。
画面 8: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 QueryWrapper 的创建和 userInfoService 的调用。
画面 9: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 PageResult 的声明和初始化。
画面 10: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。
画面 11: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setLikeCount 和 comments.setHasLiked 的代码。
画面 12: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setLikeCount 和 comments.setHasLiked 的代码。
画面 13: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。
画面 14: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("comments")
public class CommentsController {

    @Autowired
    private CommentsService commentsService;

    @GetMapping
    public PageResult queryCommentsList(@RequestParam("movementId") String publishId,
                                        @RequestParam(value = "page", defaultValue = "1") Integer page,
                                        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
        PageResult_pageResult this.commentsService.queryCommentsList(publishId, page, pageSize);
    }
}
```

画面 4:
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("comments")
public class CommentsController {

    @Autowired
    private CommentsService commentsService;

    @GetMapping
    public PageResult queryCommentsList(@RequestParam("movementId") String publishId,
                                        @RequestParam(value = "page", defaultValue = "1") Integer page,
                                        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
        PageResult_pageResult this.commentsService.queryCommentsList(publishId, page, pageSize);
    }
}
```

画面 5:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Autowired
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 6:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 7:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 8:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 9:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 10:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 11:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 12:
```java
package com.tanhua.server.Service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList

