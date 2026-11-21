# 画面线理解：09-自定义工具类：导入工具类测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\09-自定义工具类：导入工具类测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:38, 01:10, 01:38, 02:20, 02:56, 03:25, 03:47, 04:06, 04:26, 04:46, 05:08, 05:46, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:10:42

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
- 日志内容：`2018-12-19 21:44:45.631 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure 2018-12-19 21:44:45.655 INFO 200 - trap-executor-0] c.n.d.s.a.w.ConfigClusterResolver: Resolving eureka endpoints via configure`

画面11：
- 展示了登录页面，用户名为“USR00000001”，密码已输入，点击“登录”按钮。
- 页面内容：用户名输入框显示“USR00000001”，密码输入框显示“••••••”，下方有“登录”按钮。

画面12：
- 展示了文件选择对话框，用户正在选择“导入测试模板.xlsx”文件。
- 对话框内容：文件名输入框为空，下方有“打开”和“取消”按钮。

画面13：
- 展示了 `ExcelImportUtil.java` 文件中 `convertAttrType` 方法的代码。
- 代码内容：`if (field == null) { System.out.println(convertAttrType(field, cell)); field.set(entity, convertAttrType(field, cell)); } catch (Exception e) { e.printStackTrace(); } return list; } /** * 类型转换，将cell单元格格式转为字段类型 */ private Object convertAttrType(Field field, Cell cell) throws Exception { String fieldType = field.getType().getSimpleName(); if ("String".equals(fieldType)) { return getValue(cell); } else if ("Date".equals(fieldType)) { return new SimpleDateFormat(pattern).parse
