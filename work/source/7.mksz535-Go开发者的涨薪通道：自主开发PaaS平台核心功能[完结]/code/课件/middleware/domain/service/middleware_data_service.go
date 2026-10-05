package service

import (
	"context"
	"errors"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/middleware/domain/model"
	"git.imooc.com/coding-535/middleware/domain/repository"
	"git.imooc.com/coding-535/middleware/proto/middleware"
	"k8s.io/api/apps/v1"
	v13 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/api/resource"
	v12 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"strconv"
)

//这里是接口类型
type IMiddlewareDataService interface {
	AddMiddleware(*model.Middleware) (int64, error)
	DeleteMiddleware(int64) error
	UpdateMiddleware(*model.Middleware) error
	FindMiddlewareByID(int64) (*model.Middleware, error)
	FindAllMiddleware() ([]model.Middleware, error)
	//根据类型查找中间件
	FindAllMiddlewareByTypeID(int64) ([]model.Middleware, error)
	//操作中间件s
	CreateToK8s(*middleware.MiddlewareInfo) error
	DeleteFromK8s(*model.Middleware) error
	UpdateToK8s(*middleware.MiddlewareInfo) error
}

//创建
//注意：返回值 IMiddlewareDataService 接口类型
func NewMiddlewareDataService(middlewareRepository repository.IMiddlewareRepository, clientSet *kubernetes.Clientset) IMiddlewareDataService {
	return &MiddlewareDataService{MiddlewareRepository: middlewareRepository, K8sClientSet: clientSet}
}

type MiddlewareDataService struct {
	//注意：这里是 IMiddlewareRepository 类型
	MiddlewareRepository repository.IMiddlewareRepository
	K8sClientSet         *kubernetes.Clientset
}
//更新中间件到k8s
func (u *MiddlewareDataService) UpdateToK8s(info *middleware.MiddlewareInfo) error {
	statefulSet := u.setStatefulSet(info)
	if _,err := u.K8sClientSet.AppsV1().StatefulSets(info.MiddleNamespace).Get(context.TODO(),info.MiddleName,v12.GetOptions{});err !=nil {
		common.Error(err)
		return errors.New("中间件 "+ info.MiddleName + " 不存在请先创建")
	}else {
		if _,err = u.K8sClientSet.AppsV1().StatefulSets(info.MiddleNamespace).Update(context.TODO(),statefulSet,v12.UpdateOptions{});err!=nil{
			common.Error(err)
			return err
		}
		common.Info("中间件 "+ info.MiddleName + " 更新成功！")
		return nil
	}

}

//删除中间件
func (u *MiddlewareDataService) DeleteFromK8s(middleware *model.Middleware)(err error) {
	if err:= u.K8sClientSet.AppsV1().StatefulSets(middleware.MiddleNamespace).Delete(context.TODO(),middleware.MiddleName,v12.DeleteOptions{});err!=nil{
		common.Error(err)
		return err
	} else {
		if err:= u.DeleteMiddleware(middleware.ID);err!=nil{
			common.Error(err)
			return err
		}
		common.Info("删除中间件："+middleware.MiddleName+"成功！")
		return nil

	}

}

//在k8s中创建中间件
func (u *MiddlewareDataService) CreateToK8s(info *middleware.MiddlewareInfo) error {
	statefulSet := u.setStatefulSet(info)
	if _,err := u.K8sClientSet.AppsV1().StatefulSets(info.MiddleNamespace).Get(context.TODO(),info.MiddleName,v12.GetOptions{});err!=nil{
		//如果没有获取到
		if _,err = u.K8sClientSet.AppsV1().StatefulSets(info.MiddleNamespace).Create(context.TODO(),statefulSet,v12.CreateOptions{});err!=nil{
			common.Error(err)
			return err
		}
		common.Info("中间件："+info.MiddleName+"创建成功")
		return nil
	} else {
		common.Error("中间件："+info.MiddleName+"创建失败")
		return errors.New("中间件："+info.MiddleName+"创建失败")
	}
}

