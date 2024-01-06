from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.requirement"
    _description = "Requirement"    
    name = fields.Char("Title")
    description = fields.Text("Description")
    parent_id = fields.Many2one("mgmt.requirement", "Hierarchy")
    compliancestatement_ids = fields.One2many("mgmt.compliancestatement", "requirement_id",
        string="Compliancestatements",)        
    paragraph_ids = fields.Many2many("mgmt.paragraph", 
        string="Paragraphs")   
    paragraph_name = fields.Char(
        string="Paragraph",
        related="paragraph_ids.name")

    @api.onchange('description')
    def _onchange_description(self):
        if self.description and not self.name:
            self.name = self.description[:40] + '...'