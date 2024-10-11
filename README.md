List of libraries to install in order:
Selenium: pip install selenium
Webdriver Manager: pip install webdriver-manager
pytest: pip install pytest
pytest-html: pip install pytest-html
(optional) msedge-selenium-tools: pip install msedge-selenium-tools

Additional notes:
Edge Browser: Make sure you have Microsoft Edge installed on your computer since we are using Edge in this example.
WebDriver for Edge: webdriver-manager will automatically download the appropriate version of WebDriver (EdgeDriver), so you don't need to do it manually.
Project folders: Ensure that your project structure is correct, with pages, tests, and possibly reports folders if they haven't been created yet.
How to run everything:
Install all the above libraries in your virtual or global environment (e.g., in venv).
Make sure your project structure is correct (with pages, tests folders).
Run the test with the command:
bash

pytest --html=reports/raport_kryptochart.html --self-contained-html
After the tests are completed, check the generated HTML report in the reports folder.
By following these steps, Selenium tests will run according to your code, and reports will be generated automatically.
