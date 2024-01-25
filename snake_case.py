def snake_case(text):
    if isinstance(text, int):
        return str(text)
    snake = ""
    for i in str(text):
        if i.isupper():
            snake += "_" + i
        else:
            snake += i
    return snake[1:].casefold()


# tests:
assert snake_case("HelloWorld") == "hello_world", "Should be hello_world"
assert snake_case("TestController") == "test_controller", "Should be test_controller"
assert snake_case("MoviesAndBooks") == "movies_and_books", "Should be movies_and_books"
assert snake_case("App7Test") == "app7_test", "Should be app7_test"
assert snake_case(1) == "1", "Should be 1"
