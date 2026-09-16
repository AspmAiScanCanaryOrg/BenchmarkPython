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

from flask import redirect, url_for, request, make_response, render_template, session
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/weakrand-01/BenchmarkTest00318', methods=['GET'])
	def BenchmarkTest00318_get():
		return BenchmarkTest00318_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00318', methods=['POST'])
	def BenchmarkTest00318_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00318")
		if not param:
			param = ""

		import helpers.utils
		bar = helpers.utils.escape_for_html(param)

		import random

		num = 'BenchmarkTest00318'[13:]
		user = f'SafeRandall{num}'
		cookie = f'rememberMe{num}'
		session_key = f'{cookie}_value'
		value = str(random.SystemRandom().random())[2:]

		if session.get(session_key) and request.cookies.get(cookie) == session.get(session_key):
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
			response = make_response(RESPONSE)
		else:
			session[session_key] = value
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)
			response = make_response(RESPONSE)
			response.set_cookie(cookie, session[session_key], httponly=True, samesite='Lax')

		return response
