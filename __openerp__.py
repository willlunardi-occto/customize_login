{
    'name': 'Customize Login Page',
    'version': '1.0',
	'description': "Este módulo customiza a tela de login do OpenERP",
    'category': 'web',
    'complexity': "easy",
    'description': """
Este módulo irá alterar a página de login.
=================
Alteração da homepage de login, logotipo e algumas propriedades CSS.

    """,
    'author': 'OCCTO',
    'website': 'http://www.occto.com.br',
    'installable': True,
    'active': False,
	'depends': ['web'],
    'qweb' : [
        "static/src/base.xml",
    ],
	'css': [
		"static/src/css/login.css",
	],
}