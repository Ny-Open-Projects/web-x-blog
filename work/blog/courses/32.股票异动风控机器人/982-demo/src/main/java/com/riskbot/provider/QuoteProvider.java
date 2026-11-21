package com.riskbot.provider;

import com.riskbot.domain.StockTick;

import java.util.List;

/**
 * 行情接入抽象（感知层）。mock 源与真实源实现同一接口，
 * 由 Spring profile 决定注入哪一个 —— 这是「可切真实 API」的关键解耦点。
 */
public interface QuoteProvider {
    List<StockTick> nextTicks();

    String market();
}
