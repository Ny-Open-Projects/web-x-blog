package com.imooc.socialecom.controller;


import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.pojo.Brand;
import com.imooc.socialecom.pojo.Category;
import com.imooc.socialecom.service.BrandService;
import com.imooc.socialecom.service.CategoryService;
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
@RequestMapping("/category")
public class CategoryController {

    @Autowired
    private CategoryService categoryService;

    @RequestMapping(value="create",method={RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestBody Category category){
        categoryService.save(category);
        return JsonReturnType.createType(category);
    }


}
