-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135005838
-- LeetCode 700. 二叉搜索树中的搜索 — Lua 版（方案2）
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

local function search_bst(root, val) -- local function search_bst(根节点, 值)
	local cur = root -- 把 根节点 写入 local cur
	while cur do -- while 当前值 do
		if cur.val == val then
			return cur.val
		end -- 若 当前值.值 等于 值 then return 当前值.值 终点
		if cur.val > val then
			cur = cur.left
		else
			cur = cur.right
		end -- 若 当前值.值 超过 值 then 当前值 赋值为 当前值.左边界 else 当前值 赋值为 当前值.右边界 终点
	end -- 终点
	return nil -- 返回 nil
end -- 终点
local t = build_tree({ 4, 2, 7, 1, 3 }) -- 把 build_tree({4, 2, 7, 1, 3}) 写入 local t
assert(search_bst(t, 2) == 2) -- 断言校验
assert(search_bst(t, 5) == nil) -- 断言校验
assert(search_bst(t, 4) == 4) -- 断言校验
assert(search_bst(nil, 1) == nil) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
