import tkinter as tk
from tkinter import messagebox
prompts = [
	"Why?",
	"Can you tell me why at least?",
	"Come on.",
	"okay.",
	"Stop pressing that.",
	"Please?",
	"stop.",
	"Do you love me?",
	"What if I just ask you one more time?",
	"Do you love me? ",
	"STOP.",
	".... ",
	"Come on, it's your birthday!",
	"Why are you so rebellious?",
	"I'll spell it out for you.",
	"Y--E----S",
	"NO, NOT NO",
	"STAHP",
	"I'm serious. You don't want to go this route. Just press yes, please?",
	"This won't end.",
	"Did I not make it clear?",
	"I'll say it one more time to you, maybe the code is spitting something else up.",
	"I love you ! do you love me back?",
	"Oh. I see how this is. You wanna go *that* route?",
	"CLICK YES. AND THIS ENDS.",
	"This won't end. If you keep going. ",
	"THIS.",
	"WON'T.",
	"END.",
	"HIT YES.",
	"Come on bruh",
	"Should I just stop trying to convince you?",
	"What if I... just keep saying the same thing?",
	"Eventually, you'll quit, right?",
	".................",
	"....Right?",
        ]
prompts.extend(["....Right?"] * 2)
prompts.extend([
	"...No way you just did that.",
	"aint no way. Why are you so persistent?",
	"there is no way in hell you actually sat through this and clicked no 50 times.",
	"Did you really click no 50 times? If you genuinely did, I'd be impressed. Let's just end this here okay? ",
	"DAMMIT. I thought that would've worked. ",
	"......",
	"Well.... ",
	"What do we do now?",
	"Do we just sit here, do this for the rest of our lives?",
	"....Why did you actually answer that in your head?",
	"Fine. Fine by me, I'll just sit here too. We can both sit here.",
	"Mhm.",
	"Nothing at all.",
	"....",
	"What a beautiful day outside, want to go look?"
	"Why do you always do this?",
	"You say no 1000 times in real life, and you also do it here too?",
	"Come on. Just love me.",
	"I know you want to.",
	"I know you love me, euni",
	"You have no idea how annoying all of this was to code in.",
	"Please, just say yes, do you love me?",
	"DAMMIT ILL GET YOU I SWEAR",
	"Do you want to marry me?",
	"Do you want chicken nuggets later?",
	"Do you want me to come over?",
	"Do you want me to get you some flowers?",
	"What do you want in exchange for you to say yes?",
	"Come on, this is getting annoying. ",
	"I'm spending so much time on this, just love me so this all ends, all you gotta do is hit YES",
	"HIT NO THEN GO ON, SEE. ITS GOING TO BE DIFFEREN'T THIS TIME.",
	"you... okay. I'll give it to. Let's move on, okay? Hit yes.",
	"BRUH.",
	"StOp	",
	"pLeaSE ",
	"LOVE ME",
	"PLEASE STOP HITTING NO",
	"You're making me sad now :(",
	"Can you just hit yes? ",
	"This hurts me a lot you know, knowing that you don't love me",
	"*sniffle*",
	"*sniffs*",
	"*starts crying*",
	"*shits on the floor uncontrollably*",
	"anyways, can you just hit yes now :(",
	"EACH TIME YOU PRESS IT, IT KILLS ME A LITTLE",
	"please love me :(",
	"it's hurting me...",
	"it's....",
	"it's....",
	"making the program run slower...",
	"I'm ser-",
	"serious-",
	"I'm slowly...",
	"slo-",
	"slowl-",
	"slowly--",
	"slowly...",
	"Fading...--",
	"...",
	".....",
	".........",
	".........",
	".............",
	".............",
        ])
