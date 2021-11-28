from custom_logger import CustomLogger


if __name__ == '__main__':

    # demo

    runLogger_info = CustomLogger('run_logger', 'info', 1)
    runLogger_debug = CustomLogger('run_logger', 'debug')

    #### TESTING THE INFO FUNC

    def my_func_info():
        x = 0
        x += 1
        runLogger_info.log_message('Function done.')


    my_func_info()  # success


    #### TESTING THE DEBUG FUNC

    def my_func_debug(x, y):

        try:
            z = x / y
        except ZeroDivisionError:
            runLogger_debug.log_message('Division by zero is not permitted.')
        else:
            runLogger_info.log_message('Division done.')


    my_func_debug(3, 0)  # fail
    my_func_debug(4, 2)  # success


