from django import template

register = template.Library()

@register.filter

def str_to_int(my_string):

    my_int = int(my_string)

    return my_int

@register.filter

def tls_num(my_num):

    state = "윷"

    if(my_num==-1):
        state='빽도'

    elif(my_num==1):
        state='도'

    elif(my_num==2):
        state='개'

    elif(my_num==3):
        state='걸'

    elif(my_num==4):
        state='윷'

    elif(my_num==5):
        state='모'

    return state