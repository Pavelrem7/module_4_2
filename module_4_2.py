def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # вызов функции inner_function внутри ифункции test_function. Результат - ничего не возвращает


# inner_function() вызов фкнкции inner_function вне функции test_function. Резудьтат - приводит к ощибке.
test_function()  # Работает
