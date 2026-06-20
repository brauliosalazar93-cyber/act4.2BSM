from flask import Flask, render_template
import socket

app = Flask(__name__)
HOST = "172.20.10.2"    ## Ip del servidor
PORT = 12345            ## Puerto del servidor

def leer_sensor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode().strip()
            print("RECIBIDO:", data)
            ejeX, ejeY = data.split(',')
            ejeX = float(ejeX.replace('X:', ''))
            ejeY = float(ejeY.replace('Y:', ''))
            return ejeX, ejeY
    except Exception as e:
        print("ERROR:", e)
        return 0, 0

def celda_4x4(x, y):
    fila = 0 if y >= 0.5 else (1 if y >= 0 else (2 if y >= -0.5 else 3))
    col  = 0 if x < -0.5 else (1 if x < 0 else (2 if x < 0.5 else 3))
    return fila, col

def celda_3x3(x, y):
    fila = 0 if y >= 0.33 else (1 if y >= -0.33 else 2)
    col  = 0 if x < -0.33 else (1 if x <= 0.33 else 2)
    return fila, col

def segmentos_barras(x, y):
    seg_x = 0 if x < -0.5 else (1 if x < 0 else (2 if x < 0.5 else 3))
    seg_y = 0 if y >= 0.5 else (1 if y >= 0 else (2 if y >= -0.5 else 3))
    return seg_x, seg_y

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    ejeY, ejeX = leer_sensor()  ## órden ejes
    fila, col = celda_4x4(ejeX, ejeY)
    return render_template('page1.html', ejeX=ejeX, ejeY=ejeY, fila=fila, col=col)

@app.route('/page2')
def page2():
    ejeY, ejeX = leer_sensor()
    fila, col = celda_3x3(ejeX, ejeY)
    return render_template('page2.html', ejeX=ejeX, ejeY=ejeY, fila=fila, col=col)

@app.route('/page3')
def page3():
    ejeY, ejeX = leer_sensor()
    seg_x, seg_y = segmentos_barras(ejeX, ejeY)
    return render_template('page3.html', ejeX=ejeX, ejeY=ejeY, seg_x=seg_x, seg_y=seg_y)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
