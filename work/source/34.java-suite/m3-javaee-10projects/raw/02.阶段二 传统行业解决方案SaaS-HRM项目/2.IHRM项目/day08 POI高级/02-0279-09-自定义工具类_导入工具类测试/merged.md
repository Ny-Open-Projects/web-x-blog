# 09-自定义工具类：导入工具类测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\09-自定义工具类：导入工具类测试_【海量资源尽在 ubkz.com】.mp4
- 时长 6分1秒（音频 362s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 使用工具类完成了一个报表导出接下来还有一个工具类就是做一个上传导入的这么一个工具类我们一起来看一下如何去用其实也比较简单找到我们昨天写的批量注册上传注册的这么一个方法在这个方法里面我们开始使用工具类来完成使用工具类的形式如何去做咱们这个工具类也写过叫做ExcelExcelImportUtil
[00:31] 那我们可以new一个import utils出来好了new的过程当中我们一起来看一下这个工程呢需要这么一个构造方法一个参数那这个参数就是说你希望把你上传的这个报表每一行给它构造成哪个对象你就把哪个对象的字节码写过来那我们昨天呢上传的是一个excel报表那这个excel报表呢我们一起来找一下好了就是导入模板的这个数据就在这儿那我们
[01:03] 知道了每一行是不是应该把它封装成一个user对象就可以啊所以呢我这边new对象的时候各位就比较明确了要写一个user.class好了user.class继续打点我们调用里面的read excel方法这个read excel方法呢简单的对里面的参数做一个说明好了其中的第一个叫做as第二个叫做row indexrow index好了第三个叫做cellindex那这几个参数呢做一个简单的
[01:36] 说明那第一个参数S其实就是我们文件上传的文件上传的就是流信息就是我们的文件流好了接着rowindexrowindex是这样的就是说我们导入数据的这个里面我们要进行读取你这个数据应该从第几行开始读那对于我们来说01是不是应该从第一行进行读取得到里面的TET001
[02:06] 得到第一行数据所以呢这个肉index指的是我们读取数据的起始行起始行那除了读取数据的起始行之外那底下是不是每一列也有一个表格它的一个起始的一个表格的一个行啊好了好了接下来就是读取数据的叫做起始单元格位置OK那好了接下来呢这一期
[02:40] 都比较简单都比较简单那接下来我们要做的事情就很简单了调用里面的方法一个一个来构造首先第一个参数我们知道是一个文件流那文件流可以通过fill打点get input stream那接下来呢就是说我这里面的行01列01是不是都应该是1都好1没错吧那这样一来我整个读取就可以都省略了那我们直接可以通过我们的方法得到
[03:12] user-list-gehe好了但是呢如果想要这个方法能够正常运行的话还需要对你的这个user.class里面使用注解进行一个简单的配置那这个注解呢如何去配置呢其实就是我们刚才说过的你这个用户名这个对应的是哪个字段那这个属性上给他来一个注解来进行声明就可以了我们的用户名称有的nameat excel attributesort应该就是注意0
[03:41] 是不是1啊OK1好了接下来呢这边手机号继续找位置012那这个就应该是2当然了还有公号work number这个应该就是3了0123好了拼用形式好了在上面4好了入职时间time在这那这个就是5好了最后一个
[04:17] 部门编码因为我们说过了部门编码先给它放到ID这个属性上那我们这边写一个6OK那这样一来我这边呢也已经都搞定了搞定了之后我们把这个用户微服再重新启动一下来看一下能不能够批量的把用户注册上来OK而这边呢已经开始启动了我呢打开页面准备进行数据的一个好了刷新一把这边登录失败了OK02进来员工
[04:52] 好了导入一些数据但是在导入数据之前呢我们先打开数据库啊找到用户把里面这三个先给它删掉先给它删掉因为呢防止会有一些影响好了接着往里导入我们的导入数据模板好了已经导入成功我们来看一下数据库表里面的数据究竟对不对刷新一把你发现123TESTVOK都有没有问题那我们
[05:26] 现在已经可以使用工具类的形式完成导入以及导出的这些操作了其实我们这个工具类可以涵盖我们整个系统里面的基本上大部分的Excel导入以及导出只需要满足我们的使用规则其实就可以了当然在这边我们的代码写的相对来说还是比较简单的如果各位朋友想要了解一下代码究竟是怎么构成的其实可以看一下这个原码它都不难并且各位都能够理解
[05:56] OK那这样一来我们整个工具类的这一块呢就跟各位都说过了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过自定义注解和工具类实现 Excel 数据导入功能，并展示其在实际项目中的应用。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了 IntelliJ IDEA 中的项目结构，选中了 `UserController.java`。
- 代码内容：`@RequestMapping(value="/user/import",method = RequestMethod.POST) public Result importUser(@RequestParam(name="file") MultipartFile file) throws Exception { Workbook wb = new XSSFWorkbook(file.getInputStream()); Sheet sheet = wb.getSheetAt(0); List<User> list = new ArrayList<>(); for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) { Row row = sheet.getRow(rowNum); Object[] values = new Object[row.getLastCellNum()]; for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) { Cell cell = row.getCell(cellNum); Object value = getCellValue(cell); values[cellNum] = value; } User user = new User(values); list.add(user); } userService.saveAll(list,companyId,companyName); return new Result(ResultCode.SUCCESS); }`

