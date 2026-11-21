# 08.Elasticsearch实现位置查询之编码实现（更新用户地理位置的单元测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\08.Elasticsearch实现位置查询之编码实现（更新用户地理位置的单元测试）_【海量资源尽在 666java.com】.mp4
- 时长 3分49秒（音频 229s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就把刚刚我们所写这个方法呢我们来测试一下那么下面呢我们就把这个测试用力呢我们来拷贝一下那我们来做一个执行那么我们先把这个包呢我们先在我们的test这个目录下面那我们先去创建出来然后呢栽赃然后呢去创建一个这个包好然后呢下面呢我们就把这个测试用力吧我们就拷贝过来直接丢到这个包里面来
[00:30] 然后呢下面这个呢我们就这样我们先给它注射掉因为这个方法我们还没有写嘛然后呢我们先来测试上面的一个save这个操作好那我们来看一下这个操作那么这个呢是跟我们在前面测试mongodb的时候是一样的那么就是我们去传递我们的一个用户ID
[00:50] 然后呢传递我们的一个这个经纬度啊然后呢去呃传递一个地名然后呢去做一个操作的一个操作啊那么这样我们在我们的update这个里面呢我们去打一个断点呃然后呢我们来执行一下这个呃操作啊debug走
[01:06] 好那我们来等待一下它的一个执行好那么我们这个断点呢就进来了我们来看一下啊然后呢首先呢来判断我们这个库是否存在那肯定是什么不存在的对不对然后呢我们去创建我们这个库好那我们来看一下这个碳花这个库创建好了吗是不是已经创建好了那我们可以看到呢它是不是有六个这个分片然后呢每一个分片呢都有两个备份那总共呢就有三个比如说
[01:32] 这个0呢这个0是不是备份啊这个是我们的一个组的一个这个0那总共呢会有6个这个分片啊好那么这个呢就创建好了那么接下来呢我们继续往下面走然后呢去判断我们这个所以啊这个类型是不是存在也不存在然后呢去做一个这个put的操作好那么我们再进入这个里面呢来看一下我们的一个所以那么现在呢有一个他啊然后呢我们现在呃刷新一下啊刷新一下
[01:58] 然后呢我们来看一下这个里面的一个索引的一个状态啊应该我们看索引的信息啊来看这个索引信息那么下面呢我们可以看一下我们这个mapping然后呢下面是不是有个叫做UserLocation然后呢它的一个这个属性呢有这么多啊那这个是我们的一个last update是一个long类型addressed是keyword然后呢created是long那么location呢是一个注意来看啊
[02:28] 这个type变成什么GU一个point那么这个是不是就可以去存储地理位置信息所以说这个是关键好嘞好那么我们的类型就创建好了然后往下面走去做一个查询查询存在不存在显然是不存在的那就往下面走走走走走走到这这条数据肯定就插进去了对吧
[02:50] 好那我们来刷新一下到这个里面吧浏览数据那么可以看到现在是不是有一条数据已经插入了对吧然后呢有这个比如说这个是用户ID啊然后呢这个是location的数据然后呢还有我们的一个address啊还有三个这个时间好嘞那么我们继续往下面去走啊然后呢通过吧走到下一个这个操作啊下一个插入呢就判断肯定是存在了那就不会再再次去做一个执行了
[03:17] 那么就去做下面的操作然后呢判断存在吗也是不存在的做新增啊那我们就直接通过了把这个断点呢就去掉直接通过那么然后呢就执行成功了对吧好那我们来刷新一下啊DAO杖吧直接刷新那么是不是这个数据呢就已经写入到我们的elag设置中了那么接下来呢我们针对于这个数据那么是不是就可以去做一些啊这个查询的操作了哎OK
[03:42] 好那么关于我们这个测试用力的一个这个新增的这样的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 ElasticsearchTemplate 来实现用户地理位置的增删改查功能，包括索引和类型的创建、数据的更新与查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 UserLocationService.java 文件内容，展示服务类中定义的 updateUserLocation 方法。
- 代码中包含对索引是否存在进行判断并创建索引的逻辑。
- 代码中包含对类型是否存在进行判断并创建映射的逻辑。

画面 2：
- 显示 TestUserLocationService.java 文件内容，展示测试类中定义的 testUpdateUserLocation 方法。
- 代码中包含对用户位置数据进行更新的调用，参数包括用户ID、经纬度和地址。

画面 3：
- 显示 TestUserLocationService.java 文件内容，展示测试类中定义的 testUpdateUserLocation 方法。
- 代码中包含对用户位置数据进行更新的调用，参数包括用户ID、经纬度和地址。

画面 4：
- 显示 TestUserLocationService.java 文件内容，展示测试类中定义的 testQuery 方法。
- 代码中包含对用户位置数据进行查询的逻辑，使用 GeoDistance 计算距离。

画面 5：
- 显示 TestUserLocationService.java 文件内容，展示测试类中定义的 testUpdateUserLocation 方法。
- 代码中包含对用户位置数据进行更新的调用，参数包括用户ID、经纬度和地址。

画面 6：
- 显示 TestUserLocationService.java 文件内容，展示测试类中定义的 testUpdateUserLocation 方法。
- 代码中包含对用户位置数据进行更新的调用，参数包括用户ID、经纬度和地址。

