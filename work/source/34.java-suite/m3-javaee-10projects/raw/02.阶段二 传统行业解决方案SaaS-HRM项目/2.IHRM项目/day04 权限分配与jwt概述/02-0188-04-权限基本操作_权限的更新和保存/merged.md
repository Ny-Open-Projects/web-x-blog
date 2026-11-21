# 04-权限基本操作：权限的更新和保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\04-权限基本操作：权限的更新和保存_【海量资源尽在 ubkz.com】.mp4
- 时长 15分20秒（音频 920s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 已经把大致的轮廓我们写出来了那接下来呢就根据不同的API去完成一个一个操作其实就可以了那首先呢我们来看的是第一个就是用户的一个新增那用户新增的时候它传递了很多的属性但是这些属性呢是有可能是为空的如果你保存的是一个权限和菜单的一个关系那它只有权限相应的这些属性以及menu菜单我们相应的这些属性
[00:28] 如果你关注的是一个API那它只有菜单和那它只有我们的权限和API相关的这些属性那对于我们来说要做的事情呢就是根据这个type进行判断进行判断那其实呢不管是你怎么传递权限应该有接下来如果传递的是1我们从这里面拿到一些属性构造出我们的菜单对象接着再保存其实就可以了
[00:51] OK那我们这个应该接收什么样的参数类型其实这个参数类型呢我们可以通过一个map形式来进行接收接收好了之后需要哪个从map当中去获取其实就够了那好了接下来我们就可以完成保存的这个工作那完成保存的这个工作我们说过了这边呢需要把你传递的参数封装成一个map集合那我们知道map的key应该是我们传递的我们的参数名称那它就是一个string
[01:17] 那接下来就是value那value就用一个object来进行描述就可以了那接下来呢我们已经有了参数我们就可以add all to where进来我们的serviceprivate Service那接下来我们可以调用Service完成保存操作打点save把map集合传递进去那接下来呢我们就需要修改一下Service那Service这边我们还是需要拿到一个map集合map集合
[01:51] 那拿到MAP集合那接下来呢我们这个代码就需要去做一个简单的修改了那么做修改如何去做呢咱们简单的说一下我们整个的一个步骤首先第一件事我们通过MAP去构造权限对象因为不管你保存什么那你这个权限对象都有不管是菜单不管是API不管是你的按钮那权限对象都有那不一样的是不是根据就是根据我们的类型
[02:21] 去构造不同的我们叫做资源对象当然这个资源有很多比如说呢有我们的菜单比如说有我们的叫做按钮比如说有我们的API接口那好了这些我们都构造好了之后接着第三件事完成保存操作其实就可以了当然我们这边叫做保存权限啊OK那接下来呢我们就开始依照着我们这个步骤把这个代码先给它搞定
[02:46] 那对于我这个代码呢其实有一点点需要跟各位来声明的就是我这边呢可以通过一个map集合直接构造成对象不用一个一个map打点getmap打点get那样太麻烦了那么怎么做呢可以把这个给它封装到一个工具类当中通过工具类自动的去给我构造那这个工具类呢在今天代码当中也给各位准备好了那对于我们而言把这两个工具类直接Ctrl C给它copy到我们
[03:15] common 模块当中就可以了好了这边呢找到common 模块找到 utils好了 control v 直接靠进去那靠进来了之后呢简单的和各位来聊一下就是我这里面呢一共有两个第一个工具类呢叫做 bin map utilsbin map utils 两个方法第一个方法就是直接将一个对象转化成 map 集合那 map 集合的 key 是对象里面的属性value 是对象里面的属性值
[03:46] 那接下来第二个方法是我们关注的我们可以把一个map集合转化成你指定的一个对象那转化对象的时候呢如果这个对象里面的属性和map集合key保持它的名字一致的话它就会能把这个对象属性附上值就是这么一个简单的两个方法好了呢这个工具列介绍了还有一个叫做permission contents这里面其实就是我们权限类型的一个常量的一个说明
[04:13] 那比如说1我们都知道是菜单2是功能3是API我们一会儿方便的进行对它进行一个判断那好了接下来我们这两个工具类都看过了那我们可以直接就将你传递过来的MAP集合构造成Permission对象PermissionBPM好了它就等于我们叫做binMapUtils打点它有一个方法MapToBin我们把Map集合传进去接着想要封装成Permission
[04:44] 点class那这样一来就已经构造好了这边有一个异常我们处理一下那接下来呢就是说呢构造permission的时候我们需要指定你当因为要保存嘛要指定他的一个IDside id上面已经通过选项算法算出来那好了剩下的事情根据类型构造资源那类型呢我们拿过来intertabprm打点gettab那这样一来其实就已经得到了类型那得到类型之后我们开始
[05:13] 去构造不同的资源对象完成保存操作那我们这边就可以借助一个switch来做了switchswitch判断的依据呢那就是我们的type属性的这个值了OK那接着呢里面就可以一个一个的case好了第一个呢就是说当你这个type的值等于我们的菜单的时候比如说我们刚才写了一个工具类permissionconstancepermissionconstance放到什么地方呢在这儿
[05:51] 拿过来Promission content打点我们叫做menu好了break这边少一毛号那接下来呢继续如果它case这回呢就等于我们叫做菜单在那呢我们习惯把它叫做连接点好了这边呢同样break那继续再来还需要一个那这回呢我们把它称之为APIOK那接下来default
[06:35] 那如果是default就是说默认情况下都不符合的话我们可以抛出一个异常其实就可以了throw new一个我们叫做commoncommon exceptionok那这个common exception呢我们之前写过其实里面需要一个这么一个构造方法那这个构造方法传递的是我们的一个枚举那这个枚举里面我们就可以给它来一个fail失败resultresultcoderesultcode
[07:14] 点OK那这样一来呢我们基本的这个代码呢其实结构已经写好了剩下的事情就是根据不同的判断构造不同的对象然后保存操作那好了这边呢我们可以一起来看一下同样的如果你传递的是一个比如说呢是我们的菜单类型那菜单类型我们也可以通过这个工具类构造成我们需要的菜单那我们的菜单呢叫做PromissionMenu
[07:41] 好了那这样一来就能构造出我们的一个menu对象出来menuOK当然了你传递的内容传递的参数这些参数名称和这个里面的属性必须要对应上啊那menu我们有了之后接下来就是这个menu保存的时候它的ID我们之前说过跟我们全新的ID是一样的所以menu打点setID好了就是ID那接下来呢我们就可以保存这个menu对象
[08:08] 那menu对象保存我们需要注入很多的do这边呢一次性都给他写好好了里面可以传递一个叫做menu domenu dook那除了menu do之外呢还需要我们有api的还有其他的比如说pont也就是我们的菜单或者我们的权点那接下来呢这边呢就是apiok全部给他拷过来那
[08:44] 这样一来我们底下就可以通过我们叫做menu deal改一下名字太长了menu deal点sale方法保存menuOK那我们菜单搞定了之后底下的这个逻辑基本上都是一模一样的只不过底下呢变成了我们叫做point好了这边就叫做point好了这边得到的是point对象好了point.setid那我们这边通过的是point deal
[09:19] ok搞定那接下来呢最后一个就是API那对于API呢其实都是大同小异的好了这边API好了这边API set ID好了我们这边是API deal好了把API保存
[09:41] 那千万别忘了我们现在每一个资源都保存了那我们试试是不是这个整个的权限也要保存继续啊所以我底下呢还需要保存权限permissiondo打点savepermok那这样一来我们的保存其实就已经搞定了保存我们写好了之后接下来就是关注的第二个呢我们就是继续往下写就更新吧那更新呢其实跟我们这个保存的套路其实是一模一样的就写更新了
[10:11] 那同样的我们这边呢也是可以获取到所有的参数给它封装成一个map集合封装成一个map集合这个soup方法怎么报错这个报错是简单这边来一个一张处理OK那对于更新而言呢同样跟之前的保存差不多啊permission Service打点我就update那update我们就可以把map集合给它传递过来
[10:44] map集合传递过来但是对于map集合传递过来的内容呢有可能这个map集合里面没有ID所以我map打点put把你得到的这个ID我也放进去OK那这样一来呢我们就已经把这个空气方法写好了这边就是构造ID好了那接下来在update方法里面跟之前保存的逻辑基本上是一模一样的好了这边参数
[11:15] 好了里面的方法跟这边这个逻辑基本上一模一样我就把这边直接Ctrl C拷过来了当然了我们不需要去搞它的主件OK好了那这个代码呢我们应该如何去做呢虽然我现在只是把基本的这个逻辑先给它拿过来那我们这个保存或者我们这个更新用户来说首先呢第一件事我们呢就可以可以通过你传递的我们叫做权限ID查询我们的权限
[11:48] 那权限搞定了之后接着根据我们的类型构造不同的我们叫做资源那接下来呢我们可以一般常规操作不同的资源那每一个资源是不是都是查询不同的资源设置设置修改的属性好了全部都搞定了之后接着我们叫做更新我们的权限
[12:13] 更新我们的资源其实就可以了所以一共就这么几个步骤也都不难也都不难那么一个一个的来看首先第一件事把方法拷过来抱歉拷多了第一个件事把底下这个方法呢Ctrl C拿过来Ctrl V拷过来那拷过来之后呢在这边有一个异常我们一起来处理一下那我想说的是
[12:39] 通过传递的权限ID已经在PRM里面已经有了我们可以通过这个先去数据库查询Permission.findbyID好了PRM.getID那这样一来呢我们就已经抱歉这边还少一个.getOK那这样一来我们就能得到我们的权限那得到了权限之后呢要更新权限的话有可能要对权限里面的一些属性进行修改
[13:15] 因为我们是先查再改好了打点set比如说我可能要修改一下它的名称名称我们perm打点get nameOK可能还要修改一些其他的内容我们就稍微快一点了打点set codeperm打点get code同样的打点set比如说可能还要更新它的描述信息perm点get它的描述信息同样的打点set
[13:46] 它的可见性PRM打点getOK好了全线相应的更新的内容我们都已经设置好了之后接着就是根据不同的构套不同的资源那跟我们这边的这个switch基本上是一模一样的写到中间好了这边这个ID可以删掉这个方法也可以删掉好了那接下来来看就是说呀就是说呀那对于我们第二步而言呢其实
[14:20] 不错全部都构造出属性来了构造出来了之后呢构造出资源那我们是不是应该从数据库查询呀那我们从数据库查询主要是为了防止它这个GPA你更新的时候把这个不存把我没有传递的数据更新成那那其实呢如果你这个资源的内容都传递了它直接更新其实就可以了也不用查了所以这边呢我们为了简单
[14:43] 我在这边就不再去进行查询那个操作了那样会比较浪费时间比较浪费效率那在这边呢我们直接就可以你要我更新什么把ID附上值直接更新其实就可以那这个ID在哪呢我们其实全部在Premium对象里面打点Get ID因为是ID是一模一样的资源的ID跟全新的ID是一样的
[15:04] OK那这样一来他就会把你传进内容全部都给我进行更新了那接着还有最后一步千万别忘了千万别忘了我们还需要对我们这个权限也要做一个更新的一个操作OK那这样一来我这个更新方法也已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现权限管理模块的控制器与服务层代码，包括权限保存、查询、更新等核心功能，并涉及对象映射、类型判断和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PermissionController.java 中的 save 和 findAll 方法，以及 findById 方法的定义，用于处理权限的增删改查。
画面2：在 PermissionController.java 中，为 save 方法添加了 @RequestBody 注解，用于接收前端传入的 JSON 数据。
画面3：切换到 BeanMapUtils.java，展示将 Map 转换为对象的工具类方法 beanToMap 和 mapToBean。
画面4：展示 PermissionService.java 中的 save 方法，用于处理权限保存逻辑，包括生成 ID、创建 Permission 对象并设置类型。
画面5：在 PermissionService.java 中，为 save 方法添加了 @Cacheable 注解，用于缓存操作结果。
画面6：在 PermissionService.java 中，为 save 方法添加了 switch 语句，根据权限类型（如菜单、点、API）进行不同处理，并抛出异常。
画面7：在 PermissionService.java 中，为 save 方法添加了 PermissionMenuDao 和 PermissionMenuDao 的字段。
画面8：在 PermissionService.java 中，为 save 方法添加了 PermissionPoint 和 PermissionApi 的处理逻辑。
画面9：展示 PermissionController.java 中的 findById 方法，用于根据 ID 查询权限。
画面10：在 PermissionService.java 中，为 update 方法添加了根据 ID 查询目标对象并保存的逻辑。
画面11：在 PermissionService.java 中，为 update 方法添加了通过 BeanMapUtils 将 Map 转换为 PermissionPoint 对象并保存的逻辑。
画面12：在 PermissionService.java 中，为 update 方法添加了通过 BeanMapUtils 将 Map 转换为 Permission 对象并设置属性的逻辑。
画面13：在 PermissionService.java 中，为 findAll 方法添加了根据 Map 参数动态构建查询条件的逻辑。
画面14：在 PermissionService.java 中，为 update 方法添加了根据类型判断并保存对应对象的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.解析跨域
@CrossOrigin
//2.声明restController
@RestController
//3.设置访问路径
@RequestMapping(value = "/sys")
public class PermissionController {
    @Autowired
    private PermissionService permissionService;

