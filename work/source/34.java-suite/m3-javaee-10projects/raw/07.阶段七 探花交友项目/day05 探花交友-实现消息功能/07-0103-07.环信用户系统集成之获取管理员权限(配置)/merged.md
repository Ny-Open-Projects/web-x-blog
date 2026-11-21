# 07.环信用户系统集成之获取管理员权限（配置）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\07.环信用户系统集成之获取管理员权限（配置）_【海量资源尽在 666java.com】.mp4
- 时长 2分54秒（音频 175s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实际的操作一下那么接下来呢我们将我们的这个用户体系的集成的逻辑啊我们写入到我们的SSO系统中那么首先呢我们需要在我们的SSO系统中啊去创建一个配置文件啊叫做环信啊.public配置文件那么我们创建一个fail把这个名字呢拷贝过来
[00:25] 叫环信然后呢publish fill然后呢需要有这么几个参数我们把这个参数也拷贝过来那么首先第一个呢是url那么这个url从哪来的呢其实刚才我们在讲这个API的时候呢可以看到它的地址是不是在这里啊这是它的一个这个地址啊然后呢这个odname那么odname它呢是在哪里可以找到呢我们在我们的控制台中啊那么再找一下啊那么这个
[00:54] AppKey都包含的就是一个autoname那么大家下面也有就它把它拷贝一下放到这儿来AppName就是我们所创建的名称叫什么叫做看花那么接着继续往下面看这个叫做什么Client ID那么Client ID在哪是在下面这个位置就是它那么把这个拷贝一下跟它一样然后还有个Client Secret这个是在下面的这个位置OK
[01:23] 好嘞好那么当然了下面还有这个就是用户的一个注册模式啊那么我们可以把它改为什么呢就是开放注册点击这个切换就可以了但是我们不需要切换啊那我们就保持这个呃禁止呃就是这个授权注册啊就可以了哎ok好那么有了这个配置文件之后啊那么接下来呢我们就需要把这个配置文件呢去载入到我们的spin的容器啊那我们需要写一个叫做环信config这样的一个
[01:51] 这个类然后呢去读取配置文件那么其他的在我们的一些其他的一些对象中啊我们只需要注入这个config就可以拿到关于这个属性的值了好那我们来拷贝一下把它拷贝到这config这个下面来啊好那么我们来看一下这个里面的这个配置啊那么首先呢我们这个里面呢去指定了我们这个类是一个configuration啊这样的一个类然后呢下面呢他呢去去引入我们的一个配置文件啊叫做什么呢
[02:21] class pass下面的一个环信publish配置文件然后我们去指定我们配置文件的参数prefix就它的前缀是这个碳化点这个环信这样的一个前缀那么我们来看一下我们的配置文件那么它的前缀是不是有这样的一个前缀所以说在我们这个位置就可以把这个值是不是就注进来了那么这样的话我们在其他类里面就能够直接去使用它了
[02:50] OK好那么关于配置我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

