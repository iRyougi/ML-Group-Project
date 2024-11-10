# 可以用这份代码爬取数据集
# 爬取目标 https://www.runoob.com/python/python-100-examples.html

import os
import requests
from bs4 import BeautifulSoup

def crawl_website(url, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through link names from "Python 练习实例1" to "Python 练习实例100"
    for i in range(3, 101):
        link_text = f"Python 练习实例{i}"
        print(f"Looking for link: {link_text}")

        # Send a GET request to the website
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the link with the specified text
        link = soup.find('a', string=link_text)
        if link:
            href = link.get('href')
            if not href.startswith('http'):
                href = url + href  # Ensure the URL is complete
            print(f"Processing link: {href}")
            link_response = requests.get(href)
            if link_response.status_code == 200:
                link_soup = BeautifulSoup(link_response.content, 'html.parser')
                example_codes = link_soup.find_all("div", {"class": "example_code"})
                
                if example_codes:
                    example_code = example_codes[-1]  # Select the last div with the class 'example code'
                    print("Example code found.")
                    # Save the content to a file with a numbered filename


                    content = example_code.get_text().replace('\xa0', ' ').replace('&nbsp;', ' ') 
                    # Save the content to a file with a numbered filename 
                    filename = os.path.join(output_folder, f"exercise_{i}.py") 
                    with open(filename, 'w', encoding='utf-8') as file: 
                        file.write(content)
                    print(f'Saved content to {filename}')
                else:
                    print("No example code found.")
            else:
                print(f"Failed to access {href}, status code: {link_response.status_code}")
        else:
            print(f"Link with text '{link_text}' not found.")

# Example usage
crawl_website('https://www.runoob.com/python/python-100-examples.html', './数据集/Data')
