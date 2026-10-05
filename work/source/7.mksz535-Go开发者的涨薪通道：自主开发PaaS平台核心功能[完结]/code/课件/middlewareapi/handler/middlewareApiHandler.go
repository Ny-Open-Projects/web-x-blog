package handler

import (
	"context"
    "encoding/json"
	"errors"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/middlewareApi/plugin/form"
	log "github.com/asim/go-micro/v3/logger"
    middleware "git.imooc.com/coding-535/middleware/proto/middleware"
	middlewareApi "git.imooc.com/coding-535/middlewareApi/proto/middlewareApi"
	"strconv"
)

type MiddlewareApi struct{
    MiddlewareService middleware.MiddlewareService
}


// middlewareApi.FindMiddlewareById 通过API向外暴露为/middlewareApi/findMiddlewareById，接收http请求
// 即：/middlewareApi/FindMiddlewareById 请求会调用go.micro.api.middlewareApi 服务的middlewareApi.FindMiddlewareById 方法
func (e *MiddlewareApi) FindMiddlewareById(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.FindMiddlewareById request")
	if _,ok:=req.Get["middle_id"];!ok{
		return errors.New("参数异常！")
	}
	idString := req.Get["middle_id"].Values[0]
	id,err := strconv.ParseInt(idString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	middleInfo,err:=e.MiddlewareService.FindMiddlewareByID(ctx,&middleware.MiddlewareId{Id:id})
	rsp.StatusCode = 200
	b, _ := json.Marshal(middleInfo)
	rsp.Body = string(b)
	return nil
}

// middlewareApi.AddMiddleware 通过API向外暴露为/middlewareApi/AddMiddleware，接收http请求
// 即：/middlewareApi/AddMiddleware 请求会调用go.micro.api.middlewareApi 服务的middlewareApi.AddMiddleware 方法
func (e *MiddlewareApi) AddMiddleware(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.AddMiddleware request")
	addMiddleInfo := &middleware.MiddlewareInfo{}
	//设置端口
	port,err := e.setMiddlePort(req)
	if err != nil {
		common.Error(err)
		return err
	}
	addMiddleInfo.MiddlePort = port

	//设置环境变量
	addMiddleInfo.MiddleEnv = e.setMiddleEnv(req)

	//设置存储
	addMiddleInfo.MiddleStorage = e.setMiddleStorage(req)

	//获取类型
	middleTypeInfo := e.getMiddleType(req)

	//判断不同的类型设置不同的值
	switch middleTypeInfo.MiddleTypeName {
	case "MYSQL":
		middleConfig := e.setMiddleConfig(req)
		addMiddleInfo.MiddleConfig = &middleConfig
	}

	//处理表单
	form.FormToMiddlewareStruct(req.Post,addMiddleInfo)
	//调用后端服务添加数据
	response,err := e.MiddlewareService.AddMiddleware(ctx,addMiddleInfo)
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

//设置mysql config 设置
func (e *MiddlewareApi) setMiddleConfig(req *middlewareApi.Request)(middleConfig middleware.MiddleConfig) {
	middleConfig.MiddleConfigRootUser = e.getValue(req,"middle_config_root_user")
	middleConfig.MiddleConfigRootPwd = e.getValue(req,"middle_config_root_pwd")
	middleConfig.MiddleConfigUser = e.getValue(req,"middle_config_user")
	middleConfig.MiddleConfigPwd = e.getValue(req,"middle_config_pwd")
	middleConfig.MiddleConfigDataBase = e.getValue(req,"middle_config_data_base")
	return
}

//获取post值
func (e *MiddlewareApi) getValue(req *middlewareApi.Request,key string) string  {
	value,ok := req.Post[key]
	if ok {
		return value.Values[0]
	}
	return ""
}

//获取类型
func (e *MiddlewareApi) getMiddleType(req *middlewareApi.Request)(middleTypeInfo middleware.MiddleTypeInfo) {
	typeValue,ok := req.Post["middle_type_id"]
	if ok {
		typeId,err := strconv.ParseInt(typeValue.Values[0],10,64)
		if err !=nil {
			common.Error(err)
			return
		}
		typeInfo,err := e.MiddlewareService.FindMiddleTypeByID(context.TODO(),&middleware.MiddleTypeId{
			Id: typeId,
		})
		if err != nil {
			common.Error(err)
			return
		}
		middleTypeInfo = *typeInfo
	}
	return
}

//设置中间件的存储
func (e *MiddlewareApi) setMiddleStorage(req *middlewareApi.Request) []*middleware.MiddleStorage {
	storageSlice := []*middleware.MiddleStorage{}
	//处理环境变量
	i := 1
	for {
		nameTag := "middle_storage.name."+strconv.Itoa(i)
		sizeTag := "middle_storage.size."+strconv.Itoa(i)
		pathTag := "middle_storage.path."+strconv.Itoa(i)
		key,ok := req.Post[nameTag]
		if ok {
			sizeValue,_ := strconv.ParseFloat(req.Post[sizeTag].Values[0],32)
			storage := &middleware.MiddleStorage{
				MiddleStorageName:       key.Values[0],
				MiddleStorageSize:       float32(sizeValue),
				MiddleStoragePath:       req.Post[pathTag].Values[0],
				MiddleStorageClass:      "csi-rbd-sc",
				MiddleStorageAccessMode: "ReadWriteOnce",
			}
			storageSlice = append(storageSlice,storage)
		} else {
			break
		}
		i++
	}
	return storageSlice
}

//设置中间件环境变量
func (e *MiddlewareApi) setMiddleEnv(req *middlewareApi.Request) []*middleware.MiddleEnv {
	envSlice := []*middleware.MiddleEnv{}
	//处理环境变量
	i:=1
	for {
		tag := "middle_env.key."+strconv.Itoa(i)
		valueTag := "middle_env.value."+strconv.Itoa(i)
		key,ok := req.Post[tag]
		if ok {
			env := &middleware.MiddleEnv{
				EnvKey:   key.Values[0],
				EnvValue: req.Post[valueTag].Values[0],
			}
			envSlice = append(envSlice,env)
		} else {
			break
		}
		i++
	}
	return envSlice
}

//设置端口
func (e *MiddlewareApi) setMiddlePort(req *middlewareApi.Request)([]*middleware.MiddlePort,error) {
	dataSlice,ok:= req.Post["middle_port"]
	if ok {
		//特殊处理
		middlePortSlice := []*middleware.MiddlePort{}
		for _,v := range dataSlice.Values{
			i,err := strconv.ParseInt(v,10,64)
			if err != nil {
				common.Error(err)
			}
			port := &middleware.MiddlePort{
				MiddlePort:     int32(i),
				MiddleProtocol: "TCP",
			}
			middlePortSlice = append(middlePortSlice,port)
		}
		return middlePortSlice,nil
	}
	return nil,errors.New("无端口")
}

// middlewareApi.DeleteMiddlewareById 通过API向外暴露为/middlewareApi/DeleteMiddlewareById，接收http请求
// 即：/middlewareApi/DeleteMiddlewareById 请求会调用go.micro.api.middlewareApi 服务的 middlewareApi.DeleteMiddlewareById 方法
func (e *MiddlewareApi) DeleteMiddlewareById(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.DeleteMiddlewareById request")
	if _,ok:=req.Get["middle_id"];!ok {
		return errors.New("参数异常")
	}
	IdString := req.Get["middle_id"].Values[0]
	Id,err := strconv.ParseInt(IdString,10,64)
	if err != nil {
		common.Error(err)
		return err
	}
	response,err:=e.MiddlewareService.DeleteMiddleware(ctx,&middleware.MiddlewareId{
		Id: Id,
	})
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}

// middlewareApi.UpdateMiddleware 通过API向外暴露为/middlewareApi/UpdateMiddleware，接收http请求
// 即：/middlewareApi/UpdateMiddleware 请求会调用go.micro.api.middlewareApi 服务的middlewareApi.UpdateMiddleware 方法
func (e *MiddlewareApi) UpdateMiddleware(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.UpdateMiddleware request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/middlewareApi/UpdateMiddleware'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法middlewareApi.Call 通过API向外暴露为/middlewareApi/call，接收http请求
// 即：/middlewareApi/call或/middlewareApi/ 请求会调用go.micro.api.middlewareApi 服务的middlewareApi.FindMiddlewareById 方法
func (e *MiddlewareApi) Call(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}
func (e *MiddlewareApi) FindAllMiddlewareByTypeId(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}

func (e *MiddlewareApi) FindMiddleTypeById(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}
func (e *MiddlewareApi) AddMiddleType(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	typeInfo:=&middleware.MiddleTypeInfo{
		//MiddleTypeName:     "CONSUL",
		//MiddleTypeImageSrc: "/consul.jpg",
		//MiddleVersion:      []*middleware.MiddleVersion{
		//	{
		//		MiddleDockerImage: "docker/consul",
		//		MiddleVs:          "v1.0.1",
		//	},
		//	{
		//		MiddleDockerImage: "docker/consul",
		//		MiddleVs:          "v1.0.2",
		//	},
		//},
	}
	rspInfo,err:=e.MiddlewareService.AddMiddleType(ctx,typeInfo)
	if err != nil {
		common.Error(err)
		return err
	}

	rsp.StatusCode = 200
	b, _ := json.Marshal(rspInfo)
	rsp.Body = string(b)
	return nil
}
func (e *MiddlewareApi) DeleteMiddleTypeById(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}
func (e *MiddlewareApi) UpdateMiddleType(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}

func (e *MiddlewareApi) FindAllMiddleType(ctx context.Context, req *middlewareApi.Request, rsp *middlewareApi.Response) error {
	log.Info("Received middlewareApi.Call request")
	allType,err:=e.MiddlewareService.FindAllMiddleType(ctx,&middleware.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allType)
	rsp.Body = string(b)
	return nil
}




