package com.imooc.socialecom.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.imooc.socialecom.pojo.Item;
import com.imooc.socialecom.mapper.ItemMapper;
import com.imooc.socialecom.pojo.Sku;
import com.imooc.socialecom.service.*;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@Service
public class ItemServiceImpl extends ServiceImpl<ItemMapper, Item> implements ItemService {


    @Autowired
    private SkuService skuService;

    @Autowired
    private SkuAttributeInfoService skuAttributeInfoService;

    @Autowired
    private BrandService brandService;
    @Autowired
    private CategoryService categoryService;

    @Autowired
    private SellerService sellerService;


    @Override
    @Transactional
    public Sku createSku(Sku sku) {
        skuService.save(sku);
        sku.getSkuAttributeInfoList().forEach(skuAttributeInfo -> {
            skuAttributeInfo.setSkuId(sku.getId());
            skuAttributeInfoService.save(skuAttributeInfo);
        });

        return sku;
    }

    @Override
    public Item getItem(Long id, Long shopId) {
        Item item = getById(id);
        if(item == null){
            return null;
        }
        item.setSellerName(sellerService.getById(item.getSellerId()).getSellerName());
        item.setBrand(brandService.getById(item.getBrandId()).getName());
        item.setCategory(categoryService.getById(item.getCategoryId()).getName());

        QueryWrapper<Sku> skuQueryWrapper = new QueryWrapper<>();
        skuQueryWrapper.eq("item_id",item.getId());
        List<Sku> skuList = skuService.listByShopId(skuQueryWrapper,shopId);
        item.setSkuList(skuList);
        return item;
    }

    @Override
    public List<Item> search(String name, Long shopId) {
        QueryWrapper queryWrapper = new QueryWrapper();
        queryWrapper.like("name",name);
        queryWrapper.select("id");
        List<Long> itemIdList = super.listObjs(queryWrapper);
        List<Item> itemList = itemIdList.stream().map(obj->{
            return getItem(obj,shopId);
        }).collect(Collectors.toList());
        return itemList;
    }
}
