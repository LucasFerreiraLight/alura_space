from django.contrib import admin
from apps.galeria.models import Fotografia

class listandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "publicada",)

    list_display_links = ("id", "nome", "legenda")

    search_fields = ("nome",)

    list_filter = ("categoria", "usuario")

    list_editable = ("publicada",)

    list_per_page = 10

    



    #search_fields = ["nome"]
 
    



admin.site.register(Fotografia, listandoFotografias)



