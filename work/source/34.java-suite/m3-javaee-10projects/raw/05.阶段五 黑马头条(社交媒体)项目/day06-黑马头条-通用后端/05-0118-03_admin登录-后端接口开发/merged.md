# 03_admin登录-后端接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\03_admin登录-后端接口开发【海量资源尽在 666java.com】.mp4
- 时长 11分4秒（音频 665s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成登录接口的后端开发当前的微服已经有了现在咱们就来去开发接口首先还是来看一下当前的接口定义当前的接口是叫名称是叫loginlog然后是有一个in然后当前的dto就是当前的用户叫aduseraduser它其实admin端的一个user然后你返回的时候重点去强调了一个东西就是有一个token
[00:29] 还是token是吧还有一个用户信息跟咱们之前登录好像没啥区别是吧其实类似的现在咱们就快点写好吧不浪费时间首先这个就是那个表这个表的话就是AD user里边你也可以打开这个表去看一下在这右键你可以打开对象消息这个就是一些字段的描述其实跟咱们当前自媒体那个用户其实差不多的是差不多的
[00:59] 行这个表比较简单咱们也只是去查一下做个简单的登录行咱们下面就来去完成当前的Map这Map的话还是一个还是要去创建一个名称去查询目前用户的一个方法好打开当前的model打开model之后在这Map下面Map私下边有一个admin在admin上面去创建好这个就创建完了创建完之后它需要干嘛它需要有一个这种映射文件
[01:31] 拷贝一下改个名叫user好吧然后把里边内容删掉是什么aguser mypro是吧好那这样的话咱们把这个方法给拿过来只有一个就只是查询是按照名称去查询上面是一些映射下面是一个circle片段是它的字段名然后下面是真正的一个查询的方法
[02:05] OK就是根据当前的名字去查询好那这个查询完之后啊下面咱们就来写Service那这个Service咱们就还是在当前的admin啊admin端去创建Service就可以了来看一下嗯打开这这咱们在这之前是不是创建那个Service这个包啊在这去创建个类啊叫goeserlogin Service它是一个接口这里边呢有一个方法那这个方法怎么
[02:38] 就叫login public response result然后是login好吧参数是啥参数就是dd user完了这个就是登录这写一下是登录下面咱们就来写它的实现类去创建一个类什么mpl下面的user login Service
[03:08] 让他去实现当前的user login Service好那这个方法就实现了在这去加一个Service注解然后你可以把你的mypro给输入进来private 叫 ad user mypro好 注进来之后咱们下面就来去写他的逻辑首先还是要去
[03:37] 这里边咱们要去判断参数你这里边你一个页面里边你要去输入用户名或者是密码是吧所以说咱们首先要判断的参数呢不是用户名和密码我说你的密码和用户名空的话呢咱们肯定就这个就不能让他去往下走了是吧所以说在这啊写一个string use.get user
[04:07] 按的按的按的啥呢啊这是写错了往外一点啊按的什么就是准youtube.isempty什么youtube.setpassword如果说他两个都为空的话呢我们就直接return就可以了returnvice-result 而 error result如果你的参数有问题pp参数有问题是这个是下面这个啊下面咱们可以提示一句话是吧提示啥呀
[04:37] 我们就可以说啊用户货密码啊用户和密码不能未空好和这是和不是货因为咱们现在是那两个是暗的的关系好吧行那创建完之后啊咱们下面继续往下看那这报错是吧怎么办呢先不写啊在这去加一个什么duperduper warning是吧ok先去提示啊看着不爽啊好接着往下看啊然后下面呢咱们就来干嘛了
[05:07] 下面咱们就可以去查询了啊查询比如说ad user-myper.select by name或是user.get name好这时候就拿到一个ad user拿到ad user之后啊咱们就可以判断了啊他到底是否为空ad user若说他没等应当那这时候呢就没查出来呗没查出来的话咱们就可以提示用户return raise bounce result.error by result
[05:38] 最终是有一个数据不存在啊我们找一找啊先写吧然后再下面去删掉一个叫做datanautexense是吧说你的数据不存在啊你可以去提示一句提示啥呢提示啊你说你的用户不存在用户不存在OK那这个如果说都没问题的话啊没问题的话咱们下面呢就可以干嘛呢就可以去返回了啊
[06:10] 这个else呢咱们就可以去先去判断密码是吧这个UFO能查出来但是密码对不对呢咱们在这user.get password然后呢是.eco下面是aduser.get password这个呢是从哪从前台传过来的这是从数据库中查出来的对吧如果说他俩一这样的话呢
[06:41] 这时候才真正的去往下走如果说不一样的话咱们可以提示一下VLSI不一样的话就提示密码错误就可以了直接return还是response咱们之前是写过的写一个app h然后你说你的密码错了怎么写一个login按sword说你的密码错了好吧这个试完之后试完之后咱们下面就可以在这去写了
[07:09] 刚才说了咱们这介绍里边呢咱们需要去封装一些东西封装token和usertoken和user啊所以说啊咱们在这啊先去创建一个map这map里边咱们再去装当前的user和token啊比如说object嗯开包说map等于new一个hashi map好加完之后呢咱们就可以去设置东西了啊比如说map.put
[07:45] 谁呢第一个就是token好我怎么拿呀是不是有个类呀叫appdwt然后是打什么有一个ad user你把谁装进去啊ad user装进去就完事了好吧然后再往下啊还有是map.put是谁呢put咱们的一个user把user也装进去然后他呢就是ad user然后最终呢你可以去returnreturn是谁呀
[08:18] 要ResponseResultOK好把当前的MAP装进去完了这样的话咱们这个接口就算是写完了写完之前呢还要再给大家提个醒这个密码是不是咱们不正常返回啊ADUser.set什么password你谁空还有一个叫什么ADUser.set一个言是吧set是吧这东西咱们也要设置为空安全起见啊
[08:49] 你说这块你一定要设置为空那目前的话这个接口就算是设置完了把这个给他删了行那当前那个Service就算是做完了下面咱们就顺便的去来去再去写一个Controller在这去写啊啊可能说之前呢咱们还是在当前的APS里边啊去定义打开APS来打开这然后呢在这呢去创建一个没有的命是吧哎在这去写打开一个额的命创建个包吧
[09:18] 直接创建个类型admin.apis.logincontroller.tp好吧它是一个类型有一个方法方法的话就是谁啊response.login好吧单数就是aduser这样的话咱们就算是定完了这是登录然后下面咱们就来去定义它的具体的Controller
[09:51] 现在admin下面这去写右键在这去写一个类叫他把API给他去掉让他去实现谁呀实现刚才定的接口嗯错了啊这个拨名导错了啊那个呀admin下面的啊然后是ctrl i在这去加一个东西叫什么best control然后下面去顺便把这东西也加上啊
[10:25] 叫request mapping这个呢前面是叫要注意啊前面是叫login啊login啊好那么这个咱们也加上叫post mapping然后是这啥就是in好吧那这时候呢你就可以去把当前的Service给注入进来了啊我private叫user login Service好进来之后呢你可以去注入注入完之后可以直接就用而login把user装进去完事
[10:56] 他们这个Service-add-in-Controller写起来呢还是比较简单的好吧行那这个东路的接口啊咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
<Mapper namespace="com.heima.model.mappers.admin.AdUserMapper">
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
</Mapper>
```
画面5：
```
public interface UserLoginService {
    ResponseResult login(AdUser user);
}
```
画面6：
```
package com.heima.admin.Service.impl;
import com.heima.admin.Service.UserLoginService;
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
package com.heima.admin.Controller;
import com.heima.admin.Service.UserLoginService;
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

