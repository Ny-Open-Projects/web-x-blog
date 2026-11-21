# 画面线理解：08.Elasticsearch实现位置查询之编码实现（更新用户地理位置的单元测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\08.Elasticsearch实现位置查询之编码实现（更新用户地理位置的单元测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:10, 00:25, 00:36, 00:44, 01:02, 01:19, 01:46, 02:03, 02:40, 02:47, 03:10, 03:22, 03:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:27:09

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
import org.springframework.data.elasticsearch.core.ElasticsearchTemplate;
import org.springframework.data.elasticsearch.core.query.*;
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
package com.tanhua.es.service;

import org.elasticsearch.common.geo.GeoDistance;
import org.elasticsearch.common.unit.DistanceUnit;
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
package com.tanhua.es.service;

import org.elasticsearch.common.geo.GeoDistance;
import org.elasticsearch.common.unit.DistanceUnit;
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
