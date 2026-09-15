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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00313', methods=['GET'])
	def BenchmarkTest00313_get():
		return BenchmarkTest00313_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00313', methods=['POST'])
	def BenchmarkTest00313_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00313")
		if not param:
			param = ""

		import helpers.ThingFactory
		
		thing = helpers.ThingFactory.createThing()
		bar = thing.doSomething(param)

		import base64
		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00313'[13:]
		user = f'SafeTruman{num}'
		cookie = f'rememberMe{num}'
		value = secrets.token_urlsafe(32)
		issued_tokens = mysession.get(cookie)
		if not isinstance(issued_tokens, set):
			issued_tokens = set()
			legacy_token = mysession.get(cookie)
			if isinstance(legacy_token, str) and legacy_token:
				issued_tokens.add(legacy_token)
			mysession[cookie] = issued_tokens

		if request.cookies.get(cookie) in issued_tokens:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			issued_tokens.add(value)
			RESPONSE += (
				f'{user} has been remembered with cookie:'
				f'{cookie} whose value is: {value}<br/>'
			)

		return RESPONSE
