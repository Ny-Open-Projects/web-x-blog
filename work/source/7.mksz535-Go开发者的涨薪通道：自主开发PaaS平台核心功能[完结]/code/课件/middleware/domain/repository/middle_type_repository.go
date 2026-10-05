package repository

import (
	"git.imooc.com/coding-535/middleware/domain/model"
	"github.com/jinzhu/gorm"
)
//创建需要实现的接口
type IMiddleTypeRepository interface{
	//初始化表
	InitTable() error
	//根据ID查处找数据
	FindTypeByID(int64) (*model.MiddleType, error)
	//创建一条 middleware 数据
	CreateMiddleType(*model.MiddleType) (int64, error)
	//根据ID删除一条 middleware 数据
	DeleteMiddleTypeByID(int64) error
	//修改更新数据
	UpdateMiddleType(*model.MiddleType) error
	//查找middleware所有数据
	FindAll()([]model.MiddleType,error)

	FindVersionByID(int64)(*model.MiddleVersion,error)
	FindAllVersionByTypeID(int64)([]model.MiddleVersion,error)

}
//创建MiddleTypeRepository
func NewMiddleTypeRepository(db *gorm.DB) IMiddleTypeRepository  {
	return &MiddleTypeRepository{mysqlDb:db}
}

type MiddleTypeRepository struct {
	mysqlDb *gorm.DB
}

//初始化表
func (u *MiddleTypeRepository)InitTable() error  {
	return u.mysqlDb.CreateTable(&model.MiddleType{},&model.MiddleVersion{}).Error
}

//按照 ID 查找中间件类型
func (u *MiddleTypeRepository) FindTypeByID(middleTypeID int64)(middleType *model.MiddleType,err error)  {
	middleType = & model.MiddleType{}
	return middleType,u.mysqlDb.Preload("MiddleVersion").First(middleType,middleTypeID).Error
}
//创建中间件
func (u *MiddleTypeRepository) CreateMiddleType(middleType *model.MiddleType)(int64,error){
	return middleType.ID,u.mysqlDb.Create(middleType).Error
}
//删除中间件
func (u *MiddleTypeRepository) DeleteMiddleTypeByID(middleTypeID int64) error{
	tx := u.mysqlDb.Begin()
	//遇到问题回滚
	defer func() {
		if r:=recover();r!=nil{
			tx.Rollback()
		}
	}()
	//遇到错误返回
	if tx.Error !=nil{
		return tx.Error
	}
	//删除中间件类型
	if err:= u.mysqlDb.Where("id = ?",middleTypeID).Delete(&model.MiddleType{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//开始删除版本
	if err:= u.mysqlDb.Where("middle_type_id = ?", middleTypeID).Delete(&model.MiddleVersion{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	return tx.Commit().Error
}
//更新middleware 信息
func (u *MiddleTypeRepository) UpdateMiddleType(middleType *model.MiddleType) error {
	return u.mysqlDb.Model(middleType).Update(middleType).Error
}
//获取类型的结果集
func (u *MiddleTypeRepository) FindAll()(middleTypeAll []model.MiddleType,err error)  {
	return middleTypeAll,u.mysqlDb.Find(&middleTypeAll).Error
}

//根据ID查找单个版本
func (u *MiddleTypeRepository) FindVersionByID(middleVersionID int64)(middleVersion *model.MiddleVersion,err error) {
	middleVersion = &model.MiddleVersion{}
	return middleVersion,u.mysqlDb.First(middleVersion,middleVersionID).Error
}
//根据中间件类型查找所有版本
func (u *MiddleTypeRepository) FindAllVersionByTypeID(middleTypeID int64)(middleVersionAll []model.MiddleVersion,err error)  {
	return middleVersionAll,u.mysqlDb.Where("middle_type_id = ?",middleTypeID).Find(&middleVersionAll).Error
}



