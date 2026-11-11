-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856
-- LeetCode 1472. 设计浏览器历史记录 — Lua 版（方案1）
local BrowserHistory = {} -- 把 {} 写入 local BrowserHistory
BrowserHistory.__index = BrowserHistory -- 把 BrowserHistory 写入 BrowserHistory.__index
function BrowserHistory.new(homepage) -- function BrowserHistory.new(homepage)
	return setmetatable({ history = { homepage }, cur = 1 }, BrowserHistory)
end -- 终点
function BrowserHistory:visit(url) -- function BrowserHistory:visit(url)
	for i = #self.history, self.cur + 1, -1 do
		self.history[i] = nil
	end
	self.history[#self.history + 1] = url -- 把 url 写入 self.history[#self.history + 1]
	self.cur = #self.history -- 把 #self.history 写入 当前值
end -- 终点
function BrowserHistory:back(steps) -- function BrowserHistory:back(steps)
	self.cur = math.max(1, self.cur - steps) -- 把 math.取较大值 1, self.当前值 减 steps) 写入 当前值
	return self.history[self.cur] -- 返回 self.history[self.当前值]
end -- 终点
function BrowserHistory:forward(steps) -- function BrowserHistory:forward(steps)
	self.cur = math.min(#self.history, self.cur + steps) -- 把 math.取较小值 #self.history, self.当前值 加 steps) 写入 当前值
	return self.history[self.cur] -- 返回 self.history[self.当前值]
end -- 终点
local b = BrowserHistory.new("leetcode.com") -- 把 BrowserHistory.new(「leetcode.com」) 写入 local b
b:visit("google.com")
b:visit("facebook.com")
b:visit("youtube.com")
assert(b:back(1) == "facebook.com") -- 断言校验
assert(b:back(1) == "google.com") -- 断言校验
assert(b:forward(1) == "facebook.com") -- 断言校验
b:visit("linkedin.com") -- b:visit(「linkedin.com」)
assert(b:forward(2) == "linkedin.com") -- 断言校验
assert(b:back(2) == "google.com") -- 断言校验
assert(b:back(7) == "leetcode.com") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
