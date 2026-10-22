package com.imooc.socialecom.helper;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.imooc.socialecom.pojo.Trade;
import com.imooc.socialecom.service.TradeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

import java.time.LocalDateTime;
import java.util.List;

@Configuration
@EnableScheduling
public class SchedulerTask {

    @Autowired
    private TradeService tradeService;

    //@Scheduled(cron="0/5 * * * * ?")
    private void configureTask(){
        //待支付订单且创建时间大于15分钟
        QueryWrapper<Trade> tradeQueryWrapper = new QueryWrapper<>();
        tradeQueryWrapper.eq("status",1);
        tradeQueryWrapper.lt("create_time",LocalDateTime.now().minusMinutes(15));
        List<Trade> tradeList = tradeService.list(tradeQueryWrapper);
        tradeList.forEach(trade -> {
            try{
                tradeService.cancel(trade);
            }catch(Exception e){

            }
        });
    }
}
