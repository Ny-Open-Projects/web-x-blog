# 画面线理解：day06-6-开户第一阶段-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-6-开户第一阶段-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:52, 02:30, 02:59, 03:42, 04:03, 05:09, 05:33, 06:02, 06:25, 08:04, 08:53, 09:31, 10:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:16:06

1) 这一组画面整体在讲什么（一句话）：
演示如何在 waningzp-consumer-service 项目中，基于 MyBatis-Plus 和 Spring Boot，实现 BankCardService 接口的两个方法：根据用户 ID 查询银行卡信息和根据卡号查询银行卡信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 BankCardMapper.xml 文件，准备编写 MyBatis 映射文件。
画面2：展示 PPT 内容，其中包含“BankCardDTO getByCardNumber(String cardNumber)”方法的说明，以及多个服务模块的截图，如 adminService、configService 等。
画面3：展示 BankCardService 接口定义，包含两个方法：getByConsumerId(Long consumerId) 和 getByCardNumber(String cardNumber)。
画面4：展示 BankCardServiceImpl.java 文件，准备编写服务实现类。
画面5：在 BankCardServiceImpl.java 中，导入 Spring Boot 和 MyBatis-Plus 的相关包，并声明类继承 ServiceImpl。
画面6：在 BankCardServiceImpl.java 中，声明类继承 ServiceImpl，并实现 BankCardService 接口。
画面7：在 BankCardServiceImpl.java 中，编写 getByConsumerId 方法，使用 QueryWrapper 构造查询条件。
画面8：在 BankCardServiceImpl.java 中，编写 getByCardNumber 方法，准备使用 QueryWrapper。
画面9：在 BankCardServiceImpl.java 中，为 getByCardNumber 方法的 QueryWrapper 设置查询条件，使用 lambda 表达式。
画面10：在 BankCardServiceImpl.java 中，为 getByCardNumber 方法的 QueryWrapper 设置查询条件，使用 lambda 表达式。
画面11：在 BankCardServiceImpl.java 中，为 getByCardNumber 方法的 QueryWrapper 设置查询条件，使用 lambda 表达式。
画面12：在 BankCardServiceImpl.java 中，编写 convertBankCardEntityToDTO 方法，用于将实体对象转换为 DTO 对象。
画面13：在 BankCardServiceImpl.java 中，调用 convertBankCardEntityToDTO 方法，将查询结果转换为 DTO。
画面14：在 BankCardServiceImpl.java 中，完成 getByCardNumber 方法的编写，返回转换后的 DTO 对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<Xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0/EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.waningzp.consumer.mapper.BankCardMapper">
</mapper>

画面3：
import com.banndow.mybatplus.extension.service.IService;
/**
 * 用户绑定银行卡信息 服务类
 */
public interface BankCardService extends IService<BankCard> {
    /**
     * 获取银行卡信息
     * @param consumerId 用户ID
     * @return
     */
    BankCardDTO getByConsumerId(Long consumerId);

    /**
     * 获取银行卡信息
     * @param cardNumber 卡号
     * @return
     */
    BankCardDTO getByCardNumber(String cardNumber);
}

画面5：
import org.springframework.stereotype.Service;
@Service
public class BankCardServiceImpl extends ServiceImpl<BankCardMapper, BankCard> implements BankCardService {

画面6：
import cn.itcast.waningzp.consumer.entity.BankCard;
import cn.itcast.waningzp.consumer.mapper.BankCardMapper;
import com.banndow.mybatplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;
@Service
public class BankCardServiceImpl extends ServiceImpl<BankCardMapper, BankCard> implements BankCardService {

画面7：
import cn.itcast.waningzp.api.consumer.model.BankCardDTO;
import cn.itcast.waningzp.consumer.entity.BankCard;
import cn.itcast.waningzp.consumer.mapper.BankCardMapper;
import com.banndow.mybatplus.core.conditions.query.QueryWrapper;
import com.banndow.mybatplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;
@Service
public class BankCardServiceImpl extends ServiceImpl<BankCardMapper, BankCard> implements BankCardService {
    @Override
    public BankCardDTO getByConsumerId(Long consumerId) {
        BankCard bankCard = getOne(new QueryWrapper<BankCard>().lambda().eq(BankCard::getConsumerId, consumerId));
        return convertBankCardEntityToDTO(bankCard);
    }

画面12：
private BankCardDTO convertBankCardEntityToDTO(BankCard bankCard) {
    if (bankCard == null) {
        return null;
    }
    BankCardDTO bankCardDTO = new BankCardDTO();
    BeanUtils.copyProperties(bankCard, bankCardDTO);
    return bankCardDTO;
}

画面14：
@Override
public BankCardDTO getByCardNumber(String cardNumber) {
    BankCard bankCard = getOne(new QueryWrapper<BankCard>().lambda().eq(BankCard::getCardNumber, cardNumber));
    return convertBankCardEntityToDTO(bankCard);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
PPT 标题：4. 新建 BankCardServiceImpl 类实现上述两个方法：
内容：
- BankCardDTO getByCardNumber(String cardNumber);
- 服务模块截图：
  - adminService
  - ApolloPortal
  - configService
  - waningzp-discover-server
  - waningzp-gateway-server
  - waningzp-usa-service

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
