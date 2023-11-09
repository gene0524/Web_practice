from flask import Flask, render_template, request, redirect, url_for
from githubapi import GitHubUser, GitHubUserRepo, GitHubRepo

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route("/")  # 函式的裝飾(Decorator)： 以函式為基礎，提供附加的功能
def home():
    return render_template("index.html")


@app.route("/test")  # 當網站連接到根目錄底下的test路徑，執行test函式
def test():
    return "This is a test."


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    return process_query(q)


if __name__ == "__main__":
    app.run(debugger=True)


##########################################

@app.route("/github/form")
def github_form():
    return render_template("githubform.html")


@app.route("/github/form/submit", methods=["POST"])
def github_form_submit():
    input_username = request.form.get("username")
    return redirect(url_for("github_user", username=input_username))


@app.route("/github/<username>")
def github_user(username):
    user = GitHubUser(username)
    followers_count = user.getFollowersCount()
    following_count = user.getFollowingCount()
    userRepo = GitHubUserRepo(username)
    repo_list = userRepo.getRepoLists()
    # The commits_list will contains a 2D list of each repo
    commits_list = []
    for reponame in userRepo.getRepoName():
        repo = GitHubRepo(reponame)
        commits_list.append(repo.getRepoCommitsLists())
    return render_template(
        "greet.html",
        username=username,
        followers=followers_count,
        following=following_count,
        repos=repo_list,
        commits=commits_list,
    )


@app.route("/github/<username>/followers")
def github_user_followers(username):
    user = GitHubUser(username)
    followers, avatar_urls = user.getFollowers()
    return render_template(
        "githubfollowers.html",
        username=username,
        followers=followers,
        avatar_urls=avatar_urls,
    )


@app.route("/github/<username>/following")
def github_user_following(username):
    user = GitHubUser(username)
    following, avatar_urls = user.getFollowing()
    return render_template(
        "githubfollowing.html",
        username=username,
        following=following,
        avatar_urls=avatar_urls,
    )