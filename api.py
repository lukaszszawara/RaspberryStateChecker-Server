from flask import Flask
import subprocess
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello :)'
@app.route('/temp/')
def temp():
        return "{\"temp\":"+subprocess.getoutput("cat /sys/devices/virtual/thermal/thermal_zone0/temp")+",\"datetime\":\""+str(datetime.now())+"\",\"sysInfo\":\"{"+subprocess.getoutput("screenfetch -n -N")+"}\",\"hdd\":\"{" +subprocess.getoutput("df -h | grep ^/dev")+"\}\",\"who\":\"{"+subprocess.getoutput("who")+"}\"}"
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
