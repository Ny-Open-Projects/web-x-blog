# 画面线理解：09.Elasticsearch实现位置查询之编码实现（查询）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\09.Elasticsearch实现位置查询之编码实现（查询）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:22, 02:20, 04:59, 07:05, 09:03, 10:58, 12:10, 13:28, 14:57, 16:23, 17:22, 18:34, 19:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:28:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 NativeSearchQueryBuilder 构建基于地理位置的查询和排序功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 UserLocationController 中的 @GetMapping 查询用户位置的接口，以及 @PostMapping 更新用户位置的接口。代码中包含参数解析和异常处理。
画面 2: 展示了 TestLocationService 中的 testQueryById 方法，用于测试根据用户 ID 查询位置信息，并计算与给定经纬度的距离。
画面 3: 展示了 UserLocationController 中的 @PostMapping 更新用户位置的接口，以及对应的目录结构，包括 controller、service、resources 等包。
画面 4: 展示了 UserLocationService 中的 NativeSearchQueryBuilder 的 build() 方法，用于构建 NativeSearchQuery。
画面 5: 展示了 UserLocationService 中的 queryUserFromLocation 方法，开始构建 NativeSearchQueryBuilder。
画面 6: 展示了在 queryUserFromLocation 方法中，创建 GeoDistanceQueryBuilder 并设置中心点和距离范围。
画面 7: 展示了在 queryUserFromLocation 方法中，创建 BoolQueryBuilder 并将 GeoDistanceQueryBuilder 添加到其中。
画面 8: 展示了在 queryUserFromLocation 方法中，创建 GeoDistanceSortBuilder 并设置排序字段和单位。
画面 9: 展示了在 queryUserFromLocation 方法中，将 GeoDistanceSortBuilder 设置到 nativeSearchQueryBuilder 中。
画面 10: 展示了 DistanceUnit 类的源码，定义了距离单位，如 MILES 和 METERS。
画面 11: 展示了 TestLocationService 类的测试方法 testUpdateUserLocation，用于测试更新用户位置功能。
画面 12: 展示了 application.properties 文件中的配置，包括 location 路由和 proxy 相关的设置。
画面 13: 展示了 UserLocationController 中的 queryUserFromLocation 方法，包含参数解析和异常处理。
画面 14: 展示了 day10 课程笔记中关于 RestTemplate 的配置和使用，以及 UserLocationController 中的 queryUserFromLocation 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@GetMapping("userId")
public ResponseEntity<UserLocationES> queryUserLocation(@PathVariable("userId") Long userId) {
    try {
        this.userLocationService.queryUserById(userId);
        if (null == userLocationES) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        return ResponseEntity.ok(userLocationES);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}

/**
 * 更新用户的地址位置
 */
@PutMapping("update")
public ResponseEntity<UserLocationES> updateUserLocation(@RequestBody Map<String, Object> param) {
    Long userId = Long.valueOf(param.get("userId").toString());
    Double longitude = Double.valueOf(param.get("longitude").toString());
    Double latitude = Double.valueOf(param.get("latitude").toString());
    String address = param.get("address").toString();
    boolean result = this.userLocationService.updateUserLocation(userId, longitude, latitude, address);
    if (result) {
        return ResponseEntity.ok(null);
    } catch (NumberFormatException e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}
```

画面 2:
```java
public void testQueryById() {
    this.userLocationService.updateUserLocation(userId: 301, longitude: 121.462452, latitude: 31.253463);
    this.userLocationService.updateUserLocation(userId: 321, longitude: 121.815478, latitude: 31.157478);
    this.userLocationService.updateUserLocation(userId: 341, longitude: 121.327908, latitude: 31.20033);
    this.userLocationService.updateUserLocation(userId: 361, longitude: 121.490155, latitude: 31.277876);
    this.userLocationService.updateUserLocation(userId: 431, longitude: 121.594194, latitude: 31.207761);
}

@Test
public void testQuery() {
    Page<UserLocationES> userLocationPage = this.userLocationService.queryUserFromLocation(121.512253, 31.24094, 1000);
    userLocationPage.forEach(userLocationES -> {
        System.out.println(userLocationES.getLoca);
        double distance = GeoDistance.ARC.calculate(31.24094, 121.512253, userLocationES.getLoca);
        System.out.println("距离实：" + distance + "米");
    });
}
```

画面 3:
```java
@GetMapping("list")
public ResponseEntity<List<UserLocationES>> queryUserFromLocation(@RequestParam Map<String, Object> param) {
    Double longitude = Double.valueOf(param.get("longitude").toString());
    Double latitude = Double.valueOf(param.get("latitude").toString());
    Double distance = Double.valueOf(param.get("distance").toString());
    Integer page = param.get("page") == null ? 1 : Integer.valueOf(param.get("page").toString());
    Integer pageSize = param.get("pageSize") == null ? 100 : Integer.valueOf(param.get("pageSize").toString());
    Page<UserLocationES> userLocationES = this.userLocationService.queryUserFromLocation(longitude, latitude, distance, page, pageSize);
    return ResponseEntity.ok(userLocationES.getContent());
} catch (NumberFormatException e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
```

画面 4:
```java
public NativeSearchQueryBuilder withIndicesOptions(IndicesOptions indicesOptions) {
    this.indicesOptions = indicesOptions;
    return this;
}

public NativeSearchQueryBuilder build() {
    NativeSearchQuery nativeSearchQuery = new NativeSearchQuery(queryBuilder, filterBuilder, sortBuilder, highlightBuilder, highlightFields);
    nativeSearchQuery.setPageable(pageable);
    nativeSearchQuery.setTrackScores(trackScores);
    if (indices != null) {
        nativeSearchQuery.addIndices(indices);
    }
    if (types != null) {
        nativeSearchQuery.addTypes(types);
    }
    return nativeSearchQuery;
}
```

画面 5:
```java
public Page<UserLocationES> queryUserFromLocation(Double longitude, Double latitude, Double distance, Integer page, Integer pageSize) {
    // NativeSearchQueryBuilder nativeSearchQueryBuilder = new NativeSearchQueryBuilder();
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize);
    nativeSearchQueryBuilder.withPageable(pageRequest);
    // 定义bool查询
    BoolQueryBuilder boolQueryBuilder = new BoolQueryBuilder();
    return null;
}
```

画面 6:
```java
// geo查询，定义中心点，指定查询范围
GeoDistanceQueryBuilder geoDistanceQueryBuilder = new GeoDistanceQueryBuilder(fieldName);
geoDistanceQueryBuilder.point(latitude, longitude);
geoDistanceQueryBuilder.distance(distance);
```

画面 7:
```java
// geo查询，定义中心点，指定查询范围
GeoDistanceQueryBuilder geoDistanceQueryBuilder = new GeoDistanceQueryBuilder(fieldName);
geoDistanceQueryBuilder.point(latitude, longitude);
geoDistanceQueryBuilder.distance(distance / 1000, DistanceUnit.KILOMETERS);
```

画面 8:
```java
// 按照距离排序
GeoDistanceSortBuilder geoDistanceSortBuilder = new GeoDistanceSortBuilder(fieldName, latitude, longitude);
geoDistanceSortBuilder.unit(DistanceUnit.KILOMETERS); // 距离单位
```

画面 9:
```java
// 按照距离排序
GeoDistanceSortBuilder geoDistanceSortBuilder = new GeoDistanceSortBuilder(fieldName, latitude, longitude);
geoDistanceSortBuilder.unit(DistanceUnit.KILOMETERS); // 距离单位
nativeSearchQueryBuilder.sort(geoDistanceSortBuilder);
```

画面 10:
```java
// 'm' is a suffix of 'nm' so it must follow 'nm'
MILES(1609.344, "mi", "miles"),
// since 'm' is suffix of other unit
// it must be the last entry of unit
// otherwise parsing would fail
METERS(1, "m", "meters");
public static final DistanceUnit DEFAULT = METERS;
DistanceUnit(double meters, String... names) {
    this.meters = meters;
    this.names = names;
}
```

画面 11:
```java
package com.tanhua.es.service;

import com.tanhua.es.pojo.UserLocationES;
import org.elasticsearch.common.unit.DistanceUnit;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4
