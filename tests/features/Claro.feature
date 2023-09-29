@claro
Feature: Home Claro

    @claroservice
    Scenario: Servicio
        Given que un usuario llama al servivio "/api/contentManagement?content=Productos_destacados_spot"
        Then obtiene de respuesta del servicio "200"