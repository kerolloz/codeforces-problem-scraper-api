import bs4
import requests


def parse_problem(problem_link):
    markup = requests.get(problem_link).text
    soup = bs4.BeautifulSoup(markup, "html.parser")
    problem = {
        "title": soup.find('div', 'title').string,
        "timeLimit": split_limit(soup.find('div', 'time-limit').contents[1].string),
        "memoryLimit": split_limit(soup.find('div', 'memory-limit').contents[1].string),
        "statement": get_statement(soup),
        "inputSpecification": get_content(soup, 'input-specification'),
        "outputSpecification": get_content(soup, 'output-specification'),
        "samples": get_sample_tests(soup),
        "note": get_content(soup, 'note'),
    }
    return problem


def split_limit(soup):
    l = soup.split()
    return {
        "value": int(l[0]),
        "unit": l[1]
    }


def group_tests(lst):
    """returns a list of list({input, output})"""
    return [{"input": _in, "output": _out} for _in, _out in pairwise(lst)]


def get_sample_tests(souped_html):
    return group_tests(get_tags_contents(souped_html, 'pre'))


def get_tags_contents(souped_html, tag_name, class_name=None):
    """This function returns all the tags contents in a souped html"""
    return [concat_contents(tag.contents) for tag in souped_html.find_all(tag_name, class_name)]


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def get_statement(soup):
    return concat_contents(soup.find('div', 'header').next_sibling.contents)


def get_content(soup, _class=''):
    element = soup.find('div', _class)
    if not element:
        return None
    tags = element.contents
    tags.pop(0)
    return concat_contents(tags)


def concat_contents(ls):
    return ''.join([str(i) for i in ls])
