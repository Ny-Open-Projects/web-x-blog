package form

import (
	"errors"
	"git.imooc.com/coding-535/appStoreApi/proto/appStoreApi"
	"git.imooc.com/coding-535/common"
	"sort"
	"strings"

	"strconv"
	"time"
	"reflect"
)

//判断字符串是否存在
func isIn(target string,strArray []string)bool  {
	sort.Strings(strArray)
	index := sort.SearchStrings(strArray,target)
	if index <len(strArray) && strArray[index] == target{
		return true
	}
	return false
}


func FormToAppStoreStruct(data map[string]*appStoreApi.Pair,obj interface{})  {
	objValue := reflect.ValueOf(obj).Elem()
	for i := 0; i < objValue.NumField(); i++ {
		//获取sql对应的值
		dataTag := strings.Replace(objValue.Type().Field(i).Tag.Get("json"),",omitempty","",-1)
		dataSlice, ok := data[dataTag]
		if !ok {
			continue
		}
		valueSlice := dataSlice.Values
		if len(valueSlice)<=0{
			continue
		}

		//排除列表
		tagList := []string{"app_image","app_pod","app_middle","app_volume","app_comment"}
		//进行排除
		if isIn(dataTag,tagList) {
			continue
		}
		value := valueSlice[0]

		//端口，环境变量的单独处理
		//获取对应字段的名称
		name := objValue.Type().Field(i).Name

		//获取对应字段类型
		structFieldType := objValue.Field(i).Type()
		//获取变量类型，也可以直接写"string类型"
		val := reflect.ValueOf(value)
		var err error
		if structFieldType != val.Type() {
			//类型转换
			val, err = TypeConversion(value, structFieldType.Name()) //类型转换
			if err != nil {
				common.Error(err)
			}
		}
		//设置类型值
		objValue.FieldByName(name).Set(val)
	}
}

//类型转换
func TypeConversion(value string, ntype string) (reflect.Value, error) {
	if ntype == "string" {
		return reflect.ValueOf(value), nil
	} else if ntype == "time.Time" {
		t, err := time.ParseInLocation("2006-01-02 15:04:05", value, time.Local)
		return reflect.ValueOf(t), err
	} else if ntype == "Time" {
		t, err := time.ParseInLocation("2006-01-02 15:04:05", value, time.Local)
		return reflect.ValueOf(t), err
	} else if ntype == "int" {
		i, err := strconv.Atoi(value)
		return reflect.ValueOf(i), err
	} else if ntype == "int32" {
		i, err := strconv.ParseInt(value, 10, 32)
		if err != nil {
			return reflect.ValueOf(int32(i)), err
		}
		return reflect.ValueOf(int32(i)), err
	} else if ntype == "int64" {
		i, err := strconv.ParseInt(value, 10, 64)
		return reflect.ValueOf(i), err
	} else if ntype == "float32" {
		i, err := strconv.ParseFloat(value, 64)
		return reflect.ValueOf(float32(i)), err
	} else if ntype == "float64" {
		i, err := strconv.ParseFloat(value, 64)
		return reflect.ValueOf(i), err
	}

	//else if .......增加其他一些类型的转换

	return reflect.ValueOf(value), errors.New("未知的类型：" + ntype)
}
