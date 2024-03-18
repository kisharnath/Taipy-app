from taipy.gui import Gui
import taipy as tp


from pages.root import root
from pages.country.country import country_md
pages = {
    '/':root,
    'country': country_md
    
    
}


gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="Earth quake ",use_reloader=True)