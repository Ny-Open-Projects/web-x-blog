# 画面线理解：13.环信用户系统集成之发送消息给客户端

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\13.环信用户系统集成之发送消息给客户端_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:45, 01:08, 01:29, 01:35, 01:48, 02:13, 02:33, 02:53, 03:22, 03:36, 04:02, 04:26, 05:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:12:24

1) 这一组画面整体在讲什么（一句话）：
演示如何通过后端服务向移动端用户发送消息，并在模拟器中验证消息推送功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“4.8. 发送消息给客户端”章节，说明接下来要进行测试发送消息。
画面2：在 Typora 文档中，展示“点赞”按钮的交互效果，说明点击后会发送一条消息。
画面3：在 Windows 资源管理器中，选中并右键“app-debug-14.apk”文件，准备安装到模拟器。
画面4：展示 Genymotion 模拟器的桌面，准备安装应用。
画面5：在 Genymotion 模拟器中，点击“应用”图标，准备安装 APK。
画面6：在 Genymotion 模拟器中，打开应用，显示“手机号登录注册”界面。
画面7：在 IntelliJ IDEA 中，查看 UserService.java 的 login 方法，用于验证用户登录。
画面8：在 Genymotion 模拟器中，输入手机号并点击“获取验证码”按钮。
画面9：在 Advanced REST Client 中，准备发送 POST 请求以模拟登录。
画面10：浏览器中打开环信 IM 的文档页面。
画面11：在环信 IM Console 中，查看用户列表，并点击“发送消息”。
画面12：在 Genymotion 模拟器中，打开“消息”界面。
画面13：在 Genymotion 模拟器中，点击“表情”按钮，展示表情面板。
画面14：在 Typora 文档中，展示“消息”界面，显示已发送的消息内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7：
```java
public String login(String mobile, String code) {
    //校验验证码是否正确
    String redisKey = "CHECK_CODE_" + mobile;
    String value = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.isEmpty(value)) {
        return null;
    }
    if (!StringUtils.equals(value, code)) {
        // 验证码输入错误
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
