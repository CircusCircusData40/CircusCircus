from flask import *
from flask_login.utils import login_required
from forum.object_models import *


#VIEWS

@app.route('/')
def index():
	subforums = Subforum.query.filter(Subforum.parent_id == None).order_by(Subforum.id)
	return render_template("subforums.html", subforums=subforums)

@app.route('/subforum')
def subforum():
	subforum_id = int(request.args.get("sub"))
	subforum = Subforum.query.filter(Subforum.id == subforum_id).first()
	if not subforum:
		return error("That subforum does not exist!")
	posts = Post.query.filter(Post.subforum_id == subforum_id).order_by(Post.id.desc()).limit(50)
	if not subforum.path:
		subforum.path = generateLinkPath(subforum.id)

	subforums = Subforum.query.filter(Subforum.parent_id == subforum_id).all()
	return render_template("subforum.html", subforum=subforum, posts=posts, subforums=subforums, path=subforum.path)

@app.route('/loginform')
def loginform():
	return render_template("login.html")


@login_required
@app.route('/addpost')
def addpost():
	subforum_id = int(request.args.get("sub"))
	subforum = Subforum.query.filter(Subforum.id == subforum_id).first()
	if not subforum:
		return error("That subforum does not exist!")

	return render_template("createpost.html", subforum=subforum)

@app.route('/viewpost')
def viewpost():
	postid = int(request.args.get("post"))
	post = Post.query.filter(Post.id == postid).first()
	if not post:
		return error("That post does not exist!")
	if not post.subforum.path:
		subforum.path = generateLinkPath(post.subforum.id)
	comments = Comment.query.filter(Comment.post_id == postid).order_by(Comment.id.desc()) # no need for scalability now
	return render_template("viewpost.html", post=post, path=subforum.path, comments=comments)


def error(errormessage):
	return "<b style=\"color: red;\">" + errormessage + "</b>"

def generateLinkPath(subforumid):
	links = []
	subforum = Subforum.query.filter(Subforum.id == subforumid).first()
	parent = Subforum.query.filter(Subforum.id == subforum.parent_id).first()
	links.append("<a href=\"/subforum?sub=" + str(subforum.id) + "\">" + subforum.title + "</a>")
	while parent is not None:
		links.append("<a href=\"/subforum?sub=" + str(parent.id) + "\">" + parent.title + "</a>")
		parent = Subforum.query.filter(Subforum.id == parent.parent_id).first()
	links.append("<a href=\"/\">Forum Index</a>")
	link = ""
	for l in reversed(links):
		link = link + " / " + l
	return link