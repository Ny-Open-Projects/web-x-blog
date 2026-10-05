package handler

import (
	"context"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/pod/domain/model"
	"git.imooc.com/coding-535/pod/domain/service"
	"git.imooc.com/coding-535/pod/proto/pod"
	"strconv"
)

type PodHandler struct {
	//注意这里的类型实 IPodDataService 接口类型
	PodDataService service.IPodDataService
}

//添加创建POD
func (e *PodHandler) AddPod(ctx context.Context, info *pod.PodInfo, rsp *pod.Response) error {
	common.Info("添加pod")
	podModel := &model.Pod{}
	err := common.SwapTo(info,podModel)
	if err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}

	if err:=e.PodDataService.CreateToK8s(info);err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	} else {
		//操作数据库写入数据
		podID,err := e.PodDataService.AddPod(podModel)
		if err != nil {
			common.Error(err)
			rsp.Msg = err.Error()
			return err
		}
		common.Info("Pod 添加成功数据库ID号为：" + strconv.FormatInt(podID, 10))
		rsp.Msg = "Pod 添加成功数据库ID号为：" + strconv.FormatInt(podID, 10)
	}
	return nil
}

//删除k8s中的pod 和数据库中的数据
func (e *PodHandler) DeletePod(ctx context.Context, req *pod.PodId, rsp *pod.Response) error {
	//先查找数据
	podModel ,err := e.PodDataService.FindPodByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := e.PodDataService.DeleteFromK8s(podModel);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

//更新指定的pod
func (e *PodHandler) UpdatePod(ctx context.Context, req *pod.PodInfo, rsp *pod.Response) error {
	//先更新k8s中的pod信息
	err := e.PodDataService.UpdateToK8s(req)
	if err != nil {
		common.Error(err)
		return err
	}
	//查询数据库中的pod
	podModel,err:=e.PodDataService.FindPodByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	err = common.SwapTo(req,podModel)
	if err != nil {
		common.Error(err)
		return err
	}
	e.PodDataService.UpdatePod(podModel)
	return nil

}

//查询单个信息
func (e *PodHandler) FindPodByID(ctx context.Context,req *pod.PodId,rsp *pod.PodInfo) error  {
	//查询pod数据
	podModel ,err := e.PodDataService.FindPodByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	err = common.SwapTo(podModel,rsp)
	if err != nil {
		common.Error(err)
		return err
	}
	return nil

}

//查询所有pod
func (e *PodHandler) FindAllPod(ctx context.Context, req *pod.FindAll, rsp *pod.AllPod) error {
	//查询所有pod
	allPod ,err := e.PodDataService.FindAllPod()
	if err != nil {
		common.Error(err)
		return err
	}
	//整理格式
	for _,v:=range allPod{
		podInfo := &pod.PodInfo{}
		err := common.SwapTo(v,podInfo)
		if err != nil {
			common.Error(err)
			return err
		}
		rsp.PodInfo = append(rsp.PodInfo,podInfo)
	}
	return nil
}



