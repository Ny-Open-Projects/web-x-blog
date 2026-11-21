# 23_app文章列表_逻辑测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\23_app文章列表_逻辑测试【海量资源尽在 666java.com】.mp4
- 时长 9分54秒（音频 594s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们下面呢就来去测一下咱们刚才是写了那么多代码看看到底有没有问题有问题咱们就来调试一下在这啊再去创建一个自由硬的测试com.hematical test 点什么tp article test这里边首先咱们要去集成sperm bootsperm boot test里边给个classes是吧
[00:31] 指定的就是咱们前的这种引导类Article.class好再往下是一个runwaysrunways.classOK那这样的话就集成完了啊要去测试Service所以说咱们在这把它给注入进来就可以了好吧然后是private的一个什么AP serviceArticle Service
[01:05] app article Service好写个测试类呗public test article那这里边咱们要去写啥呢怎么测呢应该想想啊现在呀这个这个里边啊这里边呢是有一个load是吧一个load你只要传不同参数呢它就可以去加载不同的东西那咱们先测第一个啊比如说我现在呀呃传一个参数叫pp什么loadload里边啊
[01:39] 一个是DTO一个是DTO第二个呢是shout就是类型那这个DTO啊我先不传参数我先传一个none行不行啊然后第二个呢咱们就设置一个什么是constants把它去load墨一下好吧load墨啊好返回一个response result那就是result啊好下面咱们去打印一下resultresult.getdata应该是把这个数据给拿到好咱们执行一下
[02:22] 这样的话呢它应该是加载比较多的数据啊稍等有点慢啊好大家可以看一下当前的数据啊其实已经拿到了哎没有问题啊这里边是加载加载的默认应该是20条数据因为咱们的size值它是20即使你传的是none啊因为呢咱们在Service里边去做过处理可以看一眼啊如果说它是none的话咱们就是不是在这儿去设置了一个默认值是20啊
[02:53] 行那这样啊咱们为了能够更方便的能够再去熟悉一下这个逻辑咱们呢可以干嘛呢可以打个断点来在这打断点啊打断点之后呢咱们再来去测一下用debug的方式去测一下咱们走一下这个弹门这个一般一般这个Springboost去测试的时候由于加载的环境比较多所以说呢它有可能会比较慢到后期的话有可能会更慢一些啊行那到这了啊刚才咱们说了啊这个DTO呢咱们传的是一个None那是None的话呢
[03:30] 咱们为了容错性更高所以说呢它是那咱们就创创建了一个空的空的对象是吧这个type呢就是个1ok这已经看到了啊好往下走呗啊教验啊它没有那就是给它重新创建了一下那这些肯定是没有值的往下走啊没有值的话咱们就去重新给它复了一个值是吧好当前时间最小值也是一样啊没有值就重新复了一个当前时间好再往下啊那这个size肯定也是空所以说咱们要去
[03:59] 重新付一个20是吧下面这个就去20就可以了因为它不大于50好再往下走啊嗯这个标签的话应该是没有的是吧没有的话咱们也给了一个标标识默认的标识就是杠杠奥杠杠是吧现在这个参数啊肯定是有值的因为咱们目前的话传了一个typetype就是几啊1是吧就是1啊往下走那当前用户有没有呢那肯定是没有的因为咱们现在呢只是在后台测试咱们并没有往这个线程中去
[04:29] 给他存放当前的用户他肯定是不存在的也就是说他应该会走这个逻辑是吧那走逻辑之后呢他呢是DTO里边是有些值的现在可以看一下应该是有时间是吧还有默认是20还有一个奥是吧最终的咱们就可以去加载出二条文章好可以看一下你看他这个size是不是20啊这样数据是不是就拿到了呀OK啊那行那这个逻辑啊是没有问题的啊
[04:58] 那这个测完之后啊咱们再来测一个测个什么呢测一个当前呢是有用户的情况下看看该怎么去测那有用户的情况下呢其实也很简单这块内容呢主要呢是呃用户信息呢它是从当前的现成是吧Thread local中去拿的咱们只需要往这个Thread local中去存放一个用户信息就完事了那怎么存呢哎在这非常非常简单AP吗threadAPP什么APP Thread
[05:28] localutils.setuseruser没有就创建一个叫apuser等于new一个这时候咱们就可以给个IDID给谁呢为了能够查询出来的东西我在这去加了一层数据并且在这设了一个2104的用户同时对应的article ID是10120
[06:00] 我这边是能够查询出来当前在什么10120的也就是说我查询当前的用户那有用户我就能查出查询出来一条文章信息对吧所以说我当前这个user id应该设置为104这browser加个l啊最终呢你把这个用户啊给存进去这样测可以了啊那咱们呢可以还在这打断点啊这时候呢咱们在这打断点就可以了啊那上面断点把它给去掉咱们直接看一下当前用户
[06:31] 有没有信息就可以好吧他有信息肯定是走这么一段脑袋是吧那行那咱们就来走一下啊第八个走好他这个加载啊速度是刚才说了是有点慢啊大家要耐心等一下正在加载完马上马上结束啊来了啊来了之后呢咱们可以直接往下走看看有没有信息回来你看这个用户是不是已经拿到了是吧这个ID是不是就是2104啊OK那这个既然不等于那的话
[07:10] 这之后呢他肯定是要通过当前的用户是吧还有其他的一些条件呢进行查询那查询啥呢就是通过当前的用户信息查询他用户所拥有的当前的推荐的这种数据列表最终呢咱们把这个数据列表呢作为条件再去查询是吧所以说呢他应该会走到get user article咱们就进去啊点这个进去进去之后呢咱们就来去查
[07:40] 看看有没有它显然它是有一条数据是吧有咱们表中只有一条数据那这种查到这个例子之后呢咱们还要再去查一次因为呢咱们要基于当前的什么这个里边的一个article id然后再去哪啊再去ap article中去查对吧所以说呢咱们还要再去查一次啊咱们想走走好咱们走走走报错了是吧
[08:10] 好,报错了,来看一看报什么错说article id找不着是吧,没有该的方法那咱们这应该是写错了啊咱们打开当前的这个article,article,ap article myper文件里边啊这啊,应该是这块写错了首先呢,这块是,这不是下滑线id啊这个你要知道,这是atom是谁啊它传过来的是一个对象,所以说并没有下滑线那应该是article id,这是跟它的属性要联上的
[08:43] 还有这再补全一下这个时候检查一下这雷道的麦克里边呢你们少了一个这种返回好那咱们再来测一下这个断点呢直接去订入到哪呢来订入到这好吧直接订入到这好把上面断点呢咱们给它去掉好再来测一下啊debug好稍等一下啊好来之后咱们可以来去走一下啊
[09:22] 这个是有一个值刚才说到了就是他现在根据当前用户能够查询出来一条推荐的文章然后往下走走好走咱们看一下Article List里边是不是只有一条数据他这个ID是不是就是10120就是咱们当前对应的
[09:41] 10120啊OK那没问题那这个数据其实也查到了最终它就能够在控制台上给打印出来这条数据好吧那行啊那这个测试啊咱们就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过单元测试驱动开发，验证文章服务加载逻辑，包括SQL动态条件构建、分页处理和数据库查询结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中ArticleTest.java文件，准备编写测试用例，鼠标悬停在@Autowired注解上，提示其作用。
画面2：在ArticleTest.java中，定义了测试类，使用@SpringBootTest和@RunWith注解，准备测试AppArticleService。
画面3：在测试方法中调用appArticleService.load方法，传入null参数和LOADTYPE_LOAD_MORE常量，IDE提示“Expression expected”。
画面4：运行测试，控制台输出Hibernate初始化日志，显示连接池已添加连接，但提示“hibernate.properties not found”。
画面5：测试运行中，控制台输出Spring Boot初始化日志，包括RepositoryConfigurationDelegate的注册信息。
画面6：进入调试模式，查看AppArticleServiceImpl中的load方法，变量dto的size被设置为20。
画面7：调试器中显示dto对象的属性，包括size=20，tag=null，其他字段如provincId、child等为null。
画面8：在测试方法中，IDE提示“Press Ctrl+空格 to choose the selected for first suggestion...”，准备输入代码。
画面9：在测试方法中，创建ApUser对象并设置其id为2104，调用AppThreadLocalUtils.setUser()设置当前用户。
画面10：运行测试，控制台输出Spring Boot启动日志，显示“Started ArticleTest in 10.319 seconds”。
画面11：切换到Navicat，查看数据库表ap_user_article_list，显示一条记录，其中user_id=2104，channel_id=10120。
画面12：在AppArticleMapper.xml中，展示SQL语句，包含动态条件判断和分页限制。
画面13：在AppArticleServiceImpl中，展示getArticleList方法的逻辑，根据用户是否存在返回不同结果。
画面14：运行测试，控制台输出测试通过的日志，显示“Tests passed: 1”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<select id="loadArticleListByUser" resultMap="BaseResultMap">
    select * from ap_user_article_list
    where
        user_id = #{user.id} and is_show = 0 and is_read = 0
    <if test="type != null and type == 1">
        and recommend_time <![CDATA[>]]> #{dto.minShowTime}
    </if>
    <if test="type != null and type == 2">
        and recommend_time <![CDATA[<]]> #{dto.maxShowTime}
    </if>
    <if test="dto.tag == '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag

