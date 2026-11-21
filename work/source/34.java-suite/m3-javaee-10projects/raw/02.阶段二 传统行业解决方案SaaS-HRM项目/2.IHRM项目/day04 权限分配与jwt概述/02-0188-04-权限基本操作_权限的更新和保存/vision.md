# 画面线理解：04-权限基本操作：权限的更新和保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\04-权限基本操作：权限的更新和保存_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:28, 03:46, 04:56, 06:10, 07:10, 08:25, 09:47, 10:11, 11:22, 12:47, 13:29, 14:02, 15:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:50:35

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
package com.ihrm.system.service;

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
package com.ihrm.system.service;

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
