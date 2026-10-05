package handler

import (
	"context"
    "encoding/json"
	"errors"
	"git.imooc.com/coding-535/appStoreApi/proto/form"
	"git.imooc.com/coding-535/common"
	log "github.com/asim/go-micro/v3/logger"
    appStore "git.imooc.com/coding-535/appStore/proto/appStore"
	appStoreApi "git.imooc.com/coding-535/appStoreApi/proto/appStoreApi"
	"strconv"
)

type AppStoreApi struct{
    AppStoreService appStore.AppStoreService
}

//获取 url 中的应用ID
func (e *AppStoreApi) GetId(req *appStoreApi.Request) (int64, error) {
	if _,ok := req.Get["app_id"]; !ok{
		return 0,errors.New("参数异常")
	}
	//获取到ID后进行转化
	IdString := req.Get["app_id"].Values[0]
	Id ,err := strconv.ParseInt(IdString,10,64)
	if err != nil {
		common.Error(err)
		return 0,err
	}
	return Id,nil
}

// appStoreApi.FindAppStoreById 通过API向外暴露为/appStoreApi/findAppStoreById，接收http请求
// 即：/appStoreApi/FindAppStoreById 请求会调用go.micro.api.appStoreApi 服务的appStoreApi.FindAppStoreById 方法
func (e *AppStoreApi) FindAppStoreById(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response) error {
	log.Info("Received appStoreApi.FindAppStoreById request")
	Id,err := e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	//获取应用市场中应用的相关信息
	info,err := e.AppStoreService.FindAppStoreByID(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(info)
	rsp.Body = string(b)
	return nil
}

// appStoreApi.AddAppStore 通过API向外暴露为/appStoreApi/AddAppStore，接收http请求
// 即：/appStoreApi/AddAppStore 请求会调用go.micro.api.appStoreApi 服务的appStoreApi.AddAppStore 方法
func (e *AppStoreApi) AddAppStore(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response) error {
	log.Info("Received appStoreApi.AddAppStore request")
	addAppStore := &appStore.AppStoreInfo{}
	//进行简单form数据映射
	form.FormToAppStoreStruct(req.Post,addAppStore)
	//设置图片
	e.SetImage(req,addAppStore)
	//设置POD
	e.SetPod(req,addAppStore)
	//设置中间件
	e.SetMiddle(req,addAppStore)
	//设置存储
	e.SetVolume(req,addAppStore)

	//调用后端服务进行更新
	response,err:=e.AppStoreService.AddAppStore(ctx,addAppStore)
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

//设置图片
func (e *AppStoreApi) SetImage(req *appStoreApi.Request,appStoreInfo *appStore.AppStoreInfo) {
	dataSlice,ok := req.Post["app_image"]
	if ok {
		imageSlice:=[]*appStore.AppImage{}
		for _,v := range dataSlice.Values {
			image := &appStore.AppImage{
				AppImageSrc: v,
			}
			imageSlice = append(imageSlice,image)
		}
		appStoreInfo.AppImage = imageSlice
	}
}

//设置POD模板
func (e *AppStoreApi) SetPod(req *appStoreApi.Request,appStoreInfo *appStore.AppStoreInfo)  {
	dataSlice,ok := req.Post["app_pod"]
	if ok {
		podSlice := []*appStore.AppPod{}
		for _,v := range dataSlice.Values {
			id,err := strconv.ParseInt(v,10,64)
			if err != nil {
				common.Error(err)
				continue
			}
			pod := &appStore.AppPod{
				AppPodId: id,
			}
			podSlice = append(podSlice,pod)
		}
		appStoreInfo.AppPod = podSlice
	}
}

//设置中间件模板
func (e *AppStoreApi) SetMiddle(req *appStoreApi.Request,appStoreInfo *appStore.AppStoreInfo)  {
	dataSlice,ok := req.Post["app_middle"]
	if ok {
		middleSlice := []*appStore.AppMiddle{}
		for _,v := range dataSlice.Values {
			id,err := strconv.ParseInt(v,10,64)
			if err != nil {
				common.Error(err)
				continue
			}
			middle := &appStore.AppMiddle{
				AppMiddleId: id,
			}
			middleSlice = append(middleSlice,middle)
		}
		appStoreInfo.AppMiddle = middleSlice
	}

}

//设置存储
func (e *AppStoreApi) SetVolume(req *appStoreApi.Request, appStoreInfo *appStore.AppStoreInfo) {
	dataSlice,ok := req.Post["app_volume"]
	if ok {
		volumeSlice := []*appStore.AppVolume{}
		for _,v := range dataSlice.Values {
			id,err:=strconv.ParseInt(v,10,64)
			if err != nil {
				common.Error(err)
				continue
			}
			volume := &appStore.AppVolume{
				AppVolumeId: id,
			}
			volumeSlice = append(volumeSlice,volume)
		}
		appStoreInfo.AppVolume = volumeSlice
	}
}

// appStoreApi.DeleteAppStoreById 通过API向外暴露为/appStoreApi/DeleteAppStoreById，接收http请求
// 即：/appStoreApi/DeleteAppStoreById 请求会调用go.micro.api.appStoreApi 服务的 appStoreApi.DeleteAppStoreById 方法
func (e *AppStoreApi) DeleteAppStoreById(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response) error {
	log.Info("Received appStoreApi.DeleteAppStoreById request")
	Id,err:=e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	response ,err := e.AppStoreService.DeleteAppStore(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// appStoreApi.UpdateAppStore 通过API向外暴露为/appStoreApi/UpdateAppStore，接收http请求
// 即：/appStoreApi/UpdateAppStore 请求会调用go.micro.api.appStoreApi 服务的appStoreApi.UpdateAppStore 方法
func (e *AppStoreApi) UpdateAppStore(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response) error {
	log.Info("Received appStoreApi.UpdateAppStore request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/appStoreApi/UpdateAppStore'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法appStoreApi.Call 通过API向外暴露为/appStoreApi/call，接收http请求
// 即：/appStoreApi/call或/appStoreApi/ 请求会调用go.micro.api.appStoreApi 服务的appStoreApi.FindAppStoreById 方法
func (e *AppStoreApi) Call(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response) error {
	log.Info("Received appStoreApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}

//安装统计接口
func (e *AppStoreApi) AddInstallNum(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response)error {
	Id,err := e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	response,err:= e.AppStoreService.AddInstallNum(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}
//获取安装数量
func (e *AppStoreApi)GetInstallNum(ctx context.Context,req *appStoreApi.Request,rsp *appStoreApi.Response) error {
	Id,err := e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	response,err:= e.AppStoreService.GetInstallNum(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
	
}

//安装统计接口
func (e *AppStoreApi) AddViewNum(ctx context.Context, req *appStoreApi.Request, rsp *appStoreApi.Response)error {
	Id,err := e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	response,err:= e.AppStoreService.AddViewNum(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}
//获取安装数量
func (e *AppStoreApi)GetViewNum(ctx context.Context,req *appStoreApi.Request,rsp *appStoreApi.Response) error {
	Id,err := e.GetId(req)
	if err != nil {
		common.Error(err)
		return err
	}
	response,err:= e.AppStoreService.GetViewNum(ctx,&appStore.AppStoreId{
		Id: Id,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil

}
