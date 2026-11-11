-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136684493
-- LeetCode 230. 二叉搜索树中第K小的元素 — Lua 版（方案1）
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

local function kth_smallest(root, k) -- local function kth_smallest(根节点, 下标 k)
	local stack = {} -- 把 {} 写入 local stack
	local cur = root -- 把 根节点 写入 local cur
	while cur or #stack > 0 do -- while 当前值 or #栈 超过 0 do
		while cur do -- while 当前值 do
			stack[#stack + 1] = cur -- 把 当前值 写入 stack[#stack + 1]
			cur = cur.left -- 把 当前值.左边界 存入 当前值
		end -- 终点
		cur = table.remove(stack) -- 把 table 弹出 栈) 存入 当前值
		k = k - 1 -- 把 下标 k 减 1 存入 下标 k
		if k == 0 then
			return cur.val
		end -- 若 下标 k 等于 0 then return 当前值.值 终点
		cur = cur.right -- 把 当前值.右边界 存入 当前值
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
local t = build_tree({ 3, 1, 4, "null", 2 }) -- 把 build_tree({3, 1, 4, 「null」, 2}) 写入 local t
assert(kth_smallest(t, 1) == 1) -- 断言校验
assert(kth_smallest(t, 2) == 2) -- 断言校验
local t2 = build_tree({ 5, 3, 6, 2, 4, "null", "null", 1 }) -- 把 build_tree({5, 3, 6, 2, 4, 「null」, 「null」, 1}) 写入 local t2
assert(kth_smallest(t2, 3) == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
