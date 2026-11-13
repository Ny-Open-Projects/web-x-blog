// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091772
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func insertIntoBST(root *TreeNode, val int) *TreeNode { // 定义函数/方法 insertIntoBST
	if root == nil { // 若 根节点 等于 nil
		return &TreeNode{Val: val} // 返回 按位与 TreeNode{Val: 值}
	}
	pos := root      // 把 根节点 写入 pos :
	for pos != nil { // 把 nil { 写入 for pos !
		if val < pos.Val { // 若 值 小于 pos.Val
			if pos.Left == nil { // 若 pos.Left 等于 nil
				pos.Left = &TreeNode{Val: val} // 把 按位与 TreeNode{Val: 值} 写入 pos.Left
				break                          // 跳出循环
			} else { // 否则
				pos = pos.Left // 把 pos.Left 写入 pos
			}
		} else { // 否则
			if pos.Right == nil { // 若 pos.Right 等于 nil
				pos.Right = &TreeNode{Val: val} // 把 按位与 TreeNode{Val: 值} 写入 pos.Right
				break                           // 跳出循环
			} else { // 否则
				pos = pos.Right // 把 pos.Right 写入 pos
			}
		}
	}
	return root // 返回 根节点
}

func toList(root *TreeNode) []int { // 定义函数/方法 toList
	res := []int{}             // 把 []int{} 写入 res :
	stack := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 stack :
	for len(stack) > 0 {       // for 长度(栈) 超过 0 {
		node := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 node :
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		if node != nil {             // 若 节点 不等于 nil
			res = append(res, node.Val)       // 把 append(结果, 节点.Val) 写入 结果
			stack = append(stack, node.Right) // 把 append(栈, 节点.Right) 写入 栈
			stack = append(stack, node.Left)  // 把 append(栈, 节点.Left) 写入 栈
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	root1 := &TreeNode{4, &TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}, &TreeNode{7, nil, nil}}
	got1 := toList(insertIntoBST(root1, 5)) // 把 toList(insertIntoBST(root1, 5)) 写入 got1 :
	want1 := []int{4, 2, 1, 3, 7, 5}        // 把 []int{4, 2, 1, 3, 7, 5} 写入 want1 :

	got2 := toList(insertIntoBST(nil, 5)) // 把 toList(insertIntoBST(nil, 5)) 写入 got2 :
	want2 := []int{5}                     // 把 []int{5} 写入 want2 :

	root3 := &TreeNode{40, &TreeNode{20, &TreeNode{10, nil, nil}, &TreeNode{30, nil, nil}}, &TreeNode{70, nil, nil}}
	got3 := toList(insertIntoBST(root3, 35)) // 把 toList(insertIntoBST(root3, 35)) 写入 got3 :
	want3 := []int{40, 20, 10, 30, 35, 70}   // 把 []int{40, 20, 10, 30, 35, 70} 写入 want3 :

	ok := true                           // 把 true 写入 ok :
	if !reflect.DeepEqual(got1, want1) { // 若 取反 reflect.DeepEqual(got1, want1
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL case1", got1) // 打印输出
	}
	if !reflect.DeepEqual(got2, want2) { // 若 取反 reflect.DeepEqual(got2, want2
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL case2", got2) // 打印输出
	}
	if !reflect.DeepEqual(got3, want3) { // 若 取反 reflect.DeepEqual(got3, want3
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL case3", got3) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
