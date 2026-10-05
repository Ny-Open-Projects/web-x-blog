package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.Test;
import com.imooc.socialecom.pojo.User;
import com.imooc.socialecom.service.TestService;
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
@RequestMapping("/test")
public class TestController {

    @Autowired
    private TestService testService;

    @RequestMapping(value="/get",method = {RequestMethod.GET})
    @ResponseBody
    public JsonReturnType get(@RequestParam(name="id")Long id){
        Test test = testService.getById(id);
        if(test != null){
            return JsonReturnType.createType(test);
        }else{
            return JsonReturnType.createErrorType("test不存在");
        }
    }
}
