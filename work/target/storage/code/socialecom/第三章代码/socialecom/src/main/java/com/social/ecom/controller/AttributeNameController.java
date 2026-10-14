package com.social.ecom.controller;


import com.social.ecom.base.JsonReturnType;
import com.social.ecom.pojo.AttributeName;
import com.social.ecom.pojo.Brand;
import com.social.ecom.service.AttributeNameService;
import com.social.ecom.service.BrandService;
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
@RequestMapping("/attribute-name")
public class AttributeNameController {

    @Autowired
    private AttributeNameService attributeNameService;

    @RequestMapping(value="create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody AttributeName attributeName){
        attributeNameService.save(attributeName);
        return JsonReturnType.createType(attributeName);
    }

}
