import inspect

def transfer(amount, *, from_acc="A", to_acc="B", fee=0.0):
    return f"{from_acc} -> {to_acc}: {amount} fee={fee}"

if __name__ == "__main__":
    sig = inspect.signature(transfer)
    for name, param in sig.parameters.items():
        default = "REQUIRED" if param.default is inspect.Parameter.empty else param.default
        print(f"{name:10s} kind={param.kind.name:20s} default={default}")

    bound = sig.bind(100, to_acc="C")
    bound.apply_defaults()
    print("normalized:", dict(bound.arguments))
    print(transfer(*bound.args, **bound.kwargs))
