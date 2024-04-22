
class Assertions:

    @staticmethod
    def assert_text_element(self, element, expected_text):
        assert element.text == expected_text, "Incorrect text"
