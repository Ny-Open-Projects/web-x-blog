package template

var (
//	HandlerFNC = `package handler
//
//import (
//	"context"
//
//	{{.Alias}} "{{.Dir}}/proto/{{.Alias}}"
//)
//
//type {{title .Alias}} struct{}
//
//
//`

	HandlerSRV = `package handler
import (
	"context"
    "{{.Dir}}/domain/service"
	log "github.com/asim/go-micro/v3/logger"
	{{.Alias}} "{{.Dir}}/proto/{{.Alias}}"
)
type {{title .Alias}}Handler struct{
     //注意这里的类型是 I{{title .Alias}}DataService 接口类型
     {{title .Alias}}DataService service.I{{title .Alias}}DataService
}


// Call is a single request handler called via client.Call or the generated client code
func (e *{{title .Alias}}Handler) Add{{title .Alias}}(ctx context.Context,info *{{.Alias}}.{{title .Alias}}Info , rsp *{{.Alias}}.Response) error {
	log.Info("Received *{{.Alias}}.Add{{title .Alias}} request")


	return nil
}

func (e *{{title .Alias}}Handler) Delete{{title .Alias}}(ctx context.Context, req *{{.Alias}}.{{title .Alias}}Id, rsp *{{.Alias}}.Response) error {
	log.Info("Received *{{.Alias}}.Delete{{title .Alias}} request")

	return nil
}

func (e *{{title .Alias}}Handler) Update{{title .Alias}}(ctx context.Context, req *{{.Alias}}.{{title .Alias}}Info, rsp *{{.Alias}}.Response) error {
	log.Info("Received *{{.Alias}}.Update{{title .Alias}} request")

	return nil
}

func (e *{{title .Alias}}Handler) Find{{title .Alias}}ByID(ctx context.Context, req *{{.Alias}}.{{title .Alias}}Id, rsp *{{.Alias}}.{{title .Alias}}Info) error {
	log.Info("Received *{{.Alias}}.Find{{title .Alias}}ByID request")

	return nil
}

func (e *{{title .Alias}}Handler) FindAll{{title .Alias}}(ctx context.Context, req *{{.Alias}}.FindAll, rsp *{{.Alias}}.All{{title .Alias}}) error {
	log.Info("Received *{{.Alias}}.FindAll{{title .Alias}} request")

	return nil
}


`

//	SubscriberFNC = `package subscriber
//
//import (
//	"context"
//
//	log "github.com/micro/go-micro/v2/logger"
//
//	{{.Alias}} "{{.Dir}}/proto/{{.Alias}}"
//)
//
//type {{title .Alias}} struct{}
//
//
//`

//	SubscriberSRV = `package subscriber
//
//import (
//	"context"
//
//	{{.Alias}} "{{.Dir}}/proto/{{.Alias}}"
//)
//
//type {{title .Alias}} struct{}
//
//`

	HandlerAPI = `package handler

import (
	"context"
    "encoding/json"
	log "github.com/asim/go-micro/v3/logger"
    {{.ApiDefaultServerName}} "git.imooc.com/coding-535/{{.ApiDefaultServerName}}/proto/{{.ApiDefaultServerName}}"
	{{.Alias}} "{{.Dir}}/proto/{{.Alias}}"
)

type {{title .Alias}} struct{
    {{title .ApiDefaultServerName}}Service {{.ApiDefaultServerName}}.{{title .ApiDefaultServerName}}Service
}


// {{.Alias}}.Find{{title .ApiDefaultServerName}}ById 通过API向外暴露为/{{.Alias}}/find{{title .ApiDefaultServerName}}ById，接收http请求
// 即：/{{.Alias}}/Find{{title .ApiDefaultServerName}}ById 请求会调用go.micro.api.{{.Alias}} 服务的{{.Alias}}.Find{{title .ApiDefaultServerName}}ById 方法
func (e *{{title .Alias}}) Find{{title .ApiDefaultServerName}}ById(ctx context.Context, req *{{.Alias}}.Request, rsp *{{.Alias}}.Response) error {
	log.Info("Received {{.Alias}}.Find{{title .ApiDefaultServerName}}ById request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/{{.Alias}}/Find{{title .ApiDefaultServerName}}ById'}")
	rsp.Body = string(b)
	return nil
}

// {{.Alias}}.Add{{title .ApiDefaultServerName}} 通过API向外暴露为/{{.Alias}}/Add{{title .ApiDefaultServerName}}，接收http请求
// 即：/{{.Alias}}/Add{{title .ApiDefaultServerName}} 请求会调用go.micro.api.{{.Alias}} 服务的{{.Alias}}.Add{{title .ApiDefaultServerName}} 方法
func (e *{{title .Alias}}) Add{{title .ApiDefaultServerName}}(ctx context.Context, req *{{.Alias}}.Request, rsp *{{.Alias}}.Response) error {
	log.Info("Received {{.Alias}}.Add{{title .ApiDefaultServerName}} request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/{{.Alias}}/Add{{title .ApiDefaultServerName}}'}")
	rsp.Body = string(b)
	return nil
}

// {{.Alias}}.Delete{{title .ApiDefaultServerName}}ById 通过API向外暴露为/{{.Alias}}/Delete{{title .ApiDefaultServerName}}ById，接收http请求
// 即：/{{.Alias}}/Delete{{title .ApiDefaultServerName}}ById 请求会调用go.micro.api.{{.Alias}} 服务的 {{.Alias}}.Delete{{title .ApiDefaultServerName}}ById 方法
func (e *{{title .Alias}}) Delete{{title .ApiDefaultServerName}}ById(ctx context.Context, req *{{.Alias}}.Request, rsp *{{.Alias}}.Response) error {
	log.Info("Received {{.Alias}}.Delete{{title .ApiDefaultServerName}}ById request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/{{.Alias}}/Delete{{title .ApiDefaultServerName}}ById'}")
	rsp.Body = string(b)
	return nil
}

// {{.Alias}}.Update{{title .ApiDefaultServerName}} 通过API向外暴露为/{{.Alias}}/Update{{title .ApiDefaultServerName}}，接收http请求
// 即：/{{.Alias}}/Update{{title .ApiDefaultServerName}} 请求会调用go.micro.api.{{.Alias}} 服务的{{.Alias}}.Update{{title .ApiDefaultServerName}} 方法
func (e *{{title .Alias}}) Update{{title .ApiDefaultServerName}}(ctx context.Context, req *{{.Alias}}.Request, rsp *{{.Alias}}.Response) error {
	log.Info("Received {{.Alias}}.Update{{title .ApiDefaultServerName}} request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问/{{.Alias}}/Update{{title .ApiDefaultServerName}}'}")
	rsp.Body = string(b)
	return nil
}

// 默认的方法{{.Alias}}.Call 通过API向外暴露为/{{.Alias}}/call，接收http请求
// 即：/{{.Alias}}/call或/{{.Alias}}/ 请求会调用go.micro.api.{{.Alias}} 服务的{{.Alias}}.Find{{title .ApiDefaultServerName}}ById 方法
func (e *{{title .Alias}}) Call(ctx context.Context, req *{{.Alias}}.Request, rsp *{{.Alias}}.Response) error {
	log.Info("Received {{.Alias}}.Call request")
	rsp.StatusCode = 200
	b, _ := json.Marshal("{success:'成功访问：Call'}")
	rsp.Body = string(b)
	return nil
}

`
//
//	HandlerWEB = `package handler
//
//import (
//	"context"
//	"encoding/json"
//	"net/http"
//	"time"
//
//	"github.com/micro/go-micro/v2/client"
//	{{.Alias}} "path/to/service/proto/{{.Alias}}"
//)
//
//func {{title .Alias}}Call(w http.ResponseWriter, r *http.Request) {
//	// decode the incoming request as json
//	var request map[string]interface{}
//	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
//		http.Error(w, err.Error(), 500)
//		return
//	}
//
//	// call the backend service
//	{{.Alias}}Client := {{.Alias}}.New{{title .Alias}}Service("{{.Namespace}}.service.{{.Alias}}", client.DefaultClient)
//	rsp, err := {{.Alias}}Client.Call(context.TODO(), &{{.Alias}}.Request{
//		Name: request["name"].(string),
//	})
//	if err != nil {
//		http.Error(w, err.Error(), 500)
//		return
//	}
//
//	// we want to augment the response
//	response := map[string]interface{}{
//		"msg": rsp.Msg,
//		"ref": time.Now().UnixNano(),
//	}
//
//	// encode and write the response as json
//	if err := json.NewEncoder(w).Encode(response); err != nil {
//		http.Error(w, err.Error(), 500)
//		return
//	}
//}
//`
)
