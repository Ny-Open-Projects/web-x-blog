-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135666411
-- LeetCode 257. 二叉树的所有路径 — Lua 版（方案1）
local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

local function build_tree(vals) -- local function build_tree(vals)
	if not vals or #vals == 0 or vals[1] == "null" then
		return nil
	end
	local root = TreeNode.new(vals[1]) -- 把 TreeNode.new(vals[1]) 写入 local root
	local queue = { root } -- 把 {根节点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	local i = 2 -- 把 2 写入 local i
	while head <= #queue and i <= #vals do -- 把 #队列 and 下标 i 不超过 #vals do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.left = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 左边界
				queue[#queue + 1] = node.left -- 把 节点.左边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.right = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 右边界
				queue[#queue + 1] = node.right -- 把 节点.右边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点

local function binary_tree_paths(root) -- local function binary_tree_paths(根节点)
	local paths = {} -- 把 {} 写入 local paths
	local function dfs(n, path) -- local function dfs(元素个数, 当前路径)
		if not n then
			return
		end -- 若 not 元素个数 then return 终点
		path = path .. n.val -- 把 当前路径 .. 元素个数.值 存入 当前路径
		if not n.left and not n.right then -- 若 not 元素个数.左边界 and not 元素个数.右边界 then
			paths[#paths + 1] = path -- 把 当前路径 写入 paths[#paths + 1]
		else -- 否则
			path = path .. "->" -- 把 当前路径 .. 「 减 超过 」 存入 当前路径
			dfs(n.left, path) -- dfs(元素个数.左边界, 当前路径)
			dfs(n.right, path) -- dfs(元素个数.右边界, 当前路径)
		end -- 终点
	end -- 终点
	dfs(root, "") -- dfs(根节点, 「」)
	return paths -- 返回 paths
end -- 终点
local a = binary_tree_paths(build_tree({ 1, 2, 3 })) -- 把 binary_tree_paths(build_tree({1, 2, 3})) 写入 local a
assert(#a == 2 and a[1] == "1->2" and a[2] == "1->3") -- 断言校验
local b = binary_tree_paths(build_tree({ 1 })) -- 把 binary_tree_paths(build_tree({1})) 写入 local b
assert(#b == 1 and b[1] == "1") -- 断言校验
assert(#binary_tree_paths(nil) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
