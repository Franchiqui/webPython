from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.traductor import traductor_func
from app.video import video_func


app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: str
    


@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}

@app.get("/libros/({id}")
def mostrar_libro(id: int):
    return {"data": id}

@app.get("/libros")
def mostrar_libros():
    return {"data": "Lista de libros"}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro (libro.titulo) insertado"}

@app.put("/libros/{id}")
def actualizar_libro(id: int, libro: Libro):
    return {"message": f"libro (libro.titulo) actualizado"}

@app.delete("/libros/{id}")
def eliminar_libro(id: int):
    return {"message": f"libro (libro.titulo) eliminado"}



class TraductorRequest(BaseModel):
    translate_text: str
    target_lang: str

@app.get("/video")
def video():
    return video_func()

@app.post("/traductor")
async def traductor_endpoint(request: Request, traductor_data: TraductorRequest):
    translate_text = traductor_data.translate_text
    target_lang = traductor_data.target_lang
    traduccion = traductor_func(translate_text, target_lang)
    return {"data": traduccion}

