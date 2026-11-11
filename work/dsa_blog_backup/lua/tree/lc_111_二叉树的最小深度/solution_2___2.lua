-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135759583
-- LeetCode 111. 二叉树的最小深度 — Lua 版（方案2）
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

local function min_depth(root) -- local function min_depth(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local q = { { root, 1 } } -- 把 {{根节点, 1}} 写入 local q
	local head = 1 -- 把 1 写入 local head
	while head <= #q do -- 把 #节点 do 写入 while head <
		local n, l = table.unpack(q[head]) -- 把 table.unpack(节点[头节点]) 写入 local n, l
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if not n.left and not n.right then
			return l
		end -- 若 not 元素个数.左边界 and not 元素个数.右边界 then return 左指针 终点
		if n.left then
			q[#q + 1] = { n.left, l + 1 }
		end -- 若 元素个数.左边界 then 节点[#节点 加 1] 赋值为 {元素个数.左边界, 左指针 加 1} 终点
		if n.right then
			q[#q + 1] = { n.right, l + 1 }
		end -- 若 元素个数.右边界 then 节点[#节点 加 1] 赋值为 {元素个数.右边界, 左指针 加 1} 终点
	end -- 终点
	return 0 -- 返回 0
end -- 终点
assert(min_depth(build_tree({ 3, 9, 20, "null", "null", 15, 7 })) == 2) -- 断言校验
assert(min_depth(build_tree({ 2, "null", 3, "null", 4, "null", 5, "null", 6 })) == 5) -- 断言校验
assert(min_depth(nil) == 0) -- 断言校验
assert(min_depth(build_tree({ 1 })) == 1) -- 断言校验
assert(min_depth(build_tree({ 1, 2 })) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
