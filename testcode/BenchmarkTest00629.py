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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00629', methods=['GET'])
	def BenchmarkTest00629_get():
		return BenchmarkTest00629_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00629', methods=['POST'])
	def BenchmarkTest00629_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		bar = "This should never happen"
		if 'should' in bar:
			bar = param

		import secrets
		import time
		from helpers.utils import mysession

		num = 'BenchmarkTest00629'[13:]
		user = f'SafeRobbie{num}'
		cookie = f'rememberMe{num}'
		value = secrets.token_urlsafe(32)
		client_key = (
			cookie,
			request.remote_addr or '',
			request.headers.get('User-Agent', ''),
		)
		stored = mysession.get(client_key)
		remembered = False

		if isinstance(stored, dict):
			stored_value = stored.get('value')
			stored_expires_at = stored.get('expires_at')
			request_cookie = request.cookies.get(cookie)
			if (
				isinstance(stored_value, str)
				and isinstance(stored_expires_at, (int, float))
				and isinstance(request_cookie, str)
				and request_cookie == stored_value
				and stored_expires_at > time.time()
			):
				remembered = True

		if remembered:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
			resp = make_response(RESPONSE)
		else:
			mysession[client_key] = {
				'value': value,
				'expires_at': time.time() + (60 * 60 * 24 * 30),
			}
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)
			resp = make_response(RESPONSE)
			resp.set_cookie(
				cookie,
				value,
				max_age=60 * 60 * 24 * 30,
				httponly=True,
				secure=request.is_secure,
				samesite='Lax',
			)

		return resp
