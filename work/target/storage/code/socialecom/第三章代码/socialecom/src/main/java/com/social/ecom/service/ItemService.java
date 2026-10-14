package com.social.ecom.service;

import com.social.ecom.pojo.Item;
import com.baomidou.mybatisplus.extension.service.IService;
import com.social.ecom.pojo.Sku;

import java.util.List;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
public interface ItemService extends IService<Item> {

    Sku createSku(Sku sku);

    Item getItem(Long id, Long shopId);

    List<Item> search(String name,Long shopId);

}
