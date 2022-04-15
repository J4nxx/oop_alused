import requests
import pygal
from pygal.style import Style
python_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
javas_url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
response = requests.get(python_url)
response_javas = requests.get(javas_url)
print("Status code:" ", respnse.status_code")
response_dict = response.json()
response_dict_javas = response_javas.json()
print("Total repositories: ", response_dict["total_count"])
repo_dicts = response_dict["items"]
repo_dicts_javas = response_dict_javas["items"]
print("Repositories returned: ", len(repo_dicts))
python_names = []
python_stars = []
javas_names = []
javas_stars = []
i = 0
for repo in repo_dicts:
    python_names.append(repo_dicts[i]["name"])
    python_stars.append(repo_dicts[i]["stargazers_count"])
    i += 1
j = 0
for repo in repo_dicts_javas:
    javas_names.append(repo_dicts_javas[j]["name"])
    javas_stars.append(repo_dicts_javas[j]["stargazers_count"])
    j += 1
my_style = Style(color = "128AF3")
my_config = pygal.Config()
chart = pygal.Bar(style = my_style, x_label_rotation = 60, show_legend = True)
chart.title = "Most-Starred Python and JavaScript Projects on GitHub"
chart.add("JavaScript", javas_stars)
chart.add("Python", python_stars)
chart.render_in_browser()