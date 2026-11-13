-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137409838
-- LeetCode 572. 另一棵树的子树 — Lua 版（方案3）
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

local function check(a, b) -- local function check(数组, b)
	if not a and not b then
		return true
	end -- 若 not 数组 and not b then return true 终点
	if not a or not b or a.val ~= b.val then
		return false
	end -- 若 not 数组 or not b or 数组.值 ~ 赋值为 b.值 then return false 终点
	return check(a.left, b.left) and check(a.right, b.right) -- 返回 check(数组.左边界, b.左边界) and check(数组.右边界, b.右边界)
end -- 终点
local function is_subtree(root, sub) -- local function is_subtree(根节点, sub)
	if not root then
		return false
	end -- 若 not 根节点 then return false 终点
	return check(root, sub) or is_subtree(root.left, sub) or is_subtree(root.right, sub)
end -- 终点
assert(is_subtree(build_tree({ 3, 4, 5, 1, 2 }), build_tree({ 4, 1, 2 })) == true) -- 断言校验
assert(is_subtree(build_tree({ 3, 4, 5, 1, 2, "null", "null", "null", "null", 0 }), build_tree({ 4, 1, 2 })) == false) -- 断言校验
assert(is_subtree(nil, nil) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
