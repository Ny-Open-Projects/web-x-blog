package com.imooc.socialecom.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.imooc.socialecom.base.JsonReturnType;
import com.imooc.socialecom.mapper.UserMapper;
import com.imooc.socialecom.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller("/user")
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserMapper userMapper;


    @RequestMapping(value="/get",method = {RequestMethod.GET})
    @ResponseBody
    public JsonReturnType get(@RequestParam(name="id")Long id){
        User user = userMapper.selectById(id);
        if(user != null){
            return JsonReturnType.createType(user);
        }else{
            return JsonReturnType.createErrorType("用户不存在");
        }
    }
    @RequestMapping(value="/create",method = {RequestMethod.GET,RequestMethod.POST})
    @ResponseBody
    public JsonReturnType create(@RequestParam(name="userName",defaultValue = "")String userName,
                                 @RequestParam(name="userPassword",defaultValue = "")String userPassword,
                                 @RequestParam(name="userTel",defaultValue = "")String userTel){

        User user = new User();
        user.setUserName(userName);
        user.setUserTel(userTel);
        user.setUserPassword(userPassword);

        userMapper.insert(user);

        return JsonReturnType.createType(user);
    }


    @RequestMapping(value="/update",method = {RequestMethod.GET,RequestMethod.POST})
    @ResponseBody
    public JsonReturnType update(@RequestParam(name="id",defaultValue = "0")Long id,
                                @RequestParam(name="userName",defaultValue = "")String userName,
                                 @RequestParam(name="userPassword",defaultValue = "")String userPassword,
                                 @RequestParam(name="userTel",defaultValue = "")String userTel){

        User user = userMapper.selectById(id);
        user.setUserName(userName);
        user.setUserTel(userTel);
        user.setUserPassword(userPassword);

        int rowAffected = userMapper.updateById(user);
        if(rowAffected < 1){
            return JsonReturnType.createErrorType("更新失败");
        }
        return JsonReturnType.createType(user);
    }

    @RequestMapping(value="/getforupdate",method = {RequestMethod.GET,RequestMethod.POST})
    @ResponseBody
    public JsonReturnType getforupdate(@RequestParam(name="id",defaultValue = "0")Long id){
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        wrapper.eq("id",id);
        wrapper.last("for update");
        User user = userMapper.selectOne(wrapper);
        return JsonReturnType.createType(user);
    }

    @RequestMapping(value="/updatebyversion",method = {RequestMethod.GET,RequestMethod.POST})
    @ResponseBody
    public JsonReturnType updatebyversion(@RequestParam(name="id",defaultValue = "0")Long id,
                                 @RequestParam(name="userName",defaultValue = "")String userName,
                                 @RequestParam(name="userPassword",defaultValue = "")String userPassword,
                                 @RequestParam(name="userTel",defaultValue = "")String userTel){

        User user = userMapper.selectById(id);
        user.setUserName(userName);
        user.setUserTel(userTel);
        user.setUserPassword(userPassword);

        int rowAffected = userMapper.updateById(user);
        if(rowAffected < 1){
            return JsonReturnType.createErrorType("更新失败");
        }

        return JsonReturnType.createType(user);
    }


    @RequestMapping(value="batchget",method = {RequestMethod.GET})
    @ResponseBody
    public JsonReturnType batchget(@RequestParam(name="ids",defaultValue = "")List<Integer> ids){
        List<User> userList = userMapper.selectBatchIds(ids);
        return JsonReturnType.createType(userList);
    }


    @RequestMapping(value="getbycondition",method = {RequestMethod.GET})
    @ResponseBody
    public JsonReturnType getbycondition(@RequestParam(name="id",required = false)Long id,
                                         @RequestParam(name="userName",defaultValue = "")String userName,
                                         @RequestParam(name="userTel",defaultValue = "")String userTel,
                                         @RequestParam(name="page",defaultValue = "1")Integer currentPage,
                                         @RequestParam(name="size",defaultValue = "20")Integer size ){
        Page<User> page = new Page<>(currentPage,size);

        QueryWrapper queryWrapper = new QueryWrapper();
        if(id != null){
            queryWrapper.eq("id",id);
        }
        if(!StringUtils.isEmpty(userName)){
            queryWrapper.like("user_name",userName);
        }

        if(!StringUtils.isEmpty(userTel)){
            queryWrapper.like("user_tel",userTel);
        }

        List<User> userList = userMapper.selectPage(page,queryWrapper).getRecords();
        //IPage<User> userPageList = userMapper.selectPage(page,queryWrapper);

        return JsonReturnType.createType(userList);
    }





}
