from app import create_app

app = create_app()

@app.route('/')
def home():
    return "Welcome to the Contact App API!"  

if __name__ == "__main__":
    app.run(debug=True)
