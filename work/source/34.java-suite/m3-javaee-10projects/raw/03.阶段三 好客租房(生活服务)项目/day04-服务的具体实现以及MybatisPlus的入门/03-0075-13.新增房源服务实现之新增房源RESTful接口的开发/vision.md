# 画面线理解：13.新增房源服务实现之新增房源RESTful接口的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\13.新增房源服务实现之新增房源RESTful接口的开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:11, 01:52, 02:25, 03:22, 04:03, 04:58, 05:46, 06:40, 07:16, 07:43, 08:30, 09:52, 10:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:47:44

1) 这一组画面整体在讲一个基于 Spring Boot 和 Dubbo 的房屋资源管理系统的后端开发流程，包括项目结构、依赖配置、服务层与控制层代码编写及数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 IntelliJ IDEA 中项目结构，选中模块 "itcast-haoke-manage-api-server"。
画面2: 显示 pom.xml 文件内容，其中包含 Spring Boot Web 依赖和 Dubbo 服务依赖。
画面3: 在项目结构中选中 "resources" 目录。
画面4: 显示 HouseResourcesService.java 服务层代码，包含 @Reference 注解和 save 方法。
画面5: 在项目结构中选中 "controller" 包。
画面6: 显示 HouseResourcesController.java 控制器代码，包含 @PostMapping 和 try-catch 块。
画面7: 显示 HouseResourcesController.java 控制器代码，包含 @Autowired 注解和 save 方法。
画面8: 显示 application.properties 文件为空。
画面9: 显示 DubboApiApplication.java 启动类代码，包含 @SpringBootApplication 注解。
画面10: 浏览器显示 Google 主页，地址栏中显示 "127.0.0.1:3000"。
画面11: 显示 HouseResourcesController.java 控制器代码，包含 @GetMapping 和 get 方法。
画面12: 显示 EditPlus 编辑器中的 SQL 语句，包含创建 tb_estate 和 tb_house_resources 表的语句。
画面13: 显示 PDF 文档中测试数据，包含房屋资源的 URL 和 JSON 数据。
画面14: 显示 PDF 文档中 5.3 节内容，包含 HouseResourcesController 的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>itcast-haoke-manage</artifactId>
        <groupId>cn.itcast.haoke.manage</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-api-server</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>cn.itcast.haoke.manage</groupId>
            <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>
</project>
```

画面4:
```java
package cn.itcast.haoke.dubbo.api.service;
import cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import com.alibaba.dubbo.config.annotation.Reference;
import org.springframework.stereotype.Service;

@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }
}
```

画面6:
```java
package cn.itcast.haoke.dubbo.api.controller;
import cn.itcast.haoke.dubbo.api.service.HouseResourcesService;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Controller
@RequestMapping("house/resources")
public class HouseResourcesController {
    @Autowired
    private HouseResourcesService houseResourcesService;

    @PostMapping
    public ResponseEntity<Void> save(@RequestBody HouseResources houseResources) {
        try {
            boolean bool = this.houseResourcesService.save(houseResources);
            if (bool) {
                return ResponseEntity.status(HttpStatus.CREATED).build();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面12:
```sql
CREATE TABLE `tb_estate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL COMMENT '楼盘名称',
  `province` varchar(10) DEFAULT NULL COMMENT '所在省',
  `city` varchar(10) DEFAULT NULL COMMENT '所在市',
  `area` varchar(10) DEFAULT NULL COMMENT '具体地址',
  `year` varchar(10) DEFAULT NULL COMMENT '建筑年代',
  `type` varchar(10) DEFAULT NULL COMMENT '物业类型',
  `property_cost` varchar(10) DEFAULT NULL COMMENT '物业费',
  `developers` varchar(20) DEFAULT NULL COMMENT '开发商',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `updated` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=utf8 COMMENT='楼盘表';

-- 初始化数据
INSERT INTO `tb_estate` (`id`, `name`, `province`, `city`, `area`, `year`, `type`, `property_cost`, `developers`, `created`, `updated`) VALUES
(1, '东方曼哈顿', '北京', '北京', '朝阳区', '2010', '住宅', '3.5', '东方地产', '2010-01-01 00:00:00', '2010-01-01 00:00:00'),
(2, '东方曼哈顿', '北京', '北京', '朝阳区', '2010', '住宅', '3.5', '东方地产', '2010-01-01 00:00:00', '2010-01-01 00:00:00');

CREATE TABLE `tb_house_resources` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL COMMENT '房源标题',
  `estate_id` bigint(20) DEFAULT NULL COMMENT '楼盘ID',
  `building_num` varchar(5) DEFAULT NULL COMMENT '楼号（栋）',
  `building_unit` varchar(5) DEFAULT NULL COMMENT '单元号',
  `building_floor_num` varchar(5) DEFAULT NULL COMMENT '楼层',
  `front` int(10) DEFAULT NULL COMMENT '租金',
  `rent_method` varchar(10) DEFAULT NULL COMMENT '租凭方式，1-整租，2-合租',
  `covered_area` varchar(10) DEFAULT NULL COMMENT '面积',
  `use_area` varchar(10) DEFAULT NULL COMMENT '使用面积',
  `orientation` varchar(10) DEFAULT NULL COMMENT '朝向',
  `facilities` varchar(10) DEFAULT NULL COMMENT '设施',
  `rent` int(10) DEFAULT NULL COMMENT '租金',
  `property_cost` varchar(10) DEFAULT NULL COMMENT '物业费',
  `floor` varchar(10) DEFAULT NULL COMMENT '楼层',
  `housetype` varchar(10) DEFAULT NULL COMMENT '房屋类型',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `updated` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=utf8 COMMENT='房源表';
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面13:
标题：测试数据
数据：
url: http://127.0.0.1:18080/house/resources
数据：
{
  "title": "东方曼哈顿 3室2厅 16000",
  "buildingNum": "2",
  "buildingUnit": "1",
  "rent": "111",
  "paymentMethod": "1",
  "coveredArea": "2",
  "useArea": "2",
  "orientation": "南",
  "facilities": "1,2,3,8,9",
  "houseDesc": "这个楼盘人很懒，没有核心卖点",
  "rent": "1111111111",
  "img": "http://127.0.0.1:18080/house/resources/1.jpg",
  "propertyCost": "11",
  "floor": "1/2",
  "housetype": "1",
  "estateId": "1005"
}

5) 无
