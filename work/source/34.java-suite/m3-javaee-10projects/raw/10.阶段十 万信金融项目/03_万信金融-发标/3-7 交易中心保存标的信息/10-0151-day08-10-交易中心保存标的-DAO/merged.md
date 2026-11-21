# day08-10-交易中心保存标的-DAO

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-10-交易中心保存标的-DAO_【海量资源尽在 666java.com】.mp4
- 时长 2分3秒（音频 124s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好接口定义好之后呢咱接下来就开始具体实现功能那功能的话无非就是分成两块一块是数据访问层就是稻草对吧一块就是对要啊就是Service那咱按照顺序吧咱还是先搞一搞对数据访问层啊就是dao那么dao这一块呢我们仍然是使用我们的好机友mp来实现那这个大家都知道了这个非常简单对不对简单的有点过分了啊我们就是搞一个接口
[00:29] 继承MP的接口然后再搞一个相配套的什么对应设配有念然后DOO从头到后我们就搞定了非常非常简单所以咱接下来找到这个哪个包啊Mapper包对不对需要新建一个对接口名字呢我们跟讲义保持一致叫ProjectMapper刚才说了Project就是标底的意思啊这里边没啥好说的就是继承MP的那个接口就行了
[00:59] 我说这么一继承咱这个接口就不是什么呀对就不是空接口这个接口里边是不是就有很多很多的什么呀方法啊比如说最常见的什么呀对增山盖茶啊这些方法就全部都有啊这是咱以前讲过的不再说了啊然后呢还要创建一个跟他相配套的硬核配合文件是不是啊那咱通过咱们的idea咱以前配过这个模板吗这个名字呢还是叫这还是叫这名啊我再重新粘一下吧
[01:30] 就是这个名字然后这里边是不是只需要设置那个接口的这个包路径就行了那就是cn.itcast.再点那translation.Mapper.就是他其他用不用写代码其他地方都不用管啊那这样子的话咱就把这个哪一层的代码搞定了对数据访问层就丢这块代码搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
     <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
     <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
     </Mapper>
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
     <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
     <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
     </Mapper>
     ```
  3. 在 Service 包中新建 ProjectService 接口，并定义 createProject 方法：
     （此部分在画面中未显示完整，仅在 PPT 中提及）

画面 6:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.Mapper;

  public interface ProjectMapper {
  }
  ```

画面 7:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.Mapper;

  public interface ProjectMapper {
  }
  ```

画面 8:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.Mapper;

  public interface ProjectMapper extends BaseMapper<Project> {
  }
  ```

画面 9:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.java`。
- 代码内容：
  ```java
  package cn.itcast.wanxing2p.transaction.Mapper;

  import cn.itcast.wanxing2p.transaction.entity.Project;
  import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

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
  package cn.itcast.wanxing2p.transaction.Mapper;

  import cn.itcast.wanxing2p.transaction.entity.Project;
  import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

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
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
  </Mapper>
  ```

画面 12:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.xml`。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
  </Mapper>
  ```

画面 13:
- 展示了 IntelliJ IDEA 的项目结构，选中了 `ProjectMapper.xml`。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
  </Mapper>
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
     <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
         "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
     <Mapper namespace="cn.itcast.wanxing2p.transaction.Mapper.ProjectMapper">
     </Mapper>
     ```
  3. 在 Service 包中新建 ProjectService 接口，并定义 createProject 方法：
     （此部分在画面中未显示完整，仅在 PPT 中提及）

