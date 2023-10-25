from django import template
from myapp.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)

    def render_submenu(menu_item):
        submenu_items = MenuItem.objects.filter(menu_name=menu_name, parent=menu_item)

        if submenu_items:
            result = '<ul>'
            for item in submenu_items:
                is_active = current_url == item.url
                result += f'<li {"class=active" if is_active else ""}><a href="{item.url}">{item.title}</a>'
                result += render_submenu(item)
                result += '</li>'
            result += '</ul>'
            return result
        return ''

    menu_html = '<ul>'
    for item in menu_items:
        is_active = current_url == item.url
        menu_html += f'<li {"class=active" if is_active else ""}><a href="{item.url}">{item.title}</a>'
        menu_html += render_submenu(item)
        menu_html += '</li>'
    menu_html += '</ul>'

    return menu_html
