from django.urls import path

from applications.security.views.auth import signin, signout
from applications.security.views.menu import MenuCreateView, MenuDeleteView, MenuListView, MenuUpdateView
from applications.security.views.module import ModuleCreateView, ModuleDeleteView, ModuleListView, ModuleUpdateView
from applications.security.views.usuario import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from applications.security.views.groupModulePermission import GroupModulePermissionListView, GroupModulePermissionCreateView, GroupModulePermissionUpdateView, GroupModulePermissionDeleteView 


app_name='security' # define un espacio de nombre para la aplicacion
urlpatterns = [
  
  #  usuarios
  
  path('usuario_list/', UsuarioListView.as_view(), name='usuario_list'),
  path('usuario_create/', UsuarioCreateView.as_view(),name="usuario_create"),
  path('usuario_update/<int:pk>/', UsuarioUpdateView.as_view(),name='usuario_update'),
  path('usuario_delete/<int:pk>/', UsuarioDeleteView.as_view(),name='usuario_delete'),
  
  #  grupos de permisos
  path('group_module_permission_list/', GroupModulePermissionListView.as_view(), name="group_module_permission_list"),
  path('group_module_permission_create/', GroupModulePermissionCreateView.as_view(), name="group_module_permission_create"),
  path('group_module_permission_update/<int:pk>/', GroupModulePermissionUpdateView.as_view(), name='group_module_permission_update'),
  path('group_module_permission_delete/<int:pk>/', GroupModulePermissionDeleteView.as_view(), name='group_module_permission_delete'),

  #  modulos
  path('module_list/',ModuleListView.as_view() ,name="module_list"),
  path('module_create/', ModuleCreateView.as_view(),name="module_create"),
  path('module_update/<int:pk>/', ModuleUpdateView.as_view(),name='module_update'),
  path('module_delete/<int:pk>/', ModuleDeleteView.as_view(),name='module_delete'),

#  menus
  path('menu_list/',MenuListView.as_view() ,name="menu_list"),
  path('menu_create/', MenuCreateView.as_view(),name="menu_create"),
  path('menu_update/<int:pk>/', MenuUpdateView.as_view(),name='menu_update'),
  path('menu_delete/<int:pk>/', MenuDeleteView.as_view(),name='menu_delete'),

  # autenticacion
  path('logout/', signout, name='signout'),
  path('signin/', signin, name='signin'),
  #path('signup/', signup, name='signup'),
]