# day04-17-认证(登录)功能测试(过网关)

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-17-认证(登录)功能测试(过网关)_【海量资源尽在 666java.com】.mp4
- 时长 2分53秒（音频 174s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们的这个登录功能测试完之后呢咱接下来再进行一个测试什么测试呢过网关去获得令牌或者说过网关去实现什么呀登录那么这个过网关测试呢其实也是为后边的前后端集成测试是不是打下基础的对不对打基础的啊因为大家知道以前咱说过前后端集成测试的时候前端发了所有的请求都要先过什么呀网关
[00:30] 所以咱这呢加一个过网关测试其实说白了就是端口号改成什么呀网关的端口号53010吧是不是其他不用动啊咱看行不行那我这的话其实可以进行一个复制啊点这个选项复制一下就行是不是然后呢这样呢你可以改成叫什么呀对过网关这非常方便你看普通版是不是改成过网关的然后你看这里边的请求地址啊包括这些参数啊你看
[01:05] 现成的因为咱是复制过来的但你要注意这就不能是53020了这应该改成53010是53020吗是不是的话你想确认一下也简单我们在这看看它的启动参数就OK了应该是53010对不对53010那53010的话那咱接下来看看啊那这个时候就注意了啊我在发请求的时候这个请求是不是先过了什么呀网关有网关转发到什么呀
[01:35] 就这点这个流程发生变化那另外呢提醒大家特别注意你在进行过网关测试的时候一定要注意Gateway上面是不是要配置到UAA的这个什么呀路由转发有印象吗你要检查你的Apollo你没有配你得加上反正你得检查检查就是网关Gateway因为咱前面Conda和Consumer都配过就在Application里面吧咱展开
[02:05] 眼镜文本看好了啊我这儿是配过了但是你的我觉得应该是没配的就这个地方这儿啊你就复制之前consumer hallaccount然后复制过来然后改一改就行了就这儿改成ua就行了啊这个地方一定要做要检查没有就加上否则你这个过网关测试是肯定是行不通的这个一定要注意这是要提前做好的啊提前做好你在这儿进行什么呀测试啊一定要注意这点
[02:35] 好我们接下来点击一下send好目前大家看是不是也没有问题吧是不是也能正常获取到什么呀令牌那么这也就为将来咱们前后端集成测试这个电竞技术

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Postman 发起 OAuth2.0 认证请求，并结合 Apollo 配置中心管理微服务的路由规则。

2) 按时间顺序列出每张画面的要点：
画面1：Postman 中选中“统一认证中心”集合下的“登录获取令牌”请求，准备发送。
画面2：IntelliJ IDEA 中打开项目 wanxingzp-uaa-Service，准备启动服务。
画面3：在 IntelliJ IDEA 中，点击“Run”菜单，准备运行服务。
画面4：在 IntelliJ IDEA 的运行配置中，将 Main class 设置为 cn.itcast.wanxingzp.uaa.GatewayServer，启动网关服务。
画面5：Postman 中编辑 POST 请求，设置 URL 为 http://localhost:5331/oauth/token，Body 为 form-data 格式，包含 grant_type、client_id、client_secret、username、password、domain、authenticationType 等参数。
画面6：浏览器访问 Apollo 配置中心首页，显示项目列表。
画面7：浏览器访问 Apollo 配置中心的配置页面，URL 为 localhost:8070/config.html#/?appId=gateway-server。
画面8：在 Apollo 配置中心，选择“application”配置项，查看其下多个微服务的配置。
画面9：在 Apollo 配置中心，点击“新增配置”按钮，准备添加新的配置。
画面10：在 Apollo 配置中心，编辑“application”配置项，显示其内容，包括多个 zuul.routes 的配置。
画面11：Postman 中再次显示“登录获取令牌”请求的 Body 参数。
画面12：Postman 中发送请求后，显示响应结果，包含 access_token、token_type、expires_in、scope、code 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4 中的运行配置：
Main class: cn.itcast.wanxingzp.gateway.GatewayServer
JVM options: -Dspring.profiles.active=dev -Dserver.port=8080
Program arguments: 
Working directory: 
Environment variables: 
Use classpath of modules: wanxingzp-gateway-server
Include dependencies with "Provided" scope: true
Spring Boot JAR: Default (1.8.0-SNAPSHOT)
Shorten command line: true
Enable debug output: false
Hide banner: true
Enable launch optimization: true
Enable JMX Agent: true
Running debug actions: Do nothing
On Update actions: Do nothing
On frame destruction: Do nothing
Active profiles: dev

画面10 中的 Apollo 配置内容：
zuul.routes.consumer-Service.stripPrefix = false
zuul.routes.account-Service.stripPrefix = false
zuul.routes.naa-Service.stripPrefix = false
zuul.routes.account-Service.path = /account
zuul.routes.consumer-Service.path = /consumer
zuul.routes.naa-Service.path = /naa
zuul.retryable = true
zuul.add-host-header = true
zuul.ignoredServices = 

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

