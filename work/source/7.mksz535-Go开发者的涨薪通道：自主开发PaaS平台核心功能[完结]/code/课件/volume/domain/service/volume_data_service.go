package service

import (
	"context"
	"errors"
	"git.imooc.com/coding-535/common"
	"git.imooc.com/coding-535/volume/domain/model"
	"git.imooc.com/coding-535/volume/domain/repository"
	"git.imooc.com/coding-535/volume/proto/volume"
	"k8s.io/api/apps/v1"
	v12 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/api/resource"
	v13 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"strconv"
)

//这里是接口类型
type IVolumeDataService interface {
	AddVolume(*model.Volume) (int64 , error)
	DeleteVolume(int64) error
	UpdateVolume(*model.Volume) error
	FindVolumeByID(int64) (*model.Volume, error)
	FindAllVolume() ([]model.Volume, error)

	CreateVolumeToK8s(*volume.VolumeInfo) error
	DeleteVolumeFromK8s(*model.Volume) error
}


//创建
//注意：返回值 IVolumeDataService 接口类型
func NewVolumeDataService(volumeRepository repository.IVolumeRepository,clientSet *kubernetes.Clientset) IVolumeDataService{
	return &VolumeDataService{ VolumeRepository:volumeRepository, K8sClientSet: clientSet,deployment:&v1.Deployment{}}
}

type VolumeDataService struct {
    //注意：这里是 IVolumeRepository 类型
	VolumeRepository repository.IVolumeRepository
	K8sClientSet  *kubernetes.Clientset
	deployment  *v1.Deployment
}
//从 k8s 删除一个 pvc
func (u *VolumeDataService) DeleteVolumeFromK8s(volume *model.Volume) (err error) {
	//先从K8s 中删除
	if err = u.K8sClientSet.CoreV1().PersistentVolumeClaims(volume.VolumeNamespace).Delete(context.TODO(),volume.VolumeName, v13.DeleteOptions{});err!=nil {
		common.Error(err)
		return err
	} else {
		//从数据表中删除
		if err := u.DeleteVolume(volume.ID);err !=nil {
			common.Error(err)
			return err
		}
		common.Info("删除存储ID"+ strconv.FormatInt(volume.ID,10)+" 成功！")
	}
	return
}

//创建存储到 k8s 中
func (u *VolumeDataService) CreateVolumeToK8s(info *volume.VolumeInfo)(err error) {
	volume := u.setVolume(info)
	if _,err = u.K8sClientSet.CoreV1().PersistentVolumeClaims(info.VolumeNamespace).Get(context.TODO(),info.VolumeName,v13.GetOptions{});err !=nil {
		//如果存储不存在
		if _,err = u.K8sClientSet.CoreV1().PersistentVolumeClaims(info.VolumeNamespace).Create(context.TODO(),volume,v13.CreateOptions{});err !=nil{
			common.Error(err)
			return err
		}
		common.Info("存储创建成功")
		return nil
	}else {
		common.Error("存储空间"+ info.VolumeName +" 已经存在")
		return errors.New("存储空间"+ info.VolumeName +" 已经存在")
	}
}
//设置 pvc 的详情信息
func (u *VolumeDataService) setVolume(info *volume.VolumeInfo) *v12.PersistentVolumeClaim {
	pvc := &v12.PersistentVolumeClaim{}
	//设置接口类型
	pvc.TypeMeta = v13.TypeMeta{
		Kind:       "PersistentVolumeClaim",
		APIVersion: "v1",
	}
	//设置存储基础信息
	pvc.ObjectMeta = v13.ObjectMeta{
		Name:                       info.VolumeName,
		Namespace:                  info.VolumeNamespace,
		Annotations: map[string]string{
			"pv.kubernetes.io/bound-by-controller":"yes",
			"volume.beta.kubernetes.io/storage-provisioner":"rbd.csi.ceph.com",
			"Cap":"cap 老师！",
		},
	}
	//设置存储动态信息
	pvc.Spec = v12.PersistentVolumeClaimSpec{
		AccessModes:      u.getAccessModes(info),
		Resources:        u.getResource(info),
		StorageClassName: &info.VolumeStorageClassName,
		VolumeMode:       u.getVolumeMode(info),
	}
	return pvc

}

//获取存储类型
func (u *VolumeDataService) getVolumeMode(info *volume.VolumeInfo) *v12.PersistentVolumeMode {
	var pvm v12.PersistentVolumeMode
	switch info.VolumePersistentVolumeMode {
	case "Block":
		pvm = v12.PersistentVolumeBlock
	case "Filesystem":
		pvm = v12.PersistentVolumeFilesystem
	default:
		pvm = v12.PersistentVolumeFilesystem
	}
	return &pvm
}

//获取资源配置
func (u *VolumeDataService) getResource (info *volume.VolumeInfo)(source v12.ResourceRequirements)  {
	source.Requests = v12.ResourceList{
		"storage": resource.MustParse(strconv.FormatFloat(float64(info.VolumeRequest),'f',6,64)+"Gi"),
	}
	return
}

//获取访问模式
func (u *VolumeDataService) getAccessModes(info *volume.VolumeInfo)(pvam []v12.PersistentVolumeAccessMode)  {
	var pm v12.PersistentVolumeAccessMode
	switch info.VolumeAccessMode {
	case "ReadWriteOnce":
		pm = v12.ReadWriteOnce
	case "ReadOnlyMany":
		pm = v12.ReadOnlyMany
	case "ReadWriteMany":
		pm = v12.ReadWriteMany
	case "ReadWriteOncePod":
		pm = v12.ReadWriteOncePod
	default:
		pm = v12.ReadWriteOnce
	}
	pvam = append(pvam,pm)
	return pvam
	
}

//插入
func (u *VolumeDataService) AddVolume(volume *model.Volume) (int64 ,error) {
	 return u.VolumeRepository.CreateVolume(volume)
}

//删除
func (u *VolumeDataService) DeleteVolume(volumeID int64) error {
	return u.VolumeRepository.DeleteVolumeByID(volumeID)
}

//更新
func (u *VolumeDataService) UpdateVolume(volume *model.Volume) error {
	return u.VolumeRepository.UpdateVolume(volume)
}

//查找
func (u *VolumeDataService) FindVolumeByID(volumeID int64) (*model.Volume, error) {
	return u.VolumeRepository.FindVolumeByID(volumeID)
}

//查找
func (u *VolumeDataService) FindAllVolume() ([]model.Volume, error) {
	return u.VolumeRepository.FindAll()
}

