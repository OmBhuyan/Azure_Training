import os

from azure.storage.blob import BlobServiceClient, __version__

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


def folderview(folder, container):
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountombhuyan;AccountKey=n1qicd6RN7+0pnOI8BDubKl1jrbikYbPmMoNNUVtj1zA6Zuzhaj/m0Eowzi8uNcxZF+VEyEbI7YY+AStzCO32g==;EndpointSuffix=core.windows.net"
    """Create the BlobServiceClient object which
    will be used to create a container client"""
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    """Get a client to interact with a specific
    container - though it may not yet exist"""
    container_client = blob_service_client.get_container_client(container)

    filenames = list()
    for blob in container_client.list_blobs(
        name_starts_with=str(folder) + "/"
    ):
        print("Found blob: ", blob.name)
        filenames.append(blob.name)
    return filenames


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/", methods=["POST", "GET"])
def blob_app():
    if request.method == "POST":
        folder = request.form["folder"]
        container = request.form["container"]
        filenames = folderview(folder, container)
        return render_template("data.html", data=filenames)


if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", debug=True)
