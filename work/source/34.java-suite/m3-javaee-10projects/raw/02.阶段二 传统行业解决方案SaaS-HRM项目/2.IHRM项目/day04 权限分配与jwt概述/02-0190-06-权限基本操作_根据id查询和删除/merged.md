# 06-权限基本操作：根据id查询和删除

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\06-权限基本操作：根据id查询和删除_【海量资源尽在 ubkz.com】.mp4
- 时长 8分34秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那对于根据ID查询来说呢首先看一下API根据ID查询get方法那我们传递的数据跟之前的套路差不多如果你这个ID代表的是一个API权限那拿到的就是这些内容有权限的属性有API对象的属性如果是菜单那只有菜单和我们权限的这些属性那针对这个需求呢怎么做呢其实返回以返回MAP对象更加合适一些
[00:29] 所以接下来呢我们就开始去构造我们这个方法那在这个方法当中呢我们可以根据ID查询返回MAP集合所以我得到的是一个MAP集合等于PromiseService打点我叫做find把ID传进去得到MAP那底下我构造MAP并且返回就可以了那接下来呢我们关注Service
[00:57] 那在Service当中注意那在Service当中我们要做的事情呢简单的写一下第一个首先要查询权限好了接着第二个根据权限的类型查询资源那接着我们第三件事构造map集合其实就可以了所以我们围绕的这三件事来做文章首先第一件事根据ID查询权限Promission DO打点find
[01:26] 把ID放进去打点get那这样一来我们能够得到权限对象perm那得到权限对象之后呢我们可以拿到它的tab类型打点get tab那剩下的事情我们可以构造根据类型我们去拿到不同的对象好了object object等于我先写in now好了我这边呢可能就做一个简单的判断iftab
[01:58] 等于等于我们之前写过一个常量类点menu那这个时候呢object它就可以等于我们这边的通过按钮进行查询按钮deal菜单dealpermission menu deal打点find注意他们的id其实都是公用的ok else if那如果你当前的类型呢传递的是这回呢变成了叫做punt我们的
[02:31] 全一点当然全一点我们习惯把它叫做菜单啊这叫做按钮啊其实是一样好了这边呢就可以通过point deal来进行查询当然了还有一个no static method哦抱歉这边应该是小写的pelse if这个都是一模一样的api好了同样的道理同样的类型Ctrl c Ctrl v 拿过来这边呢变成我们叫做api dealapipiapi
[03:15] OK那接下来呢就是else如果真的再传其他的我们就只能抛出异常了死肉new一个common exception抛出异常然后呢在我们的统一常处理里面会对这个异常信息做处理好了result code打点fail搞做一个失败了好了那这个我们看过了之后接下来呢就是说在这儿啊我们开始
[03:46] 拿到了这个数据复制到一个叫做object对象当中那接下来构造map集合那构造map集合呢其实很简单我们之前写过一个叫做binmaputil打点bin2map那么可以把object因为这个类型不明确所以我把这个object给它构造过来那这样一来我得到了一个map集合那剩下呢就是说如果你得到的是一个我们叫做按钮它就有map里面就有按钮的key value
[04:13] 那如果是一个菜单菜单的KL全新APIAPI的KL那这个里面都有了之后注意还没有全线相关的内容所以把全新的内容呢一个一个的加进来其实就可以了打点put那put可能要put很多啊put很多那全线里面的内容呢简单的来看一下有这一大堆这个就是一个我们叫体力活开始call好了可以把全新的name拿过来好了把type拿过来
[04:53] code拿过来description拿过来pid invisible剩下这些我们就可以都删掉了好了但这些值都在哪呢各位是不是都应该在我们这个权限对象所以我一个一个权限打点get去获取就可以了好了打点get name打点get typeok打点get codecode打点get description打点get pid
[05:37] 打点get invisibleOK那这样一来我这个map也构造好了那最后呢我把这个map给它返回即可好了我们这边返回值构造一个map即可好了那这样一来呢注意那这样一来我这个根据ID查询的方法就已经写好了ID查询搞定了那接下来就是最后一个根据ID删除那根据ID删除其实没什么那直接调用Promotion.do
[06:11] 打点delete把ID传下去就可以了这个都比较简单那需要各位注意的是我们根据ID删除我们要做的事情呢首先第一件事跟刚才一样要删除我们的权限那除了删除权限之外还要删除权限删除权限对应的资源所以对于我这个方法呢和之前的增删改查基本上都是一个套路所以我从这边的更新权限这边拿过来一份
[06:41] 拿过来一份进行一个改造就可以了首先根据ID从从我们的数据库里面查权限那查到了权限之后通过权限的类型进行比较进行比较那如果是我们的按钮类型我们从按钮里删从按钮里面删对抱歉这是菜单
[07:14] 那如果是按钮从按钮你删如果是API从API来删如果有问题抛出异常即可那我们删除的逻辑比较简单首先呢我们先把这个权限删掉打点deletebyid permission啊抱歉delete不用byid这个呢对于这个SpringDataGPA而言呢除了根据ID删除之外还可以直接根据对象删啊我直接把对象传过去它也可以删掉好了那接下来呢
[07:47] 针对每一个资源我们就delete by id 了因为 id 都是共享的吧delete by iddelete by id好了 id 传过来传过来如果符合规则它就去删除了好这边是根据 id 查ok那当然了那这样一来呢我整个的这个删除其实也搞定了这个删除呢不难delete by id 等等等等那需要各位注意我们这个里面呢
[08:18] 方法当中的很多都用到了我们的多个表的一个操作所以我上面加一个transactiontransaction代表的是有事物相关的一个支持OK那这样一来我整个这个权限的增深改查的操作就已经都搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过控制器、服务层和数据访问层实现权限模块的增删改查功能，重点是根据权限类型（菜单、按钮、API）动态查询和保存权限数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了权限 API 的文档页面，参数包括 type（权限类型）、pid（父id）、enVisible（是否查询全部权限）。
- type 的可选值：0（菜单）、1（按钮）、3（API接口）。
- enVisible 的可选值：0（查询全部）、1（只查询企业所属权限）。

