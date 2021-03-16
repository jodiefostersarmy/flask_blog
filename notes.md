# Notes about Flask

- When Flask projects get bigger, it doesn't make sense to keep all the code in one mammoth file.
- Python projects use _packages_ to organize code into multiple modules that can be imported where needed.

- A Flask application is an instance of the Flask class. 
    - Config and URLS will be registered with this class.

- When creating a large application that uses the Flask instance, you will need to create it inside a function, which is known as the **application factory**.
    - config, registration and other setup will need to be applied within the factory.

- A view function is the code you write to respond to the requests to your application. Flask uses patterns to match the incoming request URL to the view that should handle it. The view returns data that Flask turns into an outgoing response. Flask can also go the other direction and generate a URL to a view based on its name and arguments.

Q: What is a Blueprint?
A: A Blueprint is a way to organize a group of related views and other code.
 - for example: This blog we are creating, we are going to create a Blueprint for the authentication functions and one for the blog posts functions.

 