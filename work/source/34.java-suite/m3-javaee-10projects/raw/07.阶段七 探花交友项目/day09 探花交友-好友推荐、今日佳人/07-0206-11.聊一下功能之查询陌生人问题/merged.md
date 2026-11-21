# 11.聊一下功能之查询陌生人问题

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\11.聊一下功能之查询陌生人问题_【海量资源尽在 666java.com】.mp4
- 时长 6分3秒（音频 363s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个聊一下这个功能啊那么这个功能呢是在我们进入我们这个详情这个页面之后然后点击这个聊一下那我们这个功能呢需要有两个接口的一个支持那么第一个接口呢就是去查询啊对方设置的这个问题那第二呢就是提交这个答案
[00:22] 那么提交答案之后呢我们需要给对方的去发送一个消息啊这一点要注意所以说呢我们需要去做这么两件事情啊那么首先呢我们先来做第一件事情就是查询对方设置的一个问题那么他所对应的一个Mock接口呢是在这里那么我们来看一下啊那我们来找一下吧是在我们的这个这个里面有一个交友然后呢有一个查询陌生人的问题
[00:48] 然后呢我们可以看到查询的参数呢就是一个用户ID然后返回的就是这个一个字幕刷就是这个问题好那么下面我们就来实现啊那么我们接下来首先来设计它的一个表结构那么就是叫做TB啊叫Question然后呢这个呢就是有几个字段我们来看一下啊那么有这个ID有用户ID还有这个Text就是我们的这个问题的一个内容
[01:16] 然后呢还有创建时间啊更新时间啊那么它的组件啊以及它的一个索引啊然后呢我们下面插入两条这个测试数据好那么接下来呢我们来操作一下那么我们去拷贝一下它然后呢找到我们的这个有个叫麦看花然后呢我们来执行哎来执行一下这个售后语句啊走那么这个呢就OK了那么下面把他呢也啊拷贝过来走
[01:46] 那么我们来看一下我们的这个数据啊啊刷新一下然后呢在这啊然后呢是不是有这么两条数据啊那么我们给用户ID呃唯一的这个用户呢设置了一个问题那么用户ID为57的这个用户呢也设置了一个问题啊那么为什么要给他设置呢原因就是呃我们这个金日嘉仁中呃是不是我们就是这个57这个用户啊那么方便我们测试啊就给他设置了这样的一个问题
[02:14] 那么接下来呢我们就来看具体的这个实现那么接下来呢我们就来编写我们这个question这个对象那么这是我们的一个实体对象那么我们来拷贝一下把它呢就拷贝到我们的这个server这个server这个里面来那么我们找到我们这个就是叫一个什么呢pojo那么拷到这个里面来
[02:39] 然后呢主要呢是有三个字段啊然后它继承这个base puzzle那就会拥有了created和update两个字段然后呢接下来呢我们就来去编写它的一个Mapper那么拷贝一下然后到我们这个里面来这是我们的一个question这样的一个Mapper然后呢我们下面来看Service啊Service那么在我们Service中啊那么需要去注这个
[03:05] question的一个map然后呢我们去做一个question的一个查询根据用户ID啊这个查询就非常简单了那我们就不做这个实现了我们就直接来拷贝吧我们就丢到这个里面来好嘞那么这个呢就OK搞定了对吧好那么把这个也关掉那么接下来呢我们就来实现我们的一个这个接口那么我们在我们的today best中然后呢去编写这个Controller然后呢我们去把它呢来拷贝一下
[03:34] 那么找到我们的一个就是today best的一个这个Controller然后呢把它呢就丢进来然后呢我们去实现这个方法就可以了然后它的一个体积参数呢就是uid那么我们去创建我们的这个方法创建这个方法然后呢我们去实现它实现非常简单就调用这个Service去查询然后最后return就ok了
[04:01] 那么我们就不做具体的一个实现码很简单那么当然这个question的一个Service那么我们需要把它注入进来我们注一下然后Service把它就注入进来把它注入好嘞好那么注入进来之后就可以去使用它了去做一个查询了那么接下来我们就把我们的这个server重新跑起来那我们来测试一下
[04:29] 好那么我们来看一下我们的这个接口啊它所返回的就是我们的这个问题对吧刷新一下如果我们把它设置为1的话那就是查询用户ID为1设置的这个问题那么我们还是查询这个57啊那么57然后呢去做一个查询那就是这样的一个问题了那么接下来呢还是我们把模拟器呢跑起来那我们来看一下它的一个效果
[04:56] 好那我们来测试一下那么还是去通过这个02026868这个用户去登录一下然后呢我们去123456然后呢我们去进入到我们的首页然后呢我们就去点击我们的今日家人然后呢这个是57这个用户啊然后呢我们点击这个聊一下那么其实可以看到是不是已经出现了这个
[05:22] 问题了那我们就可以输入这个问题了对吧输入这个问题呢就可以去比如说我们输入这个问题比方喜欢什么颜色呢我喜欢这个红色这个可能是输入法的问题那么至少我们现在看到它是不是可以去输入这个显示这个颜色显示这个问题然后呢我们去输入比如说我喜欢这个红色好嘞那么这样的话我点击聊一下就可以了那么但是我们聊一下还没有实现好嘞
[05:53] 好那么这个呢就是我们的一个这个查询陌生人这样的一个问题啊OK好那么关于我们这个查询陌生的问题呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过后端服务查询并展示陌生人问题功能，涉及数据库表、Mapper接口、Controller和Service层代码实现，以及前端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Typora文档中“4.5. 查询陌生人问题”章节的目录结构，当前聚焦于“4.5.1. TodayBestController”。
画面2：展示API文档页面，其中“请求参数”表格显示“名称: string”，“是否必填: 是必填”，“备注: 陌生人问题”，“示例: 你喜欢什么颜色?”。
画面3：Navicat Premium中连接到MySQL数据库，显示数据库列表，当前选中“mytanhua”数据库。
画面4：在Navicat中打开“tb_question”表，显示两条记录，第二条记录的“txt”字段内容为“你喜欢什么颜色?”。
画面5：IntelliJ IDEA中打开“MovementsController.java”，代码中包含@GetMapping("/all")方法，用于查询相册列表。
画面6：Typora文档中展示“4.3. QuestionMapper”部分，包含一个接口定义。
画面7：IntelliJ IDEA中打开“QuestionMapper.java”，显示一个空的接口定义。
画面8：IntelliJ IDEA中打开“Question.java”，显示一个包含@Data、@NoArgsConstructor、@AllArgsConstructor注解的实体类。
画面9：Typora文档中展示“4.5.1. TodayBestController”和“4.5.2. TodayBestService”章节，显示TodayBestController的@GetMapping("/strangerQuestions")方法。
画面10：IntelliJ IDEA中打开“TodayBestService.java”，显示@Service注解的类，包含@Autowired注入的UserService、UserInfoService、RecommendUserService，以及private Long defaultUserId字段。
画面11：IntelliJ IDEA中显示TodayBestService.java的代码，包含queryTodayBest()方法和queryQuestion()方法，以及控制台输出的Dubbo服务调用日志。
画面12：电脑桌面，显示“黑马程序员”和“博学谷”标志。
画面13：Genymotion模拟器中打开应用，弹出对话框“对方设置了问题”，问题为“你喜欢什么颜色?”。
画面14：Genymotion模拟器中，用户在输入框中输入“red”，点击“下一步”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5代码：
```java
@GetMapping("all")
public ResponseEntity<PageResult> queryAlbumList(@RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @RequestParam
        @

