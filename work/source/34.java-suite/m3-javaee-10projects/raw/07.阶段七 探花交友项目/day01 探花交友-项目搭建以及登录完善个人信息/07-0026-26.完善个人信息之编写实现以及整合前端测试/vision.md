# 画面线理解：26.完善个人信息之编写实现以及整合前端测试

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\26.完善个人信息之编写实现以及整合前端测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:03, 02:13, 03:41, 04:47, 05:31, 06:39, 07:19, 08:35, 09:20, 10:35, 11:45, 13:00, 14:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:15:24

1) 这一组画面整体在讲什么（一句话）：
实现完善用户个人信息功能，包括前端接口定义、后端服务层代码编写、数据库操作及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“4.3. 实现完善个人信息”章节，包含 mock 接口地址 https://mock.boxuegu.com/project/164/interface/api/28553，用于定义完善个人信息的请求参数（Headers: Content-Type: application/json，Body: gender, nickname, birthday, city）。
画面2：展示 UserInfoService.java 代码，定义了 saveUserInfo 方法，注入了 UserInfoMapper、UserService、FaceEngineService、PicUploadService。
画面3：在 UserInfoService.java 中，展示 saveUserInfo 方法的逻辑，通过 token 查询用户，若用户为空则返回 false，否则创建 UserInfo 对象并设置属性。
画面4：展示 UserInfoController.java 代码，定义了 saveUserInfo 接口，接收 param 和 token 参数，调用 userInfoService.saveUserInfo。
画面5：展示 UserInfoController.java 的完整代码，包含注解 @RestController、@RequestMapping、@Autowired、@PostMapping 等。
画面6：在 Advanced REST Client 中，设置 POST 请求地址为 http://172.16.55.153:18080/user/loginRegInfo，设置 Authorization 头，Body 为 JSON 格式数据：{"gender": "man", "nickname": "张三", "birthday": "2000-01-01", "city": "北京"}。
画面7：展示 UserInfoService.java 中 saveUserInfo 方法的完整代码，包括设置用户信息、插入数据库、返回 true。
画面8：在 Advanced REST Client 中，展示历史请求记录，包含多个 POST 请求，如 /user/loginRegInfo、/user/login、/picupload 等。
画面9：展示 UserInfoController.java 中 saveLogo 方法的代码，用于处理头像上传，调用 userInfoService.saveLogo，异常时返回错误信息。
画面10：展示 Genymotion 模拟器中手机登录注册页面，用户输入手机号并点击“获取验证码”。
画面11：在 Navicat Premium 中，展示 tb_user 表的数据，包含 password、created、updated 字段。
画面12：展示 Genymotion 模拟器中手机登录注册页面，用户输入手机号并点击“获取验证码”。
画面13：展示 Genymotion 模拟器中手机登录注册页面，用户点击“获取验证码”按钮。
画面14：展示 Typora 文档中“4.3.1. UserInfoMapper”和“4.3.2. UserInfoService”章节，UserInfoMapper 接口定义了插入用户信息的方法，UserInfoService 包含 import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
import org.springframework.web.multipart.MultipartFile;
import java.util.Map;
@Service
public class UserInfoService {
    private static final Logger LOGGER = LoggerFactory.getLogger(UserInfoService.class);
    @Autowired
    private UserInfoMapper userInfoMapper;
    @Autowired
    private UserService userService;
    @Autowired
    private FaceEngineService faceEngineService;
    @Autowired
    private PicUploadService picUploadService;
    // 完善个人信息
    @Return
    public Boolean saveUserInfo(Map<String, String> param, String token) {
        User user = this.userService.queryUserByToken(token);
        if (user == null) {
            return false;
        }
        UserInfo userInfo = new UserInfo();
        userInfo.setUserId(user.getId());
        userInfo.setSex(StringUtils.equals(param.get("gender"), "man") ? SexEnum.MAN : SexEnum.WOMAN);
        userInfo.setNickname(param.get("nickname"));
        userInfo.setBirthday(param.get("birthday"));
        userInfo.setCity(param.get("city"));
        // 保存UserInfo数据到数据库
        this.userInfoMapper.insert(userInfo);
        return true;
    }
```

画面4：
```java
package com.tanhua.sso.controller;
import ...
@RestController
@RequestMapping("user")
public class UserInfoController {
    @Autowired
    private UserInfoService userInfoService;
    /*
     * 完善个人信息
     * @param param
     * @param token
     * @return
     */
    @PostMapping("/loginRegInfo")
    public ResponseEntity<Object> saveUserInfo(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
        Boolean saveUserInfo = this.userInfoService.saveUserInfo(param, token);
        return ResponseEntity.ok(saveUserInfo);
    }
```

画面7：
```java
UserInfo userInfo = new UserInfo();
userInfo.setUserId(user.getId());
userInfo.setSex(StringUtils.equals(param.get("gender"), "man") ? SexEnum.MAN : SexEnum.WOMAN);
userInfo.setNickname(param.get("nickname"));
userInfo.setBirthday(param.get("birthday"));
userInfo.setCity(param.get("city"));
// 保存UserInfo数据到数据库
this.userInfoMapper.insert(userInfo);
return true;
```

画面9：
```java
try {
    Boolean bool = this.userInfoService.saveLogo(file, token);
    if (bool) {
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").errMessage("图片非人像，请重新上传").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面14：
```java
package com.tanhua.sso.mapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.tanhua.sso.pojo.UserInfo;
public interface UserInfoMapper extends BaseMapper<UserInfo> {
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
