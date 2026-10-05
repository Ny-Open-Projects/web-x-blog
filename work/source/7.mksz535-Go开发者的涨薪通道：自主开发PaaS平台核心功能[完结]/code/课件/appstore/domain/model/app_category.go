package model

type AppCategory struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	CategoryName string `json:"category_name"`
	//@TODO
}
