package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.AttributeName;
import com.imooc.socialecom.pojo.AttributeValue;
import com.imooc.socialecom.service.AttributeNameService;
import com.imooc.socialecom.service.AttributeValueService;
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
@RequestMapping("/attribute-value")
public class AttributeValueController {
    @Autowired
    private AttributeValueService attributeValueService;

    @RequestMapping(value="create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody AttributeValue attributeValue){
        attributeValueService.save(attributeValue);
        return JsonReturnType.createType(attributeValue);
    }
}
