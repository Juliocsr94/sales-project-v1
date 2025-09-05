from django.urls import path
from .views import listar_produtos, cadastrar_produto, editar_produto, remover_produto, vender_produto

urlpatterns = [
    path("", listar_produtos, name="listar_produtos"),
    path("cadastrar/", cadastrar_produto, name="cadastrar_produto"),
    path("editar/<int:id>/", editar_produto, name="editar_produto"),
    path("remover/<int:id>/", remover_produto, name="remover_produto"),
    path("vender/<int:id>/", vender_produto, name="vender_produto"),
]
