from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import requests
import json
from flask import Flask, request, abort, send_file

responseJson = ""
app = Flask(__name__)

def getMinput(graph):
    updatedGraph = graph.strip().replace(" ", "%20")
    #print(updatedGraph)
    
    r = requests.get('https://api.wolframalpha.com/v2/query?appid=LL5K8H-LHX2KVGWHK&input=plot%20' + updatedGraph + '&format=minput&includepodid=3DPlot&output=json')
    #print(r.json())
    jsonDict = r.json()
    return jsonDict["queryresult"]["pods"][0]["subpods"][0]["minput"]

def sendToEchoar():
    url = "https://console.echoAR.xyz/upload"
    payload={'key': 'broken-darkness-6663',
    'email': 'possiblyiswarren@gmail.com',
    'target_type': '2',
    'hologram_type': '2',
    'type': 'upload'}
    files=[
      ('file_model',('graph.obj',open('C:\\Users\\Richard\\Desktop\\Wolfram Echoar stuff\\graph.obj','rb'),'application/obj')),
      ('file_model',('graph.mtl',open('C:\\Users\\Richard\\Desktop\\Wolfram Echoar stuff\\graph.mtl','rb'),'application/mtl'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    responseJson = json.loads(response.text)
    print("Go to this website: " + responseJson["additionalData"]["shortURL"])
    return responseJson["additionalData"]["shortURL"]



'''
session = WolframLanguageSession('E:\\Wolfram\\WolframKernel.exe')
try:
    
    graph = input("Input the equation you would like to plot: ")
    print("Now what should the range be (only put the number):")
    xmin = input("X min: ")
    xmax = input("X max: ")
    ymin = input("Y min: ")
    ymax = input("Y max: ")
    print("Loading...")
    
    minput = getMinput(graph)
    justPlot = minput[0:minput.find("{x")]
    #print('Export["test.obj", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + "}]]")
    #print('Export["test.obj", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + '}, PerformanceGoal -> "Quality", ColorFunction -> Function[{x, y, z}, Hue[.65 (1 - z)]]]]')
    
                  
    session.evaluate(wlexpr('Export["test.ply", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + '}, PerformanceGoal -> "Quality", ColorFunction -> Function[{x, y, z}, Hue[.65 (1 - z)]]]]'))
    #print("did it")
    sendToEchoar()
    
    
    
except Exception as e:
    print(e)
finally:
    session.stop()
'''


@app.route("/test", methods=['POST', 'GET'])
def webhook2():
    return send_file('error.html')

@app.route("/equation", methods=['POST', 'GET'])
def webhook():
    
    session = WolframLanguageSession('E:\\Wolfram\\WolframKernel.exe')
    try:
        graph = request.form['equation']
        xmin = request.form['xmin']
        xmax = request.form['xmax']
        ymin = request.form['ymin']
        ymax = request.form['ymax']

        print("Loading...")
        
        minput = getMinput(graph)
        justPlot = minput[0:minput.find("{x")]
        #print('Export["test.obj", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + "}]]")
        #print('Export["test.obj", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + '}, PerformanceGoal -> "Quality", ColorFunction -> Function[{x, y, z}, Hue[.65 (1 - z)]]]]')
        
                      
        session.evaluate(wlexpr('Export["graph.obj", ' + justPlot + "{x, " + xmin.strip() + ", " + xmax.strip() + "}, {y, " + ymin.strip() + ", " + ymax.strip() + '}, PerformanceGoal -> "Quality", ColorFunction -> Function[{x, y, z}, Hue[.65 (1 - z)]]]]'))
        #print("did it")
        redirect = sendToEchoar()
        f = open("redirect.html", 'w')
        f.write('''
                
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
                <meta http-equiv="refresh" content="0; URL=''' + "'" + redirect + "'" + '''" />
            <title>Loading...</title>
          </head>
          <body>
            Loading...
          </body>
        </html>
        ''')
        f.close()
        return send_file('redirect.html')
        
                
        
    except Exception as e:
        print(e)
        return send_file('error.html')
        
    finally:
        session.stop()
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')

