# 07_动态ip代理池管理_更新动态ip

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\07_动态ip代理池管理_更新动态ip【海量资源尽在 666java.com】.mp4
- 时长 4分52秒（音频 293s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去完成这个方法叫更新动态代理IP那这个更新该怎么去更新呢其实呢这时候呢咱们又要用到了目前的第二个地址就是这个就是这个地址好咱们可以拷贝一下啊把它呢打开啊其实这个我已经打开了就是这个东西啊咱们可以重新拷贝一下那这块呢这个呢是一个89的IP地址啊这样它是一个免费的动态IP
[00:29] 网上有很多你可以在网上去搜一搜啊只是一个啊这样的话呢咱们主要的就是用到当前的这些IP咱们做的第一步呢就是说咱们要干嘛呢要去从当前的页面上去下载下来下载下来之后呢解析解析了解析之后呢拿到这些所有的IP然后呢去校验一个一个去校验如果说没有问题咱们再去存入到咱们的数据库中这样就可以了
[00:57] 好吧那咱们下面呢就来去来执行一下当前这些步骤啊嗯首先呢咱们要去下载当前这个IP啊下载怎么办呢咱们在这啊再去抽出来一个方法好吧这叫getbatch的话怎么写啊p-r-a-b啊然后是c-r-p然后是p-o-r然后是list那这个是没有参数的啊没有参数
[01:26] 这里边怎么写啊?
[01:29] 要返回的其实就是一个CL是一个集合啊没有是吧?
[01:38] 没有的话怎么就创建出来好这是什么呢?
[01:46] 是获取什么?
[01:48] 获取发取的发取的动态代理IP如果说你现在已经在网上去发取了当前的IP
[02:02] 然后你该怎么办呢然后咱们就要去校验了是吧在这写一下吧在网上抓取免费的IP好这是一个啊然后下面呢就是校验呗校验怎么校验的先去判断呗那就校验的话只能是一个一个去校验啊如果说None呢不等于当前的CLIPPlist然后是并且干嘛是它不等于空是吧好
[02:34] 然后下面咱们就可以去循环循环的话就是还是一种方式拿到这个之后咱们首先要做的第一件事就是先去调验前的微向好吧那调验完之后如果说没有问题咱们这时候就可以去保存去保存这样咱们先去判断一下调验完之后当前的这个Mable如果说是True的话但是可用
[03:06] 是可用的话咱们就可以去保存了保存之前咱们还是要去检查一下检查啥呢你还检查啥呢检查的话是从表中看看有没有看这个IP有没有有的话咱们就没有必要再去保存了没有的话咱们再去保存好吧这时候咱们还是用今天的callerIP pro Service.r有一个什么一个check check this一个是当人的他cl.getip
[03:37] 第二个呢是当前的什么这样的话它就返回了当前的一个这种过日的形如果说啊如果说非当前这个东西不存在不存在的话这时候呢你就可以去保存了保存很容易的啊是用当前的对象点儿有一个save你把当前这个对象放进去就可以了好吧这样的话就算是保存成功那咱们在这儿再去一个东西吧
[04:08] logif里面怎么写啊叫加入代理ip嗯行就这么写吧然后呢ip是多少然后是pot是pot是哪个下面是getip然后是getpot好了那这样的话我们就把这个东西给定义完了啊那定义完之后这里边还少一步是吧你怎么去获取啊
[04:44] 这个获取的方式其实就是干嘛就是去网上去下载当前的IP好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中通过 ProxyManager 类管理代理池，包括获取代理列表、验证代理、检查代理是否存在并保存有效代理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 crawler.properties 配置文件，其中包含 WebDriver、代理验证 URL、是否使用代理等配置。
画面2：浏览器打开一个空白页面，URL 为 http://www.89ip.cn/。
画面3：在 ProxyManager.java 文件中，展示 updateProxyIp 方法的开头部分，设置连接池参数。
画面4：在 updateProxyIp 方法中，调用 getGrabCllPoolList() 获取代理列表，IDE 显示方法返回类型为 List<ClipPool>。
画面5：在 updateProxyIp 方法中，对获取的代理列表进行空值和空集合判断，IDE 显示 if 语句的条件。
画面6：在 updateProxyIp 方法中，对代理列表进行遍历，IDE 显示 for 循环的结构。
画面7：在 updateProxyIp 方法中，对每个代理对象调用 validateProxyIp 方法进行验证。
画面8：在 updateProxyIp 方法中，调用 crawlerIpPoolService.checkExist 方法检查代理是否存在。
画面9：在 updateProxyIp 方法中，调用 crawlerIpPoolService.saveCrawlerIp 方法保存有效代理。
画面10：在 updateProxyIp 方法中，添加日志记录，输出插入的代理 IP 和端口。
画面11：在 updateProxyIp 方法中，IDE 显示方法的完整结构和注释。
画面12：在 updateProxyIp 方法中，IDE 显示方法的完整结构和注释。
画面13：在 updateProxyIp 方法中，IDE 显示方法的完整结构和注释。
画面14：在 updateProxyIp 方法中，IDE 显示方法的完整结构和注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
# windows
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/local/bin/chromedriver
proxy.setUrl=http://www.89ip.cn/tejia/api/1.html?port=500&num=100&address=isp
proxy.validate.url=http://http://wip.kkhe.com
# 是否使用代理
proxy.isUsedProxy=false
csdn.comment.url=https://blog.csdn.net/${author}/phoenix/comment/list/${id}?page=1&size=100&type=1
crawler.cookie.name=new_sc_v2
crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=java,web,arch,unix,db,mobile,open,cloud,engineering,iot,fund,career
# 爬取页面时
crawler.help.nextPagingSize=0
# 爬取页面时
crawler.help.nextPageSize=10
# 爬取页面时
crawler.nextupdatehours=4,16,64,128,256
```

画面3：
```
clpPool.setEnable(true)
clpPool.setCode(groxyValidate.getReturnCode());
clpPool.setDuration(groxyValidate.getDuration());
clpPool.setErrror(HMSStringUtils.getFixedLengthStr(groxyValidate.geterror(), length: 70));
```

画面6：
```
List<ClipPool> clpPoolList = getGrabCllPoolList();
if(null != clpPoolList && !clpPoolList.isEmpty()){
    for (ClipPool clipPool : clpPoolList) {
        validateProxyIp(clipPool);
        if(clipPool.getEnable()){
            crawlerIpPoolService.checkExist(clipPool.getIp(), clipPool.getPort());
            if(!exist){
                crawlerIpPoolService.saveCrawlerIp(clipPool);
                log.info("插入代理ip,ip: {},port: {}", clipPool.getIp(), clipPool.getPort());
            }
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

