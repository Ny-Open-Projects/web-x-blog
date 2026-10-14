package com.social.ecom.controller;


import com.social.ecom.base.JsonReturnType;
import com.social.ecom.pojo.Shop;
import com.social.ecom.service.ShopService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@RestController
@RequestMapping("/shop")
public class ShopController {

    @Autowired
    private ShopService shopService;

    @RequestMapping(value="/create",method = {RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Shop shop){
        shopService.save(shop);
        return JsonReturnType.createType(shop);
    }






}
