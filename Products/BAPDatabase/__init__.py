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
}