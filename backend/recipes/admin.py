from django.contrib import admin

from recipes.models import Favorite, IngredientAmount, Recipe, ShoppingCart
from tags_ingr.models import Ingredient, Tag


class IngredientAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Ingredient."""
    list_display = (
        'pk',
        'name',
        'measurement_unit',
    )
    list_editable = ('name', 'measurement_unit')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Tag."""
    list_display = (
        'pk',
        'name',
        'color',
        'slug',
    )
    list_editable = ('name', 'color', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Recipe."""
    list_display = (
        'pk',
        'name',
        'author',
        'image',
        'count_added'
    )
    exclude = ('ingredients',)
    inlines = (IngredientAmountInline,)
    list_filter = ('author', 'name', 'tags')
    search_fields = ('author__username', 'name', 'tags__name')
    empty_value_display = '-пусто-'

    def count_added(self, obj):
        return obj.favorite.count()


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'ingredient',
        'amount',
    )
    search_fields = ('recipe__name', 'ingredient__name')


class FavoriteShoppingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe'
    )
    search_fields = ('user__username', 'recipe__name')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteShoppingAdmin)
admin.site.register(ShoppingCart, FavoriteShoppingAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
