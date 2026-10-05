package repository
import (
	"github.com/jinzhu/gorm"
	"git.imooc.com/coding-535/volume/domain/model"
)
//创建需要实现的接口
type IVolumeRepository interface{
    //初始化表
    InitTable() error
    //根据ID查处找数据
    FindVolumeByID(int64) (*model.Volume, error)
    //创建一条 volume 数据
	CreateVolume(*model.Volume) (int64, error)
    //根据ID删除一条 volume 数据
	DeleteVolumeByID(int64) error
    //修改更新数据
	UpdateVolume(*model.Volume) error
    //查找volume所有数据
	FindAll()([]model.Volume,error)

}
//创建volumeRepository
func NewVolumeRepository(db *gorm.DB) IVolumeRepository  {
	return &VolumeRepository{mysqlDb:db}
}

type VolumeRepository struct {
	mysqlDb *gorm.DB
}

//初始化表
func (u *VolumeRepository)InitTable() error  {
	return u.mysqlDb.CreateTable(&model.Volume{}).Error
}

//根据ID查找Volume信息
func (u *VolumeRepository)FindVolumeByID(volumeID int64) (volume *model.Volume,err error) {
	volume = &model.Volume{}
	return volume, u.mysqlDb.First(volume,volumeID).Error
}

//创建Volume信息
func (u *VolumeRepository) CreateVolume(volume *model.Volume) (int64, error) {
	return volume.ID, u.mysqlDb.Create(volume).Error
}

//根据ID删除Volume信息
func (u *VolumeRepository) DeleteVolumeByID(volumeID int64) error {
	return u.mysqlDb.Where("id = ?",volumeID).Delete(&model.Volume{}).Error
}

//更新Volume信息
func (u *VolumeRepository) UpdateVolume(volume *model.Volume) error {
	return u.mysqlDb.Model(volume).Update(volume).Error
}

//获取结果集
func (u *VolumeRepository) FindAll()(volumeAll []model.Volume,err error) {
	return volumeAll, u.mysqlDb.Find(&volumeAll).Error
}