//根据info信息设置值
func (u *MiddlewareDataService) setStatefulSet(info *middleware.MiddlewareInfo) *v1.StatefulSet {
	statefulSet := &v1.StatefulSet{}
	statefulSet.TypeMeta = v12.TypeMeta{
		Kind:       "StatefulSet",
		APIVersion: "v1",
	}
	//设置详情
	statefulSet.ObjectMeta = v12.ObjectMeta{
		Name:      info.MiddleName,
		Namespace: info.MiddleNamespace,
		//设置label标签
		Labels: map[string]string{
			"app-name": info.MiddleName,
			"author":   "Caplost",
		},
	}
	statefulSet.Name = info.MiddleName
	statefulSet.Spec = v1.StatefulSetSpec{
		//副本数
		Replicas: &info.MiddleReplicas,
		Selector: &v12.LabelSelector{
			MatchLabels: map[string]string{
				"app-name": info.MiddleName,
			},
		},
		//设置容器模版
		Template: v13.PodTemplateSpec{
			ObjectMeta: v12.ObjectMeta{
				Labels: map[string]string{
					"app-name": info.MiddleName,
				},
			},
			//设置容器详情
			Spec: v13.PodSpec{
				Containers: []v13.Container{
					{
						Name:  info.MiddleName,
						Image: info.MiddleDockerImageVersion,
						//获取容器的端口
						Ports: u.getContainerPort(info),
						//获取环境变量
						Env: u.getEnv(info),
						//获取容器CPU，内存
						Resources: u.getResources(info),
						//设置挂载目录
						VolumeMounts: u.setMounts(info),
					},
				},
				//不能设置为0，这样不安全
				//https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/
				TerminationGracePeriodSeconds:u.getTime("10"),
				//私有仓库设置密钥
				ImagePullSecrets: nil,
			},
		},
		VolumeClaimTemplates: u.getPVC(info),
		ServiceName:          info.MiddleName,
	}
	return statefulSet

}

func (u *MiddlewareDataService) getTime(stringTime string) *int64 {
	b,err := strconv.ParseInt(stringTime,10,64)
	if err != nil {
		common.Error(err)
		return nil
	}
	return &b
}

//设置存储路径
func (u *MiddlewareDataService) setMounts(info *middleware.MiddlewareInfo)(mount []v13.VolumeMount) {
	if len(info.MiddleStorage) == 0 {
		return
	}
	for _,v := range info.MiddleStorage{
		mt := &v13.VolumeMount{
			Name:             v.MiddleStorageName,
			MountPath:        v.MiddleStoragePath,
		}
		mount = append(mount ,*mt)
	}
	return
}
//获取pvc
func (u *MiddlewareDataService) getPVC(info *middleware.MiddlewareInfo)(pvcAll []v13.PersistentVolumeClaim) {
	if len(info.MiddleStorage) ==0 {
		return
	}
	for _,v:= range info.MiddleStorage {
		pvc := &v13.PersistentVolumeClaim{
			TypeMeta:   v12.TypeMeta{
				Kind:       "PersistentVolumeClaim",
				APIVersion: "v1",
			},
			ObjectMeta: v12.ObjectMeta{
				Name:                       v.MiddleStorageName,
				Namespace:                  info.MiddleNamespace,
				Annotations: map[string]string{
					"pv.kubernetes.io/bound-by-controller":"yes",
					"volume.beta.kubernetes.io/storage-provisioner":"rbd.csi.ceph.com",
					"Cap":"cap 老师课程创建！",

				},
			},
			Spec:       v13.PersistentVolumeClaimSpec{
				AccessModes:      u.getAccessModes(v.MiddleStorageAccessMode),
				Resources:        u.getPvcResource(v.MiddleStorageSize),
				VolumeName:       v.MiddleStorageName,
				StorageClassName: &v.MiddleStorageClass,
			},
		}
		pvcAll = append(pvcAll,*pvc)
	}
	return
}

