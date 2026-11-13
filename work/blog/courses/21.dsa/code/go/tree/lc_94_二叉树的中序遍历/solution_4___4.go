// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
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

func inorderTraversal(root *TreeNode) []int { // 定义函数/方法 inorderTraversal
	res := []int{}                     // 把 []int{} 写入 res :
	stack := []*TreeNode{}             // 把 [] 乘 TreeNode{} 写入 stack :
	cur := root                        // 把 根节点 写入 cur :
	for cur != nil || len(stack) > 0 { // 把 nil 或 长度(栈) 超过 0 { 写入 for cur !
		if cur != nil { // 若 当前值 不等于 nil
			stack = append(stack, cur) // 把 append(栈, 当前值) 写入 栈
			cur = cur.Left             // 把 当前值.Left 写入 当前值
		} else { // 否则
			cur = stack[len(stack)-1]    // 把 栈[长度(栈) 减 1] 写入 当前值
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			res = append(res, cur.Val)   // 把 append(结果, 当前值.Val) 写入 结果
			cur = cur.Right              // 把 当前值.Right 写入 当前值
		}
	}
	return res // 返回 结果
}

func buildTree(vals []int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == -1 { // 若 长度(vals) 等于 0 或 vals[0] 等于 减 1
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0]} // 把 按位与 TreeNode{Val: vals[0]} 写入 root :
	q := []*TreeNode{root}          // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                          // 把 1 写入 i :
	for i < len(vals) {             // for 下标 i 小于 长度(vals) {
		node := q[0]                        // 把 节点[0] 写入 node :
		q = q[1:]                           // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Left = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Left
			q = append(q, node.Left)            // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                 // 下标 i 加一
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Right = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Right
			q = append(q, node.Right)            // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                       // 把 true 写入 ok :
	if got := inorderTraversal(nil); len(got) != 0 { // 若 got : 赋值为 inorderTraversal(nil); 长度(got) 不等于 0
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL nil got=%v\n", got) // 打印输出
	}
	root := buildTree([]int{1, -1, 2, -1, 3}) // 把 buildTree([]int{1, 减 1, 2, 减 1, 3}) 写入 root :
	got := inorderTraversal(root)             // 把 inorderTraversal(根节点) 写入 got :
	want := []int{1, 2, 3}                    // 把 []int{1, 2, 3} 写入 want :
	if !reflect.DeepEqual(got, want) {        // 若 取反 reflect.DeepEqual(got, want
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
