# codeforces-problem-scrapper-api

Simple Flask-Python API to parse Codeforces problem into JSON.

Make GET request on root `/?id=1325/A` and provide query parameter `id`.
The `id` should be equal to `contest_id/problem_letter`.

for example if you try to parse [this](https://codeforces.com/contest/1325/problem/A) problem you get the following JSON response:

```json
{
  "input_specification": "<p>The first line contains a single integer $$$t$$$ $$$(1 \\le t \\le 100)$$$  — the number of testcases.</p><p>Each testcase consists of one line containing a single integer, $$$x$$$ $$$(2 \\le x \\le 10^9)$$$.</p>",

  "memory_limit": "256 megabytes",

  "note": "<p>In the first testcase of the sample, $$$GCD(1,1)+LCM(1,1)=1+1=2$$$.</p><p>In the second testcase of the sample, $$$GCD(6,4)+LCM(6,4)=2+12=14$$$.</p>",

  "output_specification": "<p>For each testcase, output a pair of positive integers $$$a$$$ and $$$b$$$ ($$$1 \\le a, b \\le 10^9)$$$ such that $$$GCD(a,b)+LCM(a,b)=x$$$. It's guaranteed that the solution always exists. If there are several such pairs $$$(a, b)$$$, you can output any of them.</p>",

  "sample_tests": [
    {
      "in": "\n2\n2\n14\n",
      "out": "\n1 1\n6 4\n"
    }
  ],

  "statement": "<p>You are given a positive integer $$$x$$$. Find <span class=\"tex-font-style-bf\">any</span> such $$$2$$$ positive integers $$$a$$$ and $$$b$$$ such that $$$GCD(a,b)+LCM(a,b)=x$$$.</p><p>As a reminder, $$$GCD(a,b)$$$ is the greatest integer that divides both $$$a$$$ and $$$b$$$. Similarly, $$$LCM(a,b)$$$ is the smallest integer such that both $$$a$$$ and $$$b$$$ divide it.</p><p>It's guaranteed that the solution always exists. If there are several such pairs $$$(a, b)$$$, you can output any of them.</p>",

  "time_limit": "1 second",

  "title": "A. EhAb AnD gCd"
}
```

## Usage

You need python3 installed.

- Install packages in `requirements.txt` using pip3.  
  `pip3 install -r requirements.txt`
- Start the server.  
  `python3 api.py`