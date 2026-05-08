from django.urls import path

from .views import (
    lista_pagamentos,
    criar_pagamento
)

urlpatterns = [

    path(
        '',
        lista_pagamentos,
        name='lista_pagamentos'
    ),

    path(
        'novo/',
        criar_pagamento,
        name='criar_pagamento'
    ),
]