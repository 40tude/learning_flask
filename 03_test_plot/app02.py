# import os
import numpy as np 
import matplotlib.pyplot as plt 
from flask import Flask, render_template 

import io
import base64



app = Flask(__name__) 

# Generate a scatter plot and returns the figure 
def get_plot(): 
	
	data = { 
		'a': np.arange(50), 
		'c': np.random.randint(0, 50, 50), 
		'd': np.random.randn(50) 
	} 
	data['b'] = data['a'] + 10 * np.random.randn(50) 
	data['d'] = np.abs(data['d']) * 100

	plt.scatter('a', 'b', c='c', s='d', data=data) 
	plt.xlabel('X label') 
	plt.ylabel('Y label') 
	
	img = io.BytesIO()
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	
  # convert PNG data to base64 string which can be used directly in HTML
	plot_url = base64.b64encode(img.getvalue())
	#plot_url = base64.b64encode(img.read())
	return plot_url.decode() 

@app.get('/') 
def single_converter(): 
	plot_url = get_plot() 
	return render_template('matplotlib-plot2.html', plot_url=plot_url) 

# Main Driver Function 
if __name__ == '__main__': 
	app.run(debug=True, host="0.0.0.0", port=8080)