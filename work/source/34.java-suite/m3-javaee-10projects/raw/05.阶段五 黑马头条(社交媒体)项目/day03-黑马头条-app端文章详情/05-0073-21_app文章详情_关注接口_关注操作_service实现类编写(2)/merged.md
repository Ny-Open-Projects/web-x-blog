# 21_app文章详情_关注接口_关注操作_service实现类编写(2)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\21_app文章详情_关注接口_关注操作_service实现类编写(2)【海量资源尽在 666java.com】.mp4
- 时长 3分54秒（音频 234s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成处理取消关注的逻辑取消代码量稍微小一些在去删除之前咱们还是要先去查下面先去查询当前的Float Slag进去查的时候如果说它有值就不用再删除了说错了没值咱们就不用再去删除了好吧行再往下看首先是Burst他们参数看哪个第一个是Burst是吧
[00:29] 然后是哪个刚才咱们讲了是不是当前的一个有user.id好然后第二个参数呢第二个参数就是当前的一个user.id然后第三个参数就是flow的好吧咱们就去判断一下如果说呢来看看如果说ap user flow它等于none的话呢等于等于啊
[01:01] 这时候其实你就不用删除了因为它根本就没有关注所以说咱们在这直接去returnreturn一个叫response without.irror你这个数据不存在就是未关注app.dateNodeExists这时候数据就不存在了这时候咱们就可以说未关注未关注就不用删除了
[01:31] 然后再往下看这时候它如果说里边没事它已经过了这了就是说咱们可以写个else好吧写个elseelse里边咱们就可以去做一个删除首先咱们要删除的第一个就是当前的粉丝粉丝表粉丝表里边你删除之前事是一样的咱们也要去查询当前的粉丝slide一个是burst
[02:01] youtube.group1这里面其实要传传传传的是float id然后第二个参数其实也是float id第三个参数就是user.getid行咱们看能不能查出来如果说它不等于空好来看如果说它不等于空ap user fun它不等于空的话咱们再去调用删除就可以了ap user fun myprod delete
[02:31] 这里边需要去设置一些参数第一个是first因为咱们要去看那个分片里边去删除然后是还是格鲁伯万还是flowed id这个参数传的是一样的flowed id然后是user.getid好这个就删除了这个删完之后你看它是等于等一样如果说它等一样的话是不是走这走这的话咱们要去删除第二个就是把这个给删了
[03:01] 删除的话其实很简单啊就是把它呢拿过来直接调一个什么delete第一个呢还是一样啊还是当前的这个东西那个还是他第三个还是他好直接去钻过来就可以了啊过来之后呢咱们可以去返回一个叫count吧看影响多少行是吧然后最终呢咱们直接去返回就可以了response result.ok把当前那个count放进去那这时候
[03:31] 咱们这个取消关注的逻辑咱们也就处理完了啊行那这个报错我看看点报错啊那这少一个分号是吧好其他这就没有没有报错了啊逻辑呢咱们这个代码可能比较长啊大家写的时候一定要注意啊就是首先呢你要把这个思路给捋清捋清完之后呢你再去写这个代码就会容易一些好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写并调试一个取消关注功能的 Java 服务层代码，涉及数据库操作、异常处理和业务逻辑判断。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：

画面 1:
- 编辑器中显示 `AppUserRelationServiceImpl.java` 文件。
- 代码正在编写 `followCancelById` 方法的逻辑。
- 代码中包含注释“处理取消关注的逻辑”。
- 当前光标位于方法体内部，准备编写后续逻辑。

画面 2:
- 代码中 `apUserFollowMapper.selectById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `selectById` 方法调用处。

画面 3:
- 代码中 `apUserFollowMapper.selectById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `selectById` 方法调用处。

画面 4:
- 代码中 `if (user.getId() == 0)` 条件判断。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `==` 运算符处。

画面 5:
- 代码中 `if (user.getId() == 0)` 条件判断。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `==` 运算符处。

画面 6:
- 代码中 `if (apUserFollow == null)` 条件判断。
- IDE 提示“Cannot resolve method 'errorResult'”，表明方法未找到。
- 光标位于 `errorResult` 方法调用处。

画面 7:
- 代码中 `apUserFollowMapper.selectById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `selectById` 方法调用处。

画面 8:
- 代码中 `apUserFanMapper.selectById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `selectById` 方法调用处。

画面 9:
- 代码中 `apUserFanMapper.deleteById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `deleteById` 方法调用处。

画面 10:
- 代码中 `apUserFanMapper.deleteById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `deleteById` 方法调用处。

画面 11:
- 代码中 `apUserFanMapper.deleteById(...)` 方法调用。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `deleteById` 方法调用处。

画面 12:
- 代码中 `return ...` 语句。
- IDE 提示“Expression expected”，表明此处语法错误。
- 光标位于 `return` 关键字后。

画面 13:
- 代码中 `@Autowired` 注解用于注入 `apUserFollowMapper`、`apUserFanMapper`、`sequences` 和 `appFollowBehaviorService`。
- 代码中包含注释“处理关注的逻辑”。
- 光标位于方法体内部，准备编写后续逻辑。

画面 14:
- 代码中 `apAuthorMapper.selectById(...)` 方法调用。
- 代码中包含注释“处理当前用户是否已经关注”。
- 光标位于 `if (user.getOperation() == 0)` 条件判断处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：

画面 1:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 2:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 3:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 4:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 5:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 6:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    } else {
        ApUserFan apUserFan = apUserFanMapper.selectById(BurstUtils.groudOne(followId, followId, user.getId()));
        if (apUserFan == null) {
            apUserFanMapper.deleteById(BurstUtils.groudOne(followId, followId, user.getId()));
        }
    }
}
```

画面 7:
```java
private ResponseResult followCancelById(User user, Integer followId) {
    if (user.getId() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, errorMessage: "未关注");
    }
    ApUserFollow apUserFollow = apUserFollowMapper.selectById(BurstUtils.groudOne(user.getId(), user.getId(), followId));
    if (apUserFollow == null) {
        return ResponseResult.errorResult(AppHttp

