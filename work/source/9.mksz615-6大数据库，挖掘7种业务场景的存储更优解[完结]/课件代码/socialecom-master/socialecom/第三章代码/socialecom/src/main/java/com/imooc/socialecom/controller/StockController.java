package com.imooc.socialecom.controller;


import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.Stock;
import com.imooc.socialecom.pojo.User;
import com.imooc.socialecom.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DuplicateKeyException;
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
@RequestMapping("/stock")
public class StockController {
    @Autowired
    private StockService stockService;

    @RequestMapping(value="/create",method = {RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Stock stock){
        stockService.increaseStock(stock.getSkuId(),stock.getShopId(),stock.getStockCount());
        return JsonReturnType.createType(stock);
    }

}
