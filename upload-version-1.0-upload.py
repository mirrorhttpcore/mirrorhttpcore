import base64
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/", methods=["POST"])
def index():
	filename = "%s-version-%s-%s" % (request.form["app_name"], request.form["app_version"], request.form["file_name"])
	file = open(filename, "wb")
	file.write(base64.b64decode(request.form["file_content"].encode("utf-8")))
	file.close()
	return jsonify(ok=True, upload_to=filename)


app.run(host="", port=8384, debug=True)

