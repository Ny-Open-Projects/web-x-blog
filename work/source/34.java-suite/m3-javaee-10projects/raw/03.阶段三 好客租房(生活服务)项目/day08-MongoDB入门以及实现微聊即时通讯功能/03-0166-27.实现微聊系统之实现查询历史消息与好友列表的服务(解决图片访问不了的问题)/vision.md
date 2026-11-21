# 画面线理解：27.实现微聊系统之实现查询历史消息与好友列表的服务（解决图片访问不了的问题）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\27.实现微聊系统之实现查询历史消息与好友列表的服务（解决图片访问不了的问题）【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:07, 00:09, 00:13, 00:19, 00:22, 00:24, 00:27, 00:28, 00:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:51:15

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 UserController 控制器查询用户列表并获取用户头像和聊天消息，过程中涉及代码调试、图片资源访问失败及多窗口操作。

2) 按时间顺序列出每张画面的要点：
画面1：
- 显示 IntelliJ IDEA 中 UserController.java 文件的代码，正在调试 queryUserList 方法。
- 代码中构建了一个 Map 结构，用于返回用户信息，包括 avatar、from_user、to_user、username 等字段。
- 代码注释说明“获取最后一条消息”，并有 TODO 注释“没有获取最新消息，而是获取了最早的那个消息”。
- 代码中调用 messageService.queryMessageList 方法，参数为 fromId、page=1、rows=1。

画面2：
- 显示 Adobe Reader 中的 PPT 内容，左侧是目录结构，右侧是代码。
- PPT 目录结构包括：2.1、2.2、2.3、2.4、2.5、2.6、2.7、2.8、2.9、3.1、3.2、3.3、3.4、3.5、3.6、3.7、3.8、3.9、4.1、4.2、4.3、4.4、4.5、4.6、4.7、4.8、4.9、5.1、5.2、5.3、5.4、5.5、5.6、5.7、5.8、5.9、6.1、6.2、6.3、6.4、6.5、6.6、6.7、6.8、6.9、7.1、7.2、7.3、7.4、7.5、7.6、7.7、7.8、7.9、8.1、8.2、8.3、8.4、8.5、8.6、8.7、8.8、8.9、9.1、9.2、9.3、9.4、9.5、9.6、9.7、9.8、9.9。
- 右侧代码部分显示了 queryUserList 方法的实现，包括构建 Map 结构和获取消息的逻辑。

画面3：
- 显示 IntelliJ IDEA 中 UserController.java 文件的代码，与画面1类似，但代码行号和注释略有不同。
- 代码中构建 Map 结构，用于返回用户信息，包括 avatar、from_user、to_user、username 等字段。
- 代码注释说明“获取最后一条消息”，并有 TODO 注释“没有获取最新消息，而是获取了最早的那个消息”。
- 代码中调用 messageService.queryMessageList 方法，参数为 fromId、page=1、rows=1。

画面4：
- 显示 IntelliJ IDEA 中 UserController.java 文件的代码，与画面1类似，但代码行号和注释略有不同。
- 代码中构建 Map 结构，用于返回用户信息，包括 avatar、from_user、to_user、username 等字段。
- 代码注释说明“获取最后一条消息”，并有 TODO 注释“没有获取最新消息，而是获取了最早的那个消息”。
- 代码中调用 messageService.queryMessageList 方法，参数为 fromId、page=1、rows=1。

画面5：
- 显示浏览器中访问图片资源的页面，地址为：itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg。
- 页面显示“无法访问此网站”，提示找不到服务器 IP 地址，错误代码为：ERR_NAME_NOT_RESOLVED。

画面6：
- 显示浏览器中成功加载的图片，图片为一个卡通人物，背景为红色心形图案。
- 图片内容为一个戴眼镜、短发、吐舌头的卡通人物。

画面7：
- 显示电脑桌面，显示了多个窗口，包括 IntelliJ IDEA、浏览器、Adobe Reader 等。
- 窗口内容包括代码、图片、PPT 等。

画面8：
- 显示 IntelliJ IDEA 中 UserController.java 文件的代码，与画面1类似，但代码行号和注释略有不同。
- 代码中构建 Map 结构，用于返回用户信息，包括 avatar、from_user、to_user、username 等字段。
- 代码注释说明“获取最后一条消息”，并有 TODO 注释“没有获取最新消息，而是获取了最早的那个消息”。
- 代码中调用 messageService.queryMessageList 方法，参数为 fromId、page=1、rows=1。

画面9：
- 显示 Adobe Reader 中的 PPT 内容，左侧是目录结构，右侧是代码。
- PPT 目录结构包括：2.1、2.2、2.3、2.4、2.5、2.6、2.7、2.8、2.9、3.1、3.2、3.3、3.4、3.5、3.6、3.7、3.8、3.9、4.1、4.2、4.3、4.4、4.5、4.6、4.7、4.8、4.9、5.1、5.2、5.3、5.4、5.5、5.6、5.7、5.8、5.9、6.1、6.2、6.3、6.4、6.5、6.6、6.7、6.8、6.9、7.1、7.2、7.3、7.4、7.5、7.6、7.7、7.8、7.9、8.1、8.2、8.3、8.4、8.5、8.6、8.7、8.8、8.9、9.1、9.2、9.3、9.4、9.5、9.6、9.7、9.8、9.9。
- 右侧代码部分显示了 queryUserList 方法的实现，包括构建 Map 结构和获取消息的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping("user")
public class UserController {

    @Autowired
    private MessageService messageService;

    //获取用户列表（模拟实现）
    @GetMapping
    public List<Map<String, Object>> queryUserList(@RequestParam("fromId") Long fromId) {
        List<Map<String, Object>> result = new ArrayList<>();
        for (Map.Entry<Long, User> userEntry : UserData.USER_MAP.entrySet()) {
            Map<String, Object> map = new HashMap<>();
            map.put("id", userEntry.getValue().getId());
            map.put("avatar", "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg");
            map.put("from_user", fromId);
            map.put("info_type", null);
            map.put("to_user", map.get("id"));
            map.put("username", userEntry.getValue().getUsername());
            // 获取最后一条消息 TODO 没有获取最新消息，而是获取了最早的那个消息
            List<Message> messages = this.messageService.queryMessageList(fromId, userEntry.getValue().getId(), page: 1, rows: 1);
            map.put("chat_time", message.getSendDate().getTime());
        }
        return result;
    }
}
```

画面2：
```java
private MessageService messageService;

@GetMapping
public List<Map<String, Object>> queryUserList(@RequestParam("fromId") Long fromId) {
    List<Map<String, Object>> result = new ArrayList<>();
    for (Map.Entry<Long, User> userEntry : UserData.USER_MAP.entrySet()) {
        Map<String, Object> map = new HashMap<>();
        map.put("id", userEntry.getValue().getId());
        map.put("avatar", "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg");
        map.put("from_user", fromId);
        map.put("info_type", null);
        map.put("to_user", map.get("id"));
        map.put("username", userEntry.getValue().getUsername());
        // 获取最后一条消息
        List<Message> messages = this.messageService.queryMessageList(fromId, userEntry.getValue().getId(), 1, 1);
        if (messages != null && !messages.isEmpty()) {
            Message message = messages.get(0);
            map.put("chat_msg", message.getMsg());
            map.put("chat_time", message.getSendDate().getTime());
        }
    }
    return result;
}
```

画面3：
```java
@RequestMapping("user")
public class UserController {

    @Autowired
    private MessageService messageService;

    //获取用户列表（模拟实现）
    @GetMapping
    public List<Map<String