画面2：
- 展示了 `ExcelImportUtil.java` 文件内容。
- 代码内容：`package com.ihm.common.poi; import ... public class ExcelImportUtil<T> { private Class<T> clazz; private Field fields[]; @SuppressWarnings("unchecked") public ExcelImportUtil(Class<T> clazz) { this.clazz = clazz; fields = clazz.getDeclaredFields(); } /** * 基于解析excel */ public List<T> readExcel(InputStream is, int rowIndex,int cellIndex) { List<T> list = new ArrayList<>(); T entity = null; try { XSSFWorkbook workbook = new XSSFWorkbook(is); Sheet sheet = workbook.getSheetAt(0); for (int rowNum = rowIndex; rowNum <= sheet.getLastRowNum(); rowNum++) { Row row = sheet.getRow(rowNum); entity = (T) clazz.newInstance(); System.out.println(row.getLastCellNum()); for (int j = cellIndex; j < row.getLastCellNum(); j++) { Cell cell = row.getCell(j); if (field.annotationPresent(ExcelAttribute.class)) { field.setAccessible(true); } } } } catch (Exception e) { e.printStackTrace(); } return list; } }`

画面3：
- 展示了 `UserControll.java` 中的 `importUser` 方法，与画面1内容基本一致，但注释更详细。
- 代码内容：`@RequestMapping(value="/user/import",method = RequestMethod.POST) public Result importUser(@RequestParam(name="file") MultipartFile file) throws Exception { //1.根据Excel文件创建工作簿 Workbook wb = new XSSFWorkbook(file.getInputStream()); //2.获取sheet Sheet sheet = wb.getSheetAt(0); //3.读取sheet中的每一个行，和每一个单元格 List<User> list = new ArrayList<>(); for (int rowNum = 1; rowNum < sheet.getLastRowNum(); rowNum++) { Row row = sheet.getRow(rowNum); Object[] values = new Object[row.getLastCellNum()]; for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) { Cell cell = row.getCell(cellNum); Object value = getCellValue(cell); values[cellNum] = value; } User user = new User(values); list.add(user); } //3.批量存用户 userService.saveAll(list,companyId,companyName); return new Result(ResultCode.SUCCESS); }`

画面4：
- 展示了在 `ExcelImportUtil` 类中，通过右键“Copy Class”功能，将类复制到 `com.ihm.common.poi` 包下。
- 弹窗内容：`Copy class com.ihm.common.poi.ExcelImportUtil New name: ExcelImportUtil Destination package: com.ihm.common.poi Target destination directory: ...ihm_common/src/main/java/com/ihm/common/poi`

画面5：
- 展示了 Excel 文件 `导入测试模板.xlsx` 的内容，包含“用户名”、“手机号”、“工号”、“聘用形式”、“入职时间”、“部门编码”等列。
- 表格数据：A1: 用户名, B1: 手机号, C1: 工号, D1: 聘用形式, E1: 入职时间, F1: 部门编码。A2: test001, B2: 13900000001, C2: 2001, D2: 1, E2: 2018/1/1, F2: DEPT-DEV。A3: test002, B3: 13900000002, C3: 2002, D3: 1, E3: 2018/1/1, F3: DEPT-DEV。A4: test003, B4: 13900000003, C4: 2003, D4: 1, E4: 2018/1/1, F4: DEPT-DEV。

画面6：
- 展示了 Excel 文件中“工号”列（C列）的选中状态。

画面7：
- 展示了 `User.java` 类的代码，其中包含 `@ExcelAttribute(sort = 6)` 注解用于“部门ID”，以及 `@ExcelAttribute(sort = 5)` 注解用于“入职时间”。
- 代码内容：`@NoArgsConstructor public class User implements Serializable { private static final long serialVersionUID = 4297464181893878307L; @Id private String id; /** * 手机号码 */ private String mobile; /** * 用户名 */ private String username; /** * 密码 */ private String password; /** * 启用状态 0为禁用 1为启用 */ private Integer enableState; private Date createTime; private String companyId; private String companyName; @ExcelAttribute(sort = 6) private String departmentId; @ExcelAttribute(sort = 5) private Date hireTime; }`

画面8：
- 展示了 Excel 文件中“用户名”列（B列）的选中状态。

画面9：
- 展示了 Excel 文件中“工号”列（C列）的选中状态。

画面10：
- 展示了项目运行日志，显示服务正在启动并解析 Eureka 端点。
- 日志内容：`2018-12-19 21:44:45.631 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving Eureka endpoints via configure`

画面11：
- 展示了登录页面，用户名为“USR00000001”，密码已输入，点击“登录”按钮。
- 页面内容：用户名输入框显示“USR00000001”，密码输入框显示“••••••”，下方有“登录”按钮。

画面12：
- 展示了文件选择对话框，用户正在选择“导入测试模板.xlsx”文件。
- 对话框内容：文件名输入框为空，下方有“打开”和“取消”按钮。

画面13：
- 展示了 `ExcelImportUtil.java` 文件中 `convertAttrType` 方法的代码。
- 代码内容：`if (field == null) { System.out.println(convertAttrType(field, cell)); field.set(entity, convertAttrType(field, cell)); } catch (Exception e) { e.printStackTrace(); } return list; } /** * 类型转换，将cell单元格格式转为字段类型 */ private Object convertAttrType(Field field, Cell cell) throws Exception { String fieldType = field.getType().getSimpleName(); if ("String".equals(fieldType)) { return getValue(cell); } else if ("Date".equals(fieldType)) { return new SimpleDateFormat(pattern).parse

