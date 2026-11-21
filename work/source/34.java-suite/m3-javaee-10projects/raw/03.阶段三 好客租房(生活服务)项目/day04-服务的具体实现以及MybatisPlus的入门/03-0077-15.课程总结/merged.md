# 15.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\15.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 5分24秒（音频 325s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们对今天的内容呢给大家做一个总结啊做一个总结那么今天呢我们学了这么些内容啊那么首先呢我们学了是通过这个Docker的方式来安装了我们的MySQL对吧然后呢我们讲了一些它的一些这个衍生版啊PredCanner是什么然后呢包括它的一些安装啊部署然后呢下面呢我们讲了这个
[00:26] mybattis plus的一个入门那么其实我们可以看到它呢是一个使用的非常简单的这样的一个插件那么大大的简化了我们使用mybattis的这个框架的一个使用那么也其实也就提升了我们开发的一个效率啊OK那么具体这个内容呢就不重复了大家可以自己去去阅读一下这里面的一些内容好那么然后呢下面呢我们又去讲了它的一些什么base Mapper
[00:54] 中的一些具体的一些实现啊OK好那么我们后面也讲了一个叫让我们不可啊那么这个呢就是去实现了什么呢是就是可以帮助我们去去简化我们的加坏一些代码让我们看起来呢更清爽一点啊实际上它并不会真正的改变我们这个代码而是说让我们看起来更舒服一点啊就是这样的一个也不能说是框架了就是一个工具包了哎呀OK
[01:23] 好那么具体这个用法大家可以测试一下我们只是讲了一些他常用的注解他还有一些其他注解我们并没有讲到啊好那么后面呢我们去搭建了一个他的后台的一个服务的这样的一个系统那么这个服务系统呢我们依然采用的是double的一种服务做一个这样的一个管理哎呀ok那么这个里面需要大家搞清楚这么几个呃几个工程啊一定要搞清楚别搞混啊这个工程名呢有点长也容易搞混
[01:50] 一定要把它搞清楚那么每个字它的作用是什么它的定位是什么一定要搞清楚OK好那么我们在下面是不是就实现了新增房源的服务那么在这个里面有一个点需要大家特别的注意就是我们在去写服务的时候那么一定要区分清楚那么什么是我们的Spring的服务那么什么又是我们的Double的服务那么我们为什么要去做这样的一个区分那么这个一定要搞明白一定要搞清楚OK
[02:20] 好这个是我们这个这个是这个是我们的sprint的服务对吧你看它的实现的是这样的一个实现这样的一个实现然后呢上面这个呢是double这个服务是不一样的那么在这个位置呢是我们有一个base Service的具体的一个实现那么这个呢希望大家呢自己去把这个代码去阅读一下或者说如果你要是有时间精力的话把这个代码呢重写一下ok这样的话呢你就能够去
[02:49] 更加深刻的去理解我们为什么这样去做OK好那么我们继续往下面看那么这个呢我们就往后过了那么继续往下面看啊那么我们就实现了这个实现了我们这个double这个服务啊OK最后呢我们可以看到这个服务呢就注册到我们的注册中心了然后呢我们再去实现了一个RESTful这样的一个接口OK好那么实现了这个接口
[03:20] 好那么继续往下面看那么实现了之后我们做了这样的一个测试那么如果大家没有这个测试工具的话如果你没有安装的话那么可以去谷歌的这个ChromeChrome这个在线的商店去搜索一个REST CLIENT的工具去做一个安装就可以了OK好那么通过测试会发现这个流程是能够跑通的然后我们是不是最后就整合了一个前端去做我们的一个测试
[03:47] 那么这个前端的我们前面其实已经开发好了只是说有一些这个具体逻辑还没有去写那么我呢并没有去带着大家一点一点去写而是给大家去讲解了一些这个他的一个实现那么其实他的关键点呢就我们刚刚讲的这么几个点啊那么包括一定要理清楚他的这个model啊以及这个model以及他的这个什么呢还有这个Service他们之间是怎么去调用怎么去玩的然后呢我们在这个位置是不是重点讲了一个
[04:16] 他的一个这个反向代理来解决这个跨越的这个这个问题啊怎么样去解决那么这个代理那么等到我们去开发上线的时候是不是我们就不需要这样的一个代理了或者说我们就需要去改变他的一个这个地址就可以了哎呀OK好最后呢我们会发现前后端在整合之后那么前端是不是做自己的开发后端做开发开发完之后呢二者一整合发现哎OK这个结果是能跑通的好那么
[04:44] 这个呢就是我们实现的一个新增房源的这样的一个效果最后我们就可以看到数据是不是已经保存到我们的数据库了OK好那么关于我们今天内容呢我们就这么多那么我们今天这个内容呢其实需要大家动手的内容是比较多的啊我们其实讲解的部分可能会有些有些点吧就我们就会直接就会去过啊那么也希望大家在做的过程中你就会发现有一些
[05:13] 有一些细节的一些点OK好那么如果在学习过程中有什么一些问题那就及时给予这个反馈好那么今天内容我们就先讲到这里了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Docker 安装 MySQL 数据库、使用 MyBatis-Plus 快速开发并集成前端系统，实现一个房源管理的完整流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解使用 Docker 安装 MySQL，介绍 Percona Server 版本，并给出拉取镜像和创建容器的命令。
画面 2: 展示 MyBatis-Plus 的架构图，说明其核心组件和功能，同时提示创建数据库 haoke。
画面 3: 介绍 Lombok 的作用和配置方法，给出 Maven 依赖的 XML 代码。
画面 4: 展示使用 Lombok 注解简化 Java POJO 类的代码，例如 Item 类。
画面 5: 展示数据库表 tb_house_resources 的建表语句和部分数据。
画面 6: 展示 Spring Boot 项目结构，包含 Controller 层的 save 和 get 方法。
画面 7: 展示 Service 层的 save 方法，包含参数校验和调用父类 save 方法。
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
#镜像地址: https://hub.Docker.com//percona/
#拉取镜像
Docker pull percona:5.7.23
#创建容器
Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
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
    return this.Mapper.insert(record);
}
public Integer update(T record) {
    record.setUpdated(new Date());
    return this.Mapper.updateById(record);
}
public Integer deleteById(Long id) { return this.Mapper.deleteById(id); }
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

