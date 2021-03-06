"""
Unit tests for the Person class
"""

# import code to be tested
from person import Person


def describe_a_person():
    def that_has_a_first_name_and_last_name():
        alice = Person("Alice", "Alison", "alice@example.com")
        assert alice.first_name == "Alice"
        assert alice.last_name == "Alison"
        assert alice.email == "alice@example.com"
