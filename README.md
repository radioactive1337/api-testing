# api-testing

## Description

API framework for the practice of modules such as requests, allure and other tools \
I used an open api [sendrequest](https://sendrequest.me/) \
[Example of the allure report is shown here](https://radioactive1337.github.io/api-testing/)

## Project structure

| Name        | Desc               |
|:------------|:-------------------|
| api         | for work with api  |
| data        | data for tests     |
| data_models | pydantic models    |
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

Also, you can create docker image and run it (with pre-installed docker ofc C:)

~~~bash
docker build -t <your_image_name> .
~~~

Then run it

~~~bash
docker run <your_image_name>
~~~

Copy allure report from docker volume

~~~bash
docker cp $(docker ps -a -q | head -1):<your path to workdir> .
~~~

Then create report page