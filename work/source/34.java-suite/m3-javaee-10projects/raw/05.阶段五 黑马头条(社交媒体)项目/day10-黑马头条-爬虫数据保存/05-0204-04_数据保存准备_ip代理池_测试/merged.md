# 04_数据保存准备_ip代理池_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\04_数据保存准备_ip代理池_测试【海量资源尽在 666java.com】.mp4
- 时长 5分12秒（音频 313s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下当前咱们刚才写的当前这个关于IP代理池这块啊那测试呢你就在这啊在当前这个单元测试里边再去创建一个当前的这个Service就可以了啊开然后是这是一个test然后这个啊咱们就写写吧Spring Boot test然后是run with是吧Spring run的点class好说完之后呢下面你就应该去注入谁呀注入当前的
[00:32] 注入当前的callerip pro Service是吧好注入进来之后呢咱们下面就可以写方法啊这样咱们就少测两个啊咱们就测两个吧好吧测两个啊测两个之后呢咱们再去测试啊public void然后是test1但是这个方法名不太好是吧你可以找啊比如说找一个咱们就先测一个保存吧测一个保存测一个查询好吧这个之后啊这个之后啊咱们在这去加一个
[01:04] 直接去找他就可以了他里边有个.save但是save里边咱们需要有个对象是吧所以说在这去创建一个CLIPCLIP.new一个CLIP poolok没问题然后咱们可以在这设比如说设一个当前的IPIP的话咱们可以设置22224333好这是随便设的随便写的
[01:36] 再来去设置一个比如说再去设置一个CLIP.SET的一个port你们可以设置一个811好吧这个没有设过啊下面是CLIP.PROCE.SET.NABLE你得让它能用是设置一个true上面是CLIP然后是.SET一个credit好吧行那设置完之后啊咱们就先保存这几个吧你把它给保存
[02:07] 执行完之后呢那这个啊咱们就直接去查数据库就可以了好吧走稍等等他执行刚才我是保存了一条啊之前保存的这是啊咱们现在呢可以再去再去查询就可以了啊等他执行完之后咱们直接查询这个IP就可以了看看有没有这个数据到这啊确定没有是吧现在是没有啊那执行完之后咱们再来查好执行完了是吧你查一次
[02:40] yp这个点应用不管用了是吧好的指数了我看看啊四个五是吧把这个四个五骗他一下啊把这东西的删了好吧好你看再查是不是就有了啊没问题啊我现在这个数据咱们就算是保存完了那保存完之后啊咱们下面就可以再去测一个啊再去测一个嗯再去测一个简单的吧测一个第二个好吧第二个啊第二个的话就是当前的哪个
[03:16] 是否存在好吧是否存在的话咱们是有一个host有一个pot两个就可以了啊那这个东西就比较简单了啊删了然后呢这个东西也不是什么呢第一个呢第一个值就是当前这个值看这个值存在不存在就可以了好吧然后这是第一个那第二个呢就是你当前的这个1111啊就是你的通口好 设完之后啊我们在这儿去打印一下
[03:51] 所以是处和是force就可以了是吧试完之后啊你在这去执行一遍如果说打是处就是对的稍等当然这个剩下的方法啊你们也可以去测一测啊最好是让每一个这种方法都能去用啊正式开发的时候肯定是都要去测的啊这个咱们也是为了节省时间啊咱们就不再测了咱们就测两个代表就可以了你看目前的话是不是处啊
[04:27] 当然如果说你要是比如说你这样你可以给他随便加点东西那这个肯定找不着的啊我老的话你再去执行的话他肯定打印的是什么印的是一个force好吧行等一等啊等一等啊咱们就看一下咱们就测量方法咱们稍微等一等我再说了再说一遍啊其他的方法呢你们最好的是去测一测啊最好是测一测啊真正开发的时候肯定是得测测的没问题之后呢你才能正式提交啊才能去部署测试
[04:56] 然后不说测试完之后呢才能上正式对吧行你看这块啊这是一个force因为他没有找到ok行呃那这个啊这个弄完之后啊咱们当前的ip代理池这一块啊这个当前这个方法或者当前这个接口算是写完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中编写和测试一个用于管理爬虫代理IP池的服务层（CrawlerIpPoolService），包括保存、检查是否存在、更新和查询代理IP池的功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，选中测试类 CrawlerIpPoolServiceTest，右侧编辑器显示服务实现类 CrawlerIpPoolServiceImpl 中的 delete、unavailableProxy 方法。
画面2：在测试类 CrawlerIpPoolServiceTest 中，使用 @SpringBootTest 注解并添加 @RunWith(SpringRunner.class)。
画面3：在测试类中，使用 @Autowired 注解注入 crawlerIpPoolService。
画面4：在测试方法中，调用 crawlerIpPoolService.saveCrawlerIpPool() 方法。
画面5：在测试方法中，创建一个 ClipPool 对象并设置属性，然后调用 save 方法。
画面6：在测试方法中，使用 IDE 的代码补全功能，选择方法名 testSaveCrawlerIpPool。
画面7：在测试方法中，调用 crawlerIpPoolService.saveCrawlerIpPool() 方法并运行测试，终端显示 Spring Boot 启动日志。
画面8：测试成功，终端显示测试通过。
画面9：展示服务实现类 CrawlerIpPoolServiceImpl 中的 save、checkExist、update 方法。
画面10：在测试类中，编写测试方法 testCheckExist，并使用 IDE 的代码补全功能。
画面11：在测试方法中，调用 crawlerIpPoolService.checkExist() 方法并打印返回值，终端显示日志。
画面12：在测试方法中，调用 crawlerIpPoolService.updateByPrimaryWay() 方法，终端显示 HikariPool 日志。
画面13：在服务实现类中，编写查询可用IP池的代码，终端显示 Spring Boot 启动日志。
画面14：在测试方法中，调用 crawlerIpPoolService.checkExist() 方法并打印返回值，终端显示测试通过。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@Override
public List<ClipPool> queryAvailableList(ClipPool clipPool) {
    return clipPoolMapper.selectList(clipPool);
}

