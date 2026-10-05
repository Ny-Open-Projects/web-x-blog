package main

import (
	"fmt"
	"git.imooc.com/coding-535/common"
    go_micro_service_route "git.imooc.com/coding-535/route/proto/route"
	"github.com/afex/hystrix-go/hystrix"
	"github.com/asim/go-micro/plugins/registry/consul/v3"
	ratelimit "github.com/asim/go-micro/plugins/wrapper/ratelimiter/uber/v3"
	opentracing2 "github.com/asim/go-micro/plugins/wrapper/trace/opentracing/v3"
    "github.com/asim/go-micro/plugins/wrapper/select/roundrobin/v3"
	"github.com/asim/go-micro/v3"
    "github.com/asim/go-micro/v3/server"
	"github.com/asim/go-micro/v3/registry"

	_ "github.com/jinzhu/gorm/dialects/mysql"
	"github.com/opentracing/opentracing-go"
	"net"
	"net/http"
	"git.imooc.com/coding-535/routeApi/handler"
	hystrix2 "git.imooc.com/coding-535/routeApi/plugin/hystrix"
	"strconv"

    
	routeApi "git.imooc.com/coding-535/routeApi/proto/routeApi"
)

var (
    //服务地址
	hostIp = "192.168.0.115"
    //服务地址
    serviceHost = hostIp
    //服务端口
	servicePort = "8088"
	//注册中心配置
	consulHost  = hostIp
	consulPort int64 = 8500
	//链路追踪
	tracerHost = hostIp
	tracerPort = 6831
	//熔断端口，每个服务不能重复
	hystrixPort = 9098
	//监控端口，每个服务不能重复
	prometheusPort = 9198
)

func main() {
    //需要本地启动，mysql，consul中间件服务
	//1.注册中心
	consul:=consul.NewRegistry(func(options *registry.Options) {
		options.Addrs = []string{
			consulHost+":"+strconv.FormatInt(consulPort,10),
		}
	})
 

	//2.添加链路追踪
	t,io,err := common.NewTracer("go.micro.api.routeApi",tracerHost+":"+strconv.Itoa(tracerPort))
	if err !=nil {
		common.Error(err)
	}
	defer io.Close()
	opentracing.SetGlobalTracer(t)

	//3.添加熔断器
	hystrixStreamHandler := hystrix.NewStreamHandler()
	hystrixStreamHandler.Start()

	//添加日志中心
	//1）需要程序日志打入到日志文件中
	//2）在程序中添加filebeat.yml 文件
	//3) 启动filebeat，启动命令 ./filebeat -e -c filebeat.yml
	fmt.Println("日志统一记录在根目录 micro.log 文件中，请点击查看日志！")

	//启动监听程序
	go func() {
		//http://192.168.0.112:9092/turbine/turbine.stream
		//看板访问地址 http://127.0.0.1:9002/hystrix，url后面一定要带 /hystrix
		err = http.ListenAndServe(net.JoinHostPort("0.0.0.0",strconv.Itoa(hystrixPort)),hystrixStreamHandler)
		if err !=nil {
			common.Error(err)
		}
	}()

	//4.添加监控
	common.PrometheusBoot(prometheusPort)

	//5.创建服务
	service := micro.NewService(
		//自定义服务地址，且必须写在其它参数前面
		micro.Server(server.NewServer(func(opts *server.Options) {
			opts.Advertise = serviceHost+":"+servicePort

		})),
		micro.Name("go.micro.api.routeApi"),
		micro.Version("latest"),
		//指定服务端口
		micro.Address(":"+servicePort),
		//添加注册中心
		micro.Registry(consul),
		//添加链路追踪
		micro.WrapHandler(opentracing2.NewHandlerWrapper(opentracing.GlobalTracer())),
		micro.WrapClient(opentracing2.NewClientWrapper(opentracing.GlobalTracer())),
		//只作为客户端的时候起作用
		micro.WrapClient(hystrix2.NewClientHystrixWrapper()),
		//添加限流
		micro.WrapHandler(ratelimit.NewHandlerWrapper(1000)),
        //增加负载均衡
		micro.WrapClient(roundrobin.NewClientWrapper()),
	)
 
	service.Init()
 
	// 指定需要访问的服务，可以快速操作已开发的服务，
    // 默认API服务名称带有"Api"，程序会自动替换
    // 如果不带有特定字符会使用默认"XXX" 请自行替换
	routeService:=go_micro_service_route.NewRouteService("go.micro.service.route",service.Client())
   // 注册控制器
	if err := routeApi.RegisterRouteApiHandler(service.Server(), &handler.RouteApi { RouteService:routeService});err !=nil {
		common.Error(err)
	}

	// 启动服务
	if err := service.Run(); err != nil {
        //输出启动失败信息
		common.Fatal(err)
	}
}
