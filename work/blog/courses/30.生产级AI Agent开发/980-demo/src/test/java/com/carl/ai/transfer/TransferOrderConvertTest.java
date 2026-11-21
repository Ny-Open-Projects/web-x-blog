package com.carl.ai.transfer;

import com.carl.ai.transfer.convert.TransferOrderConvert;
import com.carl.ai.transfer.domain.model.BbTransferOrder;
import com.carl.ai.transfer.domain.model.BbTransferOrderItem;
import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * MapStruct 转换层单测（复刻 5-16 的 LocalDate 坑）。
 * 验证：param 用 String 接日期 → model 的 LocalDate 正确；null 日期安全转 null。
 */
class TransferOrderConvertTest {

    private final TransferOrderConvert convert = TransferOrderConvert.INSTANCE;

    @Test
    void paramToModel_mapsStringDateToLocalDate() {
        TransferOrderParam param = new TransferOrderParam();
        param.setSourceWarehouseId(1);
        param.setTargetWarehouseId(2);
        param.setTransferType(1);
        param.setTransferDate("2026-10-20");           // String → LocalDate
        param.setCreatedBy("agent");

        BbTransferOrder model = convert.paramToModel(param);

        assertEquals(1, model.getSourceWarehouseId());
        assertEquals(2, model.getTargetWarehouseId());
        assertEquals(LocalDate.of(2026, 10, 20), model.getTransferDate()); // 正确转换
    }

    @Test
    void nullDateConvertsToNullSafely() {
        TransferOrderParam param = new TransferOrderParam();
        param.setTransferDate(null);
        BbTransferOrder model = convert.paramToModel(param);
        assertNull(model.getTransferDate());
    }

    @Test
    void itemParamsToModel_mapsList() {
        TransferOrderItemParam item = new TransferOrderItemParam();
        item.setSku("SKU-A");
        item.setQty(10);
        List<BbTransferOrderItem> models = convert.itemParamsToModel(List.of(item));
        assertEquals(1, models.size());
        assertEquals("SKU-A", models.get(0).getSku());
        assertEquals(10, models.get(0).getQty());
    }
}
