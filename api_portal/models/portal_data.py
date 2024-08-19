from odoo import models, fields

class PortalData(models.Model):
    _name = 'portal.data'  # The model name
    _description = 'Portal Data'  # Description of the model

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    sale_dept = fields.Char(string='Sale Department', required=True)
    date = fields.Char(string="Date", required=True)
    profile_name = fields.Char(string="Profile Name",required=True)
    client_user_id = fields.Char(string="Client User ID",required=True)
    client_name = fields.Char(string="Client Name",required=True)
    order_num = fields.Char(string="Order Number",required=True)
    order_link = fields.Char(string="Order Link",required=True)
    remarks = fields.Char(string="Remarks",required=True)
    assigned_team = fields.Char(string="Assigned Team",required=True)
    order_status = fields.Char(string="Order Status",required=True)
    service_lane = fields.Char(string="Service Line",required=True)
    deli_by = fields.Char(string="Delivered By",required=True)
    deli_date = fields.Char(string="Deli Date",required=True)
    deli_amo = fields.Char(string="Deli Amount",required=True)
    deadline = fields.Char(string="Deadline",required=True)
    platform_stat = fields.Char(string="Platform Status",required=True)