package com.imooc.socialecom.base;

public class JsonReturnType {

    private String status;

    private Object data;

    public static JsonReturnType createType(Object model){
        JsonReturnType returnType = new JsonReturnType();
        returnType.setData(model);
        returnType.setStatus("success");
        return returnType;
    }

    public static JsonReturnType createErrorType(String errMsg){
        JsonReturnType returnType = new JsonReturnType();
        returnType.setData(errMsg);
        returnType.setStatus("fail");
        return returnType;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Object getData() {
        return data;
    }

    public void setData(Object data) {
        this.data = data;
    }
}
