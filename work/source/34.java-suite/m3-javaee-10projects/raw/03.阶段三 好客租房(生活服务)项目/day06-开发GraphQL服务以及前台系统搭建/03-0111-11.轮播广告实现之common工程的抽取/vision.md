# 画面线理解：11.轮播广告实现之common工程的抽取

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\11.轮播广告实现之common工程的抽取【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 02:36, 03:18, 03:43, 04:12, 04:33, 05:05, 05:36, 06:28, 06:55, 07:16, 07:46, 08:13, 08:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:13:05

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并配置一个名为 "itcast-haoke-manage-dubbo-server-common" 的 Maven 项目模块，用于存放公共的 POJO 和 Service 接口实现，以支持 Dubbo 服务的开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目结构，当前选中模块为 "itcast-haoke-manage-dubbo-server"，并显示了 GraphQL 文件中的字段定义，如 coveredArea、floor、orientation 等。
画面 2: 在项目结构中选中了 "itcast-haoke-manage" 项目根目录。
画面 3: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了该模块的 pom.xml 文件内容，其中包含 <parent> 和 <artifactId> 等配置。
画面 4: 在项目结构中右键点击 "itcast-haoke-manage-dubbo-server-common" 模块，弹出创建新文件的菜单。
画面 5: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BasePojo.java 文件内容。
画面 6: 在项目结构中右键点击 "itcast-haoke-manage-dubbo-server-common" 模块，弹出创建新文件的菜单。
画面 7: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 8: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BaseServiceImpl.java 文件内容，其中包含 @Autowired 注解和 queryById 方法。
画面 9: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 10: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BaseServiceImpl.java 文件内容，其中包含 queryAll 方法。
画面 11: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 HouseResourcesServiceImpl.java 文件内容，其中包含 @Transactional 注解和方法参数。
画面 12: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 13: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 14: 显示了 PDF 文档 "定义.pdf" 的第 3.3.2 节，标题为“3.3.2. 创建 common 工程”，内容说明创建 "itcast-haoke-manage-dubbo-server-common" 工程，并将 BasePojo、BaseServiceImpl 移动到该工程中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```graphql
coveredArea:String
useArea:String
floor:String
orientation:String
decoration:Int
facilities:String
pic:String
houseDesc:String
contact:String
mobile:String
time:Int
propertyCost:String

type TableResult{
  list:[HouseResources]
  pagination:Pagination

type Pagination{
  current:Int
  pageSize:Int
```

画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>itcast-haoke-manage-dubbo-server</artifactId>
        <groupId>cn.itcast.haoke.manage</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
```

画面 5:
```java
package cn.itcast.haoke.dubbo.server.pojo;

import ...

@Data
public abstract class BasePojo implements java.io.Serializable {

    private Date created;
    private Date updated;
}
```

画面 6:
```java
// 代码片段未完整显示
```

画面 7:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>
```

画面 8:
```java
@Autowired
private BaseMapper<T> mapper;

/**
 * 根据id查询数据
 * @param id
 * @return
 */
public T queryById(Long id) { return this.mapper.selectById(id); }

/**
 * 查询所有数据
 * @return
 */
public List<T> queryAll() { return this.mapper.selectList(null); }
```

画面 10:
```java
@Autowired
private BaseMapper<T> mapper;

/**
 * 根据id查询数据
 * @param id
 * @return
 */
public T queryById(Long id) { return this.mapper.selectById(id); }

/**
 * 查询所有数据
 * @return
 */
public List<T> queryAll() { return this.mapper.selectList(null); }
```

画面 11:
```java
package cn.itcast.haoke.dubbo.server.service.impl;

import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.service.HouseResourcesService;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.apache.commons.lang3.StringUtils;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class HouseResourcesServiceImpl extends BaseServiceImpl<HouseResources> {

    @Override
    public HouseResources queryById(Long id) {
        if (StringUtils.isBlank(id.toString())) {
            throw new RuntimeException("输入的参数不符合要求，0：数据插入数据库失败，1：数据更新失败");
        }
        return this.baseMapper.selectById(id);
    }
}
```

画面 12:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

画面 13:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
标题：3.3.2. 创建 common 工程
内容：
- 实现独立的 dubbo 服务，便于后期的扩展和维护
- 多个 dubbo 服务，需要抽取公共的类、方法到 common 工程中
- 创建 itcast-haoke-manage-dubbo-server-common 工程，将 BasePojo、BaseServiceImpl 移动到该工程中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
