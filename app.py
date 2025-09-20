# # from flask import Flask, render_template, request, jsonify, session, redirect, url_for
# # from pymongo import MongoClient
# # from assistant import ask_perplexity
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = Flask(__name__)
# # app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# # # MongoDB setup
# # client = MongoClient(os.getenv("MONGO_URI"))
# # db = client.get_database("ai_assistant")
# # users_collection = db.get_collection("users")
# # chats_collection = db.get_collection("chats")

# # from flask import send_from_directory

# # @app.route('/favicon.ico')
# # def favicon():
# #     return send_from_directory('static', 'Assistant.png', mimetype='image/png')

# # @app.route('/')
# # def home():
# #     if 'user_id' in session:
# #         return render_template('chat.html')
# #     return redirect(url_for('login'))

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         password = request.form['password']
# #         user = users_collection.find_one({"email": email, "password": password})
# #         if user:
# #             session['user_id'] = str(user['_id'])
# #             return redirect(url_for('home'))
# #         return "Invalid credentials"
# #     return render_template('login.html')

# # @app.route('/signup', methods=['GET', 'POST'])
# # def signup():
# #     if request.method == 'POST':
# #         name = request.form['name']
# #         father_name = request.form['father_name']
# #         email = request.form['email']
# #         password = request.form['password']
# #         users_collection.insert_one({
# #             "name": name,
# #             "father_name": father_name,
# #             "email": email,
# #             "password": password
# #         })
# #         return redirect(url_for('login'))
# #     return render_template('signup.html')

# # @app.route('/logout')
# # def logout():
# #     session.pop('user_id', None)
# #     return redirect(url_for('login'))

# # @app.route('/ask', methods=['POST'])
# # def ask():
# #     user_msg = request.json.get('message')
# #     reply = ask_perplexity(user_msg)

# #     if 'user_id' in session:
# #         user_id = session['user_id']
# #         chats_collection.insert_one({
# #             "user_id": user_id,
# #             "user_message": user_msg,
# #             "bot_response": reply
# #         })

# #     return jsonify({'reply': reply})

# # if __name__ == "__main__":
# #     app.run(debug=True)

# # # from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
# # # from pymongo import MongoClient
# # # from assistant import ask_perplexity
# # # from werkzeug.security import generate_password_hash, check_password_hash
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # app = Flask(__name__)
# # # app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# # # # MongoDB setup
# # # client = MongoClient(os.getenv("MONGO_URI"))
# # # db = client.get_database("ai_assistant")
# # # users_collection = db.get_collection("users")
# # # chats_collection = db.get_collection("chats")

# # # @app.route('/favicon.ico')
# # # def favicon():
# # #     return send_from_directory('static', 'Assistant.png', mimetype='image/png')

# # # @app.route('/')
# # # def home():
# # #     print("SESSION DATA:", dict(session))  # Debug log
# # #     if 'user_id' in session:
# # #         return render_template('chat.html')
# # #     return redirect(url_for('login'))

# # # @app.route('/login', methods=['GET', 'POST'])
# # # def login():
# # #     if request.method == 'POST':
# # #         email = request.form['email']
# # #         password = request.form['password']

# # #         user = users_collection.find_one({"email": email})
# # #         print("USER FOUND:", user)

# # #         if user and check_password_hash(user['password'], password):
# # #             session['user_id'] = str(user['_id'])
# # #             print("SESSION AFTER LOGIN:", dict(session))
# # #             return redirect(url_for('home'))
# # #         return "Invalid credentials"
# # #     return render_template('login.html')

# # # @app.route('/signup', methods=['GET', 'POST'])
# # # def signup():
# # #     if request.method == 'POST':
# # #         name = request.form['name']
# # #         father_name = request.form['father_name']
# # #         email = request.form['email']
# # #         password = request.form['password']

# # #         hashed_pw = generate_password_hash(password)  # ✅ Hash password
# # #         users_collection.insert_one({
# # #             "name": name,
# # #             "father_name": father_name,
# # #             "email": email,
# # #             "password": hashed_pw
# # #         })
# # #         return redirect(url_for('login'))
# # #     return render_template('signup.html')

# # # @app.route('/logout')
# # # def logout():
# # #     session.pop('user_id', None)
# # #     return redirect(url_for('login'))

# # # @app.route('/ask', methods=['POST'])
# # # def ask():
# # #     user_msg = request.json.get('message')
# # #     reply = ask_perplexity(user_msg)

# # #     if 'user_id' in session:
# # #         user_id = session['user_id']
# # #         chats_collection.insert_one({
# # #             "user_id": user_id,
# # #             "user_message": user_msg,
# # #             "bot_response": reply
# # #         })

