from datetime import datetime
import requests
import random

README_PATH = "README.md"


def get_dino():
    url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"
    try:
        response = requests.get(url, timeout=2.5)
        if response.status_code == 200:
            data = response.json()
            return data["Name"], data["Description"]
    except Exception:
        pass
    return "Unknown Dino", "Could not fetch dinosaur data"


def get_days():
    current_date = datetime.now()
    end_of_year = datetime(current_date.year, 12, 31)
    days_left = (end_of_year - current_date).days
    return days_left, current_date.year


def get_progress_bar():
    current_date = datetime.now()
    start_of_year = datetime(current_date.year, 1, 1)
    end_of_year = datetime(current_date.year, 12, 31)
    total_days = (end_of_year - start_of_year).days + 1
    days_passed = (current_date - start_of_year).days + 1
    percent = (days_passed / total_days) * 100

    bar_length = 20
    filled_blocks = int(bar_length * days_passed // total_days)
    bar = "█" * filled_blocks + "░" * (bar_length - filled_blocks)

    return f"📅 Year Progress: {bar} {percent:.2f}%"


def get_ascii_dino():
    ascii_dinos = [
        """
<pre><code>
             __
            / _)
     .-^^^-/ /
  __/       /
 <__.|_|-|_|
</code></pre>
""",
        """
<pre><code>
           __
          / _)
   .-^^^-/ /
__/       /
<__.|_|-|_|
</code></pre>
""",
        """
<pre><code>
          __
         /oo\\
        (    )
         `--'
</code></pre>
""",
    ]
    return random.choice(ascii_dinos)


if __name__ == "__main__":
    days, year = get_days()
    dino_name, dino_desc = get_dino()
    progress_bar = get_progress_bar()
    ascii_dino = get_ascii_dino()

    readme_content = f"""
# 🦖 Welcome to My GitHub!

Hi there! Here's some fun info for today:

## 📅 Days Until New Year
👉 **{days} days** left in {year}!

{progress_bar}

## 🌟 🦕 Dinosaur of the Day 🌟

{ascii_dino}

> ### **{dino_name}**
> {dino_desc}
>
> ---

## 📊 GitHub Stats
![GitHub stats](https://github-readme-stats.vercel.app/api?username=MAadinP&show_icons=true&theme=tokyonight)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=MAadinP&layout=compact&theme=tokyonight)
    """

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content.strip())
