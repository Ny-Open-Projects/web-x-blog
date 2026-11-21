# day06-10-开户第一阶段-功能实现6

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-10-开户第一阶段-功能实现6_【海量资源尽在 666java.com】.mp4
- 时长 3分23秒（音频 203s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好大家看这里啊还是要看开户的这个实际图我们目前是不是正在实现1.1到1.7就是第一阶段的这个功能那第一阶段功能呢大家也知道我们是不是涉及到两个微服一个是用户中心一个是存管代理服务而刚刚我们把用户中心这块代码已经全部搞定了那按照顺序接下来我们该搞定哪一块的代码了呀对存管代理服务这块代码这个代码搞完之后呢咱第一阶段就搞定了就可以进行测试
[00:29] 那从来代理服务这一块呢大家知道是我们新增的一个微服务工程是吧那我们这个代码得从头开始写那我们简单回顾一下这里边的话他都设定了哪个功能你看一点四一点五这是最核心的功能啊一点四呢就是我们要要生成签名加密数据嘛一点五呢就是这边要把开户呢当成一个交易记录进行什么呀保存对他涉及到数据库操作那我们这个代码从来开始写
[00:57] 那涉及到数据库操作嘛我们自然就是从数据访问层就这开始它用的也是mybattlesplusmp那这个大家都比较熟了我们用mp开发数据访问层是不是非常非常的简单来一个接口记成mp的接口然后再给一个空的映射配置软件基本上这个呃常见的自然改革功能是不是就有啊对不对那咱快速的把这一块搞一下啊
[01:22] 我们找到这个谁啊存管代理服务然后找到哪个包Mapper包MapperMapper对吧然后我们新建一个接口接口名字呢跟讲义里边保持一致DepositoryRecordMapper好粘过来然后呢我们需要让他继承这个谁啊对这是谁提供的呀MP对不对我就直接把这块粘过来吧
[01:57] 比较简单的东西我就不再从头敲了这是这个接口就有了对不对大家也知道这个框架将来是不是会根据这个接口生成代理类啊代理对象等等等等相关的一些东西咱们就比较的省事好然后呢跟它是不是还相配套的有一个什么东西啊对映射配置文件我们点右键咱之前配过一个模板嘛就是它然后呢名字呢咱也保持一致一般都是这个接口的名字
[02:36] 粘过来OK然后哪需要改一改是不是对不对我们需要给上那个接口的路径我们的接口叫dpository然后reco没有提示吗我们从头敲cn.atcast.对然后我们这应该是depository对吧.map.就是它了这搞定了这是哪一层就搞定了
[03:14] 对啊这不是数据访问层就搞定了吗搞定完之后呢咱这个最基本的话最常见的自然改善功能就有

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在万向金融开户系统中，为存管代理生成开户数据的功能，创建 MyBatis 的 Mapper 接口和对应的 XML 映射文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程 PPT 页面，标题为“3.3.3.2 存管代理生成开户数据”，子标题“1. 数据访问层”。
- PPT 内容要求：在 Mapper 包中新建 DepositoryRecordMapper 接口；在 Mapper 包中新建 DepositoryRecordMapper.xml。
- 画面左侧显示了项目结构，当前选中的是“wanningzp_depository_agent_service”模块。

画面 2：
- PPT 页面内容与画面 1 相同，但下方新增了“2. 新建 DepositoryRecordService 接口，并定义 createConsumer 方法”。
- 画面右侧的编辑器中，显示了“DepositoryRecordMapper”接口的代码框架，但尚未完成。

画面 3：
- 展示了 IntelliJ IDEA 的项目结构视图，选中了“wanningzp_depository_agent_service”模块。
- 编辑器区域为空，显示“Search Everywhere Double Shift”等提示。

画面 4：
- 在项目结构中选中了“Mapper”包，右键点击，弹出创建新文件的上下文菜单。
- 选中了“New” -> “Java Class” 选项。

画面 5：
- 弹出“Create New Class”对话框，用户正在选择类类型。
- “Kind”下拉菜单中选中了“Class”，“Name”输入框中输入了“DepositoryRecordMapper”。

