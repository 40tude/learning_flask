# import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template
import io
import base64

app = Flask(__name__)


# Generate a scatter plot and returns the figure
def get_plot_as_string():
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

    # img = io.StringIO()
    img = io.BytesIO()

    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)

    # convert PNG data to base64 string which can be used directly in HTML
    # plot_bytes = base64.b64encode(img.read())            # read() or getvalue() can be used. read is lower level ?
    plot_bytes = base64.b64encode(img.getvalue())          # convert to base64 as bytes
    plot_str = plot_bytes.decode()                         # Decode the bytes using the codec, return str
    return plot_str


@app.get("/")
def single_converter():
    plot_str = get_plot_as_string()
    return render_template("matplotlib-plot2.html", plot_url=plot_str)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