    @RequestMapping(value = "/permission", method = RequestMethod.POST)
    public Result save(@RequestBody Map<String, Object> map) {
        return new Result(ResultCode.SUCCESS);
    }

    @RequestMapping(value = "/permission", method = RequestMethod.GET)
    public Result findAll(int page, int size, @RequestParam Map map) {
        return new Result(ResultCode.SUCCESS);
    }

    @RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
    public Result findById(@PathVariable(value = "id") String id) {
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面2：
```java
@RequestMapping(value = "/permission", method = RequestMethod.POST)
public Result save(@RequestBody Map<String, Object> map) {
    return new Result(ResultCode.SUCCESS);
}
```

画面3：
```java
public static <T> Map<String, Object> beanToMap(T bean) {
    Map<String, Object> map = new HashMap<>();
    if (bean != null) {
        BeanMap beanMap = BeanMap.create(bean);
        for (Object key : beanMap.keySet()) {
            map.put(key + "", beanMap.get(key));
        }
    }
    return map;
}

public static <T> T mapToBean(Map<String, Object> map, Class<T> clazz) throws Exception {
    T bean = clazz.newInstance();
    BeanMap beanMap = BeanMap.create(bean);
    beanMap.putAll(map);
    return bean;
}
```

画面4：
```java
package com.ihrm.system.Service;

import ...

@Service
public class PermissionService {

    @Autowired
    private PermissionDao permissionDao;

    @Autowired
    private IdWorker idWorker;

    /**
     * 1.保存权限
     */
    public void save(Map<String, Object> map) throws Exception {
        //设置主键的值
        String id = IdWorker.nextId()+"";
        //1.通过Map内容创建permission对象
        Permission perm = BeanMapUtils.mapToBean(map, Permission.class);
        perm.setId(id);
        //2.根据类型选择不同的资源对象（菜单，按钮，api）
        int type = perm.getType();
        switch (type) {
            case PermissionConstants.PERMISSION_MENU:
                break;
            case PermissionConstants.PERMISSION_POINT:
                break;
            case PermissionConstants.PERMISSION_API:
                break;
            default:
                throw new CommonException(ResultCode.FAIL);
        }
    }
}
```

画面5：
```java
@Cacheable
public void save(Map<String, Object> map) throws Exception {
    //设置主键的值
    String id = IdWorker.nextId()+"";
    //1.通过Map内容创建permission对象
    Permission perm = BeanMapUtils.mapToBean(map, Permission.class);
    perm.setId(id);
    //2.根据类型选择不同的资源对象（菜单，按钮，api）
    int type = perm.getType();
    switch (type) {
        case PermissionConstants.PERMISSION_MENU:
            break;
        case PermissionConstants.PERMISSION_POINT:
            break;
        case PermissionConstants.PERMISSION_API:
            break;
        default:
            throw new CommonException(ResultCode.FAIL);
    }
}
```

画面6：
```java
public void save(Map<String, Object> map) throws Exception {
    //设置主键的值
    String id = IdWorker.nextId()+"";
    //1.通过Map内容创建permission对象
    Permission perm = BeanMapUtils.mapToBean(map, Permission.class);
    perm.setId(id);
    //2.根据类型选择不同的资源对象（菜单，按钮，api）
    int type = perm.getType();
    switch (type) {
        case PermissionConstants.PERMISSION_MENU:
            break;
        case PermissionConstants.PERMISSION_POINT:
            break;
        case PermissionConstants.PERMISSION_API:
            break;
        default:
            throw new CommonException(ResultCode.FAIL);
    }
}
```

画面7：
```java
package com.ihrm.system.Service;

import ...

@Service
public class PermissionService {

    @Autowired
    private PermissionDao permissionDao;

    @Autowired
    private IdWorker idWorker;

    @Autowired
    private PermissionMenuDao permissionMenuDao;

    /**
     * 1.保存权限
     */
    public void save(Map<String, Object> map) throws Exception {
        //设置主键的值
        String id = IdWorker.nextId()+"";
        //1.通过Map内容创建permission对象
        Permission perm = BeanMapUtils.mapToBean(map, Permission.class);
        perm.setId(id);
        //2.根据类型选择不同的资源对象（菜单，按钮，api）
        int type = perm.getType();
        switch (type) {
            case PermissionConstants.PERMISSION_MENU:
                break;
            case PermissionConstants.PERMISSION_POINT:
                break;
            case PermissionConstants.PERMISSION_API:
                break;
            default:
                throw new CommonException(ResultCode.FAIL);
        }
    }
}
```

画面8：
```java
switch (type) {
    case PermissionConstants.PERMISSION_MENU:
        PermissionMenu menu = BeanMapUtils.mapToBean(map, PermissionMenu.class);
        menu.setId(id);
        permissionMenuDao.save(menu);
        break;
    case PermissionConstants.PERMISSION_POINT:
        PermissionPoint point = BeanMapUtils.mapToBean(map, PermissionPoint.class);
        point.setId(id);
        permissionPointDao.save(point);
        break;
    case PermissionConstants.PERMISSION_API:
        PermissionApi api = BeanMapUtils.mapToBean(map, PermissionApi.class);
        api.setId(id);
        permissionApiDao.save(api);
        break;
    default:
        throw new CommonException(ResultCode.FAIL);
}
```

画面9：
```java
@RequestMapping(value = "/permission", method = RequestMethod.POST)
public Result save(@RequestBody Map<String, Object> map) {
    permissionService.save(map);
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/permission", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    return new Result(ResultCode.SUCCESS);
}
```

画面10：
```java
public void update(Permission permission) {
    //1.根据id查询
    Permission target = permissionDao.findById(permission.getId()).get();
    //2.设置权限属性
    permission.setPermission(target);
    permissionDao.save(target);
}
```

画面11：
```java
public void update(Map<String, Object> map) throws Exception {
    Permission perm = BeanMapUtils.mapToBean(map, Permission.class);
    //1.通过传递的权限id查询权限
    Permission permission = permissionDao.findById(perm.getId()).get();
    //2.设置权限属性
    permission.setName(perm.getName());
    permission.setCode(perm.getCode());
    permission.setDescription(perm.getDescription());
    permission.setEnVisible(perm.getEnVisible());
    //3.根据类型判断不同的资源对象
    int type = perm.getType();
    switch (type) {
        case PermissionConstants.PERMISSION_MENU:
            PermissionMenu menu = BeanMapUtils.mapToBean(map, PermissionMenu.class);
            menu.setId(perm.getId());
            permissionMenuDao.save(menu);
            break;

