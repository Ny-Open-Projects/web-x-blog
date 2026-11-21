# 画面线理解：05-权限基本操作：查询列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\05-权限基本操作：查询列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:03, 01:10, 01:55, 02:11, 02:30, 02:50, 04:49, 05:29, 06:31, 07:08, 07:31, 07:45, 08:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:51:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Controller 层定义权限相关的 REST API，并在 Service 层使用 Specification 动态构建查询条件，实现对权限数据的增删改查功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 PermissionController.java 文件中的三个 HTTP 方法：POST 用于保存权限，PUT 用于更新权限，GET 用于查询权限列表。
- 代码片段：
  ```java
  @RequestMapping(value = "/permission", method = RequestMethod.POST)
  public Result save(@RequestBody Map<String, Object> map) throws Exception {
      permissionService.save(map);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/permission/{id}", method = RequestMethod.PUT)
  public Result update(@PathVariable(value = "id") String id, @RequestBody Map<String, Object> map) throws Exception {
      map.put("id", id);
      permissionService.update(map);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/permission", method = RequestMethod.GET)
  public Result findAll(int page, int size, @RequestParam Map map) {
      return new Result(ResultCode.SUCCESS);
  }
  ```

画面 2：
- 显示 API 文档页面，展示 GET /permission 接口的参数说明。
- 参数包括：
  - type：权限类型（0：菜单+按钮，1：菜单，2：按钮，3：API接口）
  - pid：父id
  - enVisible：是否查询全部权限（0：查询全部，1：只查询企业所属权限）
- 响应类型为 application/json。

画面 3：
- 显示 PermissionController.java 文件中，对 findAll 方法的光标定位，准备查看其 Service 层实现。
- 同时显示了 IDE 的自动补全建议，包括 PermissionService、PermissionController、PaintEvent、Package、ParseException 等类。

画面 4：
- 显示 Permission.java 文件，定义了权限实体类。
- 代码片段：
  ```java
  @Entity
  @Table(name = "pe_permission")
  @Setter
  @Getter
  @NoArgsConstructor
  @DynamicInsert(true)
  @DynamicUpdate(true)
  public class Permission implements Serializable {
      private static final long serialVersionUID = 4999819027542971546L;
      @Id
      private String id;
      private String name;
      private Integer type;
      private String code;
  }
  ```

画面 5：
- 显示 PermissionService.java 文件中，findById 方法的实现。
- 代码片段：
  ```java
  public Permission findById(String id) {
      return permissionDao.findById(id).get();
  }
  ```

画面 6：
- 显示 PermissionService.java 文件中，findAll 方法的实现，开始构建动态查询条件。
- 代码片段：
  ```java
  public Page findAll(Map<String, Object> map, int page, int size) {
      //1.准备查询条件
      Specification<Permission> spec = new Specification<Permission>() {
          @Override
          public Predicate toPredicate(Root<Permission> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
              List<Predicate> list = new ArrayList<>();
              //根据id查询
              if (!StringUtils.isEmpty(map.get("id"))) {
                  list.add(criteriaBuilder.equal(root.get("id").as(String.class), (String) map.get("id")));
              }
              //根据公司id查询
              if (!StringUtils.isEmpty(map.get("companyId"))) {
                  list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
              }
              //根据部门id查询
              if (!StringUtils.isEmpty(map.get("departmentId"))) {
                  list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String) map.get("departmentId")));
              }
              //根据岗位id查询
              if (!StringUtils.isEmpty(map.get("postId"))) {
                  list.add(criteriaBuilder.equal(root.get("postId").as(String.class), (String) map.get("postId")));
              }
              //根据角色id查询
              if (!StringUtils.isEmpty(map.get("roleId"))) {
                  list.add(criteriaBuilder.equal(root.get("roleId").as(String.class), (String) map.get("roleId")));
              }
              //根据权限类型查询
              if (!StringUtils.isEmpty(map.get("type"))) {
                  String ty = (String) map.get("type");
                  if ("0".equals(ty)) {
                      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
                  } else {
                      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
                  }
              }
              return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
          }
      };
      return permissionDao.findAll(spec, new Pageable(page - 1, size));
  }
  ```

画面 7：
- 显示 PermissionService.java 文件中，构建动态查询条件的代码，重点处理 type 参数。
- 代码片段：
  ```java
  if (!StringUtils.isEmpty(map.get("type"))) {
      String ty = (String) map.get("type");
      if ("0".equals(ty)) {
          list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
      } else {
          list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
      }
  }
  ```

画面 8：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```

画面 9：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```

画面 10：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```

画面 11：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```

画面 12：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```

画面 13：
- 显示 PermissionService.java 文件中，对 type 参数的处理逻辑，使用 String 类的 equals 方法进行比较。
- 代码片段：
  ```java
  if ("0".equals(ty)) {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "0"));
  } else {
      list.add(criteriaBuilder.equal(root.get("type").as(String.class), "1"));
  }
  ```
