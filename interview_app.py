from flask import Flask, jsonify, request
import os
import pickle
app = Flask(__name__)

# we need to add a route(2 actually)
# a route for the homepage

@app.route('/', methods=["GET"])

def index():
    # need to return content and response code
    return "<h1>Welcome to my App!!</h1>",200

# a route for predict
@app.route("/predict",methods=["GET"])
def predict():
    level = request.args.get("level",'')
    lang = request.args.get("lang",'')
    tweets = request.args.get("tweet",'')
    phd = request.args.get("phd",'')
    print("level:",level)
    print("lang:",lang)
    print("tweets:",tweets)
    print("phd:",phd)


    prediction = predict_interviews_well([level,lang,tweets,phd])
    if prediction is not None:
        result = {
        "prediction": prediction
    }
        return jsonify(result),200
    else:
        return "Error making prediction", 400

    
    
    

def predict_interviews_well(instance):
    infile = open('tree.p','rb')
    header, interview_tree = pickle.load(infile)
    print('header: ', header)
    print('interview tree: ', interview_tree)
    infile.close()
    try:
        return tdidt_classifier(interview_tree,header,instance)
    except:
        return None

def tdidt_classifier(tree, header, instance):
    info_type = tree[0]
    if info_type == "Attribute":
        attribute = tree[1]
        attribute_index = header.index(attribute)
        test_value = instance[attribute_index]
        for i in range(2,len(tree)):
            value_list = tree[i]
            if value_list[1] == test_value:
                return tdidt_classifier(value_list[2], header, instance)
    else:
        leaf_label = tree[1]
        return leaf_label



if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0",port=port)