# Computers API with Django

This Django project provides an API to access the computer configurations collected by the Scrapy project. It allows you to retrieve the data as JSON and filter the results based on specific criteria and parameters.

---

# Steps to Start the Project

1. Create a new folder on your local machine where you want to store the project.

2. Open a terminal and navigate to the newly created folder. Clone the project from GitHub using the following command:

    ```git clone https://github.com/BlackRock17/Computers_API.git```

3. After successful cloning, navigate to the project folder:

   ```cd Computers_API```


4. Create a virtual environment (venv) for the project to isolate the dependencies:

   ```python -m venv venv```

5. Then activate the virtual environment:

- For Windows:

    ```venv\Scripts\activate```

- For Unix or MacOS:

    ```source venv/bin/activate```

6. Install the required packages listed in the requirements.txt file:

   ```pip install -r requirements.txt```

7. Open the settings.py file and locate the database settings.
   Set the 'NAME' field to the path of the computers.db file that was created in the spiders folder after running the Scrapy project and collecting the computer configuration data.
   In my case, the database settings look like this:
   
```
   DATABASES = {

       'default': {

           'ENGINE': 'django.db.backends.sqlite3',

           'NAME': 'D:\scrapy_project\Collection_Data_Scrapy\data_collection\data_collection\spiders\computers.db',

       }

   }
```

    However, your path may be different depending on the folders where you store your projects.

8. Start the Django project by running the following command:

   ```python manage.py runserver```

9. You can now access the computer configurations as JSON at the following URLs:

   ```http://localhost:8000/api/computers/``` - Returns all computer configurations.

   ```http://localhost:8000/api/computers/?processor=Intel&ram=8GB``` - Filters configurations by processor and RAM.

   ```http://localhost:8000/api/computers/?processor=AMD&ram=16GB``` - Filters configurations by processor and RAM.

   ```http://localhost:8000/api/computers/?gpu=NVIDIA&motherboard=Intel``` - Filters configurations by GPU and motherboard.

    You can customize the filtering criteria and parameters based on your specific requirements for a computer configuration.

# Notes

1. This issue might be specific to my setup, but I want to share it in case you encounter the same problem.
   When I access http://localhost:8000/api/computers/, everything works as expected, and I get the desired result.
   However, when I try to access http://127.0.0.1:8000/api/computers/, I get an error "OperationalError at /api/computers/". Usually, both URLs should point to the same local server, but in my case, one of them doesn't work.

2. In the views.py file, there is commented code at the bottom of the 'def get_queryset(self):' method. This code can be used for "OR" clauses, while the current implementation uses "AND" clauses by default, as per the task requirements.

### If you have any questions, feel free to contact me via email at lyyubo@gmail.com or by phone at 0895028398.

### Thank you!
