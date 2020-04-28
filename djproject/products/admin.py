from django.contrib import admin
from .models import Product


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'featured']
    list_filter = ['price']
    ordering = ('price',)
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}
    list_per_page = 5
    actions = ('set_actions_product', )
    # fields = ('title', 'fields')
    exclude = ['slug', ]

    def set_actions_product(self, request, queryset):
        import pdb; pdb.set_trace()
        self.message_user(request, f"Successfully disabled {count}")
    set_actions_product.short_description = "Disable Featured"

admin.site.site_title = " Application title"
admin.site.site_header = "My Application "
admin.site.index_title = "Admin Operations"
admin.site.register(Product, BlogAdmin)