# 画面线理解：02.搜附近功能实现之编写dubbo接口

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\02.搜附近功能实现之编写dubbo接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:32, 04:21, 05:05, 05:39, 06:43, 07:31, 09:37, 10:58, 11:54, 12:44, 13:30, 14:15, 15:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:21:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在基于 Dubbo 的服务中，使用 MongoDB 实现根据用户 ID 查询附近好友的地理位置功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“搜附近”功能的 UI 效果，提示“您附近有25个好友”。
画面2：展示代码编辑器中 UserLocationVo 类的定义，注释说明“由于UserLocation不能序列化，所以要再定义UserLocationVo进行返回数据”，并列出导入的包。
画面3：展示 UserLocationVo 类的 format 方法，用于将 UserLocation 对象转换为 UserLocationVo 对象。
画面4：展示 UserLocationVo 类的 format 方法，与画面3内容一致。
画面5：展示 UserLocationApiImpl 类中的 save 方法和 queryById 方法，其中 queryById 方法返回 null。
画面6：在 queryById 方法中，使用 CriteriaDefinition 构建查询条件。
画面7：在 queryById 方法中，调用 format 方法转换返回值。
画面8：展示一个绘图软件界面，用于演示地理围栏的圆形区域。
画面9：在 queryUserFromLocation 方法中，创建 GeoJsonPoint 对象。
画面10：在 queryUserFromLocation 方法中，创建 Distance 对象。
画面11：在 queryUserFromLocation 方法中，创建 Circle 对象。
画面12：在 queryUserFromLocation 方法中，使用 Query.query(Criteria.where()) 构建查询。
画面13：在 queryUserFromLocation 方法中，使用 this.mongoTemplate.find(d) 执行查询。
画面14：在 queryUserFromLocation 方法中，返回 UserLocationVo.formatToList(userLocations)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
```

画面3：
```java
public static final UserLocationVo format(UserLocation userLocation) {
    UserLocationVo userLocationVo = new UserLocationVo();
    userLocationVo.setAddress(userLocation.getAddress());
    userLocationVo.setCreated(userLocation.getCreated());
    userLocationVo.setUpdated(userLocation.getUpdated());
    userLocationVo.setUserId(userLocation.getUserId());
    userLocationVo.setLongitude(userLocation.getLocation().getX());
    userLocationVo.setLatitude(userLocation.getLocation().getY());
    return userLocationVo;
}

public static List<UserLocationVo> formatToList(List<UserLocation> userLocations) {
    List<UserLocationVo> list = new ArrayList<>();
    for (UserLocation userLocation : userLocations) {
        list.add(format(userLocation));
    }
    return list;
}
```

画面5：
```java
userLocation.setCreated(System.currentTimeMillis());
userLocation.setUpdated(userLocation.getCreated());
this.mongoTemplate.save(userLocation);
return userLocation.getId().toHexString();
```

画面6：
```java
CriteriaDefinition criteriaDefinition
```

画面7：
```java
return UserLocationVo.format(userLocation);
```

画面9：
```java
GeoJsonPoint geoJsonPoint = new GeoJsonPoint(longitude, latitude);
```

画面10：
```java
Distance distance = new Distance(value / 1000, Metrics.KILOMETERS);
```

画面11：
```java
Circle circle = new Circle(geoJsonPoint, distance);
```

画面12：
```java
Query query = Query.query(Criteria.where(...));
```

画面13：
```java
this.mongoTemplate.find(d)
```

画面14：
```java
return UserLocationVo.formatToList(userLocations);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：展示一个绘图软件界面，用于演示地理围栏的圆形区域，没有标题或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
