import unittest
import requests

class TestWebsite(unittest.TestCase):
    def test_website_load(self):
        url = "https://atg.world/"  
        print(f"Attempting to connect to {url}")
        
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the response status code is 200
        if response.status_code == 200:
            print("Website loaded successfully")
        else:
            print(f"Failed to load website. Status code: {response.status_code}")

            # Print the response text for debugging purposes
            print("Response text:")
            print(response.text)
        
        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200, f"Failed to load website: {url}")

if __name__ == '__main__':
    unittest.main()
