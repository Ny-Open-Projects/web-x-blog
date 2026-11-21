# 画面线理解：day10-17-投标预览-接口3-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-17-投标预览-接口3-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:06, 01:51, 03:13, 04:09, 04:45, 05:14, 05:39, 06:17, 06:54, 07:22, 08:16, 08:56, 09:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:27:36

1) 这一组画面整体在讲用户中心服务中获取借款人信息接口的实现，包括接口定义、服务层代码、数据传输对象（DTO）设计及数据库表结构。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了用户投标业务的系统架构图，包含“浏览器/APP”、“交易中心”、“用户服务”、“存管代理服务”和“存管系统”五个模块，以及接口①至⑤的调用流程。
画面2: 展示了文档中“2.2.4 用户中心获取借款人信息接口(接口③)”的章节，其中包含在ConsumerService接口中新增getBorrower方法的定义，以及在ConsumerServiceImpl中实现该方法的代码片段。
画面3: 展示了IDE中ConsumerServiceImpl类的代码，其中包含了@Autowired注解注入的多个服务对象，如accountAgent、bankCardService等。
画面4: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面5: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面6: 展示了BorrowerDTO类的定义，其中包含多个@ApiModelProperty注解，用于描述字段如“用户id”、“用户名”、“真实姓名”、“身份证号”、“手机号”等。
画面7: 展示了数据库管理工具中consumer表的结构，包含字段如id、borrower_id、full_name、mobile等。
画面8: 展示了BorrowerDTO类中“性别”字段的定义，使用@ApiModelProperty注解。
画面9: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面10: 展示了IDCardUtil类中的getInfo方法，用于从身份证号中提取年龄、生日和性别。
画面11: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面12: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面13: 展示了ConsumerServiceImpl类中getBorrower方法的实现，其中包含对ConsumerDTO的获取和转换为BorrowerDTO。
画面14: 展示了ConsumerController类中getBorrower方法的实现，其中包含@Operation注解和@GetMapping注解，用于定义接口路径和参数。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```java
/**
 * 获取借款人基本信息
 * @param id
 * @return
 */
BorrowerDTO getBorrower(Long id);

@Override
public BorrowerDTO getBorrower(Long id) {
    ConsumerDTO consumerDTO = get(id);
    BorrowerDTO borrowerDTO = new BorrowerDTO();
    BeanUtils.copyProperties(consumerDTO, borrowerDTO);
    Map<String, String> cardInfo = IDCardUtil.getInfo(borrowerDTO.getIdNumber());
    borrowerDTO.setAge(cardInfo.get("age"));
    borrowerDTO.setBirthday(cardInfo.get("birthday"));
    borrowerDTO.setGender(cardInfo.get("gender"));
    return borrowerDTO;
}
```

画面6:
```java
@ApiModel(value = "BorrowerDTO", description = "借款人用户信息")
public class BorrowerDTO {

    @ApiModelProperty("用户id")
    private Long id;

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("真实姓名")
    private String fullname;

    @ApiModelProperty("身份证号")
    private String idNumber;

    @ApiModelProperty("手机号")
    private String mobile;

    @ApiModelProperty("年龄")
    private Integer age;

    @ApiModelProperty("生日")
    private String birthday;

    @ApiModelProperty("性别")
    private String gender;
}
```

画面7:
```sql
Columns (13)
Field          Type          Comment
id             bigint(20)    主键
borrower_id    varchar(50)   借款人id
full_name      varchar(50)   借款人姓名
mobile         varchar(50)   手机号
user_type      varchar(50)   用户类型
role           varchar(50)   角色
auto_list      varchar(50)   自动列表
to_dir_card    varchar(50)   转入卡号
load_amount    decimal(10,6) 可贷金额
status         varchar(50)   状态
```

画面10:
```java
public static Map<String, String> getInfo(String idNumber) {
    String birthday = "";
    String age = "";
    String gender = "";
    int year = Calendar.getInstance().get(Calendar.YEAR);
    if (idNumber.length() == 15) {
        birthday = "19" + idNumber.substring(6, 8) + "-" + idNumber.substring(8, 10) + "-" + idNumber.substring(10, 12);
        age = (year - Integer.parseInt(idNumber.substring(6, 8))) + "";
    } else if (idNumber.length() == 18) {
        birthday = idNumber.substring(6, 10) + "-" + idNumber.substring(10, 12) + "-" + idNumber.substring(12, 14);
        age = (year - Integer.parseInt(idNumber.substring(6, 10))) + "";
        gender = idNumber.substring(16, 17);
        if (Integer.parseInt(idNumber.substring(16, 17)) % 2 == 0) {
            gender = "女";
        } else {
            gender = "男";
        }
    }
    Map<String, String> map = new HashMap<>();
    map.put("birthday", birthday);
    map.put("age", age);
    map.put("gender", gender);
    return map;
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 架构图结构：
- “浏览器/APP”指向“交易中心”（接口①）
- “交易中心”指向“用户服务”（接口②）
- “用户服务”指向“存管代理服务”（接口③）
- “存管代理服务”指向“存管系统”（接口⑤）
- “用户服务”指向“存管代理服务”（接口④）
- “存管代理服务”指向“存管系统”（接口⑤）
- “用户服务”指向“存管代理服务”（接口④）
- “存管代理服务”指向“存管系统”（接口⑤）

5) 无。