# # #     return jsonify({'reply': reply})

# # # if __name__ == "__main__":
# # #     app.run(debug=True)

# # # # from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
# # # # from pymongo import MongoClient
# # # # from assistant import ask_perplexity
# # # # from werkzeug.security import generate_password_hash, check_password_hash
# # # # import os
# # # # from dotenv import load_dotenv

# # # # load_dotenv()

# # # # app = Flask(__name__)
# # # # app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# # # # # MongoDB setup
# # # # client = MongoClient(os.getenv("MONGO_URI"))
# # # # db = client.get_database("ai_assistant")
# # # # users_collection = db.get_collection("users")
# # # # chats_collection = db.get_collection("chats")

# # # # @app.route('/favicon.ico')
# # # # def favicon():
# # # #     return send_from_directory('static', 'Assistant.png', mimetype='image/png')

# # # # @app.route('/')
# # # # def home():
# # # #     print("SESSION DATA:", dict(session))  # Debug log
# # # #     if 'user_id' in session:
# # # #         # Get user email for the template
# # # #         user = users_collection.find_one({"_id": session['user_id']})
# # # #         user_email = user['email'] if user else None
# # # #         return render_template('chat.html', user_email=user_email)
# # # #     return redirect(url_for('login'))

# # # # @app.route('/chat')
# # # # def chat():
# # # #     if 'user_id' not in session:
# # # #         return redirect(url_for('login'))
    
# # # #     # Get user email for the template
# # # #     user = users_collection.find_one({"_id": session['user_id']})
# # # #     user_email = user['email'] if user else None
# # # #     return render_template('chat.html', user_email=user_email)

# # # # @app.route('/login', methods=['GET', 'POST'])
# # # # def login():
# # # #     if request.method == 'POST':
# # # #         email = request.form['email']
# # # #         password = request.form['password']

# # # #         user = users_collection.find_one({"email": email})
# # # #         print("USER FOUND:", user)

# # # #         if user and check_password_hash(user['password'], password):
# # # #             session['user_id'] = str(user['_id'])
# # # #             session['user_email'] = email  # Store email in session too
# # # #             print("SESSION AFTER LOGIN:", dict(session))
            
# # # #             # Redirect to home page which will render chat.html with user_email
# # # #             return redirect(url_for('home'))
# # # #         else:
# # # #             # Return login page with error message
# # # #             return render_template('login.html', error="Invalid credentials"), 401
    
# # # #     return render_template('login.html')

# # # # @app.route('/signup', methods=['GET', 'POST'])
# # # # def signup():
# # # #     if request.method == 'POST':
# # # #         name = request.form['name']
# # # #         father_name = request.form['father_name']
# # # #         email = request.form['email']
# # # #         password = request.form['password']

# # # #         # Check if user already exists
# # # #         if users_collection.find_one({"email": email}):
# # # #             return render_template('signup.html', error="Email already exists")

# # # #         hashed_pw = generate_password_hash(password)
# # # #         users_collection.insert_one({
# # # #             "name": name,
# # # #             "father_name": father_name,
# # # #             "email": email,
# # # #             "password": hashed_pw
# # # #         })
# # # #         return redirect(url_for('login'))
    
# # # #     return render_template('signup.html')

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.clear()  # Clear all session data
# # # #     return redirect(url_for('login'))

# # # # @app.route('/ask', methods=['POST'])
# # # # def ask():
# # # #     if 'user_id' not in session:
# # # #         return jsonify({'error': 'Not authenticated'}), 401
        
# # # #     user_msg = request.json.get('message')
# # # #     reply = ask_perplexity(user_msg)

# # # #     user_id = session['user_id']
# # # #     chats_collection.insert_one({
# # # #         "user_id": user_id,
# # # #         "user_message": user_msg,
# # # #         "bot_response": reply
# # # #     })

# # # #     return jsonify({'reply': reply})

# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
# from pymongo import MongoClient
# from werkzeug.security import generate_password_hash, check_password_hash
# from bson.objectid import ObjectId
# import os
# from dotenv import load_dotenv
# import requests
# import json

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# # MongoDB setup
# try:
#     client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
#     db = client.get_database("ai_assistant")
#     users_collection = db.get_collection("users")
#     chats_collection = db.get_collection("chats")
    
#     # Test connection
#     client.admin.command('ismaster')
#     print("MongoDB connected successfully!")
    
# except Exception as e:
#     print(f"MongoDB connection error: {e}")
#     # Fallback to in-memory storage for development
#     users_collection = None
#     chats_collection = None

