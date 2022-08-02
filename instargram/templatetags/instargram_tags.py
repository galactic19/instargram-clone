from django import template

register = template.Library()


@register.filter(name='is_like')
def is_like_user(post, user):
    return post.like_user_set.filter(pk=user.pk).exists()