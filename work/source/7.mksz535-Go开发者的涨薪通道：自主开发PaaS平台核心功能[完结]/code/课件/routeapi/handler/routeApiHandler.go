package handler

import (
	"context"
    "encoding/json"
	"errors"

	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/routeApi/form"
	log "github.com/asim/go-micro/v3/logger"
    route "git.imooc.com/coding-535/route/proto/route"
	routeApi "git.imooc.com/coding-535/routeApi/proto/routeApi"
	"strconv"
)

type RouteApi struct{
    RouteService route.RouteService
}


// routeApi.FindRouteById 通过API向外暴露为/routeApi/findRouteById，接收http请求
// 即：/routeApi/FindRouteById 请求会调用go.micro.api.routeApi 服务的routeApi.FindRouteById 方法
func (e *RouteApi) FindRouteById(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.FindRouteById request")
	if _,ok := req.Get["route_id"];!ok{
		rsp.StatusCode =500
		return errors.New("参数异常")
	}
	//获取 route id
	routeIdString := req.Get["route_id"].Values[0]
	routeId,err:= strconv.ParseInt(routeIdString,10,64)
	if err !=nil {
		common.Error(err)
		return err
	}
	//获取route信息
	routeInfo ,err := e.RouteService.FindRouteByID(ctx,&route.RouteId{
		Id: routeId,
	})
	if err !=nil {
		common.Error(err)
		return err
	}
	//返回route结果
	rsp.StatusCode = 200
	b, _ := json.Marshal(routeInfo)
	rsp.Body = string(b)
	return nil
}

// routeApi.AddRoute 通过API向外暴露为/routeApi/AddRoute，接收http请求
// 即：/routeApi/AddRoute 请求会调用go.micro.api.routeApi 服务的routeApi.AddRoute 方法
func (e *RouteApi) AddRoute(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.AddRoute request")
	addRouteInfo := &route.RouteInfo{}
	routePathName,ok:=req.Post["route_path_name"]
	if ok && len(routePathName.Values)>0{
		port,err:=strconv.ParseInt(req.Post["route_backend_service_port"].Values[0],10,32)
		if err !=nil {
			common.Error(err)
			return err
		}
		//这里如果有多个Path需要处理多个
		routePath:=&route.RoutePath{
			RoutePathName:           req.Post["route_path_name"].Values[0],
			RouteBackendService:     req.Post["route_backend_service"].Values[0],
			RouteBackendServicePort: int32(port),
		}
		//合并
		addRouteInfo.RoutePath = append(addRouteInfo.RoutePath,routePath)
	}
	form.FormToSvcStruct(req.Post,addRouteInfo)
	response,err:=e.RouteService.AddRoute(ctx,addRouteInfo)
	if err !=nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// routeApi.DeleteRouteById 通过API向外暴露为/routeApi/DeleteRouteById，接收http请求
// 即：/routeApi/DeleteRouteById 请求会调用go.micro.api.routeApi 服务的 routeApi.DeleteRouteById 方法
func (e *RouteApi) DeleteRouteById(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.DeleteRouteById request")
	if _,ok := req.Get["route_id"];!ok{
		rsp.StatusCode =500
		return errors.New("参数异常")
	}
	//获取 route id
	routeIdString := req.Get["route_id"].Values[0]
	routeId,err:= strconv.ParseInt(routeIdString,10,64)
	if err !=nil {
		common.Error(err)
		return err
	}
	//调用route 删除服务
	response,err:=e.RouteService.DeleteRoute(ctx,&route.RouteId{
		Id: routeId,
	})
	if err !=nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// routeApi.UpdateRoute 通过API向外暴露为/routeApi/UpdateRoute，接收http请求
// 即：/routeApi/UpdateRoute 请求会调用go.micro.api.routeApi 服务的routeApi.UpdateRoute 方法
func (e *RouteApi) UpdateRoute(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.UpdateRoute request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/routeApi/UpdateRoute'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法routeApi.Call 通过API向外暴露为/routeApi/call，接收http请求
// 即：/routeApi/call或/routeApi/ 请求会调用go.micro.api.routeApi 服务的routeApi.FindRouteById 方法
func (e *RouteApi) Call(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.Call request")
	allRoute,err:=e.RouteService.FindAllRoute(ctx,&route.FindAll{})
	if err !=nil{
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allRoute)
	rsp.Body = string(b)
	return nil
}

