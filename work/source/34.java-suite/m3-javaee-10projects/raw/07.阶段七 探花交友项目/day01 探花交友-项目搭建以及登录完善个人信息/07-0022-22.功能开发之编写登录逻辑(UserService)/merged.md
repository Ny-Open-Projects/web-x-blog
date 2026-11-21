# 22.功能开发之编写登录逻辑（UserService）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\22.功能开发之编写登录逻辑（UserService）_【海量资源尽在 666java.com】.mp4
- 时长 21分31秒（音频 1291s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊那么接下来呢我们来看一下用户登录那么前面的这个流程其实我们也说到过啊主要呢是我们去根据前端呢所给我们提交的手机号啊以及这个验证码呢我们去做一下这个校验然后呢我们去生成token然后呢我们去存到release啊这样的一个逻辑啊好那么下面我们就实际的来操作一下
[00:26] 那么首先呢我们来看一下这个MOOC接口啊那么大概呢是这样的一个接口了那么就是去传递两个参数啊一个是手机号一个就是验证码然后呢我们如果校验成功的话那么需要返回一个这个tokentoken呢是这样的一个格式就是我们前面所说的啊这个JWT啊这样的格式去响应了这个token然后呢下面呢还有一个标识就是is new
[00:53] 就是是否是新用户这个类型呢是一个不二类型啊这个要注意一下好嘞好那么下面呢我们就实际的来编写一下这个代码逻辑那么我们找到我们的这个代码在这个Controller下面啊那么我们需要去创建一个叫做usercontroller然后呢我们把它标记为这是一个什么restcontroller然后呢再写一个叫做request mapping
[01:24] 那么这个位置怎么写呢它其实取决于什么呢取决于啊我们这一块的一个啊我们这一块的这个就是请求的地址啊是在这儿好那么我们写一个这个叫优惠呃然后呢下面呢是不是就去做一个教验了对吧那么教验呢呃跟我们之前一样那么如果成功的话那么响应的状态码呢是200那么如果响应的是失败的话那状态码呢是500所以说呢在这个位置呢依然是需要
[01:54] 通过什么呢ResponseEdit然后呢返回是一个Object去做一个啊这样的一个编写那么这个方法呢我们就叫login吧这个是真正的login了对吧好那么我们写一个叫做request这个叫PostMapping然后呢我们去写它的一个这个名字啊这个名字呢其实我们来靠一下吧这个有点长我们靠一下啊那么这个呢就是做一个登录了那么
[02:23] 在我们login中的我们可以看到他所提交的这个参数的类型呢依然是什么呢阶层这种类型那么所以呢在这个位置呢我们要使用什么呢raise requestrequest body然后呢我们去写一个这个mapstream然后来一个obj或者stream可以啊那么用stream会方便一些因为他所提交的可以看到
[02:50] 都是什么呢这么串啊这么串这种类型啊就用string会比较方便一些好那么我们来写一个这个叫paramount啊paramount那么有了这个这个之后呢我们是不是就能够拿到拿到我们这两个啊这个参数那么这两个参数呢我们就来call一下吧那么就是就它了把这两个call过来那么我们就不需要tostring了直接就可以去啊直接就拿到它就是
[03:20] 我们的这个Stream对吧那么拿到这两个传递的参数之后呢我们就需要去编写我们的这个Service然后呢通过这个Service呢去做一些这个业务逻辑的处理那么所以呢我们下面呢需要在这个Service中呢去创建一个叫做user serviceuser Service然后呢把它标记为呢这是一个Service哎OK
[03:48] 好然后呢我们就在这个user Controller中啊那么就可以把这个什么呢user Service去注入进来那么我们这个Service呢我们就不写这个接口了啊直接去写这个实现类了呃然后呢我们就在user Service中呢就可以去写逻辑了那么这样来写吧那么通过user Service点什么呢这个login去做一个登录那我们把这个mobile和code啊传递过去啊把它传递过去然后呢我们在这个Service中呢
[04:18] 去让他自动生成这个方法OK那么这个login的返回值是什么呢大家想一下他应该返回的是不是一个stream呢是不是就是一个token呢如果登录成功的话那么就返回这个token那么如果是我们来写一下这个是我们的登录逻辑那么这个return就是如果这个校验成功返回这个token
[04:49] 那么这个呢是没有n啊那么如果是校验失败的话失败那就返回什么呢是这样的一个逻辑啊所以说呢我们这个地方返回正不错啊就可以了然后呢下面我们来看一下这个里面的逻辑的处理那么我们当我们拿到这个手机号和验证码的话那么首先呢对吧
[05:19] 首先我们需要什么呢去校验我们的验证码是否正确那么如何去校验我们的验证码是否正确呢是不是需要通过我们的readies是不是来做一个操作呀那我们就需要把谁呢是不是readyreadiestemplate去注进来范型呢那就是这个stream啊stream了key value都是这么创那么来一个readiestemplate
[05:49] 然后呢把它呢就注入进来那么注入进来之后呢那么我们就去做一个操作对吧那么点什么呢ops for value然后呢点做一个get这个操作那么key是什么呢我们定义一个叫做redis key等于什么呢这个是不是在前面我们是不是去发送手机验证码的时候呢是不是去将它是不是去保存到我们redis中啊
[06:18] 那么是在哪个位置呢是不是在这里啊它的这个写法是不这样的对吧然后呢我们把它拷贝一下就放到这来这就是我们的一个这个key那么我们去get这个key对吧我们看能不能拿到数据呢那么这个就是什么呢我们的一个value吧那么如果我们做一个判断那么如果这个有tils啊is empty
[06:48] 如果这个value为空那代表什么呢是不是我们这个验证码是不是已经失效了那么我们这个位置呢直接就返回谁呢是不是return对吧那我们加一个注释就是验证码失效失效那么如果这个不失效就是说这个值依然还存在的话那么我们是不是就需要做一个判断那么我们来判断什么呢是treeUtils.eqs
[07:17] 谁呢value和谁呢和我们的code是不是做一个对比对吧那么如果这两个是相等的话对吧如果我们就取法吧如果不相等那么如果不相等是不是就应该return呢那就是什么呢验证码输入错误输入错误两个不匹配对吧那么接下来如果走到这呢就代表的验证码是
[07:46] 成功了是OK的对不对那么要注意了在这个位置验证码是OK了那么接下来我们需要校验什么呢是不是我们需要去校验该手机号是否已经注册那么如果没有注册那么是不是需要需要什么呢如果没有注册呢就需要注册一个账号
[08:14] 那么如果已经注册是不是就直接登录对不对那是不是有这样的一个逻辑在里面那么怎么实现这个逻辑是不是就需要去查询我们的数据库了那么在这个位置我们就需要把我们之前所写这个U的什么Mapper是不是去注进来对吧那么把这个U Mapper注进来然后我们去做一个查询怎么样查询我们需要根据一个条件所以我们给它定一个怎么
[08:43] query wrap然后呢这个呢是一个user然后呢query wrap等于new一个query wrap然后呢我们这个query wrap点是不是eq说是谁呢来看一下我们的这个colon字段啊那么字段中是不是就这个mobile对吧mobile然后呢eq谁呢如果和这个相等就是说去等于它啊
[09:10] 那么我们是不是就需要调用类似点这个user map点select one对吧select one那么就把这个query wrap去传递过去那么如果他能够查到我们这个user的话拿查到这个user的话对吧那么我们就来喊你判断一下对吧那我们就判断一下那么如果他等于这个空的话那么代表什么呢是不是就是该
[09:40] 手机号未注册那么未注册的我们就需要给他去注册一下那么怎么样注册呢那我们就需要给他去是不是new一个对象然后插入进去所以这个他就应该等于什么new一个什么User然后User点set谁呢这个手机号是不是就我们签名传mobile然后User点set谁呢密码密码这个位置其实对我们目前当前的应用而言
[10:09] 他已经是没什么太大的用了啊所以说呢但是呢我们还是需要给他去设置一个密码那么我们在在这个位置啊我们就给他去简单的来处理一下吧我们就使用这个MD5去做一个加密那么我们就使用之前的我们这个导入这个包啊叫做codec里面那个包digestutils.MD5MD5啊去做一个这个加密那么我们给他就默认什么呢123456吧
[10:39] 就默认这样的一个这样的一个这个默认这个密码然后呢我们来看一下它呢是有这个它是接收什么呢接收的是一个byte的宿主那么我们这个我们调用API调用错了那么我们来看一下应该是调用的我们就传递这不错这个那么123456那么这个呢我们说明一下这是默认密码
[11:13] 默认密码好嘞好那么下面呢这个里面呢就没有其他的字段了啊那么set可以看一下那么id不能够去做一个set那么ok了那么接下来呢我们就需要把它保存到数据库是不是叫用race.urlmapper.insert去做一个这个插入哎呦ok好那么这样的话是不是就完成了一个呃这个哎这个写错了叫未注册啊就是我们手机号是未注册的
[11:40] 这样的一个逻辑那么接下来到往下面走我们是不是就需要来实现我们登录的这样的一个流程了那么在我们登录的最后返回的时候是不是需要有一个我们是否是新用户的一个标识所以说我们上面还少一个小的一个逻辑那么我们在这去把它应该我们到这就在这里去加一个什么布尔值布尔值
[12:08] 不知道是什么呢叫做一日一日六等于什么呢就是默认呢默认是什么呢非新住默认什么呢默认是已注册已注册的好那么如果走到这个逻辑中呢那我们就把它设置为什么呢好那么这样的话这个逻辑就完整了那么接下来呢在下面呢我们就需要去做一个这个
[12:39] 登录了对吧那么登录呢我们就需要去生成我们的一个这个token那么这个token是怎么样去生成的前面是吧我们写了测试用力中也有这样的一个逻辑啊那我就把这个逻辑呢就拿过来那么在这啊在这那么我们把它丢到这个里面来哎丢到这那么我们可以看到这个呢是我们生成这个token逻辑那么我们给他也存两个这个字段吧那么一个就是我们的手机号那么就是传入的这个什么呢mobile
[13:10] 另外一个呢就是ID那么ID呢就是我们这个url.getID那么要注意了这个url.getID呢它呢在这个位置呢是做一个新增新增之后呢会把这个ID再回写到这个对象中所以说在这个位置我们是可以拿到这个ID的好然后呢我们就去生成这个token那么我们这个写个token吧然后呢在这个位置我们需要我们的一个这个
[13:39] secret就是这个言那么这个言呢是不是在我们之前的配置文件中是不是我们已经配置过了是不是就它呀所以说呢我们是不是就可以直接来使用它呢对吧好那么我们来看一下那我们就去把它去注入进来那么怎么样注入呢就不要它了那就它吧然后呢写一个这个value$在$大括号这样的话
[14:09] 是不是就可以完成一个zoo的一个操作那么下面我们是不是就可以使用secret然后就生成token了那么生成token之后那么我们接下来是不是就需要把token是不是存储到我们的redis中所以说下面逻辑就是叫什么就是将我们token存储到redis中那么逻辑怎么写我们就还是调用redis template点什么
[14:38] 这个ops for value然后呢做一个set一个操作啊那么set这个操作呢我们需要是要key啊所以我们定义一个什么呢key那么key呢叫做什么redis tokenkey它等于什么呢我们给它一个前对叫token吧呃去加一个我们的一个这个呃不能加手机号啊要加这个token啊把它去存起来那么这个呢是我们的一个key
[15:10] 那么value是谁呢我们来看一下再定义一个radius token token value它等于谁呢它是不是就需要把我们的这个U的对象去存储起来那么我们需要把这个U对象去做一个序列化那么调用这个没有定义那么我们来定义一个就是我们的JSON的一个map对象叫做static然后object map
[15:39] 把它呢去定义进来等于new一个objectMapper然后呢我们通过这个Mapper呢去做一个序列化点WriteValue as string然后呢我们把这个User对象呢传递给它那么这样的话呢其实我们就有了这个Value了对吧这第二个这个参数那么第三个参数呢它是需要一个时间对吧需要一个这个时间我们来看一下
[16:06] 那么这个时间呢我们就来一个我们给它多长时间呢就是比方说我们给它保存一小时吧一小时这样的一个时间这个呢有点错误啊来看一下什么错误呢我们这个放错位置了对吧那么这个应该把它丢到后面来啊set这个位置啊好这样的话就OK了然后呢我们来看一下这个是有异常那么异常呢我们就来处理一下吧那么我们就
[16:36] 前面这个OK那么这样我们就把它去做一个try cut的处理做一个try cut的处理那么如果有异常的话那我们用exception去做一个补货好嘞好那么我们就写到这吧那么如果我们出异常的话那我们还是需要有一个日制对象对吧那么定义一下private然后呢statutefinal然后呢这个logger然后呢
[17:08] log等于loger factorylogger然后点getlogger就是yoda Service.给它class好那么我们有了log对象就可以去打日志了那么就打到这个位置来就是我们error然后写一个什么就是去存储token出错对吧
[17:41] 然后呢我们把这个义呢打印出来哎OK好那么这样的话呢我们就完成了一个存储了对不对那么完成了这个存储之后呢那么接下来呢我们是不是就哎如果说出异常了那我们就应该return了啊return down对吧好嘞好那么如果没有问题的话那我们是不是把这个token是不是存起来了那么存起来之后呢要注意最后一个逻辑啊是什么呢
[18:09] 那么在我们之前的这个逻辑中呢是不是可以看到在这儿是不是有一个发送消息啊所以说呢我们在在这个位置呢需要去发送消息啊那么这个消息呢我们需要去把我们的这个就是RocketMQ去注入进来那么就写一个RocketMQ啊RocketMQ template去注入进来把这个模板呢也注入进来
[18:36] 那么注入件之后呢通过它呢是不是就可以去做一个这个发送了那么这个位置它提醒是有点这个错误其实这个是这个工具的提醒的问题它应该是能够注入的好那么一会儿我们可以来测一下吧那么我们需要发送这个发送消息发送这个消息那么怎么样发送消息呢通过这个RockdamQ
[19:01] 点convert 按send去做一个发送就可以了那么我们发送的消息是什么我们需要定义一个map去做一个发送那么stream来一个object然后叫message等于new一个hc map那么我们这个message中去存什么东西我们存一个就是 id就是当前用户的id就是叫user.getid
[19:32] get id那么还有一个呢就是我们再去存他的一个手机号吧叫mobile然后呢这个mobile存入进来那么我们再给他去存一个什么呢点put再给他存一个时间就是他所登录的一个时间叫new一个date好我们把这个时间呢也传递过去然后呢我们就去做一个发送那么第一个呢就是
[20:03] 我们需要去发送给我们指定的我们的一个这个队列那么第二个呢就是我们这个对象了我们的这个目标嘛目标我们就写叫什么呢叫itcast-什么呢碳花然后呢sso或者我们这样写吧叫itcast叫碳花sso-什么呢login嘛这样来写好那么这个就代表着我们登录的这样的一个逻辑啊好
[20:32] 然后呢我们return啊return谁呢最后呢是不是我们要return的就是我们的这个isnew对吧isnew去加一个谁呢加一个我们的一个这个token我们最好给它分割一下用数杠去做一个分割好这样的话是不是就完成一个登录这个里面有一个小细节呢大家注意一下啊
[20:57] 就是这个发送消息呢我们一般呢都要给它通过try catch去处理起来那么如果发送消息失败的话那么我们不希望它去影响到我们正常一个逻辑的一个执行那我们就用一个exception吧去做一个补货那么这个就我们来写一个叫做发送消息出错
[21:18] OK好这样的话我们是不是就搞定了那么到这里我们这个Service是不是就已经写好了那么接下来我们是不是编写逻辑就是在Controller中好我们先把这个视频先停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 Spring Boot 的用户登录系统，包含前端请求、SSO 服务验证、Redis 存储验证码、用户注册与密码加密、以及发送短信验证码的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示用户登录流程图，包含客户端、SSO、Redis、数据库、JWT Token 等组件及其交互关系。
画面2：展示 UserController 类的代码，定义了 login 接口，接收手机号和验证码。
画面3：在 UserController 中，通过右键菜单选择创建 Java 类，准备添加新功能。
画面4：展示 UserService 类，定义了 login 方法，接收手机号和验证码。
画面5：在 UserService 中，开始编写 login 方法，准备从 Redis 获取验证码。
画面6：在 UserService 中，使用 StringUtils 判断验证码是否为空。
画面7：在 UserService 中，使用 QueryWrapper 查询用户是否存在。
画面8：在 UserService 中，如果用户不存在则创建新用户并设置密码。
画面9：在 UserService 中，使用 redisTemplate.opsForValue() 方法操作 Redis。
画面10：在 UserService 中，将生成的 token 存储到 Redis。
画面11：在 UserService 中，定义 Logger 日志对象。
画面12：在 UserService 中，开始编写登录逻辑。
画面13：在 UserService 中，使用 SignatureAlgorithm.HS256 算法对 token 进行签名，并发送短信。
画面14：展示 UserController 中的 login 方法，调用 UserService 的 login 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
用户接收收到验证码后，进行输入验证码，点击登录，前端系统将手机号以及验证码提交到SSO进行校验。
```

画面2：
```java
package com.tanhua.sso.Controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

}
```

画面4：
```java
@Service
public class UserService {

