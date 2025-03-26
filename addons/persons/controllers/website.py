import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class PersonsController(http.Controller):
    @http.route("/persons", auth="public", website=True)
    def index(self):
        _logger.info("start processing request..")

        # last 5 recs
        persons = request.env["persons.person"].search([], limit=5, order="create_date desc")

        _logger.info(f"received {len(persons)} recs..")

        return request.render("persons.persons_template", {"persons": persons})

    @http.route("/persons/create", type="http", auth="public", website=True, methods=["POST"], csrf=False)
    def create_person(self, **post):
        _logger.info(f"recieve form data: {post} ..")

        # create new rec
        person = request.env["persons.person"].sudo().create({
            "first_name": post.get("first_name"),
            "last_name": post.get("last_name"),
            "birthday": post.get("birthday"),
            "sex": post.get("sex"),
        })

        _logger.info(f"Created rec: {person.full_name} ..")

        # redirect to list recs
        return request.redirect("/persons")
