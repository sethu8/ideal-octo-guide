from flask import Flask, render_template, request

app = Flask(__name__)


def decode_message(secret):

    secret = secret.strip()

    if secret == "":
        return ""

    # First word
    first_word = secret.split()[0]

    # Shift value
    shift = len(first_word)

    decoded = ""

    for ch in secret:

        # Keep spaces
        if ch == " ":
            decoded += " "

        # Uppercase
        elif 'A' <= ch <= 'Z':

            value = ord(ch) - ord('A')
            value = (value - shift) % 26

            decoded += chr(value + ord('A'))

        # Lowercase
        elif 'a' <= ch <= 'z':

            value = ord(ch) - ord('a')
            value = (value - shift) % 26

            decoded += chr(value + ord('a'))

        else:
            decoded += ch

    return decoded


@app.route("/", methods=["GET", "POST"])
def home():

    decoded = ""

    if request.method == "POST":

        secret = request.form.get("secret", "")

        decoded = decode_message(secret)

    return render_template("index.html", decoded=decoded)


if __name__ == "__main__":
    app.run(debug=True)
