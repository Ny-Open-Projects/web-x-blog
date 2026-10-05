package service

import (
	"context"
	"errors"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/route/domain/model"
	"git.imooc.com/coding-535/route/domain/repository"
	"git.imooc.com/coding-535/route/proto/route"
	"k8s.io/api/apps/v1"
	v12 "k8s.io/api/networking/v1"
	v14 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"strconv"
)

//这里是接口类型
type IRouteDataService interface {
	AddRoute(*model.Route) (int64 , error)
	DeleteRoute(int64) error
	UpdateRoute(*model.Route) error
	FindRouteByID(int64) (*model.Route, error)
	FindAllRoute() ([]model.Route, error)

	CreateRouteToK8s(*route.RouteInfo) error
	DeleteRouteFromK8s(*model.Route) error
	UpdateRouteToK8s(*route.RouteInfo) error
}


//创建
//注意：返回值 IRouteDataService 接口类型
func NewRouteDataService(routeRepository repository.IRouteRepository,clientSet *kubernetes.Clientset) IRouteDataService{
	return &RouteDataService{ RouteRepository:routeRepository, K8sClientSet: clientSet,deployment:&v1.Deployment{}}
}

type RouteDataService struct {
    //注意：这里是 IRouteRepository 类型
	RouteRepository repository.IRouteRepository
	K8sClientSet  *kubernetes.Clientset
	deployment  *v1.Deployment
}

//创建k8s（把proto 属性补全）
func (u *RouteDataService) CreateRouteToK8s(info *route.RouteInfo) (err error) {
	ingress:=u.setIngress(info)
	//查找是否存在
	if _,err=u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Get(context.TODO(),info.RouteName,v14.GetOptions{});err!=nil{
		if _,err=u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Create(context.TODO(),ingress,v14.CreateOptions{});err!=nil{
			//创建不成功记录错误
			common.Error(err)
			return err
		}
		return nil
	} else {
		common.Error("路由 "+ info.RouteName +" 已经存在")
		return errors.New("路由 "+ info.RouteName +" 已经存在")
	}
}

func (u *RouteDataService) setIngress(info *route.RouteInfo) *v12.Ingress  {
	route:=&v12.Ingress{}
	//设置路由
	route.TypeMeta = v14.TypeMeta{
		Kind:       "Ingress",
		APIVersion: "v1",
	}
	//设置路由基础信息
	route.ObjectMeta = v14.ObjectMeta{
		Name:                       info.RouteName,
		Namespace:                  info.RouteNamespace,
		Labels: map[string]string{
			"app-name":info.RouteName,
			"author":"Caplost",
		},
		Annotations: map[string]string{
			"k8s/generated-by-cap":"由Cap老师代码创建",
		},
	}
	//使用 ingress-nginx
	className := "nginx"
	//设置路由 spec 信息
	route.Spec = v12.IngressSpec{
		IngressClassName: &className,
		//默认访问服务
		DefaultBackend:   nil,
		//如果开启https这里要设置
		TLS:              nil,
		Rules:            u.getIngressPath(info),
	}
	return route
}

//根据info信息获取path路径
func (u *RouteDataService) getIngressPath(info *route.RouteInfo)(path []v12.IngressRule) {
	//1.设置host
	pathRule := v12.IngressRule{Host:info.RouteHost}
	//2.设置Path
	ingressPath := []v12.HTTPIngressPath{}
	for _,v := range info.RoutePath{
		pathType := v12.PathTypePrefix
		ingressPath = append(ingressPath,v12.HTTPIngressPath{
			Path:     v.RoutePathName,
			PathType: &pathType,
			Backend:  v12.IngressBackend{
				Service:  &v12.IngressServiceBackend{
					Name: v.RouteBackendService,
					Port: v12.ServiceBackendPort{
						Number: v.RouteBackendServicePort,
					},
				},
			},
		})
	}

	//3.赋值 Path
	pathRule.IngressRuleValue=v12.IngressRuleValue{HTTP:&v12.HTTPIngressRuleValue{Paths:ingressPath}}
	path = append(path,pathRule)
	return
}

//更新route
func (u *RouteDataService) UpdateRouteToK8s(info *route.RouteInfo)(err error)  {
	ingress := u.setIngress(info)
	if _,err = u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Update(context.TODO(),ingress,v14.UpdateOptions{});err!=nil{
		common.Error(err)
		return err
	}
	return nil
}

//删除route
func (u *RouteDataService) DeleteRouteFromK8s(route2 *model.Route)(err error) {
	//删除Ingress
	if err=u.K8sClientSet.NetworkingV1().Ingresses(route2.RouteNamespace).Delete(context.TODO(),route2.RouteName,v14.DeleteOptions{});err!=nil{
		//如果删除失败记录下
		common.Error(err)
		return err
	} else {
		if err:= u.DeleteRoute(route2.ID);err!=nil{
			common.Error(err)
			return err
		}
		common.Info("删除 ingress ID："+ strconv.FormatInt(route2.ID, 10) + " 成功！" )
	}
	return
}

//插入
func (u *RouteDataService) AddRoute(route *model.Route) (int64 ,error) {
	 return u.RouteRepository.CreateRoute(route)
}

//删除
func (u *RouteDataService) DeleteRoute(routeID int64) error {
	return u.RouteRepository.DeleteRouteByID(routeID)
}

//更新
func (u *RouteDataService) UpdateRoute(route *model.Route) error {
	return u.RouteRepository.UpdateRoute(route)
}

//查找
func (u *RouteDataService) FindRouteByID(routeID int64) (*model.Route, error) {
	return u.RouteRepository.FindRouteByID(routeID)
}

//查找
func (u *RouteDataService) FindAllRoute() ([]model.Route, error) {
	return u.RouteRepository.FindAll()
}

