package com.carl.ai.transfer.convert;

import com.carl.ai.transfer.domain.model.BbTransferOrder;
import com.carl.ai.transfer.domain.model.BbTransferOrderItem;
import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.factory.Mappers;

import java.util.List;

/**
 * POJO 转换层（复刻 5-15 MapStruct）。
 * <p>
 * 课程核心坑（5-16）：param 与 model 的日期一个用 {@code String}、一个用 {@code LocalDate}，
 * MapStruct 会自动用 {@code LocalDate.parse(String)} 完成转换；反之若两边都用 LocalDate 则报错。
 * 这里 param.transferDate 是 String，model.transferDate 是 LocalDate —— 转换安全。
 * <p>
 * 同时提供 INSTANCE 静态实例（与课程的 {@code TransferOrderConvert.INSTANCE} 用法一致），
 * 也支持 Spring 注入（{@code componentModel = "spring"}）。
 */
@Mapper(componentModel = "spring", imports = java.time.LocalDate.class)
public interface TransferOrderConvert {

    TransferOrderConvert INSTANCE = Mappers.getMapper(TransferOrderConvert.class);

    /** param 主单 → model 主单（transferDate: String → LocalDate 由 MapStruct 自动完成）。 */
    @Mapping(target = "id", ignore = true)
    BbTransferOrder paramToModel(TransferOrderParam param);

    /** param 子项集合 → model 子项集合。 */
    List<BbTransferOrderItem> itemParamsToModel(List<TransferOrderItemParam> params);
}
