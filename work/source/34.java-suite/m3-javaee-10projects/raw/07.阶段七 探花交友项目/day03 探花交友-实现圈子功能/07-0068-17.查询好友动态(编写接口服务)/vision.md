# 画面线理解：17.查询好友动态（编写接口服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\17.查询好友动态（编写接口服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:06, 03:56, 05:29, 07:08, 08:45, 11:02, 12:28, 14:06, 15:27, 17:21, 18:52, 19:45, 20:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:44:45

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 服务端实现“好友动态”功能的接口，包括定义数据模型、编写 Controller 层的分页查询接口、Service 层的业务逻辑处理（如数据转换、用户信息关联等），并配合 Mock 服务进行接口调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Mock 服务（mock.boxuegu.com）中“好友动态”接口的详情页，接口状态为“已就绪”，Mock 地址为 https://mock.boxuegu.com/mock/164/movements。
画面 2: 显示了 Typora 编辑器中的文档 day03.md，内容为“2.4.4. 编写 movementsService”章节，展示了 Movements 对象的 Java 类定义，包含 id、userId、avatar、nickname、gender、age、textContent、imageContent、distance、createDate、commentCount、likeCount、hasLiked、hasLoved 等字段。
画面 3: 在 IntelliJ IDEA 中，展示了 MovementsController.java 文件中 queryPublishList 方法的代码，该方法接收分页参数并调用 movementsService 的 queryPublishList 方法。
画面 4: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，其中包含获取用户信息、查询发布列表、判断集合是否为空的逻辑。
画面 5: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环的开始处，准备进行数据转换。
画面 6: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，正在将 Publish 对象转换为 Movements 对象，并设置点赞数、评论数等属性。
画面 7: 显示了 Typora 编辑器中的文档 day03.md，内容为“2.4.5. 测试”章节，展示了测试用例的示例数据（helma，30）。
画面 8: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，准备进行数据转换。
画面 9: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 @Autowired 注解下方，准备编写方法体。
画面 10: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，准备进行数据转换。
画面 11: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，正在设置 Movements 对象的标签、昵称、性别、头像、年龄等属性。
画面 12: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，正在设置 Movements 对象的标签、昵称、性别、头像、年龄等属性。
画面 13: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，正在设置 Movements 对象的标签、昵称、性别、头像、年龄等属性。
画面 14: 在 IntelliJ IDEA 中，展示了 MovementsService.java 文件中 queryPublishList 方法的代码，光标位于 for 循环内部，正在设置 Movements 对象的标签、昵称、性别、头像、年龄等属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.tanhua.server.vo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
public class Movements {
    private String id; //动态id
    private Long userId; //用户id
    private String avatar; //头像
    private String nickname; //昵称
    private String gender; //性别 man woman
    private Integer age; //年龄
    private String[] tags; //标签
    private String textContent; //文字动态
    private String[] imageContent; //图片动态
    private String distance; //距离
    private String createDate; //发布时间：如：10分钟前
    private Integer commentCount; //评论数
    private Integer likeCount; //点赞数
    private Integer hasLiked; //是否点赞（1是，0否）
    private Integer hasLoved; //是否收藏（1是，0否）
}
```

画面 3:
```java
@GetMapping
public ResponseEntity<PageResult> queryPublishList(@RequestParam("page") Integer page,
                                                  @RequestParam("pagesize") Integer pageSize) {
    PageResult pageResult = this.movementsService.queryPublishList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}
```

画面 4:
```java
public PageResult queryPublishList(Integer page, Integer pageSize) {
    User user = UserThreadLocal.get();
    PageInfo<Publish> pageInfo = this.quanZiApi.queryPublishList(user.getId(), page, pageSize);
    List<Publish> records = pageInfo.getRecords();
    if (Collections.isEmpty(records)) {
        return null;
    }
}
```

画面 5:
```java
for (Publish record : records) {
}
return null;
```

画面 6:
```java
pageResult.setPage(page);
List<Publish> records = pageInfo.getRecords();
if (CollectionUtils.isEmpty(records)) {
    return pageResult;
}
List<Movements> movementsList = new ArrayList<>();
for (Publish record : records) {
    Movements movements = new Movements();
    movements.setId(record.getId().toString());
    movements.setUserId(record.getUserId());
    movements.setLikeCount(100); //TODO 点赞数
    movements.setCommentCount(30); //TODO 评论数
    movements.setDistance(record.getDistance());
    movementsList.add(movements);
}
return null;
```

画面 7:
```markdown
2.4.5. 测试
helma 30
```

画面 8:
```java
movementsList.add(movements);
```

画面 9:
```java
@Service
public class MovementsService {
    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;
    @Autowired
    private UserInfoService userInfoService;
    // ...
}
```

画面 10:
```java
List<Movements> movementsList = new ArrayList<>();
List<Long> userIds = new ArrayList<>();
for (Publish record : records) {
    Movements movements = new Movements();
    movements.setId(record.getId().toString());
    movements.setUserId(record.getUserId());
    userIds.add(record.getUserId());
    movementsList.add(movements);
}
```

画面 11:
```java
QueryWrapper<UserInfo> userInfoQueryWrapper = new QueryWrapper<>();
userInfoQueryWrapper.in("user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(userInfoQueryWrapper);
for (Movements movements : movementsList) {
    for (UserInfo userInfo : userInfoList) {
        if (movements.getUserId().longValue() == userInfo.getUserId().longValue()) {
            movements.setTags(StringUtils.split(userInfo.getTags(), ','));
            movements.setNickname(userInfo.getNickName());
            movements.setGender(userInfo.getSex().name().toLowerCase());
            movements.setAvatar(userInfo.getLogo());
            movements.setAge(userInfo.getAge());
            break;
        }
    }
}
```

画面 12:
```java
movements.setTags(StringUtils.split(userInfo.getTags(), ','));
movements.setNickname(userInfo.getNickName());
movements.setGender(userInfo.getSex().name().toLowerCase());
movements.setAvatar(userInfo.getLogo());
movements.setAge(userInfo.getAge());
```

画面 13:
```java
movements.setTags(StringUtils.split(userInfo.getTags(), ','));
movements.setNickname(userInfo.getNickName());
movements.setGender(userInfo.getSex().name().toLowerCase());
movements.setAvatar(userInfo.getLogo());
movements.setAge(userInfo.getAge());
```

画面 14:
```java
movements.setTags(StringUtils.split(userInfo.getTags(), ','));
movements.setNickname(userInfo.getNickName());
movements.setGender(userInfo.getSex().name().toLowerCase());
movements.setAvatar(userInfo.getLogo());
movements.setAge(userInfo.getAge());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