//获取大小
func (u *MiddlewareDataService) getPvcResource(size float32) (source v13.ResourceRequirements) {
	source.Requests = v13.ResourceList{
		"storage" : resource.MustParse(strconv.FormatFloat(float64(size),'f',6,64)+"Gi" ),
	}
	return
}

//获取权限的
func (u *MiddlewareDataService) getAccessModes(accessMode string)(pvam []v13.PersistentVolumeAccessMode) {
	var pm v13.PersistentVolumeAccessMode
	switch accessMode {
	case "ReadWriteOnce":
		pm = v13.ReadWriteOnce
	case "ReadOnlyMany":
		pm = v13.ReadOnlyMany
	case "ReadWriteMany":
		pm = v13.ReadWriteMany
	case "ReadWriteOncePod":
		pm = v13.ReadWriteOncePod
	default:
		pm = v13.ReadWriteOnce
	}
	pvam = append(pvam,pm)
	return pvam
}

//获取容器的端口
func (u *MiddlewareDataService) getContainerPort(info *middleware.MiddlewareInfo) (containerPort []v13.ContainerPort) {
	for _, v := range info.MiddlePort {
		containerPort = append(containerPort, v13.ContainerPort{
			Name:          "middle-port-" + strconv.FormatInt(int64(v.MiddlePort), 10),
			ContainerPort: v.MiddlePort,
			Protocol:      u.getProtocol(v.MiddleProtocol),
		})
	}
	return
}

//获取protocol 协议
func (u *MiddlewareDataService) getProtocol(protocol string) v13.Protocol {
	switch protocol {
	case "TCP":
		return "TCP"
	case "UDP":
		return "UDP"
	case "SCTP":
		return "SCTP"
	default:
		return "TCP"
	}

}

//获取中间件的环境变量
func (u *MiddlewareDataService) getEnv(info *middleware.MiddlewareInfo) (envVar []v13.EnvVar) {
	for _, v := range info.MiddleEnv {
		envVar = append(envVar, v13.EnvVar{
			Name:      v.EnvKey,
			Value:     v.EnvValue,
			ValueFrom: nil,
		})
	}
	return
}

//获取中间件需要的资源
func (u *MiddlewareDataService) getResources(info *middleware.MiddlewareInfo) (source v13.ResourceRequirements) {
	//最大能够使用的资源
	source.Limits = v13.ResourceList{
		"cpu":    resource.MustParse(strconv.FormatFloat(float64(info.MiddleCpu), 'f', 6, 64)),
		"memory": resource.MustParse(strconv.FormatFloat(float64(info.MiddleMemory), 'f', 6, 64)),
	}
	//最小请求资源
	source.Requests = v13.ResourceList{
		"cpu":    resource.MustParse(strconv.FormatFloat(float64(info.MiddleCpu), 'f', 6, 64)),
		"memory": resource.MustParse(strconv.FormatFloat(float64(info.MiddleMemory), 'f', 6, 64)),
	}
	return
}

//插入
func (u *MiddlewareDataService) AddMiddleware(middleware *model.Middleware) (int64, error) {
	return u.MiddlewareRepository.CreateMiddleware(middleware)
}

//删除
func (u *MiddlewareDataService) DeleteMiddleware(middlewareID int64) error {
	return u.MiddlewareRepository.DeleteMiddlewareByID(middlewareID)
}

//更新
func (u *MiddlewareDataService) UpdateMiddleware(middleware *model.Middleware) error {
	return u.MiddlewareRepository.UpdateMiddleware(middleware)
}

//查找
func (u *MiddlewareDataService) FindMiddlewareByID(middlewareID int64) (*model.Middleware, error) {
	return u.MiddlewareRepository.FindMiddlewareByID(middlewareID)
}

//查找
func (u *MiddlewareDataService) FindAllMiddleware() ([]model.Middleware, error) {
	return u.MiddlewareRepository.FindAll()
}

//根据类型查找所有的中间件
func (u *MiddlewareDataService) FindAllMiddlewareByTypeID(typeID int64)([]model.Middleware,error) {
	return u.MiddlewareRepository.FindAllByTypeID(typeID)
}
