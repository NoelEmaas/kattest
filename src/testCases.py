import re
import sys
import requests
from bs4 import BeautifulSoup


def parse_test_cases(raw_test_cases):
    test_cases = []
    raw_test_cases = list(map(str, raw_test_cases))

    for i in range(0, len(raw_test_cases), 2):
        input_text = re.search(r"<pre>(.*?)</pre>", raw_test_cases[i], re.DOTALL).group(1)
        output_text = re.search(r"<pre>(.*?)</pre>", raw_test_cases[i + 1], re.DOTALL).group(1)

        test_case = {
            'input' : input_text.strip(),
            'output' : output_text.strip()
        }

        test_cases.append(test_case)
    
    return test_cases


def get_test_cases(url):
    response = requests.get(url, data={'script' : 'true'})
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    test_cases = soup.find_all('pre')

    search_phrase = 'Sample Input'
    has_test_cases = soup.find_all(text=lambda text: text and search_phrase.lower() in text.lower())
    
    if has_test_cases:
        test_cases = parse_test_cases(test_cases)
    else:
        sys.exit('This problem does not provide sample test cases.')


    return test_cases
