-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
-- LeetCode 104. 二叉树的最大深度 — Lua 版（方案9：分治递归（assertEq 风格自测））
-- harness：层序数组建树，"null" 表示空节点

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

-- 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
local function max_depth(root) -- local function max_depth(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local l = max_depth(root.left) -- 把 max_depth(根节点.左边界) 写入 local l
	local r = max_depth(root.right) -- 把 max_depth(根节点.右边界) 写入 local r
	if l > r then
		return 1 + l
	else
		return 1 + r
	end -- 若 左指针 超过 右指针 then return 1 加 左指针 else return 1 加 右指针 终点
end -- 终点

-- 自测：与 blog 方案用例一致
local tests = { -- 把 { 写入 local tests
	{ {}, 0 },
	{ { 3, 9, 20, "null", "null", 15, 7 }, 3 },
	{ { 1, 2, 3, 4, 5 }, 3 },
	{ { 1, "null", 2, "null", 3 }, 3 },
}
for idx, t in ipairs(tests) do -- 遍历取 另一字符串
	local got = max_depth(build_tree(t[1])) -- 把 max_depth(build_tree(另一字符串[1])) 写入 local got
	local want = t[2] -- 把 另一字符串[2] 写入 local want
	assert(got == want, string.format("case %d failed: got %d want %d", idx, got, want)) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
