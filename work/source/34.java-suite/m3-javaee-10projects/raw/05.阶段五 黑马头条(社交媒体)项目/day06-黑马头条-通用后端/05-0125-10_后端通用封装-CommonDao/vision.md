# 画面线理解：10_后端通用封装-CommonDao

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\10_后端通用封装-CommonDao【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:49, 01:32, 03:02, 04:02, 04:52, 05:44, 07:51, 09:12, 10:36, 11:27, 13:02, 14:01, 14:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:04:21

1) 这一组画面整体在讲什么（一句话）：
创建并编写一个通用的 MyBatis DAO 接口 CommonDao，用于支持分页查询、统计、条件查询和增删改等通用数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程大纲中“4.6 CommonDao”章节，说明要创建 CommonDao 接口，使用注解方式提供通用的列表查询和增删改功能，并使用 #{...} 拼接字符串方式，生成动态的 SQL 语句。
画面 2: 在 IDEA 中，通过“Create New Class”对话框，创建名为 “dao.CommonDao” 的新 Java 类。
画面 3: 在 CommonDao.java 文件中，开始编写接口定义，导入必要的包，如 java.util.HashMap, java.util.List。
画面 4: 继续编写接口，添加了 @Mapper 注解，并定义了第一个方法：List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size)。
画面 5: 在方法定义中，使用 @Select 注解，编写了 SQL 语句：select * from ${tableName} limit #{start},#{size}。
画面 6: 为方法添加了 @ResultType(HashMap.class) 注解，指定返回值类型。
画面 7: 继续编写接口，添加了第二个方法：int listCount(String tableName)。
画面 8: 为 listCount 方法添加了 @Select 注解，编写了 SQL 语句：select count(*) from ${tableName}。
画面 9: 为 listCount 方法添加了 @ResultType(Integer.class) 注解，指定返回值类型。
画面 10: 继续编写接口，添加了第三个方法：List<HashMap> listWhere(String tableName, @Param("where") String where, @Param("start") int start, @Param("size") int size)。
画面 11: 为 listWhere 方法添加了 @Select 注解，编写了 SQL 语句：select * from ${tableName} where 1=1 and ${where} limit #{start},#{size}。
画面 12: 为 listWhere 方法添加了 @ResultType(HashMap.class) 注解，指定返回值类型。
画面 13: 继续编写接口，添加了第四个方法：int update(String tableName, @Param("where") String where, @Param("sets") String sets)。
画面 14: 为 update 方法添加了 @Update 注解，编写了 SQL 语句：update ${tableName} set ${sets} where ${where}。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
4.6 CommonDao
创建com.heima.admin.dao.CommonDao类，使用注解方式提供通用的列表查询和增删改功能，并使用#{...}拼接字符串方式，生成动态的SQL语句。
```

画面 2:
```
Create New Class
Name: dao.CommonDao
Kind: Class
```

画面 3:
```
package com.heima.admin.dao;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
```

画面 4:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
```

画面 5:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select
```

画面 6:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select
    @ResultType(Integer.class)
    int listCount(String tableName);
```

画面 7:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select
```

画面 8:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select("select * from ${tableName} where 1=1 and ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(String tableName, @Param("where") String where, @Param("start") int start, @Param("size") int size);
```

画面 9:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select("select * from ${tableName} where 1=1 and ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(String tableName, @Param("where") String where, @Param("start") int start, @Param("size") int size);
    @Update
```

画面 10:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select("select * from ${tableName} where 1=1 and ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(String tableName, @Param("where") String where, @Param("start") int start, @Param("size") int size);
    @Update("update ${tableName} set ${sets} where ${where}")
    @ResultType(Integer.class)
    int update(String tableName, @Param("where") String where, @Param("sets") String sets);
```

画面 11:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select("select * from ${tableName} where 1=1 and ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(String tableName, @Param("where") String where, @Param("start") int start, @Param("size") int size);
    @Update("update ${tableName} set ${sets} where ${where}")
    @ResultType(Integer.class)
    int update(String tableName, @Param("where") String where, @Param("sets") String sets);
    @Insert
```

画面 12:
```
package com.heima.admin.dao;
import org.apache.ibatis.annotations.*;
import java.util.HashMap;
import java.util.List;
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(String tableName, @Param("start") int start, @Param("size") int size);
    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(String tableName);
    @Select("select * from ${tableName} where 1=1 and ${where
