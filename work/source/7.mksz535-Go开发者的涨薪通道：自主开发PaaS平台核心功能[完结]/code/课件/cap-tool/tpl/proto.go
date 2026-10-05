package template

var (
	ProtoFNC = `syntax = "proto3";

package {{.FQDN}};

option go_package = "{{.Dir}}/proto/{{.Alias}};{{.Alias}}";

service {{title .Alias}} {
	rpc Call(Request) returns (Response) {}
}

message Message {
	string say = 1;
}

message Request {
	string name = 1;
}

message Response {
	string msg = 1;
}
`

	ProtoSRV = `syntax = "proto3";

package {{.Alias}};

option go_package = "./proto/{{.Alias}};{{.Alias}}";

service {{title .Alias}} {
	//对外提供添加服务
	rpc Add{{title .Alias}}({{title .Alias}}Info) returns (Response) {}
	rpc Delete{{title .Alias}}({{title .Alias}}Id) returns (Response) {}
	rpc Update{{title .Alias}}({{title .Alias}}Info) returns (Response) {}
	rpc Find{{title .Alias}}ByID({{title .Alias}}Id) returns ({{title .Alias}}Info) {}
	rpc FindAll{{title .Alias}}(FindAll) returns (All{{title .Alias}}) {}
}
message {{title .Alias}}Info {
	int64 id = 1;
}

message {{title .Alias}}Id {
	int64 id = 1;
}

message FindAll {

}

message Response {
	string msg =1 ;
}

message All{{title .Alias}} {
	repeated {{title .Alias}}Info {{.Alias}}_info = 1;
}


`

	ProtoAPI = `syntax = "proto3";

package {{.Alias}};

option go_package = "./proto/{{.Alias}};{{.Alias}}";

service {{title .Alias}} {
    rpc Find{{title .ApiDefaultServerName}}ById(Request) returns (Response){}
	rpc Add{{title .ApiDefaultServerName}}(Request) returns (Response){}
	rpc Delete{{title .ApiDefaultServerName}}ById(Request) returns (Response){}
	rpc Update{{title .ApiDefaultServerName}}(Request) returns (Response){}
	//默认接口
	rpc Call(Request) returns (Response){}
}

message Pair {
	string key = 1;
	repeated string values = 2;
}


message Request {
	string method = 1;
	string path = 2;
	map<string, Pair> header = 3;
	map<string, Pair> get = 4;
	map<string, Pair> post = 5;
	string body = 6;
	string url = 7;
}


message Response {
	int32 statusCode = 1;
	map<string, Pair> header = 2;
	string body = 3;
}

`


	ProtoApi = `

`
)
