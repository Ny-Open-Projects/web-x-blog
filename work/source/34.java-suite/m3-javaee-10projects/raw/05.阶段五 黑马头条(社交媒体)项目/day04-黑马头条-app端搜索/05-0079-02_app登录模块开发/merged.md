# 02_app登录模块开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\02_app登录模块开发【海量资源尽在 666java.com】.mp4
- 时长 16分57秒（音频 1017s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们首先呢来完成一个登录的接口开发那这个登录接口呢咱们还要再去创建一个微服务啊这个是关专门用来进行登录的一个微服务好吧专门用来APP登录的一个微服务啊这样说啊那行那这个呢咱们做呃先看一下这个这个接口定义吧好吧一会咱们再去创建的工程啊然后这个接口呢主要呢就是呃这么一个路径是吧啊这是路径啊然后下面呢他有个请求的DTO
[00:28] DTU的话呢就是AP user因为这里边啊他一般会输入啥呢输入用户名号密码是吧输入用户名号密码啊然后呢去验证啊验证就可以了验证完之后呢咱们需要去响应响应啥呢响应一个token那这个token的话其实就是一个JWT的字符串然后还有用户信息那还有用户信息行那这个呢其实就是接口的定义好了啊那首先呢咱们先去干嘛呢先去创建当前这个微服务
[00:56] 来拷贝一下他这会写了就是能靠其他微服务去创建就可以了这个对于大家来说应该是很容易了直接创建的模块然后下一步拷进来提换一下点finish好稍等微服务其实就创建完了咱们可以检查一下这一块有没有这块是不是加进来了加进来之后你可以在这再去看一下当前login是不是也加进来了没问题
[01:24] 那加进来之后呢咱们就可以参考着其他的模块去创建比如说咱们随便创随便找一个就找这个比开尔吧把当前的配置文件是不是考过来好嗯然后呢然后是两个呃两个配置文件是为sauce下边两个配置文件一个是vk的跑跑历史一个是关于日志的啊好也考到这考到这之后呢你需要去改掉东西啊这个呢其实就不是比开尔的是谁啊这是login
[01:57] 下面这个也是老爷啊那个改完之后啊下面还有些东西需要去加进来比如说当前的一些依赖信息因为他呢也需要去查询数据库所以说基本上的依赖啊都要去有你直接去参考其他的服务去考过来就可以啊比如说咱们去参考当前的行为服务啊去拿过来好那考过来之后啊这个模块啊就算是创建完了是比较简单的对吧咱们在这儿去定一个包吧好吧
[02:34] 创建完那个包啊这个包的话咱们什么黑马然后是模块名是吧OK啊然后在这呢去创建一个引导类是咱们最基础的步骤啊叫login啊对错了是吧这不是叫user啊叫login啊login啊改完之后啊这啊嗯改完之后呢咱们在这直接去创建一个引导类loginapplication
[03:14] 然后是写当前的svm是吧然后是sbrmapplication.run然后是当前的login然后是x然后下面是还有什么东西有一个sbrmbootapplication是吧行那咱们的环境算是搭完了搭完之后咱们就继续下面咱们就继续编写这个接口咱们还是老套路
[03:44] 首先呢咱们还是要去编写当前的一个MIPRO文件这个MIPRO文件非常简单就是通过当前一个用户名称其实用户名称就是手机号啊因为APP一般都是手机号去登录所以说咱们就先根据当前手机号去查询就可以了好了非常简单那咱们先去找到当前这个MIPRO这个MIPRO其实咱们之前定义过所以说用户名称去创建了啊找一下什么AP user MIPRO
[04:13] 好吧你在这啊这已经有了一个是吧我看那就拷贝下啊是你从这跑过来就可以下面还有这东西是吧这东西你就拷一下完之后呢直接站到这就可以了啊因为他这个呢就是基于当前一个国际号去查询并且是查询异常数据对吧没问题啊行那这个做完之后呢咱们下面呢就来去写他的Service这个Service其实就是一个验证的过程是吧好那咱们就来写一下啊
[04:41] 首先呢在当前的login里边去创建一些包啊这个包的话咱们一块去创建完吧首先创建个Service然后再去创建什么config是吧然后再去创建一个啊control r v1是吧一样那行那这个咱们写Service之前呢这个少一步啊在这你应该去先去嗯处理化一些东西啊咱们叫什么my circle吧用他们小茶库啊my circle config那他呢是怎么写
[05:17] 这个configuration是吧然后是compound scan这个不是哪个包还记得吗com.黑马common my circle行那这个就扫描完了扫描完之后咱们就来去写这个Service这个Service咱们就叫做啥呢它是个介绍什么叫做AP读语AP开头AP user login Service好吧行
[05:49] 先拷贝一下它然后点ok然后呢咱们就写前面的逻辑这个逻辑的话其实非常简单就是根据用户名和密码登录验证是吧登录验证这个方法怎么写统一还是返回什么response result然后是写个loginauthor好吧就这么写啊参数是啥呢参数参数在咱们这是不是已经有了
[06:21] 是不是这种参数啊他会传过来一个ap user对吧就在这写ap user我们就写一个叫user吧好吧user好了啊那这样的话咱们Service就写完了Service写完之后呢咱们就来写他的一个这种实现啊在这去加一个他impl好背不对是吧行吧ap user login Service mpl
[06:53] 它是一个类然后是实现当前的apuserlogisservice好,ctrl i一下这时候咱们在这去加一个助解叫Service这里边该去写啥首先你要干第一个事就是先把这种mypro给输入进来是吧privateapusermyproapusermypro防止不好看是吧加个superwarning
[07:26] 那这个时候那里边的业务是啥呢首先呢你第一步永远都是第一步他要根据当前用户名号密码去判断是吧所以说你首先呢应该先去根据当前的这种参数进行验证咱们先做一个验证参数验证参数其实你两个都要验证首先第一个就是优色点他们需要去通过手机号去查询
[07:57] 说咱们咱们呢可以用一个工具类去接业证呃死u t u s r isample如果说他为空的话啊或者是是啥呢或者是当前第二个u t u s risample然后呢这个是password是user.getpassword他两个有另一个为空咱们都去返回就可以了啊回啥呢反过错误呗
[08:28] 这里边是有一个值叫参数有问题是吧就他啊猜数哎有问题啊那行那这个参数没有问题咱们再往下看啊这时候如果说没问题的话呢咱们就可以去查询了查啥呢就是查询当前用户其实咱们已经写好了当前的一个麦普是吧所以说你在这你看啊点什么slack的i就是根据当前的手机号直接就是
[08:57] user.get当然他有可能是不是没查找完全有可能如果说没查找怎么办没查找就不行cp user等一等一当的话直接返回就可以了这时候你肯定是错的说一个用户不存在就可以了raisebondswithout.irror然后是app这里边应该是有一个叫做
[09:31] 点AP user用户的什么数据不存在是吧咱们可以返回给他然后再往下看啊当然了这个用户如果说查着了这时候还要再去验证一下什么密码啊这密码的话那怎么去判断呢其实就是目前你传过来的这个密码和你查了的密码是一样的话那就说明成功了对吧
[09:59] 所以说咱们在这去判断一下怎么判断如果说user.getpassword.egos是谁呢egos就是前的apuser.getpassword它俩是一样的话怎么着那不一样的话咱们就不行是吧直接如果说不一样一样密码肯定错了然后就是什么respawns还是反过来的错误error result然后里边咱们有一个
[10:30] 应该是登录的错误啊找一找啊app他然后三了而login密码错误是吧是有密码错误的啊比如说咱们直接提示密码错误就可以啊然后呢咱们如果说这一步没问题这一步也没问题啊那这时候那就登录成功了啊登录成功之后呢咱们就可以去返回那返回啥呢来看一下啊返回的是response里面装的是一个对象对象里边有个
[10:59] token 和一个 userok 那 token 怎么拿呢去 token 的话咱们就用 dwt 去做就可以了啊嗯去生成就可以来看一下啊首先呢咱们在这先去用什么卖卖子轮 object object 宝宝我们叫卖婆吧无所谓啊用一个哈西卖婆然后呢然后咱们在里边去卖婆点 put
[11:30] 或者啥呢第一个呢其实就是谁呀就是talk啊talk啊然后第二个是啥咱们呃第一个咱们用的说啊卖破点put这个啥呢第二个是useruser很好很好理解就是你查出来的这个user叫apuser是吧这talk怎么拿呢talk呢其实咱们在咱们前第一天导入当前项目的时候在youtube4里边呢已经有了一个工具类好打开这工具里啊叫他叫app
[12:00] DWT YouTube这里边其实有两个方法第一个是要叫什么来着找找叫get tokenget tokenget token其实你就可以去传过来一个你可以传过来一个AP user然后他就可以给你当前用户的信息去生成一个给你返回一个主券这个其实就token怎么在这直接写叫什么叫APP
[12:32] AWT点什么那getok传的是apuser就是ap最终咱们可以直接返回了那就是wisbonc.ok然后这里边就是当前的map没问题吧这里边还要注意一个事这里边是也不含了密码对不对这里边是不是也不含了密码
[13:00] 你再把命名给发明文反过来是不是不太好啊因为咱们这边并没有加密是吧所以说咱们在这啊密码一都不反啊一般都不反所以说user.setpassword然后是这个空啊是这个空啊就是为了安全性所以说咱们在这啊专门是这个空然后说我们空之后呢再去返回就可以了好吧行那这里边呢咱们就算是设置完了啊行那这个Service写完了就继续写当前的Controller好吧
[13:29] Ctrl也很好写啊打开当前的login那这时候呢你首先写Ctrl之前的你先去干嘛呢先去在这啊去创建一个什么接口是吧登录了接口啊这有个login是吧user relationlogin有了是吧那有的话那咱们就不用再去重新创建了啊直接在这去写就可以了这个login的它好像不太合适是吧这个部分咱们改了吧好吧改了啊
[14:02] 怎么改成当前的user好吧这是user啊好然后再去创建一个login啊login应该有了怎么在这再去创建一个包叫什么appis点什么logincontrollerapi好吧好了有了啊那这个user的话还是user啊user比方管还是之前的login是login啊loginlogin不一样啊行那在在这呢这里边就
[14:37] 就有一个中的方法直接用response然后下面是login好吧就叫login吧login方法名叫啥就无所谓啊这咱们是有一个路径是吧他们的一个呃参数就是vp user吧vp useruser完了哦对这是一个inface啊错了啊那这样的话咱们就算是定义完了啊用完之后呢咱们在这啊去创建一个Controller啊
[15:11] 叫什么login让他去实现刚才那个接口logincontrollerapi就他没问题行这去加一个什么restcontroller加一个requestmyping然后这里边怎么写api然后是ve然后什么login没问题吧下面咱们再去写
[15:44] 这里边咱们还要去写一个post mapping这里边咱们又写一个叫loginlogin author然后aut也是完了说完之后咱们在这儿还是再去加一个叫什么request bodyrequest body加完之后咱们就可以调用方法了这个方法的话咱们需要去注入当前的Service这个Service叫什么applogin
[16:20] 有吗我叫什么叫PP userlogin sorrystop了然后扎进来之后呢咱们再去注入啊注入之后呢咱们就可以调用然后是点log给他然后是把当前的user传进去就完事了好吧那这个咱们就算是看完了啊那看完之后啊咱们这个测试啊就先不测了啊
[16:47] 到后期咱们会一会儿一会儿去集成前端的时候咱们再去测好吧行那这个当前登录的接口咱们就先说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import com.heima.login.Service.ApUserLoginService;
import com.heima.model.common.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ApUserLoginServiceImpl implements ApUserLoginService {

画面8：
import com.heima.login.Service.ApUserLoginService;
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
import com.heima.login.Service.ApUserLoginService;
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
import com.heima.login.Service.ApUserLoginService;
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
package com.heima.login.Controller.v1;
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

