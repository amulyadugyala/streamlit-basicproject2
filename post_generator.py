import random

def generate_post(platform, tone, topic, custom_hashtags=""):
    templates = {
        "Instagram": {
            "Casual": [
                f"Just thinking about {topic} lately... 🌟 What’s your take on it?",
                f"Can't stop loving the vibe around {topic}! 💫",
            ],
            "Professional": [
                f"Exploring the impact of {topic} in our daily routines. Insights coming soon. 👀",
                f"Why {topic} is more important than ever in today’s world. #growth",
            ],
            "Funny": [
                f"When you try to master {topic} but end up napping instead. 😴",
                f"{topic}? Sounds like a superhero name, not a lifestyle. 😂",
            ],
            "Inspirational": [
                f"{topic} is the first step to unlocking your potential. Start today! 🚀",
                f"Your journey toward {topic} starts with a single step. Keep going! 💪",
            ]
        },
        "Twitter": {
            "Casual": [
                f"{topic} hits different at 2AM. #randomthoughts",
                f"That moment when {topic} actually works 😮‍💨",
            ],
            "Professional": [
                f"Sharing some thoughts on {topic} and why it matters in modern work culture.",
                f"3 ways {topic} can improve your productivity 🧵👇",
            ],
            "Funny": [
                f"{topic} is like trying to teach a cat to swim. 😂",
                f"Trying to explain {topic} like... yeah, good luck with that. 🤡",
            ],
            "Inspirational": [
                f"{topic} is your secret weapon. Believe in yourself. 💥",
                f"Never underestimate the power of {topic}. Push forward. ✨",
            ]
        },
        "LinkedIn": {
            "Casual": [
                f"Been reflecting on {topic} recently — how do you see it playing a role in your day-to-day?",
                f"{topic} isn’t just a buzzword. It’s a mindset. Curious what others think!",
            ],
            "Professional": [
                f"Today, I had a deep conversation on {topic}. Here's what I learned...",
                f"{topic} has a significant impact on team productivity. Let’s discuss how.",
            ],
            "Funny": [
                f"{topic} in the workplace? Sounds like a sitcom waiting to happen. 😂",
                f"When your boss says ‘embrace {topic}’ and you Google what it means 😅",
            ],
            "Inspirational": [
                f"{topic} is a game-changer for leaders who want to make an impact. 💼",
                f"The future belongs to those who practice {topic} with intention and integrity.",
            ]
        }
    }

    post_template = random.choice(templates[platform][tone])
    hashtags = custom_hashtags.strip() if custom_hashtags else f"#{topic.replace(' ', '').lower()}"

    return post_template, hashtags
