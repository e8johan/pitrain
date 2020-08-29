# PiTrain LED Server
# Copyright(C) 2020 Johan Thelin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

@app.route('/api/scenes/start/', methods=['POST'])
def api_scene_start():
    ledserver.start_sequence()
    return '{"status": "ok"}'

if __name__ == '__main__':
    ledserver.start_sequence()
    app.run('0.0.0.0', 8080, True)
