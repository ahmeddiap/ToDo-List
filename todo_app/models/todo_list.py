from odoo import models, fields


class ToDoApp (models.Model):
    _name = 'todo.task'

    Task_name = fields.Char(required=1)
    assign_to_id = fields.Many2one('res.partner')
    description = fields.Text()
    due_date = fields.Date()
    status = fields.Selection([
        ('new', 'New'),
        ('in progress', 'In progress'),
        ('completed', 'Completed'),
    ],)

    def action_new(self):
        for rec in self:
            print("inside new action")
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            print("inside in progress action")
            rec.status = 'in progress'

    def action_completed(self):
        for rec in self:
            print("inside completed action")
            rec.status = 'completed'




