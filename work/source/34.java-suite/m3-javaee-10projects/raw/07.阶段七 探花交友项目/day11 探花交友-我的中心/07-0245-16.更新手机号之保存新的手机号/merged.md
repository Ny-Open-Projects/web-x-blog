# 16.更新手机号之保存新的手机号

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\16.更新手机号之保存新的手机号_【海量资源尽在 666java.com】.mp4
- 时长 11分38秒（音频 698s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来看一下我们这个保存新的手机号那么这个呢是我们更新手机号的第三步这个操作那么下面呢我们就来看一下我们的这个MOOC的一个接口然后呢地址呢是这样的一个地址然后呢去提交一个我们的一个手机号这个是一个新手机号响应的是没有一些数据的对吧那我们就直接去返回一个200状态就可以了那么接下来呢我们就来去
[00:29] 做一个这个保存对吧然后呢我们在下面去写方法public返回值呢responseEdit然后t呢就是我们的一个word然后呢我们做一个c5new一个什么然后呢我们来看一下那么在这个里面我们接收的是一个body啊那说明也是一个我们的一个就是json所以我们通过我们的一个map去做一个接收
[00:58] 然后呢我们这样的话就OK了然后呢我们来看请求啊地址呢是这样的一个地址请求呢是post请求加一个post mapping然后加一个他然后呢把前面的这个users拿掉那么就保留成一个份啊就可以了然后呢我们去这样我们先得通过这个param点get谁呢是不是就是我们的一个先get到我们的手机号先get他
[01:28] 然后呢他拿到之后呢就是我们的这个newnew份啊或者是new mobile啊都可以然后呢拿到之后啊那么接下来呢我们就需要去调用我们的us Service做一个sale或者叫update啊都可以那么sale吧也叫updateupdate我们的一个new的一个mobile好那么我们把这个一个是token另外一个就是我们的一个
[02:01] new一个new分传递过去然后呢在这个里面呢我们去返回值呢我们就期望它返回的是一个布尔类型等于它然后呢判断如果这个布尔等于chew那么我们就return我们的这个200那我们就把它拿过来然后这个rout呢我们就设置为什么呢好那么
[02:35] 如果出现异常的话那么就给他就直接去响应我们的500那么到这个位置来好那么上面呢我们在这呢去加注释那么这个是什么呢我们去保存保存我们新的这个手机号啊然后呢我们去去实现这个方法去没有提示吗没有提示那这个我们就得去
[03:11] 自己写这个方法了没有提示那就来写一下吧那么下面呢就public然后呢返回的是boiler类型然后呢是一个update有两个这个参数那我们把这个参数呢拷贝过来来着string啊string两个都是string类型好嘞那么这个里面怎么去做呢那肯定是还是先拿到我们的这个user对吧那么就是上面的这个了
[03:45] 那么就是上面的这个先拿到这个优惠如果拿不到那就先给他去返回这个返回force那么如果拿到之后啊拿到之后呢我们就需要去做一个更新了那我们就调用this.这个user Service.我们就写一个updateupdatenew mobile
[04:11] 然后呢我们去传递两个参数那么一个呢就是我们的一个UIDU的点get一个ID那么另外一个呢那就是我们的这个新的一个手机号然后呢我们希望它呢就它就直接return吧return它然后呢由这个方法来返回一个报纸现在可能是不是这个工具出了点问题啊不提示了啊不提示那么我们就还是自己来
[04:42] 写一下吧那就进到这个里面来进到这个里面来我们就放到最下面来好那我们来看一下这个应该怎么去做当然它不是token了它就是我们这个lang类型的这个id好那么接下来呢我们就需要去做一个更新了那么这个呢我们就是直接操作的就是我们的数据库了对不对好那我们来看一下怎么样去操作呢通过我们list
[05:13] 这瑞士点这个什么呢叫优的map然后呢做一个update那么显然呢我们是需要去根据我们的一个组件的去做一个更新了对吧那么我们来看一下啊需要更新谁呢那么然后呢在上面呢我们需要去做一个什么呢这个优的定一个这个优的然后呢优的等于6一个优的然后呢我们把这个优的点然后呢set一个id
[05:41] 那就是这个ID了然后呢我们再去u的点set一个mobile那就是一个new分好那么把它传进进来来做一个save啊这样的话做一个update这样是不是就可以了啊大家想一下啊这样对不对有的肯定不对啊你这个return啊没有返回布尔值那么我们就给它来一个return它大于啊0如果大于0是不是就OK了这样对不对呢大家想一想啊其实呃是不是很对的啊为什么呢
[06:11] 原因是你修改了新的手机号那么在我们就是说其他的用户有没有注册了新的手机号或者说你自己有没有注册我们手机号在注册所以说我们前面需要有一个校验的逻辑就是校验我们新手机号是否已经注册
[06:36] 是否已经注册所以说这个我们就还需要去做一个查询我们就需要通过一个这个Mapper.select1去做一个查询那么定义一个叫做querywrap然后呢我们定义这是一个user然后呢querywrap去new一个这个querywrap好那我们把它呢传递过去那么然后呢我们来设置这个条件然后呢eq等于谁呢就是我们这个
[07:06] 我们的这个字段我们来看一下那么我们找到这个U的这个字段是不是这个目标这个字段那么如果这个目标这个字段那么如果是EQ等于谁呢这个new一个new分的话那么如果它能够查到我们的一个这个叫old吧old U的那么如果它空不等于old U的话
[07:35] 如果不等于的话那说明已经存在了对不对所以我们就应该return什么呢false了好这个就是什么说明什么呢这个叫该手机号已经已经注册了已经注册好所以说呢就不能够继续去做一个更新了所以这个逻辑啊大家千万别忘记千万别忘记好那么接下来呢我们就把这个这块有包充吗没有了
[08:06] 好那么接下来呢我们就把一些这个服务呢就跑起来那我们来测试一下啊好那么现在呢我们就呃重新把这个SSO呢跑起来了接下来我们就来测试一下啊那么我还是通过我的这个手机号去做一个登录然后呢拿到13456好嘞那么现在呢就登录成功了然后呢我们就进入到我的这个模块中修改手机号那我们把
[08:35] 整个这个流程呢我们来走一下看他有没有问题啊那么之前的这个断点啊我们来看一下如果有的话就把它去掉那么这个断点应该就没了啊好那我们来测试一下来看一下我们的这个手机然后呢我们输入这个先去点击获取验证码那么验证码呢我们就123456下一步然后呢输入新的一个手机号那么
[09:00] 现在手机号呢是17602026868对不对我改成6869啊改成6869点击这个确定啊绑定那么DAO断是不是就绑定成功了啊但是有一个问题就是这个位置它显示的还是这个就是我们当前的登录的这个这个用户呢并没有去得到一个更新啊那我们啊尝试着我们去因为我们退出登录这个没有做啊但我们就把它关闭掉啊
[09:28] 再来去登录一次看他有没有问题啊那么我们去输17602026869啊因为我改成69了嘛当然我们可以先去我们的数据库去检查一下看改了没哎是不是已经改成69了那我们再来去通过这个69呢我们去做一个登录啊那么获取验证码然后呢123456哎是不是又进入到就是还是我们刚才那个用户啊用户ID为1的这个用户
[09:59] 那么可以看一下这个头像对吧还是这个黑马这个用户然后通用设置中呢这块啊现在他就改了这个逻辑了对吧那我们再把它改回来吧然后呢我们获取验证吧123456然后呢下一步走然后呢手机号呢就变成17602026868绑定一下好绑定成功了那我们再次测试一下这回应该就没有问题了
[10:26] 我们再去通过17602026868然后呢去登录一次123456好那么这个时候是不是就OK了没有问题了那么到这里呢我们这个修改手机号的这个逻辑是不是也就搞定了然后呢我们在通用设置中呢是不是也就基本上呢是不是也就搞定了
[10:49] 好我们来看一下我们的讲义那么我们保存新的手机号我们的Controller是这样去做一个编写然后Service我们是需要调用我们user Service中的update这个方法然后我们在我们的user Service中需要注意的是我们需要首先去去查选一下我们手机号
[11:11] 就是我们新的这个手机号它是不是已经使用了如果已经使用的话那肯定就不能够再次使用了所以说我们先需要判断一下所以说呢我们要有这样的一个逻辑因为我们的这个在设计我们表的时候啊那我们的手机号是不能重复的这一点大家一定要注意了OK好那么关于我们的这个更新手机号的一个逻辑呢功能呢我们就先讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，通过 REST API 验证用户手机验证码并更新手机号的完整流程，涉及前端请求、后端 Controller、Service 层逻辑及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：使用 Advanced REST Client 发送 POST 请求，请求体为 JSON 格式，包含 phone 和 verificationCode 字段，请求成功返回状态码 200，响应体为 {"errorCode": "00000", "errorMessage": "验证成功"}。
画面 2：在 IntelliJ IDEA 中，展示 UsersController.java 文件中 checkVerificationCode 方法的代码，该方法接收 @RequestBody 和 @RequestHeader 参数。
画面 3：在 UsersController.java 文件中，展示 checkVerificationCode 方法的 try-catch 块，其中调用 userService.checkVerificationCode 方法。
画面 4：在 UsersController.java 文件中，展示 checkVerificationCode 方法的完整代码，包括 try 块和 catch 块，以及 @PostMapping 注解。
画面 5：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 User 对象的 equals 方法的调用。
画面 6：在 UsersService.java 文件中，展示 updateNewMobile 方法的代码，其中包含对 redisTemplate 的操作。
画面 7：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 redisTemplate.opsForValue().get 方法的调用。
画面 8：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 QueryWrapper 的使用。
画面 9：在 UsersService.java 文件中，展示 updateNewMobile 方法的代码，其中包含对 QueryWrapper 的使用。
画面 10：展示手机应用界面，用于演示用户操作。
画面 11：在 UsersController.java 文件中，展示 checkVerificationCode 方法的代码，其中包含对 userService.checkVerificationCode 方法的调用。
画面 12：在 Navicat Premium 中，展示 tb_user 表的数据，用于演示数据库操作。
画面 13：展示手机应用界面，用于演示用户操作。
画面 14：在 Typora 中，展示 day11 识文.md 文件的内容，其中包含 UsersController 和 UsersService 的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```json
{
  "phone": "18620320863",
  "verificationCode": "123456"
}
```