# # Simple AI response function (replace with your actual AI integration)
# def ask_ai(message):
#     """
#     Replace this with your actual AI integration
#     This is a simple fallback response
#     """
#     try:
#         # Example responses based on keywords
#         message_lower = message.lower()
        
#         if any(word in message_lower for word in ['hello', 'hi', 'hey']):
#             return "Hello! How can I help you today?"
#         elif any(word in message_lower for word in ['python', 'code', 'programming']):
#             return """Here's a simple Python example:

# ```python
# def greet(name):
#     return f"Hello, {name}!"

# # Usage
# print(greet("World"))
# ```

# This function takes a name parameter and returns a greeting. Python is great for beginners because of its readable syntax!"""
#         elif 'weather' in message_lower:
#             return "I don't have access to real-time weather data, but I'd recommend checking a reliable weather service for current conditions in your area."
#         elif any(word in message_lower for word in ['story', 'write', 'creative']):
#             return """Here's a short story:

# **The Digital Garden**

# In the year 2045, Maya discovered an old computer in her grandmother's attic. When she powered it on, she found a simple text-based program called "Digital Garden." As she typed words, they bloomed into virtual flowers on the screen. Each word she wrote made the garden more beautiful.

# Years later, Maya realized the true magic wasn't in the program, but in how writing had transformed her thoughts into something beautiful and lasting."""
#         else:
#             return f"""I understand you're asking about: "{message}"

# I'm here to help with a variety of topics including:
# - **Explanations** of concepts and ideas
# - **Creative writing** and storytelling  
# - **Code help** and programming questions
# - **Planning and advice** for various tasks
# - **General questions** and conversation

# Could you provide more details about what specifically you'd like to know or discuss?"""
            
#     except Exception as e:
#         print(f"AI response error: {e}")
#         return "I apologize, but I'm having trouble processing your request right now. Could you please try again?"

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/')
# def home():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
#     return render_template('chat.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         try:
#             email = request.form.get('email', '').strip().lower()
#             password = request.form.get('password', '')
            
#             if not email or not password:
#                 return jsonify({'error': 'Email and password are required'}), 400
            
#             if users_collection is not None:
#                 user = users_collection.find_one({"email": email})
#                 if user and check_password_hash(user['password'], password):
#                     session['user_id'] = str(user['_id'])
#                     session['user_email'] = user['email']
#                     session['user_name'] = user['name']
#                     return redirect(url_for('home'))
            
#             return jsonify({'error': 'Invalid credentials'}), 401
            
#         except Exception as e:
#             print(f"Login error: {e}")
#             return jsonify({'error': 'Server error occurred'}), 500
    
#     # If user is already logged in, redirect to home
#     if 'user_id' in session:
#         return redirect(url_for('home'))
        
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         try:
#             name = request.form.get('name', '').strip()
#             father_name = request.form.get('father_name', '').strip()
#             email = request.form.get('email', '').strip().lower()
#             password = request.form.get('password', '')
            
#             # Validate inputs
#             if not all([name, father_name, email, password]):
#                 return jsonify({'error': 'All fields are required'}), 400
            
#             if len(password) < 6:
#                 return jsonify({'error': 'Password must be at least 6 characters'}), 400
            
#             if '@' not in email or '.' not in email:
#                 return jsonify({'error': 'Invalid email format'}), 400
            
#             if users_collection is not None:
#                 # Check if user already exists
#                 if users_collection.find_one({"email": email}):
#                     return jsonify({'error': 'Email already registered'}), 409
                
#                 # Hash password before storing
#                 hashed_password = generate_password_hash(password)
                
#                 # Insert new user
#                 result = users_collection.insert_one({
#                     "name": name,
#                     "father_name": father_name,
#                     "email": email,
#                     "password": hashed_password
#                 })
                
#                 if result.inserted_id:
#                     return jsonify({'message': 'Account created successfully'}), 201
            
#             return jsonify({'error': 'Failed to create account'}), 500
            
#         except Exception as e:
#             print(f"Signup error: {e}")
#             return jsonify({'error': 'Server error occurred'}), 500
    
#     # If user is already logged in, redirect to home
#     if 'user_id' in session:
#         return redirect(url_for('home'))
        
#     return render_template('signup.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))

# @app.route('/ask', methods=['POST'])
# def ask():
#     # Check if user is logged in
#     if 'user_id' not in session:
#         return jsonify({'error': 'Not authenticated'}), 401
    
#     try:
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
            
#         user_msg = data.get('message', '').strip()
#         if not user_msg:
#             return jsonify({'error': 'Message is required'}), 400
        
#         # Get AI response
#         reply = ask_ai(user_msg)
        
