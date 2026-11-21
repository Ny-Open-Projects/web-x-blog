# 画面线理解：day03-12-用户中心保存信息-Mapper

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-12-用户中心保存信息-Mapper_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:47, 00:56, 01:13, 01:17, 01:27, 01:33, 01:56, 02:00, 02:11, 02:32, 02:44, 02:47, 03:10, 03:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:35:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建 MyBatis-Plus 的 Mapper 接口，并编写对应的 XML 映射文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在项目结构中选中 `mapper` 包，准备创建新文件。
画面 2: 右键点击 `mapper` 包，弹出菜单，选择“New” -> “Interface”。
画面 3: 弹出“Create New Class”对话框，设置类名为 `ConsumerMapper`，类型为 `Interface`。
画面 4: 新建的 `ConsumerMapper.java` 文件内容为空，等待编写代码。
画面 5: 展示 PPT 内容，说明需要新建 Mapper 接口并继承 BaseMapper，以及新建 Mapper 配置文件。
画面 6: 展示桌面多个窗口，包括 SQLyog、ApolloPortal、adminService 等，说明系统环境。
画面 7: 在 `ConsumerMapper.java` 中，导入 MyBatis-Plus 的 BaseMapper。
画面 8: 为 `ConsumerMapper` 接口选择继承 `BaseMapper<Consumer>`。
画面 9: 展示 PPT 内容，说明需要新建 Mapper 接口并继承 BaseMapper，以及新建 Mapper 配置文件。
画面 10: `ConsumerMapper.java` 文件中已编写好继承语句。
画面 11: 右键点击 `mapper` 包，弹出菜单，选择“New” -> “XML File”。
画面 12: `ConsumerMapper.java` 文件内容已编写完成。
画面 13: 在项目结构中选中 `mapper` 包，准备创建新文件。
画面 14: 新建的 `ConsumerMapper.xml` 文件内容为空，等待编写代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
package cn.itcast.wanxing2p.consumer.mapper;

public interface ConsumerMapper {

}
```

画面 5:
```java
@Repository
public interface ConsumerMapper extends BaseMapper<Consumer> {

}

<mapper namespace="cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper">
</mapper>
```

画面 7:
```java
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
```

画面 8:
```java
public interface ConsumerMapper extends BaseMapper<Consumer> {
```

画面 10:
```java
package cn.itcast.wanxing2p.consumer.mapper;

import cn.itcast.wanxing2p.consumer.entity.Consumer;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

public interface ConsumerMapper extends BaseMapper<Consumer> {

}
```

画面 11:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper">
</mapper>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
标题：3) Mapper
内容：
- 新建一个 Mapper 接口，继承 MyBatis-Plus 的 BaseMapper:
  ```java
  @Repository
  public interface ConsumerMapper extends BaseMapper<Consumer> {
  }
  ```
- 新建一个 Mapper 配置文件:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper">
  </mapper>
  ```

画面 9:
标题：3) Mapper
内容：
- 新建一个 Mapper 接口，继承 MyBatis-Plus 的 BaseMapper:
  ```java
  @Repository
  public interface ConsumerMapper extends BaseMapper<Consumer> {
  }
  ```
- 新建一个 Mapper 配置文件:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper">
  </mapper>
  ```

画面 5 和 9 的 PPT 内容完全相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
