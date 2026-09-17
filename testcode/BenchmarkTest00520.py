'''
OWASP Benchmark for Python v0.1

This file is part of the Open Web Application Security Project (OWASP) Benchmark Project.
For details, please see https://owasp.org/www-project-benchmark.

The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, version 3.

The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

  Author: Theo Cartsonis
  Created: 2025
'''

import os

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00520', methods=['GET'])
	def BenchmarkTest00520_get():
		return BenchmarkTest00520_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00520', methods=['POST'])
	def BenchmarkTest00520_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00520")
		
		if headers:
			param = headers[0]

		string64527 = 'help'
		string64527 += param
		string64527 += 'snapes on a plane'
		bar = string64527[4:-17]

		import helpers.utils

		fileName = None
		fd = None

		base_dir = os.path.abspath(helpers.utils.TESTFILES_DIR)
		fileName = os.path.abspath(os.path.join(base_dir, bar))

		if os.path.commonpath([base_dir, fileName]) != base_dir:
			RESPONSE += (
				'File name must stay within the test files directory'
			)
			return RESPONSE

		try:
			fd = open(fileName, 'rb')
			RESPONSE += (
				f'The beginning of file: \'{escape_for_html(fileName)}\' is:\n\n'
				f'{escape_for_html(fd.read(1000).decode('utf-8'))}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{{escape_for_html(fileName)}}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE
