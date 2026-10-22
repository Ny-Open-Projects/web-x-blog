package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.Item;
import com.imooc.socialecom.pojo.Sku;
import com.imooc.socialecom.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@RestController
@RequestMapping("/item")
public class ItemController {

    @Autowired
    private ItemService itemService;



    @RequestMapping(value="/create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Item item){
        itemService.save(item);
        return JsonReturnType.createType(item);
    }

    @RequestMapping(value="/createsku",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType createsku(@RequestBody Sku sku){
        itemService.createSku(sku);
        return JsonReturnType.createType(sku);
    }

    @RequestMapping(value="/get",method={RequestMethod.GET})
    @ResponseBody
    public JsonReturnType get(@RequestParam(name="id")Long id,
                              @RequestParam(name="shopId")Long shopId ){
        Item item = itemService.getItem(id,shopId);
        return JsonReturnType.createType(item);
    }

    @RequestMapping(value="/search",method={RequestMethod.GET})
    @ResponseBody
    public JsonReturnType search(@RequestParam(name="name")String name,
                              @RequestParam(name="shopId")Long shopId ){
        List<Item> itemList = itemService.search(name,shopId);
        return JsonReturnType.createType(itemList);
    }
}
