from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def resume():
    resume_data = {
        "name": "Aakriti kumari",
        "email": "aakritikumari130@gmail.com",
        "phone": "+919279996309",
        "summary": "A passionate Python developer with strong backend and web development skills.",
        "skills": ["Python", "Flask", "HTML", "CSS",  "Git"],
       
    }

    return render_template("resume.html", **resume_data)

if __name__ == "__main__":
    app.run(debug=True)