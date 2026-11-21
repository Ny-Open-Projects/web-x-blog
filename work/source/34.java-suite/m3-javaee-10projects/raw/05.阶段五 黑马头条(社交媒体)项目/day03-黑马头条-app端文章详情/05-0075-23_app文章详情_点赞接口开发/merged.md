# 23_app文章详情_点赞接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\23_app文章详情_点赞接口开发【海量资源尽在 666java.com】.mp4
- 时长 12分47秒（音频 767s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去做第四个接口就是就是点赞的接口啊这个接口呢相对来说会容易一些因为这个接口呢只需要去做一个保存就可以当用户点赞之后呢咱们应该保存到当前行为啊一条行为就是点赞的记录好吧那这个呢咱们来看一下当前的接口名称哎就是他然后那个DTO呢这里边是有这么一个类这个类呢咱们可以去打开去看一下啊
[00:28] 两个shift然后是去搜一下这个类这里边首先是有一个当前的设备ID然后是当前的entry ID其实这个就是一个文章动态评论的ID到底是哪一个咱们一路在说这个一般情况咱们都是文章当然看它传递过来的内容是啥
[00:49] 然后下面还有一个就是文章的类型啊类型的话到底还是零是文章一是动态啊评二是评论当然一般的话都是零啊都是零啊然后下面还有一个点赞或者是取消点赞啊行那咱们呢下面呢就来去设置当前的一个呃Service或者叫mypro啊首先咱们还是要去创建mypro啊这个这个mypro的话呢刚才说了就只是啥呢只是做了一个保存的操作这个mypro咱们之前是写过的所以说咱们在这
[01:17] 去加这么一个方法就可以打开当前的model然后找到当前的这个lags就是点赞点赞的话是叫APLagsBehaviourMapper然后是这里边找到目前是一个方法咱们再加一个就是保存保存操作好这个保存之后呢咱们在这儿还需要在当前的Mapper文件中去加一条数据那这个呢其实咱们也可以考过来就是insert
[01:57] 嗯行啊这个好像是有问题是吧我们把这个名让稍微改一改好吧就是当前的这个类好背一下考到这考到这之后呢咱们把这个笔记啊也稍微改改啊记就是改成跟这个单板是一样的啊行那就改完之后呢咱们这个麦普尔就算是做完了当然你也可以去看一下当前这个当前的这个插入啊这个插入呢这个idea是自己维护的因为呢他需要通过当前的sirquiz
[02:34] 就是Keyboard生成的自动主件去插入并且Boss咱们也要去设置好吧其他的资讯的话就包括当前的设备IDEntryID就包括就是当前咱们说的你到底是文章评论还是动态等等这个是类型还有一个是点赞或者是取消点赞的一个操作创建时间还有一个Boss好吧那行那这个是咱们的一个Maple文件然后下面咱们就去
[03:02] 写当前的Service代码那这Service呢这一块呢是需要去从当前的行为的微服务模块中去定义这时候咱们可以啊在这去创建一个Service打开behaviour然后是找到Service在这啊去创建一个类这个应该是个接口是吧叫啥呢咱们叫applikelike啊like啊behaviour
[03:36] 然后是Service好吧这里边是有一个方法一个方法的话其实就是当前的一个保存public response without然后是一个save legs legs behavior好了这里边参数其实就是当前的这个类当前这个类拷贝一下然后是拷到这对应该是它应该是一个dto
[04:08] 这个dto是谁呢这个dto应该是前面这个参数是吧是lag becover dto好放下包dto这里边有啥呢刚才也看了这里边其实刚才咱们这个这几个参数咱们已经说完了行咱们下面就来去做具体的操作来编写它的一个什么它的一个实现类在这再去创建一个类然后是叫impl让它去实现前这个接口ctrl i好
[04:43] 那时候去加一个Service好了啊这里边该怎么去写呢这写的话其实很简单这个呢就是跟咱们之前写的那种行为呢其实差不多的首先呢你也要去拿到当前的行为实体那这个呢其实跟咱们之前代码是差不多的啊我直接去直接从这烤过来了啊用这个呢都是一样的直接烤到这烤一下然后在这去加一个东西当前的这个东西没有是吧没有就定义一下啊
[05:14] Providebit然后是叫APDHiver MyPro然后注入进来就行了这个会报错我们就加一个super warning好吧那这个加完之后这个当前的行为实体就算是拿到了拿到了之后咱们就可以进行保存了如果说他到这一块还没有问题咱们就保存呗保存谁呢就是保存当前的这个Likes点赞
[05:47] 所以说你要把当前的接口我这个MAP文件给注入进来就是APLexMapperXCoverMapper把它注进来之后咱们再去设置把它来去点里边是有一个叫做insertinsert的话需要去有一个对象是吧咱们在这去手动去创建一下APLexCoverOK
[06:18] 到ARB好吧,等于new一个APlex.bhav好这里边咱们就可以去设置值了.setid这个id是需要自己维护的刚才单面也说了这个是由circuit去创建所以说呢想去用的话在这去创建一个circuit这个主keeper这个是不是已经倒进来了啊比如说在这去加一个circuit好,注入进去了啊注入完之后呢咱们可以去拷贝一下啊
[06:53] 拿到当前的一个likes就拿到这个ID了啊行咱们再往下看看还有什么需要去设置set前的一个叫做behavenid啊这个呢其实就是当前的他的ID对吧我背下他getid这样就拿到了啊然后再往下看还有啥呢还有一个是set create time好吧这个就很简单啊这就直接用个date就可以了又一个
[07:24] 好这个有问题吗crate time youtube这不是youtube吗导播导错了吗我看看啊嗯java youtube date没问题啊那为什么报错呢看看删了重新来irb.setcrate time这个date是吧一个好没问题啊然后再往下看irb.set什么呢
[08:00] 我们要去设置一个entry id那这个entry id其实咱们再往下看这个entry id其实就是dto中的entry iddto我用dto吗我看啊dto.get entry id这个到底是传的是啥那就看前台了好吧然后再往下看lb.set当前的一个operationtype也行type type的话就是dto的好吧然后再往下
[08:31] ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB ARB
[09:01] 第一个呢就是ARB的ID第二个值呢第二个值的话应该是当前的实体ID当前的实体ID啊当前的实体呢是这个东西是吧所以说你可以直接去把它给拷过来就可以了当然标准心法应该这样写ARB.NET BEHIND NETID那这样写是最好的好吧那这个设置完之后呢你可以把它呢去直接去保存就可以了保存完之后它有一个返回值
[09:32] 看一下啊还是有一个insertok没问题咱们在这啊去直接raisebounceresult.ok来个insert装进去就完了这个就是保存的一个数量这个呢其实就是咱们之前说过的啊这个东西啊就是行为尸体然后后面是要去保存当前的lagsok那完了啊那这个Service写完之后呢咱们顺便啊再去写一下
[09:58] 当前的一个Controller这Controller的话其实更简单一些咱们首先还是得去在哪去定义在当前的APIS里边找到这里边少东西是吧咱们再去加个东西加一个包包呢叫behind.apis好吧然后在里边去创建一个接口吧接口呢咱们叫做我看看叫behindbehind我看稍等这个是吧
[10:36] BehaviourControl API好保存一下这里边咱们是不是创建过这是有一个是吧有一个的话那这样咱们就还是在这样咱们把它给挪出来好吧Behaviour就Behaviour咱们这件事定义错了直接把它挪出来挪出来之后咱们就放到这继续好挪出来之后咱们再去这里边再去新建一个方法就可以了方法就是去保存当前的一个这种
[11:15] 保存点赞行为好吧然后在这去设置一个还是RacePunksResult然后下面是有一个SaveLegs然后Behaviour好参数呢就是刚才说的参数就是LegsLegsBehaviourDTODTO好了啊那这时候咱们就说完了啊说完之后呢咱们再去写前的一个类那这个就是Controller啊
[11:48] 打开它打开它打开它然后咱们再去找到它其实这里这里咱们以前也创建完了直接让他再去重写这个方法就可以了Ctrl alt加iCtrl i那这时候咱们就可以去入当前的一个serviceprivate是哪个Service是app叫app legslegs-becover-Service是吧然后是它
[12:22] 之后咱们就直接去不用就可以了直接去调用.save把这个DTO传进去,完事了好吧那目前的话这个咱们就算是做完了这个测试咱们目前就不测了到后期咱们集成前端之后咱们再一块再去测试好吧行那这个就是点赞接口

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现点赞行为的 Service 层代码，包括定义接口、实现类、使用 MyBatis-Plus Mapper 进行数据库操作，以及 Controller 层的调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，选中 `heima-leadnews-user` 模块，准备进入 `heima-leadnews-behavior` 子模块。
画面 2：在项目结构中选中 `heima-leadnews-user` 模块，准备进入 `heima-leadnews-model` 模块。
画面 3：展示 PPT 内容，讲解 `ApLikesBehaviorMapper.xml` 中的插入语句和 `ApLikesBehaviorService` 接口定义。
画面 4：在 IDE 中打开 `ApLikesBehaviorService.java` 文件，开始编写接口。
画面 5：在 IDE 中打开 `ApLikesBehaviorServiceImpl.java` 文件，开始编写实现类。
画面 6：在 `ApLikesBehaviorServiceImpl.java` 中编写实现类，导入必要的包并定义类。
画面 7：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 8：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 9：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 10：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 11：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 12：在 `ApLikesBehaviorServiceImpl.java` 中编写 `saveLikeBehavior` 方法，调用 `apLikesBehaviorMapper.insert()`。
画面 13：在 IDE 中打开 `BehaviorControllerApi.java` 文件，准备编写 Controller 层代码。
画面 14：展示 PPT 内容，讲解在 `BehaviorController` 中实现 `saveLikesBehavior` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```xml
<insert id="insert" parameterTypes="com.heima.model.behavior.pojos.ApLikesBehavior">
    insert into ap_likes_behavior (id, behavior_entry_id, entry_id, type, operation,
    created_line,burst)
    values
    #{id},#{behaviorEntryId},#{entryId},#{type},#{operation},
    #{createdTime},#{burst}
</insert>
```
画面 3：
```java
public interface ApLikesBehaviorService {
    /**
     * 保存点赞数据
     * @param dto
     * @return
     */
    ResponseResult saveLikeBehavior(LikesBehaviorDto dto);
}
```
画面 6：
```java
import com.heima.behavior.Service.ApLikesBehaviorService;
import com.heima.model.behavior.pojos.ApLikesBehavior;
import com.heima.model.common.enums.AppliCodeEnum;
import com.heima.model.user.pojos.ApUser;
import com.heima.utils.threadlocal.AppliedLocalUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ApLikesBehaviorServiceImpl implements ApLikesBehaviorService {
```
画面 7：
```java
    @Override
    public ResponseResult saveLikeBehavior(LikesBehaviorDto dto) {
        //获取用户信息，获取设备id
        ApUser user = AppliedLocalUtils.getUser();
        if(user==null||dto.getEquipmentId()==null){
            return ResponseResult.errorResult(AppliCodeEnum.PARAM_INVALID);
        }
        //获取行为实体
        ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(dto.getEquipmentId());
        if(apBehaviorEntry==null){
            return ResponseResult.errorResult(AppliCodeEnum.PARAM_INVALID);
        }
        ApLikesBehavior alb = new ApLikesBehavior();
        alb.setBehaviorEntryId(apBehaviorEntry.getId());
        alb.setEntryId(dto.getEntryId());
        alb.setOperation(dto.getOperation());
        alb.setType(dto.getType());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user.getId());
        alb.setCreatedTime(new Date());
        alb.setBurst(BurstUtils.encrypt(alb.getBurst()));
        alb.setUserId(user

