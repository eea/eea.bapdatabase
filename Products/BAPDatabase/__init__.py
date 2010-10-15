import BAPDatabase
from App.ImageFile import ImageFile

def initialize(context):
    """ 
        Product initialization method
        @param context: Zope server context 
    """
    context.registerClass(
        BAPDatabase.BAPDatabase,
        constructors = (
            BAPDatabase.manage_add_html,
            BAPDatabase.manage_add_bap),
    )

misc_ = {
    'bap.js':ImageFile('www/js/bap.js', globals()),
    'showLoading.js':ImageFile('www/js/showLoading.js', globals()),
    'ajax-loader.gif':ImageFile('www/ajax-loader.gif', globals()),
    'bullet_orange.png':ImageFile('www/bullet_orange.png', globals()),
    'bullet_blue.png':ImageFile('www/bullet_blue.png', globals()),
    'bullet_red.png':ImageFile('www/bullet_red.png', globals()),
    'up.png':ImageFile('www/up.png', globals()),
    'down.png':ImageFile('www/down.png', globals()),
}