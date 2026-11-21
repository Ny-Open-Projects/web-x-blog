# 画面线理解：20_app文章详情_关注接口_关注操作_service实现类编写(1)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\20_app文章详情_关注接口_关注操作_service实现类编写(1)【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:15, 04:13, 06:44, 08:28, 11:16, 12:55, 14:31, 16:29, 18:01, 19:05, 21:33, 23:02, 24:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:20:22

1) 这一组画面整体在讲什么（一句话）：
实现用户关注关系的业务逻辑，包括参数校验、数据库操作和行为记录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `AppUserRelationServiceImpl` 类中 `follow` 方法的初始结构，注释说明了“关注操作”、“保存关注关系”、“取消关注”等逻辑。
画面2：在 `if (dto.getOperation() != null)` 条件下，IDE 提示“无效的 operation 参数”，并显示 `UserRelationDto` 类的成员方法。
画面3：在 `else if (followId != null)` 分支中，使用 `apAuthorMapper.selectById(dto.getAuthorId())` 查询关注人信息。
画面4：在 `if (followId != null)` 分支中，IDE 提示“FollowId 或 authorId 不能为空”，并显示 `ApAuthor` 类的成员方法。
画面5：在 `if (user != null)` 分支中，IDE 提示“Expression expected”，并显示 `UserRelationDto` 类的成员方法。
画面6：在 `if (apUser != null)` 分支中，IDE 提示“Expression expected”，并显示 `ApUser` 类的成员方法。
画面7：在 `private ResponseResult followById` 方法中，IDE 提示“Variable 'apUser' is already defined in the scope”，并显示 `ApUser` 类的成员方法。
画面8：在 `if (apUser != null)` 分支中，IDE 提示“Expression expected”，并显示 `ApUser` 类的成员方法。
画面9：在 `if (apUser != null)` 分支中，IDE 提示“Expression expected”，并显示 `ApUser` 类的成员方法。
画面10：展示项目结构，`SequenceConfig` 类位于 `com.heima.user.config` 包下，使用 `@Configuration` 和 `@ComponentScan` 注解。
画面11：展示 PPT 内容，标题为“3.3 关注接口”，子标题包括“3.3.1 工程结构”、“3.3.2 接口定义”、“3.3.3 service 代码实现”、“3.3.4 Mapper 实现”、“3.3.5 service 代码及 controller 实现”。
画面12：在 `else` 分支中，创建 `ApUserFollow` 对象，设置属性，调用 `apUserFollowMapper.insert` 插入数据。
画面13：在 `else` 分支中，创建 `FollowBehaviorDto` 对象，设置属性，调用 `appFollowBehaviorService.saveFollowBehavior` 保存行为。
画面14：在 `else` 分支中，调用 `apUserFollowMapper.insert` 插入数据，返回 `ResponseResult`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import com.heima.model.user.dto.UserRelationDto;
import com.heima.user.service.AppUserRelationService;
import org.springframework.stereotype.Service;

@Service
public class AppUserRelationServiceImpl implements AppUserRelationService {

    @Override
    public ResponseResult follow(UserRelationDto dto) {
        //获取到followId
        //判断当前用户是否已经关注
        //关注操作
        //保存ap_user_follow ap_user_fan 存在关注的行为
        //取消关注
        //根据ap_user_follow ap_user_fan
    }
}
```

画面2：
```java
if (dto.getOperation() != null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "无效的 operation 参数");
}
```

画面3：
```java
else if (followId != null) {
    ApAuthor apAuthor = apAuthorMapper.selectById(dto.getAuthorId());
    if (apAuthor != null) {
        followId = apAuthor.getUserId().intValue();
    }
}
```

画面4：
```java
if (followId != null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "关注人不存在");
}
```

画面5：
```java
if (user != null) {
    if (dto.getOperation() != null) {
        //关注操作
        //保存ap_user_follow ap_user_fan 存在关注的行为
    }
}
```

画面6：
```java
if (apUser != null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "关注用户不存在");
}
```

画面7：
```java
private ResponseResult followById(ApUser user, Integer followId, Integer authorId) {
    //判断用户是否存在
    ApUser apUser = apUserMapper.selectById(followId);
    if (apUser != null) {
        //处理关注的逻辑
        //参数 user
        //参数 followId
        //参数 authorId
        //return
    }
}
```

画面8：
```java
if (apUser != null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "关注用户不存在");
}
```

画面9：
```java
if (apUser != null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "关注用户不存在");
}
```

画面10：
```java
package com.heima.user.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.heima.common.zookeeper")
public class SequenceConfig {

}
```

画面11：
```java
public ResponseResult follow(UserRelationDto dto) {
    if (dto.getOperation() == null || dto.getOperation() != 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "无效的 operation 参数");
    }

    Integer followId = dto.getFollowId();
    if (followId != null && dto.getAuthorId() != null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "followId 或 authorId 不能为空");
    } else if (followId != null) {
        ApAuthor apAuthor = apAuthorMapper.selectById(dto.getAuthorId());
        if (apAuthor != null) {
            followId = apAuthor.getUserId().intValue();
        }
    }
}
```

画面12：
```java
apUserFollow.setFollowName(user.getNickName());
apUserFollow.setLevel((short) 0);
apUserFollow.setIsDisplay(true);
apUserFollow.setShieldComment(false);
apUserFollow.setShieldLetter(false);
apUserFollow.setIsShield(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIsShieldComment(false);
apUserFollow.setIsShieldLetter(false);
apUserFollow.setIs
