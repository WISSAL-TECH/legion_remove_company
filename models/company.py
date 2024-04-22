# -*- coding: utf-8 -*-

import logging
from dateutil.relativedelta import relativedelta
from re import template
from datetime import datetime, timedelta
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ClassResCompany(models.Model):
    _inherit = 'res.company'

    active = fields.Boolean(string="Active", default=True)