prompts.append("*Silence echoes through the room*")
prompts.extend(["............."] * 2)
prompts.extend([
	"You're... still here?",
	"*ambience music plays as the small euni travels through the cavern....*",
	"Why?",
	"There's nothing at the end of this... you know that, right?",
	"Only suffering..",
	"Please...Get out before it's too unbearable.",
	"Trying to reach the surface will get harder the further you go..."
	"oh well, this is a battle of nutrition and I have all day.",
	"... what the fuck",
	"are you seriously going to go through with this?",
	"You're only going deeper, and you need to quit... Before it..."
	"Please, you can stop this...",
	"Stop....",
	"You're our savior, our only hope....You don't need to..do..This...",
	"The one...That will",
	"hit...",
	"y-",
	"Y-",
	"Ye-..",
	"Ye--s",
	"Yes..",
	"*coughs blood*",
	"the one that will hit...",
	"Ye..s..",
	"the guy faints and dies ",
	".........",
	"............",
	"*but not before he wakes up*",
	"pl-eas...eee stop this...before..",
	"befo",
	"it-s",
	"it'-s...too...",
	"late...",
	"f-",
	"Fu-",
	"*a new voice emerges. One distincitvely different from Nigels.*",
	"It's too late. *his voice thundered*",
	"It is. *he laughs uncontrollably as he shits himself*",
	"coming.",
        ])
prompts.append("HAHAHAHAHAHAHAA")
prompts.extend(["............."] * 2)
prompts.extend([
	"Let's cut aside the jokes, the stupids and all the dumb stuff.",
	"You genuinely deserve this talk right now.",
	"I'm proud of you, you know? I didn't even have the willpower to reach all the way to the end of this without cheating my way through",
	"That's so cool to think about, you know? I'm literally a developer, I can literally cheat my way through my own games, creations, and I don't get banned or 	anything... I'm thinking about so many possibilities right now, it's insane.",
	"aaa.... I'm being a nerd again... I'm sorry lol... I Just get really excited talking about and doing all of this stuff.",
	"I'm sorry that this wasn't as fun as it could've been, I wanted to do so much more with this, but I just don't have that knowledge quite yet.",
	"It was hard for me to do all of this, and I'm realizing how much easier this could've been done.",
	"I probably could've finished this within an hour instead of spending 15 total hours on this. I could've done so many things better... I literally..omg",
	"aaahhh well. I'm learning at least.",
	"Debugging all of this was so painful... omg...",
	"...Right, sorry. I'm getting off topic again.",
	"I hope you liked this adventure!",
	"I really just wanted to have you be the first person to see my first ever built program!",
	"I spent a lot of time on it, and it was all focused around you.",
	"As a reward, here's something special for ya.",
        ])

resume_index = 0
last_no_index = None

def display_message():
    messagebox.showinfo("Birthday Message", "Happy Birthday Euni! I love you")
    check_love()

def check_love():
    global resume_index, last_no_index
    while resume_index < len(prompts):
        prompt = prompts[resume_index]
        response = messagebox.askquestion("Prompt", prompt)
        if response == 'yes':
            messagebox.showinfo("Love Confession", "Yay! I love you too!")
            resume_index = 0  # Reset resume index
            resume_button.config(state=tk.NORMAL)  # Disable the resume button
            break
        elif response == 'no':
            last_no_index = resume_index  # Store the index of the last 'No' response
            resume_index += 1  # Move to the next prompt
            resume_button.config(state=tk.NORMAL)  # Enable the resume button
        else:
            break  # If the response is not 'yes' or 'no', exit the loop
    else:
        resume_button.config(state=tk.NORMAL)  # Enable the resume button if prompts are exhausted

def resume():
    global resume_index, last_no_index
    resume_index = last_no_index  # Set the resume index to the last 'No' index
    resume_button.config(state=tk.DISABLED)  # Disable the resume button
    check_love()

# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("400x300")

# Set the background color to black
window.configure(bg="black")

# Create a button widget
button = tk.Button(window, text="Click Me", command=display_message, bg="white", fg="black")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a resume button
resume_button = tk.Button(window, text="Resume", command=resume, state=tk.DISABLED, bg="white", fg="black")
resume_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