#         # Save chat to database
#         if chats_collection is not None:
#             try:
#                 chats_collection.insert_one({
#                     "user_id": session['user_id'],
#                     "user_message": user_msg,
#                     "bot_response": reply,
#                     "timestamp": ObjectId().generation_time
#                 })
#             except Exception as e:
#                 print(f"Error saving chat: {e}")
        
#         return jsonify({'reply': reply})
        
#     except Exception as e:
#         print(f"Chat error: {e}")
#         return jsonify({'error': 'Failed to process message'}), 500

# @app.route('/chat-history')
# def chat_history():
#     if 'user_id' not in session:
#         return jsonify({'error': 'Not authenticated'}), 401
    
#     try:
#         if chats_collection is not None:
#             chats = list(chats_collection.find(
#                 {"user_id": session['user_id']},
#                 {"_id": 0, "user_message": 1, "bot_response": 1, "timestamp": 1}
#             ).sort("timestamp", -1).limit(50))
#             return jsonify({'chats': chats})
#         return jsonify({'chats': []})
#     except Exception as e:
#         print(f"Chat history error: {e}")
#         return jsonify({'error': 'Failed to fetch chat history'}), 500

# @app.route('/user-info')
# def user_info():
#     if 'user_id' not in session:
#         return jsonify({'error': 'Not authenticated'}), 401
    
#     return jsonify({
#         'user_id': session.get('user_id'),
#         'email': session.get('user_email'),
#         'name': session.get('user_name')
#     })

# # Error handlers
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return jsonify({'error': 'Internal server error'}), 500

# if __name__ == "__main__":
#     # Create indexes for better performance
#     if users_collection is not None:
#         try:
#             users_collection.create_index("email", unique=True)
#             chats_collection.create_index([("user_id", 1), ("timestamp", -1)])
#             print("Database indexes created successfully!")
#         except Exception as e:
#             print(f"Index creation error: {e}")
    
#     app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# MongoDB setup
try:
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db = client.get_database("ai_assistant")
    users_collection = db.get_collection("users")
    chats_collection = db.get_collection("chats")
    
    # Test connection
    client.admin.command('ismaster')
    print("MongoDB connected successfully!")
    
except Exception as e:
    print(f"MongoDB connection error: {e}")
    # Fallback to in-memory storage for development
    users_collection = None
    chats_collection = None

# Perplexity AI integration
def ask_perplexity(user_input):
    """
    Enhanced Perplexity AI integration with detailed responses
    """
    API_KEY = os.getenv("PERPLEXITY_API_KEY")
    
    if not API_KEY:
        return "Please set your PERPLEXITY_API_KEY in your .env file to get AI responses."
    
    # Enhanced system prompt for longer, more detailed responses
    system_prompt = """You are an intelligent and comprehensive AI assistant. When responding to user queries:

1. Provide detailed, thorough explanations rather than brief answers
2. Include relevant examples, context, and background information
3. Break down complex topics into understandable sections
4. Use formatting like bullet points, numbered lists, and headers when appropriate
5. Offer practical tips, suggestions, or next steps where relevant
6. Aim for responses that are informative, engaging, and helpful
7. If the topic is broad, cover multiple aspects or perspectives
8. Include real-world applications and use cases when applicable

Always strive to be comprehensive while remaining clear and well-organized."""

    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 2000,  # Increased for longer responses
        "top_p": 0.9
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions", 
            json=payload, 
            headers=headers,
            timeout=30  # Add timeout
        )
        response.raise_for_status()
        
        assistant_msg = response.json()["choices"][0]["message"]["content"]
        
        # Ensure minimum response length
        if len(assistant_msg.strip()) < 100:
            fallback_prompt = f"""Please provide a more detailed and comprehensive answer to this question: {user_input}

Include:
- Detailed explanation
- Examples or use cases
- Step-by-step guidance if applicable
- Additional context or background information
- Practical tips or recommendations"""
            
            # Make second request for more detailed response
            payload["messages"] = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": fallback_prompt}
            ]
            
            fallback_response = requests.post(
                "https://api.perplexity.ai/chat/completions", 
                json=payload, 
                headers=headers,
                timeout=30
            )
            
            if fallback_response.status_code == 200:
                assistant_msg = fallback_response.json()["choices"][0]["message"]["content"]
        
        return assistant_msg
        
    except requests.exceptions.RequestException as e:
        error_message = f"API request failed: {e}"
        print(error_message)
        
        # Fallback response with helpful information
        return f"""I'm currently experiencing connectivity issues with the AI service. Here's what you can try:

**Immediate Steps:**
- Check your internet connection
- Try your question again in a few moments
- Verify your PERPLEXITY_API_KEY is correctly set

**About Your Question:** "{user_input}"
While I can't provide the full AI-powered response right now, this appears to be a question about {user_input.split()[0] if user_input.split() else 'a general topic'}. 

**What You Can Do:**
- Try rephrasing your question
- Break complex questions into smaller parts
- Check if there are any specific aspects you'd like me to focus on

The AI service should be back online shortly. Please try again!"""
    
    except Exception as e:
        print(f"Unexpected error in ask_perplexity: {e}")
        return f"""I encountered an unexpected error while processing your request. 

**Your Question:** "{user_input}"

**Troubleshooting Steps:**
1. Ensure your PERPLEXITY_API_KEY is set in your .env file
2. Check your internet connection
3. Try a simpler version of your question
4. Contact support if the issue persists

I apologize for the inconvenience. Please try again or rephrase your question."""

