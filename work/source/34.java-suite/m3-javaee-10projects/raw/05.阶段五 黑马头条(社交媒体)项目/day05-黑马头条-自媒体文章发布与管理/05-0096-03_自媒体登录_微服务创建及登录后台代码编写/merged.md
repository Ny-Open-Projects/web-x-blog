# 03_自媒体登录_微服务创建及登录后台代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\03_自媒体登录_微服务创建及登录后台代码编写【海量资源尽在 666java.com】.mp4
- 时长 19分41秒（音频 1181s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成当前登录模块的开发在开发之前呢咱们还得先去创建一个模块这模块呢是叫Media就是Media咱们当前的一个微服务那这样咱们先去来把这个模块给创建一下当前的工程中去创建一下当前的这个微服务就见呢在这干嘛模块是吧下一步点进去好复备一下啊然后下一步这个替换一下
[00:30] 好那这模块就出来了啊他这忽略了把它给取消忽略啊好了啊这个模块已经创建完了就他这时候呢咱们就干嘛呢就把这个配置文件给拷过来啊那这里边说了咱们需要这三个配置文件是吧那这三个配置文件呢其实呢咱们在可以参考之前其他的这种微服务去拷贝过来就可以了啊拷贝过来之后呢下面还有两个配置文件啊就是说
[01:05] 你在当前的这个resource下边有两个一个是application properties另外一个是当前的日志啊所以说你也直接考到当前resource下边然后呢在这改一改啊这叫啥呢媒体是吧也改了啊这个我就不再看了啊这个在comment中在comment中的配置文件中已经定义了啊这里边分别是他自己的端口号和他的应用名称是吧那行那这个考完之后呢怎么还有啥呢
[01:35] 其实还有一些东西咱们需要拷贝啊就是当前呢它有一些依赖信息这依赖你也参考其他的微服务就可以了拷贝拷贝完之后直接拷到这然后下面咱们就可以去创建当前微服务的什么引导类咱们在这啊先去创建一个包奥姆点黑马是吧然后呢咱们在这直接去创建了啊对这是个包是吧在这个包下边去创建一个类
[02:10] 就是咱们的一个引导类啊叫MediaApplication好然后呢在上面加个注解叫什么叫SpringBootApplication是吧然后下面是一个卖方法然后怎么着SpringApplicationRun然后是当前的MediaData然后是阿克斯那这样的话引导类就算传讲完了啊
[02:41] 创建完之后呢咱们在这顺便顺便在这把这个包给它补全对吧然后上面什么config然后下面还有什么还有Service还有Controller对吧v1然后是加了版本号那这个就算是做完了做完之后呢这块还有个东西就是咱们需要去分别去配置当前这三块内容第一个是mycircle第二个是dixon第三个是servet
[03:13] 咱们现在就需要去在当前的微服务的配置config中去把它加进来首先加一个叫什么其实也可以这样你也可以从其他的服务中直接拷贝过来因为都差不多比如在行为这一块直接拷一下就可以了比如说是有一个init有一个mycircleprokeeper咱们现在先不用应该是会用到咱们先不用也行用到的时候咱们再说先把这两个拷过来还没地儿
[03:49] 好跑过来之后呢咱们再看一看啊这是initinit的话其实就是jax那个东西啊还有mycircleconfig就是mycircle的一些扫描是吧还有整合买卖地址的其实都在这里边然后还有一个啊就是security那这个security啊咱们来看一下当前comment下边就咱们之前的在其他模块东西引入过你用户登录之后呢咱们需要去放到哪啊去那个把用户啊去做一下过滤是吧
[04:19] 检验我检验Token或者说你检验你的检验你的签名咱们之前用过的是APP下面的咱们现在是用WMWM包下面的这两个类其实两个类差不多功能是一样的只是每一个端不一样比如这是admin这是APP这是web meeting好吧行咱们下面就来去引用一下引用的话在这怎么引用在这去创建一个类是吧叫什么来着叫SERVICESECU
[04:51] 然后这块是一个什么这个complication然后呢是server lightcompany这个一定要注意啊这是server light因为这里边那边扫描的最终呢是一个这种啊算是过滤器啊比如说在这写com.hema然后什么web是吧common commonweb点什么wm.se
[05:21] 完了其实就是扫描到具体的模块下边的包可以了好吧那行那这个配置啊咱们就算是做完了啊做完之后呢咱们下面呢就来去完成当前的登录啊就是咱们先去完成后台一会咱们再去说前台好吧这里边做登录的话呢其实咱们这块内容呢只是需要去做一个非常简单的登录只需要去通过用户名和密码去验证就可以了
[05:49] 首先这里边涉及到一个表就是WMUserWebMedia然后这里边是有一个这种类这个表你可以打开这个表这个表就是谁就是他这个表你可以这样看可以看到当前的他的一个这种字段字段的话其实咱们目前的话也不用关注那么多登录功能咱们之前做过很多
[06:16] 所以说咱们只是做一个非常简单的动作功能就可以了通过当前用户名和密码进行动作就可以了好吧嗯行那这是他的一个参数啊他返回的内容你要大家注意啊返回的是首先是一个talking这talking怎么拿还知道吗这talking是不是通过JWT去根据用户去生成一个什么字符串是吧最终把用户信息给返回就可以了好吧要返回两部分啊第一个是talking第二个是user好吧行那这个啊
[06:44] 咱们下面就来去写当前的这种麦普念啊这是他的一个实体类啊实体类大家也可以看一看啊现在我们现在目前不用关注那么多啊咱们只需要去关注当前的用户名和密码就可以了都是一个死论好吧咱们也不进行去加密了啊只是做一个明文只是为了能够拿到当前的一个token信息而已好吧好往下看啊然后下面呢首先呢咱们在这去创建一个当前的什么呃这种
[07:14] 这个接口的话咱们还是老套路开当前的model这接口里边其实就只是一个啥呢只是根据当前用户名去查询某一个用户打开当前的mypres之前咱们一直在app这个包下边去创建现在咱们要换了叫vmedia我们到这个里边去创建前的mypres文件好吧
[07:42] 因为它这个是Media啊就功能它的模块不一样所以说大家一定要区分然后这就是根据当前的名称去查找某一个用户好吧行那这个咱们创建完之后还要在这去创建啥拷贝一个出来啊到当前的Media然后下载去创建当前一个Map文件然后前面都给它删了WMU4Map然后呢把内容给它删了创完之后呢这个APP这个包也要
[08:14] 然后是wm.yme.然后下面是点好吧然后下面咱们就来去写写的话其实也很简单就是根据当前用户名去查询某一个用户好咱们还是老套路直接考过来考过来之后你看这个咱们其实用了那么多但是也加上比如说这一块是它的一个映射是吧然后下面是一个circle的片段然后
[08:45] 下面这个呢下面这个就是根据当前用户名去查询就可以了啊他只能查询了一个啊当然你也可以去做一个这种约束啊那现在没有做约束也没有没有问题啊咱们只查询了一个就可以了保证他不报错可以了因为最终当前这个方法干嘛这里边只是查询到一个用户是吧查询到一个用户啊行那这个咱们下面就往下去写下面咱们去写Service好吧这Service的话呢咱们就在这啊在这写在当前的
[09:13] 没地点下面去创建用这个包啊咱们已经创建完了在这去创建一个这个接口啊叫什么来着咱们可以叫user login Service啊userlogin Service哇这创建完之后呢这里边有个方法是吧然后是public response是吧还是知道没忘吧response里到他然后下面怎么着我们只写一个方法叫login好吧然后你需要给我传
[09:47] 穿啥呢WMUser当前的用户对象用户里边包含了包含了用户名和密码好吧那这穿进来之后啊咱们就下面就来去实现目前这个是前面加一个包啊叫impl然后是下面是加了impl啊是一个实现类好让他去实现目前的user login Service
[10:18] 好了啊这个方法就实现了实现完之后啊咱们在这儿就直接去写一个Service好在这防止暴速再加一个什么什么为了干嘛干嘛呀这是是不是为了防止警告出现警告啊好了啊那这个说完之后呢咱们下面就来去写代码去完成首先呢在这里边啊先去拿到谁呀你拿到他的用户名和密码所以说咱们在这儿啊先去判断啊七手式都是判断大家一定要注意啊首先呢咱们在这儿啊
[10:49] 如果说他未空如果说他俩都未空的话呢你们这手啊那就不行了啊应该是
[11:19] 往下走啊应该是这两个哪个不能为空啊咱们直接返回就可以了好吧这是什么 response without error然后这边咱们可以说一个啊你的参数啊有问题啊这有问题咱们当然了也可以去提醒一句话说啥呢说啊你的用户名号密码不能为空用户名或密码不能为空
[11:49] 那这个咱们就说完了啊如果说他不为空的话呢咱们就现在呢就可以去查了啊首先呢咱们在这要要去查的话呢你得先去干嘛呢先去注入当前的mypro是吧打开然后是下面private wmu user mypro注入进来之后啊咱们在这就可以直接去调用以前那个方法了啊.slack的byname就是user.get好这是他最终返回当前的一个项目
[12:21] 就像的话咱们在这先去判断如果说wmuser等于等于不等于那不等于那的话咱们再往下走再往下走但如果说等于那怎么办等于那的话咱们直接还可以再去返回好这一块咱们应该是有一个叫做用户不存在的一个东西我看看这里边是稍等找一找Log有没有
[13:02] it notit not exist是吧说数据不存在是吧因为这个数据当前的用户没查找过那就数据不存在呗是吧也可以提示当前的什么什么不存在呀就是用户名不存在用户不存在好吧那这是一个啊下面这个啊如果说它不为空的话咱们它就会走到这走到这要干嘛呢这咱们首先呢要去判断当前密码到底是否一样是吧怎么判断呢ifif啥呢首先是user的
[13:34] get password,recos,recos谁呀,是wmuser,reget password,你看啊,这个呢是从前台传过来的,前面这个是从前台传过来的啊,后面这个呢是从数据库中查出来的,如果说他俩一致的话呢,那这事就好办了,如果说不一致的话,那就不行啊,所以说咱们在这啊,还得去,还得去往下去写,这时候啊,咱们如果说他两个啊,一样的话,怎么办呢?
[14:04] 再写一个它一样的话咱们就正常去保存返回就可以了不一样我们再去做一个密码错误就可以了好吧这咱们就说啥呢说当前的密码错误啊logpassword error好吧这是密码错误然后最重要的代码是在这啊在这啊这都已经没问题了说运动户查到了啊你的密码也都也都能追应上那这时候呢咱们需要去返回了那返回啥呢
[14:36] 咱们刚才说了啊这个返回的话呢其实就是反过来看啊咱先说结束啊说一个token和一个user是吧token跟user啊好那这个时候呢咱们就来去把这东西给返回那这个是一个map啊所以说咱们在这啊先去创建一个mapmap然后第一个呢是street啊第二是object好吧别说了啊object然后最终呢咱们是叫redo的好吧renew一个hashi map好
[15:11] 然后呢然后咱们就往里边去填数据就可以了啊比如说卖啊 result啊result点root第一个呢是token啊token的话是怎么写啊token的话是不是有一个app jwtqt点啊叫get token然后你需要去传一个用户进去wm user啊wmok那这样的话这样的话就生成了一个块啊还有一个result点什么
[15:44] 还要去把当前用户信息装进去啊WMU4最终呢咱们就可以直接去返回了return response withoutOKOK就是把当前这个result返回完事了那行啊那这块内容呢咱们就算是做完了那做完之后啊这边还有一个东西就是你在这啊需要去清空一些东西因为最终你不能把用户的所有信息都返回到前台是吧这时候怎么办呢
[16:13] 在返回之前,你应该wmuser.setpassword里面应该设置完之前是不是设置为空我给它把这个密码清空这就是wmuser.setset有个言言的话咱们也应该把它给清空目前的话这个表这里边就简单说一说你看这个表里边有一个叫做set言是吧,号一个密码
[16:42] 还有个密码啊这个密码是怎么来的呢其实密码的话如果说你要加MD5的话呢用MD5创建之后呢咱们通过延再去给它算一下最终这个密码是需要加延之后的密码所以说呢你要去解密的话呢你也要去通过这个延啊所以说咱们把这个延呢也干嘛呢也给它清空好吧也清空啊行那这个啊咱们就算是Service就算是写完了啊那顺便呢就把当前的啥写写啊这水晶档你给它删了啊那顺便就把当前的
[17:11] 也写写啊先关掉嗯关了一下啊啊在这啊你在这去创建啊在这去创建什么的创建一个接口啊嗯login嗯咱们在哪创建呢我看看啊还是到media啊咱们在这创建一个包先创建一个包啊叫什么一个media好吧行然后下面呢就在这就在这里边呢去创建一个接口logincontroller
[17:46] api好吧然后它是一个接口然后在这直接写一个方法就可以了是动用方法response without然后是login然后下面是有个wmu user然后下面咱们就来去实现当前这个接口还是到到当前的measur在这个Controller下边去创建一个类把这api去掉让它去实现
[18:21] 这个接口好这是加什么东西啊首先加一个rest Controller然后是加request my ping是吧前面这个咋写咱们又再说啊下面咱们要去调用啊不能调用的private然后是前面一个loginloginservice哎卖了我看看啊user login是吧user login Service就叫它吧好吧
[18:56] 然后下完呃这个说完之后你在这可以不用想然后是login把当前的user传进去完了啊那下面咱们要补全啊那这个补全的话咱们就参考笔记去写啊因为这个跟咱们之前好像不太一样啊呃找到当前的Controller啊嗯这是吧怎么还先这么写啊又不是看前台怎么写啊先这么写有时候有问题的话咱们可以再调好吧这啊这块是一个request买品login好吧
[19:30] 行一会咱们再聊好吧行这个目前的话咱们就先写到这啊对于测试的话咱们一会集成前端之后一块测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的用户登录功能的开发过程，包括项目结构、配置文件、数据库表设计、Mapper 接口、Service 实现和 Controller 控制器的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开 IntelliJ IDEA，显示项目结构，当前选中 pom.xml。
画面 2: 打开 application.properties 文件，显示配置项 server.port=3(port.media) 和 spring.application.name=3(sn.media)。
画面 3: 打开 MediaApplication.java，展示 Spring Boot 启动类，光标在 main 方法中。
画面 4: 打开 IntConfig.java 文件，展示 @Configuration 注解和 @ComponentScan 注解。
画面 5: 打开 Navicat for MySQL，显示数据库表结构，正在编写 CREATE TABLE `wm_user` 语句。
画面 6: 在 IDEA 中，弹出复制文件对话框，准备复制文件到 mappers 目录。
画面 7: 在 IDEA 中，右键点击项目目录，弹出创建新文件的菜单。
画面 8: 打开 UserLoginServiceImpl.java，正在编写 login 方法，光标在 if (StringUtils.isEmpty(user.getUserName())) 判断语句。
画面 9: 在 UserLoginServiceImpl.java 中，光标在 wuUserMapper.selectByName(user.getUserName()) 方法调用处。
画面 10: 在 UserLoginServiceImpl.java 中，光标在 if (user.getPassword().equals(wuUser.getPassword())) 判断语句。
画面 11: 在 UserLoginServiceImpl.java 中，光标在 result.put("token", JwtUtil.getToken()) 语句。
画面 12: 打开 UserLoginService.java 接口文件，定义 login 方法。
画面 13: 打开 LoginControllerApi.java，展示 @RestController 和 @RequestMapping 注解。
画面 14: 打开 LoginController.java，展示 @RestController、@RequestMapping("/api/v1/media") 和 login 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
server.port=3(port.media)
spring.application.name=3(sn.media)

画面 3:
package com.heima.media;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MediaApplication {
    public static void main(String[] args) {
        SpringApplication.run(MediaApplication.class, args);
    }
}

画面 4:
package com.heima.media.config;
import ...
@Configuration
@ComponentScan("com.heima.login.common.init")
public class IntConfig {

}

画面 5:
CREATE TABLE `wm_user` (
  id int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  ap_author_id int(11) DEFAULT NULL,
  name varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '登录用户名',
  password varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '登录密码',
  nickname varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '昵称',
  image varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '头像',
  phone varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号',
  email varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '邮箱',
  score tinyint(3) unsigned DEFAULT NULL COMMENT '积分',
  login_time datetime DEFAULT NULL COMMENT '登录时间',
  status tinyint(1) DEFAULT '1' COMMENT '状态',
  create_time datetime DEFAULT NULL COMMENT '创建时间',
  update_time datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_user_name` (`name`),
  KEY `idx_user_email` (`email`),
  KEY `idx_user_phone` (`phone`),
  KEY `idx_user_password` (`password`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),

