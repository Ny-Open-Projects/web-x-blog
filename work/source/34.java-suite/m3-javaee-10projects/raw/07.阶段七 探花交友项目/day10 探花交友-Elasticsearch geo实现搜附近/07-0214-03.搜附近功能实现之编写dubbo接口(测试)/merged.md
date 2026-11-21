# 03.搜附近功能实现之编写dubbo接口（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\03.搜附近功能实现之编写dubbo接口（测试）_【海量资源尽在 666java.com】.mp4
- 时长 5分56秒（音频 356s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来测试一下啊我们刚刚所写的这个服务那么下面呢我们把这个测试用力啊我们就拷贝过来那么我们之前来看一下啊那么在我们的这个Service下面呢我们来找一下我们的测试用力啊那么之前呢其实我们已经有一个这个test user location啊那么接下来呢我们就
[00:23] 把它呢就这样我们这样来拷贝一下就把这两个测试方法我们拷贝过来啊就可以了然后呢我们拷贝一下因为写这个呢是挺费时间的啊那么这两个方法在做了一个什么事情啊其实就是一个是在做更新用户的一个这个位置另外一个呢就是
[00:46] 去做查询那么首先我们来看一下这个呢就是调用我们之前所写的这个方法然后呢我们插入了一些我们的测试数据然后呢我们是随机的我们去选了一些用户然后呢给他去做了一些这个位置的一个更新那么比如说这个121012这个数据啊在这个里面呢我们可以看到比如说1这个用户那么他呢所在的位置啊当前位置就在金茂大厦
[01:15] 这个位置啊那么都是以这个上海的一个上海市的一个这个地址呢去选取了一些这个地名啊当然了我们这个还是集中在这个上海的那个东方明珠这一块的一些这个位置啊那么我们怎么样能够找到他的这个所在的坐标呢其实我们呢有一个地址啊那么打开来看一下那么这个呢是百度啊百度的一个这个
[01:41] 拾取坐标系统的这样的一个系统那么在这个位置我们比如说可以输入什么上海上海经贸大厦我们输入一下那么其实可以看到在这个位置你看是不是他已经就找到经贸大厦了那么这个坐标拷贝一下就OK了这个就是经贸大厦所在的地理位置那么东方明珠就是在这个位置在这东方明珠
[02:11] 然后我们来看一下这个数据比如说这个二号用户他现在就在东方明珠这一块而这个十号用户是在陆家嘴地铁站这一块然后十二号用户是在上海中心大厦等等有一些这个数据当然有一些远一些的比如说这个浦东机场那么这个就会离得比较远一点
[02:33] 那么然后还有像红条火车站也是相对比较远的一些位置那么我们就把这些数据可以去插入到我们的表里面来然后上面的查询就是什么我们来看一下那么它所设置的就是我当前用户就是我用户ID唯一的用户然后设置它的一个精度和纬度然后我们设置一个转折就是一个范围就是1000
[03:01] 那么就是查询在一公里范围内的一些这个用户那么下面呢我们就来执行一下那么首先呢我们执行这个下面的这个测试用力好那我们等待他的一个执行好那么我们这个测试用力呢就执行结束了下面我们来刷新一下我们的这个库然后呢下面我们找到就有个叫做什么的炭花然后有个叫做优仁我们来找一下
[03:28] 那张表呢在这啊叫UseLocation啊这张表那么我们就有这些数据啊那么用户ID为1的这个用户然后呢用户ID为2的这个用户啊好那么现在呢我们就已经完成了数据的一个插入啊那么接下来呢我们就来做查询那么我们去查询这个一公里范围内的一个用户
[03:49] 那么我们是不是也可以去查询这样两公里范围内的对吧那我们先来去做一个查询吧先查询这个一公里范围内的好那我们来等待他的一个执行好那么我们这个呢就执行结束了那么在我当前这个用户范围内呢那么我们查询到有四条数据啊其实是三条因为我们要把第一条这个排除掉就是自己要排除掉啊那么是不是查到有三条这个数据啊那么你比如说我现在呢把这个
[04:16] 范围呢我扩展到五公里那我再去做一个查询那我们来看一下他能够查询到几条数据好那我们来看一下他的执行的结果啊那么可以看到呢当我们把这个范围扩大到五公里的时候呢查询到了这个数据啊显然是不是就比之前就多很多了是吧比如说像这个经贸大厦然后呢火车站呢这个上海中心大厦上海市公安局还有一些像鲁迅公园啊
[04:46] 然后还有些东方明珠这个都已经就查到了对吧所以这个范围就更大了更大了ok好那么到这里其实就测试出我们这个方法它是不是就是ok的对吧那么我们也可以来测试一下那么我们的用户的位置对吧我们来查询一下这样我们来写一个方法去查询一下那么写一个test query然后location
[05:14] 然后呢by user id啊做这样的一个查询好那么我们去查询一下那么我就调用类似点这个location api然后呢我们去query去做一个查询我们查询这个1啊这个用户他的一个信息那么我们去查询到是一个这个vo这个对象那我们把这个vo这个对象呢我们就打印出来好那我们来执行一下
[05:40] 好那么我们来看一下查询的结果那么显然呢就查询到我们这个用户的一个这个信息了那就说明我们写这两个方法呢是不是都没有问题啊哎OK好那么关于我们这个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot 单元测试，调用服务层接口查询和保存用户地理位置信息，并验证数据在 MongoDB 中的存储情况。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 TestUserLocationApi 的代码，包含 testQuery 和 testSaveTestData 方法，用于查询和保存用户位置。
画面2：展示 testSaveTestData 方法中，向数据库插入多个用户位置数据，包含用户ID、经纬度和地址。
画面3：展示 testSaveTestData 方法中，插入的用户位置数据列表，包含用户ID、经纬度和地址。
画面4：展示 TestUserLocationApi 类的代码，包含 @SpringBootTest、@RunWith、@Autowired 注解，以及 testQuery 方法。
画面5：展示百度地图拾取坐标系统，显示坐标 (121.512253, 31.24094) 对应的地址“金茂大厦”。
画面6：展示 testSaveTestData 方法中，插入的用户位置数据列表，包含用户ID、经纬度和地址。
画面7：展示 testSaveTestData 方法中，插入的用户位置数据列表，包含用户ID、经纬度和地址。
画面8：展示 MongoDB 数据库中 userLocation 集合的文档内容，显示插入的用户位置数据。
画面9：展示 testUpdate 方法，用于更新用户位置，返回更新后的 ID。
画面10：展示 testQuery 方法，用于查询用户位置。
画面11：展示 testQuery 方法的运行结果，打印出查询到的用户位置数据。
画面12：展示 UserLocationApi 类的代码，包含 get 和 update 方法。
画面13：展示 UserLocationApi 类的代码，包含 get 和 update 方法。
画面14：展示 TestUserLocationApi 类的代码，包含 @SpringBootTest、@RunWith、@Autowired 注解，以及 testQuery 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.vo.UserLocationVo;
@Test
public void testQuery() {
    Double longitude = 121.512253;
    Double latitude = 31.24094;
    Integer range = 1000;
    List<UserLocationVo> userLocationVos = this.userLocationApi.queryUserFromLocation(longitude, latitude, range);
    for (UserLocationVo userLocationVo : userLocationVos) {
        System.out.println(userLocationVo);
    }
}
@Test
public void testSaveTestData() {
    this.userLocationApi.updateUserLocation(11, 121.512253, 31.24094, "金茂大厦");
    this.userLocationApi.updateUserLocation(101, 121.506377, 31.243844, "东方明珠");
    this.userLocationApi.updateUserLocation(102, 121.508815, 31.239185, "上海中心大厦");
    this.userLocationApi.updateUserLocation(25L, 121.493444, 31.240513, "上海公安");
    this.userLocationApi.updateUserLocation(30L, 121.462452, 31.253463, "上海火车站");
    this.userLocationApi.updateUserLocation(34L, 121.327908, 31.20333, "上海博物馆");
    this.userLocationApi.updateUserLocation(38L, 121.425155, 31.277476, "鲁迅公园");
}
```

画面2：
```java
@Test
public void testSaveTestData() {
    this.userLocationApi.updateUserLocation(11, 121.512253, 31.24094, "金茂大厦");
    this.userLocationApi.updateUserLocation(101, 121.506377, 31.243844, "东方明珠");
    this.userLocationApi.updateUserLocation(102, 121.508815, 31.239185, "上海中心大厦");
    this.userLocationApi.updateUserLocation(25L, 121.493444, 31.240513, "上海公安");
    this.userLocationApi.updateUserLocation(30L, 121.462452, 31.253463, "上海火车站");
    this.userLocationApi.updateUserLocation(34L, 121.327908, 31.20333, "上海博物馆");
    this.userLocationApi.updateUserLocation(38L, 121.425155, 31.277476, "鲁迅公园");
}
```

画面3：
```java
@Test
public void testSaveTestData() {
    this.userLocationApi.updateUserLocation(11, 121.512253, 31.24094, "金茂大厦");
    this.userLocationApi.updateUserLocation(101, 121.506377, 31.243844, "东方明珠");
    this.userLocationApi.updateUserLocation(102, 121.508815, 31.239185, "上海中心大厦");
    this.userLocationApi.updateUserLocation(25L, 121.493444, 31.240513, "上海公安");
    this.userLocationApi.updateUserLocation(30L, 121.462452, 31.253463, "上海火车站");
    this.userLocationApi.updateUserLocation(34L, 121.327908, 31.20333, "上海博物馆");
    this.userLocationApi.updateUserLocation(38L, 121.425155, 31.277476, "鲁迅公园");
}
```

画面4：
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.vo.UserLocationVo;
import org.junit.Test;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLocationApi {
    @Autowired
    private UserLocationApi userLocationApi;
    @Test
    public void testQuery() {
    }
}
```

