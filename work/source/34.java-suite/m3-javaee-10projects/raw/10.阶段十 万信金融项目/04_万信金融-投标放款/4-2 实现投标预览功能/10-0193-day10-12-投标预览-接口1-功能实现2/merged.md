# day10-12-投标预览-接口1-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-12-投标预览-接口1-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 15分26秒（音频 926s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把标的信息查询了一下查完之后呢我们是不是已经在这做封装了就是把project的对象转换成什么呀DTO的对象那在转换过程当中呢我们发现呢这个project DTO里边它还需要什么呀封装剩余余额以及什么呀出现人数所以咱接下来的话要把这两块信息也查询一下那咱首先查一下这个什么呀剩余额度吧
[00:29] 这个剩余额度啊查出来之后是在这用的这个地方啊大家就这个信息并不是标的信息里边一部分也就是说呢标的信息查出来之后里边是没有这个信息的啊这个需要我们单独做处理那这个剩余额度怎么查呢大家看一个表看哪个表看这个tender表tender呢咱前面提过它就是投标的意思对不对那这个表里边存的就是投标信息投标信息啊
[00:58] 那将来呢这里边很多人如果进行了投标呢他这个投标信息呢就会保存到这个表里边咱熟悉一下这里边的一些字段这里边大家看一下这块是不是投资人的信息了相当于对吧投资人嘛投标人其实就是投资人他的一些用户的标识用户名用户编码对吧这一块是什么呀那个标底信息就是你投到哪个标这标底的标识就是那个ID嘛标底的编码然后报告投了多少钱是不是
[01:28] 投标状态创建时间等等等等然后这里边还有一个可用状态对吧status这个可能状态指的是大家看这个可用状态指的就是这个就是同步不同步的状态那如果说将来哎这个银行那边也处理完了也处理成功了那么这个状态会改成什么一同步为为同步就是0嘛一同步就是什么一嘛这个咱以前也见过这种情况包括其他的一些什么一些这个
[01:56] 标底的名称啊一些利息等等之类的信息这就是投标这个信息表那我们接下来就要通过这张表去查询什么呀对查询这个剩余额度怎么查呢大家想一想怎么查呢大家想一个标底是不是可以有多个人去投标那比如一个标底有五个人投标那我问大家在这个表里边是不是应该有五条记录这五条记录应该是五个投标人但是这个标底的标识应该是同一个标识吗
[02:26] 就五个人对一个标的进行什么呀投标是这一次吧那我在这个表里边能查出来剩余额度吗你是查不出来的你在这个表里边只能查出来已投了多少金额比如说这个人要借十万块钱有现在呢有五个人给他投标了这五个人一共投了五万这个五万已投的五万我在这个表里边能查出来吗可以吧那剩余是不是还有五万剩余这个五万怎么查出来剩余的五万
[02:56] 就要拿着这个什么呀当时借款人一共要借多少钱十万块钱吧减去现在已经投到这个五万剩下五万是不是就是剩余金额大家能听明白什么意思吗所以我们首先要从这个表里边查出来已投的金额然后呢再做一个减法运算就OK了那怎么从这个表里边查这个已投金额呢我们需要写一条搜狗语句我们在这写一下slag什么呀我们要查什么信息
[03:31] 对大家注意了啊我们要查的是这个以投的这个金额信息那这里边这个都查什么信息我们先放到这啊我们要从哪个表查呀我们能确定就是T1D1对吧那有没有条件呢有啊我一定是查某个标的这个什么呀以投进去那所以说这里边一定有个条件就是这个谁啊对这个标的来历是不是他等于谁
[04:04] 然后呢我们其实这里边还需要再加一个条件就是这个状态这个状态呢一定得是谁呀一必须得等于一为什么呢因为我刚才给大家提到过你在这儿是不是要获取某个标的你投的这个金额对吧什么叫一投金额呢就是说这个金额一定是经过银行那边处理过处理完了那么他的状态就会变成几变成一同步这个一同步的值是不是就一呀
[04:33] 那这个处理完了状态变成一同步了这个投标才算成功那么这个投标金额才算数啊才算数如果银行那边处理失败了那这个投标金额是不算数的你是不应该把它也查询出来了啊所以咱这个条件一共有几个呀得有两个一个是我要查的是某个标的的一投金额然后还得确保这个是投标是已经成功的这个状态啊所以我们这个一就表示一同步啊已经处理成功了这条件我们先明确一下
[05:03] 填兴明确完之后我们到底查什么呀我们是要求和呀是要求和呀求哪个字段的和呀我们要求的就是这个字的这个字段是不是就是投标冻结金额吧那这个我刚才说的就是投资人投的这个钱嘛就刚才说的每个人投了一万块钱这个就是那个一万块钱我是不是应该求这个字段和比如有五个人每个人都投了一万是不是求和应该是五万吧所以我要对这个字段进行求和我要的就是这个和那求和用哪个函数啊
[05:33] 是不是SAM对不对SAM这里边就写上谁啊写上AMOUNTOUNT就是他那么在在求和的时候呢我们要注意我们要做一些细节的处理吧因为你看他将来的话我们要考虑这个资本里边万一有这个空值对不对防止他出错吧我们在这呢做对他做一个进一步的一个处理用一个函数叫IFNOW大家有印象吗IFNOW然后呢通过他可以干什么呀
[06:05] 可以把空值给它替换成什么呀替换成数字00.0吧我们做这么一个操作这条伺候语句呢咱基本上就写完了大家看一眼啊我们要从tender表里边查数据怎么查呢我要查某个标底的什么呀以投金额而且呢这个投标这个动作是已经成功的那么我要查的只是这个什么呀投标的这个金额
[06:36] 而且我是要求和就是所有人就是这个标的以投的所有的金额所以我要对这个字弹进行求和求完和之后我又对空值做了一个处理如果是空值的话我是不是给它转换成0了对不对这样更保险一些所以说这是我们的思考语句有些小周我们怎么通过MP进行查询我们就要找到咱们前面定义的tender Mapper这个接口在这个接口里边要自定义一个方法
[07:06] 然后呢进行刚才咱写的那个查询对不对那这块呢咱看看讲义吧讲义里边的话在这儿啊有这块代码我给他粘过来咱们再看一看就行了粘到这儿好大家看一下我们是不是自定义的一个方法发的名字比较长啊然后参数呢是一个id这个id呢就是那个标底的id对吧这条诉考语句咱看
[07:42] 看一下是不是放到了slack的注解里边因为咱是查询这条搜狗鱼是不是咱刚才在搜狗鱼箱里边一起分析出来那条搜狗鱼只不过这个问号原来的问号是不是换成 mybilletplus的这种写法将来id的值是不是就会放到这然后进行查询对不对这里边有一个细节需要大家注意的就是这个地方就是这儿不知道你有没有注意过这个地方有点意思有啥意思
[08:13] 大家看一下我们这条搜据按说查出来的就是一个什么呀不就是一个数字吗是不是我们的sum聚合按说反回来是不是就一个数字吗那一个数字的话我这个方法的反位值为什么是一个集合呢有这个必要吗对不对我这查出来就是单个值吗那这为什么要设计成是一个集合呢这个有没有哪个同学能想到呢这个跟哪有关呢这一定得用集合不用集合肯定是不行的
[08:49] 大家觉得这跟哪有关对大家想一想我们前面在讲这个什么发标的时候我们讲过说这个transaction就是交易这个库我们是不是对它进行分库分表大家有印象吗然后咱们前面的实验发标的时候我们说这个发标呢是不是存到了project的这个表里我们当时你看这很明显是不是分表了那将来发发标的时候呢这个信息有可能会存到零里边也有可能会存到什么一里边那你想想
[09:22] 咱将来投标是不是也是如此呢虽然咱现在还没有实现投标功能但是呢咱这也分库分标了呀它跟发标的时候那个效果是一样我们将来投标的时候这个数据是不是要保存到tender表里面你看咱tender表有没有进行分库分表也进行了呀那我们进行了分库分表大家想一下那有没有可能出现这种情况同样一个标底信息同样一个标我在投标的时候这个投标的数据是不是会分散到不同的这些表里面
[09:52] 大家想有没有可能它不可能一定是在一张表里是不是那所以说你想想我这条搜据将来通过sharding-gdbc进行搜索的时候这个核查出来的可不止一个对不对它有可能是tender0里边查出来一个值tender1里边查出来一个值那包括这个库里边是不是也有可能tender0查出来值tender1查出来值那我们要的这个什么呀以投金额是不是应该是
[10:21] 这几张表的这个总和还要加到一起然后加到一起的这个和才是我们最终要的什么呀一头金啊明白什么意思吧所以说呢这儿你不能是哎我就用一个什么呀逼个decimal哎一接受就完事他将来通过分副分表进行查询查出来的这个结果可不止一个啊不止一个所以他是多个值多个值呢我们就要用什么呀list的集合来进行什么呀接受啊所以说这个细节非常非常重要
[10:51] 主要原因就是在于我们这个地方进行了分库分表啊说这个细节大家一定要注意那而Mapper接口里边方法咱搞定之后接下来我们是不是要回到什么呀业务层啊回到这个地方在这是不是调用一下就行了对吧好咱现在找到这个Service是不是要在这其实调用一下这个方法是不是就OK了对吧我们就得到这个集合集合里边呢这些数据我们是不是还要再相加一下对不对
[11:23] 那咱就在这调用一下吧要想调用的话我们是不是需要把这个Mapper接口注一下因为这个Mapper接口咱新定义的以前没有注入过Drivet然后叫TNDRTenderMapper注入进来之后呢我们是不是就可以在哪个地方在这儿来调用方法获取到这个什么呀以头的熬度然后再用总金额
[11:54] 借款的总金额减去这个什么呀你投的额度就导到了我们想要的剩余额度那这一块呢这个代码我们呢就准备把它抽取出来放到一个方法里那这块咱们可以先看看讲义应该讲义当中呢我们就单独抽取出来了这么一个方法大家看一下这个代码也没几行挺简单的咱看一看让我们单独定义一个方法专门求什么呀求这个剩余的额度
[12:23] 然后我们把这个标的信息这个对象整个传过来传来之后呢你看首先咱是是根据标的ID调用咱刚才MemberJacker里边这个方法是不是得到了该标的一头的这个什么呀金额我们说了是一个粒子的集合嘛因为他得到应该是好几个这个这个值然后这几个值我们是不是还要相加嘛对不对那怎么相加呢你要注意咱求出来是BigDecimal可不是简单的用加法
[12:52] 运算一下就行了不行啊我们得调用big decimal这个对象的add方法因为我们考虑到将来这个金额有可能很大嘛所以说我们没有用double啊是用的big decimal所以我们应该要便利这个集合是不是便利这个集合便利过程当中呢把每个值取出来通过add方法进行求和一定要注意我们这是big decimal啊不是doubledouble你用加号就可以进行求和了是不是那大家注意了
[13:23] 我们整个循环结束之后得到的这个和才是我们真正的这个什么呀一头金额是不是一头金额然后这个剩余额度怎么求呢剩余额度就是从标底的对象里边得到这个什么呀借款的总金额啊他这里边这个有个做款的借款的总金额的大家可以看一下这个普尔借款对象你看这里边有一个借款的总额度这是借款的总金额啊
[13:52] 所以说呢我们拿着这个总金额这个方法是减法运算啊也是逼个decimal对象里边减法运算减去谁啊减去咱刚才求出来的这个什么呀以头的总金额那得到的结果就是剩余额啊所以这个代码呢虽然有好几行但是相当于说比较简单那这个代码呢我就不再给大家编写了我们就直接粘过来用那我们就粘到下边这个地方是不是就OK了
[14:22] 我们调整一下这个格式调整一下格式那这个方法定义好之后呢我们接下来就可以在这个地方是不是调用一下对这个方法然后呢我们要给他扔进去一个什么呀对project的对象你看咱这不是一个循环吗循环里边是不是就会取出来project对象然后呢就扔给这个方法在这里边根据ID查出来这个什么一头镜子
[15:08] 然后把这几个以投金额呢做一个加运算然后呢再用总金额一减就得到了剩余额度我们在这一样方法就得到这个什么呀对得到剩余额度了这是这个功能吧咱就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在万向金融P2P交易系统中，通过Java代码查询项目信息、计算剩余金额并封装返回DTO，涉及数据库表结构、SQL查询及MyBatis映射。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法用于查询项目ID列表。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面2：
- 显示数据库管理工具（SQLyog）中p2p_transaction_0数据库的表结构。
- 列出数据库中的6张表：claim_0, claim_1, project_0, project_1, tender_0, tender_1。

