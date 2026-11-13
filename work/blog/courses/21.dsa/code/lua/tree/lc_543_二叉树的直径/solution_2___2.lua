-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135572347
-- LeetCode 543. 二叉树的直径 — Lua 版（方案2）
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

local function diameter_of_binary_tree(root) -- local function diameter_of_binary_tree(根节点)
	local ans = 0 -- 把 0 写入 local ans
	local function depth(n) -- local function 深度(元素个数)
		if not n then
			return 0
		end -- 若 not 元素个数 then return 0 终点
		local l = depth(n.left) -- 把 深度(元素个数.左边界) 写入 local l
		local r = depth(n.right) -- 把 深度(元素个数.右边界) 写入 local r
		if l + r > ans then
			ans = l + r
		end -- 若 左指针 加 右指针 超过 答案 then 答案 赋值为 左指针 加 右指针 终点
		return 1 + math.max(l, r) -- 返回 1 加 math.取较大值 左指针, 右指针)
	end -- 终点
	depth(root) -- 深度(根节点)
	return ans -- 返回 答案
end -- 终点
assert(diameter_of_binary_tree(build_tree({ 1, 2, 3, 4, 5 })) == 3) -- 断言校验
assert(diameter_of_binary_tree(nil) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
