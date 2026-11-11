-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
-- LeetCode 621. 任务调度器 — Lua 版

-- 方案6（公式法另一写法：Counter 值列表 + count(freq)）
local function least_interval(tasks, n) -- local function least_interval(tasks, 元素个数)
	local cnt = {} -- 把 {} 写入 local cnt
	for _, t in ipairs(tasks) do -- 遍历取 另一字符串
		cnt[t] = (cnt[t] or 0) + 1 -- 把 (计数[另一字符串] or 0) 加 1 写入 cnt[t]
	end -- 终点
	local list = {} -- 把 {} 写入 local list
	for _, v in pairs(cnt) do
		list[#list + 1] = v
	end -- 遍历取 值
	local freq = 0 -- 把 0 写入 local freq
	for _, v in ipairs(list) do -- 遍历取 值
		if v > freq then
			freq = v
		end -- 若 值 超过 频次表 then 频次表 赋值为 值 终点
	end -- 终点
	local same = 0 -- 把 0 写入 local same
	for _, v in ipairs(list) do -- 遍历取 值
		if v == freq then
			same = same + 1
		end -- 若 值 等于 频次表 then same 赋值为 same 加 1 终点
	end -- 终点
	return math.max((freq - 1) * (n + 1) + same, #tasks) -- 返回 math.取较大值 (频次表 减 1) 乘 (元素个数 加 1) 加 same, #tasks)
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local cases = { -- 把 { 写入 local cases
	{ { "A", "A", "A", "B", "B", "B" }, 2, 8 },
	{ { "A", "A", "A", "A" }, 2, 10 },
	{ { "A", "B", "C", "D" }, 0, 4 },
}
for i, c in ipairs(cases) do -- 遍历取 字符
	local got = least_interval(c[1], c[2]) -- 把 least_interval(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("FAIL case %d got %d want %d", i, got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
