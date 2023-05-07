from rest_framework.validators import ValidationError

from tags_ingredients.models import Ingredient, Tag


def validate_time(value):
    """Валидация поля модели - время приготовления."""
    if value < 1:
        raise ValidationError(
            ['Время не может быть менее минуты.']
        )


def validate_ingredients(data):
    """Валидация ингредиентов и количества."""
    if not data:
        raise ValidationError('Обязательное поле.')
    if len(data) < 1:
        raise ValidationError('Не переданы ингредиенты.')
    unique_ingredient = []
    for ingredient in data:
        if not ingredient.get('id'):
            raise ValidationError('Отсутствует id ингредиента.')
        id = ingredient.get('id')
        if not Ingredient.objects.filter(id=id).exists():
            raise ValidationError('Ингредиента нет в БД.')
        if id in unique_ingredient:
            raise ValidationError(
                'Нельзя дублировать имена ингредиентов.')
        unique_ingredient.append(id)
        amount = int(ingredient.get('amount'))
        if amount < 1:
            raise ValidationError('Количество не может быть менее 1.')
    return data


def validate_tags(data):
    """Валидация тэгов: отсутствие в request, отсутствие в БД."""
    if not data:
        raise ValidationError('Обязательное поле.')
    if len(data) < 1:
        raise ValidationError('Хотя бы один тэг должен быть указан.')
    for tag in data:
        if not Tag.objects.filter(id=tag).exists():
            raise ValidationError('Тэг отсутствует в БД.')
    return data
