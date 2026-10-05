package handler
import (
	"context"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/route/domain/model"
	"git.imooc.com/coding-535/route/domain/service"
	log "github.com/asim/go-micro/v3/logger"
	route "git.imooc.com/coding-535/route/proto/route"
	"strconv"
)
type RouteHandler struct{
     //注意这里的类型是 IRouteDataService 接口类型
     RouteDataService service.IRouteDataService
}


// 添加路由
func (e *RouteHandler) AddRoute(ctx context.Context,info *route.RouteInfo , rsp *route.Response) error {
	log.Info("Received *route.AddRoute request")
	route := &model.Route{}
	if err := common.SwapTo(info,route);err!=nil{
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	//创建route到k8s
	if err:= e.RouteDataService.CreateRouteToK8s(info);err!=nil{
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	} else {
		//写入数据库
		routeID,err := e.RouteDataService.AddRoute(route)
		if err !=nil {
			common.Error(err)
			rsp.Msg = err.Error()
			return err
		}
		common.Info("Route 添加成功 ID 号为："+  strconv.FormatInt(routeID, 10))
		rsp.Msg="Route 添加成功 ID 号为："+  strconv.FormatInt(routeID, 10)
	}
	return nil
}
//删除route
func (e *RouteHandler) DeleteRoute(ctx context.Context, req *route.RouteId, rsp *route.Response) error {
	log.Info("Received *route.DeleteRoute request")
	routeModel,err := e.RouteDataService.FindRouteByID(req.Id)
	if err!=nil {
		common.Error(err)
		return err
	}
	//从k8s中删除，并且删除数据库中数据
	if err:= e.RouteDataService.DeleteRouteFromK8s(routeModel);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

//更新route
func (e *RouteHandler) UpdateRoute(ctx context.Context, req *route.RouteInfo, rsp *route.Response) error {
	log.Info("Received *route.UpdateRoute request")
	if err:=e.RouteDataService.UpdateRouteToK8s(req);err!=nil{
		common.Error(err)
		return err
	}
	//查询数据库的信息
	routeModel,err:=e.RouteDataService.FindRouteByID(req.Id)
	if err!=nil{
		common.Error(err)
		return err
	}
	//数据更新
	if err := common.SwapTo(req,routeModel);err!=nil{
		common.Error(err)
		return err
	}
	return e.RouteDataService.UpdateRoute(routeModel)
}

//根据ID查询route信息
func (e *RouteHandler) FindRouteByID(ctx context.Context, req *route.RouteId, rsp *route.RouteInfo) error {
	log.Info("Received *route.FindRouteByID request")
	routeModel,err:=e.RouteDataService.FindRouteByID(req.Id)
	if err !=nil {
		common.Error(err)
		return err
	}
	//数据转化
	if err := common.SwapTo(routeModel,rsp);err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

func (e *RouteHandler) FindAllRoute(ctx context.Context, req *route.FindAll, rsp *route.AllRoute) error {
	log.Info("Received *route.FindAllRoute request")
	allRoute,err := e.RouteDataService.FindAllRoute()
	if err !=nil {
		common.Error(err)
		return err
	}
	//整理下格式
	for _,v :=range allRoute{
		//创建实例
		routeInfo := &route.RouteInfo{}
		//把查询出来的数据进行转化
		if err := common.SwapTo(v,routeInfo);err!=nil{
			common.Error(err)
			return err
		}
		//数据合并
		rsp.RouteInfo = append(rsp.RouteInfo,routeInfo)
	}
	return nil
}


