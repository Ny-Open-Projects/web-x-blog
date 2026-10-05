package handler
import (
	"context"
	"git.imooc.com/coding-535/appStore/domain/model"
	"git.imooc.com/coding-535/appStore/domain/service"
	"git.imooc.com/coding-535/common"
	log "github.com/asim/go-micro/v3/logger"
	appStore "git.imooc.com/coding-535/appStore/proto/appStore"
	"strconv"
)
type AppStoreHandler struct{
     //注意这里的类型是 IAppStoreDataService 接口类型
     AppStoreDataService service.IAppStoreDataService
}

//添加安装统计
func (e *AppStoreHandler) AddInstallNum(ctx context.Context,req *appStore.AppStoreId,rsp *appStore.Response) error {
	if err:=e.AppStoreDataService.AddInstallNum(req.Id);err!=nil{
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "统计成功"
	return nil
}
//获取安装数量
func (e *AppStoreHandler) GetInstallNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Number) error {
	rsp.Num = e.AppStoreDataService.GetInstallNum(req.Id)
	return nil
}
//添加查询统计
func (e *AppStoreHandler) AddViewNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	if err:=e.AppStoreDataService.AddViewNum(req.Id);err!=nil{
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "统计成功"
	return nil
}
//获取查询数量
func (e *AppStoreHandler) GetViewNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Number) error {
	rsp.Num = e.AppStoreDataService.GetViewNum(req.Id)
	return nil


}

// Call is a single request handler called via client.Call or the generated client code
func (e *AppStoreHandler) AddAppStore(ctx context.Context,info *appStore.AppStoreInfo , rsp *appStore.Response) error {
	log.Info("Received *appStore.AddAppStore request")
	appStoreModel := &model.AppStore{}
	if err:=common.SwapTo(info,appStoreModel);err!=nil{
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}

	appStoreID,err:= e.AppStoreDataService.AddAppStore(appStoreModel)
	if err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "应用市场中新应用添加成功 ID 号为："+strconv.FormatInt(appStoreID,10)
	common.Info(rsp.Msg)
	return nil
}

func (e *AppStoreHandler) DeleteAppStore(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	log.Info("Received *appStore.DeleteAppStore request")
	return e.AppStoreDataService.DeleteAppStore(req.Id)
}

func (e *AppStoreHandler) UpdateAppStore(ctx context.Context, req *appStore.AppStoreInfo, rsp *appStore.Response) error {
	log.Info("Received *appStore.UpdateAppStore request")
	appStoreModel,err:=e.AppStoreDataService.FindAppStoreByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := common.SwapTo(req,appStoreModel);err!=nil{
		common.Error(err)
		return err
	}
	return e.AppStoreDataService.UpdateAppStore(appStoreModel)
}

func (e *AppStoreHandler) FindAppStoreByID(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.AppStoreInfo) error {
	log.Info("Received *appStore.FindAppStoreByID request")
	appStoreModel ,err:= e.AppStoreDataService.FindAppStoreByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err:= common.SwapTo(appStoreModel,rsp);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

func (e *AppStoreHandler) FindAllAppStore(ctx context.Context, req *appStore.FindAll, rsp *appStore.AllAppStore) error {
	log.Info("Received *appStore.FindAllAppStore request")
	allAppStore,err := e.AppStoreDataService.FindAllAppStore()
	if err != nil {
		common.Error(err)
		return err
	}
	//整理数据格式
	for _,v := range allAppStore{
		appStoreInfo := &appStore.AppStoreInfo{}
		if err:=common.SwapTo(v,appStoreInfo);err!=nil{
			common.Error(err)
			return err
		}
		rsp.AppStoreInfo = append(rsp.AppStoreInfo,appStoreInfo)
	}
	return nil
}


