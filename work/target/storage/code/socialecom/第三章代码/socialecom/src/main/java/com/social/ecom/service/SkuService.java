package com.social.ecom.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.social.ecom.pojo.Sku;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
public interface SkuService extends IService<Sku> {
    List<Sku> listByShopId(QueryWrapper<Sku> queryWrapper,Long shopId);

}
