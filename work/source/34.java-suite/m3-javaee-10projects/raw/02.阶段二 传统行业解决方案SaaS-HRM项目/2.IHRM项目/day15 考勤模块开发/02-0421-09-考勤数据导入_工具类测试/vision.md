# 画面线理解：09-考勤数据导入：工具类测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\09-考勤数据导入：工具类测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:38, 00:55, 01:36, 02:15, 02:51, 04:12, 04:28, 04:53, 05:36, 06:00, 06:18, 07:33, 08:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:34:38

1) 这一组画面整体在讲如何使用 Java 的 POI 库读取 Excel 文件并映射到 Java 对象。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个 Excel 文件，包含员工姓名、手机号、工号、上班时间、下班时间等列，其中第一行是表头，第二行是数据。
画面2：在 IntelliJ IDEA 中打开 `ExcelImportUtil.java` 文件，展示读取 Excel 的核心方法 `readExcel` 的代码，其中包含对 `XSSFWorkbook`、`Sheet`、`Row`、`Cell` 的操作，以及通过注解 `@ExcelAttribute` 自动映射字段。
画面3：在 IntelliJ IDEA 中展示项目结构，选中 `po` 包，该包下包含 `AtteUploadVo` 等 VO 类。
画面4：展示 Excel 文件，其中员工姓名列被选中，数据行完整显示。
画面5：在 IntelliJ IDEA 中切换到 `ihrm_common_model` 模块，展示项目结构。
画面6：在 IntelliJ IDEA 中打开 `AtteUploadVo.java` 文件，展示 VO 类的定义，包含 `@ExcelAttribute` 注解指定字段映射关系。
画面7：在 IntelliJ IDEA 中打开 `PoTest.java` 文件，准备编写测试代码。
画面8：在 IntelliJ IDEA 中运行 `PoTest.java`，出现 `Exception` 异常列表，提示缺少依赖或配置。
画面9：在 IntelliJ IDEA 中展示 `PoTest.java` 代码，使用 `ExcelImportUtil` 实例化并调用 `readExcel` 方法。
画面10：展示桌面，有“黑马程序员”和“博学谷”的标志。
画面11：在 IntelliJ IDEA 中展示 `PoTest.java` 代码，使用 `new FileInputStream` 创建输入流。
画面12：在 Windows 资源管理器中展示项目文件夹，包含 `demo.xlsx` 文件。
画面13：在 IntelliJ IDEA 中展示 `PoTest.java` 代码，使用 `FileInputStream` 读取 `demo.xlsx` 文件。
画面14：在 IntelliJ IDEA 中展示 `PoTest.java` 代码，编译成功，准备运行。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```java
this.clazz = clazz;
fields = clazz.getDeclaredFields();
...
public List<T> readExcel(InputStream is, int rowIndex,int cellIndex) {
    List<T> list = new ArrayList<T>();
    entity = null;
    try {
        XSSFWorkbook workbook = new XSSFWorkbook(is);
        Sheet sheet = workbook.getSheetAt(index);
        for (int rowNum = rowHeader; rowNum < sheet.getLastRowNum(); rowNum++) {
            Row row = sheet.getRow(rowNum);
            entity = (T) clazz.newInstance();
            for (int j = cellIndex; j < row.getLastCellNum(); j++) {
                Cell cell = row.getCell(j);
                if(field.isAnnotationPresent(ExcelAttribute.class)){
                    field.setAccessible(true);
                    ExcelAttribute ea = field.getAnnotation(ExcelAttribute.class);
                    if(j == ea.sort()){
                        System.out.println(convertAttrType(field, cell));
                        field.set(entity, convertAttrType(field, cell));
                    }
                }
            }
            list.add(entity);
        }
    }
}
```

画面6：
```java
package com.ihrm.attendance.vo;
@Data
@ToString
public class AtteUploadVo {
    //员工姓名，手机号，工号，上班时间，下班时间
    @ExcelAttribute(sort=0,format="String")
    private String username;
    @ExcelAttribute(sort=1,format="String")
    private String mobile;
    @ExcelAttribute(sort=2,format="String")
    private String workNumber;
    @ExcelAttribute(sort=3,format="Date")
    private Date inLine;
    @ExcelAttribute(sort=4,format="Date")
    private Date outLine;
}
```

画面9：
```java
import com.ihrm.common.poi.ExcelImportUtil;
import com.ihrm.domain.atte.vo.AtteUploadVo;
...
public class PoTest {
    public static void main(String[] args) {
        ExcelImportUtil<Object> util = new ExcelImportUtil<>(AtteUploadVo.class);
        util.readExcel(input, rowindex, cellindex);
    }
}
```

画面13：
```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
...
public class PoTest {
    public static void main(String[] args) throws FileNotFoundException {
        ExcelImportUtil<AtteUploadVo> util = new ExcelImportUtil<>(AtteUploadVo.class);
        FileInputStream stream = new FileInputStream(new File("E:\\demo.xlsx"));
        List<AtteUploadVo> list = util.readExcel(stream, rowindex: 1, cellindex: 0);
        for (AtteUploadVo atteUploadVo : list) {
            System.out.println(atteUploadVo);
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
