from odoo import models, _
import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _create_invoice(self, move_vals):
        invoice = super()._create_invoice(move_vals)

        try:
            invoice.set_document_type_by_partner_or_fiscal_position()
        except Exception as e:
            _logger.exception("No se pudo establecer el tipo de documento fiscal en %s: %s", invoice.name, str(e))

        try:
            invoice.generar_numero_de_control_y_codigo_generacion()
        except Exception as e:
            _logger.exception("No se pudo establecer el número del documento fiscal en %s: %s", invoice.name, str(e))

        try:
            if invoice.country_code == 'SV' and invoice.move_type in ('out_invoice', 'out_refund'):
                if invoice.l10n_sv_document_type != '05':
                    invoice.action_generate_json()
                else:
                    _logger.info("Nota de crédito generada desde POS: JSON debe generarse manualmente.")
        except Exception as e:
            _logger.exception("Error al generar JSON DTE para la factura POS %s: %s", invoice.name, str(e))

        return invoice
