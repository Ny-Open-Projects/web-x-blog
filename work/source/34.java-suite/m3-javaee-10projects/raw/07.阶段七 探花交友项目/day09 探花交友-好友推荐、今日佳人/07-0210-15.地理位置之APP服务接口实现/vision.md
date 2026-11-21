# 画面线理解：15.地理位置之APP服务接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\15.地理位置之APP服务接口实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:41, 01:02, 01:31, 02:03, 02:35, 03:00, 03:23, 03:34, 04:08, 04:45, 05:16, 05:46, 06:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:19:42

1) 这一组画面整体在讲如何通过 Spring Boot 实现一个更新用户位置的 RESTful 接口，并通过 Mock 服务和真实服务进行测试。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Mock 服务的接口文档，路径为 /baidu/location，请求头 Content-Type 为 application/json，请求体包含 latitude、longitude、addrStr 三个必填参数。
画面 2: 展示了 Typora 中的文档，标题为“6.5、实现服务接口”，并显示了 BaiduController 的 Java 代码，包含 @RestController、@RequestMapping、@Autowired 等注解。
画面 3: 展示了 IntelliJ IDEA 中 BaiduController.java 的代码，定义了 updateLocation 方法，接收 Map<String, Object> param 参数，用于解析请求体。
画面 4: 展示了 BaiduService.java 的代码，定义了 updateLocation 方法，接收 longitude、latitude、address 参数，调用 UserLocationApi 更新用户位置。
画面 5: 展示了 BaiduController.java 的代码，完善了 updateLocation 方法，将解析后的参数传递给 baiduService.updateLocation，并根据返回值决定返回 ResponseEntity.ok(null) 或 ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面 6: 展示了 DubboApplication 启动后的控制台日志，显示了服务注册成功，包括 clientConnector、org.apache.zookeeper.ClientCnx 等信息。
画面 7: 展示了 Robo ST 1.2 软件界面，显示了 user_location 集合中的文档，其中包含一个 Object 类型的 Value。
画面 8: 展示了 IntelliJ IDEA 中 BaiduController.java 的调试界面，显示了 updateLocation 方法的参数和 baiduService 的值。
画面 9: 展示了 Advanced REST Client 中发送的 POST 请求，请求体为 {"longitude": 121.51677520125, "latitude": 31.1219412243813, "addrStr": "上海"}，响应状态为 200。
画面 10: 展示了 UserLocationApiImpl.java 的代码，其中包含更新用户位置的逻辑，使用 mongoTemplate.save 和 updateFirst 方法。
画面 11: 展示了 map.yanue.net 网站，显示了多个窗口的缩略图，包括代码编辑器、数据库、地图等，下方有百度地图的广州区域。
画面 12: 展示了 IntelliJ IDEA 中 BaiduController.java 的调试界面，显示了 updateLocation 方法的参数和 baiduService 的值。
画面 13: 展示了 Typora 中的文档，标题为“6.6、测试”，并显示了测试接口的 URL http://192.168.31.99/baidu/location。
画面 14: 展示了 Typora 中的文档，标题为“6.6、测试”，并显示了测试接口的 URL http://192.168.31.99/baidu/location，请求体为 {"longitude": 121.51677520125, "latitude": 31.1219412243813, "addrStr": "上海"}，响应状态为 200。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```java
package com.tanhua.server.controller;

import com.tanhua.server.pojo.UserLocation;
import com.tanhua.server.service.BaiduService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("baidu")
public class BaiduController {

    @Autowired
    private BaiduService baiduService;
}
```

画面 3:
```java
package com.tanhua.server.controller;

import com.tanhua.server.pojo.UserLocation;
import com.tanhua.server.service.BaiduService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("baidu")
public class BaiduController {

    @Autowired
    private BaiduService baiduService;

    @PostMapping("location")
    public ResponseEntity<Void> updateLocation(@RequestBody Map<String, Object> param) {
        try {
            Double longitude = Double.valueOf(param.get("longitude").toString());
            Double latitude = Double.valueOf(param.get("latitude").toString());
            String address = param.get("addrStr").toString();
            Boolean bool = this.baiduService.updateLocation(longitude, latitude, address);
            if (bool) {
                return ResponseEntity.ok(null);
            } else {
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
            }
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}
```

画面 4:
```java
package com.tanhua.server.service;

import com.alibaba.dubbo.config.annotation.Reference;
import com.tanhua.dubbo.server.api.UserLocationApi;
import com.tanhua.server.pojo.User;
import org.springframework.stereotype.Service;

@Service
public class BaiduService {

    @Reference(version = "1.0.0")
    private UserLocationApi userLocationApi;

    public Boolean updateLocation(Double longitude, Double latitude, String address) {
        try {
            User user = UserThreadLocal.get();
            this.userLocationApi.updateUserLocation(user.getId(), longitude, latitude, address);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
```

画面 5:
```java
public ResponseEntity<Void> updateLocation(@RequestBody Map<String, Object> param) {
    try {
        Double longitude = Double.valueOf(param.get("longitude").toString());
        Double latitude = Double.valueOf(param.get("latitude").toString());
        String address = param.get("addrStr").toString();
        Boolean bool = this.baiduService.updateLocation(longitude, latitude, address);
        if (bool) {
            return ResponseEntity.ok(null);
        } else {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 6:
```
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.zookeeper.ZooKeeper : Client environment:java.version=1.8.0_181
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.zookeeper.ZooKeeper : Client environment:java.vendor=Oracle Corporation
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.zookeeper.ZooKeeper : Client environment:java.home=/usr/lib/jvm/java-8-oracle
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.zookeeper.ZooKeeper : Client environment:java.class.path=/usr/lib/jvm/java-8-oracle/lib/tools.jar:/usr/lib/jvm/java-8-oracle/lib/dt.jar
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.zookeeper.ZooKeeper : Client environment:java.library.path=/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr
