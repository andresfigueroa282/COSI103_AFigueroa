from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

'''% APIKEY: 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'''

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <li> <a href="{url_for('gptdemo')}">Ask questions to GPT</a> </li>
        <li> <a href="{url_for('about')}">About</a> </li>
        <li> <a href="{url_for('team')}">Team Members</a> </li>
        <li> <a href="{url_for('andresgpt')}">Andres GPT</a> </li>
    '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        <a href={url_for('index')}> Home</a>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>About</h1>
        <hr>
        <a href="{url_for('index')}">Home</a>
        <hr>
        <br><br>
        <h2>Summary:<h2>
        <p style="font-size: 14px;"> This is a web application created with Flask. The program makes use of prompt engineering, a method for producing relevant answers to specific questions or prompts by using predefined prompts or inputs. Andres Figueroa is the application's creator. The application's goal is to give users useful and educational answers to their inquiries based on the prompts or inputs they provide. </p>
        
    '''

@app.route('/team')
def team():
    ''' display a link to the team page '''
    print('processing / route')
    return f'''
        <h1>Team Members</h1>
        <hr>
        <a href="{url_for('index')}">Home</a>
        <hr>
        <br><br>
        <h2>Andres Figueroa:<h2>
        <p style="font-size: 14px;">Andres Figueroa is a Computer Science major at Brandeis. He is interested in software development and web development. He is also interested in artificial intelligence and machine learning.</p>    '''

@app.route('/andresgpt')
def andresgpt():
    ''' display a link to Andres's page '''
    print('processing / route')
    if request.method == 'POST':
        animal = request.form['animal']
        answer = gptAPI.andres(animal)
        return f'''
        <h1>AndresGPT Demo</h1>
        <pre style="bgcolor:yellow">{"What can a " + str(animal) + " not do?"}</pre>
        <hr>
        <div style="border:thin solid black">{answer}</div>
        <hr>
        <br><br>
        <a href={url_for('index')}>Home</a>
        <a href={url_for('andresgpt')}>Reload AndresGPT</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        What can a {insert animal} not do?
        <form method="post">
            <textarea name="animal"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)