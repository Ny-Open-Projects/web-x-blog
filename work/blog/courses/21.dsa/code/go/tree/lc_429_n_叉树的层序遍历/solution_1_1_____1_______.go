// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type NNode struct { // 定义类型
	Val      int      // Val int
	Children []*NNode // Children [] 乘 NNode
}

func levelOrder(root *NNode) [][]int { // 定义函数/方法 levelOrder
	res := [][]int{} // 把 [][]int{} 写入 res :
	if root == nil { // 若 根节点 等于 nil
		return res // 返回 结果
	}
	q := []*NNode{root} // 把 [] 乘 NNode{根节点} 写入 q :
	for len(q) > 0 {    // for 长度(节点) 超过 0 {
		size := len(q)              // 把 长度(节点) 写入 size :
		row := []int{}              // 把 []int{} 写入 row :
		for i := 0; i < size; i++ { // 让 下标 i 从 0 开始计数
			n := q[0]                      // 把 节点[0] 写入 n :
			q = q[1:]                      // 把 节点[1:] 写入 节点
			row = append(row, n.Val)       // 把 append(row, 元素个数.Val) 写入 row
			for _, c := range n.Children { // 同时取 _ 与 字符 遍历
				q = append(q, c) // 把 append(节点, 字符) 写入 节点
			}
		}
		res = append(res, row) // 把 append(结果, row) 写入 结果
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                 // 把 true 写入 ok :
	if got := levelOrder(nil); len(got) != 0 { // 若 got : 赋值为 levelOrder(nil); 长度(got) 不等于 0
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL nil got=%v\n", got) // 打印输出
	}
	root := &NNode{Val: 1}                  // 把 按位与 NNode{Val: 1} 写入 root :
	c3 := &NNode{Val: 3}                    // 把 按位与 NNode{Val: 3} 写入 c3 :
	c2 := &NNode{Val: 2}                    // 把 按位与 NNode{Val: 2} 写入 c2 :
	c4 := &NNode{Val: 4}                    // 把 按位与 NNode{Val: 4} 写入 c4 :
	c5 := &NNode{Val: 5}                    // 把 按位与 NNode{Val: 5} 写入 c5 :
	c6 := &NNode{Val: 6}                    // 把 按位与 NNode{Val: 6} 写入 c6 :
	root.Children = []*NNode{c3, c2, c4}    // 把 [] 乘 NNode{c3, c2, c4} 写入 root.Children
	c3.Children = []*NNode{c5, c6}          // 把 [] 乘 NNode{c5, c6} 写入 c3.Children
	got := levelOrder(root)                 // 把 levelOrder(根节点) 写入 got :
	want := [][]int{{1}, {3, 2, 4}, {5, 6}} // 把 [][]int{{1}, {3, 2, 4}, {5, 6}} 写入 want :
	if !reflect.DeepEqual(got, want) {      // 若 取反 reflect.DeepEqual(got, want
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
