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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00751', methods=['GET'])
	def BenchmarkTest00751_get():
		return BenchmarkTest00751_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00751', methods=['POST'])
	def BenchmarkTest00751_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00751")
		param = ""
		if values:
			param = values[0]

		bar = ""
		if param:
			lst = []
			lst.append('safe')
			lst.append(param)
			lst.append('moresafe')
			lst.pop(0)
			bar = lst[0]

		import os
		import helpers.utils
		fileName = ''

		try:
			base_dir = os.path.abspath(helpers.utils.TESTFILES_DIR)
			candidate = os.path.abspath(os.path.join(base_dir, bar))
			if not bar or os.path.isabs(bar) or os.path.commonpath([base_dir, candidate]) != base_dir:
				raise IOError(0, 'Invalid file path')
			fileName = candidate
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
