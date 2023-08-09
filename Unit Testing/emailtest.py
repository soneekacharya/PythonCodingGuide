""" Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure there are no no disposable email providers 
    such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and invalid addresses 
    (Use unittest module). """

import unittest
import re

def validate_email(email):
    valid_providers = ['yahoo.com', 'gmail.com', 'outlook.com']
    disposable_providers = ['yopmail.com', 'example.com', 'mailinator.com']

    if '@' not in email or ' ' in email:
        return False

    _, domain = email.split('@', 1)
    if domain in valid_providers and domain not in disposable_providers:
        return True
    return False

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            'user@yahoo.com',
            'john@gmail.com',
            'mary@outlook.com'
        ]
        for email in valid_emails:
            self.assertTrue(validate_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            'user@yopmail.com',
            'invalid-email',
            'noatsymbol.com'
        ]
        for email in invalid_emails:
            self.assertFalse(validate_email(email))

if __name__ == '__main__':
    unittest.main()
