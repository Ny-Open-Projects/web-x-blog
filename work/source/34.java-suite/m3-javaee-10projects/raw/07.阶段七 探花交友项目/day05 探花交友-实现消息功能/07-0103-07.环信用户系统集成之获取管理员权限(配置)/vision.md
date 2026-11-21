# 画面线理解：07.环信用户系统集成之获取管理员权限（配置）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\07.环信用户系统集成之获取管理员权限（配置）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:22, 00:30, 00:38, 00:50, 01:00, 01:12, 01:20, 01:30, 01:38, 01:43, 02:02, 02:42, 02:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:07:52

1) 这一组画面整体在讲如何在 Spring Boot 项目中配置并集成环信（EaseMob）IM 服务，包括获取应用凭证、配置属性文件、编写配置类和控制器代码。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中查看 `MovementsController.java` 代码，其中包含调用 `this.quanziMQService.sendQueryPublishMsg(...)` 的逻辑。
画面2：在 IntelliJ IDEA 中右键点击 `resources` 目录，弹出“New”菜单，准备创建新文件。
画面3：在 IntelliJ IDEA 中打开 `huanxin.properties` 文件，准备编辑。
画面4：在浏览器中查看环信 API 文档，展示获取 token 的示例响应（200 成功，400 失败）。
画面5：在浏览器中访问环信 Console，显示应用列表页面，当前应用名为“探花”。
画面6：在 IntelliJ IDEA 中编辑 `huanxin.properties` 文件，配置环信服务的 URL、orgName、appName、clientId 和 clientSecret。
画面7：在浏览器中查看环信 Console 的应用详情页，显示应用的基本信息。
画面8：在浏览器中查看环信 Console 的应用详情页，鼠标悬停在 Client ID 上。
画面9：在浏览器中查看环信 Console 的应用详情页，弹出提示框询问是否将用户注册模式从“强制注册”改为“开放注册”。
画面10：在 IntelliJ IDEA 中编辑 `huanxin.properties` 文件，ClientSecret 字段被高亮显示。
画面11：在 Typora 中打开文档 `day05 满足.md`，显示“4.4.2. 获取token”章节的 Java 配置类代码。
画面12：在 Typora 中查看“4.4.2. 获取token”章节，代码高亮显示。
画面13：在 IntelliJ IDEA 中打开 `HuanXinConfig.java` 文件，显示 Spring Boot 配置类代码，其中 `@ConfigurationProperties(prefix = "tanhua.huanxin")` 被高亮。
画面14：在 Typora 中查看“4.4.2. 获取token”章节，代码高亮显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**（逐字原样抄录）：
画面1：
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryMovementsById(@PathVariableT
try {
    Movements movements = this.movementsService.queryMovement
    if(null != movements) {
        // 发送消息
        this.quanziMQService.sendQueryPublishMsg(publishId);
        return ResponseEntity.ok(movements);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR);
```

画面6：
```properties
tanhua.huanxin.url=http://al.easemob.com/
tanhua.huanxin.orgName=1105190515097562
tanhua.huanxin.appName=tanhua
tanhua.huanxin.clientId=YXA67ZoFwIblEems-_Fh-17T2g
tanhua.huanxin.clientSecret=YXA60r45rNy2Ux5wQ7YYoEPwYnHmU2k
```

画面11：
```java
package com.tanhua.sso.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:huanxin.properties")
@ConfigurationProperties(prefix = "tanhua.huanxin")
@Data
public class HuanXinConfig {
    private String url;
    private String orgName;
    private String appName;
    private String clientId;
    private String clientSecret;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
