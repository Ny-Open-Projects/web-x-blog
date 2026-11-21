# 13-Shiro结合redis的统一会话管理：自定义会话管理器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\13-Shiro结合redis的统一会话管理：自定义会话管理器_【海量资源尽在 ubkz.com】.mp4
- 时长 12分4秒（音频 724s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们接下来就来看一下如何通过自定义绘画管理器的形式将我们的认证数据存到Redis服务器当中好了那我们这边呢先来看一下如果要想完成结合Redis的这么一个统一绘画管理的话我们的步骤是如何去做的那我们关注的步骤呢其实就是说第一个Session Manager如何自己去写
[00:29] 如何定义那如何去做或者我们如何去实现它好了那接下来在Session Manager当中它其实是通过Session DO完成对Redis数据库它一个访问的这么一个过程那接下来对Session DO而言我们不需要关注额外的代码我们要知道它的一个逻辑关系Session Manager管理着Session DOSession DO才是跟Redis进行操作那所以我们这边要知道
[00:54] 我们呢要想自定义我们的绘画管理如果现在是跟ready打交道所以我们要通过default web session manager来自己维护绘画那自己维护绘画的时候需要通过session do来实现对于ready的数据库的一个赃产改查那接下来你自定义session do的时候那注意需要指定ready的服务器它的一个接口它的一个请求的地址和它的端口信息
[01:20] 那在这边呢我个人电脑上呢已经安装好了Reddit这么一个服务那在这边呢我只需要打开它就可以了Reddit Server好了这是我本地的一个Reddit服务器那Reddit服务器已经启动成功了通过一个桌面的扣端工具我们来看一下好了这边呢这个桌面扣端工具呢比较简单这边呢Add New Connection填写上你的请求的路径名称OK其实就可以了
[01:49] 那我这边的Localhost我本集的打开来看Ready目前当中什么都没有好了这些准备的工作我们都准备好了之后接下来我们就可以编写代码把这个功能给它实现出来那编写代码实现功能首先呢就是说我们说过了对于这个里面呢可能有自己定义SessionDuo的这么一个操作那要跟Ready打交道那这些内容呢我们不需要自己去重复的去造轮子自己再去写这些重的代码
[02:18] 在网上有很多开源的一些组件咱们只需要用它写的这些坐标的一些用它写的这些jar 包里面的功能就可以了那我们这边借助的是一个叫做shareal-reddit这么一个开源组件那这个开源组件里面封装好了我们三神迪欧封装好了和reddit进行交互的这么一些代码操作那对于我而言直接把坐标引入到我的工程其实就可以了那我们打开碰文件一起来看一下碰文件
[02:47] 在这边我已经引入过来了就叫做share-redis好了第一件事坐标引入成功了把受影响的全部都关掉那接下来第二件事就是说我需要指定一下我redis服务器的地址在Springboard的程序当中可以打开配置文件在这边填写上redishost我的主机名我的端口默认6379
[03:09] OK那这些基本的准备工作咱们都已经搞定了那接下来我们关注的点剩下关注的点就两个方面那一个方面是什么呢注意第一个方面就是咱们自定义session manager那自定义session manager咱们怎么做注意就是default web session manager那怎么做呢很简单好了在这边呢右键创建一个类吧
[03:42] 把它放到sessionmanager这个包下就session这个包下好了那我叫做什么呢我叫做consume我自己写的c-u-s-t-o-mconsume sessionmanagerok好了那这个是我们自定义的manager那对于这个自定义manager如何去做注意很简单我们只需要去
[04:17] 叫做继承一个tens继承一个副类这个副类叫做什么default web session managerfault default web session manager注意别选错share提供的OK好了有的朋友就比较迷惑我们自定义这个session manager究竟它可以做什么样的功能那我需要跟各位解释一下咱们可以回到讲义一起看一下我们刚才这个案例的这个分析
[04:52] 那是这样的对于我们而言咱们的一个前五端分离的这么一个项目前端发送请求进行登录认证上面这个逻辑那认证成功之后我返回给前端的是不是就是一个参数叫做一个我们叫做token或者是我们的一个session id那拿着这个session id我们一般是不是把它可以放到请求投信息当中发送给我们的订单服务或者我们的企业为服务
[05:16] 那发送过来之后我们是不是通过这个session id得到你这个绘画session的整个存储的一些内容啊所以呢对于这个session id而言那从哪咱们这个绘画管理当中这个session id总经从哪得到那这个时候咱们就收到收到那对于session id默认默认他的share当中的绘画管理器是把它放到了cookie当中并且以g session id的形式进行命名
[05:46] 它是放到cookie当中那如果你是这个session id你放到请求里了那我们怎么办我们就需要去重写我们需要去继承这个default web session manager重写它的一个方法那指定你session id的获取方式指定session id的获取方式那么需要重写它的一个方法
[06:16] 好了这个方法呢我们一起来看一下override method这个方法呢叫做get session id好了get session id我们用的是第二个方法request以及responseok好了接下来这个代码呢我们应该如何去写呢其实比较简单其实比较简单咱们其实可以看一下它的基本的一个原代码的一个编写方式这是它的基本的它之前那个原代码我点进来的来点进来
[06:55] 这是它的一个基本的一个源代码get reference等等等等其实就可以按照人家这个逻辑来写那只不过呢我们这个session id你请求过来我们是不是把它放到了投信息当中啊投信息中具有我们叫做session id那我们这个请求头那这个请求头的名字叫什么呢我们之前说过叫做a o t h o r i z a t o also relation是它
[07:31] 那我们的请求头里就是它了那比如说你给我发送一个请求多写了一个请求头这个请求头里面写了你自己的session id那我们就想方设法的根据你的request得到你请求头里面的awesomeawesome recent信息得到里面的session id其实就可以了好了那我们应该如何去做注意很简单首先呢咱们可以获取一把id等于直接借助shareware提供的一个工具类web utils
[08:03] Sherlock提供的工具类Web Utils打点叫做ToHTTP注意这边得到的一个对象是Servlet Request它未必就是我们的HTTP Request所以这边我们需要做一个转化好了转化好了之后接着它提供了一个方法打点Get Header你请求头这个头叫什么名字注意我们之前有一个约定你发送过我请求的时候要加一个头信息这个头叫做Also Released
[08:33] 好了Ctrl C Ctrl V拿过来那这样一来就能够获取请求头中的数据那获取请求头的数据这个请求数据不就是我们刚才说过的你发送请求的session id吗那这个session id我们已经有了所以我这边可以做一个判断if叫做student utils打点is empty判断一下是否为空
[09:04] 各位别忘了如果是你第一次登录我们这个第一次使用这个系统那你这边它肯定是一个空啊那如果是空怎么办呢注意如果没有携带那怎么办我们可以生成你登录的时候不是没有吗那没有的时候给你生成一个那生成的时候那按照什么规则给你生成呢注意注意按照什么规则给你生成我可以调用复类里面的方法因为复类里面其实它有自己的逻辑它会帮你生成所以这个时候呢我就return
[09:43] super打点getsensoryid好了把我们这个request和response传递过去就可以了抱歉这边是点OK好了那接下来else也就是说你这玩意儿不为空那这玩意儿不为空那我们怎么办呢那很简单你这玩意儿不就代表的是你的sensoryid吗
[10:12] 那session id其实已经有了那接下来我们关注的点就是让它返回其实就可以那返回session id的时候需要各位注意啊就返回值session id的时候那需要各位注意其实在session当中呢其实在shadow当中还有一些基本的参数需要做一个简单的设定那这些设定是通过session.setattribute的形式来做的那设置的参数有什么注意我这边就不废话了我直接通过它的源码一起来找一下其实就可以
[10:48] 这个原码呢一共有这么三段第一个Ctrl Ccall过来Ctrl V第一个好了这边呢还有一个Ctrl C这边也call过来Ctrl V我简单的解释一下这个呢是对于Shared Session管理里面的一些参数的一些配置首先第一个就是说你这个ID是从哪获取到的来源是哪那对于我们而言这边呢是不是咱们放到了请求头里所以我这边把它定义成此由头Header
[11:21] 好了第二个值呢指的是你当前这个session id具体是什么你的session id究竟叫什么它的值是什么往里设置指的是三数好了第三个指的是你这个session id要不要验证处咱们就可以了当了这三句话是固定我们直接call过来其实就可以那接下来还有一个返回值return把id返回这样一来我们这个
[11:47] 绘画管理系Session Manager咱们就已经自定义结束了其实比较简单咱们关注的就是我们这个Session ID从哪获取那么获取的是从请求头里面获取的如果请求里面也要给它生成一个新的即可OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过自定义Shiro的SessionManager并结合Redis实现统一的会话管理。

