{
    'name': 'Cloth Exchange - ReWear',
    'version': '1.0',
    'summary': 'Community clothing exchange system with swapping and point redemption.',
    'description': """ 
        ReWear - A sustainable clothing exchange platform.
        Users can list items, request swaps, or redeem via points.
        Includes admin moderation and user dashboard.
    """,
    'category': 'Website',
    'author': 'The Falcon Team',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/item_views.xml',
        'views/user_details_views.xml',
        # 'views/swap_request_view.xml',
    ],
 

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}