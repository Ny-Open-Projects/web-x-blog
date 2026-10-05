package repository

import (
	"git.imooc.com/coding-535/appStore/domain/model"
	"git.imooc.com/coding-535/common"
	"github.com/jinzhu/gorm"
)
//创建需要实现的接口
type IAppStoreRepository interface{
    //初始化表
    InitTable() error
    //根据ID查处找数据
    FindAppStoreByID(int64) (*model.AppStore, error)
    //创建一条 appStore 数据
	CreateAppStore(*model.AppStore) (int64, error)
    //根据ID删除一条 appStore 数据
	DeleteAppStoreByID(int64) error
    //修改更新数据
	UpdateAppStore(*model.AppStore) error
    //查找appStore所有数据
	FindAll()([]model.AppStore,error)

    //添加安装数量
    AddInstallNumber(int64)error
    //获取安装数量
    GetInstallNumber(int64)int64
    //添加浏览量
    AddViewNumber(int64)error
    //获取浏览量
    GetViewNumber(int64)int64

}
//创建appStoreRepository
func NewAppStoreRepository(db *gorm.DB) IAppStoreRepository  {
	return &AppStoreRepository{mysqlDb:db}
}

type AppStoreRepository struct {
	mysqlDb *gorm.DB
}

//初始化表
func (u *AppStoreRepository)InitTable() error  {
	return u.mysqlDb.CreateTable(&model.AppStore{},&model.AppComment{},&model.AppVolume{},&model.AppPod{},&model.AppImage{},&model.AppCategory{},&model.AppIsv{},&model.AppMiddle{}).Error
}
//添加安装数量统计
func (u *AppStoreRepository)AddInstallNumber(appID int64)error  {
	return u.mysqlDb.Model(&model.AppStore{}).Where("id = ?",appID).UpdateColumn("app_install",gorm.Expr("app_install + ?",1)).Error
}

//获取安装数量统计
func (u *AppStoreRepository) GetInstallNumber(appID int64)int64 {
	appStore ,err := u.FindAppStoreByID(appID)
	if err != nil {
		common.Error(err)
		return 0
	}
	return appStore.AppInstall
}

//添加浏览统计
func (u *AppStoreRepository) AddViewNumber(appID int64)error {
	return u.mysqlDb.Model(&model.AppStore{}).Where("id =  ?",appID).UpdateColumn("app_views",gorm.Expr("app_views + ?",1)).Error
}
//获取浏览数量
func (u *AppStoreRepository) GetViewNumber(appID int64) int64 {
	appStore,err:=u.FindAppStoreByID(appID)
	if err != nil {
		common.Error(err)
		return 0
	}
	return appStore.AppViews
}

//根据ID查找AppStore信息
func (u *AppStoreRepository)FindAppStoreByID(appStoreID int64) (appStore *model.AppStore,err error) {
	appStore = &model.AppStore{}
	return appStore, u.mysqlDb.Preload("AppImage").Preload("AppPod").Preload("AppMiddle").Preload("AppVolume").Preload("AppComment").First(appStore,appStoreID).Error
}

//创建AppStore信息
func (u *AppStoreRepository) CreateAppStore(appStore *model.AppStore) (int64, error) {
	return appStore.ID, u.mysqlDb.Create(appStore).Error
}

//根据ID删除AppStore信息
func (u *AppStoreRepository) DeleteAppStoreByID(appStoreID int64) error {
	//开启事务
	tx := u.mysqlDb.Begin()
	//遇到问题回滚
	defer func() {
		if r:= recover();r!=nil{
			tx.Rollback()
		}
	}()
	//遇到问题返回
	if tx.Error !=nil{
		return tx.Error
	}

	//删除应用
	if err:= u.mysqlDb.Where("id = ?", appStoreID).Delete(&model.AppStore{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除应用图片
	if err:=u.mysqlDb.Where("app_id = ?",appStoreID).Delete(&model.AppImage{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除中间件
	if err:=u.mysqlDb.Where("app_id = ?",appStoreID).Delete(&model.AppMiddle{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除对应的Pod组合
	if err:=u.mysqlDb.Where("app_id = ?",appStoreID).Delete(&model.AppPod{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除存储
	if err:=u.mysqlDb.Where("app_id = ?",appStoreID).Delete(&model.AppVolume{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除应用评论
	if err:= u.mysqlDb.Where("app_id = ?",appStoreID).Delete(&model.AppComment{}).Error;err!=nil{
		tx.Rollback()
		return err
	}

	return tx.Commit().Error
}

//更新AppStore信息
func (u *AppStoreRepository) UpdateAppStore(appStore *model.AppStore) error {
	return u.mysqlDb.Model(appStore).Update(appStore).Error
}

//获取结果集
func (u *AppStoreRepository) FindAll()(appStoreAll []model.AppStore,err error) {
	return appStoreAll, u.mysqlDb.Find(&appStoreAll).Error
}

