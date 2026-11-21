# day10-17-投标预览-接口3-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-17-投标预览-接口3-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 10分1秒（音频 601s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把接口二这块功能搞定了也测试通过那接下来呢咱开始开发接口三这块功能那么接口三这个功能也比较简单它只是查询借款人的信息啊对应的前端界面是这你看这是原始借款人什么信息在这展示他的一些基本信息就可以了所以也是一个查询但是有一个细节大家需要注意啊接口三我们在查询的时候是跟谁打交道啊用户中心啊
[00:29] 你看咱前两个功能是不是都是跟什么交易中心所以说这个你要注意一下那也是一个查询用户中心这边DU层的代码我们还用编写不用了consumer那边我们是不是老早都已经开发过这个什么DU层了所以说我们直接从业务层开始就行了那老套路业务层也是接口里边先定一个方法然后在实现类当中实现这个方法就行了我们找到业务层的
[00:59] 接口那我们需要新增一个什么呀获取借款人信息的方法好咱看看讲义很简单来咱把这块拿过来瞅一眼啊好大家看一下其实我们这里边哎这个方案的名字叫get a borrower这个就是借款人的意思参数呢就是一个ID是不是根据这个什么呀这个标识嘛就是ID来查询这个借款人的信息
[01:37] 那么返回的数据呢我们封装成barwa dto对象就ok了这是接口里边定义的方法然后呢我们在测试类当中呢实现这个方法就行好在这个地方那怎么查呢这个很简单呢我们有id了那直接就去表里边做一次查询就行了对吧怎么查呢我们的MP对业务层是不是有封装嘛我们看一下他会有什么方法呢我们用哪个呢get one
[02:15] 不用啊没那么麻烦我们直接用什么呀get by id就行了你看见名之义嘛你给我一个主件id的值哎我就给你查出来什么呀用户信息呢这个consumer对象直接就返回了嘛对不对但是考虑到这个功能有可能将来在其他地方也会经常用我们准备把这块代码给封装到一个方法里面那咱看看讲一把这块代码就不再写了用非常简单的来看这然后我单独封装了一个方法叫get方法啊然后传过来的就是这个id
[02:45] 然后呢你看我们就是调用什么方法刚才我们说了对给他白地方直接能查出来一个consumer对象而且我们这还做了一个什么呀飞空漫断啊如果这个没查出来的话我们就抛一个异常啊就用户不存在呗对不对那如果查出来的话你看我还在这在这做了一个什么事情啊对直接把这个consumer对象就给他转换成什么呀dq对象啊就我们刚才说了吗考虑到这块带吗可能将来在别的地方也会经常用所以说我们简单做一个封装吧那我就真到这个旁边了
[03:17] 那有了这个方法之后呢我在这儿其实就简单了我就直接调用一下哪个方法对get方法就行了那我就直接得到了一个什么呀对得到了一个DTO对象是不是因为我们这儿已经做什么呀做转换了所以这儿呢我就用一个consumer DTO来接收一下就OK了这就完了吗查询是完了但是你看看咱这儿要的是什么呀browser DTO啊
[03:49] 是不是但咱得到的目前是什么呀consumer DTO大家明白接下来又要干嘛了吧对要做这个转换了只不过这一次是两个DTO之间的转换那把consumer DTO转换成barber DTO一样的套路都一样先来一个什么呀新的一个对象然后就开始做这个什么转换就行了那咋转呢那无非就是把consumer DTO对象里边的属性值是不是付到这个什么呀barber
[04:20] DTO里边就想咋复啊还是用这个Being Utils的Corp Propriet方法然后呢把这个谁啊对Consumer DTO里边属性的值给谁啊给Balmer DTO这基本上就完成了什么呀转换啊非常简单但是呢还没完啊接下来呢还有一个细节需要处理什么细节呢来大家看看这个Balmer DTO它里边的属性啊
[04:47] 嗯他里边的话有这几个东西大家需要注意第一个就是年龄还有什么呀生日还有什么呀性别这些信息我们也需要提供那啥意思呢那难道我们这个这查询的时候没有查出来刚才那些信息吗那有没有的话我们去这个consumer表里边瞅一瞅就行了啊你看看我们的consumer当时设计的时候对不对有没有这些字段啊就是我们刚才说的都什么呀对年龄
[05:18] 这个什么呀生日性别你看有吗没有吧有年龄吗没有吧有生日吗没有吧然后看有有什么呀有性别吗都没有啊哎但是你看啊我们的这个barber detail里边他可是要这些东西的哎让大家再抽一要不要东西那但是我们查就查不出来这些东西表里边就没有啊怎么办哎这里边大家别忘了我们以前提过十分正号里边是不是就包含这些信息啊
[05:50] 是不是即使不包含你像年龄啥的我们能不能就是给它计算出来可不可以可以了对不对所以说我们接下来要做一个处理就是根据身份证号身份证号我们是查出来然后怎么通过身份证号得到年龄得到生日得到性别我们要做这么一个处理那这个怎么实现我们这给他提供了一个怎么说也是一个工具类叫叫IDcard YouTube就是它
[06:20] 专门处理身份证号的一个工具类我们可以看一看这里边你看就可以通过身份证号获取什么呀他的生日性别年龄对不对现成的方法我们直接拿着用就行了就通过这个get info你传进来一个什么呀身份证号他会把这个什么呀这个生日啊性别年龄呢分别获取出来然后放到一个map集合里边返回那我们将来呢
[06:50] 得到这个麦克集合然后从麦克集合里边去我们想要的值就想这一代吧你下去可以自己看一下这是什么咱们都能看他从里边截取一些对应位置上的那个值做一些判断就得到这个什么呀这些信息啊呃那我们这呢就是直接使用一下就行了那我们就调他刚才说的什么给他info然后呢把什么呀把我们手头上得到的这个什么身份证号扔给他然后我们说了他返回来是一个什么呀
[07:20] 对map集合那么范型呢都是stream我们就起个名字叫card info吧就这样那么现在这个map集合里边它就有什么呀它就有我们想要的什么呀年龄啊生日啊还有性别这些东西那我们接下来呢就是从map集合来取这些数据就行从map集合里边怎么取这些数据那就是get方法呗
[07:53] 对不对是不是根据键得到值吗那我怎么知道他这些键是什么样的那你可以看看这个这个工具类码这个圆码吗我们刚才说了因为这些代码大家都是能看懂的你往这里边瞅瞅你看看到没有这是他处理完之后把这些信息往这个麦布集团里边存的这比如键的名字吗看到了吧对不对查一查圆码就行了那这块代码的话我就不在这个一行一行给大家编写了就是这一块
[08:24] 这比较简单你看是不是我们就对上get方法根据键得到我们的值啊该做类型转换做类型转换取出来之后呢就开始往DTO对象里边存就行了啊那这send数据咱是不是就有有了之后这就处理完了我们直接就返回什么呀对我们直接就返回这个DTO对象就OK了那咱这一次这个查询就全部搞定了就是根据ID做一次查询只不过这里边呢要做一些转换而已
[08:57] 这是右层的代码咱就写完啊右层代码写完之后呢咱接下来是不是也是顺手把Controller的这个代码给他这个补充一下就行了Controller咱找一找当时是应该是这个吧是不是你看根据ID获取借款人用户的信息嘛啊这个Controller代码也比较简单是不是调上右层就行了啊consumer Service.我们刚才那个方法叫get borrow对吧
[09:29] 给他包啊然后把这个ID给他扔进去呗然后我们这个方刚才看到反而他是不是就是一个包肉DTO对象对不对然后把这个对象的封装成rest response就可以返回给前端还是通过succes方法进行封装把这个放进去这就封装完了然后呢直接返回给前端然后这个功能咱就搞定了一会呢咱就进行功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

