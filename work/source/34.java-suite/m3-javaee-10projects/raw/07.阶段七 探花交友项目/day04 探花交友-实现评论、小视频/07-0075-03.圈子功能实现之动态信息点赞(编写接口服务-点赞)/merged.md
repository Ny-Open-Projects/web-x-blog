# 03.圈子功能实现之动态信息点赞（编写接口服务-点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\03.圈子功能实现之动态信息点赞（编写接口服务-点赞）_【海量资源尽在 666java.com】.mp4
- 时长 12分42秒（音频 763s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来编写我们的服务的接口那么前面呢我们已经完成了double接口的一个实现那么下面我们来看对接到我们APP应用中的这个服务接口那么首先呢我们来看一下它的一个接口的一个路径啊是这样的一个路径啊这样的路径然后呢它的Mock地址呢是这样的一个Mock地址然后呢我们可以看到在我们的这个参数这个位置啊
[00:30] 就是在参数这个位置呢是通过我们的这个ID去做一个传递当然这个ID呢就是我们动态ID也就是我们那个publish ID那么下面这个就是他的这个请求的参数啊然后呢呃注意他的一个返回值啊返回数据的一个类型呢是什么呢是我们的这个在我们响应的时候呢需要去返回数据返回谁呢返回一个int类型的
[00:55] 这样的一个值其实就是点证数啊就最后呢要返回这个点证数啊那么接下来呢我们就将来实现一下它啊那么首先呢我们来找到我们的server这个工程来看一下那么server这个工程那么我们首先呢来编写我们的Controller啊然后呢在就在这个里面这个里面去编写我们Controller的方法那么public哎嗯public然后呢返回值呢
[01:24] response.edit然后呢这个t我们存放的是什么呢那么t存放的那我们其实不用返回它了我们直接返回这个lang就可以了对吧就是我们的这个数量这个数量然后呢我们叫什么呢这个叫like对吧like comment然后呢我们写一个方法叫做request叫get mappingget mapping
[01:52] 然后get mapping呢是请求的是get请求然后呢这个它的路径呢前面会有一个这个ID对吧那我们把这个就拷贝过来那我们来这样写一下那么大家没有前面这个S啊那么这个我们需要去通过一个大括号把它做一个站位然后呢下面我们来获取它的一些这个参数那我们通过这个pass variable去做一个
[02:18] 获取叫什么呢ID那么这个其实拿到了就是谁呢我们的public IDID拿到它那么拿到这个public ID之后呢我们就可以去做一个这个操作了那么下面呢我们就通过我们这个Service然后这个moments Service然后点那我们就叫什么呢likecomment然后呢我们把这个public ID呢传递过去
[02:47] 那么它的返回值呢其实我们所期望的它返回的是一个浪类型的一个什么呢count啊就是这个数量啊那么我们希望它返回这样的然后呢如果这个空等于count的话啊如果等于count的话那就说明我们这个点赞是不是失败了那么失败的话那我们还是需要状态码那还得写这个啊直接写个浪还不行因为还是要有这个状态码啊
[03:14] 那么如果它等于空的话那就return吧return这个additive然后呢来一个stateshttp然后呢states点internal server arrow然后呢build然后呢如果这个是等于空的话是返回500那如果不等于空的话那我们就给它响应那我们是不是应该这样去写我们把这个写成什么呢
[03:42] 这个如果不等于空的话那么反一下啊把这个呢先拷贝到下面来吧如果不等于空的话那就应该直接OK就可以了这样的话会比较方便一些那么把counter往这一丢好嘞那么一旦啊等于空或者是我们会出异常的话啊那么我们就去走到下面这个逻辑来那么这个呢其实就是我们的一个点赞的这样的一个操作啊
[04:07] 点赞的一个操作好那么接下来呢我们就实现Service中的这个方法啊那我们来生成一下这个方法啊ok那么好那么这个逻辑呢我们来编写一下那么首先呢我们来拿到这个user这个对象啊肯定是和用户相关的对吧那么一定要先拿到这个userservilocal.get然后呢下面呢我们再来去做一个操作
[04:33] 那么我们将通过我们的这个叫做圈子API然后呢我们去做一个这个操作叫sell like comment需要两个参数那么第一个参数呢就是user.getid那第二个参数呢就是这个publicid啊publicid然后它的返回值呢就是我们这个boot啊它的返回值就是这个boot所以呢在这个位置呢我们去需要去判断一下
[05:01] 如果这个布尔值等于fos的话就是就是我们这个保存失败了对吧那我们就应该return down对不对啊return down然后呢下面呢是不是就这个到这儿啊我们来加一个做事啊这个就是我们的一个这个保存失败啊保存失败那么下面呢是保存保存成功啊成功啊保存成功那么
[05:26] 我们这个是保存成功那么接下来往下面呢我们就需要去什么呢去获取它的一个什么点赞数那就是我们去获就是我们点赞之后啊它的一个数量那么这个点赞这个数量呢大家可以想一下那么我们这个数量是我们去从我们的mongodb去查询呢还是我们应该从我们的redis做一个查询大家可以思考一下啊
[05:54] 那么其实我们显然更好的一种方案呢就是通过我们的这个redis去做一个查询为什么呢原因是呢我们这个数量它其实是需要去缓存起来并且呢我们会有很多地方呢需要这个数量那我们直接去通过mongodb去查询数量的话这个效率呢就比较低了所以说我们直接可以把这个数量呢去缓存起来那么接下来呢我们就来看一下这个应该怎么去做啊
[06:23] 那么我们需要去先去我们的ready时钟是不是去先去做一次这个查询对吧那么如果能够查询到的话那么我们就直接去做一个返回如果要查询不到的话那么我们是不是就应该去拿到它的一个总数然后再去做这样的一个记录对吧所以说有这样的一个逻辑在里面
[06:49] 那么我们首先呢先把我们的这个readys的template呢去注入进来那么叫做呢readys啊template去注入进来那么这个呢是street啊street呃然后呢我们去来写一下这个叫readys的template去做一个注入呃那么下面这个代码我们就方便去写了那么首先呢我们需要去定义一个我们的一个呃叫做key对吧就readys的key那么叫like
[07:19] 然后呢ready like commentkey它等于什么呢我们是不是应该就写的比较全一些啊那我们可以来参考一下我们的讲义啊那么讲义呢是在这个位置的我们去考下它啊这个是我们的一个key然后呢再去加一个publish idpublish id那么下面呢我们就先去做一个判断
[07:46] 就是我们通过我们的这个圈子哎不是圈子然后呢是readies啊template然后呢我们去判断一下它是不是去呃包含了我们这个key对吧呃如果如果要是包含了这个key的话那么呃我们先来看一下如果不包含吧先处理这个不包含那么如果不包含这个key的话那我们就需要去查询一下我们的数量了啊那么就通过这个圈子点
[08:16] query count对吧一个是publish id那么另外一个就是type那么我们点赞是1所以传递1然后它的值拿到的是一个count然后上面我们还需要去先去记录一下这个long行的一个叫like count先等于00l
[08:46] 那么这个count数啊它其实就是我们这个like数了对吧那么like count等于这个count去做一个复制然后呢我们就需要把它去写入回去对吧然后呢来一个ops然后呢点set操作那么这个key呢那就是我们的这个like a common key然后呢value呢那就是我们这个like count
[09:12] 这个是我们的一个啊这是我们的一个这个来个counter这样的一个呃数量对吧然后他说这个是要存储的是一个支付券那么我们就写一个吧然后呢写一个street啊street.valueof啊valueof.valueof然后把它拿过来好那么这是如果不存在的这个情况啊那么如果是存在的情况那么会
[09:42] 怎么样呢那么如果存在呢那我们就需要去拿到我之前的这个值是不是去做一个加1的一个操作对吧那么我们就应该是叫直接去做一个递增啊是不是就可以了那么把这个k呢传递给他去做一个加1啊这样的一个操作然后呢他的值最后他的返回值就是增加之后的值那么他就应该等于这个来个count
[10:07] 那么最后我们所返回的是不是也是这个LagCount那么下面这个其实还有一个小逻辑需要我们去编写啊什么呢大家可以看一下这前面啊前面呢我们在这个位置会有一个数值就是说我们是否喜欢是否点赞那么下面在这个位置那么就需要去做一个记录就说我呢就当前这个用户他已经点赞过了那么这个应该怎么去做呢我们再去定义一个
[10:36] 定一个这个叫做law吧law然后comment然后呢key等于什么呢就等于这个等于它然后呢我们其实应该写一个什么呢叫和user相关的对吧就是记录哪一个用户那么我们去加一个这个用户叫做user.getid然后再加一个小滑线就是说我这个我这个什么呢我这个用户啊那我这个用户
[11:07] 对这个就是这个动态的已经点赞过了那我就做一个标记啊那么怎么做标记呢那我们直接去写然后呢点set一个key那就是这个low comment key然后呢这个值呢我们就直接去写一个1做一个标记就可以了做一个这个标记好嘞好那么这样的话呢我们是就完成了那么这个呢是这个用于记录记录什么
[11:36] 记录这个这个什么当前当前用户已经已经点赞已经点赞好嘞好那么这样的话呢这个是不是就搞定了就搞定了好那么接下来呢我们就来看一下先来看一下我们的讲义吧下面我们来再做测试啊那么这个是我们服务的一个定义啊服务的一个定义这个点赞啊下面这个是取消点赞那么一会儿我们再来去做这个取消点赞
[12:06] 然后呢下面呢我们具体的一个实现呢是在这个位置对吧这个是我们那个点赞的这样的一个实现哎OK那当然在我们讲一中这个逻辑呢会有点问题啊这个其中我们是不需要去加一的啊直接去做复制啊就可以了那么因为之前的已经就把它啊就加进去了对吧已经保存了一条了那我们直接查询的就是最新的啊这样的一个抗的数量了不需要加一啊然后呢直接去保存最后呢去做一个
[12:36] 点赞的一个赞的一个记录啊就OK好那么关于我们这个服务的一个编写呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现点赞功能，包括定义接口、编写控制器、服务层逻辑以及与 Redis 和第三方 API 的交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了接口文档页面，接口路径为 GET /movement/{id}/like，请求头包含 Content-Type: application/json 和 Authorization: Bearer <token>。
画面 2: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，其中定义了 @Param 注解的 page 和 pageSize 参数，以及 @GetMapping("/like") 方法的开始部分。
画面 3: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，正在编写 @GetMapping("/like") 方法，参数为 @PathVariable("id") String publishId。
画面 4: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，@GetMapping("/like") 方法已定义为返回 ResponseEntity<Long>，并开始编写业务逻辑。
画面 5: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，@GetMapping("/like") 方法中添加了 try-catch 块，用于处理异常并返回 ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面 6: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 likeComment 方法，其中调用了 quanZiApi.saveLikeComment。
画面 7: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，定义了 @Reference 注解的 quanZiApi、@Autowired 注解的 picUploadService 和 userInfoService。
画面 8: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。
画面 9: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 redisTemplate 的相关代码，用于操作 Redis。
画面 10: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 11: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 12: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 13: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。
画面 14: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@Param page
@Param pageSize
@Return
```
画面 3:
```java
@GetMapping("/id/like")
public Long likeComment(@PathVariable("id") String publishId {
```
画面 4:
```java
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId {
```
画面 5:
```java
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId {
    try {
        Long count = this.movementsService.likeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```
画面 6:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    this.quanZiApi.saveLikeComment(user.getId(), publishId);
    return null;
}
```
画面 7:
```java
@Service
public class MovementsService {
    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;
    @Autowired
    private PicUploadService picUploadService;
    @Autowired
    private UserInfoService userInfoService;
    private RedisTemplate<String, String> redisTemplate;
```
画面 8:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLikeComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    Long likeCount = 0L;
    //保存点赞到redis
    String key = "QUANZI_COMMENT_LIKE_" + publishId;
    if (this.redisTemplate.hasKey(key)) {
        Long count = this.quanZiApi.queryCommentCount(publishId, 1);
        likeCount = count;
        this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
    } else {
        likeCount = this.redisTemplate.opsForValue().increment(key);
    }
    return null;
}
```
画面 9:
```java
private RedisTemplate<String, String> redisTemplate;
```
画面 10:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 11:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 12:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 13:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLikeComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    Long likeCount = 0L;
    //保存点赞到redis
    String key = "QUANZI_COMMENT_LIKE_" + publishId;
    if (this.redisTemplate.hasKey(key)) {
        Long count = this.quanZiApi.queryCommentCount(publishId, 1);
        likeCount = count;
        this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
    } else {
        likeCount = this.redisTemplate.opsForValue().increment(key);
    }
    return null;
}
```
画面 14:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8 和 13: PPT 标题为“day04 评论.md”，内容包括“点赞功能”、“保存点赞到 redis”、“获取点赞数”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

