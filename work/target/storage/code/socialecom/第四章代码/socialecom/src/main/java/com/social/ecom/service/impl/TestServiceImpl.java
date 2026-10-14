package com.social.ecom.service.impl;

import com.social.ecom.pojo.Test;
import com.social.ecom.mapper.TestMapper;
import com.social.ecom.service.TestService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author socialecom
 * @since 2022-10-02
 */
@Service
public class TestServiceImpl extends ServiceImpl<TestMapper, Test> implements TestService {

}
