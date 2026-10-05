package model

//云应用评论
type AppComment struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	AppCommentTitle string `json:"app_comment_title"`
	AppCommentDetail string `json:"app_comment_detail"`
	AppUserID int64 `json:"app_user_id"`
	//@TODO
}
