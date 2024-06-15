# Book Recommendation

## Introduction
Welcome to the Book Recommendation repository! This project is built using Django, a powerful Python web framework, and Neo4j, an advanced graph database management system. The project is contained within a virtual environment to ensure that dependencies are managed effectively.
   - <img width="1470" alt="Screenshot 2024-06-15 at 23 59 36" src="https://github.com/sysbr0/send_email/assets/112288155/01f15f8d-7cba-4d8b-b959-123f467b8595">

This Book Recommendation project requires users to create an account to access its features. Once registered, users will be presented with a selection of random books fetched from the Neo4j database. Clicking on a book will display detailed information about it, and the system will record the book's ID, category ID, and the average age of users who rated the book.

![Screenshot 2024-06-16 at 00 09 38](https://github.com/sysbr0/send_email/assets/112288155/bcefea85-c949-45f6-8402-a3e4bf555e57)


Based on this interaction, the home page will show personalized book recommendations for the user, alongside recommendations from other users. Additionally, three charts will display statistics about the user's reading preferences, helping to predict the types of books they might be interested in.

## Table of Contents
1. [Introduction](#introduction)
   - Overview of the project and its purpose

2. [Installation](#installation)
   - Step-by-step guide to setting up the project locally
3. [Usage](#usage)
   - Instructions on how to use the project and its features
4. [Features](#features)
   - List of key features and functionalities
5. [Contributing](#contributing)
   - Guidelines for contributing to the project
6. [License](#license)
   - Information about the project's license
7. [Acknowledgements](#acknowledgements)
   - Credits to those who have contributed or inspired the project

## Installation

### Prerequisites
- Python (>=3.6)
- Django (specified in `requirements.txt`)
- Neo4j (hosted online)
- Virtualenv

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sysbr0/Book-Recomandition.git
    cd Book-Recomandition
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure your Django settings:**
    - Update the `DATABASES` setting in `settings.py` to connect to your online Neo4j database.
    - Example configuration:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.dummy',
        },
        'neo4j': {
            'ENGINE': 'django_neomodel',
            'HOST': 'bolt://<username>:<password>@<your-neo4j-host>:<port>',
        }
    }
    ```
    - Replace `<username>`, `<password>`, `<your-neo4j-host>`, and `<port>` with your Neo4j connection details.

6. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

8. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
Once the server is running, you can access the application at `http://127.0.0.1:8000/`. Create an account and log in to explore the features:
- **Random Books:** View random book suggestions from the Neo4j database.
- **Book Details:** Click on a book to see detailed information and record the interaction.
- **Personalized Recommendations:** Get book recommendations based on your recorded interactions.
- **Other Users' Recommendations:** See what books other users recommend.
- **User Statistics:** View charts showing your reading preferences and book interests.

## Features
- User registration and authentication
- Random book display from Neo4j database
- Detailed book information view
- Recording user interactions with books
- Personalized book recommendations
- Display of other users' recommendations
- User statistics and reading preference charts

## Contributing
We welcome contributions! To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes tests where applicable.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
We would like to thank the Django and Neo4j communities for their excellent tools and support.
