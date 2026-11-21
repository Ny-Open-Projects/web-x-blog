# 04.MybatisPlus入门之架构讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\04.MybatisPlus入门之架构讲解【海量资源尽在 ubkz.com】.mp4
- 时长 3分15秒（音频 195s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下mybitties plus这个插件的一个架构啊那么这个图里面呢所展现出的呢就是它的整体的一个架构啊那我们首先来看一下右边的这个部分那么这个呢就是mybitties plus中一些模块啊它提供的一些这种模块或者说功能啊比如说你看像这个mybitties plus bootstar
[00:26] 那么这个其实我们从这个名字上面就能看出这个是不是就是买Bitplus对什么呢Spring Boot项目的一种支持对吧OK那么后面我们在学习这个买Bitplus的时候那么主要的我们也是使用这个工程来做就是我们因为我们我们基本的一个框架使用是Spring Boot对不对所以它必然会使用到
[00:49] 还有像什么呢扩展就是对mybidis做了一些这种扩展然后generator去生成前面有说过是不是可以生成一些代码的文件还有一些注解这个我们也是用的会比较多就是它的相关的一些注解然后还有一些它的核心的一些code核心然后它整体的一些提供的一些框架或者说它的一些模块
[01:14] 然后我们来看一下左边的这个是表示出他整个工作的流程的然后首先我们可以看他scan去做一个扫描我们的一些实体也就扫描了我们一些这种pojo这种实体然后通过反射通过反射然后提取出什么提取出一些我们的一些表的一些信息什么字段表明这种一些信息
[01:41] 那么通过我们提取到的一些这个字段和一些表明呢我们去做一些这个分析啊做一些这个分析然后呢通过我们分析的这个结果然后呢我们再去生成一些这个什么呢CLUD的一些这个社会语句啊生成一些这种CLUD然后呢我们将这些CLUD然后呢再注入到买杯的这个容器中那么是不是在交由买杯类似做一个执行
[02:10] OK他就他整体的一个逻辑就是这样就是说他大体的一个逻辑呢大概是这样的啊就是我们画一个简单的一个图啊我们来说明一下就是这个是我们原有比方这个框啊这个代表的是我们原有的mybodies这个框架对吧然后呢他在外围做了一些这个事情就是做什么呢根据我们的实体然后去做一些分析最后再得出一些什么我们的一些生成一些这个社会语句
[02:40] 然后把这个circle语句最终你还是交给mybeddy的框架去做一个执行所以说他对mybeddy的框架是没有任何的侵入的对不对他只是在外围做了一些这种事情做了这样的事情然后最终生成了circle语句交由mybeddy做一个执行然后拿到结果再去做一些分装ok这个就是mybeddy plus这个插件所做的事情他所做的内容就在外面的外围的这一块ok
[03:08] 好那么关于买背的replus的这个插件的一个架构啊咱们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 MyBatis-Plus 的架构组成及其核心模块之间的关系。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 MyBatis-Plus 架构图，左侧为功能模块（Scan Entity → Analysis Table Name Column → Injection Mybatis Container），右侧为模块组成（mybatis-plus-boot-starter 包含 annotation、extension、core、generator）。
画面2: 与画面1相同，无新增内容。
画面3: 在“mybatis-plus-boot-starter”模块上添加红色下划线。
画面4: 在“extension”模块上添加红色下划线。
画面5: 在“core”模块上添加红色下划线。
画面6: 在“generator”模块上添加红色下划线。
画面7: 在“Scan Entity”模块上添加红色下划线。
画面8: 在“Analysis Table Name Column”模块上添加红色下划线。
画面9: 在“Injection Mybatis Container”模块上添加红色下划线。
画面10: 移除“Scan Entity”模块上的红色下划线。
画面11: 在“Scan Entity”模块上添加红色框线。
画面12: 在“Scan Entity”模块上添加红色箭头指向“Analysis Table Name Column”模块。
画面13: 在“Analysis Table Name Column”模块上添加红色箭头指向“Injection Mybatis Container”模块。
画面14: 移除所有红色标记，恢复原始架构图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
PPT标题：2.3、架构
架构图结构：
- 左侧模块组（虚线框）：
  - Scan Entity → Reflection extraction → Analysis Table Name Column → SQL (Insert, Delete, Update, Select) → Injection Mybatis Container
- 右侧模块组（虚线框）：
  - mybatis-plus-boot-starter → 包含：annotation、extension、core、generator
- 左侧模块组与右侧模块组之间有箭头指向，表示左侧模块依赖右侧模块。

5) 无。

