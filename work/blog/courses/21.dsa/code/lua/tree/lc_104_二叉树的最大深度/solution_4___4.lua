-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
-- LeetCode 104. 二叉树的最大深度 — Lua 版（方案4：分治递归 + 树遍历辅助（中序/自底向上层序/根叶路径/层均值））
-- harness：层序数组建树，"null" 表示空节点

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

-- 辅助：中序遍历
local function inorder(root, out) -- local function inorder(根节点, out)
	out = out or {} -- 把 out or {} 存入 out
	if not root then
		return out
	end -- 若 not 根节点 then return out 终点
	inorder(root.left, out) -- inorder(根节点.左边界, out)
	out[#out + 1] = root.val -- 把 根节点.值 写入 out[#out + 1]
	inorder(root.right, out) -- inorder(根节点.右边界, out)
	return out -- 返回 out
end -- 终点

-- 辅助：自底向上层序遍历
local function level_order_bottom(root) -- local function level_order_bottom(根节点)
	local res = {} -- 把 {} 写入 local res
	local queue = {} -- 把 {} 写入 local queue
	if root then
		queue[1] = root
	end -- 若 根节点 then 队列[1] 赋值为 根节点 终点
	while #queue > 0 do -- while #队列 超过 0 do
		local vals = {} -- 把 {} 写入 local vals
		local nxt = {} -- 把 {} 写入 local nxt
		for i = 1, #queue do -- 把 1, #队列 do 写入 for i
			local node = queue[i] -- 把 队列[下标 i] 写入 local node
			vals[#vals + 1] = node.val -- 把 节点.值 写入 vals[#vals + 1]
			if node.left then
				nxt[#nxt + 1] = node.left
			end -- 若 节点.左边界 then nxt[#nxt 加 1] 赋值为 节点.左边界 终点
			if node.right then
				nxt[#nxt + 1] = node.right
			end -- 若 节点.右边界 then nxt[#nxt 加 1] 赋值为 节点.右边界 终点
		end -- 终点
		table.insert(res, 1, vals) -- table 插入 结果, 1, vals)
		queue = nxt -- 把 nxt 存入 队列
	end -- 终点
	return res -- 返回 结果
end -- 终点

-- 辅助：所有根到叶路径
local function binary_tree_paths(root) -- local function binary_tree_paths(根节点)
	local out = {} -- 把 {} 写入 local out
	local function dfs(n, path) -- local function dfs(元素个数, 当前路径)
		if not n then
			return
		end -- 若 not 元素个数 then return 终点
		path = path .. tostring(n.val) -- 把 当前路径 .. tostring(元素个数.值) 存入 当前路径
		if not n.left and not n.right then -- 若 not 元素个数.左边界 and not 元素个数.右边界 then
			out[#out + 1] = path -- 把 当前路径 写入 out[#out + 1]
			return -- return
		end -- 终点
		path = path .. "->" -- 把 当前路径 .. 「 减 超过 」 存入 当前路径
		dfs(n.left, path) -- dfs(元素个数.左边界, 当前路径)
		dfs(n.right, path) -- dfs(元素个数.右边界, 当前路径)
	end -- 终点
	dfs(root, "") -- dfs(根节点, 「」)
	return out -- 返回 out
end -- 终点

-- 辅助：每层节点均值
local function average_of_levels(root) -- local function average_of_levels(根节点)
	local result = {} -- 把 {} 写入 local result
	local queue = {} -- 把 {} 写入 local queue
	if root then
		queue[1] = root
	end -- 若 根节点 then 队列[1] 赋值为 根节点 终点
	while #queue > 0 do -- while #队列 超过 0 do
		local total = 0 -- 把 0 写入 local total
		local nxt = {} -- 把 {} 写入 local nxt
		for i = 1, #queue do -- 把 1, #队列 do 写入 for i
			local node = queue[i] -- 把 队列[下标 i] 写入 local node
			total = total + node.val -- 把 总和 加 节点.值 存入 总和
			if node.left then
				nxt[#nxt + 1] = node.left
			end -- 若 节点.左边界 then nxt[#nxt 加 1] 赋值为 节点.左边界 终点
			if node.right then
				nxt[#nxt + 1] = node.right
			end -- 若 节点.右边界 then nxt[#nxt 加 1] 赋值为 节点.右边界 终点
		end -- 终点
		result[#result + 1] = total / #queue -- 把 总和 除以 #队列 写入 result[#result + 1]
		queue = nxt -- 把 nxt 存入 队列
	end -- 终点
	return result -- 返回 结果
end -- 终点

-- 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
local function max_depth(root) -- local function max_depth(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local l = max_depth(root.left) -- 把 max_depth(根节点.左边界) 写入 local l
	local r = max_depth(root.right) -- 把 max_depth(根节点.右边界) 写入 local r
	if l > r then
		return 1 + l
	else
		return 1 + r
	end -- 若 左指针 超过 右指针 then return 1 加 左指针 else return 1 加 右指针 终点
end -- 终点

-- 自测：与 blog 方案用例一致
local tests = { -- 把 { 写入 local tests
	{ { 3, 9, 20, "null", "null", 15, 7 }, 3 },
	{ { 1, 2, 3, 4, 5 }, 3 },
}
for idx, t in ipairs(tests) do -- 遍历取 另一字符串
	local got = max_depth(build_tree(t[1])) -- 把 max_depth(build_tree(另一字符串[1])) 写入 local got
	local want = t[2] -- 把 另一字符串[2] 写入 local want
	assert(got == want, string.format("case %d failed: got %d want %d", idx, got, want)) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
