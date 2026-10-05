package template

var (
	DomainModel=`package model

type {{title .Alias}} struct{
	ID int64 `+"`gorm:\"primary_key;not_null;auto_increment\"`"+`
}

`
)

var (
	DomainRepository=`package repository
import (
	"github.com/jinzhu/gorm"
	"{{.Dir}}/domain/model"
)
//创建需要实现的接口
type I{{title .Alias}}Repository interface{
    //初始化表
    InitTable() error
    //根据ID查处找数据
    Find{{title .Alias}}ByID(int64) (*model.{{title .Alias}}, error)
    //创建一条 {{.Alias}} 数据
	Create{{title .Alias}}(*model.{{title .Alias}}) (int64, error)
    //根据ID删除一条 {{.Alias}} 数据
	Delete{{title .Alias}}ByID(int64) error
    //修改更新数据
	Update{{title .Alias}}(*model.{{title .Alias}}) error
    //查找{{.Alias}}所有数据
	FindAll()([]model.{{title .Alias}},error)

}
//创建{{.Alias}}Repository
func New{{title .Alias}}Repository(db *gorm.DB) I{{title .Alias}}Repository  {
	return &{{title .Alias}}Repository{mysqlDb:db}
}

type {{title .Alias}}Repository struct {
	mysqlDb *gorm.DB
}

//初始化表
func (u *{{title .Alias}}Repository)InitTable() error  {
	return u.mysqlDb.CreateTable(&model.{{title .Alias}}{}).Error
}

//根据ID查找{{title .Alias}}信息
func (u *{{title .Alias}}Repository)Find{{title .Alias}}ByID({{.Alias}}ID int64) ({{.Alias}} *model.{{title .Alias}},err error) {
	{{.Alias}} = &model.{{title .Alias}}{}
	return {{.Alias}}, u.mysqlDb.First({{.Alias}},{{.Alias}}ID).Error
}

//创建{{title .Alias}}信息
func (u *{{title .Alias}}Repository) Create{{title .Alias}}({{.Alias}} *model.{{title .Alias}}) (int64, error) {
	return {{.Alias}}.ID, u.mysqlDb.Create({{.Alias}}).Error
}

//根据ID删除{{title .Alias}}信息
func (u *{{title .Alias}}Repository) Delete{{title .Alias}}ByID({{.Alias}}ID int64) error {
	return u.mysqlDb.Where("id = ?",{{.Alias}}ID).Delete(&model.{{title .Alias}}{}).Error
}

//更新{{title .Alias}}信息
func (u *{{title .Alias}}Repository) Update{{title .Alias}}({{.Alias}} *model.{{title .Alias}}) error {
	return u.mysqlDb.Model({{.Alias}}).Update({{.Alias}}).Error
}

//获取结果集
func (u *{{title .Alias}}Repository) FindAll()({{.Alias}}All []model.{{title .Alias}},err error) {
	return {{.Alias}}All, u.mysqlDb.Find(&{{.Alias}}All).Error
}

`


	DomainService = `package service

import (
	"{{.Dir}}/domain/model"
	"{{.Dir}}/domain/repository"
	"k8s.io/api/apps/v1"
	"k8s.io/client-go/kubernetes"
)

//这里是接口类型
type I{{title .Alias}}DataService interface {
	Add{{title .Alias}}(*model.{{title .Alias}}) (int64 , error)
	Delete{{title .Alias}}(int64) error
	Update{{title .Alias}}(*model.{{title .Alias}}) error
	Find{{title .Alias}}ByID(int64) (*model.{{title .Alias}}, error)
	FindAll{{title .Alias}}() ([]model.{{title .Alias}}, error)
}


//创建
//注意：返回值 I{{title .Alias}}DataService 接口类型
func New{{title .Alias}}DataService({{.Alias}}Repository repository.I{{title .Alias}}Repository,clientSet *kubernetes.Clientset) I{{title .Alias}}DataService{
	return &{{title .Alias}}DataService{ {{title .Alias}}Repository:{{.Alias}}Repository, K8sClientSet: clientSet,deployment:&v1.Deployment{}}
}

type {{title .Alias}}DataService struct {
    //注意：这里是 I{{title .Alias}}Repository 类型
	{{title .Alias}}Repository repository.I{{title .Alias}}Repository
	K8sClientSet  *kubernetes.Clientset
	deployment  *v1.Deployment
}


//插入
func (u *{{title .Alias}}DataService) Add{{title .Alias}}({{.Alias}} *model.{{title .Alias}}) (int64 ,error) {
	 return u.{{title .Alias}}Repository.Create{{title .Alias}}({{.Alias}})
}

//删除
func (u *{{title .Alias}}DataService) Delete{{title .Alias}}({{.Alias}}ID int64) error {
	return u.{{title .Alias}}Repository.Delete{{title .Alias}}ByID({{.Alias}}ID)
}

//更新
func (u *{{title .Alias}}DataService) Update{{title .Alias}}({{.Alias}} *model.{{title .Alias}}) error {
	return u.{{title .Alias}}Repository.Update{{title .Alias}}({{.Alias}})
}

//查找
func (u *{{title .Alias}}DataService) Find{{title .Alias}}ByID({{.Alias}}ID int64) (*model.{{title .Alias}}, error) {
	return u.{{title .Alias}}Repository.Find{{title .Alias}}ByID({{.Alias}}ID)
}

//查找
func (u *{{title .Alias}}DataService) FindAll{{title .Alias}}() ([]model.{{title .Alias}}, error) {
	return u.{{title .Alias}}Repository.FindAll()
}

`

//	Common=`
////这里添加公共方法
//`
)