@Override
public void delete(ClipPool clipPool) {
    clipPoolMapper.deleteById(clipPool.getId());
}

@Override
public void unavailableProxy(CrawlerProxy proxy, String errorMsg) {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp(proxy.getIp());
    clipPool.setPort(proxy.getPort());
    clipPool.setEnable(false);
    clipPool.setRemark(errorMsg);
    clipPool.setCreateTime(new Date());
    List<ClipPool> clipPools = clipPoolMapper.selectList(clipPool);
    if (!clipPools.isEmpty()) {
        for (ClipPool clipPool : clipPools) {
            clipPoolMapper.updateById(clipPool);
        }
    }
}
```

画面2：
```java
package com.heima.crawler.Service;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
public class CrawlerIpPoolServiceTest {
```

画面3：
```java
@Autowired
private CrawlerIpPoolService crawlerIpPoolService;
```

画面4：
```java
crawlerIpPoolService.saveCrawlerIpPool();
```

画面5：
```java
@Test
public void testSaveCrawlerIpPool() {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp("2222.3333.444.5555");
    clipPool.setPort(1111);
    clipPool.setEnable(true);
    clipPool.setCreateTime(new Date());
    crawlerIpPoolService.saveCrawlerIpPool(clipPool);
}
```

画面6：
```java
@Test
public void testSaveCrawlerIpPool() {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp("2222.3333.444.5555");
    clipPool.setPort(1111);
    clipPool.setEnable(true);
    clipPool.setCreateTime(new Date());
    crawlerIpPoolService.saveCrawlerIpPool(clipPool);
}
```

画面7：
```java
@Test
public void testSaveCrawlerIpPool() {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp("2222.3333.444.5555");
    clipPool.setPort(1111);
    clipPool.setEnable(true);
    clipPool.setCreateTime(new Date());
    crawlerIpPoolService.saveCrawlerIpPool(clipPool);
}
```

画面8：
```java
@Test
public void testSaveCrawlerIpPool() {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp("2222.3333.444.5555");
    clipPool.setPort(1111);
    clipPool.setEnable(true);
    clipPool.setCreateTime(new Date());
    crawlerIpPoolService.saveCrawlerIpPool(clipPool);
}
```

画面9：
```java
public void saveCrawlerIpPool(ClipPool clipPool) {
    clipPoolMapper.insertSelective(clipPool);
}

@Override
public boolean checkExist(String host, int port) {
    ClipPool clipPool = new ClipPool();
    clipPool.setIp(host);
    clipPool.setPort(port);
    List<ClipPool> clipPools = clipPoolMapper.selectList(clipPool);
    if (null != clipPools && !clipPools.isEmpty()) {
        return true;
    }
    return false;
}

@Override
public void updateCrawlerIpPool(ClipPool clipPool) {
    clipPoolMapper.updateByPrimaryWay(clipPool);
}
```

画面10：
```java
@Test
public void testCheckExist() {
    boolean b = crawlerIpPoolService.checkExist("2222.3333.444.5555", 1111);
    System.out.println(b);
}
```

画面11：
```java
@Test
public void testCheckExist() {
    boolean b = crawlerIpPoolService.checkExist("2222.3333.444.5555", 1111);
    System.out.println(b);
}
```

画面12：
```java
@Override
public List<ClipPool> query(ClipPool clipPool) {
    return clipPoolMapper.selectList(clipPool);
}

@Override
public List<ClipPool> queryAvailableList(ClipPool clipPool) {
    return clipPoolMapper.selectList(clipPool);
}
```

画面13：
```java
List<ClipPool> clipPools = clipPoolMapper.selectList(clipPool);
if (!clipPools.isEmpty()) {
    for (ClipPool clipPool : clipPools) {
        clipPool.setEnable(false);
        clipPool.setRemark("error");
        clipPoolMapper.updateByPrimaryWay(clipPool);
    }
}
```

画面14：
```java
@Test
public void testCheckExist() {
    boolean b = crawlerIpPoolService.checkExist("2222.3333.444.5555", 1111);
    System.out.println(b);
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

