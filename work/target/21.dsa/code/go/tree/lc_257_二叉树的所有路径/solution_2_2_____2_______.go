// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083565
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
	"sort"
	"strconv"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func binaryTreePaths(root *TreeNode) []string { // 定义函数/方法 binaryTreePaths
	paths := []string{} // 把 []string{} 写入 paths :
	if root == nil {    // 若 根节点 等于 nil
		return paths // 返回 paths
	}
	nodeQ := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 nodeQ :
	pathQ := []string{strconv.Itoa(root.Val)} // 把 []string{strconv.Itoa(根节点.Val)} 写入 pathQ :
	for len(nodeQ) > 0 {                      // for 长度(nodeQ) 超过 0 {
		n := nodeQ[0]                        // 把 nodeQ[0] 写入 n :
		nodeQ = nodeQ[1:]                    // 把 nodeQ[1:] 写入 nodeQ
		path := pathQ[0]                     // 把 pathQ[0] 写入 path :
		pathQ = pathQ[1:]                    // 把 pathQ[1:] 写入 pathQ
		if n.Left == nil && n.Right == nil { // 若 元素个数.Left 等于 nil 且 元素个数.Right 等于 nil
			paths = append(paths, path) // 把 append(paths, 当前路径) 写入 paths
		} else { // 否则
			if n.Left != nil { // 若 元素个数.Left 不等于 nil
				nodeQ = append(nodeQ, n.Left) // 把 append(nodeQ, 元素个数.Left) 写入 nodeQ
				pathQ = append(pathQ, path+"->"+strconv.Itoa(n.Left.Val))
			}
			if n.Right != nil { // 若 元素个数.Right 不等于 nil
				nodeQ = append(nodeQ, n.Right) // 把 append(nodeQ, 元素个数.Right) 写入 nodeQ
				pathQ = append(pathQ, path+"->"+strconv.Itoa(n.Right.Val))
			}
		}
	}
	return paths // 返回 paths
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
	ok := true                                      // 把 true 写入 ok :
	if got := binaryTreePaths(nil); len(got) != 0 { // 若 got : 赋值为 binaryTreePaths(nil); 长度(got) 不等于 0
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL nil got=%v\n", got) // 打印输出
	}
	root := buildTree([]int{1, 2, 3, -1, 5}) // 把 buildTree([]int{1, 2, 3, 减 1, 5}) 写入 root :
	got := binaryTreePaths(root)             // 把 binaryTreePaths(根节点) 写入 got :
	want := []string{"1->2->5", "1->3"}      // 把 []string{「1 减 超过 2 减 超过 5」, 「1 减 超过 2 减 超过 5」} 写入 want :
	gs := append([]string{}, got...)         // 把 append([]string{}, got...) 写入 gs :
	ws := append([]string{}, want...)        // 把 append([]string{}, want...) 写入 ws :
	sort.Strings(gs)                         // sort.Strings(gs)
	sort.Strings(ws)                         // sort.Strings(ws)
	if !reflect.DeepEqual(gs, ws) {          // 若 取反 reflect.DeepEqual(gs, ws
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
