package com.imooc.socialecom.mapper;

import com.imooc.socialecom.pojo.Stock;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Param;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
public interface StockMapper extends BaseMapper<Stock> {
    int decreaseStock(@Param("skuId")Long skuId,@Param("shopId")Long shopId,@Param("stockCount")Integer stockCount);

    int tradeRollbackStock(@Param("skuId")Long skuId,@Param("shopId")Long shopId,@Param("stockCount")Integer stockCount);


}
