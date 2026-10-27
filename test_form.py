
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(
            any(f.get("id") == "registrationForm"
                for f in self.parser.forms),
            "Registration form not found"
        )

    def test_required_input_fields_exist(self):
        fields = {
            field.get("name"): field
            for field in self.parser.inputs
        }

        self.assertIn("name", fields)
        self.assertIn("email", fields)
        self.assertIn("contact", fields)

        self.assertEqual(fields["name"].get("type"), "text")
        self.assertEqual(fields["email"].get("type"), "email")
        self.assertEqual(fields["contact"].get("type"), "tel")

    def test_fields_are_required(self):
        fields = {
            field.get("name"): field
            for field in self.parser.inputs
        }

        for name in ["name", "email", "contact"]:
            self.assertIn(
                "required",
                fields[name],
                f"{name} field must be required"
            )

    def test_submit_button_exists(self):
        self.assertTrue(
            any(button.get("type") == "submit"
                for button in self.parser.buttons),
            "Submit button not found"
        )


if __name__ == "__main__":
    unittest.main()
