package model

//应用市场
type AppStore struct{
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	//应用的标识
	AppSku string `gorm:"unique_index;not null" json:"app_sku"`
	//应用标题
	AppTitle string `json:"app_title"`
	//应用描述
	AppDetail string `json:"app_detail"`
	//应用价格
	AppPrice float32 `json:"app_price"`
	//安装次数
	AppInstall int64 `json:"app_install"`
	//访问次数
	AppViews int64 `json:"app_views"`
	//应用审核
	AppCheck bool `json:"app_check"`
	//应用分类
	AppCategoryID int64 `json:"app_category_id"`
	//服务商
	AppIsvID int64 `json:"app_isv_id"`
	//应用图片
	AppImage[] AppImage `gorm:"ForeignKey:AppID" json:"app_image"`
	//应用组合,应用的模板
	AppPod[] AppPod `gorm:"ForeignKey:AppID" json:"app_pod"`
	//中间件组合
	AppMiddle[] AppMiddle `gorm:"ForeignKey:AppID" json:"app_middle"`
	//存储组合
	AppVolume[] AppVolume `gorm:"ForeignKey:AppID" json:"app_volume"`
	//评论
	AppComment[] AppComment `gorm:"ForeignKey:AppID" json:"app_comment"`
}

