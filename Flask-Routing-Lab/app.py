from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/shirts")
def shirtsPage():
    return render_template("shirts.html")

@app.route("/pants")
def pantsPage():
    return render_template("pants.html")

@app.route("/sweatshirts")
def sweatshirtsPage():
    return render_template("sweatshirts.html")

@app.route("/socks")
def socksPage():
    return render_template("socks.html")

@app.route("/product")
def productPage():
    return render_template("product.html")

@app.route("/cart")
def gotocart():
    return render_template("cart.html")

@app.route("/added to cart")
def added():
    return render_template("sweatshirt-cart.html")


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