画面6：
```java
@Test
public void testSaveTestData() {
    this.userLocationApi.updateUserLocation(11, 121.512253, 31.24094, "金茂大厦");
    this.userLocationApi.updateUserLocation(101, 121.506377, 31.243844, "东方明珠");
    this.userLocationApi.updateUserLocation(102, 121.508815, 31.239185, "上海中心大厦");
    this.userLocationApi.updateUserLocation(25L, 121.493444, 31.240513, "上海公安");
    this.userLocationApi.updateUserLocation(30L, 121.462452, 31.253463, "上海火车站");
    this.userLocationApi.updateUserLocation(34L, 121.327908, 31.20333, "上海博物馆");
    this.userLocationApi.updateUserLocation(38L, 121.425155, 31.277476, "鲁迅公园");
}
```

画面7：
```java
@Test
public void testSaveTestData() {
    this.userLocationApi.updateUserLocation(11, 121.512253, 31.24094, "金茂大厦");
    this.userLocationApi.updateUserLocation(101, 121.506377, 31.243844, "东方明珠");
    this.userLocationApi.updateUserLocation(102, 121.508815, 31.239185, "上海中心大厦");
    this.userLocationApi.updateUserLocation(25L, 121.493444, 31.240513, "上海公安");
    this.userLocationApi.update

