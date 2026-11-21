# 画面线理解：05.我的喜欢之喜欢数列表（app服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\05.我的喜欢之喜欢数列表（app服务实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:29, 04:18, 06:29, 08:31, 10:11, 11:35, 13:07, 14:35, 15:57, 17:20, 19:58, 22:07, 23:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:39:36

1) 这一组画面整体在讲什么（一句话）：
实现用户关注、粉丝、查看记录等业务的后端接口，包括控制器层参数处理、服务层逻辑分发与数据组装，以及Redis缓存校验逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示UserController中@GetMapping("/friends/{type}")方法，定义了type、page、pageSize、nickname四个参数及其默认值和必填要求。
画面2：展示UsersService中queryLikeList方法的实现，调用userLikeApi的queryEachLikeList、queryLikeCount、queryFanCount方法获取数据。
画面3：展示UserController中@GetMapping("/friends/{type}")方法的完整代码，包含try-catch异常处理和返回ResponseEntity。
画面4：展示UsersService中queryLikeList方法的switch语句，case 1调用queryEachLikeList，case 2调用queryLikeList，case 3调用queryFanList，case 4调用topVisitor。
画面5：展示case 2的代码，调用userLikeApi的queryLikeList方法。
画面6：展示case 4的代码，调用visitorsApi的topVisitor方法。
画面7：展示case 4的代码，调用visitorsApi的topVisitor方法，提示用户选择类型。
画面8：展示UsersService中queryLikeList方法的后续代码，使用QueryWrapper进行用户信息查询。
画面9：展示UsersService中queryLikeList方法的后续代码，使用UserLikeListVo对象封装用户信息。
画面10：展示UsersService中queryLikeList方法的后续代码，将UserLikeListVo对象添加到PageResult中并返回。
画面11：展示UsersService中queryLikeList方法的后续代码，调用recommendUserService的queryScore方法。
画面12：展示UsersService中queryLikeList方法的后续代码，调用redisTemplate的OpsForValue的get方法获取缓存值。
画面13：展示UsersService中queryLikeList方法的switch语句，case 4调用visitorsApi的topVisitor方法。
画面14：展示手机端“谁看过我”页面的UI界面，显示最近访问用户列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@GetMapping("/friends/{type}")
public ResponseEntity<PageResult> queryLikeList(@PathVariable("type") String type,
        @RequestParam(value = "page", defaultValue = "1") Integer page,
        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize,
        @RequestParam(value = "nickname", required = false) string nickname) {
    try {
        page = Math.max(1, page);
        PageResult pageResult = this.userService.queryLikeList(integer.valueOf(type), page, pageSize, nickname);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面2：
```java
public PageResult queryLikeList(Integer valueOf, Integer page, Integer pageSize, String nickname) {
    User user = UserThreadLocal.get();
    PageResult pageResult = new PageResult();
    pageResult.setPage(page);
    pageResult.setPages(0);
    return pageResult;
}
```

画面3：
```java
@GetMapping("/friends/{type}")
public ResponseEntity<PageResult> queryLikeList(@PathVariable("type") String type,
        @RequestParam(value = "page", defaultValue = "1") Integer page,
        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize,
        @RequestParam(value = "nickname", required = false) string nickname) {
    try {
        page = Math.max(1, page);
        PageResult pageResult = this.userService.queryLikeList(integer.valueOf(type), page, pageSize, nickname);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面4：
```java
switch (type) {
    case 1: {
        PageInfo<UserLike> pageInfo = this.userLikeApi.queryEachLikeList(user.getId(), page, pageSize);
        for (UserLike record : pageInfo.getRecords()) {
            userIds.add(record.getUserId());
        }
        break;
    }
    case 2: {
        PageInfo<UserLike> pageInfo = this.userLikeApi.queryLikeList(user.getId(), page, pageSize);
        for (UserLike record : pageInfo.getRecords()) {
            userIds.add(record.getLikeUserId());
        }
        break;
    }
    case 3: {
        PageInfo<UserLike> pageInfo = this.userLikeApi.queryFanList(user.getId(), page, pageSize);
        for (UserLike record : pageInfo.getRecords()) {
            userIds.add(record.getLikeUserId());
        }
        break;
    }
    case 4: {
        PageInfo<Visitors> pageInfo = this.visitorsApi.topVisitor(user.getId(), page, pageSize);
        for (Visitors record : pageInfo.getRecords()) {
            userIds.add(record.getVisitorUserId());
        }
        break;
    }
    default: {
        break;
    }
}
```

画面5：
```java
case 2: {
    PageInfo<UserLike> pageInfo = this.userLikeApi.queryLikeList(user.getId(), page, pageSize);
    for (UserLike record : pageInfo.getRecords()) {
        userIds.add(record.getLikeUserId());
    }
    break;
}
```

画面6：
```java
case 4: {
    PageInfo<Visitors> pageInfo = this.visitorsApi.topVisitor(user.getId(), page, pageSize);
    for (Visitors record : pageInfo.getRecords()) {
        userIds.add(record.getVisitorUserId());
    }
    break;
}
```

画面7：
```java
case 4: {
    PageInfo<Visitors> pageInfo = this.visitorsApi.topVisitor(user.getId(), page, pageSize);
    for (Visitors record : pageInfo.getRecords()) {
        userIds.add(record.getVisitorUserId());
    }
    break;
}
```

画面8：
```java
if (CollectionUtils.isEmpty(userIds)) {
    return pageResult;
}
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("user_id", userIds);
if (StringUtils.isNotBlank(nickname)) {
    queryWrapper.like("nick_name", nickname);
}
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(queryWrapper);
return pageResult;
```

画面9：
```java
for (UserInfo userInfo : userInfoList) {
    UserLikeListVo userLikeListVo = new UserLikeListVo();
    userLikeListVo.setNickname(userInfo.getNickName());
    userLikeListVo.setGender(userInfo.getSex().name().toLowerCase());
    userLikeListVo.setEducation(userInfo.getEdu());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
    userLikeListVo.setAge(userInfo.getAge());
    userLikeListVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
    userLikeListVo.setMatchRate(userInfo.getMatchRate());
    userLikeListVo.setId(userInfo.getId());
    userLikeListVo.setCity(userInfo.getCity());
    userLikeListVo.setAvatar(userInfo.getLogo());
