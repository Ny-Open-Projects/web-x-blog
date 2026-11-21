# 画面线理解：13-刷脸登录：搭建环境-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\13-刷脸登录：搭建环境-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:07, 01:46, 02:13, 02:32, 03:33, 05:08, 05:32, 06:15, 06:57, 09:02, 09:30, 09:45, 10:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:01:58

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成百度人脸 API 实现人脸登录功能，包括依赖配置、实体类、工具类开发和配置文件设置。

2) 按时间顺序列出每张画面的要点：
画面1：桌面环境，显示“黑马程序员”和“博学谷”标志，无具体操作。
画面2：Notepad++ 编辑器中显示 Maven 依赖配置，包含百度 SDK 和 ZXing 依赖。
画面3：IntelliJ IDEA 项目结构，展示 ihm_parent 项目下的 ihm_system 模块。
画面4：桌面环境，鼠标悬停在“ihm”文件上。
画面5：PPT 页面，展示用户登录流程图，包含二维码生成、Redis 状态存储、人脸检测、登录成功/失败状态码逻辑。
画面6：IntelliJ IDEA 中展示 FaceLoginResult 实体类代码，包含 state、token、userId 字段和构造方法。
画面7：IntelliJ IDEA 项目结构，选中 ihm_common_model 模块。
画面8：IntelliJ IDEA 项目结构，选中 ihm_system 模块。
画面9：IntelliJ IDEA 中展示 BaiduAIUtil 工具类代码，包含 @Component 注解、私有字段和 init 方法。
画面10：IntelliJ IDEA 中展示 BaiduAIUtil 类的 faceRegister 和 faceUpdate 方法。
画面11：IntelliJ IDEA 中展示 BaiduAIUtil 类的 faceCheck 和 faceSearch 方法。
画面12：IntelliJ IDEA 项目结构，选中 ihm_employee 模块。
画面13：Notepad++ 编辑器中显示百度人脸 API 的配置信息，包括 apiId、apiKey、secretKey、imageType、groupId 和 url。
画面14：IntelliJ IDEA 中展示 application.yml 配置文件，包含数据库、Redis、ai 配置项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```xml
<dependency>
    <groupId>com.baidu.sip</groupId>
    <artifactId>java-sdk</artifactId>
    <version>4.8.0</version>
</dependency>
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>core</artifactId>
    <version>3.2.1c</version>
</dependency>
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>javasec</artifactId>
    <version>3.2.1c</version>
</dependency>
```

画面6：
```java
package com.ihm.domain.system.response;
import java.io.Serializable;
@Data
@NoArgsConstructor
@ToString
public class FaceLoginResult implements Serializable {
    private static final long serialVersionUID = -1618426841373762391L;
    // 二维使用状态
    private String state;
    // 登录信息
    private String token;
    // 用户ID
    private String userId;
    public FaceLoginResult(String state, String token, String userId) {
        this.state = state;
    }
}
```

画面9：
```java
package com.ihm.system.utils;
import org.springframework.stereotype.Component;
@Component
public class BaiduAIUtil {
    @Value("${ai.appId}")
    private String APP_ID;
    @Value("${ai.apiKey}")
    private String API_KEY;
    @Value("${ai.secretKey}")
    private String SECRET_KEY;
    @Value("${ai.imageType}")
    private String IMAGE_TYPE;
    @Value("${ai.groupId}")
    private String groupId;
    private AipFace client;
    private HashMap<String, String> options = new HashMap<>();
    public BaiduAIUtil() {
        options.put("quality_control", "NORMAL");
        options.put("liveness_control", "LOW");
    }
    @PostConstruct
    public void init() { client = new AipFace(APP_ID, API_KEY, SECRET_KEY); }
}
```

画面10：
```java
public Boolean faceRegister(String userId, String image) {
    // 人脸注册
    JSONObject res = client.addUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt("error_code");
    return errorCode == 0 ? true : false;
}
public Boolean faceUpdate(String userId, String image) {
    // 人脸更新
    JSONObject res = client.updateUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt("error_code");
    return errorCode == 0 ? true : false;
}
```

画面11：
```java
Integer errorCode = res.getInt("error_code");
return errorCode == 0 ? true : false;
public Boolean faceCheck(String image) {
    JSONObject res = client.detect(image, IMAGE_TYPE, options);
    if (res.has("error_code") && res.getInt("error_code") == 0) {
        JSONObject resultObject = res.getJSONObject("result");
        Integer faceNum = resultObject.getInt("face_num"); // 人脸数量
        return faceNum == 1 ? true : false;
    } else {
        return false;
    }
}
public String faceSearch(String image) {
    JSONObject res = client.search(image, IMAGE_TYPE, groupId, options);
    if (res.has("error_code") && res.getInt("error_code") == 0) {
        JSONObject result = res.getJSONObject("result");
        JSONArray userList = result.getJSONArray("user_list");
        if (userList.length() > 0) {
            return userList.getJSONObject(index: 0);
        }
    }
}
```

画面13：
```
apiId: 15191935
apiKey: cyWSHgac93Vtdmt42OwbM6pu
secretKey: yflGusMvCLBdOnyabFlubMyod91EDEZW
imageType: BASE64
groupId: itcast
url: https://192.168.50.110:8080/4/FaceLogin
```

画面14：
```yaml
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
jpa:
  database: MySQL
  show-sql: true
  open-in-view: true
redis:
  host: 127.0.0.1
  port: 6379
jwt:
  config:
    key: adds-ihm
    ttl: 3600000
ai:
  appId: 15191935
  apiKey: cyWSHgac93Vtdmt42OwbM6pu
  secretKey: yflGusMvCLBdOnyabFlubMyod91EDEZW
  imageType: BASE64
  groupId: itcast
  url: https://localhost:8080/faceLogin
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：PPT 页面标题为“用户登录页面”和“落地页（魔扫篇）”。流程图结构：
- 用户登录页面 → 生成二维码 → 存入 Redis（用户未扫描状态：-1）
- 用户扫描二维码 → 调用手机摄像头拍照 → 检查是否有面部头像 → 1234：-1（未扫描）
- 根据唯一标识是否登录成功 → 查询 Redis 状态 → 进行后续操作
- Redis 状态：1234：-1（未扫描）→ 1234：1（登录成功）→ 1234：0（登录失败）

5) 无其他内容。
