try:
    from fastapi import FastAPI, HTTPException, status
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
items = {1: 'apple'}

@app.post('/items', status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    new_id = max(items or {0: 0}) + 1
    items[new_id] = name
    return {'id': new_id, 'name': name}

@app.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='item not found')
    return {'id': item_id, 'name': items[item_id]}

@app.delete('/items/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    items.pop(item_id, None)
