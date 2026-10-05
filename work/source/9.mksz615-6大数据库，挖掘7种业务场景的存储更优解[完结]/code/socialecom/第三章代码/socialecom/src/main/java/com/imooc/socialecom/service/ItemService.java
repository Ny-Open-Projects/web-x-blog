package com.imooc.socialecom.service;

import com.imooc.socialecom.pojo.Item;
import com.baomidou.mybatisplus.extension.service.IService;
import com.imooc.socialecom.pojo.Sku;

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
