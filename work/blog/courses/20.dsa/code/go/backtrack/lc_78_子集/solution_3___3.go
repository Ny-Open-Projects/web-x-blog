// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134701204
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func subsets(nums []int) [][]int { // 定义函数/方法 subsets
	res := [][]int{{}}         // 把 [][]int{{}} 写入 res :
	for _, num := range nums { // 同时取 _ 与 num 遍历
		cur := len(res)            // 把 长度(结果) 写入 cur :
		for i := 0; i < cur; i++ { // 让 下标 i 从 0 开始计数
			res = append(res, append(append([]int{}, res[i]...), num))
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int   // in []int
		want [][]int // want [][]int
	}{ // }{
		{[]int{1, 2, 3}, [][]int{{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := subsets(c.in); !reflect.DeepEqual(g, c.want) { // 若 g : 赋值为 subsets(字符.in); 取反 reflect.DeepEqual(g, 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
