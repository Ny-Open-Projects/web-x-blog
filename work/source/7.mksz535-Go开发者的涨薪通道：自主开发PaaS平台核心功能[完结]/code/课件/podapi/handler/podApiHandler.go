package handler

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/pod/proto/pod"
	from "git.imooc.com/coding-535/podApi/plugin/form"
	"git.imooc.com/coding-535/podApi/proto/podApi"
	"strconv"
)

type PodApi struct {
	PodService pod.PodService
}

// podApi.FindPodById 通过API向外暴露为/podApi/findPodById，接收http请求
// 即：/podApi/FindPodById 请求会调用go.micro.api.podApi 服务的podApi.FindPodById 方法
func (e *PodApi) FindPodById(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
	fmt.Println("接受到 podApi.FindPodById 的请求")
	if _,ok := req.Get["pod_id"]; !ok {
		rsp.StatusCode = 500
		return errors.New("参数异常")
	}
	//获取podid 参数
	podIdString := req.Get["pod_id"].Values[0]
	podId,err := strconv.ParseInt(podIdString,10,64)
	if err != nil {
		return err
	}
	//获取pod相关信息
	podInfo ,err := e.PodService.FindPodByID(ctx,&pod.PodId{
		Id: podId,
	})
	if err != nil {
		return err
	}
	//json 返回pod信息
	rsp.StatusCode = 200
	b,_:= json.Marshal(podInfo)
	rsp.Body = string(b)
	return nil
}

// podApi.AddPod 通过API向外暴露为/podApi/addPod，接收http请求
// 即：/podApi/AddPod 请求会调用go.micro.api.podApi 服务的podApi.AddPod 方法
func (e *PodApi) AddPod(ctx context.Context,req *podApi.Request,rsp *podApi.Response) error {
	fmt.Println("接受到 podApi.AddPod 的请求")
	addPodInfo := &pod.PodInfo{}
	//处理 port
	dataSlice,ok := req.Post["pod_port"]
	if ok {
		//特殊处理
		podSlice:=  []*pod.PodPort{}
		for _,v := range dataSlice.Values{
			i,err := strconv.ParseInt(v,10,32)
			if err != nil {
				common.Error(err)
			}
			port := &pod.PodPort{
				ContainerPort: int32(i),
				Protocol:      "TCP",
			}
			podSlice=append(podSlice,port)
		}
		addPodInfo.PodPort=podSlice
	}
	//form类型转化到结构体中
	from.FromToPodStruct(req.Post,addPodInfo)

	response,err:=e.PodService.AddPod(ctx,addPodInfo)
	if err != nil {
		common.Error(err)
		return err
	}

	rsp.StatusCode = 200
	b,_:= json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// podApi.DeletePodById 通过API向外暴露为/podApi/deletePodById，接收http请求
// 即：/podApi/DeletePodById 请求会调用go.micro.api.podApi 服务的 podApi.DeletePodById 方法
func (e *PodApi) DeletePodById(ctx context.Context ,req *podApi.Request,rsp *podApi.Response) error  {
	fmt.Println("接受到 podApi.DeletePodById 的请求")
	if _,ok:=req.Get["pod_id"];!ok {
		return errors.New("参数异常")
	}
	//获取要删除的ID
	podIdString := req.Get["pod_id"].Values[0]
	podId,err := strconv.ParseInt(podIdString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	//删除指定服务
	response,err:= e.PodService.DeletePod(ctx,&pod.PodId{
		Id: podId,
	})
	if err != nil {
		common.Error(err)
		return err
	}

	rsp.StatusCode = 200
	b,_:= json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// podApi.UpdatePod 通过API向外暴露为/podApi/updatePod，接收http请求
// 即：/podApi/UpdatePod 请求会调用go.micro.api.podApi 服务的podApi.UpdatePod 方法
func (e *PodApi) UpdatePod(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
	fmt.Println("接受到 podApi.UpdatePod 的请求")
	rsp.StatusCode = 200
	b,_:= json.Marshal("{success:'成功访问 /podApi/UpdatePod'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法podApi.Call 通过API向外暴露为/podApi/call，接收http请求
// 即：/podApi/call或/podApi/ 请求会调用go.micro.api.podApi 服务的podApi.Call 方法
func (e *PodApi) Call(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
	fmt.Println("接受到 podApi.Call 的请求")
	allPod,err:=e.PodService.FindAllPod(ctx,&pod.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b,_:= json.Marshal(allPod)
	rsp.Body = string(b)
	return nil
}