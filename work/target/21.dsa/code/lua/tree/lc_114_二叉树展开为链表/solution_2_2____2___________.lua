-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135637716
-- LeetCode 114. 二叉树展开为链表 — Lua 版（方案2）
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

local function flatten(root) -- local function flatten(根节点)
	local prev = nil -- 把 nil 写入 local prev
	local function dfs(node) -- local function dfs(节点)
		if not node then
			return
		end -- 若 not 节点 then return 终点
		dfs(node.right) -- dfs(节点.右边界)
		dfs(node.left) -- dfs(节点.左边界)
		node.right = prev -- 把 前一个 写入 右边界
		node.left = nil -- 把 nil 写入 左边界
		prev = node -- 把 节点 存入 前一个
	end -- 终点
	dfs(root) -- dfs(根节点)
	return root -- 返回 根节点
end -- 终点
local function chain(root) -- local function chain(根节点)
	local out = {} -- 把 {} 写入 local out
	while root do -- while 根节点 do
		assert(root.left == nil, "left must be nil") -- 断言校验
		out[#out + 1] = root.val -- 把 根节点.值 写入 out[#out + 1]
		root = root.right -- 把 根节点.右边界 存入 根节点
	end -- 终点
	return out -- 返回 out
end -- 终点
local t = flatten(build_tree({ 1, 2, 5, 3, 4, "null", 6 })) -- 把 flatten(build_tree({1, 2, 5, 3, 4, 「null」, 6})) 写入 local t
local c = chain(t) -- 把 chain(另一字符串) 写入 local c
assert(#c == 6 and c[1] == 1 and c[6] == 6 and c[2] == 2 and c[3] == 3 and c[4] == 4 and c[5] == 5) -- 断言校验
local t2 = flatten(build_tree({ 7 })) -- 把 flatten(build_tree({7})) 写入 local t2
local c2 = chain(t2) -- 把 chain(t2) 写入 local c2
assert(#c2 == 1 and c2[1] == 7) -- 断言校验
assert(flatten(nil) == nil) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
