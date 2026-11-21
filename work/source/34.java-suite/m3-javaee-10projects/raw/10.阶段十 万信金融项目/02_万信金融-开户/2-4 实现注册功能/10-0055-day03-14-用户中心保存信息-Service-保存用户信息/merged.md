# day03-14-用户中心保存信息-Service-保存用户信息

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-14-用户中心保存信息-Service-保存用户信息_【海量资源尽在 666java.com】.mp4
- 时长 16分21秒（音频 981s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们把校验手机号是否存在这个功能实验完之后呢接下来呢咱就该实现注册功能就是保存用户相关的信息那我先问大家一个问题我们为什么要这么一个功能啊就检查手机号是否存在这个功能为什么呀所以从业务上来讲我们要实现注册必须得先检查这个用户是新用户还是老用户注册一定是针对什么呀新用户新用户他的手机号一定是什么呀不存在
[00:31] 所以说我们一定是在注册的时候一定是要先调用这个方法确定一下这个用户的确是新用户然后我才进行什么呀注册了对吧所以从业务上一定要知道咱为什么要写这些代码那这个register呢就是实现注册那他实现注册的话首先进来就得先调哪个方法对checkmobile我得先确定你是新用户然后我才搞注册那我们就进行一幅判断呀看看他到底是不是新用户啊
[01:02] 这里边我们只需要调用这个谁啊check什么呀目标这个手机号怎么办那手机号自然是从这个dt对象里边取出来啊这个将来一定是前端传过来的那这就是consumerdto.get什么呀对目标传进去就行了那他将来的反应值长什么样对01嘛1就表示存在0就表示什么不存在那我怎么判断我就判断他等于什么呀1吧
[01:36] 那等于就意味着它是什么呀存在了也就是说它不是新用户那老用户你还注册啥错啥热闹对不对那我就给你抛一场我说抛一场因为大家一定要注意这个reject的方法我们设计的是没有反应值那我们的意思呢就是要在这里边抛什么抛一场不再设置什么反应值那既然是老用户你就别凑热闹了我就给你抛一个异常吧此时候你有抛什么异常呢还是咱以前见过的business
[02:08] 咱自定义的这个业务异常就这然后呢具体的这个信息我们从一个类当中直接拿叫consumer error code这个类应该也不存在咱直接拿过来用啊去公共类里边找一找叫哪个呀就是他这个类是要粘到什么地方呢咱需要查一查看看啊consumer command这么长
[02:41] 咱看一看consumer有没有comment包有是吧然后他还需要在comment包里边再建一层我觉得建不建都行你想建也可以不想建的话你就可以把这一层你干什么删掉就行了是不是好转过来OK这个类就有了这个类大家看还是美剧类还是美剧类这里边是不是定义好了各种提示内容我不存在失败开户失败等等好多咱后边都要用
[03:13] 这个你直接粘过来用就行了不需要自己编写了看懂这个代码就OK了那这里边呢咱就要用这个类了啊我们直接写直接写什么呀直接写这个类叫consumer腰长啊consumer c o n s u m e r e r r o rcode点谁呢我们这个应该是用户已经存在的吧是不是已经存在的话你看是哪个107吧
[03:44] 对用户一存在我就把这个异常给他干什么呀抛出去这是我们在注册时候先要进行的一步啊判断啊这个判断搞定了之后呢那如果没抛异常就证明他是一个什么呀新用户那接下来我就要做什么操作对保存操作保存操作呢大家应该有印象还是调哪个方法save呗是不是那你看这个save方他要的是什么consumer对象consumer但是我现在手头上有的是谁啊
[04:17] 是DTO对象接下来要干什么你应该心里清楚了吧这种套路咱们在前面Account那边是不是也玩过嘛对不对所以说那咱接下来只能是把DTO里边属性的值取出来然后再存到什么呀Consumer这个对象里边说接下来还是如此我自己呢单独直接NEO一个什么Consumer然后呢就开始干什么呀取数据是吧
[04:49] 然后DTO调用getter方法然后consumer这边调用什么setter方法咱原来反正是这么干的但现在我觉得有点傻有点傻有点费劲咱不是这个见过这个东西吗是不是那你觉得我现在用它可以吗肯定可以对不对它不就是专门干这活的吗然后改一改这应该写啥对这应该写DTO就是它
[05:26] dto 后边应该写什么呀concel more这个方案什么意思前面说过对这个copy properties这个方案的作用就是把这个对象里边所有属性的值取出来然后复制给这个对象这比如说咱正想要的功能复制完之后咱就可以进行什么对save保存了con sumer没错但是这个地方大家要注意因为它这个dto里边的东西比较少
[05:58] 或者说呢它里边都有些值呢是前端没有提供的都有哪些值前端没提供呢那随便点开一个这个类我们进去看一下我们看看这个谁呀都没打开吗DTO吧随便啊比如这些状态还有可贷款的额度是不是已经绑定银行卡这些东西呢前端在传的时候呢是不包含这些信息了没有这些信息那因此呢这些信息我们只能是在业务层
[06:34] 你说在这个地方咱人工的给他付一些什么呀默认处置值说这些我们要给大家补一补也就是说呢consumer这个对象里边的某些属性的值需要在这咱人工给一下因为钱呢不提供就这意思那都有哪些呢咱一个一个来吧consumer点首先是有一个叫setuser number对user number就是用户的一个编号这个用户编号呢我们要求是不允许重复的
[07:11] 那因此我们需要怎么着生成一个不重复的一个一个一个字幕刷一个值那这个怎么办呢我们有工具类写好的现场代码咱直接拿用一下这工具类呢就是code number youtube对那它呢里边呢有一个方法就是专门生成这个用户编号的叫get number对就是get number那它里边呢又要一个什么东西一个一个一个前缀啊
[07:42] 我先把代码给你写完然后我们再看里边的东西叫code prefix code这里边的话我们是加了一个consumer的一个前缀就是这个东西把它写上就行了那具体都是什么意思呢咱接下来看一看这些类里边的这个原码这个什么呀get稍等比较卡我们直接去苦难工程里边找这个应该是谁呀一个工具类code youtube
[08:26] 就是他里边呢有一个就这一个方法get number对不对就是生成一个一个他使用的是uid底层对不对生成一个用户编号就是不重复的一个用户编号但是呢他这里边要求你告诉他要不要加钱费加还是不加加加什么样的钱费这个钱费呢是在code prefixcode里边那我们找一找这个东西是在什么地方找不着的话你可以看这个他导入的这个包嘛
[08:57] 在读闷里是不是这不是吗因为这里边啊他也是一个美举啊也是一个美举你看不使用啊使用啊使用什么样的呢你看我们这个consumer这一块consumer这一块一定要注意我们整个统一了一下啊consumer的这个用户编号前面都加了一个usr杠啊这样一个前缀所以我们刚才取的是这个值吗就这个意思啊这个代码呢你大概自己瞅一眼就能看懂说这是我们人工的给他提供了一个用户编号
[09:30] user number这个值呢我们给过之后呢接下来还有一些属性的值需要我们在这人工给我们可以打开这个表看一眼好像吗这个表你看刚才是这个吧user number你看到这说了吗用户编码生成的唯一的对不对至于它将来有什么用到时候再说啊反正有些值咱需要给还有谁还有这个哪呢是否绑定银行卡一字棒的什么看咱把这个值也给了
[10:00] consumer.set is bondcard那你觉得我们现在应该给什么值它是一个整数你看它是新用户现在刚注册你觉得它绑定银行卡了吗它上还没有走到那一步呢对不对所以说这默认值一定是什么呀00表示没绑定吧这都是默认出的值还有什么呀还有一个什么呀我们看看啊
[10:27] 呃这些东西咱暂时都不用管后边用到的时候再说还有一个状态这些咱都暂时都不用管吧都不用管咱就再加这一个就行了啊这个加好之后呢咱就可以直接进行什么呀save了也就是说呢consumer对象里边有一部分属性的值是从这来的还有两个属性的值是不是咱在这人工给的默认数值那么这些东西都给了之后最终就可以进行什么呀对保存了
[10:55] 这就是咱们业务层的代码最后呢别忘了啊很关键的一个注解咱可不能忘家就是谁啊Service没错这个注解忘了家的话将来扛出了就没法调用什么呀对Service那这是咱业务层的代码就写完了啊两个方法一共啊一个是check mobile检查这个手机号是否存在的一个是这个什么呀register就是保存这个什么呀用户信息的
[11:24] 那么这个右层的代码写完之后呢咱顺手把Controller里边的这个代码给他补一补吧好不好因为Controller那个代码咱当时是不是应该是一个空实现扔到那那咱现在补这个代码很简单嘛好咱找到那个谁呀Controller找是这个地方对咱当时一个空实现了那这呢我们只需要干什么呀对调用一下什么呀consumer Service的
[11:58] register 方法就OK了那我在这就直接写这个代码了啊那就是我们不在这直接return了啊我们一点一点写那就是consumer是不是这个Service还没注入呢是不是还没有注入所以说我们既然需要把这个Service给注入一下那就是什么呀add auto will然后呢private
[12:45] consumer serviceconsumer Service然后注进来之后我们在这就可以调用他的方法粘一下然后点他的什么方法对register这个方法然后把谁给扔进来consumer register什么呀dq是不是然后我们就可以return这次我们这么返回了rest response.success
[13:33] 因为我们刚才在这个reject的方案里边是不是出问题我们就干什么呀跑异常了呀是不是跑异常了对所以说呢我我现在就直接也不用往这里边存什么数据了我就直接返回一个成功就完事因为不成功的话他肯定会抛什么呀跑异常呃那么另外呢这里边还有一个细节需要注意的你看他这个地方是不是还有一个用户名是不是还有一个用户名这个用户名的话我们也建议咱自己给他生成一下吧
[14:10] 因为证实性的身份证号他将来开货的时候会填但是这个用户名这个前端他在发请求过来的时候也不带这个数据所以这个用户名我建议咱在这也给他人工给个值刚才把这个地方给漏掉了我们也人工给一个值还在这个地方还是在这如法炮制consumer.set什么set哪个
[14:40] 可不是full name应该是set谁user name是不是这里边有吗应该有那这个值怎么给呢咱就跟刚才这个下面这个地方用户编号也是一样的可以吧但是我们这个地方就不打算用这个前缀了不要前缀因为它是一个用户名用户名的话就不太适合用前缀咱就不使用前缀所以这个属性的值咱们也给它补一下补完之后的话我们再去看一眼这个consumer
[15:16] 不是卡随我啊是kongchou我们kongchou再打开那这边这个代码咱基本上这么写就可以了另外提醒大家注意我们这个kongchou上面方案上面是不是啥注解都没有加呀是不是这个注解我就不在自己家了我就直接从讲义里边给他把它粘过来了啊对就这一块我直接粘过来这个大家都比较熟悉了吧现在
[15:50] 一般我们Controller方法上面都要加两种注解一种是Spring MVC的注解比如说这个防露镜还有这一块就是什么注解对这一块是Swegg的注解这个呢你熟悉之后呢你也可以不用敲粘过来也可以我们可以节省一下这个开发的时间那么到目前为止的话咱们呃用户中心这一块注册功能或者说保存用户信息的这个功能我们就开发完毕

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示用户服务（Consumer Service）中用户注册功能的实现，包括服务层、控制器层的代码编写，以及数据库表结构设计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 ConsumerServiceImpl.java 文件，其中 checkMobile 方法用于校验手机号，getBMobile 方法用于查询数据库，register 方法用于注册用户。
画面 2：在 register 方法中，添加了 if 判断，如果手机号已存在则抛出异常。
画面 3：在 register 方法中，抛出的异常类型从无参数改为带参数的 BusinessException。
画面 4：在 register 方法中，抛出的异常参数设置为 ConsumerErrorCode。
画面 5：在 register 方法中，使用 BeanUtils.copyProperties 将 DTO 数据复制到实体类 Consumer 中。
画面 6：在 register 方法中，使用 CodePrefixUtil 获取用户编号前缀，并设置到 Consumer 实体。
画面 7：在 register 方法中，使用 CodePrefixUtil 获取用户编号前缀，并设置到 Consumer 实体。
画面 8：切换到 wanningzp-common 模块，查看 CodePrefixCode 类，其中定义了 CODE_REQUEST_PREFIX 常量。
画面 9：展示数据库表 pzp_consumer 的结构，包含 ID、USERNAME、FULLNAME、MOBILE、ROLE、STATUS、REQUEST_ID 等字段。
画面 10：在 ConsumerController.java 中，定义了 @Autowired 注解的 ConsumerService 服务。
画面 11：在 ConsumerController.java 中，定义了 @RestController 注解的类，并添加了 @Api(tags = "Consumer", description = "用户服务API") 注解。
画面 12：再次展示数据库表 pzp_consumer 的结构。
画面 13：在 ConsumerController.java 中，定义了 @ApiOperation 注解的 register 方法，用于处理用户注册请求。
画面 14：在 ConsumerController.java 中，定义了 @ApiImplicitParam 注解的 register 方法，用于处理用户注册请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import com.baidou.rybation.bus.core.conditions.query.QueryWrapper;
import com.baidou.rybation.bus.extension.Service.impl.ServiceImpl;
import org.springframework.beans.BeanUtils;

