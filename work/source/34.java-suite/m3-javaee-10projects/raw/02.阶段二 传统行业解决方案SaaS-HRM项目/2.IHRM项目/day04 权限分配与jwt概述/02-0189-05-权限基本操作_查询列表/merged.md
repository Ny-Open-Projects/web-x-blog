# 05-权限基本操作：查询列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\05-权限基本操作：查询列表_【海量资源尽在 ubkz.com】.mp4
- 时长 8分27秒（音频 507s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 搞定了我们全线的修改和保存之后呢接下来呢我们就关注它的列表那对于这个列表呢其实我们要做的事情呢也比较简单那我们可以看一下API在我们的API部分呢其实它已经把相应的所有的内容都已经给各位列出来了好了来看一下全部列表那在这个列表当中它会传递这么几个参数那这几个参数呢其实以get方式传递过来我们可以把它封装到map集合当中
[00:32] 那我们可以在这边呢思维当中就可以通过map集合的形式构造special case动态去进行查询那type指的是类型那还有附ID还有invisible那这个invisible呢0代表的查询全部其实这个0啊这个查询全部说的不太准确啊那0其实代表的是什么呢就是我只查询一些我们私有的一些权限就是最高的那些那因为这些权限呢可能企业看不到
[00:59] 那1呢其实就是只有企业能够看到的一些玄线如果我不传是不是能够查询全部啊所以这个呢简单的做一个更正好了呢这个我们看过了之后还有一个就是这个tab那这个tab的选项如果传0代表着我要查询菜单跟按钮如果是123那就是常规的
[01:17] 那这些我们做一个留意其实就可以了那接着看返回那返回的内容呢其实有ID, Description, Name, Type, PID Code那这些内容其实只是全线这个表里的内容我们不需要查资源那这个就是我们设计的这个设计的就是这个细节问题就在这儿我全部把一些公共的抽取到了我们全线表里资源表里就是资源的一些属性名称啊那这些我们看过了那我们接下来就可以完成我们这个全部列表的一个查询操作
[01:46] 找到我们的Controller那这边呢没有分页没有sets那么全部都删掉了那我们放到了map集合里面也没问题那好了我们可以调用permission Service打点我们叫做find all把map传过去那我们要得到的是一个list集合per permissionlist好了这边呢我再简单说一下我为什么呢封装一个list集合是因为list集合permission里面有id name typecode
[02:15] 等等等等这些内容那这些内容和我们返回内容的属性一一对应一个一个都能对应那都能对应上那我所以用这样如果对应不上我是不是就已经去自己构造了好了这个我们简单的看了一下然后呢就是Service那在Service里面呢这个都是我们拷过来的一些内容拷过来的一些内容那根据我们查询全部全现这个也不见了好了这里面呢需要我们注意的点呢回到API来看一下把它拷过来
[02:47] 好了靠过来那其中invisible在这好了type那把这个invisible呢简单的说明一下如果它传的1代表的是查询所有查询所有SaaS平台的的权限就是最高权限了那好了接下来呢1查询的就是我们企业的一些权限
[03:23] 当然如果什么都不传我们代表查询全部包含我们SaaS最高的权限还有企业的一些权限因为我们之前知道了对于一个SaaS平台来说呢那可能有一些SaaS平台里面所属的一些权限比如说SaaS管理员他可能要看一下你的企业内容那这些内容那这个菜单可能企业就看不了那同理企业里面比如说企业的一些用户信息那你觉得SaaS管理员可以让他看到吗他不能干扰我们正常企业的一个使用所以他也看不到他们两个是相互割离的当然通过我们这个状态来做的
[03:51] 这个简单的看了一下那接下来呢还有一个叫做PIDPID这个就不用多说了就是负ID因为我们之前就说过权限菜单当中呢它可能有一个负子负子关系那好了这个我们做了一个说明那接下来我们构造查询条件Special Cache那构造查询条件呢首先第一个呢我们比较简单就用PID来做好了里面PIDPIDOK一个改造完成好了那接着第二个Invisible那这个Invisible呢同样如此
[04:24] 同样如此好了如果传了那就传了如果没传那我就不查了代表查询全部好了这个是根据-ID查询好了这个是根据我们叫做invisible查询好了接下来第三个第三个是根据类型那根据类型这个tab来进行查询那根据类型tab来进行查询呢首先呢也是跟这边一样啊跟这边一样如果tab
[05:07] if string then is empty就是如果这玩意儿不为空那不为空的话那我这边呢就需要做一个简单的判断因为这个里面的type有可能是0有可能是1有可能是2有可能是3啊所以这边呢我们简单的来拿一下因为我们构造的map呢全部都构造的成是一个string类型所以我这边呢string类型的tp等于它就拿过来了string类型的
[05:45] 做一个强制转型OK那接下来呢我底下就开始做判断了if注意判断0.ecos tp那0.ecos tp我是不是要查要查两个呀那剩下的这个是不是查一个呀那针对这几个我是不是可以通过一个统一的比如说用in那如果是0我in的里面参数就是2如果是123那我in的参数不就是123吗
[06:14] 那所以我在这边构造其实就是构造in的这种查询其实就可以了那怎么去构造in查询呢那我这边跟各位做一个简单的说明那构造in查询比较简单好了我们的criteriabuilder对象打点它就有一个方法呢叫做in这里面呢可以接收我们的root打点get那我们根据tab属性来进行比较
[06:44] 那注意这样一来呢得到了一个返回值那就是一个叫做ind这么一个类型对象那这个类型对象可以往里面添加你的比较的范围的值比如说ind里面可以添加0我们是不是要比较叫做0的话我们要往里面要填的数据菜单是1按钮是2所以我们这边ind.value1.value2如果你有多个你就继续往下写如果你不想这么写你构造循环一个一个的ind
[07:13] 一个一个的 value其实也可以一模一样好了接下来 else那 else 的就是 int.value那这回 int.value是不是就是这个 type当然这个是一个死菌类型的我们需要把它转化成 integer因为我们知道 type 是一个 int 类型所以呢我来个 integer.parents好了把 tp 传进去 ok那这样一来我这个查询 specification 构造好了那构造好了之后我们底下呢直接返回通过
[07:43] Promission丢打点FindFindAll然后呢把我们这个Special Cache放进去即可这边FindAll这边呢返回值也要改一下PromissionOK好了那这样一来我这个Service构造成功了那我们这个Controller这边Controller这边需要构造一点点简单内容好了那这样一来呢我们都已经把代码就已经都写好了
[08:19] 那我们这个列表写好了之后接下来呢我们关注的就是根据ID查询

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