    private RedisTemplate<String,String> redisTemplate;

    @param mobile
    @param code
    @return
    public String login(String mobile, String code) {
        //校验验证码是否正确
        String redisKey = "CHECK_CODE_" + mobile;
        String value = this.redisTemplate.opsForValue().get(redisKey);
        if(StringUtils.isEmpty(value)) {
            return null;
        }
    }
}
```

画面5：
```java
if(StringUtils.isEmpty(value)) {
    return null;
}
```

画面6：
```java
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column, "mobile");
User user = this.userMapper.selectOne(queryWrapper);
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面7：
```java
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面8：
```java
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面9：
```java
this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
```

画面10：
```java
this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
```

画面11：
```java
private static final Logger logger = LoggerFactory.getLogger(UserService.class);
```

画面12：
```java
private static final Logger logger = LoggerFactory.getLogger(UserService.class);
```

画面13：
```java
try {
    // 将token存储到redis中
    String redisTokenKey = "TOKEN_" + token;
    String redisTokenValue = MAPPER.writeValueAsString(redisToken);
    this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
} catch (Exception e) {
    LOGGER.error("存储token出错", e);
    return null;
}
```

画面14：
```java
@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public ResponseEntity<Object> login(@RequestBody Map<String,String> params) {
        String mobile = params.get("phone");
        String code = params.get("verificationCode");
        this.userService.login(mobile, code);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
架构图结构：
- 客户端 → 手机号/验证码 → SSO
- SSO → 控制手机号 → 数据库
- 数据库 → 有效期字段 → JWT Token
- JWT Token → 用户登录成功

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

