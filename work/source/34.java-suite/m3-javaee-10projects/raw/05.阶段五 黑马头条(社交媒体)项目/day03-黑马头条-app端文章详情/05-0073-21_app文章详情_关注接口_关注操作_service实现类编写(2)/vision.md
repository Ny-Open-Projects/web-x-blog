# 画面线理解：21_app文章详情_关注接口_关注操作_service实现类编写(2)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\21_app文章详情_关注接口_关注操作_service实现类编写(2)【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:28, 00:44, 00:55, 01:06, 01:20, 01:54, 02:02, 02:20, 02:32, 02:51, 03:23, 03:37, 03:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:21:20

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
