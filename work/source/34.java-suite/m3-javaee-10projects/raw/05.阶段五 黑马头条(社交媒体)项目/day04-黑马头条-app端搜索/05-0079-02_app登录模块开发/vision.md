# 画面线理解：02_app登录模块开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\02_app登录模块开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:46, 03:00, 04:12, 05:18, 07:20, 08:30, 09:28, 10:37, 12:05, 12:53, 14:00, 15:28, 16:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:26:43

1) 这一组画面整体在讲什么（一句话）：
演示一个用户登录功能的前后端开发流程，包括接口定义、代码实现、配置文件和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文章详情前端开发文档，重点是“1.1 登录接口”部分，包含接口名称、请求DTO和响应DTO的定义。
画面2：IDEA项目结构视图，显示项目模块“heima-leadnews-login”及其依赖的配置文件。
画面3：展示`pom.xml`文件中的依赖配置，包含Spring Boot测试、Jackson数据格式化等依赖。
画面4：在IDEA中搜索并定位到`ApUserMapper`相关的类文件。
画面5：展示`MysqlConfig.java`文件，用于配置数据库连接。
画面6：展示`ApUserLoginService.java`服务接口文件。
画面7：展示`ApUserLoginServiceImpl.java`服务实现类，开始编写登录逻辑。
画面8：在`ApUserLoginServiceImpl.java`中，添加了对用户数据不存在的异常处理。
画面9：展示`ApUserLoginServiceImpl.java`中，对密码不匹配的异常处理。
画面10：展示`AppUtil.java`工具类，用于生成JWT令牌。
画面11：在`ApUserLoginServiceImpl.java`中，完成登录逻辑，返回包含用户信息和令牌的响应。
画面12：在IDEA中右键项目，选择“Run 'heima-leadnews-login'”以运行项目。
画面13：展示`LoginController.java`控制器类，用于接收前端登录请求。
画面14：在`LoginController.java`中，编写了`@PostMapping("/login_auth")`方法，调用服务层的登录方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
接口名称：/api/v1/login_auth
请求DTO：com.heima.model.user.pojos.ApUser
响应DTO：ResponseResult(token:“验证字符串”user:“用户信息”)

画面2：
无代码或配置内容。

画面3：
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.dataformat</groupId>
        <artifactId>jackson-dataformat-xml</artifactId>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.dataformat</groupId>
        <artifactId>jackson-dataformat-yaml</artifactId>
    </dependency>
</dependencies>

画面4：
无代码或配置内容。

画面5：
package com.heima.login.config;
import org.springframework.context.annotation.Configuration;
@Configuration
public class MysqlConfig {

}

画面6：
无代码或配置内容。

画面7：
import com.heima.login.service.ApUserLoginService;
import com.heima.model.common.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ApUserLoginServiceImpl implements ApUserLoginService {

画面8：
import com.heima.login.service.ApUserLoginService;
import com.heima.model.common.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApUserLoginServiceImpl implements ApUserLoginService {
    @Autowired
    private ApUserMapper apUserMapper;
    @Override
    public ResponseResult loginAuth(ApUser user) {
        if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
        }
        ApUser apUser = apUserMapper.selectByPhone(user.getPhone());
        if (apUser == null) {
            return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
        }
        return null;
    }

画面9：
import com.heima.login.service.ApUserLoginService;
import com.heima.model.common.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApUserLoginServiceImpl implements ApUserLoginService {
    @Autowired
    private ApUserMapper apUserMapper;
    @Override
    public ResponseResult loginAuth(ApUser user) {
        if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
        }
        ApUser apUser = apUserMapper.selectByPhone(user.getPhone());
        if (apUser == null) {
            return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
        }
        if (user.getPassword().equals(apUser.getPassword())) {
            return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
        }
        return null;
    }

画面10：
public static String getToken(WhUser user) { return getToken(user.getId()); }
private static String getToken(Long id) {
    Map<String, Object> claimMap = new HashMap<>();
    claimMap.put("id", id);
    long current = System.currentTimeMillis();
    return Jwts.builder()
            .setSubject("heima")
            .setIssuedAt(new Date(current))
            .setExpiration(new Date(current + TOKEN_TIME_OUT * 1000))
            .setAudience("app")
            .compressWith(CompressionCodecs.GZIP)
            .signWith(SignatureAlgorithm.HS256, generateMer())
            .addClaims(claimMap)
            .compact();
}

画面11：
import com.heima.login.service.ApUserLoginService;
import com.heima.model.common.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApUserLoginServiceImpl implements ApUserLoginService {
    @Autowired
    private ApUserMapper apUserMapper;
    @Override
    public ResponseResult loginAuth(ApUser user) {
        if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
        }
        ApUser apUser = apUserMapper.selectByPhone(user.getPhone());
        if (apUser == null) {
            return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
        }
        if (user.getPassword().equals(apUser.getPassword())) {
            return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
        }
        Map<String, Object> map = new HashMap<>();
        map.put("token", AppUtil.getToken(user));
        map.put("user", apUser);
        return ResponseResult.okResult(map);
    }

画面12：
无代码或配置内容。

画面13：
package com.heima.login.controller.v1;
import com.heima.login.apis.LoginControllerApi;
public class LoginController implements LoginControllerApi {

画面14：
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/login")
public class LoginController implements LoginControllerApi {
    @Autowired
    private ApUserLoginService apUserLoginService;
    @PostMapping("/login_auth")
    public ResponseResult login(@RequestBody ApUser user) {
        return apUserLoginService.loginAuth(user);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1 文章详情-前端开发”，子标题为“1.1 登录接口”，并包含“参考标准”部分。
画面2：无PPT或架构图。
画面3：无PPT或架构图。
画面4：无PPT或架构图。
画面5：无PPT或架构图。
画面6：无PPT或架构图。
画面7：无PPT或架构图。
画面8：无PPT或架构图。
画面9：无PPT或架构图。
画面10：无PPT或架构图。
画面11：无PPT或架构图。
画面12：无PPT或架构图。
画面13：无PPT或架构图。
画面14：无PPT或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