画面 2：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
```

画面 3：
```java
try {
    String code = param.get("verificationCode");
    this.userService.checkVerificationCode(code, token);
    Map<String, Object> result = new HashMap<>();
    result.put("verification", bool);
    return ResponseEntity.ok(result);
} catch (Exception e) {
    e.printStackTrace();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 4：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.userService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 5：
```java
User user = this.userService.queryUserByToken(token);
if (null == user) {
    return false;
}
```

画面 6：
```java
String redisKey = SmsService.REDIS_KEY_PREFIX + user.getMobile();
String value = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.equals(value, code)) {
    this.redisTemplate.delete(redisKey);
    return true;
}
return false;
```

画面 7：
```java
String redisTokenKey = "TOKEN" + token;
String cacheData = this.redisTemplate.opsForValue().get(redisTokenKey);
if (StringUtils.isEmpty(cacheData)) {
    return null;
}
```

画面 8：
```java
Query<User> query = this.userMapper.selectOne();
User user = new User();
user.setId(id);
user.setMobile(newPhone);
return this.userMapper.updateById(user) > 0;
```

画面 9：
```java
public Boolean updateNewMobile(Long id, String newPhone) {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("column", "mobile", newPhone);
    User oldUser = this.userMapper.selectOne(queryWrapper);
    if (null != oldUser) {
        return false;
    }
    User user = new User();
    user.setId(id);
    user.setMobile(newPhone);
    return this.userMapper.updateById(user) > 0;
}
```

画面 11：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.userService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 14：
```markdown
2.8.1 UsersController
2.8.2 UsersService
2.8.3 UsersController
2.8.4 UsersService
2.8.5 UsersController
2.8.6 UsersService
2.8.7 UsersController
2.8.8 UsersService
2.8.9 UsersController
2.8.10 UsersService
2.8.11 UsersController
2.8.12 UsersService
2.8.13 UsersController
2.8.14 UsersService
2.8.15 UsersController
2.8.16 UsersService
2.8.17 UsersController
2.8.18 UsersService
2.8.19 UsersController
2.8.20 UsersService
2.8.21 UsersController
2.8.22 UsersService
2.8.23 UsersController
2.8.24 UsersService
2.8.25 UsersController
2.8.26 UsersService
2.8.27 UsersController
2.8.28 UsersService
2.8.29 UsersController
2.8.30 UsersService
2.8.31 UsersController
2.8.32 UsersService
2.8.33 UsersController
2.8.34 UsersService
2.8.35 UsersController
2.8.36 UsersService
2.8.37 UsersController
2.8.38 UsersService
2.8.39 UsersController
2.8.40 UsersService
2.8.41 UsersController
2.8.42 UsersService
2.8.43 UsersController
2.8.44 UsersService
2.8.45 UsersController
2.8.46 UsersService
2.8.47 UsersController
2.8.48 UsersService
2.8.49 UsersController
2.8.50 UsersService
2.8.51 UsersController
2.8.52 UsersService
2.8.53 UsersController
2.8.54 UsersService
2.8.55 UsersController
2.8.56 UsersService
2.8.57 UsersController
2.8.58 UsersService
2.8.59 UsersController
2.8.60 UsersService
2.8.61 UsersController
2.8.62 UsersService
2.8.63 UsersController
2.8.64 UsersService
2.8.65 UsersController
2.8.66 UsersService
2.8.67 UsersController
2.8.68 UsersService
2.8.69 UsersController
2.8.70 UsersService
2.8.71 UsersController
2.8.72 UsersService
2.8.73 UsersController
2.8.74 UsersService
2.8.75 UsersController
2.8.76 UsersService
2.8.77 UsersController
2.8.78 UsersService
2.8.79 UsersController
2.8.80 UsersService
2.8.81 UsersController
2.8.82 UsersService
2.8.83 UsersController
2.8.84 UsersService
2.8.85 UsersController
2.8.86 UsersService
2.8.87 UsersController
2.8.88 UsersService
2.