画面 2：
- 显示了 PermissionController.java 文件中的部分代码，包含 findAll、findById、deleteById 方法。
- 方法签名示例：
  ```java
  @RequestMapping(value = "/permission", method = RequestMethod.GET)
  public Result findAll(@RequestParam Map<String, Object> map) {
      List<Permission> list = permissionService.findAll(map);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable(value = "id") String id) {
      Map map = permissionService.findById(id);
      return new Result(ResultCode.SUCCESS, map);
  }

  @RequestMapping(value = "/permission/{id}", method = RequestMethod.DELETE)
  public Result delete(@PathVariable(value = "id") String id) {
      return new Result(ResultCode.SUCCESS);
  }
  ```

画面 3：
- 显示了 PermissionService.java 文件中的 findId 方法，正在编写根据 type 查询不同权限的逻辑。
- 代码片段：
  ```java
  public Permission findById(String id) {
      permissionDao.findById(id).get();
  }
  ```

画面 4：
- 继续在 PermissionService.java 中编写 findId 方法，使用了 IDE 的自动补全功能。
- 代码片段：
  ```java
  public Permission findById(String id) {
      Permission perm = permissionDao.findById(id).get();
      int type = perm.getType();
      Object object = null;
      if (type == PermissionConstants.PERMISSION_MENU) {
          object = permissionMenuDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_POINT) {
          object = permissionPointDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_API) {
          object = permissionApiDao.findById(id).get();
      } else {
          throw new CommonException(ResultCode.FAIL);
      }
      return permissionDao.findById(id).get();
  }
  ```

画面 5：
- 继续编写 findId 方法，使用了 IDE 的自动补全功能。
- 代码片段：
  ```java
  public Permission findById(String id) {
      Permission perm = permissionDao.findById(id).get();
      int type = perm.getType();
      Object object = null;
      if (type == PermissionConstants.PERMISSION_MENU) {
          object = permissionMenuDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_POINT) {
          object = permissionPointDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_API) {
          object = permissionApiDao.findById(id).get();
      } else {
          throw new CommonException(ResultCode.FAIL);
      }
      return permissionDao.findById(id).get();
  }
  ```

画面 6：
- 继续编写 findId 方法，使用了 IDE 的自动补全功能。
- 代码片段：
  ```java
  public Permission findById(String id) {
      Permission perm = permissionDao.findById(id).get();
      int type = perm.getType();
      Object object = null;
      if (type == PermissionConstants.PERMISSION_MENU) {
          object = permissionMenuDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_POINT) {
          object = permissionPointDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_API) {
          object = permissionApiDao.findById(id).get();
      } else {
          throw new CommonException(ResultCode.FAIL);
      }
      return permissionDao.findById(id).get();
  }
  ```

画面 7：
- 继续编写 findId 方法，使用了 IDE 的自动补全功能。
- 代码片段：
  ```java
  public Permission findById(String id) {
      Permission perm = permissionDao.findById(id).get();
      int type = perm.getType();
      Object object = null;
      if (type == PermissionConstants.PERMISSION_MENU) {
          object = permissionMenuDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_POINT) {
          object = permissionPointDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_API) {
          object = permissionApiDao.findById(id).get();
      } else {
          throw new CommonException(ResultCode.FAIL);
      }
      return permissionDao.findById(id).get();
  }
  ```

