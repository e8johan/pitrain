import ledserver
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/api/led/toggle/<int:ledindex>/', methods=['POST'])
def api_toggle(ledindex):
    ledserver.leds[ledindex].toggle()
    return '{"status": "ok"}'

@app.route('/api/led/on/<int:ledindex>/', methods=['POST'])
def api_on(ledindex):
    ledserver.leds[ledindex].on()
    return '{"status": "ok"}'

@app.route('/api/led/off/<int:ledindex>/', methods=['POST'])
def api_off(ledindex):
    ledserver.leds[ledindex].off()
    return '{"status": "ok"}'

@app.route('/api/all/on/', methods=['POST'])
def api_all_on():
    ledserver.all_on()
    return '{"status": "ok"}'

@app.route('/api/all/off/', methods=['POST'])
def api_all_off():
    ledserver.all_off()
    return '{"status": "ok"}'

@app.route('/api/houses/on/', methods=['POST'])
def api_houses_on():
    ledserver.house_on()
    return '{"status": "ok"}'

@app.route('/api/houses/off/', methods=['POST'])
def api_houses_off():
    ledserver.house_off()
    return '{"status": "ok"}'

@app.route('/api/scene/start/', methods=['POST'])
def api_scene_start():
    ledserver.start_sequence()
    return '{"status": "ok"}'

if __name__ == '__main__':
    ledserver.start_sequence()
    app.run('0.0.0.0', 8080, True)
