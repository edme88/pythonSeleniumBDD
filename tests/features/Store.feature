@Store
Feature: Home Store

    @Store1
    Scenario: Cambio de pestaña
        Given que un usuario está en la página "Store"
        When hace click en el icono de "facebook"
        Then se redirecciona a "https://www.facebook.com/"

    @Store2
    Scenario: Login
        Given que un usuario está en la página "Store"
        When presiona el boton "Login or register" del header
        And completa usuario, password y presiona el boton de Login
        Then se verifica que el titulo es "MY ACCOUNT"