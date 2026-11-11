-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136528287
-- LeetCode 236. 二叉树的最近公共祖先 — Lua 版（方案1）
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

local function lca(n, p, q) -- local function lca(元素个数, 节点, 节点)
	if not n then
		return nil
	end -- 若 not 元素个数 then return nil 终点
	if n.val == p or n.val == q then
		return n.val
	end -- 若 元素个数.值 等于 节点 or 元素个数.值 等于 节点 then return 元素个数.值 终点
	local l = lca(n.left, p, q) -- 把 lca(元素个数.左边界, 节点, 节点) 写入 local l
	local r = lca(n.right, p, q) -- 把 lca(元素个数.右边界, 节点, 节点) 写入 local r
	if l and r then
		return n.val
	end -- 若 左指针 and 右指针 then return 元素个数.值 终点
	if l then
		return l
	end -- 若 左指针 then return 左指针 终点
	return r -- 返回 右指针
end -- 终点
local function lowest_common_ancestor(root, p, q) -- local function lowest_common_ancestor(根节点, 节点, 节点)
	return lca(root, p, q) or -1 -- 返回 lca(根节点, 节点, 节点) or 减 1
end -- 终点
local t = build_tree({ 3, 5, 1, 6, 2, 0, 8, "null", "null", 7, 4 })
assert(lowest_common_ancestor(t, 5, 1) == 3) -- 断言校验
assert(lowest_common_ancestor(t, 5, 4) == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
