from flask import Flask, render_template, request
import os
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator


from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('OPENAI_API_KEY')

app = Flask(__name__)
loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['user_query']
    result = index.query(user_query)
    return render_template('result.html', user_query=user_query, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)