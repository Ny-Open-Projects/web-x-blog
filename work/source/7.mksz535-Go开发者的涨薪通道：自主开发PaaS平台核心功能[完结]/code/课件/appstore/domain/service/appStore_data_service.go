package service

import (
	"git.imooc.com/coding-535/appStore/domain/model"
	"git.imooc.com/coding-535/appStore/domain/repository"
	"k8s.io/client-go/kubernetes"
)

//这里是接口类型
type IAppStoreDataService interface {
	AddAppStore(*model.AppStore) (int64 , error)
	DeleteAppStore(int64) error
	UpdateAppStore(*model.AppStore) error
	FindAppStoreByID(int64) (*model.AppStore, error)
	FindAllAppStore() ([]model.AppStore, error)

	//统计服务
	AddInstallNum(int64)error
	GetInstallNum(int64)int64
	AddViewNum(int64)error
	GetViewNum(int64)int64
}


//创建
//注意：返回值 IAppStoreDataService 接口类型
func NewAppStoreDataService(appStoreRepository repository.IAppStoreRepository,clientSet *kubernetes.Clientset) IAppStoreDataService{
	return &AppStoreDataService{ AppStoreRepository:appStoreRepository}
}

type AppStoreDataService struct {
    //注意：这里是 IAppStoreRepository 类型
	AppStoreRepository repository.IAppStoreRepository
}

//安装数量统计
func (u *AppStoreDataService) AddInstallNum(appID int64) error {
	return u.AppStoreRepository.AddInstallNumber(appID)
}

//查询安装数量
func (u *AppStoreDataService) GetInstallNum(appID int64) int64 {
	return u.AppStoreRepository.GetInstallNumber(appID)
}
//添加浏览统计
func (u *AppStoreDataService) AddViewNum(appID int64) error {
	return u.AppStoreRepository.AddViewNumber(appID)
}
//获取浏览量
func (u *AppStoreDataService) GetViewNum(appID int64) int64 {
	return u.AppStoreRepository.GetViewNumber(appID)
}

//插入
func (u *AppStoreDataService) AddAppStore(appStore *model.AppStore) (int64 ,error) {
	 return u.AppStoreRepository.CreateAppStore(appStore)
}

//删除
func (u *AppStoreDataService) DeleteAppStore(appStoreID int64) error {
	return u.AppStoreRepository.DeleteAppStoreByID(appStoreID)
}

//更新
func (u *AppStoreDataService) UpdateAppStore(appStore *model.AppStore) error {
	return u.AppStoreRepository.UpdateAppStore(appStore)
}

//查找
func (u *AppStoreDataService) FindAppStoreByID(appStoreID int64) (*model.AppStore, error) {
	return u.AppStoreRepository.FindAppStoreByID(appStoreID)
}

//查找
func (u *AppStoreDataService) FindAllAppStore() ([]model.AppStore, error) {
	return u.AppStoreRepository.FindAll()
}

