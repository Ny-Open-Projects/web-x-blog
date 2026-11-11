-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136210437
-- LeetCode 222. 完全二叉树的节点个数 — Lua 版（方案3）
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

local function count_nodes(root) -- local function count_nodes(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local lh, r = 0, root -- 把 0, 根节点 写入 local lh, r
	while r do
		lh = lh + 1
		r = r.left
	end -- 把 lh 加 1; 右指针 赋值为 右指针.左边界 终点 写入 while r do lh
	local rh = 0
	r = root -- 把 0; 右指针 赋值为 根节点 写入 local rh
	while r do
		rh = rh + 1
		r = r.right
	end -- 把 rh 加 1; 右指针 赋值为 右指针.右边界 终点 写入 while r do rh
	if lh == rh then
		return (1 << lh) - 1
	end -- 若 lh 等于 rh then return (1 小于 小于 lh) 减 1 终点
	return 1 + count_nodes(root.left) + count_nodes(root.right) -- 返回 1 加 count_nodes(根节点.左边界) 加 count_nodes(根节点.右边界)
end -- 终点
assert(count_nodes(build_tree({ 1, 2, 3, 4, 5, 6 })) == 6) -- 断言校验
assert(count_nodes(nil) == 0) -- 断言校验
assert(count_nodes(build_tree({ 1 })) == 1) -- 断言校验
assert(count_nodes(build_tree({ 1, 2, 3, 4, 5, 6, 7, 8 })) == 8) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
