package com.social.ecom.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.social.ecom.pojo.Sku;
import com.social.ecom.mapper.SkuMapper;
import com.social.ecom.pojo.Stock;
import com.social.ecom.service.*;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@Service
public class SkuServiceImpl extends ServiceImpl<SkuMapper, Sku> implements SkuService {


    @Autowired
    private SkuAttributeInfoService skuAttributeInfoService;

    @Autowired
    private AttributeNameService attributeNameService;

    @Autowired
    private AttributeValueService attributeValueService;

    @Autowired
    private StockService stockService;

    @Override
    public List<Sku> listByShopId(QueryWrapper<Sku> queryWrapper, Long shopId) {
        List<Sku> objectList = super.list(queryWrapper);
        objectList.forEach(obj-> {
            QueryWrapper attributeQueryWrapper = new QueryWrapper();
            attributeQueryWrapper.eq("sku_id",obj.getId());

            obj.setSkuAttributeInfoList(skuAttributeInfoService.list(attributeQueryWrapper));
            obj.getSkuAttributeInfoList().forEach(attributeInfo->{
                attributeInfo.setAttributeName(attributeNameService.getById(attributeInfo.getAttributeNameId()).getName());
                attributeInfo.setAttributeValue(attributeValueService.getById(attributeInfo.getAttributeValueId()).getValue());
            });

            QueryWrapper<Stock> queryWrapperStock = new QueryWrapper<>();
            queryWrapperStock.eq("sku_id",obj.getId());
            queryWrapperStock.eq("shop_id",shopId);
            List<Stock> stockList = stockService.list(queryWrapperStock);
            if(stockList.size() > 0){
                obj.setStockCount(stockList.get(0).getStockCount());
            }else{
                obj.setStockCount(0);
            }

        });
        return objectList;
    }
}
