from django import template
from django.utils.safestring import mark_safe
from base.refrence import ProcessStatusColor as psc
register = template.Library()

@register.filter(name='addClass')
def addClass(field, cssClass):
  return field.as_widget(attrs={"class":cssClass})

@register.filter(name='genIcon')
def genIcon(appeal):
  icon = 'flag icon'
  for color in psc:
    if color[0] is appeal.process_status:
      return mark_safe('<i class="{} {}"></i>'.format(
              color[1], icon))
  raise StatusNotFoundError('Your status of this appeal "{}" is not found'.format(appeal.process_status))

@register.filter(name='genPrivateTag')
def genPrivateTag(appeal):
  for color in psc:
    if not appeal.is_public:
      return mark_safe('<div class="ui label">私</div>')
  return ''

@register.filter(name='genColor')
def genColor(appeal):
  for color in psc:
    if color[0] is appeal.process_status:
      return color[1]
  raise StatusNotFoundError('Your status of this appeal "{}" is not found'.format(appeal.process_status))

@register.filter(name='inStatus')
def inStatus(appeals, status):
  filter_set = []
  for appeal in appeals:
    if appeal.process_status == status:
      filter_set.append(appeal)
  return filter_set


class StatusNotFoundError(Exception):
  def __init__(self, msg):
    self.msg = msg
  def __str__(self):
    return repr(self.msg)
    pass
