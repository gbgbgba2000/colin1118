#載入pymongo 元件
from pymongo.mongo_client import MongoClient
from flask import request
#from bson.objectid import ObjectId #載入objectid
uri = "mongodb+srv://colin:colinkokoko688@mycluster.pwngzeb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.member

#初始化 flask server
from flask import*
app=Flask(__name__,
          static_folder="static",
          static_url_path="/")
app.secret_key="123456"
#建立首頁route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "user" in session:
      return render_template("member.html")
    else:
      return redirect("/") 
@app.route("/signup",methods=["POST"])
def signup():
    nickname=request.form["nickname"]
    account=request.form["account"]
    password=request.form["password"]
    #success_msg=db.member.find({"name"})
    collection=db.user
    account_data=collection.find_one({"account":account})
    if account_data !=None:
       return redirect("/error?msg=註冊失敗，帳號已被註冊過")
    else:
       collection.insert_one({"name":nickname,
                              "account":account,
                              "password":password})
       return render_template("successed.html",name=nickname,account=account)
@app.route("/signin",methods=["POST"])
def signin():  
    account=request.form["account"]
    password=request.form["password"]
    collection=db.user
    result_data=collection.find_one({"$and":[
                                    {"account":account},
                                     {"password":password}
                                     ]
                                     }) 
    if result_data ==None:
       return redirect("/error?msg=登入失敗 account or password 錯誤")
       #資料庫撈出會員姓名 存入session
    session["user"]=result_data["name"]
       #return render_template("member.html",name=result_data["nickname"])
    return redirect("/member")
       
@app.route("/signout")
def signout():
    del session["user"]       
    return render_template("index.html")        
@app.route("/error")
def error():
    error_msg=request.args.get("msg","登入錯誤，請洽客服人員")
    return render_template("error.html",message=error_msg)
app.run(port=3000)

