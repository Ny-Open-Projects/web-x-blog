-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136726698
-- LeetCode 617. 合并二叉树 — Lua 版（方案2）
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

local function same_tree(p, q) -- local function same_tree(节点, 节点)
	if not p and not q then
		return true
	end -- 若 not 节点 and not 节点 then return true 终点
	if not p or not q or p.val ~= q.val then
		return false
	end -- 若 not 节点 or not 节点 or 节点.值 ~ 赋值为 节点.值 then return false 终点
	return same_tree(p.left, q.left) and same_tree(p.right, q.right) -- 返回 same_tree(节点.左边界, 节点.左边界) and same_tree(节点.右边界, 节点.右边界)
end -- 终点
local function merge_trees(t1, t2) -- local function merge_trees(t1, t2)
	if not t1 then
		return t2
	end -- 若 not t1 then return t2 终点
	if not t2 then
		return t1
	end -- 若 not t2 then return t1 终点
	t1.val = t1.val + t2.val -- 把 t1.值 加 t2.值 写入 值
	t1.left = merge_trees(t1.left, t2.left) -- 把 merge_trees(t1.左边界, t2.左边界) 写入 左边界
	t1.right = merge_trees(t1.right, t2.right) -- 把 merge_trees(t1.右边界, t2.右边界) 写入 右边界
	return t1 -- 返回 t1
end -- 终点
local function check(a, b, w) -- local function check(数组, b, 权重)
	assert(same_tree(merge_trees(build_tree(a), build_tree(b)), build_tree(w)), "merge failed") -- 断言校验
end -- 终点
check({ 1, 3, 2, 5 }, { 2, 1, 3, "null", 4, "null", 7 }, { 3, 4, 5, 5, 4, "null", 7 })
check({}, { 1 }, { 1 }) -- check({}, {1}, {1})
check({ 1 }, {}, { 1 }) -- check({1}, {}, {1})
check({ 1, 2, 3 }, { 1, 2, 3 }, { 2, 4, 6 }) -- check({1,2,3}, {1,2,3}, {2,4,6})
print("PASS") -- 全部用例通过，输出 PASS
