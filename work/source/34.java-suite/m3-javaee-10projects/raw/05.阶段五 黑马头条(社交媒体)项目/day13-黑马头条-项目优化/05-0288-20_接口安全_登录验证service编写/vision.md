# 画面线理解：20_接口安全_登录验证service编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\20_接口安全_登录验证service编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:21, 01:09, 01:34, 01:50, 02:13, 02:39, 02:53, 03:22, 03:38, 04:05, 04:40, 05:02, 05:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:59:15

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
package com.heima.login.service;
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
