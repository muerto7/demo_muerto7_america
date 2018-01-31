# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)
class DemoOdoo11(models.Model):
    _name = 'demo.odoo.11'

    texto = fields.Char(string='Texto Demo')