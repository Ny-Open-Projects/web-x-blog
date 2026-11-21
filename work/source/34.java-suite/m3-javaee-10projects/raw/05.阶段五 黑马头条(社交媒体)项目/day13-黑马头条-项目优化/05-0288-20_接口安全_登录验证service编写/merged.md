# 20_接口安全_登录验证service编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\20_接口安全_登录验证service编写【海量资源尽在 666java.com】.mp4
- 时长 5分30秒（音频 330s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们就继续这时候咱们需要在这再去创建咱们的Service这个Service就是来用于登录验证的这是一个v2这个你可以直接去找到当前的ap user login Service找到然后在这在这再去加一个v2就可以了拷贝一份然后这是啥这是v好吧这里边咱们也可以去说一下这是v2版本其他就没有什么东西了
[00:32] 其实这个参数也是一样的啊那时候呢咱们就可以去写他的实现实现的就是loginlogin author a u t h好吧请他这个实现完之后啊咱们就就具体写一写那这个写的这个写法呢其实跟前面是类似的啊类似咱们就再写一遍行是吧再回顾回顾啊我现在咱们要去轰转一下验证的验证验证参数
[01:07] StreamUtilStyle有一个叫做User.get就是分因为咱们需要去根据手机号去查询所以说如果说他为空这个不是not他为空的话呢你可以直接干嘛呢直接就是在这再加一个吧再加一个StreamUtilStyleIsEmpty谁呢
[01:39] user.getpasswordpassword说他两个任意一个为空的话咱们就可以直接retry了retry什么retry response result.error然后是有一个叫做app不是你的参数有问题好吧然后下面接着我要看这时候如果说他没有问题的话咱们就可以去查询了是查询用户查询用户好那么查查的方式就是ap user
[02:12] 有一个myport.slack的就是根据当前手机去查询user.get分好这时候返回的就是一个dbuser就是当前的dbuser就是当前的一个用户数据库中查出来的这个user是从前台转过来的是不一样的好接着我们看说你没查找怎么办就是说dbuser等于
[02:42] 这时候肯定就是吧你这个手机号本身就错了这时候你还是可以去returnreturn一个response without.error有一个app咱们可以不用这个参数.ap-user说这个用户不存在就可以了那这个如果说也没事的话这时候你就可以去验证了验证密码
[03:12] 验证密码的话这时候你需要去入当前的一个validate serviceprivate然后有一个validate Service好就它把它给注入进来刚刚写那个Service拷贝一下但是刚才说了你只能选择一种选择一种你可以选择很多个比如说DS你可以选择第五你也可以选择这种加盐的方式
[03:44] 那么可以用哪种用MD5好吧一个传的是谁传的是user对象第二个传的是DB user对象完了最终它就会返回一个补理型就说这么叫isValidate就看它返回是true或者是first好吧我们就可以判断在这下面怎么判断的if isValidate不说它为true的话肯定就是验证成功了验证成功了
[04:16] 验证成功的时候呢咱们这时候就可以干嘛呢就可以去往里边去设置数据啊那设置什么数据呢其实呢你就可以跟扇板是一样的这样吧咱们可以先练啊如果它飞飞的话呢咱们就可以先return啊然后呢如果说没事的话咱们再去return一个正常的就可以了好吧这个怎么办呢就是当前的basebounceresult.d2可以去设置一个它这个参数啊咱们可以告诉你你的密码错了啊
[04:46] 就是logsword error就是密码错误最终的下面该怎么写呢就是跟上面这个是一样的如果说你这边都已经设置完了设置完之后你就可以去把这个东西给放进去最终返回就可以了好吧好好位好位AP userAP user我看看这个既然AP user没有的话咱们就设置为当前的user就可以了好吧
[05:17] 好user就可以了这是user这也是user好那这样的话咱们就算是正常返回了请到这个Service咱们就写到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现用户登录接口的参数校验、数据库查询和密码验证逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示登录服务接口定义，包含DES/AES加密算法和MD5扩展盐的注释。
画面2：展示登录服务接口定义，包含根据用户名和密码进行验证的注释。
画面3：在登录实现类中，开始编写参数校验逻辑，判断用户输入是否为空。
画面4：在登录实现类中，使用StringUtils工具类判断手机号和密码是否为空。
画面5：在登录实现类中，使用StringUtils工具类判断手机号和密码是否为空，并返回错误结果。
画面6：在登录实现类中，使用ApUserMapper查询用户信息。
画面7：在登录实现类中，使用ApUserMapper查询用户信息，并判断查询结果是否为空。
画面8：在登录实现类中，使用ApUserMapper查询用户信息，并判断查询结果是否为空，若为空则返回错误结果。
画面9：在登录实现类中，使用ValidateService进行密码验证。
画面10：在登录实现类中，使用ValidateService进行密码验证，并判断验证结果是否为true。
画面11：在登录实现类中，使用ValidateService进行密码验证，并判断验证结果是否为true，若为false则返回错误结果。
画面12：在登录实现类中，使用ValidateService进行密码验证，并判断验证结果是否为true，若为true则返回成功结果。
画面13：在登录实现类中，使用ValidateService进行密码验证，并判断验证结果是否为true，若为true则返回成功结果，并设置用户密码为“*”。
画面14：在登录实现类中，使用ValidateService进行密码验证，并判断验证结果是否为true，若为true则返回成功结果，并设置用户密码为“*”，并返回用户信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 对加密算法：DES AES
 * 盐为MD5，MD5 扩展盐 salt
 */
public interface ValidateService {
    /**
     * DES验证
     * @param user
     * @param db
     * @return
     */
    boolean validateDES(ApUser user, ApUser db);

    /**
     * MD5验证
     * @param user
     * @param db
     * @return
     */
    boolean validateWithSalt(ApUser user, ApUser db);
}
```

画面2：
```java
package com.heima.login.Service;
import ...
public interface ApUserLoginService {
    /**
     * 根据用户名和密码进行验证
     */
    ResponseResult loginWith(ApUser user);
}
```

画面3：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return null;
    }
}
```

画面4：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult;
    }
}
```

画面5：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
}
```

画面6：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
```

画面7：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
}
```

画面8：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
```

画面9：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
    if(!isValid) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
}
```

画面10：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
    if(!isValid) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
    //设置密码为*
    user.setPassword("*");
    //生成token
    Map<String, Object> map = new HashMap<>();
    map.put("token", ApJwtUtil.getToken(user));
    map.put("user", user);
    return ResponseResult.okResult(map);
}
```

画面11：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
    if(!isValid) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
    //设置密码为*
    user.setPassword("*");
    //生成token
    Map<String, Object> map = new HashMap<>();
    map.put("token", ApJwtUtil.getToken(user));
    map.put("user", user);
    return ResponseResult.okResult(map);
}
```

画面12：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
    if(!isValid) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
    //设置密码为*
    user.setPassword("*");
    //生成token
    Map<String, Object> map = new HashMap<>();
    map.put("token", ApJwtUtil.getToken(user));
    map.put("user", user);
    return ResponseResult.okResult(map);
}
```

画面13：
```java
@Override
public ResponseResult loginWithV2(ApUser user) {
    //验证参数
    if(StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //查询用户
    ApUser dbUser = apUserMapper.selectByApPhone(user.getPhone());
    if(dbUser == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    //验证密码
    boolean isValid = validateService.validateDB(user, dbUser);
    if(!isValid) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
    //设置密码为*
    user.setPassword("*");
    //生成token
    Map<String, Object> map = new HashMap<>();
    map.put("token", ApJwt

