import BAPDatabase

def initialize(context):
    """ 
        Product initialization method
        @param context: Zope server context 
    """
    context.registerClass(
        BAPDatabase.BAPDatabase,
        constructors = (
            BAPDatabase.manage_add_html,
            BAPDatabase.manage_add),
    )