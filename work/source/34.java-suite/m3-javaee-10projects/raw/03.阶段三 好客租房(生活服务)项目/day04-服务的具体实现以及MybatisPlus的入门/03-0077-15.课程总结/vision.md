# 画面线理解：15.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\15.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:45, 00:58, 01:23, 02:01, 02:16, 02:28, 02:48, 03:10, 03:25, 03:44, 04:09, 04:44, 04:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:49:20

1) 这一组画面整体在讲如何使用 Docker 安装 MySQL 数据库、使用 MyBatis-Plus 快速开发并集成前端系统，实现一个房源管理的完整流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解使用 Docker 安装 MySQL，介绍 Percona Server 版本，并给出拉取镜像和创建容器的命令。
画面 2: 展示 MyBatis-Plus 的架构图，说明其核心组件和功能，同时提示创建数据库 haoke。
画面 3: 介绍 Lombok 的作用和配置方法，给出 Maven 依赖的 XML 代码。
画面 4: 展示使用 Lombok 注解简化 Java POJO 类的代码，例如 Item 类。
画面 5: 展示数据库表 tb_house_resources 的建表语句和部分数据。
画面 6: 展示 Spring Boot 项目结构，包含 controller 层的 save 和 get 方法。
画面 7: 展示 service 层的 save 方法，包含参数校验和调用父类 save 方法。
画面 8: 展示 baseService 中的 save、update、deleteById 方法。
画面 9: 讲解实现 RESTful 接口需要添加的依赖，给出 Maven 依赖的 XML 代码。
画面 10: 展示使用 Postman 发送 POST 请求的界面，设置 Content-Type 为 application/json。
画面 11: 展示前端页面中缺少的“房源标题”字段，给出需要补充的表单代码。
画面 12: 展示前端项目目录结构，重点是 models 文件夹下的 form.js 文件。
画面 13: 展示前端页面的表单，包含租金、支付方式、户型、建筑面积等字段。
画面 14: 展示数据库中插入的数据，确认数据已成功写入。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```
#镜像地址: https://hub.docker.com//percona/
#拉取镜像
docker pull percona:5.7.23
#创建容器
docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
```

画面 3:
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
    <version>1.18.4</version>
</dependency>
```

画面 4:
```java
package cn.itcast.mybatisplus.pojo;
import lombok.Data;
@Data
public class Item {
    private Long id;
    private String title;
    private Long price;
}
```

画面 5:
```sql
INSERT INTO tb_estate (id, name, province, city, 'area', 'address', year, type, property_cost, 'name', 'province', 'city', 'area', 'address', 'updated') VALUES ('1005', '上海阳城', '上海市', '上海市', '闵行区', '罗锦路888弄', '2018', '2', '1000', '上海阳城', '上海市', '上海市', '闵行区', '罗锦路888弄', '2018-11-06 23:23:53');
CREATE TABLE tb_house_resources (
    id bigint(20) NOT NULL AUTO_INCREMENT,
    title varchar(100) DEFAULT NULL COMMENT '房源标题',
    estate_id bigint(20) DEFAULT NULL COMMENT '楼盘id',
    building_num tinyint(1) DEFAULT NULL COMMENT '楼号',
    building_unit varchar(20) DEFAULT NULL COMMENT '门牌号',
    building_floor_num varchar(10) DEFAULT NULL COMMENT '楼层',
    rent_method tinyint(1) DEFAULT NULL COMMENT '租借方式，1-整租，2-合租',
    payment_method tinyint(1) DEFAULT NULL COMMENT '支付方式，1-付一押一，2-付二押一，3-付三押一，4-付四押一，5-付五押一',
    house_type varchar(255) DEFAULT NULL COMMENT '户型，如：2室1厅1卫',
    covered_area varchar(10) DEFAULT NULL COMMENT '建筑面积',
    use_area varchar(10) DEFAULT NULL COMMENT '使用面积',
    floor varchar(10) DEFAULT NULL COMMENT '楼层，如：8/26',
    orientation varchar(10) DEFAULT NULL COMMENT '朝向，如：东、南、西、北',
    decoration tinyint(1) DEFAULT NULL COMMENT '装修，1-精装，2-简装，3-毛坯',
    facilities tinyint(50) DEFAULT NULL COMMENT '配套设施，如：1,2,3',
    pic varchar(200) DEFAULT NULL COMMENT '图片，最多3张'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 6:
```java
public ResponseEntity<Void> save(@RequestBody HouseResource houseResource) {
    boolean bool = this.houseResourcesService.save(houseResource);
    if (!bool) {
        return ResponseEntity.status(HttpStatus.CREATED).body(null);
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
}
```

画面 7:
```java
@Transactional
@Service
public class HouseResourcesServiceImpl extends BaseServiceImpl {
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        if (StringUtils.isBlank(houseResources.getTitle())) {
            return -1;
        }
        return super.save(houseResources);
    }
}
```

画面 8:
```java
public Integer save(T record) {
    record.setCreated(new Date());
    record.setUpdated(new Date());
    return this.mapper.insert(record);
}
public Integer update(T record) {
    record.setUpdated(new Date());
    return this.mapper.updateById(record);
}
public Integer deleteById(Long id) { return this.mapper.deleteById(id); }
```

画面 9:
```xml
<dependency>
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面 10:
```
application/json
```

画面 11:
```html
<FormItem {...itemLayout} label="房源标题">
    {getFieldDecorator('title', {
        rules: [{ required: true, message: '此为必填项' }]
    })(
        <Input style={{ width: '100%' }} />
    )}
</FormItem>
```

画面 12:
```
pages
├── .umi
├── Account
├── Dashboard
├── Exception
├── Forms
├── FangDong
├── Finance
├── HeYue
└── House
    └── models
        ├── form.js
        └── AddResource.js
```

画面 13:
```
租金：2000 元/月
支付方式：付一押一
租赁方式：整租
户型：2 室 1 厅 1 卫 1 厕 1 阳台
建筑面积：80 平米
使用面积：60 平米
楼层：第 5 层 总 10 层
```

画面 14:
```
id | 开始事务 | estate_id | building_num | building_floor_num | rent
1 | 豪华地段，品质小区 | 1001 | 12 | 2 | 603 | 1900
2 | 豪华地段，品质小区 | 1002 | 1 | 2 | 603 | 1900
3 | 东方曼哈顿 3室2厅 16 | 1005 | 2 | 1 | 1 | 1111
4 | 东方曼哈顿 3室2厅 16 | 1005 | 2 | 1 | 1 | 1111
5 | 东方曼哈顿 3室2厅 16 | 1005 | 2 | 1 | 1 | 1111
6 | 东方曼哈顿 3室2厅 16 | 1002 | 1 | 2 | 3 | 2000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 2: 架构图，MyBatis-Plus 核心模块包括：Scan Entity → Reflection extraction → Analysis Table Name Column → SQL: Insert Delete Select ... → Injection MyBatis Container。右侧模块包括：mybatis-plus-boot-starter → annotation, extension, core, generator。
画面 5: 表格数据，展示 tb_house_resources 表的结构和部分数据。
画面 14: 表格数据，展示数据库中插入的数据，包含 id、estate_id、building_num、building_floor_num、rent 等字段。

5) 无。
