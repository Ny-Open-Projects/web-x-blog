# 画面线理解：11_后端通用封装-通用service-接口定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\11_后端通用封装-通用service-接口定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:28, 00:58, 01:28, 02:15, 02:23, 03:09, 03:24, 03:55, 04:11, 04:30, 04:42, 05:50, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:05:08

1) 这一组画面整体在讲什么（一句话）：
演示如何创建通用的 DAO 和 Service 接口及其实现类，用于处理 CRUD 操作，并集成分页、条件查询等通用功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CommonDao 接口的定义，包含分页查询、统计、条件查询等方法，使用 MyBatis 的动态 SQL。
画面 2: 展示了 CommonService 接口的定义，包含 list、update、delete 方法，用于业务逻辑处理。
画面 3: 展示了 CommonDao.java 文件中的完整方法定义，包括查询、统计、更新、删除等 SQL 模板。
画面 4: 展示了 CommonService.java 文件的开头部分，包含包声明和接口定义。
画面 5: 展示了 CommonService.java 文件中 list 方法的定义，注释说明其功能。
画面 6: 展示了 CommonService.java 文件中 update 方法的定义，注释说明其功能。
画面 7: 展示了 CommonService.java 文件中 delete 方法的定义，注释说明其功能。
画面 8: 展示了 CommonService.java 文件中 delete 方法的定义，注释说明其功能。
画面 9: 展示了在 IDEA 中创建 CommonServiceImpl 类的对话框。
画面 10: 展示了 CommonServiceImpl.java 文件的初始结构，包含 list、update、delete 方法的空实现。
画面 11: 展示了 CommonServiceImpl.java 文件中注入 CommonDao 的代码。
画面 12: 展示了课程 PPT 中关于辅助方法和接口方法的说明，包括 parseValue、doFilter、getWhere、getSets、getInsertSql 等方法。
画面 13: 展示了 CommonServiceImpl.java 文件中添加了 @Service 注解和 ApplicationContext 的代码。
画面 14: 展示了 CommonServiceImpl.java 文件中 list 方法的实现，返回 null。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// 如果在mycat分库分表的情况下，可以使用多个方法完成不同分片策略的链接kuoo，这里展示为常用的查询，即非复合分片的SQL实现
// Mapper
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(@Param("tableName") String tableName, @Param("start") int start, @Param("size") int size);

    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(@Param("tableName") String tableName);

    @Select("select * from ${tableName} where 1=1 ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(@Param("tableName") String tableName, @Param("where") String where);

    @Select("select count(*) from ${tableName} where 1=1 ${where}")
    @ResultType(Integer.class)
    int listCountWhere(@Param("tableName") String tableName, @Param("where") String where);
}
```

画面 3:
```java
@Select("select * from ${tableName} where 1=1 ${where} limit #{start},#{size}")
@ResultType(HashMap.class)
List<HashMap> listWhere(@Param("tableName") String tableName, @Param("where") String where);

@Select("select * from ${tableName} where 1=1 ${where}")
@ResultType(Integer.class)
int listCountWhere(@Param("tableName") String tableName, @Param("where") String where);

@Select("update ${tableName} set ${sets} where 1=1 ${where}")
@ResultType(Integer.class)
int update(@Param("tableName") String tableName, @Param("sets") String sets, @Param("where") String where);

@Select("insert into ${tableName} (${fields}) values (${values})")
@ResultType(Integer.class)
int insert(@Param("tableName") String tableName, @Param("fields") String fields, @Param("values") String values);

@Select("delete from ${tableName} where 1=1 ${where} limit 1")
@ResultType(Integer.class)
int delete(@Param("tableName") String tableName, @Param("where") String where);
```

画面 4:
```java
package com.heima.admin.service;
```

画面 5:
```java
public ResponseResult list(CommonDto dto);
```

画面 6:
```java
public ResponseResult update(CommonDto dto);
```

画面 7:
```java
public ResponseResult delete(CommonDto dto);
```

画面 10:
```java
public class CommonServiceImpl implements CommonService {
    @Override
    public ResponseResult list(CommonDto dto) {
        return null;
    }

    @Override
    public ResponseResult update(CommonDto dto) {
        return null;
    }

    @Override
    public ResponseResult delete(CommonDto dto) {
        return null;
    }
}
```

画面 11:
```java
@Service
public class CommonServiceImpl implements CommonService {
    @Autowired
    private CommonDao commonDao;
```

画面 12:
```java
// 辅助方法
- parseValue: 方法通过字段和值注入到SQL中，注释的value都需要过滤
- doFilter: 用于根据name查找对应后置处理器，如果查询，则执行对应处理器的处理
- getWhere: 拼接where子句字符串，支持like、between、等条件拼接
- getSets: 拼接修改的set子句的值
- getInsertSql: 拼接新增的sql的字段和值字符串

// 接口方法
- delete: 方法必须有查询条件，删除成功之后执行doFilter方法后置处理
- update: 方法通过mode参数判断是新增还是修改，并检查对应的必要参数后调用对应方法
    - addData: 判断数据后，调用数据插入方法，插入成功之后再调用后置处理
    - updateData: 判断数据后，调用更新方法，修改成功后，再调用后置处理方法
- list: 方法判断权限后，计算分页参数和查询条件，并获取列表和总的条数，最后调用后置方法
```

画面 13:
```java
@Service
public class CommonServiceImpl implements CommonService {
    @Autowired
    private CommonDao commonDao;
    ApplicationContext context;
```

画面 14:
```java
@Override
public ResponseResult list(CommonDto dto) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12: PPT 标题为“【辅助方法】”和“【接口方法】”，内容包括 parseValue、doFilter、getWhere、getSets、getInsertSql 等辅助方法的说明，以及 delete、update、list 等接口方法的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
