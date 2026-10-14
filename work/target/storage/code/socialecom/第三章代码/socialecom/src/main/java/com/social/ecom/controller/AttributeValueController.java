package com.social.ecom.controller;


import com.social.ecom.base.JsonReturnType;
import com.social.ecom.pojo.AttributeName;
import com.social.ecom.pojo.AttributeValue;
import com.social.ecom.service.AttributeNameService;
import com.social.ecom.service.AttributeValueService;
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
