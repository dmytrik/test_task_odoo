from odoo import http
import json

class PersonController(http.Controller):
    @http.route("/people/", type="http", auth="public", website=True)
    def persons_page(self, **kwargs):
        return http.request.render("person.people_html")
