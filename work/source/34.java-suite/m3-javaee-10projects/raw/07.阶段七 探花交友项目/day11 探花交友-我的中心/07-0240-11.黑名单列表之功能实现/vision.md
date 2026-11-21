# 画面线理解：11.黑名单列表之功能实现

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\11.黑名单列表之功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:00, 02:06, 02:35, 03:27, 04:10, 05:06, 05:42, 06:32, 07:20, 07:49, 08:23, 09:28, 10:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:43:59

1) 这一组画面整体在讲如何在用户服务中实现黑名单分页查询功能，并通过 Mock 服务模拟接口数据。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Typora 文档中“2.7.5. mock接口”章节，包含 Mock 服务的接口基本信息和请求参数，Mock 地址为 https://mock.boxuegu.com/mock/164/users/blacklist。
画面 2: 展示 IntelliJ IDEA 中 BlackListVo.java 类的定义，包含 id、avatar、nickname、gender、age 等字段。
画面 3: 展示 UsersService.java 中 queryBlacklist 方法的代码，调用 blacklistService 的 queryPageList 方法。
画面 4: 展示 UsersService.java 中 queryBlacklist 方法的代码，调用 blacklistService 的 queryPageList 方法，并显示了 User 类的成员变量列表。
画面 5: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 方法设置分页信息。
画面 6: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 和 setTotal 方法设置分页信息。
画面 7: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 和 setTotal 方法设置分页信息，并显示了 List 类的成员变量列表。
画面 8: 展示 UsersService.java 中 queryBlacklist 方法的代码，创建了 List<Long> userIds 并遍历 records 获取 userId。
画面 9: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 QueryWrapper 查询用户信息，并遍历结果。
画面 10: 展示 UsersService.java 中 queryBlacklist 方法的代码，创建 BlackListVo 对象并设置 nickname、id、avatar、gender、age 等属性。
画面 11: 展示 UsersService.java 中 queryBlacklist 方法的代码，设置 BlackListVo 的 age 属性。
画面 12: 展示 Mock 服务的接口详情页面，接口路径为 /users/blacklist，Mock 地址为 https://mock.boxuegu.com/mock/164/users/blacklist。
画面 13: 展示手机端应用的黑名单界面，显示了三个用户信息。
画面 14: 展示 Typora 文档中“2.8.1. UsersController”章节，包含黑名单列表的 UI 设计图。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```java
package com.tanhua.server.vo;
import ...
@Data
@AllArgsConstructor
@NoArgsConstructor
public class BlackListVo {
    private Long id;
    private String avatar;
    private String nickname;
    private String gender;
    private Integer age;
}
```

画面 3:
```java
public PageResult queryBlacklist(Integer page, Integer pagesize) {
    User user = UserThreadLocal.get();
    return null;
}
```

画面 4:
```java
User user = UserThreadLocal.get();
this.blacklistService.queryPageList(user.getId(), page, pagesize);
```

画面 5:
```java
this.blacklistService.queryPageList(user.getId(), page, pagesize);
```

画面 6:
```java
PageResult pageResult = new PageResult();
pageResult.setPagesize(pagesize);
pageResult.setPage(page);
pageResult.setCounts(new Long(iPage.getTotal()).intValue());
pageResult.setPages(new Long(iPage.getPages()).intValue());
```

画面 7:
```java
PageResult pageResult = new PageResult();
pageResult.setPagesize(pagesize);
pageResult.setPage(page);
pageResult.setCounts(new Long(iPage.getTotal()).intValue());
pageResult.setPages(new Long(iPage.getPages()).intValue());
List<BlackList> records = iPage.getRecords();
```

画面 8:
```java
List<Long> userIds = new ArrayList<>();
for (BlackList record : records) {
    userIds.add(record.getBlackUserId());
}
```

画面 9:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(queryWrapper);
```

画面 10:
```java
List<BlackListVo> blackListVoList = new ArrayList<>();
for (UserInfo userInfo : userInfoList) {
    BlackListVo blackListVo = new BlackListVo();
    blackListVo.setNickname(userInfo.getNickName());
    blackListVo.setId(userInfo.getId());
    blackListVo.setAvatar(userInfo.getAvatar());
    blackListVo.setGender(userInfo.getGender());
    blackListVo.setAge(userInfo.getAge());
    blackListVoList.add(blackListVo);
}
```

画面 11:
```java
blackListVo.setAge(userInfo.getAge());
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“2.7.5. mock接口”，包含“基本信息”和“请求参数”两个部分。
画面 12: PPT 标题为“接口列表”，包含“接口名称”、“接口路径”、“Mock地址”、“状态”、“创建人”、“更新时间”等字段。
画面 14: PPT 标题为“2.8.1. UsersController”，包含“黑名单列表”和“移除黑名单”两个部分。

5) 无。
