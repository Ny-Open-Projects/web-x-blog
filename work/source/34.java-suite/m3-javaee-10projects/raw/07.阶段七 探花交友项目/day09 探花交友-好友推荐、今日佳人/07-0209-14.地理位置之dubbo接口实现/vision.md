# 画面线理解：14.地理位置之dubbo接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\14.地理位置之dubbo接口实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:01, 05:02, 06:19, 07:04, 08:00, 09:10, 10:14, 11:24, 12:30, 13:15, 14:00, 15:10, 16:01, 17:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:18:44

1) 这一组画面整体在讲什么（一句话）：
实现一个用户地理位置服务，包括定义POJO、编写服务接口与实现、以及编写单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“day09 讲义.md”中“5. 地理位置”章节的“6.1. 定义pojo”部分，代码中定义了UserLocation类，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面2：在IDE中右键点击UserLocationApi.java文件，弹出菜单，显示“Delete”选项，准备删除该文件。
画面3：在UserLocationApiImpl.java中，使用@Autowired注入MongoTemplate，并定义了setLocation、setUserId、setAddress、setLastUpdated、setCreated、setUpdated、setId等方法。
画面4：在UserLocationApiImpl.java中，光标位于setCreated方法上，显示其方法签名。
画面5：在UserLocation.java中，定义了UserLocation类，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面6：在UserLocationApiImpl.java中，编写了查询用户位置的代码，使用Query.query(Criteria.where("userId").is(userId))查询，并在查询结果为null时创建新对象并保存。
画面7：在UserLocationApiImpl.java中，光标位于this.mongoTemplate上，显示其类型为MongoTemplate。
画面8：在UserLocation.java中，再次展示UserLocation类的定义，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面9：在UserLocationApiImpl.java中，编写了更新用户位置的代码，使用Update.update("location", userLocation.getLocation()).set("updated", System.currentTimeMillis()).set("lastUpdated", ul.getLastUpdated())更新，并使用this.mongoTemplate.updateFirst(query, update, UserLocation.class)执行更新。
画面10：在IDE中，弹出“Create New Class”对话框，准备创建新类。
画面11：在TestUserLocation.java中，使用@RunWith(SpringJUnit4ClassRunner.class)和@SpringBootTest注解，定义了测试类。
画面12：在网页中，显示了“map.yanue.net”网站，包含多个截图和地图。
画面13：在IDE中，调试器显示了UserLocationApiImpl类的updateUserLocation方法的执行过程，变量包括userId、longitude、latitude、userLocation等。
画面14：在课程文档“day09 讲义.md”中，展示“6.4. mock接口”部分，包含接口地址、请求参数、Headers和Body等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhu.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.geo.GeoJsonPoint;
import org.springframework.data.mongodb.core.index.CompoundIndex;
import org.springframework.data.mongodb.core.mapping.Document;
import java.io.Serializable;
@Document(collection = "user_location")
@CompoundIndex(name = "location_index", def = "{ 'location' : '2dsphere' }")
public class UserLocation implements java.io.Serializable {
    private static final long serialVersionUID = 4508668382007529970L;
    @Id
    private ObjectId id;
    @Indexed
    private Long userId; //用户id
    private GeoJsonPoint location; //x:经度 y:纬度
    private String address; //位置描述
    private Long created; //创建时间
    private Long updated; //更新时间
    private Long lastUpdated; //上次更新时间
}
```

画面3：
```java
import com.alibaba.dubbo.config.annotation.Service;
import com.tanhu.dubbo.server.pojo.UserLocation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
@Service(version = "1.0.0")
public class UserLocationApiImpl implements UserLocationApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public String updateUserLocation(Long userId, Double longitude, Double latitude) {
        UserLocation userLocation = new UserLocation();
        userLocation.setAddress(address);
        userLocation.setUserId(userId);
        userLocation.setLocation(new GeoJsonPoint(longitude, latitude));
        // 查询用户的地理位置
        Query query = Query.query(Criteria.where("userId").is(userId));
        UserLocation ul = this.mongoTemplate.findOne(query, UserLocation.class);
        if(null == ul) {
            //新增用户位置数据
            userLocation.setId(ObjectId.get());
            userLocation.setCreated(System.currentTimeMillis());
            userLocation.setLastUpdated(userLocation.getCreated());
            this.mongoTemplate.save(userLocation);
            return userLocation.getId().toHexString();
        } else {
            //更新
            Update update = Update.update("location", userLocation.getLocation())
                    .set("updated", System.currentTimeMillis())
                    .set("lastUpdated", ul.getLastUpdated());
            this.mongoTemplate.updateFirst(query, update, UserLocation.class);
            return ul.getId().toHexString();
        }
    }
}
```

画面5：
```java
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "user_location")
@CompoundIndex(name = "location_index", def = "{ 'location' : '2dsphere' }")
public class UserLocation implements java.io.Serializable {
    private static final long serialVersionUID = 4508668382007529970L;
    @Id
    private ObjectId id;
    @Indexed
    private Long userId; //用户id
    private GeoJsonPoint location; //x:经度 y:纬度
    private String address; //位置描述
    private Long created; //创建时间
    private Long updated; //更新时间
    private Long lastUpdated; //上次更新时间
}
```

画面6：
```java
// 查询用户的地理位置
Query query = Query.query(Criteria.where("userId").is(userId));
UserLocation ul = this.mongoTemplate.findOne(query, UserLocation.class);
if(null == ul) {
    //新增用户位置数据
    userLocation.setId(ObjectId.get());
    userLocation.setCreated(System.currentTimeMillis());
    userLocation.setLastUpdated(userLocation.getCreated());
    this.mongoTemplate.save(userLocation);
    return userLocation.getId().toHexString();
} else {
    //更新
    Update update = Update.update("location", userLocation.getLocation())
            .set("updated", System.currentTimeMillis())
            .set("lastUpdated", ul.getLastUpdated());
    this.mongoTemplate.updateFirst(query, update, UserLocation.class);
    return ul.getId().toHexString();
}
```

画面9：
```java
// 更新
Update update = Update.update("location", userLocation.getLocation())
        .set("updated", System.currentTimeMillis())
        .set("lastUpdated", ul.getLastUpdated());
this.mongoTemplate.updateFirst(query, update, UserLocation.class);
return ul.getId().toHexString();
```

画面11：
```java
package com.tanhu.dubbo.server.api;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLocation {
    @Test
    public void test() {
        // 测试代码
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5. 地理位置”，子标题为“6.1. 定义pojo”。
画面14：PPT标题为“6.4. mock接口”，包含接口地址、请求参数、Headers和Body等信息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
