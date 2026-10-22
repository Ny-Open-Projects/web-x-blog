package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.AttributeName;
import com.imooc.socialecom.pojo.Brand;
import com.imooc.socialecom.service.AttributeNameService;
import com.imooc.socialecom.service.BrandService;
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
