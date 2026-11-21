# 15.用户资料之查询

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\15.用户资料之查询_【海量资源尽在 666java.com】.mp4
- 时长 10分9秒（音频 610s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们的用户资料的这个功能啊那么这个功能呢是在我的这个我的这个模块中啊然后呢去可以对我们的用户信息呢进行做一些修改也就是对用户信息的做一些维护的一些操作啊那么首先呢我们需要去查询用户的信息那么要根据用户的ID呢去做一个查询了好那么下面我们就来具体实现这个接口啊那么可以先来
[00:28] 大致的来浏览一下这个接口是在下面的这个位置然后呢这有一个叫做用户资料的一个读取这个接口然后呢下面它的一些这个查询的参数一个是UID一个是环信ID那么在这块为什么要有这个环信ID呢这个我们到后面我们再说再给大家做一个解释然后呢下面我们来看一下这个结构那么大概有这么多的一些
[00:57] 需要返回的一些字段然后我们来看一下具体的一个实践那么首先我们需要根据我们的默克接口定义的一些结构我们来创建我们的一个VO对象那么就叫什么U的info VO我们来拷贝一下把它就放到我们的在server工程下面的VO这个目录里面来那么在这个里面我们其实可以看到
[01:27] 他有一些相关的一些这个资段属性啊我们一起来看一下那么这个是我们的ID也就是用户的ID呃然后呢下面这个呢是头像啊你一称啊他的生日啊年龄啊性别啊等等那么下面呢还有一些叫比如城市啊学历啊收入然后呢还有这个是他的一个这个行业啊然后呢还有他的一个婚姻状况那么
[01:53] 这个呢就是有这么些制度啊那么接下来我们就需要去做一个查询了那么这个查询还是比较简单的对吧那么我们就把这个Controller我们就拷贝过来吧那么就是那我们就直接把它拷过来那我们需要重新呢写一个这个us的一个Controller哎呀我再写啊us然后呢我们还需要有一个us的一个Service好那么写到这个里面来
[02:22] us Service然后呢把它标记为这是一个Service好那么在我们这个里面呢就可以把它注入进来了然后呢我们来看一下我们的在这一块的一些这个内容啊那么这个是我们定义的一个query有的info的这个方法然后呢我们可以看到是不是有两个请求的参数那么一个呢是us id啊一个是环信的这个id那么首先我们解释一下
[02:49] 那我们是不是可以通过我们当前的一个ServiLocal能够拿到当前这个用户那么我们为什么要在这个位置传递一个UID呢原因是呢我们可能需要查询比如说其他啊别人的一些这个用户的信息那我们就不是查询自己啊查询别人的那么可能会传递这个UID啊这是第一个这个参数那么第二个这个参数呢为什么会有这个环信的这个ID呢是这样的是由于我们的这个APP中啊
[03:19] 去集成了环信的一个这个SDK那么在用户第一次接收到这个环信的这个来信的时候呢他不会携带用户的一个这个信息所以呢需要通过这个环信的ID来做一个查询那么其实呢这个呢在我们后台我们的设计中啊我们是把这个UID
[03:40] 和环境ID设置成什么一对一的关系就是两个是其实是相等的相等这个关系的所以说我们后端的处理就相对更简单一些了那么就是说为什么要携带这两个参数的一个原因给大家来解释一下好那么接下来我们就在我们这个Service中来实现我们查询的方法好那么我们来看一下怎么样查询那么首先我们肯定需要把我们这个U的info
[04:08] 这个Service是不是我们要注进来对吧肯定我们需要做一个这个查询好然后我们接下来来看一下这个里面代码的编写那么首先我们需要拿到我当前的一个用户就叫strader一个strader local应该叫什么UserUserStraderLocal.get去获取到我们的一个对象那么首先我们先来处理这个ID的事情所以我们定义一个
[04:39] UraID它等于我们就默认的通过我们的这个Ura来get这个ID然后呢我们需要做一个判断那么如果我们所传入的这个not blank吧那么我们这个UraID不为空的话那么注意啊这个如果不为空那么我们这个UraID那么Ura这个小写的这个ID是这个小写的然后呢我们就如果我们
[05:07] 不为空那我们就采用我们这个UID好那么else再去做一个判断那么如果我们的这个环信这个ID如果我们这个环信这个ID呢也是不为空的也是不为空的呢那么我们就给它去设置我们环信的这个ID
[05:32] 所以说只要是哪个不为空我们就去设置它那么如果一旦呢这个这两个呢都为空那我们就采用我们当前的一个用户ID啊去做一个查询那么就是这样的一个逻辑啊好那么接下来呢我们就通过我们的一个Uzrinfo一个Service啊然后呢我们调用它的一个叫做queryUzrinfoByID啊这个方法那么传递一个UzrinfoByID啊进去啊然后呢我们就去啊去哎拿到它的一个
[06:02] 它的返回值就是一个UseInfo那我们去做一个判断那么如果空等于这个UseInfo的话那么就干嘛呢ReturnLong就可以了那么如果它不为空那么接下来我们就需要去分装一个我们的这个UseInfoVO这个对象去做一个返回了返回了那么我们去Nu一个这个对象然后最后去做一个返回
[06:30] 那么具体的这个分装呢我们就直接来拷贝了啊那我们就到下面吧来找到这个分装的一个过程那么这个是比较基础性的一些代码好那我们就啊提到这来那么在这个里面呢其实我们需要需要去设置的一个是什么呢是在哎那么这块有个爆错啊那么原因是我们这个婚姻状况呢这个应该是int类型的啊拿来看一下那么应该是int类型的那我们把它设置为int类型的
[06:58] 那么我们这个讲义呢是前面的稍微有点问题那我们把它改一下啊改到这个位置来好那么这样的话就没有问题了好那么我们再来看一下我们刚刚的这个实现啊那么在这个里面呢我们来注意这么两个点啊那么第一个呢就是我们这个关于我们这个收入那么后面要去加一个单位啊是key啊所以说我们要去加一个它那么在我们原有的这个库里面啊那我们并没有去那么找到这个麦太花
[07:28] 然后呢在我们这个表里面呢我们并没有去有并没有加这个key啊而是我们是直接去设置了他的这个就是一个值所以说呢我们要去加一个这个key啊然后呢下面呢第二个呢就注意的点啊就是在这个位置就是那么对于我们这个就婚姻状况呢需要用1和0来表示那么我们
[07:51] 在我们的数据库里面呢是用这个已婚和未婚啊这两个中文这个字来做一个表示啊所以在这个位置呢需要做一些这个转化好那么这样的话呢其实我们的这个就已经啊搞定了对吧就实现了我们的这个方法那么接下来呢我们就把我们的这个server呢重启一下然后呢我们去做一个测试好那么现在我们这个服务呢就已经跑起来了那么接下来呢我们还是先来登录一下
[08:18] 然后呢我们再来做测试好那么在这个位置呢我们就去登录一下我们的这个用户啊然后呢我们把这个地址我们来拷贝一下就是UIS然后呢我们就把它丢到这吧然后呢去查询走那么这个是不是就查询到我们的这个用户了对吧可以看到这个收入这个位置呢后面是不是加了一个key然后呢我们后面还可以去跟什么呢我们的这个用户ID啊比如说
[08:49] 查询这个用户ID为2的这个数据然后呢我们还可以去跟随呢跟我们的环信ID那么比如说查询这个3啊其实也是一样的这个效果啊都可以去查询到好那么接下来呢我们就来整合到我们的APP中那我们来看一下效果我们先把这个模拟器呢我们跑起来好那我们就来打开我们的模拟器呢来测试一下啊然后呢我们来做一个登录
[09:19] 然后然后呢我们去登录一下然后呢我们去输入密码验证码123456啊然后呢进入到我们的这个首页然后呢我们点击这个我的这个位置啊主要是在这个功能去做一个完成那么在这个里面呢我们点击一下修改我们的信息啊点击它然后呢其实可以看到现在是不是已经就完成了一些数据的一个加载了
[09:45] 并且在这个位置是吧也把我们当前的用户的信息是不是显示出来了那也说明我们现在的这个设备就是接口的一个编写是不是就OK了但是我们还没有做这个修改的保存那么接下来我们就要去做这个修改的保存了好那么关于我们这个用户信息的一个展现也这个查询那我们就讲到这里了那么最终效果就是这样的一个效果

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Mock 接口获取用户信息，并在后端 Java 服务中实现查询逻辑，最终在前端展示用户资料。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档中“5.1.1. mock接口”章节，包含 Mock 接口地址：https://mock.boxuegu.com/mock/164/users。
画面 2: 在 Advanced REST Client 中查看 Mock 接口的请求参数，包括 id、username、birthday、age、gender、city、education、income 等字段及其校验规则。
画面 3: 在 IntelliJ IDEA 中查看 TodayBestController.java 文件，展示 disLikeUser 接口的实现，包含异常处理。
画面 4: Typora 文档中展示“用户资料 - 读取 API-响应、易用、功能强大的可视化接口管理平台 - Google Chrome”相关说明，并展示部分代码。
画面 5: 在 IntelliJ IDEA 中查看 UsersController.java 文件，展示 queryUserInfo 接口的定义，包含 @RequestParam 注解。
画面 6: 在 IntelliJ IDEA 中查看 UsersService.java 文件，展示 queryUserInfo 方法的初始实现（返回 null）。
画面 7: 在 IntelliJ IDEA 中查看 UsersService.java 文件，展示 queryUserInfo 方法中对 userThreadLocal 的使用和参数处理。
画面 8: 在 IntelliJ IDEA 中查看 UsersService.java 文件，展示 queryUserInfo 方法中对 userThreadLocal 获取的用户 ID 进行判断和转换。
画面 9: 在 IntelliJ IDEA 中查看 UsersService.java 文件，展示 queryUserInfo 方法中调用 userInfoService.queryUserById 方法。
画面 10: 在 IntelliJ IDEA 中查看 UsersService.java 文件，展示 queryUserInfo 方法中将 User 对象转换为 UserInfoVo 对象的完整逻辑。
画面 11: 在 Navicat Premium 中查看数据库表结构，当前选中的是“mytanhua”数据库。
画面 12: Advanced REST Client 界面空白，准备发送请求。
画面 13: Genymotion 模拟器界面，显示手机壁纸“孤独无处安放”。
画面 14: Typora 文档中展示“5.1.1. mock接口”章节，显示用户资料页面的 UI 界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
@GetMapping("/id/unlove")
public ResponseEntity<Void> disLikeUser(@PathVariable("id") Long likeUserId) {
    try {
        this.todayBestService.disLikeUser(likeUserId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 4 代码：
```java
"huaxinID", required = false) String huaxinID) {
    //用户第一次 接收到 环信来的消息， 不带用户信息
    UserInfoVo userInfoVo = this.userService.queryUserInfo(userID, huaxinID);
    if (null == userInfoVo) {
        return ResponseEntity.ok(null);
    }
```

画面 5 代码：
```java
@RestController
@RequestMapping("/users")
public class UsersController {

    @Autowired
    private UsersService usersService;

    /**
     * 用户资料 - 读取
     * @param userID
     * @param huaxinID
     * @return
     */
    @GetMapping
    public ResponseEntity<UserInfoVo> queryUserInfo(@RequestParam(value = "userID") String userID, @RequestParam(value = "huaxinID") String huaxinID) {
        //用户第一次 接收到 环信来的消息， 不带用户信息
        UserInfoVo userInfoVo = this.usersService.queryUserInfo(userID, huaxinID);
        if (null == userInfoVo) {
            return ResponseEntity.ok(null);
        }
```

画面 6 代码：
```java
@Service
public class UsersService {

    public UserInfoVo queryUserInfo(String userID, String huaxinID) {
        return null;
    }
}
```

画面 7 代码：
```java
import com.tanhua.server.utils.UserThreadLocal;
import com.tanhua.server.vo.UserInfoVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UsersService {

    @Autowired
    private UserInfoService userInfoService;

    public UserInfoVo queryUserInfo(String userID, String huaxinID) {
        User user = UserThreadLocal.get();
        Long userId = user.getId();
        if (StringUtils.isNotBlank(userID)) {
            userId = Long.valueOf(userID);
        } else if (StringUtils.isNotBlank(huaxinID)) {
            userId = Long.valueOf(huaxinID);
        }
        return null;
    }
}
```

画面 8 代码：
```java
import com.tanhua.server.utils.UserThreadLocal;
import com.tanhua.server.vo.UserInfoVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UsersService {

    @Autowired
    private UserInfoService userInfoService;

    public UserInfoVo queryUserInfo(String userID, String huaxinID) {
        User user = UserThreadLocal.get();
        Long userId = user.getId();
        if (StringUtils.isNotBlank(userID)) {
            userId = Long.valueOf(userID);
        } else if (StringUtils.isNotBlank(huaxinID)) {
            userId = Long.valueOf(huaxinID);
        }
        return null;
    }
}
```

画面 9 代码：
```java
User user = UserThreadLocal.get();
Long userId = user.getId();
if (StringUtils.isNotBlank(userID)) {
    userId = Long.valueOf(userID);
} else if (StringUtils.isNotBlank(huaxinID)) {
    userId = Long.valueOf(huaxinID);
}
```

画面 10 代码：
```java
UserInfo userInfo = this.userInfoService.queryUserById(userId);
if (null == userInfo) {
    return null;
}

UserInfoVo userInfoVo = new UserInfoVo();
userInfoVo.setAge(userInfo.getAge() == null ? null : userInfo.getAge().toString());
userInfoVo.setAvatar(userInfo.getLogo());
userInfoVo.setBirthday(userInfo.getBirthDay());
userInfoVo.setCity(userInfo.getCity());
userInfoVo.setEducation(userInfo.getEducation());
userInfoVo.setGender(userInfo.getSex().name().toLowerCase());
userInfoVo.setId(userInfo.getId());
userInfoVo.setIncome(userInfo.getIncome() + "K");
userInfoVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
userInfoVo.setNickName(userInfo.getNickName());
userInfoVo.setProfession(userInfo.getIndustry());
return userInfoVo;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: PPT 标题为“用户资料 - 读取 API-响应、易用、功能强大的可视化接口管理平台 - Google Chrome”，下方有多个截图展示不同功能模块。
画面 14: PPT 标题为“5.1.1. mock接口”，下方展示用户资料页面的 UI 界面。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

