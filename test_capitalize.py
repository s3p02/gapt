# test_capitalize.py
# Reference: https://www.techiediaries.com/python-unit-tests-github-actions/
def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def test_capitalize_string():
    assert capitalize_string('test') == 'Test'
# trigger action on master
