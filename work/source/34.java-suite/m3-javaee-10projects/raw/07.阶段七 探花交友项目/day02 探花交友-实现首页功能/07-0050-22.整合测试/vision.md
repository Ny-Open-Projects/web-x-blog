# 画面线理解：22.整合测试

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\22.整合测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:25, 00:40, 00:56, 01:09, 01:28, 01:59, 02:28, 02:57, 03:10, 03:24, 04:16, 04:44, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:32:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Genymotion 模拟器上安装并测试一个名为“探花交友”的 Android 应用，该应用通过修改 API 地址来连接后端服务进行功能测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Typora 文档，标题为“4. 整合测试”。
- 文档内容提示：将资料中的 app-debug-004.apk 安装，并且修改服务地址进行测试。
- 屏幕截图展示应用启动界面，有“修改服务API地址”按钮。

画面 2：
- 展示 Genymotion 模拟器界面，显示一个虚拟设备“Custom Phone - 6.0.0”。
- 设备屏幕显示 Google 搜索栏和一个时钟图标。

画面 3：
- 展示文件资源管理器，路径为“资料\day02\资料”，其中包含“app-debug-004.apk”等文件。
- Genymotion 模拟器界面与画面 2 类似。

画面 4：
- 展示 Genymotion 主界面，显示“Your virtual devices”区域，其中有一个设备“Custom Phone - 6.0.0 - API 23 - 768x1280”。
- 界面提示“User not authenticated”。

画面 5：
- 展示 Genymotion 模拟器界面，显示一个应用界面，包含多个用户头像和点赞数。
- 屏幕右下角有“博学谷 www.boxuegu.com”水印。

画面 6：
- 展示 Genymotion 模拟器界面，设备屏幕显示一个大圆形加载动画。

画面 7：
- 展示 Windows 命令提示符窗口，显示网络适配器信息，包括“以太网适配器 Ethernet0”和“虚拟机网络适配器 VMware Network Adapter VMnet1”的 IP 地址。

画面 8：
- 展示 Genymotion 模拟器界面，显示“手机号登录注册”页面，包含“+86 输入手机号码”和“获取验证码”按钮。

画面 9：
- 展示 IntelliJ IDEA 编辑器界面，打开文件“RedisCacheInterceptor.java”。
- 代码中包含注解 `@Value("${tanhua.cache.enable}")` 和 `private Boolean enable;`。
- 调试窗口显示“preHandle”方法被调用，`enable` 值为 true。

画面 10：
- 展示 IntelliJ IDEA 编辑器界面，打开文件“MyResponseBodyAdvice.java”。
- 代码中包含 `@Override public boolean supports(MethodParameter ret)` 和 `@Override public Object beforeBodyWrite(Object body, ...)` 方法。
- Genymotion 模拟器界面显示应用主界面，包含“探花”、“附近”、“探花传音”等标签。

画面 11：
- 展示 Genymotion 模拟器界面，显示“手机号登录注册”页面，与画面 8 类似。

画面 12：
- 展示 IntelliJ IDEA 编辑器界面，显示“RedisCacheInterceptor.java”代码。
- Genymotion 模拟器界面显示应用主界面，包含“今日达人”和“推荐”内容。

画面 13：
- 显示 Typora 文档，标题为“4. 整合测试”。
- 文档内容提示：将资料中的 app-debug-004.apk 安装，并且修改服务地址进行测试。
- 屏幕截图展示应用启动界面，有“修改服务API地址”按钮。

画面 14：
- 显示 Typora 文档，内容为“修改为本机的地址：”。
- 屏幕截图展示应用设置界面，显示“Api基础地址”为“http://172.16.55.153”，并有“保存”按钮。
- 下方截图展示应用主界面，显示“今日达人”和“推荐”内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9：
```java
private RedisTemplate<String, String> redisTemplate;
@Value("${tanhua.cache.enable}")
private Boolean enable;
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
    if (enable) {
        //未开启缓存
    }
}
```

画面 10：
```java
@Override
public boolean supports(MethodParameter ret) {
    //支持的处理类，这里仅对get和post进行处理
    return returnType.hasMethodAnnotation(Post);
}
@Override
public Object beforeBodyWrite(Object body, ... ) {
    String redisKey = RedisCacheInterceptor.
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