画面 7：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对索引和类型的判断与创建逻辑。
- 代码中包含对索引是否存在进行判断并创建索引的逻辑。
- 代码中包含对类型是否存在进行判断并创建映射的逻辑。

画面 8：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对索引和类型的判断与创建逻辑。
- 代码中包含对索引是否存在进行判断并创建索引的逻辑。
- 代码中包含对类型是否存在进行判断并创建映射的逻辑。

画面 9：
- 显示 Elasticsearch Head 界面，展示索引 "tanhua" 的状态和数据。
- 界面中显示了 node01、node02、node03 三个节点的状态。

画面 10：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对用户位置数据的查询逻辑。
- 代码中包含对用户位置数据进行查询的逻辑。

画面 11：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对用户位置数据的更新逻辑。
- 代码中包含对用户位置数据进行更新的逻辑。

画面 12：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对索引和类型的判断与创建逻辑。
- 代码中包含对索引是否存在进行判断并创建索引的逻辑。
- 代码中包含对类型是否存在进行判断并创建映射的逻辑。

画面 13：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对用户位置数据的更新逻辑。
- 代码中包含对用户位置数据进行更新的逻辑。

画面 14：
- 显示 UserLocationService.java 文件内容，展示 updateUserLocation 方法中对索引和类型的判断与创建逻辑。
- 代码中包含对索引是否存在进行判断并创建索引的逻辑。
- 代码中包含对类型是否存在进行判断并创建映射的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import org.springframework.data.Elasticsearch.core.ElasticsearchTemplate;
import org.springframework.data.Elasticsearch.core.query.*;
import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;

@Service
public class UserLocationService {

    @Autowired
    private ElasticsearchTemplate elasticsearchTemplate;

    public boolean updateUserLocation(Long userId, Double longitude, Double latitude, String address) {
        try {
            // 判断索引是否存在，如果不存在需要创建
            if (!this.elasticsearchTemplate.indexExists(UserLocationES.class)) {
                // 创建索引
                this.elasticsearchTemplate.createIndex(UserLocationES.class);
            }
            // 判断类型是否存在，如果不存在，需要创建
            if (!this.elasticsearchTemplate.typeExists(index: "tanhua", type: "user_location")) {
                // 创建类型
                this.elasticsearchTemplate.putMapping(UserLocationES.class);
            }
            // 判断用户的位置数据是否存在，如果存在，进行更新操作，如果不存在，插入新的数据
            GetQuery getQuery = new GetQuery();
            getQuery.setId(userId.toString());
            UserLocationES ul = this.elasticsearchTemplate.queryForObject(getQuery, UserLocationES.class);
            if (null == ul) {
                // 新增位置数据
                UserLocationES userLocationES = new UserLocationES();
                userLocationES.setAddress(address);
                userLocationES.setCreated(System.currentTimeMillis());
                userLocationES.setUpdated(System.currentTimeMillis());
                userLocationES.setUserId(userId);
                userLocationES.setLocation(new GeoPoint(latitude, longitude));
                IndexQuery indexQuery = new IndexQueryBuilder().withObject(userLocationES).build();
                this.elasticsearchTemplate.index(indexQuery);
            } else {
                // 更新位置数据
                Map<String, Object> map = new HashMap<>();
                map.put("LastUpdated", System.currentTimeMillis());
                map.put("updated", System.currentTimeMillis());
                map.put("address", address);
                userLocationES.setAddress(address);
                userLocationES.setUpdated(System.currentTimeMillis());
                userLocationES.setCreated(userLocationES.getCreated());
                userLocationES.setUserId(userId);
                userLocationES.setLocation(new GeoPoint(latitude, longitude));
                UpdateQuery updateQuery = new UpdateQueryBuilder().withObject(userLocationES).build();
                this.elasticsearchTemplate.update(updateQuery);
            }
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
```

画面 2：
```java
package com.tanhua.es.Service;

import org.Elasticsearch.common.geo.GeoDistance;
import org.Elasticsearch.common.unit.DistanceUnit;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLocationService {

    @Autowired
    private UserLocationService userLocationService;

    @Test
    public void testUpdateUserLocation() {
        this.userLocationService.updateUserLocation(1L, 121.512253, 31.24094, "金茂大厦");
        this.userLocationService.updateUserLocation(2L, 121.506377, 31.243105, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(3L, 121.508613, 31.243844, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(4L, 121.511999, 31.248844, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(5L, 121.493444, 31.247011, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(6L, 121.462452, 31.253463, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(7L, 121.61509, 31.25033, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(8L, 121.327906, 31.227831, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(9L, 121.425611, 31.207786, "东方明珠广播电视台");
        this.userLocationService.updateUserLocation(10L, 121.311999, 31.289165, "东方明珠广播电视台");
    }
}
```

画面 3：
```java
package com.tanhua.es.Service;

import org.Elasticsearch.common.geo.GeoDistance;
import org.Elasticsearch.common.unit.DistanceUnit;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLocationService {

    @Autowired
    private UserLocationService userLocationService;

    @Test
    public void testUpdateUserLocation() {
        this.userLocationService.updateUserLocation(1L, 121.512253, 31.24094, "金茂大厦");
        this.userLocation

