from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def f_index():
    return{"FIO":"Yudina Anna Gagikovna"}

@app.get('/tools')
async def f_index1():
    return{"phone number":"89237517091"}

@app.get('/users')
async def f_index2():
    return{"skills":"Well done!"}