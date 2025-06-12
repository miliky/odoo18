# Módulo de Generación de Documentos Fiscales Electrónicos para El Salvador (DTE)
## Descripción
Este módulo permite generar, firmar y transmitir documentos fiscales electrónicos (DTE) en formato JSON para El Salvador, cumpliendo con los requisitos establecidos por el Ministerio de Hacienda y la Dirección General de Impuestos Internos (DGII). Facilita todo el ciclo de vida de los documentos fiscales electrónicos, desde su creación hasta su almacenamiento, conforme a la normativa salvadoreña vigente.

Implementa la integración completa con los servicios web de la DGII para la validación y transmisión de documentos, permitiendo a las empresas cumplir con sus obligaciones fiscales de manera eficiente y automatizada dentro del ecosistema de Odoo.

## Características principales
- Generación de archivos JSON para diferentes tipos de documentos fiscales:
  
  - Facturas de Consumidor Final (FCF)
  - Comprobantes de Crédito Fiscal (CCF)
  - Notas de Crédito (NCE)
  - Facturas de Sujeto Excluido (FSEE)
  - Comprobantes de Crédito Fiscal para Exportación (CCFE)
  - Documentos de Anulación (AN)
- Firma electrónica de documentos mediante servicio externo configurable
- Transmisión automática a los servidores de la DGII
- Almacenamiento automático de los documentos JSON como adjuntos
- Visualización del JSON generado directamente en la factura
- Gestión de contingencias para situaciones donde no hay conexión con DGII
- Anulación de documentos fiscales electrónicos con validación de plazos legales
- Generación de notas de crédito para devoluciones parciales o totales
- Generación de códigos QR para verificación de documentos
- Personalización de reportes de facturación con información DTE
## Dependencias
Este módulo depende de los siguientes módulos:

- account : Módulo base de contabilidad de Odoo
- l10n_sv_cta : Catálogo de cuentas para El Salvador
- l10n_sv_uom : Unidades de medida para El Salvador
- l10n_sv_incoterms : Términos de comercio internacional para El Salvador
- l10n_sv_payment : Términos y formas de pago para El Salvador
- l10n_sv_city : Gestión de ciudades/distritos para El Salvador
- l10n_latam_sv : Localización base para El Salvador
- l10n_sv_fiscal_positions : Posiciones fiscales para El Salvador
- l10n_sv_document_type : Tipos de documentos fiscales para El Salvador
## Configuración
### Configuración de la empresa
1. Vaya a Ajustes > Usuarios y Empresas > Empresas
2. Seleccione su empresa
3. Vaya a la pestaña Facturación Electrónica SV
4. Configure los siguientes campos:
   - Ambiente DGII : Seleccione "Pruebas" o "Producción"
   - Tipo de Transmisión : Normal o Contingencia
   - Tipo de Establecimiento : Casa Matriz, Sucursal, etc.
   - Contraseña DGII : Contraseña para autenticación en el portal API de DGII
   - URL del servicio de firma : URL del servicio para la firma electrónica
   - Contraseña para firma electrónica : Contraseña para la firma electrónica
5. Haga clic en Probar Conexión DGII para verificar la configuración
### Configuración de establecimientos
1. Vaya a Contabilidad > Configuración > Establecimientos Autorizados
2. Configure los establecimientos y puntos de venta autorizados por el Ministerio de Hacienda
3. Asigne los códigos correspondientes:
   - Código de establecimiento
   - Código de establecimiento MH
   - Código de punto de venta
   - Código de punto de venta MH
### Asignación de establecimientos a usuarios
1. Vaya a Ajustes > Usuarios y Empresas > Usuarios
2. Seleccione un usuario
3. En la pestaña Preferencias , sección Configuración El Salvador , asigne el establecimiento autorizado correspondiente
## Uso
### Generación de documentos fiscales electrónicos
1. Cree una factura normalmente en Odoo
2. Valide la factura
3. Haga clic en el botón Generar JSON y enviar a DGII
4. El sistema generará el archivo JSON, lo firmará electrónicamente y lo enviará a DGII
5. El documento se guardará como adjunto y se mostrará en la pestaña Datos JSON
### Anulación de documentos fiscales
1. Abra un documento fiscal electrónico ya generado
2. Utilice la opción de anulación estándar de Odoo
3. Se abrirá el asistente de anulación con las siguientes opciones:
   - Anulación completa : Disponible dentro de los plazos legales (24 horas para CCF, 3 meses para FCF)
   - Nota de crédito : Para devoluciones parciales o totales fuera del plazo de anulación
4. Indique el motivo de anulación
5. Confirme la acción
### Consulta de documentos fiscales electrónicos
1. Vaya a Contabilidad > Clientes > Documentos Fiscales Electrónicos
2. Visualice todos los documentos fiscales electrónicos generados
3. Para cada documento, puede consultar su estado, sello de recepción y JSON generado
## Soporte técnico
Para soporte técnico, contacte a:

- Autor : miliky
- Mantenedor : José Emilio Flores Meléndez
- Sitio web : https://github.com/miliky/odoo18
## Licencia
Este módulo está licenciado bajo LGPL-3.