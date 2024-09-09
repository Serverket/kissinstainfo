from flask import Flask, render_template, request, flash  
import instaloader  

app = Flask(__name__)  
app.secret_key = 'your_secret_key'  # Change this to a random secret key  

results_data = {}  # Store results data to use in export  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    global results_data  # Use the global variable to store results  

    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        option = request.form['option']  
        user_input = request.form.get('user_input', type=int)  

        usernames = request.form['usernames'].split(',')  

        instaloader_instance = instaloader.Instaloader()  

        try:  
            instaloader_instance.login(username, password)  

            results_data = {}  # Clear previous results  
            for user in usernames:  
                user = user.strip()  
                profile = instaloader.Profile.from_username(instaloader_instance.context, user)  
                followers = profile.get_followers()  
                
                follower_data = []  
                for follower in followers:  
                    follower_profile = instaloader.Profile.from_username(instaloader_instance.context, follower.username)  
                    follower_data.append({  
                        "username": follower.username,  
                        "name": follower_profile.full_name  # Get the name of the follower  
                    })  
                    if len(follower_data) >= user_input:  
                        break  

                # Store name and followers for this user  
                results_data[user] = {  
                    "name": profile.full_name,  # Get the name from the profile  
                    "followers": follower_data  
                }  

            return render_template('index.html', results=results_data)  

        except instaloader.exceptions.BadCredentialsException:  
            flash('Invalid credentials. Please check your username and password.')  
        except Exception as e:  
            flash(f'An error occurred: {e}')  

    return render_template('index.html', results={})  

if __name__ == '__main__':  
    app.run(debug=True)