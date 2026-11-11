// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool { // 定义判定函数 isSubtree
	if root == nil { // 若 根节点 等于 nil
		return false // 返回 false
	}
	return check(root, subRoot) || isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot) // 定义判定函数 check
}

func check(a, b *TreeNode) bool { // 定义判定函数 check
	if a == nil && b == nil { // 若 数组 等于 nil 且 b 等于 nil
		return true // 返回 true
	}
	if a == nil || b == nil { // 若 数组 等于 nil 或 b 等于 nil
		return false // 返回 false
	}
	if a.Val == b.Val { // 若 数组.Val 等于 b.Val
		return check(a.Left, b.Left) && check(a.Right, b.Right) // 定义判定函数 check
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	sub := &TreeNode{4, &TreeNode{1, nil, nil}, &TreeNode{2, nil, nil}}
	root := &TreeNode{3, &TreeNode{4, &TreeNode{1, nil, nil}, &TreeNode{2, nil, nil}}, &TreeNode{5, nil, nil}}
	sub2 := &TreeNode{4, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}
	type tc struct { // 定义类型
		name string // name string
		got  bool   // got bool
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"None/None", isSubtree(nil, nil), false},
		{"root/sub", isSubtree(root, sub), true},
		{"root/sub2", isSubtree(root, sub2), false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if c.got != c.want { // 若 字符.got 不等于 字符.want
			ok = false                                 // 把 false 写入 ok
			fmt.Println("FAIL", c.name, c.got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
