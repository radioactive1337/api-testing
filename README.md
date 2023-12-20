[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&random=false&width=435&lines=api-testing-practice)](https://git.io/typing-svg)

## Description

API framework for the practice of modules such as requests, allure and other tools \
I used an open api [sendrequest](https://send-request.me/) \
[Example of the allure report is shown here](https://radioactive1337.github.io/api-testing-practice/)

## Project structure

| Name        | Desc               |
|:------------|:-------------------|
| api         | for work with api  |
| data        | data for tests     |
| data_models | pydantic models    |
| enums       | constants          |
| schemas     | jsonschemas        |
| test        | api tests          |
| tools       | some helpful tools |

## Installation

Clone project

~~~bash
git clone https://github.com/radioactive1337/api-testing.git
~~~

~~~bash
cd api-testing
~~~

Install requirements

~~~bash
pip install -r requirements.txt
~~~

## Usage

Run all tests with allure (with pre-installed Allure)

~~~bash
pytest test --alluredir=allurereport
~~~

Create report page

~~~bash
allure serve allurereport
~~~

Also, you can create docker image and run it

~~~bash
docker build -t <your_image_name> .
~~~

Then run it

~~~bash
docker run <your_image_name>
~~~

Copy allure report from docker volume

~~~bash
docker cp <container_name>:<volume_path> <host_path>
~~~

Then create report page
