package handler

import (
	"context"
    "encoding/json"
	"errors"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/volumeApi/form"
	log "github.com/asim/go-micro/v3/logger"
    volume "git.imooc.com/coding-535/volume/proto/volume"
	volumeApi "git.imooc.com/coding-535/volumeApi/proto/volumeApi"
	"strconv"
)

type VolumeApi struct{
    VolumeService volume.VolumeService
}


// volumeApi.FindVolumeById 通过API向外暴露为/volumeApi/findVolumeById，接收http请求
// 即：/volumeApi/FindVolumeById 请求会调用go.micro.api.volumeApi 服务的volumeApi.FindVolumeById 方法
func (e *VolumeApi) FindVolumeById(ctx context.Context, req *volumeApi.Request, rsp *volumeApi.Response) error {
	log.Info("Received volumeApi.FindVolumeById request")
	if _,ok:= req.Get["volume_id"];!ok{
		rsp.StatusCode=500
		return errors.New("参数有异常")
	}
	//获取 volume_id
	volumeIdString := req.Get["volume_id"].Values[0]
	volumeId,err:= strconv.ParseInt(volumeIdString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	//获取 volume 信息
	volumeInfo,err := e.VolumeService.FindVolumeByID(ctx,&volume.VolumeId{
		Id: volumeId,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(volumeInfo)
	rsp.Body = string(b)
	return nil
}

// volumeApi.AddVolume 通过API向外暴露为/volumeApi/AddVolume，接收http请求
// 即：/volumeApi/AddVolume 请求会调用go.micro.api.volumeApi 服务的volumeApi.AddVolume 方法
func (e *VolumeApi) AddVolume(ctx context.Context, req *volumeApi.Request, rsp *volumeApi.Response) error {
	log.Info("Received volumeApi.AddVolume request")
	addVolumeInfo := &volume.VolumeInfo{}
	form.FormToSvcStruct(req.Post,addVolumeInfo)
	response,err:=e.VolumeService.AddVolume(ctx,addVolumeInfo)
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// volumeApi.DeleteVolumeById 通过API向外暴露为/volumeApi/DeleteVolumeById，接收http请求
// 即：/volumeApi/DeleteVolumeById 请求会调用go.micro.api.volumeApi 服务的 volumeApi.DeleteVolumeById 方法
func (e *VolumeApi) DeleteVolumeById(ctx context.Context, req *volumeApi.Request, rsp *volumeApi.Response) error {
	log.Info("Received volumeApi.DeleteVolumeById request")
	if _,ok := req.Get["volume_id"];!ok{
		rsp.StatusCode =500
		return errors.New("参数异常")
	}
	//获取 volume_id
	volumeIdString := req.Get["volume_id"].Values[0]
	volumeId,err:= strconv.ParseInt(volumeIdString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	//调用 volume 删除服务
	response,err:=e.VolumeService.DeleteVolume(ctx,&volume.VolumeId{
		Id: volumeId,
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

// volumeApi.UpdateVolume 通过API向外暴露为/volumeApi/UpdateVolume，接收http请求
// 即：/volumeApi/UpdateVolume 请求会调用go.micro.api.volumeApi 服务的volumeApi.UpdateVolume 方法
func (e *VolumeApi) UpdateVolume(ctx context.Context, req *volumeApi.Request, rsp *volumeApi.Response) error {
	log.Info("Received volumeApi.UpdateVolume request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/volumeApi/UpdateVolume'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法volumeApi.Call 通过API向外暴露为/volumeApi/call，接收http请求
// 即：/volumeApi/call或/volumeApi/ 请求会调用go.micro.api.volumeApi 服务的volumeApi.FindVolumeById 方法
func (e *VolumeApi) Call(ctx context.Context, req *volumeApi.Request, rsp *volumeApi.Response) error {
	log.Info("Received volumeApi.Call request")
	allVolume ,err:= e.VolumeService.FindAllVolume(ctx,&volume.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allVolume)
	rsp.Body = string(b)
	return nil
}

