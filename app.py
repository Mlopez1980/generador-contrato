from flask import Flask, render_template, request, send_file
from generador import generar_contrato_desde_formulario, MODELOS  # ⬅️ IMPORTA MODELOS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        datos = {
            "NOMBRE": request.form["nombre"],
            "DNI": request.form["dni"],
            "ESTADO_CIVIL": request.form["estado_civil"],
            "PROFESION": request.form["profesion"],
            "FECHA": request.form["fecha"],
            "PRECIO": request.form["precio"],
            "MODELO": request.form["modelo"],
            "MONTO_RESERVA": request.form["monto_reserva"],
            "FECHA_RESERVA": request.form["fecha_reserva"],
            "COMPLEMENTO_PRIMA": request.form["complemento_prima"],
            "FECHA_COMPLEMENTO": request.form["fecha_complemento"],
            "TERCER_PAGO": request.form["tercer_pago"],
        }
        nombre_archivo = generar_contrato_desde_formulario(datos)
        return send_file(nombre_archivo, as_attachment=True)

    # 🔒 Lista fija para probar el frontend
    modelos = ["1E","2D","2E","2F","3C","3E","3F","4D","4E","4F","5C","5E","5F"]
    return render_template("formulario.html", modelos=modelos)


