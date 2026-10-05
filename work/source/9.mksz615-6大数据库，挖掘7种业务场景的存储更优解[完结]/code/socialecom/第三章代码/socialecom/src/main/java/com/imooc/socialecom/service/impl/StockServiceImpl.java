package com.imooc.socialecom.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.imooc.socialecom.pojo.Stock;
import com.imooc.socialecom.mapper.StockMapper;
import com.imooc.socialecom.pojo.User;
import com.imooc.socialecom.service.StockService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@Service
public class StockServiceImpl extends ServiceImpl<StockMapper, Stock> implements StockService {

    @Override
    @Transactional
    public Stock increaseStock(Long skuId, Long shopId, Integer stockCount) {
        QueryWrapper<Stock> wrapper = new QueryWrapper<>();
        wrapper.eq("sku_id",skuId);
        wrapper.eq("shop_id",shopId);
        Stock stock = getBaseMapper().selectOne(wrapper);
        if(stock == null){
            try{
                stock = new Stock();
                stock.setSkuId(skuId);
                stock.setShopId(shopId);
                stock.setStockCount(stockCount);
                save(stock);
            }catch(DuplicateKeyException ex){
                updateStock(skuId,shopId,stockCount);
            }
        }else{
            updateStock(skuId,shopId,stockCount);
        }
        return stock;
    }

    private void updateStock(Long skuId, Long shopId, Integer stockCount){
        QueryWrapper<Stock> wrapper = new QueryWrapper<>();
        wrapper.eq("sku_id",skuId);
        wrapper.eq("shop_id",shopId);
        wrapper.last("for update");
        Stock stock = getBaseMapper().selectOne(wrapper);
        stock.setStockCount(stock.getStockCount().intValue() + stockCount);
        updateById(stock);
    }
}
