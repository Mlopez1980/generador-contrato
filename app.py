from flask import Flask, render_template, request, send_file
from generador import generar_contrato, MODELOS
import os

app = Flask(__name__)

# Lista de modelos que ya NO están disponibles
NO_DISPONIBLES = ["1A", "1B", "1C", "1D", "1F", "2A", "2B", "2C", "3A", "3B", "3D", "4A", "4B", "4C", "5A", "5B", "5D" ]  # <-- Aquí pones los vendidos

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
            "TERCER_PAGO": request.form["tercer_pago"]
        }

        archivo_generado = generar_contrato(datos)
        return send_file(archivo_generado, as_attachment=True)

    # Filtra automáticamente los modelos disponibles
    modelos_disponibles = [m for m in MODELOS.keys() if m not in NO_DISPONIBLES]

    return render_template(
    "formulario.html",
    modelos_todos=list(MODELOS.keys()),
    no_disponibles=NO_DISPONIBLES
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


