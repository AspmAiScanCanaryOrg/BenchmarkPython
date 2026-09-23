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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00640', methods=['GET'])
	def BenchmarkTest00640_get():
		return BenchmarkTest00640_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00640', methods=['POST'])
	def BenchmarkTest00640_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		bar = ''
		if param:
			bar = param.split(' ')[0]

		import secrets
		import time
		from helpers.utils import mysession

		num = 'BenchmarkTest00640'[13:]
		user = f'SafeRandall{num}'
		cookie = f'rememberMe{num}'
		now = int(time.time())
		record = mysession.get(cookie)
		presented = request.cookies.get(cookie)

		if (
			isinstance(record, dict)
			and record.get('token') == presented
			and record.get('user') == user
			and record.get('expires_at', 0) > now
		):
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
			response = make_response(RESPONSE)
		else:
			value = secrets.token_urlsafe(32)
			mysession[cookie] = {
				'token': value,
				'user': user,
				'expires_at': now + 3600,
			}
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)
			response = make_response(RESPONSE)
			response.set_cookie(
				cookie,
				value,
				max_age=3600,
				httponly=True,
				secure=True,
				samesite='Strict',
			)

		return response