2) 按时间顺序列出每张画面的要点：
画面1：展示Shiro结合Redis的统一会话管理架构图，说明身份认证、会话管理与Redis服务的关系。
画面2：展示项目目录，突出redis-server.exe文件，暗示Redis服务已准备就绪。
画面3：展示SessionManager与SessionDao的关系图，说明需要自定义SessionDao并配置Redis。
画面4：展示application.yml配置文件，包含数据库和Redis连接信息。
画面5：展示多个开发工具窗口，包括IDEA、Redis Desktop Manager、Postman等，用于演示环境。
画面6：展示CustomSessionManager类的创建，继承DefaultWebSessionManager。
画面7：展示CustomSessionManager类的初始代码结构。
画面8：展示DefaultWebSessionManager的源码，用于理解SessionId的生成逻辑。
画面9：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面10：展示Shiro的统一会话管理架构图，与画面1内容相同。
画面11：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面12：展示CustomSessionManager类中添加获取SessionId的逻辑。
画面13：展示DefaultWebSessionManager的源码，用于理解SessionId的生成逻辑。
画面14：展示CustomSessionManager类中添加获取SessionId的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
<dependency>
    <groupId>org.crazycake</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>

画面4：
server:
  port: 8081
spring:
  application:
    name: ihm-company #指定服务名
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/shiro_db?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  redis:
    host: 127.0.0.1
    port: 6379

画面6：
package cn.itcast.shiro.session;
import org.apache.shiro.web.session.DefaultWebSessionManager;

画面11：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

画面12：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

画面14：
protected String getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的Authorization
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        return super.getSessionId(request, response);
    } else {
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：标题“2.3 Shiro结合redis的统一会话管理”，架构图：前端请求 → 身份认证 → 认证中心 → 认证通过 → 会话管理 → 存储到redis；会话管理 → Redis服务。
画面3：标题“2.3.2 构建环境”，架构图：SessionManager → SessionDao → Redis。
画面10：标题“2.2 应用场景分析”，架构图：前端请求 → 身份认证 → 认证中心 → 认证通过 → 会话管理 → 存储到redis；会话管理 → Redis服务。

5) 不要评价画面美观，不要输出与课程无关的内容。

