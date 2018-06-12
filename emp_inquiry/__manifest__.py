{
    'name':'emp_inquiry',
    'description':'Employee Inquiry Form.',
    'version':'1.0',
    'summary':'Employee Management  ',
    'category':'website-apps',
    'website':'www.bistasolution.com',
    'author':'Bista solutions',
    'depends':['base','website'],
    'data':[
        'views/website_view.xml',
        'views/inquiry_view.xml',
        'data/default_config_data.xml',
    ],
    'installable':True,
    'auto-install':False,
    'application':False,
}