画面 6：
- 展示了多窗口界面，包括 PPT、IDEA、WPS、SQLyog 等。
- PPT 页面内容与画面 1 相同。
- 画面下方显示了“2. 新建 DepositoryRecordService 接口，并定义 createConsumer 方法”。

画面 7：
- 在 IDEA 中，选中了“DepositoryRecordMapper”文件，编辑器中显示了该接口的代码框架。
- 代码内容为：
  ```java
  package cn.itcast.wanxing2p.depository.Mapper;

  public interface DepositoryRecordMapper {
  }
  ```

画面 8：
- 选中了“DepositoryRecordMapper”文件，编辑器中显示了该接口的代码框架。
- 代码内容为：
  ```java
  package cn.itcast.wanxing2p.depository.Mapper;

  public interface DepositoryRecordMapper {
  }
  ```

画面 9：
- 在“DepositoryRecordMapper”文件上右键，弹出上下文菜单。
- 选中了“Run with Coverage”选项。

画面 10：
- 弹出“New MP Mapper XML”对话框，用于创建 XML 映射文件。
- “file name”输入框为空。

画面 11：
- 编辑器中显示了“DepositoryRecordMapper.xml”文件的内容。
- 代码内容为：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

画面 12：
- 编辑器中显示了“DepositoryRecordMapper.xml”文件的内容。
- 代码内容为：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

画面 13：
- 展示了课程 PPT 页面，标题为“3.3.3.2 存管代理生成开户数据”，子标题“1. 数据访问层”。
- PPT 内容要求：在 Mapper 包中新建 DepositoryRecordMapper 接口；在 Mapper 包中新建 DepositoryRecordMapper.xml。
- 画面左侧显示了项目结构，当前选中的是“wanningzp_depository_agent_service”模块。

画面 14：
- 编辑器中显示了“DepositoryRecordMapper.xml”文件的内容。
- 代码内容为：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
- PPT 内容：
  ```
  3.3.3.2 存管代理生成开户数据
  1. 数据访问层
  在Mapper包中新建DepositoryRecordMapper接口：
  在Mapper包中新建DepositoryRecordMapper.xml:
  ```

画面 2：
- PPT 内容：
  ```
  3.3.3.2 存管代理生成开户数据
  1. 数据访问层
  在Mapper包中新建DepositoryRecordMapper接口：
  在Mapper包中新建DepositoryRecordMapper.xml:
  2. 新建DepositoryRecordService接口，并定义createConsumer方法：
  ```

画面 7：
- 代码：
  ```java
  package cn.itcast.wanxing2p.depository.Mapper;

  public interface DepositoryRecordMapper {
  }
  ```

画面 11：
- XML 配置：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

画面 12：
- XML 配置：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

画面 14：
- XML 配置：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN"
      "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
  </Mapper>
  ```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- PPT 标题：“3.3.3.2 存管代理生成开户数据”。
- 子标题：“1. 数据访问层”。
- 内容：“在Mapper包中新建DepositoryRecordMapper接口：”、“在Mapper包中新建DepositoryRecordMapper.xml”。

画面 2：
- PPT 标题：“3.3.3.2 存管代理生成开户数据”。
- 子标题：“1. 数据访问层”。
- 内容：“在Mapper包中新建DepositoryRecordMapper接口：”、“在Mapper包中新建DepositoryRecordMapper.xml”。
- 新增内容：“2. 新建DepositoryRecordService接口，并定义createConsumer方法：”。

画面 6：
- PPT 标题：“3.3.3.2 存管代理生成开户数据”。
- 子标题：“1. 数据访问层”。
- 内容：“在Mapper包中新建DepositoryRecordMapper接口：”、“在Mapper包中新建DepositoryRecordMapper.xml”。
- 新增内容：“2. 新建DepositoryRecordService接口，并定义createConsumer方法：”。

画面 13：
- PPT 标题：“3.3.3.2 存管代理生成开户数据”。
- 子标题：“1. 数据访问层”。
- 内容：“在Mapper包中新建DepositoryRecordMapper接口：”、“在Mapper包中新建DepositoryRecordMapper.xml”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

