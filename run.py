from flask import Flask

print("hello world")

app=Flask(__name__)
app.config['SECRET_KEY'] = "c96418b075871ec41adaea54fee6f4ac"


app.run(debug=True)
