from website import create_app

# Call the create_app function to initialize the Flask app
app = create_app()

# Run the Flask app if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
