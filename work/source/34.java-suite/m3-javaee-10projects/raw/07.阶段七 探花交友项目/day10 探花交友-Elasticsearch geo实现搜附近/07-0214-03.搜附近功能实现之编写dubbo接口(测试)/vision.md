# 画面线理解：03.搜附近功能实现之编写dubbo接口（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\03.搜附近功能实现之编写dubbo接口（测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:27, 00:41, 01:35, 02:07, 02:43, 03:06, 03:34, 03:56, 04:22, 04:50, 05:08, 05:34, 05:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:22:26

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
