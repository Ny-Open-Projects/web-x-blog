# 画面线理解：06-权限基本操作：根据id查询和删除

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\06-权限基本操作：根据id查询和删除_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:46, 01:26, 01:52, 02:13, 02:51, 03:33, 04:32, 05:16, 05:52, 06:37, 07:07, 07:51, 08:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:52:11

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
