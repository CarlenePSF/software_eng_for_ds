# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['text_analyzer.py', 'my_package2.py'])

# Print result of PEP 8 style check
print(result.messages)