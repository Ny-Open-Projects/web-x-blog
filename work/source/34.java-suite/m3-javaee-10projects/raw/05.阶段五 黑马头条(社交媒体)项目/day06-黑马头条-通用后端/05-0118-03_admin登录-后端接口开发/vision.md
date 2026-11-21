# 画面线理解：03_admin登录-后端接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\03_admin登录-后端接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:14, 01:52, 02:23, 03:21, 04:19, 05:15, 05:48, 06:52, 07:27, 08:11, 08:46, 09:55, 10:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:59:39

1) 这一组画面整体在讲什么（一句话）：
实现管理员登录功能的后端代码，包括接口定义、实体类、Mapper、Service 和 Controller 层的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，讲解登录接口定义，包括请求DTO为 com.heima.admin.pojos.AdUser，响应DTO为返回map(token,xxx_user)。同时展示AdUser实体类的代码，包含id, name, password, salt, nickname, image, phone, status, email, login_time, created_time等字段。
画面2：展示项目结构，定位到SecurityConfig.java文件，准备引入相关依赖。
画面3：展示登录接口定义文档，定义了登录接口的请求和响应DTO。
画面4：展示项目结构，定位到AdUserMapper.xml文件，查看其中的SQL语句和resultMap定义。
画面5：展示UserLoginService接口定义，定义了login方法。
画面6：展示UserLoginServiceImpl类，开始编写login方法，导入相关依赖。
画面7：在login方法中添加了对用户名和密码是否为空的校验，如果为空则返回错误信息。
画面8：在login方法中添加了对用户是否存在和密码是否正确的校验，如果用户不存在则返回错误信息。
画面9：在login方法中添加了对密码是否正确的校验，如果密码不正确则返回错误信息。
画面10：在login方法中添加了对用户信息的封装，将用户信息放入map中并返回。
画面11：在login方法中添加了对用户密码的加密处理，将加密后的密码放入map中并返回。
画面12：展示LoginController类，定义了login方法，调用UserLoginService的login方法。
画面13：展示LoginController类，定义了login方法，调用UserLoginService的login方法。
画面14：展示LoginController类，定义了login方法，调用UserLoginService的login方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
(5) 在Bcom.heima.admin.config中引入配置：jackson, security, mysql
1.2 登录接口-后端
1.2.1接口定义
参考标准 请参考专用接口规范
端口名称 /login/in
请求DTO com.heima.model.admin.pojos.AdUser
响应DTO 返回map(token,xxx_user)
1.2.2mapper定义
(1)admin用户实体类com.heima.model.admin.pojos.AdUser
@Data
public class AdUser {
    private Long id;
    private String name;
    private String password;
    private String salt;
    private String nickname;
    private String image;
    private String phone;
}
```
画面4：
```
<mapper namespace="com.heima.model.mappers.admin.AdUserMapper">
    <resultMap id="Base_Column_List" type="com.heima.model.admin.pojos.AdUser">
        <result column="id" property="id"/>
        <result column="name" property="name"/>
        <result column="password" property="password"/>
        <result column="salt" property="salt"/>
        <result column="nickname" property="nickname"/>
        <result column="image" property="image"/>
        <result column="phone" property="phone"/>
        <result column="status" property="status"/>
        <result column="email" property="email"/>
        <result column="login_time" property="login_time"/>
        <result column="created_time" property="created_time"/>
    </resultMap>

    <sql id="Base_Column_List">
        id, name, password, salt, nickname, image, phone, status, email, login_time, created_time
    </sql>

    <select id="selectByName" resultType="com.heima.model.admin.pojos.AdUser">
        select <include refid="Base_Column_List"/>
        from ad_user where name = #{name} limit 1
    </select>
</mapper>
```
画面5：
```
public interface UserLoginService {
    ResponseResult login(AdUser user);
}
```
画面6：
```
package com.heima.admin.service.impl;
import com.heima.admin.service.UserLoginService;
import com.heima.model.admin.pojos.AdUser;
import com.heima.model.common.dtos.ResponseResult;
import org.springframework.stereotype.Service;

@Service
public class UserLoginServiceImpl implements UserLoginService {
    @Override
    public ResponseResult login(AdUser user) {
        return null;
    }
}
```
画面7：
```
public ResponseResult login(AdUser user) {
    if(StringUtils.isEmpty(user.getName()) && StringUtils.isEmpty(user.getPassword())){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "用户和密码不能为空");
    }
    return null;
}
```
画面8：
```
public ResponseResult login(AdUser user) {
    if(StringUtils.isEmpty(user.getName()) && StringUtils.isEmpty(user.getPassword())){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "用户和密码不能为空");
    }
    AdUser aduser = adUserMapper.selectByName(user.getName());
    if(aduser == null){
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "用户不存在");
    }
    return null;
}
```
画面9：
```
public ResponseResult login(AdUser user) {
    if(StringUtils.isEmpty(user.getName()) && StringUtils.isEmpty(user.getPassword())){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "用户和密码不能为空");
    }
    AdUser aduser = adUserMapper.selectByName(user.getName());
    if(aduser == null){
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "用户不存在");
    }else{
        if(user.getPassword().equals(aduser.getPassword())){
            return ResponseResult.success();
        }else{
            return ResponseResult.errorResult(AppHttpCodeEnum.LOG_IN_PASSWORD_ERROR, "密码错误");
        }
    }
    return null;
}
```
画面10：
```
public ResponseResult login(AdUser user) {
    if(StringUtils.isEmpty(user.getName()) && StringUtils.isEmpty(user.getPassword())){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "用户和密码不能为空");
    }
    AdUser aduser = adUserMapper.selectByName(user.getName());
    if(aduser == null){
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "用户不存在");
    }else{
        if(user.getPassword().equals(aduser.getPassword())){
            Map<String, Object> map = new HashMap<>();
            map.put("user", aduser);
            return ResponseResult.success(map);
        }else{
            return ResponseResult.errorResult(AppHttpCodeEnum.LOG_IN_PASSWORD_ERROR, "密码错误");
        }
    }
    return null;
}
```
画面11：
```
public ResponseResult login(AdUser user) {
    if(StringUtils.isEmpty(user.getName()) && StringUtils.isEmpty(user.getPassword())){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "用户和密码不能为空");
    }
    AdUser aduser = adUserMapper.selectByName(user.getName());
    if(aduser == null){
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "用户不存在");
    }else{
        if(user.getPassword().equals(aduser.getPassword())){
            Map<String, Object> map = new HashMap<>();
            aduser.setSalt(AdUserUtil.getSalt(aduser));
            map.put("token", AdUserUtil.getToken(aduser));
            map.put("user", aduser);
            return ResponseResult.success(map);
        }else{
            return ResponseResult.errorResult(AppHttpCodeEnum.LOG_IN_PASSWORD_ERROR, "密码错误");
        }
    }
    return null;
}
```
画面12：
```
package com.heima.admin.controller;
import com.heima.admin.service.UserLoginService;
import com.heima.model.admin.pojos.AdUser;
import com.heima.model.common.dtos.ResponseResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/login")
public class LoginController {
    @Autowired
    private UserLoginService userLoginService;

    @PostMapping("/in")
    public ResponseResult login(AdUser user) {
        return userLoginService.login(user);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
