from django import template
register = template.Library()

@register.filter
def cut_http(value):
    return value[7:-1]

@register.inclusion_tag("tags/greeting.html")
def greeting(request):
    try:
        is_auth = request.user.first_name
    except :
        is_auth = False
    return {
        'is_auth': is_auth,
}
