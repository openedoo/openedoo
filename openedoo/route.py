from openedoo import app

from openedoo.core import core
app.register_blueprint(core, url_prefix='/')

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

from modules.module_coba import module_coba
app.register_blueprint(module_coba, url_prefix='/module_coba')