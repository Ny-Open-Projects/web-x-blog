# day03-12-用户中心保存信息-Mapper

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-12-用户中心保存信息-Mapper_【海量资源尽在 666java.com】.mp4
- 时长 3分33秒（音频 214s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] MP相关的环境准备好之后呢咱们接下来就可以进行功能开发了这个具体的功能开发从哪开始呢那凡是涉及到数据库操作呢我建议你都是从数据访问层开始然后再是业务层然后再是表现层对吧当然你反过来也可以啊这个反正就是看个人习惯那我这儿呢基本上都是一个套路先数据访问层然后再业务层再表现层数据访问层呢其实对于大家来说就比较简单了因为咱使用了MP这个好机友
[00:32] 那么数据访问层变得异常的简单定一个接口继承他的接口然后呢再定义一个相配套的什么呀Mapper配有链是不是就搞定了对不对所以咱接下来把这一块呢代码编写一下好我们回到ID找到哪呢找到这个Mapper这个包在这个包里面我们要新建一个什么呀接口这个数据访问层的一个接口
[01:01] 我们起个名字就叫AC也不是ACCOD的啊CO什么呀consumercon s u m e r然后呢叫m a p p r然后呢是一个接口然后呢你们要注意咱自己定义的这个接口就这么写可不行啊这是一个真正的一个空接口我们需要它怎么着啊对我们需要它继承MP提供了什么呀BaseMap这个接口
[01:35] 咱继承一下这都是以前咱讲过的Basemapp好然后这有一个范形需要我们设置这个范形自然就是咱刚才提过的那个什么consumer那个实体类对吧con sumer那稍等一下有点卡好那咱这接口是不是就定义好了是不是对没错
[02:19] 接口了你看着是空的但是其实它是不空的因为它是不是继承了贝斯麦克这里边是不是定好了一堆的增深改查的方法没错吧好这是接口有了接口有了之后呢接下来呢接下来呢咱就要新建一个Mapper映射配置对吧还是在这个接口里面点右键怎么新建啊大家还记得咱之前是不是配过一个模板吗有印象吗我们可以直接就可以新建出来找一找就是这个
[02:49] 我们起个名字就行了就叫con sumer ma p p r好点击ok然后里边呢是不是要补充一个一个一个Mapper解口的路径对吧那就是cn点it算了他这个反应比较慢我从这直接粘过来c可能出v点搞定
[03:22] 现在是不是一个Map接口有了然后Map应用软件也有了数据访问层的代码咱就编写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建 MyBatis-Plus 的 Mapper 接口，并编写对应的 XML 映射文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在项目结构中选中 `Mapper` 包，准备创建新文件。
画面 2: 右键点击 `Mapper` 包，弹出菜单，选择“New” -> “Interface”。
画面 3: 弹出“Create New Class”对话框，设置类名为 `ConsumerMapper`，类型为 `Interface`。
画面 4: 新建的 `ConsumerMapper.java` 文件内容为空，等待编写代码。
画面 5: 展示 PPT 内容，说明需要新建 Mapper 接口并继承 BaseMapper，以及新建 Mapper 配置文件。
画面 6: 展示桌面多个窗口，包括 SQLyog、ApolloPortal、adminService 等，说明系统环境。
画面 7: 在 `ConsumerMapper.java` 中，导入 MyBatis-Plus 的 BaseMapper。
画面 8: 为 `ConsumerMapper` 接口选择继承 `BaseMapper<Consumer>`。
画面 9: 展示 PPT 内容，说明需要新建 Mapper 接口并继承 BaseMapper，以及新建 Mapper 配置文件。
画面 10: `ConsumerMapper.java` 文件中已编写好继承语句。
画面 11: 右键点击 `Mapper` 包，弹出菜单，选择“New” -> “XML File”。
画面 12: `ConsumerMapper.java` 文件内容已编写完成。
画面 13: 在项目结构中选中 `Mapper` 包，准备创建新文件。
画面 14: 新建的 `ConsumerMapper.xml` 文件内容为空，等待编写代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
package cn.itcast.wanxing2p.consumer.Mapper;

public interface ConsumerMapper {

}
```

画面 5:
```java
@Repository
public interface ConsumerMapper extends BaseMapper<Consumer> {

}

<Mapper namespace="cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper">
</Mapper>
```

画面 7:
```java
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;
```

画面 8:
```java
public interface ConsumerMapper extends BaseMapper<Consumer> {
```

画面 10:
```java
package cn.itcast.wanxing2p.consumer.Mapper;

import cn.itcast.wanxing2p.consumer.entity.Consumer;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

public interface ConsumerMapper extends BaseMapper<Consumer> {

}
```

画面 11:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper">
</Mapper>
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
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper">
  </Mapper>
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
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper">
  </Mapper>
  ```

画面 5 和 9 的 PPT 内容完全相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

