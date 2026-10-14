package com.social.ecom.controller;


import com.social.ecom.base.JsonReturnType;
import com.social.ecom.pojo.Brand;
import com.social.ecom.pojo.Seller;
import com.social.ecom.service.BrandService;
import com.social.ecom.service.SellerService;
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
@RequestMapping("/brand")
public class BrandController {

    @Autowired
    private BrandService brandService;

    @RequestMapping(value="create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Brand brand){
        brandService.save(brand);
        return JsonReturnType.createType(brand);
    }


}
