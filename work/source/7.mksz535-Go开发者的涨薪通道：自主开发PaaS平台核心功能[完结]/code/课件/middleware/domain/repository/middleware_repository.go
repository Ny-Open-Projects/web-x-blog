package repository
import (
	"github.com/jinzhu/gorm"
	"git.imooc.com/coding-535/middleware/domain/model"
)
//创建需要实现的接口
type IMiddlewareRepository interface{
    //初始化表
    InitTable() error
    //根据ID查处找数据
    FindMiddlewareByID(int64) (*model.Middleware, error)
    //创建一条 middleware 数据
	CreateMiddleware(*model.Middleware) (int64, error)
    //根据ID删除一条 middleware 数据
	DeleteMiddlewareByID(int64) error
    //修改更新数据
	UpdateMiddleware(*model.Middleware) error
    //查找middleware所有数据
	FindAll()([]model.Middleware,error)

    //根据类型查找所有中间件
    FindAllByTypeID(int64)([]model.Middleware,error)

}
//创建middlewareRepository
func NewMiddlewareRepository(db *gorm.DB) IMiddlewareRepository  {
	return &MiddlewareRepository{mysqlDb:db}
}

type MiddlewareRepository struct {
	mysqlDb *gorm.DB
}

//初始化表
func (u *MiddlewareRepository)InitTable() error  {
	return u.mysqlDb.CreateTable(&model.Middleware{},&model.MiddleConfig{},&model.MiddlePort{},&model.MiddleEnv{},&model.MiddleStorage{}).Error
}

//根据ID查找Middleware信息
func (u *MiddlewareRepository)FindMiddlewareByID(middlewareID int64) (middleware *model.Middleware,err error) {
	middleware = &model.Middleware{}
	//要多个则添加 Preload
	return middleware, u.mysqlDb.First(middleware,middlewareID).Error
}

//创建Middleware信息
func (u *MiddlewareRepository) CreateMiddleware(middleware *model.Middleware) (int64, error) {
	return middleware.ID, u.mysqlDb.Create(middleware).Error
}

//根据ID删除Middleware信息
func (u *MiddlewareRepository) DeleteMiddlewareByID(middlewareID int64) error {
	//开启事物
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
	//删除中间件
	if err:=u.mysqlDb.Where("id = ?",middlewareID).Delete(&model.Middleware{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除中间件的配置
	if err:= u.mysqlDb.Where("middle_id = ?", middlewareID).Delete(&model.MiddleConfig{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除端口
	if err:= u.mysqlDb.Where("middle_id = ?",middlewareID).Delete(&model.MiddlePort{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除中间件环境变量
	if err:=u.mysqlDb.Where("middle_id = ?",middlewareID).Delete(&model.MiddleEnv{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	//删除中间件存储
	if err:=u.mysqlDb.Where("middle_id = ?",middlewareID).Delete(&model.MiddleStorage{}).Error;err!=nil{
		tx.Rollback()
		return err
	}
	return tx.Commit().Error
}

//更新Middleware信息
func (u *MiddlewareRepository) UpdateMiddleware(middleware *model.Middleware) error {
	return u.mysqlDb.Model(middleware).Update(middleware).Error
}

//获取结果集
func (u *MiddlewareRepository) FindAll()(middlewareAll []model.Middleware,err error) {
	//要多个则添加 Preload
	return middlewareAll, u.mysqlDb.Find(&middlewareAll).Error
}

func (u *MiddlewareRepository) FindAllByTypeID(typeID int64) (middlewareAll []model.Middleware, err error) {
	//要多个则添加 Preload
	return middlewareAll,u.mysqlDb.Where("middle_type_id = ?",typeID).Find(&middlewareAll).Error
}

