def read_lines(lines):
    for line in lines:
        yield line.strip()

def non_empty(lines):
    for line in lines:
        if line:
            yield line

def parse_fields(lines, sep=","):
    for line in lines:
        yield line.split(sep)

def only_type(rows, type_name):
    for fields in rows:
        if fields and fields[0] == type_name:
            yield fields

def to_records(rows):
    for fields in rows:
        yield {"type": fields[0], "value": float(fields[1])}

if __name__ == "__main__":
    raw = ["error,0.5", "", "info,1.2", "error,2.7", "warn,0.1"]
    pipeline = to_records(
        only_type(parse_fields(non_empty(read_lines(raw))), "error")
    )
    for record in pipeline:              # 惰性:逐条流过整条管道
        print(record)
