# 19.统一增加缓存逻辑的实现（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\19.统一增加缓存逻辑的实现（上）_【海量资源尽在 666java.com】.mp4
- 时长 12分16秒（音频 736s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下缓存就是前面的我们其实开发了有两个这样的一个接口那么我们其实都需要对接口的数据呢其实做缓存因为我们不能每一次都去访问我们的数据库或者说去访问我们的mongoDB那么我们要把一些数据呢去做一些缓存这样的话可以提升我们整个系统的这样的一个响应和性能
[00:26] 所以说我们缓存是必须要去做的一件事情但是我们在做的时候其实我们会有两种做法那么第一种实现的就是我们在每一个接口中就去单独控制缓存逻辑这一种玩法那么另外一种玩法是我们统一的去写缓存的逻辑那么就是说我们不需要在每一个接口中去写缓存逻辑了
[00:55] 统一去做一个管理起来那么这两种方案大家可以思考一下那么如果是你选择的话你会选择哪一种那么显然的我们会选择第二种为什么呢原因是呢我们第二种它的这个管理成本是不是更低可以统一的去做一个处理那我们就来看一下这个第二种该如何去做一个实现
[01:21] 那么首先第一呢我们想到的一个实现逻辑呢就是使用这个什么呢使用这个拦截器进行做一个对于我们请求的一个拦截那么如果在拦截器中呢我们去判断那么如果缓存命中了我们直接返回是不是就可以了没有命中那么继续放行执行后面的逻辑就OK了那么这个本身呢其实也是一个缓存这样的一个它的一个作用和逻辑所在
[01:48] 那么接下来呢我们就来编写我们相关的一些这个拦截器的这个代码那么首先呢我们去创建一个interceptor这样的一个这样的一个包啊那我们去就在这个里面啊我们去创建我们这样的一个这样的一个包然后呢我们把这个相关这个代码呢我们就直接就贴过来了我们就不一一去写了给大家来讲解一下就可以了好那我们把这个呢就拷贝过来
[02:16] 这个里面内容稍微还是有一点点多的是吧好那我们来看一下这个里面的一些这个内容啊那么我们首先呢先来解决我们的这个就是没有导包的这个问题啊那么这个位置呢需要一个digest utils那么它呢是需要一个code c啊这样的一个包那我们来导一下那么在下面这个位置啊有个叫做有个叫code c就是commons code c啊这样的一个包
[02:45] 那么我们来看一下他还需要什么他还需要的一个是IO有TIOS那就是我们的IO包我们再来导一个comments-io就是comments-io这个包2.6好那么这样的话我们这个包就导入进来了那么接下来我们来看他还有没有一些其他的错误那么这个是不是就搞定了
[03:13] 好那么其他错误是不是就没了然后呢我们来看一下这个代码那么这个代码呢首先呢我们可以看到它呢是一个这个拦截器是吧去实现了一个HandleIntercept这样的一个接口然后呢在接口中呢实现了一个方法叫PreHandle就是在执行之前去执行它那么如果我们这个返回的值是如果是true的话就是放行那么如果是false的话就去做一个拦截OK
[03:43] 并且呢我们这个intercept我们把它标记为这是一个component就是sprint的一个组件那么就可以直接去使用和生效了那么这是我们要做的这个事情那么我们先把后面这个配置我们先加上来然后呢我们再去看这个里面的具体的逻辑那么在下面这个位置有一个我们设置了一个缓存的一个enable的开关那么我们需要把它加入到我们的一个
[04:12] 呃配置文件中那么咱们先把它呢就加入进来加到这个位置来那么为什么要有这个呃开关呢是我们比如说呢我们在做一些测试的时候呢我们就把它设置为处呃fos就可以了比如说我们要做这个呃生产上线的话那我们就可以把它设置为处啊就ok好那我们接着继续往下面看那么下面呢我还需要把这个呃就是拦截器呢去
[04:38] 注册到我们的Spring的这个容器中啊那我们把这个config我们就先拿过来啊先丢到这个里面来那么这个呢是一个webconfig啊呃他呢呃同样的也是去实现了我们这个webmvcconfiguration啊这样的一个这个接口然后呢我们去注入到我们的一个注入我们的这个就是我们写的这个ready sketchintercept这样的一个对象那么注入进来那么刚刚呢我们其实可以看到呢
[05:08] 在它的上面是不是我们已经定义了一个component这样的一个注解了对吧所以说在这个中它一定能够去注入这个对象注这个对象那么注解来之后我们需要做一个and这个操作就是我们去复写它这个里面这个and intercepts这个方法然后我们把它就加入到这个intercept中并且来设置它的一个路由的一个规则就是更新新
[05:38] 就是说所有的请求呢都会经过这个拦截器去做这样的一个处理那么接下来呢我们就来看一下我们这个拦截器的一个处理逻辑啊那么我们来看一下这个代码吧那么首先呢看一下pre-hand这个方法然后呢首先我们需要去判断我们当前有没有去开启我们的一个这个缓存如果未开启那我们就return true就可以了就是做我们请求的一个放行
[06:07] 然后呢下面呢我们获取到我们请求的一个这个message的这个方法然后呢我们去做一些这个判断那么我们仅对什么呢get和post做处理其他呢就不做处理了如果不等于这俩的话任意其中一个的话然后呢我们直接对听to也就是放行了那么走到这儿呢才需要我们真正去做一个处理那么在这个位置处理的逻辑啊其实就是呢我们需要在缓存中去
[06:36] 命中而缓存的使用的是readist那么就是在readist中做一个命中那么如果命中的话那么我们就直接去响应就可以了如果是未命中的话那我们就return true那么可以看到逻辑呢实在是就是那么我们未命中就return true如果命中的话就通过response做一个响应最后反应return false就ok那么我们知道在readist中玩的就是kv数据是不是那么这个
[07:05] key呢怎么样去做一个组成呢其实我们下面写了一个creator一个ready是key的这样的一个方法那么传递了一个request这样的一个对象那么我们如何去统一的处理我们这个key或者说我们统一的要去添加这个缓存逻辑那么这个key又该如何设计呢那么我们知道我们的这个接口的这个请求啊
[07:33] 它往往是通过什么呢我们的URL加我们的这个参数来组成的这样的一个请求那么如果我们相同的这个URL加相同的参数或者说加相同的这个投信息的话那么我们是不是就可以确定
[07:50] 这是相同的一次请求啊那我们就可以去判断它的一个结果是否有命中所以说这一点大家一定要想明白那么所以说呢我们的这个create ready is key它的一个逻辑呢其实就是这样的那么首先获取到它的一个URL然后呢我们获取它的一个请求的一个这个参数对吧那么如果如果是我们那种什么get请求啊对吧那我们就可以直接在我们的这个
[08:19] 就是问号后面传递这个参数啊那我们就可以通过这个request.getParameterMap来得到我们这个参数啊那么如果是我们发起的post请求那么我们在这个位置所提交的一些这个参数那么它是直接获取不到的啊所以这个位置要处理要注意一下啊如果它为空啊如果它为空那么就代表的是post请求那么如果不为空那么就代表的是get请求对吧那么如果是get请求就比较简单了
[08:49] 那我们直接把这个map呢做一个map做一个这个序列化就可以了得到一个这个节省对吧那么这个是相对比较简单的那么如果说是什么呢这个post请求那我们要拿它的响应体拿它的这个请求体啊拿它的请求体呢直接是拿不到的我们需要通过一个IO去读取才能够拿到但是要注意的是这个IO
[09:16] 一旦我们去读取的话那么读取完成这个IO呢就会被关闭啊就会被关闭那么也就意味着如果我们这个请求放行的话在我们的这个Controller中如果再想获取post提交的一些参数的话你是获取不到的
[09:36] 这一点要注意你是获取不到的所以说在这个位置我们需要做一个额外的一个处理怎么样处理就需要对request对象做一个重新做一个包装才能够去解决那么如何去做包装我们后面再说那么在这个位置我们先这样去写那么下面这个是处理完我们的请求的参数了那么下面这个就处理的是我们请求的投信息那么当然了这个是针对于我们当前的我们这个
[10:06] 碳花交友的这个应用而言的因为在我们碳花交友中呢我们的这个token呢是放到我们的投信机中的啊所以我们拿到他这个token信息去做一个拼接啊最后呢把它拼接到这个位置来就说我们把这个Pyramid的这个这个呃就是一个支付券啊一个支付券然后呢去做一个MD5做这样的一个加密然后呢去拼接到这个位置来那么整体去作为我们Redis中的一个key
[10:35] 来做一个存储那么这个大家应该能够理解了吧哎OK那么呃下面呢我们来看这个K就搞定了对吧然后呢我们去redis中呢去做一个我们这个呃获取对吧去读取那么如果拿不到就return to就放行了如果拿到的话那我们是不是就做一个响应啊就OK了那么这个逻辑啊那么这个逻辑其实我们就已经完成了一个这个教验是这样的一个逻辑了
[11:05] 那么在我们的配置中还稍微有一点问题就是那么我们配置文件我们并没有去写release相关的一些配置这个我们没有去写那么我们这个比较简单我们去我们的SSO里面去来拷贝一下那么在SSO里面我们是不是已经使用过release对吧那我们就把这个就拷贝过来了直接去做一个拷贝
[11:32] 然后呢我们就把它丢到下面这个server这个中丢到这个里面来那么我们就丢到这吧放到这来好那么有了这个配置之后啊那么我们这个release呢就可用了那么接下来呢我们就来尝试的去加一个我们就打一个断点放到这里然后呢我们把这个全局的这个开关呢我们去打开一下然后我们去来看一下我们这个逻辑啊写的有没有问题
[12:00] ok好那我们把我们的这个刚刚的这个server我们去把它停掉然后呢我们重新来做一个启动就是做一个debug的这样的一个启动了然后呢走好那我们来等待它的一个启动

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过拦截器实现Redis缓存命中的功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程笔记中“4.1. 采用拦截器进行缓存命中”的标题，以及对应的Java拦截器类RedisCacheInterceptor的代码开头部分，包含导入包和类声明。
画面2: 展示了RedisCacheInterceptor类中定义的成员变量，包括ObjectMapper、RedisTemplate和布尔变量enable，其中enable的值由配置文件中的${tanhua.cache.enable}注入。
画面3: 展示了项目中的pom.xml文件，其中包含mybatis-plus-boot-starter和mysql-connector-java的依赖配置。
画面4: 展示了pom.xml文件中新增的commons-codec依赖配置。
画面5: 展示了RedisCacheInterceptor类中preHandle方法的开始部分，包含对enable变量的判断。
画面6: 展示了RedisCacheInterceptor类中preHandle方法中对HTTP请求方法的判断，仅允许GET和POST请求通过。
画面7: 展示了RedisCacheInterceptor类中preHandle方法中对请求方法的判断逻辑。
画面8: 展示了RedisCacheInterceptor类中preHandle方法中创建RedisKey、查询缓存并返回数据的逻辑。
画面9: 展示了使用Advanced REST Client工具向服务器发送GET请求的界面。
画面10: 展示了RedisCacheInterceptor类中处理Authorization头的代码逻辑。
画面11: 展示了RedisCacheInterceptor类中createRedisKey方法的实现，用于生成Redis键。
画面12: 展示了application.properties配置文件中Spring Boot和Dubbo的相关配置。
画面13: 展示了application.properties配置文件中Redis集群的配置。
画面14: 展示了ServerApplication类的代码，以及右键菜单中“Run 'ServerApplication'”的选项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
package com.tanhua.server.interceptor;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework

