import logging

root = logging.getLogger("app")
child = logging.getLogger("app.db")
grand = logging.getLogger("app.db.query")

for lg in (root, child, grand):
    lg.handlers.clear()
    lg.setLevel(logging.INFO)
    lg.propagate = True

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))

if __name__ == "__main__":
    root.addHandler(handler)              # handler 只挂出口层
    grand.info("propagates to root once")

    child.addHandler(handler)             # 反面教材:父子挂同一 handler
    child.info("now printed twice")
    child.propagate = False
    child.info("cut off: printed once")
