-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
-- LeetCode LCP 10. 二叉树任务调度 — Lua 版（方案2：深度优先-优化）

-- 层序数组建树：用 "n" 字符串表示空节点（nil 会把数组截断）
local function new_node(val)
	return { val = val, left = nil, right = nil } -- 二叉树节点：val 为自身执行时间
end

local function build_tree(vals)
	if #vals == 0 then
		return nil
	end
	local root = new_node(vals[1])
	local queue = { root } -- 队列里只放非空节点
	local head, i = 1, 2
	while head <= #queue and i <= #vals do
		local node = queue[head] -- 出队一个父节点
		head = head + 1
		if i <= #vals and vals[i] ~= "n" then -- 左孩子
			node.left = new_node(vals[i])
			queue[#queue + 1] = node.left
		end
		i = i + 1
		if i <= #vals and vals[i] ~= "n" then -- 右孩子
			node.right = new_node(vals[i])
			queue[#queue + 1] = node.right
		end
		i = i + 1
	end
	return root
end

-- dfs 返回 子树总耗时, 子树最小完成时间 max_exec（Lua 多返回值）
local function dfs(root)
	if root == nil then
		return 0.0, 0.0
	end -- 空子树
	local left_sum, left_exec = dfs(root.left) -- 左子树的总耗时与最小完成时间
	local right_sum, right_exec = dfs(root.right) -- 右子树的总耗时与最小完成时间
	-- 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
	-- 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
	local parallel = (left_sum + right_sum) / 2.0 -- 两台机器均摊左右子树总工作量（浮点）
	local max_exec = root.val + math.max(math.max(left_exec, right_exec), parallel)
	return left_sum + right_sum + root.val, max_exec
end

local function minimal_execution_time(root) -- 答案 = 整棵树的最小完成时间
	local _, max_exec = dfs(root)
	return max_exec
end

local cases = { -- 三个官方用例
	{ { 47, 74, 31 }, 121.0 },
	{ { 15, 21, "n", 24, "n", 27, 26 }, 87.0 },
	{ { 1, 3, 2, "n", "n", 4, 4 }, 7.5 },
}
local fail = false
for _, case in ipairs(cases) do
	local got = minimal_execution_time(build_tree(case[1]))
	if math.abs(got - case[2]) >= 1e-6 then -- 浮点比较用 1e-6 容差
		print("FAIL got", got, "want", case[2]) -- 失败打印 FAIL
		fail = true
	end
end
if fail then
	os.exit(1)
end -- 非零退出
print("PASS") -- 全部用例通过，输出 PASS
