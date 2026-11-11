// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145090998
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

func mergeTrees(t1, t2 *TreeNode) *TreeNode { // 定义函数/方法 mergeTrees
	if t1 == nil { // 若 t1 等于 nil
		return t2 // 返回 t2
	}
	if t2 == nil { // 若 t2 等于 nil
		return t1 // 返回 t1
	}
	root := &TreeNode{Val: t1.Val + t2.Val}     // 把 按位与 TreeNode{Val: t1.Val 加 t2.Val} 写入 root :
	root.Left = mergeTrees(t1.Left, t2.Left)    // 把 mergeTrees(t1.Left, t2.Left) 写入 root.Left
	root.Right = mergeTrees(t1.Right, t2.Right) // 把 mergeTrees(t1.Right, t2.Right) 写入 root.Right
	return root                                 // 返回 根节点
}

func toList(root *TreeNode) []int { // 定义函数/方法 toList
	res := []int{}   // 把 []int{} 写入 res :
	if root == nil { // 若 根节点 等于 nil
		return res // 返回 结果
	}
	q := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 q :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		n := q[0]     // 把 节点[0] 写入 n :
		q = q[1:]     // 把 节点[1:] 写入 节点
		if n != nil { // 若 元素个数 不等于 nil
			res = append(res, n.Val)       // 把 append(结果, 元素个数.Val) 写入 结果
			q = append(q, n.Left, n.Right) // 把 append(节点, 元素个数.Left, 元素个数.Right) 写入 节点
		} else { // 否则
			res = append(res, -1) // 把 append(结果, 减 1) 写入 结果
		}
	}
	for len(res) > 0 && res[len(res)-1] == -1 { // 把 赋值为 减 1 { 写入 for len(res) > 0 && res[len(res)-1]
		res = res[:len(res)-1] // 把 结果[:长度(结果) 减 1] 写入 结果
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	t1 := &TreeNode{Val: 1}             // 把 按位与 TreeNode{Val: 1} 写入 t1 :
	t1.Left = &TreeNode{Val: 3}         // 把 按位与 TreeNode{Val: 3} 写入 t1.Left
	t1.Right = &TreeNode{Val: 2}        // 把 按位与 TreeNode{Val: 2} 写入 t1.Right
	t1.Left.Left = &TreeNode{Val: 5}    // 把 按位与 TreeNode{Val: 5} 写入 t1.Left.Left
	t2 := &TreeNode{Val: 2}             // 把 按位与 TreeNode{Val: 2} 写入 t2 :
	t2.Left = &TreeNode{Val: 1}         // 把 按位与 TreeNode{Val: 1} 写入 t2.Left
	t2.Right = &TreeNode{Val: 3}        // 把 按位与 TreeNode{Val: 3} 写入 t2.Right
	t2.Left.Right = &TreeNode{Val: 4}   // 把 按位与 TreeNode{Val: 4} 写入 t2.Left.Right
	t2.Right.Right = &TreeNode{Val: 7}  // 把 按位与 TreeNode{Val: 7} 写入 t2.Right.Right
	merged := mergeTrees(t1, t2)        // 把 mergeTrees(t1, t2) 写入 merged :
	got := toList(merged)               // 把 toList(merged) 写入 got :
	want := []int{3, 4, 5, 5, 4, -1, 7} // 把 []int{3, 4, 5, 5, 4, 减 1, 7} 写入 want :
	if !reflect.DeepEqual(got, want) {  // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
