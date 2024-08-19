from odoo import http


class customerSyncAPI(http.Controller):
    @http.route('/hww/customerSyncAPI/', auth='public', website=False, csrf=False, type='json', methods=['GET', 'POST'])
    def customerSyncAPI(self, **kw):

        contact_exists = http.request.env['portal.data'].sudo().search(
            [['email', '=', kw['email']]]).read([])

        if(contact_exists == []):
            response = http.request.env['portal.data'].sudo().create(kw)
        else:
            response = http.request.env['portal.data'].sudo().search(
                [['email', '=', kw['email']]]).write({'name': kw['name']})

        return response
