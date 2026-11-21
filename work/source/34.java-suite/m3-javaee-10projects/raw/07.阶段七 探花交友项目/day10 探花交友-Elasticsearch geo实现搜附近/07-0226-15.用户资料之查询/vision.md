# 画面线理解：15.用户资料之查询

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\15.用户资料之查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:55, 01:19, 02:08, 02:28, 04:11, 04:43, 05:21, 06:10, 06:49, 07:27, 08:24, 09:12, 10:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:33:05

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
