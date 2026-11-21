# 画面线理解：16-POI文件导入：代码实现-解析Excel构造用户列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\16-POI文件导入：代码实现-解析Excel构造用户列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 01:13, 01:47, 02:50, 03:57, 04:38, 05:12, 06:44, 07:27, 08:21, 09:13, 09:56, 10:45, 11:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:57:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过 Controller 层读取 Excel 文件并解析数据，同时展示如何使用 Feign 客户端调用远程服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 在 IntelliJ IDEA 中打开 UserContoller.java 文件。
- 代码中定义了三个 @Autowired 注入的成员变量：PermissionService、JwtUtils、DepartmentFeignClient。
- 定义了两个方法：importUser 用于导入 Excel 文件，testFeign 用于测试 Feign 客户端。

画面 2:
- 弹出“Select Classes to Import”对话框，提示导入缺失的 Apache POI 类库。
- 选中 org.apache.poi.ss.usermodel.Cell、org.apache.poi.ss.usermodel.Row、org.apache.poi.ss.usermodel.Sheet 三个类。

画面 3:
- 显示一个 Excel 文件“导入测试模板.xlsx”，其中包含用户数据，列标题包括：用户名、手机号、工号、聘用形式、入职时间、部门编码。

画面 4:
- 在 UserContoller.java 中，代码正在实现 importUser 方法。
- 代码注释说明：1.1. 解析 Excel 文件创建工作簿，1.2. 获取 Sheet，2. 获取用户数据列表，3. 批量保存用户。

画面 5:
- 显示 Excel 文件“导入测试模板.xlsx”，光标位于单元格 A18。

画面 6:
- 在 UserContoller.java 中，代码正在实现 importUser 方法。
- 代码注释说明：1.1. 解析 Excel 文件创建工作簿，1.2. 获取 Sheet，2. 获取用户数据列表，3. 批量保存用户。
- 代码中新增了 List<User> list = new ArrayList<>(); 用于存储用户数据。

画面 7:
- 显示 Excel 文件“导入测试模板.xlsx”，光标位于单元格 A20。

画面 8:
- 在 UserContoller.java 中，代码正在实现 importUser 方法。
- 代码注释说明：1.1. 解析 Excel 文件创建工作簿，1.2. 获取 Sheet，2. 获取用户数据列表，3. 批量保存用户。
- 代码中新增了 User user = new User(); 用于创建用户对象。

画面 9:
- 显示 Excel 文件“导入测试模板.xlsx”，光标位于单元格 B2。

画面 10:
- 在 IntelliJ IDEA 中打开 User.java 文件。
- 代码中定义了 User 类的属性，包括 departmentName、level、username、mobile、workNumber、formOfEmployment、timeOfEntry、roles。
- 代码中使用了 @JsonIgnore、@ManyToMany、@JoinTable 等注解。

画面 11:
- 在 IntelliJ IDEA 中打开 User.java 文件。
- 代码中定义了 User 类的属性，包括 departmentName、level、username、mobile、workNumber、formOfEmployment、timeOfEntry、roles。
- 代码中使用了 @JsonIgnore、@ManyToMany、@JoinTable 等注解。
- 代码中新增了 this.workNumber = values[2].toString(); 用于设置工号。

画面 12:
- 在 IntelliJ IDEA 中打开 User.java 文件。
- 代码中定义了 User 类的属性，包括 departmentName、level、username、mobile、workNumber、formOfEmployment、timeOfEntry、roles。
- 代码中使用了 @JsonIgnore、@ManyToMany、@JoinTable 等注解。
- 代码中新增了 this.timeOfEntry = (Date) values[4]; 用于设置入职时间。

画面 13:
- 在 IntelliJ IDEA 中打开 User.java 文件。
- 代码中定义了 User 类的属性，包括 departmentName、level、username、mobile、workNumber、formOfEmployment、timeOfEntry、roles。
- 代码中使用了 @JsonIgnore、@ManyToMany、@JoinTable 等注解。
- 代码中新增了 this.formOfEmployment = (String) values[3]; 用于设置聘用形式。

