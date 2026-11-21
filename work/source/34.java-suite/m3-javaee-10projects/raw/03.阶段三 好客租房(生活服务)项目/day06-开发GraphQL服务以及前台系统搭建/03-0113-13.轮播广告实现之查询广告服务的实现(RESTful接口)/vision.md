# 画面线理解：13.轮播广告实现之查询广告服务的实现（RESTful接口）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\13.轮播广告实现之查询广告服务的实现（RESTful接口）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:11, 02:18, 03:23, 05:21, 07:46, 09:32, 10:57, 12:47, 14:28, 16:07, 17:47, 18:48, 19:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:14:41

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Dubbo 构建并注册一个提供广告服务的微服务，包括服务接口、实现类、控制器、返回结果封装以及配置文件的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Dubbo 服务提供者的配置文件 application.properties，其中定义了服务扫描包、应用名称、协议、端口和注册中心地址。
画面2：展示服务接口类 AdService.java，定义了服务方法 queryAdList。
画面3：展示服务实现类 AdServiceImpl.java，定义了 queryAdList 方法。
画面4：展示控制器类 AdController.java，定义了 @Reference 注解用于注入服务。
画面5：展示桌面文件夹，其中包含多个开发工具的快捷方式。
画面6：展示返回结果类 WebResult.java 的定义。
画面7：展示 WebResult 类中 @Data 注解和 @JsonIgnore 注解的使用。
画面8：展示 WebResult 类中 getData 方法的实现。
画面9：展示 WebResult 类中 getMeta 方法的实现。
画面10：展示 WebResult 类中静态方法 ok 的实现。
画面11：展示 AdController 类中 queryIndexAd 方法的实现。
画面12：展示 AdController 类中 queryIndexAd 方法的完整实现。
画面13：展示 PDF 讲义中关于实现 API 接口服务（RESTful 接口）的章节，包括引入依赖和编写 Controller。
画面14：展示 PDF 讲义中关于测试的章节，包括 getData 和 getMeta 方法的实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
# 服务的扫描包
dubbo.scan.basePackages = cn.itcast.haoke.dubbo.server.api

# 应用名称
dubbo.application.name = dubbo-provider-ad

# 协议以及端口
dubbo.protocol.name = dubbo
dubbo.protocol.port = 21880

# 注册中心
dubbo.registry.address = zookeeper://172.16.55.185:2181
```

画面2：
```
package cn.itcast.haoke.dubbo.api.service;

import cn.itcast.haoke.dubbo.server.api.ApiAdService;
import org.springframework.stereotype.Service;

@Service
public class AdService {
```

画面3：
```
import cn.itcast.h
import cn.itcast.h
import cn.itcast.h
import com.alibaba
import org.spring
@Service
public class AdSer
@Reference (val
private ApiAd
public PageInfoAd queryAdList(Integer type, id) {
}
```

画面4：
```
package cn.itcast.haoke.dubbo.api.controller;
import org.springframework.web.bind.annotation.*;
@Reference (jdk.nashorn.internal.ir
@RequestMapping (org.springframework.web.bind.annotation
@RestController (org.springframework.web.bind.annotation
```

画面6：
```
package cn.itcast.haoke.dubbo.api.vo;
public class WebResult {
    private Integer status;
    private String msg;
    private Stri
```

画面7：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
```

画面8：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public Map<String,Object> getData() {
        return null;
    }
```

画面9：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public Map<String,Object> getData() {
        Map<String,Object> map = new HashMap<>();
        map.put("list", list);
        return map;
    }
```

画面10：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public static WebResult ok(List<?> list) {
        return new WebResult();
    }
```

画面11：
```
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@Autowired
private AdService adService;
@GetMapping
public WebResult queryIndexAd() {
    PageInfo<Ad> adPageInfo = new PageInfo<Ad>();
    return WebResult.ok(adPageInfo);
}
```

画面12：
```
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@Autowired
private AdService adService;
@GetMapping
public WebResult queryIndexAd() {
    PageInfo<Ad> adPageInfo = new PageInfo<Ad>();
    return WebResult.ok(adPageInfo);
}
```

画面13：
```
3.4.1、引入依赖
<dependencies>
    <groupId>cn.itcast.haoke_manage</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-ad-interface</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependencies>

3.4.2、编写Controller
package cn.itcast.haoke.dubbo.api.controller;
import cn.itcast.haoke.dubbo.api.service.AdService;
```

画面14：
```
public Map<String, Object> getData() {
    HashMap<String, Object> data = new HashMap<String, Object>();
    data.put("list", this.list);
    return data;
}
public Map<String, Object> getMeta() {
    HashMap<String, Object> meta = new HashMap<String, Object>();
    meta.put("msg", this.msg);
    meta.put("status", this.status);
    return meta;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
