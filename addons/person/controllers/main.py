from odoo import http
from odoo.http import request
import os
import json


class PersonController(http.Controller):

    @http.route("/persons/", type="http", auth="public", website=True)
    def persons_page(self, **kwargs):
        module_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
        html_file_path = os.path.join(module_path, "static", "src", "html", "people.html")

        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        return http.Response(html_content, content_type="text/html")

    @http.route('/persons/data/', type='http', auth='public', website=True, methods=['GET'])
    def persons_data(self, **kwargs):
        try:
            persons = request.env['person.person'].search([], limit=5, order='id desc')
            data = [{
                'full_name': person.full_name,
                'sex': person.sex or '',
                'age': person.age or '',
                'company': person.company_id.name
            } for person in persons]
            return http.Response(json.dumps(data), content_type='application/json')
        except Exception as e:
            return http.Response(json.dumps({'error': str(e)}), status=500, content_type='application/json')

    @http.route("/persons/create_form/", type="http", auth="public", website=True)
    def create_person_form(self, **kwargs):
        module_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
        html_file_path = os.path.join(module_path, "static", "src", "html", "create_person.html")

        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        return http.Response(html_content, content_type="text/html")

    @http.route('/person/create/', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def create_person(self, **kwargs):

        try:
            required_fields = ['first_name', 'last_name', 'company_id']
            user_data = json.loads(request.httprequest.data.decode('utf-8'))
            for field in required_fields:
                if not user_data.get(field):
                    return http.Response(
                        json.dumps({'error': f'Missing required field: {field}'}),
                        status=400,
                        content_type='application/json'
                    )

            values = {
                'first_name': user_data.get('first_name'),
                'last_name': user_data.get('last_name'),
                'company_id': int(user_data.get('company_id')),
                'birthday': user_data.get('birthday') or False,
                'sex': user_data.get('sex') or False,
            }

            new_person = request.env['person.person'].create(values)
            return http.Response(
                json.dumps({
                    'success': True,
                    'person': {
                        'id': new_person.id,
                        'full_name': new_person.full_name,
                        'age': new_person.age,
                        'sex': new_person.sex or '',
                        'company': new_person.company_id.name
                    }
                }),
                content_type='application/json'
            )
        except Exception as e:
            return http.Response(
                json.dumps({'error': str(e)}),
                status=500,
                content_type='application/json'
            )

    @http.route('/api/companies/', type='http', auth='public', methods=['GET'], csrf=False)
    def get_companies(self, **kwargs):
        try:

            companies = request.env['res.company'].search_read(
                domain=[],
                fields=['id', 'name'],
                limit=100
            )

            response_data = {
                'result': companies
            }

            return http.Response(
                json.dumps(response_data),
                status=200,
                mimetype='application/json'
            )
        except Exception as e:
            error_response = {
                'error': {
                    'code': 500,
                    'message': str(e),
                    'data': {
                        'name': 'Exception',
                        'debug': str(e)
                    }
                }
            }
            return http.Response(
                json.dumps(error_response),
                status=500,
                mimetype='application/json'
            )
