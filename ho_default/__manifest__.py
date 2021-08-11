##############################################################################
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'ho',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Customizacion para Herramientas del oeste",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/cl-ho',
    'license': 'AGPL-3',
    'depends': [
        'standard_depends_ce',
		
		'website',
		'website_crm',
		'website_crm_sms',
		'website_sms',
		'website_sale',
		'website_form',
		'website_links',
		'website_mail',
		# faltan
		'website_sale_ux',
		#faltan
		'website_blog',
			
		'stock',
		'crm',
     ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    'port': '8069',

    'git-repos': [
        'https://github.com/jobiols/cl-ho.git',
        'https://github.com/jobiols/odoo-jeo-ce.git',

		# Repositorio privado del tema utilizado por José Romero
        # ==========================================================
		'https://github.com/sebatista/HO_teme_laze.git theme_laze',

        # Adhoc para localizacion
        # ==========================================================
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/miscellaneous',
        'https://github.com/ingadhoc/sale',
        'https://github.com/ingadhoc/product',
        'https://github.com/ingadhoc/argentina-sale',
        'https://github.com/ingadhoc/account-payment',
        'https://github.com/ingadhoc/stock',
    
        # OCA para localizacion
        # ==========================================================
        'https://github.com/oca/web',        

        # ADHOC Otros repositorios adicionales
        # ==========================================================
        'https://github.com/ingadhoc/website',
        'https://github.com/ingadhoc/partner',
        'https://github.com/ingadhoc/account-invoicing',

        # OCA Otros repositorios adicionales
        # ==========================================================
        'https://github.com/oca/partner-contact',
        'https://github.com/oca/sale-workflow',
        'https://github.com/oca/server-ux',
        'https://github.com/oca/contract',
        'https://github.com/oca/social',
        'https://github.com/oca/stock-logistics-workflow.git',
		'https://github.com/OCA/server-tools',
		
        # Odoomates
        # ==========================================================
        'https://github.com/odoomates/odooapps odoomates-odooapps',
		
		# Moldeo
        # ==========================================================
		'https://github.com/ctmil/payment_mercadopago',

        # Gabriela Rivero
        # ==========================================================
        'https://github.com/regaby/odoo-custom regaby-odoo-custom',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx',
    ]
}
