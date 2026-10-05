package com.imooc.socialecom.service;

import com.imooc.socialecom.pojo.Stock;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
public interface StockService extends IService<Stock> {

    Stock increaseStock(Long skuId,Long shopId,Integer stockCount);
}
