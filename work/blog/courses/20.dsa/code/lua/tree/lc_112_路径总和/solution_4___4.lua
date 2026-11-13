-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135991021
-- LeetCode 112. 路径总和 — Lua 版（方案4）
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

local function has_path_sum(root, sum) -- local function has_path_sum(根节点, 累计和)
	if not root then
		return false
	end -- 若 not 根节点 then return false 终点
	if not root.left and not root.right then
		return root.val == sum
	end -- 若 not 根节点.左边界 and not 根节点.右边界 then return 根节点.值 等于 累计和 终点
	return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)
end -- 终点
local t = build_tree({ 5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1 })
assert(has_path_sum(t, 22) == true) -- 断言校验
assert(has_path_sum(t, 1) == false) -- 断言校验
assert(has_path_sum(nil, 0) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
