package com.imooc.socialecom.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.imooc.socialecom.pojo.Sku;
import com.imooc.socialecom.pojo.Trade;
import com.imooc.socialecom.mapper.TradeMapper;
import com.imooc.socialecom.service.SkuService;
import com.imooc.socialecom.service.StockService;
import com.imooc.socialecom.service.TradeService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.UUID;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-03
 */
@Service
public class TradeServiceImpl extends ServiceImpl<TradeMapper, Trade> implements TradeService {

    @Autowired
    private SkuService skuService;
    @Autowired
    private StockService stockService;

    @Override
    //@GlobalTransactional(rollbackFor = Exception.class)
    @Transactional(rollbackFor = Exception.class)
    public Trade createTrade(Trade trade) {
        Sku sku = skuService.getById(trade.getSkuId());
        if(sku == null){
            return null;
        }
        if(sku.getPrice().compareTo(trade.getSinglePrice()) != 0){
            return null;
        }
        boolean stockDecreaseSuccess = stockService.decreaseStock(trade.getSkuId(),trade.getShopId(),trade.getStockCount());
        if(!stockDecreaseSuccess){
            throw new RuntimeException("扣减库存失败");
        }
        trade.setStatus(1);
        save(trade);

        //去第三方支付公司预下单
        String wechatTradeId = UUID.randomUUID().toString();
        trade.setWechatTradeId(wechatTradeId);
        updateById(trade);

        return trade;
    }

    @Override
    @Transactional
    public Trade pay(Trade trade) {
        QueryWrapper<Trade> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("wechat_trade_id",trade.getWechatTradeId());
        queryWrapper.last("for update");
        trade = getBaseMapper().selectOne(queryWrapper);
        if(trade == null){
            return null;
        }
        if(trade.getStatus().intValue() == 2){
            return trade;
        }
        if(trade.getStatus().intValue() == 3){
            return exceptionPay(trade,2);
        }
        trade.setStatus(2);
        updateById(trade);
        return trade;
    }

    private Trade exceptionPay(Trade trade,int type){
        if(type == 1){
            //优先取消
            if(refund(trade.getWechatTradeId())){
                return trade;
            }else{
                return null;
            }
        }else{
            //优先支付
            boolean decreaseSuccess = stockService.decreaseStock(trade.getSkuId(),trade.getShopId(),trade.getStockCount());
            if(!decreaseSuccess){
                if(refund(trade.getWechatTradeId())){
                    return trade;
                }else{
                    return null;
                }
            }else{
                trade.setStatus(2);
                updateById(trade);
                return trade;
            }
        }



    }

    private boolean refund(String wechatTradeId){
        //调用微信支付退款
        return true;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Trade cancel(Trade trade) {
        QueryWrapper<Trade> wrapper = new QueryWrapper<>();
        wrapper.eq("id",trade.getId());
        wrapper.last("for update");
        trade = getBaseMapper().selectOne(wrapper);
        if(trade == null){
            return null;
        }
        if(trade.getStatus().intValue() == 3){
            return trade;
        }
        if(trade.getStatus().intValue() == 2){
            return null;
        }
        boolean isSuccess = stockService.tradeRollbackStock(trade.getSkuId(),trade.getShopId(),trade.getStockCount());
        if(!isSuccess){
            throw new RuntimeException("库存回补失败");
        }
        trade.setStatus(3);
        updateById(trade);
        return trade;
    }
}
