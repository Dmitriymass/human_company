import json


class Lead():
    person_url = """
        {"full_name": "Joe Doe",
        "job_title": "CEO",
        "profile_url": "https://www.linkedin.com/in/joe",
        "location": "Italy",
        "email": "joe@apple.com",
        "phone_number": "+1-354-489-4801"
        }
    """
    list_of_persons_url = """
    [
        {"full_name": "Joe Doe"
        "profile_url": "https://www.linkedin.com/in/joe"
        },
        {"full_name": "Mike Tyson"
        "profile_url": "https://www.linkedin.com/in/mike"
        },
        {"full_name": "David Stevenson"
        "profile_url": "https://www.linkedin.com/in/david"
        }
    ]
    """

    def get(self, url):
        return json.loads(requests.get(url, headers=headers).text)

    def __init__(self, full_name, job_title, profile_url, location, email, phone_number):
        self.full_name = full_name
        self.job_title = job_title
        self.profile_url = profile_url
        self.location = location
        self.email = email
        self.phone_number = phone_number

    def _format_json(self, input_json, url_type):

        if url_type == "person_url":
            return {
                "full_name": "Joe Doe",
                "job_title": "CEO",
                "profile_url": input_json["profile_url"],
                "location": "Italy",
                "email": "mail@domain.com",
                "phone_number": "+1-354-489-4804"
            }
        elif url_type == "list_of_persons_url":
            return {
                "full_name": "Joe Doe",
                "profile_url": "https://linkedin.com/in/joedoe"
            }


class Company():
    company_url = """
    {
        "name": "Apple",
        "company_url": "https://www.linkedin.com/company/apple",
        "location": "Italy, Roma",
        "revenue": "$365M"
    }
    """
    list_of_companies_url = """
            [
            {
                "name": "Apple",
                "company_url": "https://linkedin.com/company/apple"
            },
            {
                "name": "Facebook",
                "company_url": "https://linkedin.com/company/facebook"
            }
            ]
    """

    def __init__(self, name, company_url, location, revenue):
        self.name = name
        self.company_url = company_url
        self.location = location
        self.revenue = revenue

    def _format_json(self, input_json, url_type):

        if url_type == "person_url":
            return {
                "name": "Joe Doe",
                "company_url": input_json["company_url"],
                "location": "Italy, Roma",
                "revenue": "$365M"
            }
        elif url_type == "list_of_companies_url":
            return {
                "name": "Joe Doe",
                "company_url": "https://linkedin.com/in/joedoe"
            }
