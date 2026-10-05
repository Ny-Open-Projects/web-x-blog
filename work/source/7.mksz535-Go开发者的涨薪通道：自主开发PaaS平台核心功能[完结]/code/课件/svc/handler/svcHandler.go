package handler
import (
	"context"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/svc/domain/model"
	"git.imooc.com/coding-535/svc/domain/service"
	log "github.com/asim/go-micro/v3/logger"
	svc "git.imooc.com/coding-535/svc/proto/svc"
	"strconv"
)
type SvcHandler struct{
     //注意这里的类型是 ISvcDataService 接口类型
     SvcDataService service.ISvcDataService
}


//添加服务
func (e *SvcHandler) AddSvc(ctx context.Context,info *svc.SvcInfo , rsp *svc.Response) error {
	log.Info("创建服务")
	svcModel := &model.Svc{}
	//数据类型转换
	if err:=common.SwapTo(info,svcModel);err!=nil{
		common.Error(err)
		return err
	}

	//到 k8s 中创建服务
	if err := e.SvcDataService.CreateSvcToK8s(info);err!=nil{
		common.Error(err)
		return err
	} else {
		svcID,err:=e.SvcDataService.AddSvc(svcModel)
		if err != nil {
			//如果逻辑需要自行实现k8s中删除操作
			common.Error(err)
			return err
		}
		common.Info("Svc 添加数据成功ID号为："+strconv.FormatInt(svcID,10))
		rsp.Msg = "Svc 添加数据成功ID号为："+strconv.FormatInt(svcID,10)
	}
	return nil
}

//删除服务
func (e *SvcHandler) DeleteSvc(ctx context.Context, req *svc.SvcId, rsp *svc.Response) error {
	log.Info("删除服务")
	service,err:=e.SvcDataService.FindSvcByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}

	if err:= e.SvcDataService.DeleteFromK8s(service);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}
//更新svc
func (e *SvcHandler) UpdateSvc(ctx context.Context, req *svc.SvcInfo, rsp *svc.Response) error {
	log.Info("Received *svc.UpdateSvc request")
	//先更新k8s里面的数据
	if err:=e.SvcDataService.UpdateSvcToK8s(req);err!=nil{
		common.Error(err)
		return err
	}
	//查询数据库中的svc
	service,err:=e.SvcDataService.FindSvcByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	//数据类型转换
	if err := common.SwapTo(req,service);err!=nil{
		common.Error(err)
		return err
	}
	//更新到数据中
	if err:=e.SvcDataService.UpdateSvc(service);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

//服务查找
func (e *SvcHandler) FindSvcByID(ctx context.Context, req *svc.SvcId, rsp *svc.SvcInfo) error {
	log.Info("查找服务")
	svcModel,err:=e.SvcDataService.FindSvcByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err:=common.SwapTo(svcModel,rsp);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}
//查找所有服务
func (e *SvcHandler) FindAllSvc(ctx context.Context, req *svc.FindAll, rsp *svc.AllSvc) error {
	log.Info("查询所有服务")
	allSvc,err := e.SvcDataService.FindAllSvc()
	if err != nil {
		common.Error(err)
		return err
	}
	//整理格式
	for _,v:=range allSvc{
		svcInfo := &svc.SvcInfo{}
		if err:= common.SwapTo(v,svcInfo);err!=nil{
			common.Error(err)
			return err
		}
		rsp.SvcInfo = append(rsp.SvcInfo,svcInfo)
	}
	return nil
}


