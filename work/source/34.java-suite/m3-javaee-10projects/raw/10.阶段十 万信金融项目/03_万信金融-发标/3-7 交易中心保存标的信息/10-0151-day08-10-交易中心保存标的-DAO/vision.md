# 画面线理解：day08-10-交易中心保存标的-DAO

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-10-交易中心保存标的-DAO_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 00:31, 00:41, 00:43, 00:49, 00:53, 01:00, 01:01, 01:24, 01:30, 01:37, 01:46, 01:49, 01:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:49:43

1) 这一组画面整体在讲什么（一句话）：
在万方金融系统中，通过定义 MyBatis 的 Mapper 接口和对应的 XML 映射文件，实现对“标的”信息的数据库操作功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了课程 PPT 页面，标题为“3.2.2 功能实现”。
- 内容包括：
  1. 在 Mapper 包中定义 ProjectMapper 接口，并继承 MP 的 BaseMapper 接口：
     ```java
     /**
      * 标的信息Mapper接口
      */
     public interface ProjectMapper extends BaseMapper<Project> {
     }
     ```
  2. 在 Mapper 包中新建 ProjectMapper.xml 文件：
     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
     <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
     </mapper>
     ```

画面 2:
- 与画面 1 几乎完全相同，仅鼠标位置略有不同。

画面 3:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `TransactionController.java`。
- 代码内容：
  ```java
  @Api(value = "交易中心服务", tags = "transaction")
  @RestController
  public class TransactionController implements TransactionApi {
      @Override
      @ApiOperation("借款人发标", value = "标的的信息", required = true,
          dataType = "Project", paramType = "body")
      @PostMapping("/my/projects")
      public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
          return null;
      }
  }
  ```

画面 4:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `TransactionController.java`。
- 代码内容：
  ```java
  @Api(value = "交易中心服务", tags = "transaction")
  @RestController
  public class TransactionController implements TransactionApi {
      @Override
      @ApiOperation("借款人发标", value = "标的的信息", required = true,
          dataType = "Project", paramType = "body")
      @PostMapping("/my/projects")
      public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
          return null;
      }
  }
  ```

画面 5:
- 展示了课程 PPT 页面，标题为“3.2.2 功能实现”。
- 内容包括：
  1. 在 Mapper 包中定义 ProjectMapper 接口，并继承 MP 的 BaseMapper 接口：
     ```java
     /**
      * 标的信息Mapper接口
      */
     public interface ProjectMapper extends BaseMapper<Project> {
     }
     ```
  2. 在 Mapper 包中新建 ProjectMapper.xml 文件：
     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
     <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
     </mapper>
     ```
  3. 在 Service 包中新建 ProjectService 接口，并定义 createProject 方法：
     （此部分在画面中未显示完整，仅在 PPT 中提及）

画面 6:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.mapper;

  public interface ProjectMapper {
  }
  ```

画面 7:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.mapper;

  public interface ProjectMapper {
  }
  ```

画面 8:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.mapper;

  public interface ProjectMapper extends BaseMapper<Project> {
  }
  ```

画面 9:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.mapper;

  import cn.itcast.wanxing2p.transaction.entity.Project;
  import com.baomidou.mybatisplus.core.mapper.BaseMapper;

  /**
   * 标的信息Mapper接口
   */
  public interface ProjectMapper extends BaseMapper<Project> {
  }
  ```

画面 10:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.mapper;

  import cn.itcast.wanxing2p.transaction.entity.Project;
  import com.baomidou.mybatisplus.core.mapper.BaseMapper;

  /**
   * 标的信息Mapper接口
   */
  public interface ProjectMapper extends BaseMapper<Project> {
  }
  ```

画面 11:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.xml`。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
  </mapper>
  ```

画面 12:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.xml`。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
  </mapper>
  ```

画面 13:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.xml`。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
  </mapper>
  ```

画面 14:
- 展示了课程 PPT 页面，标题为“3.2.2 功能实现”。
- 内容包括：
  1. 在 Mapper 包中定义 ProjectMapper 接口，并继承 MP 的 BaseMapper 接口：
     ```java
     /**
      * 标的信息Mapper接口
      */
     public interface ProjectMapper extends BaseMapper<Project> {
     }
     ```
  2. 在 Mapper 包中新建 ProjectMapper.xml 文件：
     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
     <mapper namespace="cn.itcast.wanxing2p.transaction.mapper.ProjectMapper">
     </mapper>
     ```
  3. 在 Service 包中新建 ProjectService 接口，并定义 createProject 方法：
     （此部分在画面中未显示完整，仅在 PPT 中提及）
