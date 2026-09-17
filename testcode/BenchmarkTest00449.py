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

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00449', methods=['GET'])
	def BenchmarkTest00449_get():
		return BenchmarkTest00449_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00449', methods=['POST'])
	def BenchmarkTest00449_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00449")
		if not param:
		    param = ""

		bar = param

		import helpers.utils
		import os

		try:
			base_dir = os.path.realpath(helpers.utils.TESTFILES_DIR)
			safe_name = os.path.basename(bar)
			if safe_name != bar or safe_name in ('', '.', '..'):
				raise IOError('Invalid file name')
			fileName = os.path.realpath(os.path.join(base_dir, safe_name))
			if os.path.commonpath([base_dir, fileName]) != base_dir:
				raise IOError('Invalid file path')
			with open(fileName, 'wb') as fd:
				RESPONSE += (
					f'Now ready to write to file: {escape_for_html(fileName)}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE
