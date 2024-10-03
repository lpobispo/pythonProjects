# align html tags in a single line

import re

def minify_html(html_content):
    # Remove newlines, tabs, and extra spaces between tags
    minified_html = re.sub(r">\s+<", "><", html_content)  # Removes spaces between tags
    minified_html = minified_html.replace('\n', '').replace('\t', '').strip()  # Removes newlines and tabs
    return minified_html

# Example HTML content
html_content = """
<html>
    <head>
        <title>502 bad gateway</title>
    </head>
    <body>
        <center><h1>502 gateway</h1></center>
        <hr><center>123123123123123</center>
    </body>
</html>
"""

# Call the function
one_line_html = minify_html(html_content)

# Output the result
print(one_line_html)