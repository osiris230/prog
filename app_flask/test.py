from flask import Flask
app =  Flask(__name__)

# This is the main route of our application. It will be called when we access the root URL (/)
@app.route('/')
def hello_world():
    return """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mon Blog</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                header {
                    background-color: #333;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                }
                nav {
                    background-color: #f4f4f4;
                    padding: 10px;
                    text-align: center;
                }
                nav a {
                    text-decoration: none;
                    color: #333;
                    padding: 5px 10px;
                }
                nav a:hover {
                    background-color: #ddd;
                }
                .container {
                    width: 80%;
                    margin: auto;
                    padding: 20px;
                }
                footer {
                    background-color: #333;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
            </style>
        </head>
        <body>

        <header>
            <h1>My Blog</h1>
        </header>

        <nav>
            <a href="#">Home</a>
            <a href="#">Articles</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
        </nav>

        <div class="container">
            <h2>Article Title</h2>
            <p>Publication date: April 2nd, 2024</p>
            <p>This is a blog.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus placerat aliquam felis, at hendrerit elit accumsan a. Integer ultricies sagittis ipsum, ac venenatis felis suscipit vel. Donec et quam sit amet urna feugiat ultricies vel at nulla. Aenean ac mi non dui lacinia vestibulum. Sed vitae urna id nisi convallis lobortis a in nunc. Fusce ultrices vitae justo eget rhoncus.</p>
        </div>

        <footer>
            <p>&copy; 2024 Magic Michel's Blog - All rights reserved</p>
        </footer>

        </body>
        </html>
        """