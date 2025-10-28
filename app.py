import os, socket, random
from flask import Flask, render_template, render_template_string, jsonify
from s3_helper import list_image_urls
from pokeneas_data import random_pokenea

app = Flask(__name__)

def container_id():
    return socket.gethostname()

@app.route("/")
def home():
    return render_template("home.html")


# Anexo: listar TODO el bucket
@app.route("/imagenes")
def listar_imagenes():
    image_urls = list_image_urls()
    html = """
    <h1>Imágenes desde S3</h1>
    {% for url in image_urls %}
      <div><img src="{{ url }}" style="max-width:300px"><br><small>{{ url }}</small><hr></div>
    {% endfor %}
    """
    return render_template_string(html, image_urls=image_urls)


@app.route("/imagen")
def pokenea_imagen():
    pk = random_pokenea()  # personaje aleatorio
    nombre_archivo = pk["nombre"].lower().replace("ñ", "n") + ".png"
    imagen_url = f"https://{os.getenv('S3_BUCKET')}.s3.amazonaws.com/pokeneas/{nombre_archivo}"
    return render_template(
        "imagen.html",
        nombre=pk["nombre"],
        imagen_url=imagen_url,
        frase=pk["frase"],
        container_id=container_id()
    )

@app.route("/pokenea")
def pokenea_view():
    pk = random_pokenea()
    return render_template(
        "pokenea.html",
        id=pk["id"],
        nombre=pk["nombre"],
        altura=pk["altura"],
        habilidad=pk["habilidad"],
        frase=pk["frase"],
        container_id=container_id()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))



