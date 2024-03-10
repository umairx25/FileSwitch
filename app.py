import os
from flask import Flask, render_template, request
import convertapi

dest = os.path.expanduser("~\\Downloads")
secret_key = 'XPWjbJ24d3lCXW3c'
convertapi.api_secret = secret_key
app = Flask(__name__)


@app.route("/convert", methods=["POST"])
def convert_file():
    """
    Use the ConvertAPI to convert the user's files to desired format
    """
    input_file = request.files['input_file']
    output_format = request.form['output_format']

    # Save the uploaded file to a temporary location
    input_file_path = os.path.join(dest, input_file.filename)
    input_file.save(input_file_path)

    # Perform the file conversion
    result = convertapi.convert(output_format, {'File': input_file_path})

    # Save the converted file
    output_extension = output_format.strip(".")  # Remove leading dots if any
    result.file.save(f'converted.{output_extension}')

    return "File converted successfully! Please check for converted.{yourextension} in your downloads folder"


@app.route("/")
def index():
    """
    Runs the corresponding html file to display a user interface
    """
    return render_template("test.html")
