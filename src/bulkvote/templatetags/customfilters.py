from django import template

register = template.Library()

@register.filter
def getcount(item, choice):
    """returns the number of times choice has been selected for item"""
    return item.userchoices.filter(choice=choice).count()


@register.filter
def getuniqueitems(userchoices):
    """return a list of unique items given a bunch of userchoices"""
    items = []
    for userchoice in userchoices:
        if userchoice.item not in items:
            items.append(userchoice.item)
    return items


@register.filter
def getzerochoiceitems(items, choice):
    """return a list of unique items where the given choice has been chosen zero times"""
    returnitems = []
    for item in items:
        if item.userchoices.filter(choice=choice).count()==0:
            if item not in returnitems:
                returnitems.append(item)
    return returnitems