# Use Perplexity as the main AI function
def ask_ai(message):
    """
    Main AI function that routes to Perplexity
    """
    return ask_perplexity(message)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email', '').strip().lower()
            password = request.form.get('password', '')
            
            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400
            
            if users_collection is not None:
                user = users_collection.find_one({"email": email})
                if user and check_password_hash(user['password'], password):
                    session['user_id'] = str(user['_id'])
                    session['user_email'] = user['email']
                    session['user_name'] = user['name']
                    return redirect(url_for('home'))
            
            return jsonify({'error': 'Invalid credentials'}), 401
            
        except Exception as e:
            print(f"Login error: {e}")
            return jsonify({'error': 'Server error occurred'}), 500
    
    # If user is already logged in, redirect to home
    if 'user_id' in session:
        return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            father_name = request.form.get('father_name', '').strip()
            email = request.form.get('email', '').strip().lower()
            password = request.form.get('password', '')
            
            # Validate inputs
            if not all([name, father_name, email, password]):
                return jsonify({'error': 'All fields are required'}), 400
            
            if len(password) < 6:
                return jsonify({'error': 'Password must be at least 6 characters'}), 400
            
            if '@' not in email or '.' not in email:
                return jsonify({'error': 'Invalid email format'}), 400
            
            if users_collection is not None:
                # Check if user already exists
                if users_collection.find_one({"email": email}):
                    return jsonify({'error': 'Email already registered'}), 409
                
                # Hash password before storing
                hashed_password = generate_password_hash(password)
                
                # Insert new user
                result = users_collection.insert_one({
                    "name": name,
                    "father_name": father_name,
                    "email": email,
                    "password": hashed_password
                })
                
                if result.inserted_id:
                    return jsonify({'message': 'Account created successfully'}), 201
            
            return jsonify({'error': 'Failed to create account'}), 500
            
        except Exception as e:
            print(f"Signup error: {e}")
            return jsonify({'error': 'Server error occurred'}), 500
    
    # If user is already logged in, redirect to home
    if 'user_id' in session:
        return redirect(url_for('home'))
        
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/ask', methods=['POST'])
def ask():
    # Check if user is logged in
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        user_msg = data.get('message', '').strip()
        if not user_msg:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get AI response
        reply = ask_ai(user_msg)
        
        # Save chat to database
        if chats_collection is not None:
            try:
                chats_collection.insert_one({
                    "user_id": session['user_id'],
                    "user_message": user_msg,
                    "bot_response": reply,
                    "timestamp": ObjectId().generation_time
                })
            except Exception as e:
                print(f"Error saving chat: {e}")
        
        return jsonify({'reply': reply})
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'error': 'Failed to process message'}), 500

@app.route('/chat-history')
def chat_history():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if chats_collection is not None:
            chats = list(chats_collection.find(
                {"user_id": session['user_id']},
                {"_id": 0, "user_message": 1, "bot_response": 1, "timestamp": 1}
            ).sort("timestamp", -1).limit(50))
            return jsonify({'chats': chats})
        return jsonify({'chats': []})
    except Exception as e:
        print(f"Chat history error: {e}")
        return jsonify({'error': 'Failed to fetch chat history'}), 500

@app.route('/user-info')
def user_info():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    return jsonify({
        'user_id': session.get('user_id'),
        'email': session.get('user_email'),
        'name': session.get('user_name')
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    # Create indexes for better performance
    if users_collection is not None:
        try:
            users_collection.create_index("email", unique=True)
            chats_collection.create_index([("user_id", 1), ("timestamp", -1)])
            print("Database indexes created successfully!")
        except Exception as e:
            print(f"Index creation error: {e}")
    
    app.run(debug=True, host='0.0.0.0', port=5000)