-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135911085
-- LeetCode 654. 最大二叉树 — Lua 版（方案2）
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
local function levels_flat(root) -- local function levels_flat(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local out, q = {}, { root } -- 把 {}, {根节点} 写入 local out, q
	while #q > 0 do -- while #节点 超过 0 do
		local n = #q -- 把 #节点 写入 local n
		for _ = 1, n do -- 让 _ 从 1 走到 元素个数（Lua 1 基）
			local node = table.remove(q, 1) -- 把 table 弹出 节点, 1) 写入 local node
			out[#out + 1] = node.val -- 把 节点.值 写入 out[#out + 1]
			if node.left then
				q[#q + 1] = node.left
			end -- 若 节点.左边界 then 节点[#节点 加 1] 赋值为 节点.左边界 终点
			if node.right then
				q[#q + 1] = node.right
			end -- 若 节点.右边界 then 节点[#节点 加 1] 赋值为 节点.右边界 终点
		end -- 终点
	end -- 终点
	return out -- 返回 out
end -- 终点
local function eq(a, b) -- local function eq(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do
		if a[i] ~= b[i] then
			return false
		end
	end
	return true -- 返回 true
end -- 终点

local function construct_maximum_binary_tree(nums) -- local function construct_maximum_binary_tree(数组)
	if #nums == 0 then
		return nil
	end -- 若 #数组 等于 0 then return nil 终点
	local idx = 1 -- 把 1 写入 local idx
	for i = 1, #nums do -- 把 1, #数组 do 写入 for i
		if nums[i] > nums[idx] then
			idx = i
		end -- 若 数组[下标 i] 超过 数组[idx] then idx 赋值为 下标 i 终点
	end -- 终点
	local root = TreeNode.new(nums[idx]) -- 把 TreeNode.new(数组[idx]) 写入 local root
	local left, right = {}, {} -- 把 {}, {} 写入 local left, right
	for i = 1, idx - 1 do
		left[#left + 1] = nums[i]
	end -- 让 下标 i 从 1 走到 idx（Lua 1 基）
	for i = idx + 1, #nums do
		right[#right + 1] = nums[i]
	end -- 把 idx 加 1, #数组 do 右边界[#右边界 加 1] 赋值为 数组[下标 i] 终点 写入 for i
	root.left = construct_maximum_binary_tree(left) -- 把 construct_maximum_binary_tree(左边界) 写入 左边界
	root.right = construct_maximum_binary_tree(right) -- 把 construct_maximum_binary_tree(右边界) 写入 右边界
	return root -- 返回 根节点
end -- 终点
local t = construct_maximum_binary_tree({ 3, 2, 1, 6, 0, 5 })
assert(t.val == 6) -- 断言校验
assert(same_tree(t, build_tree({ 6, 3, 5, "null", 2, 0, "null", "null", 1, "null", "null" }))) -- 断言校验
assert(construct_maximum_binary_tree({ 1 }).val == 1) -- 断言校验
assert(construct_maximum_binary_tree({ 3, 2, 1 }).val == 3) -- 断言校验
assert(construct_maximum_binary_tree({}) == nil) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
