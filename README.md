# CodeForces Problem Scraper API

A Simple Flask-Python API to parse Codeforces problem into JSON.

Make a **GET** request to the root `/?id=1325/A` and provide the required query parameter `id`.
The `id` should be in the following format `contest_id/problem_letter`.

For example, if you try to parse [this](https://codeforces.com/contest/1325/problem/A) problem you get the following JSON response:

```json
{
  "inputSpecification": "<p>The first line contains a single integer $$$t$$$ $$$(1 \\le t \\le 100)$$$  — the number of testcases.</p><p>Each testcase consists of one line containing a single integer, $$$x$$$ $$$(2 \\le x \\le 10^9)$$$.</p>",
  "memoryLimit": {
    "unit": "megabytes",
    "value": 256
  },
  "note": "<p>In the first testcase of the sample, $$$GCD(1,1)+LCM(1,1)=1+1=2$$$.</p><p>In the second testcase of the sample, $$$GCD(6,4)+LCM(6,4)=2+12=14$$$.</p>",
  "outputSpecification": "<p>For each testcase, output a pair of positive integers $$$a$$$ and $$$b$$$ ($$$1 \\le a, b \\le 10^9)$$$ such that $$$GCD(a,b)+LCM(a,b)=x$$$. It's guaranteed that the solution always exists. If there are several such pairs $$$(a, b)$$$, you can output any of them.</p>",
  "samples": [
    {
      "input": "\n2\n2\n14\n",
      "output": "\n1 1\n6 4\n"
    }
  ],
  "statement": "<p>You are given a positive integer $$$x$$$. Find <span class=\"tex-font-style-bf\">any</span> such $$$2$$$ positive integers $$$a$$$ and $$$b$$$ such that $$$GCD(a,b)+LCM(a,b)=x$$$.</p><p>As a reminder, $$$GCD(a,b)$$$ is the greatest integer that divides both $$$a$$$ and $$$b$$$. Similarly, $$$LCM(a,b)$$$ is the smallest integer such that both $$$a$$$ and $$$b$$$ divide it.</p><p>It's guaranteed that the solution always exists. If there are several such pairs $$$(a, b)$$$, you can output any of them.</p>",
  "timeLimit": {
    "unit": "second",
    "value": 1
  },
  "title": "A. EhAb AnD gCd"
}
```

## Usage

After cloning the repository

You got 2 options:

- _Python3_ installed:
  - Go to the `/app` directory.
  - Install packages in `requirements.txt` using pip3.  
    `pip3 install -r requirements.txt`
  - Start the server.  
    `FLASK_APP=main.py flask run`
- _Docker_ installed:
  - build the image  
    `docker build -t cf-problem-scraper-api .`
  - create a container  
    `docker run -d --name cf-api -p 80:80 cf-problem-scraper-api`

## JSON Schema

```json
{
  "inputSpecification": String,
  "memoryLimit": {
    "unit": String,
    "value": Number
  },
  "note": String, // or null
  "outputSpecification": String,
  "samples": [
    {
      "input": String,
      "output": String
    }
  ],
  "statement": String,
  "timeLimit": {
    "unit": String,
    "value": Number
  },
  "title": String
}
```
