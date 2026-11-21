# 15.地理位置之APP服务接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\15.地理位置之APP服务接口实现_【海量资源尽在 666java.com】.mp4
- 时长 6分7秒（音频 368s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的Mock接口然后呢我们来实现我们的一个服务接口啊那么这个接口呢是在这个位置有一个叫做上报地理位置然后呢地址呢是这个百度有个location那就说明我们的这个APP端呢使用的是百度的这样的一个API来获取我们的一个地理位置
[00:22] 然后呢下面呢他的请求的参数呢有三个对吧然后呢是这个精度啊这个是纬度啊这个是精度然后呢这个是一个位置的一个描述啊就是我们那个比如说北京呢还是上海啊那么OK那么接下来呢我们就来看一下我们的讲义啊那么首先呢我们需要创建一个这个百度啊Controller然后呢去写这样的一个呃代码啊那么我们就直接来拷贝一下吧
[00:51] 然后我们找到我们的这个就是server然后这个下面我们要找到我们的Controller这个包Controller这个包然后我们来看一下在这个里面百度这个Controller要做百度Service然后去写一个更新位置的一个location这样的一个方法传入是一个param是一个map然后其中有三个参数然后这个是
[01:18] 这个是精度这个是纬度然后下面这个地址然后调用我们这个Service去把这三个传递过去那么基本上是比较简单的这样的一个方法那么下面我们就来实现我们的这个Service那我们把它也拷贝过来然后拷到我们这个Service里面来在这然后这个是百度Service那么这个里面的实现就比较简单了去引入我们刚刚所编写的一个UloLocation的一个API
[01:48] 然后呢我们呢去调用啊这个我们的更新这个方法传入这三个参数四个参数啊当然多了一个这个UID啊然后呢这样的话呢就OK了啊非常简单的一个编写啊这个我们就不去一一去写了那我们就直接来去把这个代码拷进来啊就可以了好嘞好那么接下来呢我们就可以来测试一下了对吧
[02:13] 那么接下来呢我们就把我们这个double接口呢服务呢以及我们这个服务呢重新启动啊那我们来测一下好那么接下来呢我们就来测一下那么还是去使用这个地址啊然后呢我们去登录一下用户提交这三个参数然后呢是它的一个就是经纬度啊这个我们写的是有点问题纬度没写啊那我们来考一下在这好嘞好那么我们去提交一下当然我们在
[02:44] 这个位置吧去打一个断点然后呢这个是12131那么我们现在的这个数据呢是我们还需要来查一下数据是多少呢Fund然后呢没有条件没有条件去做一个查询好那么我们只有一条数据那么它的一个坐标呢是116和39然后呢把它北京改成上海然后呢我们点击这个Send发送
[03:12] 然后呢断点呢就会进入到我们的这个就是打断点的位置啊然后呢我们往下走走呃拿到我们的三个这个参数呃拿到之后呢我们就去调用我们这个update这个方法然后呢往下面走去调用我们的更新啊更新就结束了然后呢return true啊那么到这呢响应的是200没有问题那么下面我们来看一下我们这个数据啊那么在我们这个数据中呢我们可以看到它是不是已经啊是
[03:42] 更新了位置对吧更新位置121和31但是我们这个这个没有更改那就说明我们刚刚写这个代码呢有点bug那我们来调一下就是刚刚我们在更新的时候呢没有把那个address呢更新上去那我们来找一下这个location的一个实现然后呢我们再去给他去set一个谁呢就是我们的一个这个address地理位置我们刚刚是没有更新他的
[04:10] 那么我们更新一下这个然后拿到这个userlocation.getaddress好那么是不是多了一个括号呀好那么这样的话呢就肯定就可以了好那我们重新来测试一下那我把这个服务呢再重新起一下好那么接下来呢我们重新来测试一下那么我们重新找一个地理位置吧比如说我们设置比如说这个广州然后呢我们去
[04:40] 解析一下好那么这个就是广州了那么它的位置是11323那么我们来修改一下这个刚刚的这个地址在这那么我们把它呢就拷过来然后呢再来一个是23这个来拷贝一下然后呢把它丢到这来那么这个地理位置呢就是谁呢我们的广州广州
[05:10] 然后呢我们去点击这个提交然后断点呢又会进入到我们这个里面来走走走那我们就直接往后走直接通过吧把断点就去掉了好我们直接来看我们的数据啊那我们去啊刷一下那么可以看到是不是地理位置已经更新了那么创建时间的没有更新但是他的一个更新时间的已经更新了啊然后呢他的location看一下坐标
[05:37] 113和23那么地理位置是不是也更新了那就说明我们现在这个接口是不是已经就搞定了那么我们的这个APP只要去定时的去上传就可以了那么我们大家需要去安装一下我们今天的资料中的这个APK那么它就会去每隔五分钟的去上传一次大家可以去测试一下
[06:02] 好那么关于我们这个地理位置的一个功能的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Boot 实现一个更新用户位置的 RESTful 接口，并通过 Mock 服务和真实服务进行测试。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Mock 服务的接口文档，路径为 /baidu/location，请求头 Content-Type 为 application/json，请求体包含 latitude、longitude、addrStr 三个必填参数。
画面 2: 展示了 Typora 中的文档，标题为“6.5、实现服务接口”，并显示了 BaiduController 的 Java 代码，包含 @RestController、@RequestMapping、@Autowired 等注解。
画面 3: 展示了 IntelliJ IDEA 中 BaiduController.java 的代码，定义了 updateLocation 方法，接收 Map<String, Object> param 参数，用于解析请求体。
画面 4: 展示了 BaiduService.java 的代码，定义了 updateLocation 方法，接收 longitude、latitude、address 参数，调用 UserLocationApi 更新用户位置。
画面 5: 展示了 BaiduController.java 的代码，完善了 updateLocation 方法，将解析后的参数传递给 baiduService.updateLocation，并根据返回值决定返回 ResponseEntity.ok(null) 或 ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面 6: 展示了 DubboApplication 启动后的控制台日志，显示了服务注册成功，包括 clientConnector、org.apache.ZooKeeper.ClientCnx 等信息。
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
package com.tanhua.server.Controller;

import com.tanhua.server.pojo.UserLocation;
import com.tanhua.server.Service.BaiduService;
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
package com.tanhua.server.Controller;

import com.tanhua.server.pojo.UserLocation;
import com.tanhua.server.Service.BaiduService;
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
package com.tanhua.server.Service;

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
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper : Client environment:java.version=1.8.0_181
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper : Client environment:java.vendor=Oracle Corporation
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper : Client environment:java.home=/usr/lib/jvm/java-8-oracle
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper : Client environment:java.class.path=/usr/lib/jvm/java-8-oracle/lib/tools.jar:/usr/lib/jvm/java-8-oracle/lib/dt.jar
2019-10-24 10:48:32.167 INFO 1100 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper : Client environment:java.library.path=/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr/lib/jvm/java-8-oracle/lib/amd64:/usr

