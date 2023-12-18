from fastapi import FastApi

app=FastApi()

@app.get('/')
async def f_index():
    return{"FIO":"Yudina Anna Gagikovna"}