// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
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

func invertTree(root *TreeNode) *TreeNode { // 定义函数/方法 invertTree
	if root == nil { // 若 根节点 等于 nil
		return nil // 返回 nil
	}
	q := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 q :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		n := q[0]                         // 把 节点[0] 写入 n :
		q = q[1:]                         // 把 节点[1:] 写入 节点
		n.Left, n.Right = n.Right, n.Left // 把 元素个数.Right, 元素个数.Left 写入 n.Left, n.Right
		if n.Left != nil {                // 若 元素个数.Left 不等于 nil
			q = append(q, n.Left) // 把 append(节点, 元素个数.Left) 写入 节点
		}
		if n.Right != nil { // 若 元素个数.Right 不等于 nil
			q = append(q, n.Right) // 把 append(节点, 元素个数.Right) 写入 节点
		}
	}
	return root // 返回 根节点
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
	ok := true                                         // 把 true 写入 ok :
	if got := toList(invertTree(nil)); len(got) != 0 { // 若 got : 赋值为 toList(invertTree(nil)); 长度(got) 不等于 0
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL nil got=%v\n", got) // 打印输出
	}
	root := buildTree([]int{4, 2, 7, 1, 3, 6, 9}) // 把 buildTree([]int{4, 2, 7, 1, 3, 6, 9}) 写入 root :
	got := toList(invertTree(root))               // 把 toList(invertTree(根节点)) 写入 got :
	want := []int{4, 7, 2, 9, 6, 3, 1}            // 把 []int{4, 7, 2, 9, 6, 3, 1} 写入 want :
	if !reflect.DeepEqual(got, want) {            // 若 取反 reflect.DeepEqual(got, want
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
