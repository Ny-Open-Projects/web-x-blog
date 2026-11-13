-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
-- LeetCode 933. 最近的请求次数 — Lua 版

-- 方案3：push + 真出队（table.remove 首元素，等价 TS 数组 shift）
local RecentCounter = {} -- 把 {} 写入 local RecentCounter
RecentCounter.__index = RecentCounter -- 把 RecentCounter 写入 RecentCounter.__index

function RecentCounter.new() -- function RecentCounter.new()
	return setmetatable({ q = {} }, RecentCounter) -- 返回 setmetatable({ 节点 赋值为 {} }, RecentCounter)
end -- 终点

function RecentCounter:ping(t) -- function RecentCounter:ping(另一字符串)
	self.q[#self.q + 1] = t -- 把 另一字符串 写入 self.q[#self.q + 1]
	while self.q[1] ~= nil and self.q[1] < t - 3000 do -- 把 nil and self.节点[1] 小于 另一字符串 减 3000 do 写入 while self.q[1] ~
		table.remove(self.q, 1) -- table 弹出 self.节点, 1)
	end -- 终点
	return #self.q -- 返回 #self.节点
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local c = RecentCounter.new() -- 把 RecentCounter.new() 写入 local c
local got = { c:ping(1), c:ping(100), c:ping(3001), c:ping(3002) }
local want = { 1, 2, 3, 3 } -- 把 { 1, 2, 3, 3 } 写入 local want
for i = 1, #want do -- 把 1, #want do 写入 for i
	assert(got[i] == want[i], string.format("FAIL case %d got %d want %d", i, got[i], want[i])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
