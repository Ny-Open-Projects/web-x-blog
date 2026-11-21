# 05_动态ip代理池管理_检验ip1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\05_动态ip代理池管理_检验ip1【海量资源尽在 666java.com】.mp4
- 时长 9分58秒（音频 598s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来去完成第二块的内容就是代理IP的更新那这里边有两个URL啊是咱们需要去在配置文件中去配置第一个呢就是咱们要去抓取的这种IP的地址比如说你的IP从哪来啊咱们是从89IP当前这个地址上去获取然后第二个呢那这IP到底能用不能用呢咱们用当前的URL呢就可以去验证
[00:28] 可以验证现在这两个咱们其实在咱们的系统中已经配完了可以看一下一个是这个一个是这个然后接着往下看下面咱们有一个类叫Proxy IP Manager这里边有吗没有的是吧咱们需要去创建这么一个类来去抓取和更新还有校验当前的IP这里边最主要有两个方法一个是校验IP的可用性
[00:55] 然后第二个呢咱们是有一个更新的代理IP更新代理IP好吧那咱们下面呢就来去干嘛呢就来去创建一下当前这个类啊这个类呢咱们是创建哪啊创建到当前这有一个plosy创建一个包就叫他啊然后下面呢咱们就在这去创建类右键class叫这个东西然后呢是让Spring去管理首先第一个啊
[01:30] compound然后上面咱们可以写个注释是吧注释呢叫做什么动态动态代理AP管理类刚才说了里边呢咱们注意最主要的是有两个方法是吧嗯咱们这样先先这加一个logof2吧这样方法呀一个呢是照验我们的IPum publicvalidatevalidatevavalidate
[02:04] DATEVALIDATE.PLUSSEIP好吧这个是没有参数的啊行那这是一个是教验IP教验教验动态代理IP然后第二个呢咱们叫啥呢叫更新动态代理IPPUBLICVOID然后是叫updatePLUSSEIP这是更新
[02:46] 动态代理IP你说这两个方法什么时候调用呢后期会再去写写的时候就是写一个定时咱们会定时的去调用这两个方法好吧好那咱们下面就来一个一个方法的去写先来去写当前的这个东西首先的这块那你说你的IP怎么来呢教验从哪去教验呢
[03:16] 这个咱们在当前的表中其实已经有一部分了这个表是在这打开咱们的数据库就是当前的mycat表然后你找到当前的serverip pool它这里边其实已经有了那么多IP但是这IP到底能用不能用所以说咱们要去不停的去校验当前这个IP也就是说咱们这个管理的IP必须得去校验然后你才能去用好吧
[03:47] 这时候咱们就去校验了你首先得先去过去当前的IP是吧所以说你要去先从表中去查出来private然后是咱们要去注入一个caller叫ip Service好吧叫他然后在这去注入注入进来之后你就可以直接查点咱们有一个sorylist这个参数这个参数的话其实你可以拗一个空的就可以了
[04:18] 又一个空的最终是没有条件是查询出来了所有的东西好下面咱们就可以各一个的去校验首先它不等于None是吧必须得查出来然后推然后是它.isEmpty如果它不为空那这时候我们就可以去查询就可以去设置它的什么这种校验应该是要校验它的一个东西校验当前IP的
[04:49] 可用性然后咱们就可以去拿到这样咱们资源之前先可以去循环ZLIPPROBLESSER.FOR然后咱们先去拿到它的这种可用不可用是吧.NABLE.JIN.NBABLE它应该是一个布尔类型什么叫OLD吧叫OLD
[05:24] 你随便起个名然后呢然后怎么办呢然后咱们就可以去校验了啊校验状态是否可用以前说的是说的是AP的状态可用啊然后接着往下看啊然后呢咱们就去校验啊写一个方法validate clauseAP这时候呢虽然是方法名是一样啊但是呢这时候咱们是有啥呢
[06:00] 是有参数的参数就是现在这个对象好吧那当然这个没有是吧没有咱们就创建出来我们叫publicprivate吧也行privateprivate然后wide然后是就叫他拷贝一下参数呢参数就是怎样参数就是当前的CLIPpro好行那这个方法咱们先去放到这啊就是在说比如说你教研完之后啊
[06:34] 接完之后这里边的值有可能会改那改哪些呢咱们可以看判断一下如果原始状态以及当前状态都不可用判断是废除的代理然后咱们又删除然后又删除这个是原始的你验证完之后它其实还有个新的应该是
[07:13] 会给他重新复制明白了吧所以说在这先去判断一下判断的就是说当前的然后呢并且呢并且的是CLgetEnable说他那个他呢也是也是first的话那这时候呢那就是要删除了好那就是删除IP删除代理吧
[07:47] 删除代理这个好办吧,all Service.delete,你就把前这个对象删了就可以了这是一块啊当然你可以在这去记录一个日志login然后这里边咱们就可以去说删除代理IP它的一个东西呢咱们也可以去设置一下比如说它的一个IP是多少IP是多少一个是IP然后第二个呢是
[08:19] 好好然后下面咱们又咱们就可以设置下叫什么啊点get ip啊第二个呢就是点get port这样的话咱们就算是打印制了啊这样你可以把上面的一块一块放到上面好那这样的话就设置完了啊当然那你说我这块啊嗯不能用啊他两个呀都是出都是出的话呢这时候呢咱们就可以干嘛呢
[08:58] 就可以去更新一下当前的IP更新怎么办呢poller-ip.Service还有一个update然后传的也是当前这个对象好吧这样的话咱们就算是更新了IPlog.info这东西叫更新更新代理IP好然后咱们在这去设置一下IP是谁呢
[09:28] 然后第二个是Port是谁呢就可以去设置下咱们下面就可以去写了我写就是还是这样写是吧第二个呢是CLPro.getPort那行那这样的话咱们就算是设置完了行那这个方法咱们还没有写咱们一会儿咱们再去写当前这个验证IP的方法

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中通过ProxyIpManager类动态管理并验证代理IP，涉及配置文件、服务层调用和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“2 代理IP更新”，具体到“2.1 ProxyIpManager类”，并显示了类的包路径“com.heima.crawler.proxy.ProxyIpManager”。
画面2：在ProxyIpManager类中，定义了静态常量proxyGetUrl和正则表达式pattern，用于获取和解析代理IP。
画面3：展示项目目录结构，重点在“src/main/resources”下的“crawler.properties”配置文件，其中包含代理IP相关配置。
画面4：展示ProxyIpManager类的顶部注解和成员变量，包括@Component、@Log4j2、以及@Autowired注入的CrawlerIpPoolService和SeleniumClient。
画面5：展示MySQL数据库中代理IP表的数据，包含id、supplier、ip、port等字段。
画面6：在ProxyIpManager类中，展示validateProxyIp方法的定义，准备实现代理IP的验证逻辑。
画面7：在validateProxyIp方法中，开始编写逻辑，判断clpPoolList是否为null。
画面8：在validateProxyIp方法中，使用for循环遍历clpPoolList，对每个代理IP进行状态检查。
画面9：在validateProxyIp方法中，调用validateProxyIp方法对当前代理IP进行验证。
画面10：在validateProxyIp方法中，使用if语句判断代理IP是否可用。
画面11：在validateProxyIp方法中，使用log.info记录日志，显示“删除代理ip.ip:0,port:0”。
画面12：在validateProxyIp方法中，使用if语句判断代理IP是否可用。
画面13：在validateProxyIp方法中，使用log.info记录日志，显示“更新代理ip.ip:0,port:0”。
画面14：在validateProxyIp方法中，使用if语句判断代理IP是否可用，如果可用则调用crawlerIpPoolService.updateCrawlerIpPool方法更新代理IP。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
crawler.properties 配置
proxy.get.url=http://www.89ip.cn/tqdl.html?api=1&num=50&port=&address=&type=1
proxy.validate.url=http://myip.kkcha.com/

画面3：
crawler.properties
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
proxy.get.url=http://www.89ip.cn/tqdl.html?api=1&num=50&port=&address=&type=1
proxy.validate.url=http://myip.kkcha.com/
#是否启用代理
proxy.isUsedProxy=false
csdn.comment.url=https://www.csdn.net/$ (author)/phoenix/comment/list/1?&id=1&page=1&size=100
crux.cookie.url=https://www.csdn.net/nav
crawler.init.url.prefix=https://www.csdn.net/nav
crawler.init.url.suffix=java
crawler.help.nextPageSize=0
#1次爬取时间
crawler.nextupdatehours=4,16,64,128,256

画面6：
public void validateProxyIp() {
}

画面7：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
    }
}

画面8：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
    }
}

画面9：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

画面10：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

画面11：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

画面12：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

画面13：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

画面14：
public void validateProxyIp() {
    List<ClipPool> clpPoolList = crawlerIpPoolService.queryList(new ClipPool());
    if (null == clpPoolList || clpPoolList.isEmpty()) {
        return;
    }
    for (ClipPool clpPool : clpPoolList) {
        //校验当前代理ip是否可用
        validateProxyIp(clpPool);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

