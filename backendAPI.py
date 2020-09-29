from flask import Flask
import gspread, requests, json

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1cJrwFP4VQ6DdQqsfntauj_DqspVGtxYu-iVLx8OYw6s')

app = Flask(__name__)

@app.route('/topHeadlines')
def topHeadlines():
    return json.dumps(sh.worksheet('topHeadlines').get_all_records())

@app.route('/business')
def business():
    return json.dumps(sh.worksheet('business').get_all_records())


@app.route('/entertainment')
def entertainment():
    return json.dumps(sh.worksheet('entertainment').get_all_records())


@app.route('/health')
def health():
    return json.dumps(sh.worksheet('health').get_all_records())


@app.route('/science')
def science():
    return json.dumps(sh.worksheet('science').get_all_records())


@app.route('/sports')
def sports():
    return json.dumps(sh.worksheet('sports').get_all_records())


@app.route('/technology')
def technology():
    return json.dumps(sh.worksheet('technology').get_all_records())


if __name__ == '__main__':
    app.run(debug=True)