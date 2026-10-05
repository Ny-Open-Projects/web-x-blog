package handler

import (
	"context"
	"encoding/json"
	"errors"
	"git.imooc.com/coding-535/common"
	svc "git.imooc.com/coding-535/svc/proto/svc"
	from "git.imooc.com/coding-535/svcApi/plugin/form"
	svcApi "git.imooc.com/coding-535/svcApi/proto/svcApi"
	log "github.com/asim/go-micro/v3/logger"
	"strconv"
)

type SvcApi struct {
	SvcService svc.SvcService
}

// svcApi.FindSvcById 通过API向外暴露为/svcApi/findSvcById，接收http请求
// 即：/svcApi/FindSvcById 请求会调用go.micro.api.svcApi 服务的svcApi.FindSvcById 方法
func (e *SvcApi) FindSvcById(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("接受 svcApi.FindSvcById 的请求")
	if _, ok := req.Get["svc_id"]; !ok {
		rsp.StatusCode = 500
		return errors.New("参数异常")
	}
	//获取 svcId 参数
	svcIdString := req.Get["svc_id"].Values[0]
	svcId, err := strconv.ParseInt(svcIdString, 10, 64)
	if err != nil {
		common.Error(err)
		return err
	}
	//获取svc相关信息
	svcInfo, err := e.SvcService.FindSvcByID(ctx, &svc.SvcId{
		Id: svcId,
	})
	if err != nil {
		common.Error(err)
		return err
	}
	//json 返回svc信息

	rsp.StatusCode = 200
	b, _ := json.Marshal(svcInfo)
	rsp.Body = string(b)
	return nil
}

// svcApi.AddSvc 通过API向外暴露为/svcApi/AddSvc，接收http请求
// 即：/svcApi/AddSvc 请求会调用go.micro.api.svcApi 服务的svcApi.AddSvc 方法
func (e *SvcApi) AddSvc(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("添加svc服务")
	//处理port
	addSvcInfo := &svc.SvcInfo{}
	svcType, ok := req.Post["svc_type"]
	if ok && len(svcType.Values) > 0 {
		svcPort := &svc.SvcPort{}
		switch svcType.Values[0] {
		case "ClusterIP":
			port, err := strconv.ParseInt(req.Post["svc_port"].Values[0], 10, 32)
			if err != nil {
				common.Error(err)
				return err
			}
			svcPort.SvcPort = int32(port)
			targetPort,err:=strconv.ParseInt(req.Post["svc_target_port"].Values[0],10,32)
			if err != nil {
				common.Error(err)
				return err
			}
			svcPort.SvcTargetPort=int32(targetPort)
			svcPort.SvcPortProtocol = req.Post["svc_port_protocol"].Values[0]
			addSvcInfo.SvcPort = append(addSvcInfo.SvcPort,svcPort)
		default:
			return errors.New("类型不支持")
		}
	}
	//form 类型转换到结构体中
	from.FormToSvcStruct(req.Post,addSvcInfo)
	response,err:= e.SvcService.AddSvc(ctx,addSvcInfo)
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// svcApi.DeleteSvcById 通过API向外暴露为/svcApi/DeleteSvcById，接收http请求
// 即：/svcApi/DeleteSvcById 请求会调用go.micro.api.svcApi 服务的 svcApi.DeleteSvcById 方法
func (e *SvcApi) DeleteSvcById(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("删除svc服务")
	if _,ok:=req.Get["svc_id"];!ok{
		return errors.New("参数异常")
	}
	//获取需要删除的ID
	svcIdString := req.Get["svc_id"].Values[0]
	svcId,err:= strconv.ParseInt(svcIdString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	//调用后端服务删除
	response,err:=e.SvcService.DeleteSvc(ctx,&svc.SvcId{
		Id: svcId,
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

// svcApi.UpdateSvc 通过API向外暴露为/svcApi/UpdateSvc，接收http请求
// 即：/svcApi/UpdateSvc 请求会调用go.micro.api.svcApi 服务的svcApi.UpdateSvc 方法
func (e *SvcApi) UpdateSvc(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("Received svcApi.UpdateSvc request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/svcApi/UpdateSvc'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法svcApi.Call 通过API向外暴露为/svcApi/call，接收http请求
// 即：/svcApi/call或/svcApi/ 请求会调用go.micro.api.svcApi 服务的svcApi.FindSvcById 方法
func (e *SvcApi) Call(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("查询所有svc服务")
	allSvc,err:=e.SvcService.FindAllSvc(ctx,&svc.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allSvc)
	rsp.Body = string(b)
	return nil
}
