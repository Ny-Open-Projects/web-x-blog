-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135586474
-- LeetCode 101. 对称二叉树 — Lua 版（方案3）
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

local function is_symmetric(root) -- local function is_symmetric(根节点)
	local function is_mirror(l, r) -- local function is_mirror(左指针, 右指针)
		if not l and not r then
			return true
		end -- 若 not 左指针 and not 右指针 then return true 终点
		if not l or not r then
			return false
		end -- 若 not 左指针 or not 右指针 then return false 终点
		return l.val == r.val and is_mirror(l.left, r.right) and is_mirror(r.left, l.right)
	end -- 终点
	if not root then
		return true
	end -- 若 not 根节点 then return true 终点
	return is_mirror(root.left, root.right) -- 返回 is_mirror(根节点.左边界, 根节点.右边界)
end -- 终点
assert(is_symmetric(nil) == true) -- 断言校验
assert(is_symmetric(build_tree({ 1, 2, 2, 3, 4, 4, 3 })) == true) -- 断言校验
assert(is_symmetric(build_tree({ 1, 2, 2, "null", 3, "null", 3 })) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
