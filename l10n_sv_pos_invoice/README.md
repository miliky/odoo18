# El Salvador - POS Types of DTE Document

## Descripción

Este módulo extiende la funcionalidad del Punto de Venta (POS) de Odoo para generar automáticamente documentos fiscales electrónicos (DTE) según los requerimientos de la Dirección General de Impuestos Internos (DGII) de El Salvador.

## Características principales

- Generación automática de documentos fiscales electrónicos desde el POS
- Asignación automática del tipo de documento según el cliente o posición fiscal
- Generación de números de control y códigos de generación
- Creación automática del JSON DTE al facturar desde POS
- Integración completa con el módulo de tipos de documentos fiscales (l10n_sv_document_type)
- Soporte para facturas de consumidor final, comprobantes de crédito fiscal y notas de crédito

## Requisitos

- Odoo 18.0
- Módulo point_of_sale
- Módulo l10n_sv_document_type

## Instalación

**Nota importante:** Para una instalación limpia, instale primero el módulo **El Salvador - Accounting (l10n_sv_cta)** antes de instalar este módulo.

1. Instale el módulo l10n_sv_cta
2. Instale el módulo l10n_sv_document_type
3. Instale este módulo (l10n_sv_pos_invoice)

## Configuración

1. Configure los establecimientos fiscales en Contabilidad > Configuración > Establecimientos
2. Asigne establecimientos a los usuarios en Usuarios > Preferencias de usuario
3. Configure los tipos de documentos fiscales para sus clientes o posiciones fiscales

## Uso

1. Cree una venta normal en el POS
2. Al facturar, el sistema asignará automáticamente el tipo de documento fiscal según el cliente
3. Se generará automáticamente el JSON DTE y se enviará a la DGII (excepto para notas de crédito que deben procesarse manualmente)

## Soporte

Para soporte técnico, contacte a:

- **Autor:** miliky
- **Mantenedor:** José Emilio Flores Meléndez
- **Sitio web:** https://github.com/miliky/odoo18

## Licencia

LGPL-3