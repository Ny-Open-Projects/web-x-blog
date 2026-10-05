package main

import (
	"fmt"
	"git.imooc.com/coding-535/base/handler"
	hystrix2 "git.imooc.com/coding-535/base/plugin/hystrix"
	base "git.imooc.com/coding-535/base/proto/base"
	"git.imooc.com/coding-535/common"
	"github.com/afex/hystrix-go/hystrix"
	"github.com/asim/go-micro/plugins/registry/consul/v3"
	ratelimit "github.com/asim/go-micro/plugins/wrapper/ratelimiter/uber/v3"
	opentracing2 "github.com/asim/go-micro/plugins/wrapper/trace/opentracing/v3"
	"github.com/asim/go-micro/v3"
	log "github.com/asim/go-micro/v3/logger"
	"github.com/asim/go-micro/v3/registry"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"github.com/opentracing/opentracing-go"
	"net"
	"net/http"
)

func main() {
	//1.注册中心
	consul:=consul.NewRegistry(func(options *registry.Options) {
		options.Addrs = []string{
			//如果放到docker-compose 也可以是服务名称
			"localhost:8500",
		}
	})
	//2.配置中心，存放经常变动的变量
	consulConfig,err := common.GetConsulConfig("localhost",8500,"/micro/config")
	if err !=nil {
		common.Error(err)
	}

	//3.使用配置中心连接 mysql
	mysqlInfo := common.GetMysqlFromConsul(consulConfig,"mysql")
	//初始化数据库
	db,err := gorm.Open("mysql",mysqlInfo.User+":"+mysqlInfo.Pwd+"@/"+mysqlInfo.Database+"?charset=utf8&parseTime=True&loc=Local")
	if err !=nil {
		common.Fatal(err)
	}
	fmt.Println("连接mysql 成功")
	common.Info("连接mysql 成功")
	defer db.Close()
	//禁止复表
	db.SingularTable(true)

	//4.添加链路追踪
	t,io,err := common.NewTracer("base","localhost:6831")
	if err !=nil {
		common.Error(err)
	}
	defer io.Close()
	opentracing.SetGlobalTracer(t)

	//5.添加熔断器
	hystrixStreamHandler := hystrix.NewStreamHandler()
	hystrixStreamHandler.Start()

	//6.添加日志中心
	//1）需要程序日志打入到日志文件中
	//2）在程序中添加filebeat.yml 文件
	//3) 启动filebeat，启动命令 ./filebeat -e -c filebeat.yml
	common.Info("添加 日志系统 ！")

	//启动监听程序
	go func() {
		//http://192.168.0.112:9092/turbine/turbine.stream
		//看板访问地址 http://127.0.0.1:9002/hystrix，url后面一定要带 /hystrix
		err = http.ListenAndServe(net.JoinHostPort("0.0.0.0","9092"),hystrixStreamHandler)
		fmt.Println("333")
		if err !=nil {
			fmt.Println(err)
		}
	}()

	//7.添加监控
	common.PrometheusBoot(9192)

	// 创建服务
	service := micro.NewService(
		micro.Name("base-cap"),
		micro.Version("latest"),
		//添加注册中心
		micro.Registry(consul),
		//添加链路追踪
		micro.WrapHandler(opentracing2.NewHandlerWrapper(opentracing.GlobalTracer())),
		micro.WrapClient(opentracing2.NewClientWrapper(opentracing.GlobalTracer())),
		//只作为客户端的时候起作用
		micro.WrapClient(hystrix2.NewClientHystrixWrapper()),
		//添加限流
		micro.WrapHandler(ratelimit.NewHandlerWrapper(1000)),
	)

	// 初始化服务
	service.Init()

	// 注册句柄，可以快速操作已开发的服务
	base.RegisterBaseHandler(service.Server(), new(handler.Base))

	// 启动服务
	if err := service.Run(); err != nil {
        //输出启动失败信息
		log.Fatal(err)
	}
}
