class Calculate:
    def start_calculation(self, expression):
        return self._to_separate(expression)

    def _add(self, number_1, number_2):
        return number_1 + number_2

    def _subtract(self, number_1, number_2):
        return number_1 - number_2

    def _multiply(self, number_1, number_2):
        return number_1 * number_2

    def  _divide(self, number_1, number_2):
        return number_1 / number_2

    def _to_separate(self, expression):
        _array_expression = expression.split()
        print(_array_expression)
       
        return self._precede_operations(_array_expression)

    def _transform_string_to_number(self, value):
        try:
            value = float(value)
            return value
        except ValueError:
            return None

    def _precede_operations(self, _array_expression):
        i = 0
        
        # multiply and divide
        while i < len(_array_expression):
            char = _array_expression[i]

            if char in ['*', '/'] and i > 0 and i < len(_array_expression) - 1:
                previous_char = self._transform_string_to_number(_array_expression[i - 1])
                later_char = self._transform_string_to_number(_array_expression [i + 1])

                match char:
                    case '*':
                        product = self._multiply(previous_char, later_char)

                        _array_expression[i] = product

                        del _array_expression[i + 1]
                        del _array_expression[i - 1]

                        i -= 1

                        print(_array_expression)
                    case '/':
                        quotient = self._divide(previous_char, later_char)

                        _array_expression[i] = quotient

                        del _array_expression[i + 1]
                        del _array_expression[i - 1]

                        i -= 1

                        print(_array_expression)

            i += 1

        i = 0

        # add and subtract
        while i < len(_array_expression):
            char = _array_expression[i]

            if char in ['+', '-'] and i > 0 and i < len(_array_expression) - 1:
                previous_char = self._transform_string_to_number(_array_expression[i - 1])
                later_char = self._transform_string_to_number(_array_expression [i + 1])

                match char:
                    case '+':
                        amount = self._add(previous_char, later_char)

                        _array_expression[i] = amount

                        del _array_expression[i + 1]
                        del _array_expression[i - 1]

                        i -= 1

                        print(_array_expression)
                    case '-':
                        rest = self._subtract(previous_char, later_char)

                        _array_expression[i] = rest
                
                        del _array_expression[i + 1]
                        del _array_expression[i - 1]

                        i -= 1

                        print(_array_expression)

            i += 1

        if len(_array_expression) == 1:
            return _array_expression[0]
        else:
            return _array_expression