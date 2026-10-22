package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.Trade;
import com.imooc.socialecom.service.TradeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author socialecom
 * @since 2022-10-03
 */
@RestController
@RequestMapping("/trade")
public class TradeController {
    @Autowired
    private TradeService tradeService;

    @RequestMapping(value="/create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Trade trade){
        try{
            trade = tradeService.createTrade(trade);
        }catch(Exception ex){
            return JsonReturnType.createErrorType("下单失败");
        }
        if(trade == null){
            return JsonReturnType.createErrorType("下单失败");
        }
        return JsonReturnType.createType(trade);
    }
    @RequestMapping(value="pay",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType pay(@RequestBody Trade trade){
        trade = tradeService.pay(trade);
        if(trade == null){
            return JsonReturnType.createErrorType("支付失败");
        }
        return JsonReturnType.createType("success");
    }

    @RequestMapping(value="cancel",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType cancel(@RequestBody Trade trade){
        try{
            trade = tradeService.cancel(trade);
        }catch(Exception ex){
            return JsonReturnType.createErrorType("取消失败");
        }
        if(trade == null){
            return JsonReturnType.createErrorType("取消失败");
        }
        return JsonReturnType.createType(trade);

    }



}