画面3：
- 显示PPT页面，标题为“用户投标业务流程图”。
- 图中包含多个模块：浏览器/App、交易中心、用户服务、存管代理服务、存管系统。
- 从“浏览器/App”指向“交易中心”，再指向“用户服务”，最后指向“存管系统”。
- 从“用户服务”指向“存管代理服务”，再指向“存管系统”。
- 图中包含多个步骤，如“1.1 获取标的的信号”、“1.2 项目标的的信号”、“1.3 项目标的的信号”、“2.5 预处理添加投标成功”、“10. 更新交易记录，状态为：已同步”。

画面4：
- 显示数据库管理工具中“tender”表的结构。
- 表结构包含字段：ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL。
- 表中数据为空。

画面5：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面6：
- 显示数据库管理工具中“tender”表的查询结果。
- 查询条件为：WHERE PROJECT_ID = 1 AND STATUS = 1。
- 查询结果为空。

画面7：
- 显示数据库管理工具中“tender”表的查询结果。
- 查询条件为：WHERE PROJECT_ID = 1 AND STATUS = 1。
- 查询结果为空。

画面8：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面9：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面10：
- 显示IDE中ProjectServiceImp.java文件，其中createProject方法的代码。
- 代码中使用RestResponse获取用户信息，设置项目状态为COLLECTING，设置项目状态为STATUS_OUT，设置项目创建时间。
- 代码注释说明：1. 获取用户信息；2. 设置项目状态；3. 设置项目状态；4. 设置项目创建时间。

画面11：
- 显示PPT页面，标题为“黑马程序员”。
- 页面内容包括：获取标的的ID，在线查询已投资金额，计算剩余金额。
- 代码中使用BigDecimal进行金额计算，通过tenderMapper.selectAmountInvestedByProjectId查询已投资金额。
- 代码注释说明：1. 根据标的的ID在线查询已投资金额；2. 计算剩余金额。

画面12：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面13：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面14：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面4：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面5：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面6：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面7：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面8：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面9：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String