画面 14:
- 在 UserContoller.java 中，代码正在实现 importUser 方法。
- 代码注释说明：1.1. 解析 Excel 文件创建工作簿，1.2. 获取 Sheet，2. 获取用户数据列表，3. 批量保存用户。
- 代码中新增了 Object value = null; 用于初始化单元格值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1:
```java
@Autowired
private PermissionService permissionService;

@Autowired
private JwtUtils jwtUtils;

@Autowired
private DepartmentFeignClient departmentFeignClient,

@RequestMapping(value = "/user/import", method = RequestMethod.POST)
public Result importUser(@RequestParam(name = "file") MultipartFile file) {
    //1.解析Excel
    return new Result(ResultCode.SUCCESS);
}

/**
 * 调试Feign组件
 * 调用系统微服务的/tost接口上传部门id，通过feign部门服务获取部门信息
 */
@RequestMapping(value = "/test/{id}", method = RequestMethod.GET)
public Result testFeign(@PathVariable(value = "id") String id) {
    Result result = departmentFeignClient.FindById(id);
}
```

画面 2:
```java
org.apache.poi.ss.usermodel.Cell
org.apache.poi.ss.usermodel.Row
org.apache.poi.ss.usermodel.Sheet
```

画面 4:
```java
@RequestMapping(value = "/user/import", method = RequestMethod.POST)
public Result importUser(@RequestParam(name = "file") MultipartFile file) throws Exception {
    //1.解析Excel文件创建工作簿
    Workbook wb = new XSSFWorkbook(file.getInputStream());
    //1.2.获取Sheet
    Sheet sheet = wb.getSheetAt(0); //获取第一个Sheet
    //2.获取用户数据列表
    List<User> list = new ArrayList<>();
    for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) {
        Row row = sheet.getRow(rowNum);
        for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
            Cell cell = row.getCell(cellNum);
            Object value = getCellValue(cell);
            sb.append(value).append("-");
        }
        System.out.println(sb.toString());
    }
    //3.批量保存用户
    return new Result(ResultCode.SUCCESS);
}
```

画面 6:
```java
//2.获取用户数据列表
List<User> list = new ArrayList<>();
for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) {
    Row row = sheet.getRow(rowNum);
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum);
        Object value = getCellValue(cell);
        values[cellNum] = value;
    }
    User user = new User();
    list.add(user);
}
//3.批量保存用户
return new Result(ResultCode.SUCCESS);
```

画面 8:
```java
//2.获取用户数据列表
List<User> list = new ArrayList<>();
for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) {
    Row row = sheet.getRow(rowNum);
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum);
        Object value = getCellValue(cell);
        values[cellNum] = value;
    }
    User user = new User();
    list.add(user);
}
//3.批量保存用户
return new Result(ResultCode.SUCCESS);
```

画面 10:
```java
private String departmentName;
private String level;
private String username;
private String mobile;
private String workNumber;
private String formOfEmployment;
private Date timeOfEntry;
private Set<Role> roles = new HashSet<>();
```

画面 11:
```java
private String departmentName;
private String level;
private String username;
private String mobile;
private String workNumber;
private String formOfEmployment;
private Date timeOfEntry;
private Set<Role> roles = new HashSet<>();
```

画面 12:
```java
private String departmentName;
private String level;
private String username;
private String mobile;
private String workNumber;
private String formOfEmployment;
private Date timeOfEntry;
private Set<Role> roles = new HashSet<>();
```

画面 13:
```java
private String departmentName;
private String level;
private String username;
private String mobile;
private String workNumber;
private String formOfEmployment;
private Date timeOfEntry;
private Set<Role> roles = new HashSet<>();
```

画面 14:
```java
//2.获取用户数据列表
List<User> list = new ArrayList<>();
for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) {
    Row row = sheet.getRow(rowNum);
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum);
        Object value = getCellValue(cell);
        values[cellNum] = value;
    }
    User user = new User();
    list.add(user);
}
//3.批量保存用户
return new Result(ResultCode.SUCCESS);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价
