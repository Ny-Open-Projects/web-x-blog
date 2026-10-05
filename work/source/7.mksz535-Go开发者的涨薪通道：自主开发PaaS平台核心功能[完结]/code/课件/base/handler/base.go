package handler
import (
	"context"
    "git.imooc.com/coding-535/base/domain/service"
	log "github.com/asim/go-micro/v3/logger"
	base "git.imooc.com/coding-535/base/proto/base"
)
type Base struct{
     //注意这里的类型是 IBaseDataService 接口类型
     BaseDataService service.IBaseDataService
}
// Call is a single request handler called via client.Call or the generated client code
func (e *Base) Call(ctx context.Context, req *base.Request, rsp *base.Response) error {
	log.Info("Received Base.Call request")
	rsp.Msg = "Hello " + req.Name
	return nil
}
// Stream is a server side stream handler called via client.Stream or the generated client code
func (e *Base) Stream(ctx context.Context, req *base.StreamingRequest, stream base.Base_StreamStream) error {
	log.Infof("Received Base.Stream request with count: %d", req.Count)
	for i := 0; i < int(req.Count); i++ {
		log.Infof("Responding: %d", i)
		if err := stream.Send(&base.StreamingResponse{
			Count: int64(i),
		}); err != nil {
			return err
		}
	}
	return nil
}
// PingPong is a bidirectional stream handler called via client.Stream or the generated client code
func (e *Base) PingPong(ctx context.Context, stream base.Base_PingPongStream) error {
	for {
		req, err := stream.Recv()
		if err != nil {
			return err
		}
		log.Infof("Got ping %v", req.Stroke)
		if err := stream.Send(&base.Pong{Stroke: req.Stroke}); err != nil {
			return err
		}
	}
}
