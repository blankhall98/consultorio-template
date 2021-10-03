from flask import Flask, render_template
app = Flask(__name__)

Info = {
    'nombre': 'Berl',
    'apellido': 'Blank',
    'especialidad': 'Ortopedia y Traumatología',
    'consultorio': [
        {
            'nombre': 'Hospital Amerimed',
            'direccion': 'Torre Médica, a un costado de las Ámericas',
            'telefono': ['9988454383'],
            'horarios': [{'dia':'Lunes','horario':['16:00','19:00']},
            {'dia':'miercoles','horario':['16:00','19:00']}]
        },
        {
            'nombre':'Clinica Venados',
            'direccion': 'Torre Médica, a un costado de las Ámericas',
            'telefono': ['9988454383'],
            'horarios': [{'dia':'Lunes','horario':['16:00','19:00']},
            {'dia':'miercoles','horario':['16:00','19:00']}]
        }],
    'alma_mater': 'Universidad Nacional Autónoma de México',
    'resumen_general': 'Revisión y tratamiento de huesos, articulaciones, tendones, ligamentos y músculos.'
}

@app.route('/')
def index():
    return render_template('index.html',Info = Info)

if __name__ == '__main__':
    app.run()
 