public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {

    @Override
    public Integer checkMobile(String mobile) {
        return getBMobile(mobile) != null ? 1 : 0;
    }

    private ConsumerDTO getBMobile(String mobile) {
        Consumer consumer = getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
        return convertConsumerEntityToDTO(consumer);
    }

    @Override
    public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    }
}
```

画面 2：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException();
    }
}
```

画面 3：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
}
```

画面 4：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
}
```

画面 5：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    save(consumer);
}
```

画面 6：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 7：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 8：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 9：
```sql
CREATE TABLE `pzp_consumer` (
  `ID` varchar(60) NOT NULL,
  `USERNAME` varchar(60) NOT NULL,
  `FULLNAME` varchar(60) NOT NULL,
  `MOBILE` varchar(60) NOT NULL,
  `ROLE` varchar(60) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `REQUEST_ID` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 10：
```java
@Autowired
private ConsumerService consumerService;
```

画面 11：
```java
@RestController
@Api(tags = "Consumer", description = "用户服务API")
public class ConsumerController implements ConsumerAPI {

    @Autowired
    private ConsumerService consumerService;

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() {
        return "hello";
    }

    @ApiOperation("测试hi")
    @GetMapping(path = "/hi")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

画面 12：
```sql
CREATE TABLE `pzp_consumer` (
  `ID` varchar(60) NOT NULL,
  `USERNAME` varchar(60) NOT NULL,
  `FULLNAME` varchar(60) NOT NULL,
  `MOBILE` varchar(60) NOT NULL,
  `ROLE` varchar(60) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `REQUEST_ID` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 13：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 14：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "AccountRegisterDTO", value = "注册信息", required = true, dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumer")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    return RestResponse.success();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

