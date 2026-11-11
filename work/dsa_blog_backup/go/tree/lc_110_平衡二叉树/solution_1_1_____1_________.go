// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144994166
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0].(int)} // 把 按位与 TreeNode{Val: vals[0].(int)} 写入 root :
	q := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                // 把 1 写入 i :
	for len(q) > 0 && i < len(vals) {     // 定义函数/方法 len
		node := q[0]                         // 把 节点[0] 写入 node :
		q = q[1:]                            // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                  // 下标 i 加一
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
			q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func abs(x int) int { // 定义函数/方法 abs
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

func max2(a, b int) int { // 定义函数/方法 max2
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func isBalanced(root *TreeNode) bool { // 定义判定函数 isBalanced
	if root == nil { // 若 根节点 等于 nil
		return true // 返回 true
	}
	var height func(node *TreeNode) int // var height func(节点 乘 TreeNode) int
	height = func(node *TreeNode) int { // 把 func(节点 乘 TreeNode) int { 写入 height
		if node == nil { // 若 节点 等于 nil
			return 0 // 返回 0
		}
		return max2(height(node.Left), height(node.Right)) + 1 // 返回 max2(height(节点.Left), height(节点.Right)) 加 1
	}
	leftHeight := height(root.Left)                                                            // 把 height(根节点.Left) 写入 leftHeight :
	rightHeight := height(root.Right)                                                          // 把 height(根节点.Right) 写入 rightHeight :
	return abs(leftHeight-rightHeight) <= 1 && isBalanced(root.Left) && isBalanced(root.Right) // 定义函数/方法 abs
}

type tc struct { // 定义类型
	root *TreeNode // 根节点 乘 TreeNode
	want bool      // want bool
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{buildTree(nil), true},
		{buildTree([]interface{}{1}), true},
		{buildTree([]interface{}{3, 9, 20, nil, nil, 15, 7}), true},
		{buildTree([]interface{}{1, 2, nil, 3, nil, 4, nil, 5}), false},
		{buildTree([]interface{}{1, 2, 2, 3, nil, nil, 3, 4, nil, nil, 4}), false},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		got := isBalanced(c.root) // 把 isBalanced(字符.根节点) 写入 got :
		if got != c.want {        // 若 got 不等于 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
