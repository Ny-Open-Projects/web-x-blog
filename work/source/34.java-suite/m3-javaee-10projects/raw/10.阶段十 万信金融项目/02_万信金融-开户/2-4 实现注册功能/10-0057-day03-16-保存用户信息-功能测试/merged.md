# day03-16-保存用户信息-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-16-保存用户信息-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 15分13秒（音频 914s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好到目前为止呢我们的注册功能就全部实现了大家看一下讲义的目录这个目录呢我们整体的看的话还是很清晰的注册咱当时是不是拆分成三个小功能了吗第一个呢就是实现发送短信验证码第二个呢就是校验手机号和验证码第三个就是咱刚实现的保存账号用户信息对不对这里边涉及到两个微服务还涉及到他们之间的远程请求远程调用对吧
[00:31] 那总之吧目前咱们注册这个功能全部实现了实现了之后呢咱还是像以前一样我们要进行功能测试那这里呢我就只通过Postman进行测试那么另外呢大家在测试这个注册功能的时候一定要注意啊我们只有用户不存在的情况下或者说是新用户或者说这个手机号在表里边不存在的情况下你才能正常的看到这个注册的功能
[01:01] 当然了你要是挑一个手机号已经存在的这个用户去测试的话他应该会抛异常啊根据咱写的这个代码会抛这个异常说这些细节呢大家需要注意那咱接下来呢就进行测试了咱测试的时候呢我们以前跟大家说过每次测试呢你都得先想一想我都需要启动哪些服务对不对这里边的话你看看都需要启动啥Apollo一定要启动是不是还有什么呀
[01:31] 那个短信呢那个服务还有redis目前不需要启动因为咱只是测试注册的话暂时用不到它那就是IDL里面这几个微服都要启动对吧服务注册中心啊Account啊Consumer啊Gateway啊等等等等这个事呢你以后要养成习惯一说测试我得先捋捋对不对哪些都是需要启动的先把这些都启动过那我这呢时间关系提前都已经启动好了
[01:59] 我们可以把控制台都给他们给清一下一会儿一旦出问题的话我们便于观察那咱就打开Postman进行测试了我们在哪测试那咱看看咱之前打开的那个图吧之前的那个图就是这个注册登录流程图你看咱现在是通过Postman把它出单位前端发起什么样注册请求先到哪先到
[02:34] 用户中心啊然后再发起远程请求到哪统一账户然后再返回注册结果到Postman对吧所以说呢我们这个发了请求首先是到什么呀用户中心所以说Postman里边咱应该是在用户中心这个集合里边是不是新增一个请求来完成这个注册功能的一个测试那我在这呢就直接new了new一个request是吧呃这个呢就叫注册吧
[03:07] 注册对然后呢我们把它放到归类为什么呀对用户中心好注册就有了然后接下来我们补充一下这些信息这些信息呢你得参考我们的Controller请求是往这发吧对不对走这啊那你看它是什么请求啊post请求这儿改一下啊请求地址是这儿对吧呃那它前面的东西咱需要补充一下http
[03:42] 冒号杠杠是吧这个用户中心的端口号是多少没记住的话没关系我们查一下这个启动参数就行了用户中心应该是53050好这样呢我要加上端口号53050然后再进来是不是有consumer这个基本的访问路径是吧con sumer对
[04:14] 这样子的话咱基本上就把这个路径给他写出来写完之后呢还得再观察一下啊你看我们往这发请求的时候是不是要传数据啊而且你看我这加的有request body 注解这意味着什么这意味着往这发请求的时候传过来的应该是什么格式的数据啊json嘛对不对json这个大家都知道啊那在postman当中如何传递json数据呢大家注意看应该选择bodybody
[04:46] Body里边呢点击哪儿啊AW啊点击AW然后这儿选择什么呀Jason对一定要注意我刚才都点了什么地方啊要注意观察那我们都给他传什么数据呢那这就要看这个实体类了对不对就DTO这个类啊这里边当然他的属性非常多了用户名啊手机号密码啊等等等等那我们这儿呢只需要给他提供一个手机号就OK了就是Mobile其他信息咱暂时不给
[05:16] 因为有些信息是不咱在代码里边给他提供了一些默认处理值嘛对不对我这呢我们只给一个目标就行了呃那回到postman当中咱需要自己造一个json格式的数据啊只需要传给他一个什么呀目标这个值就是你自己给的了对不对我们就给一个不存在的一个手机号呃你最好看一下你的表啊consumer
[05:46] 还好吧consumer目前是空的aconda呢呃我的aconda里面有一条数据手机号是这个手机号反正你要看你的数据库咱们的数据库表里边数据可能不一样啊你得看一看呃那这样吧我就造一个完全不存在的手机号呗15378791912吧这个手机号是不存在你看他是1911嘛对不对consumer完全是一个空的了是不是所以说呢
[06:16] 这个手机号是不存在的手机号也就意味着这个用户是不存在的对不对这个时候我们如果咱代码没问题的话那就正常的进行了什么注册那咱接下来直接就点击什么呀send来进行测试走好咱看下返回的结果没有报错返回0返回0的话意味着什么呀对我们以前说0就表示什么呀成功0就表示成功
[06:47] 到底有没有成功呢那你是不是去表里边瞅一眼就行了对不对刷新能问题吧你看这是那个1912那个手机号码这个user内幕包括这个user number大家有印象吗这些值的怎么产生的呀这些值咱当时是不是在诱惑藏咱们自己手动付的一些出入值是不是你看在这儿这个内幕user number好这个是否绑定银行卡默认值是零吗咱看有没有有吧对不对
[07:18] 至于其他的这个值呢咱暂时用不着先不用管了后边用到时候再说那咱还要看哪大家别忘了我们的concern是否会远程掉了看他对不对看他这里边有没有保存数据有没有有吧这是不是呢1912吗对不对这是他加密后的那个密码嘛C端用户对不对这是他自动生成的ID咱不用管了你看这个信息基本上是没有啥问题
[07:50] user name这个user name是空的我们来想一想这个user nameuser name是不是应该是来自于consumer这里边的user name咱这儿是不是少传过去一个东西是不是其他功能都是正常了那就是我们alcana这边保存的时候这儿是为空user name为空所以说呢这儿有个小bug咱需要检查检查那咱先看一看远程调用的时候
[08:17] 咱是不是给他传过去一个DTO对象是不是没事这个DTO对象我们得检查检查这里边有没有user name这里边应该是有的吧因为咱上面这是不是刚给他设置过什么呀user name这里边有个小问题你看好了这个代码你看好了这个代码咱是不是把consumer register DTO里边属性量值是不是存到这里边了
[08:46] 而consumerregisterdto这里边你看这里边注意了这里边他的user name是没有值因为咱是先复制然后再单独设置了是不是说这里边有一个bug有一个bug那这个也简单你可以这么做吗你可以这么做在这再加上一行conconsumerregisterdto对吧点set什么user
[09:20] 内然后呢从卡随梦当中吧他给取出来这样子的话在这在这做这个夸配操作的时候他里边的这个用的内部是就有值了吗然后给了这个啊上他锐杰斯的地球然后他呢就被远程扔给了什么呀我看到那边这个时候应该用的内部是不是应该就有值了对不对这是一个细节一个小大个吧
[09:48] 那咱这个既然改了一下咱就再测试一下对不对这是修改了哪个代码consumer对吧我们把consumer重启一下就行请你启动一下其他地方代码咱没有改没有改的话咱就不再管它了只启动一下consumer然后咱一会儿在postman当中再进行测试咱一会儿把手机号给它换成1913对不对就1913也是不存在咱测试一下就行了
[10:19] 咱现在就等待consumer启动完毕好应该是启动完毕了启动完毕之后呢咱接下来再做一次测试把它改成1913然后再send一下好接下来看结果0表示成功了对吧然后去表里边瞅一瞅先看看consumer这个边1913已经进来了对不对然后再看看看到这个边稍微新一下是不是也进来了而且这一次就的name是有值的对不对
[10:54] 这是正常的一种情况那咱接下来测试一个手机号已经存在了吧比如说那个其实现在13都已经存在了对不对那我现在是不是重新再点一下那按说应该看到啥应该看到咱当时是不是人工抛了一个那个异常是不是咱试一下哎他这边抛了一个500这不是咱想看到啊不是想看到那咱看看是是咱代码有问题还是咱看控制台抛了一个异常
[11:26] 这个异常是不是咱故意抛的吗对不对是咱故意抛的你看这是service41号那这应该是正常的情况你看因为现在这个1513这个手机号已经存在了所以说他这一查询发现这个手机号已经存在了存在的话是不是咱故意抛了这么一个异常这个异常不就是我们说的那个用户异存在吗是不是这是正常的但是但是是这样子的
[11:57] 就是你抛这个一长是正常的但是我希望返回给前端的不应该是500应该是什么呀应该是这个应该让前端看到的是这个信息那这呢我知道是哪的问题大家知道吗我希望前端返回过去的是就是返回前端的是这个信息而不是那个500那个不友好那这咱少做什么事了吗大家应该有印象我们前面在测试accompt里边是哪个功能的时候
[12:30] 是不是也是遇到这个问题啊咱当时少做什么事对我们少干了这么一件事还记得它吗这个东西这不是我们Sprite MAC里边进行全局异常补货的那个类吗有印象吗对我们现在就缺这个东西啊当时Account在测试功能的时候也是一样的嘛我们现在也缺这个东西啊所以我们现在需要把这个类给拷到咱们Consumer里边然后需要做一些修改
[13:02] 没有他的话咱抛到这个异常没有人捕获了嗯咱需要去consume more里边考到这个quantum里边考到这个quantum这个包里边粘过来粘过来之后呢我们应该是要做一些修改的我们整体过一下啊看哪些地方做需要做修改有没有这咱之前在account里边用过一次你整体需要过一遍代码有需要修改的吗没有任何需要进行修改直接就拿用了对吗看看啊
[13:38] 这是类名这是日志这是他要补货就是exe这个下面所有的子类这个异常这是他返回的那个格式json格式的对不对这里边的代码business咱抛的也是business嘛对不对然后应该是不需要做任何修改了那咱把这个加进来加进来之后呢这还是consumer发生了变动所以consumer我们仍然需要重新一下
[14:14] 重新一下之后呢我们接下来还是做这个测试但是我们希望看到的不是500而是看到这个什么样用户已存在这种提示信息比较友好一些的提示信息好咱等待这个consumer服务启动完毕已经启动完毕了启动完毕之后呢咱回到postman我们还是发这个请求手机号还是1913它已经是存在的手机号了好我们send了一下好我们再看
[14:47] 这次是不是就是我们期望返回的信息啊仍然是这个呃提示信息但是呢这次提示信息是非常友好的一个提示是咱自定义的到时候呢用户在前单就看到啊该用户已存在对不对这样就比较友好一些那咱关于注册这个功能整体的一个测试咱就到这了没有问题了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Postman 发起 HTTP 请求，结合 Spring Boot 服务和数据库操作，完成用户注册功能的前后端集成测试，并处理业务异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“4.7 前后端集成测试”章节，内容包含启动服务的注解配置和功能测试说明。
画面2：展示课程视频文件夹，列出 day03 相关视频文件。
画面3：展示开发环境，包含多个服务窗口（如 Postman、SQLyog、Redis Desktop Manager、ApolloPortal 等）。
画面4：在 Postman 中创建一个 POST 请求，目标地址为 http://localhost:33030/consumer/consumers。
画面5：在 SQLyog 中查看数据库表结构，当前未查询到数据。
画面6：在 SQLyog 中执行 SQL 查询语句，但未显示结果。
画面7：在 IDEA 中查看 ConsumerServiceImp.java 代码，展示用户注册逻辑。
画面8：在 IDEA 中查看控制台日志，显示服务启动过程。
画面9：在 IDEA 中查看控制台日志，显示服务启动后连接失败。
画面10：在 IDEA 中查看控制台日志，显示服务启动后抛出异常。
画面11：展示项目文件夹，包含多个 Java 文件。
画面12：在 IDEA 中查看 GlobalExceptionHandler.java 代码，展示异常处理逻辑。
画面13：在 IDEA 中查看控制台日志，显示服务启动后抛出异常。
画面14：在 Postman 中发送 POST 请求，请求体为 {"mobile": "1597801913"}，响应状态为 200 OK。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Bean
@CopyProperties(value = ConsumerRegisterDTO.class)
RestResponse<AccountDTO> restResponse = accountApiAgent
    .register(accountRegisterDTO);
if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getErrorCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
```
画面7：
```java
throw new BusinessException(ConsumerErrorCode.E_140107);
Consumer consumer = new Consumer();
BeanUtils.copyProperties(consumerRegisterDTO, consumer);
consumer.setUserName(consumerRegisterDTO.getUserName());
consumer.setMobile(consumerRegisterDTO.getMobile());
consumer.setIsCard(0);
save(consumer);
```
画面8：
```text
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Starting protocol handler [http://mic-33030]
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Client: account-Service instantiated
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Server: account-Service started
[INFO] [project.name] [110:SERVER_PORT] 2019-07-29 22:33:49,740 INFO [DirectDLog.java:133] - Server status: Server: 32.306.2.15:33030
```
画面12：
```java
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;
```
画面13：
```text
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
[ERROR] [project.name] [110:SERVER_PORT] 2019-07-29 22:37:36,124 AsyncAppender-AsyncAppender ERROR Unable to delete file C:\Users\apple\Desktop\wanning\day02\wanning_apollo\logs\project.log
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

