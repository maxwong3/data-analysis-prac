from bs4 import BeautifulSoup
import requests

amazon_url = 'https://www.amazon.com/Skechers-Stamina-Cutback-Lace-Up-Charcoal/dp/B00VR5QGOG/ref=sr_1_56?crid=AGMVPWBFH9BP&dib=eyJ2IjoiMSJ9.SJoJ5XRXDcsTUlxBVbT-Rk0GJgvjU3eaUHCNaTR5DQjFc980C33L7wY9SLw3k4QKYS9E3JMyzxiAhWJv-ko59Q6zMyj8ex3VfXHTXLem8s_EVlYpVvvlgmbzXCl_Mn8Qy1t6aslma66AWTk-rRhKN3mvn-IoD80RRuV9mTettIJHO_BIsBLiAgsICi0wn-P0OTwiwx_nd3wdONjc9ynUNdfCvwV0X00BUEKqhmAGkFy6O8UARtricmXRIQYTo8SdcpLG46rrsKaHs7Fh1CRJQa6PqUZVBatS3qK-5Foo4gY.WBsG6uXi1nGU_8r-UCsCL5uBYn6m0MgsTSc0twirugQ&dib_tag=se&keywords=mens%2Bshoes%2Bskechers&qid=1749586677&sprefix=mens%2Bshoes%2Bskechers%2Caps%2C102&sr=8-56&th=1&psc=1'

response = requests.get(amazon_url)

html = response.text