画面 8：
- 显示了 Permission.java 文件，定义了权限实体类。
- 代码片段：
  ```java
  @Entity
  @Table(name = "ne_permission")
  @Getter
  @Setter
  @AllArgsConstructor
  @DynamicInsert(true)
  @DynamicUpdate(true)
  public class Permission implements Serializable {
      private static final long serialVersionUID = -4998819027542971546L;
      /**
       * 主键
       */
      @Id
      private String id;
      /**
       * 权限名称
       */
      private String name;
      /**
       * 权限类型 1为菜单 2为功能 3为api
       */
      private Integer type;
      /**
       * 权限编码
       */
      private String code;
      /**
       * 是否可见
       */
      private Integer enVisible;
  }
  ```

画面 9：
- 继续编写 findId 方法，使用了 IDE 的自动补全功能。
- 代码片段：
  ```java
  public Permission findById(String id) {
      Permission perm = permissionDao.findById(id).get();
      int type = perm.getType();
      Object object = null;
      if (type == PermissionConstants.PERMISSION_MENU) {
          object = permissionMenuDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_POINT) {
          object = permissionPointDao.findById(id).get();
      } else if (type == PermissionConstants.PERMISSION_API) {
          object = permissionApiDao.findById(id).get();
      } else {
          throw new CommonException(ResultCode.FAIL);
      }
      return permissionDao.findById(id).get();
  }
  ```

画面 10：
- 显示了 PermissionController.java 文件中的部分代码，包含 findAll、findById、deleteById 方法。
- 方法签名示例：
  ```java
  @RequestMapping(value = "/permission", method = RequestMethod.GET)
  public Result findAll(@RequestParam Map<String, Object> map) {
      List<Permission> list = permissionService.findAll(map);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable(value = "id") String id) {
      Map map = permissionService.findById(id);
      return new Result(ResultCode.SUCCESS, map);
  }

  @RequestMapping(value = "/permission/{id}", method = RequestMethod.DELETE)
  public Result delete(@PathVariable(value = "id") String id) {
      return new Result(ResultCode.SUCCESS);
  }
  ```

画面 11：
- 继续编写 PermissionService.java 文件中的代码，实现了根据权限类型动态保存权限数据的逻辑。
- 代码片段：
  ```java
  permission.setCode(perm.getCode());
  permission.setDescription(perm.getDescription());
  permission.setEnVisible(perm.getEnVisible());
  // 根据类型构造不同的对象
  int type = perm.getType();
  switch (type) {
      case PermissionConstants.PERMISSION_MENU:
          PermissionMenu menu = BeanMapUtils.mapToBean(map, PermissionMenu.class);
          permissionMenuDao.save(menu);
          break;
      case PermissionConstants.PERMISSION_POINT:
          PermissionPoint point = BeanMapUtils.mapToBean(map, PermissionPoint.class);
          point.setId(perm.getId());
          permissionPointDao.save(point);
          break;
      case PermissionConstants.PERMISSION_API:
          PermissionApi api = BeanMapUtils.mapToBean(map, PermissionApi.class);
          api.setId(perm.getId());
          permissionApiDao.save(api);
          break;
      default:
          throw new CommonException(ResultCode.FAIL);
  }
  permissionDao.save(permission);
  ```

画面 12：
- 继续编写 PermissionService.java 文件中的 deleteById 方法，实现了根据权限类型删除权限数据的逻辑。
- 代码片段：
  ```java
  public void deleteById(String id) throws Exception {
      // 通过传递的权限id查询权限
      Permission permission = permissionDao.findById(id).get();
      // 根据类型构造不同的对象
      int type = permission.getType();
      switch (type) {
          case PermissionConstants.PERMISSION_MENU:
              permissionMenuDao.deleteById(id);
              break;
          case PermissionConstants.PERMISSION_POINT:
              permissionPointDao.deleteById(id);
              break;
          case PermissionConstants.PERMISSION_API:
              permissionApiDao.deleteById(id);
              break;
          default:
              throw new CommonException(ResultCode.FAIL);
      }
      // 保存
      permissionDao.save(permission);
  }
  ```

画面 13：
- 继续编写 PermissionService.java 文件中的 deleteById 方法，实现了根据权限类型删除权限数据的逻辑。
- 代码片段：
  ```java
  public void deleteById(String id) throws Exception {
      // 通过传递的权限id查询权限

