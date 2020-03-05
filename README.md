# jupyter json annotator


This package provides an annotation UI for arbitrary dataset in json format.


## Install
```
pip install jupyter-annotator
```


## Usage

### 1. Normal usage

```python
from jupyter_annotator import Annotator

problems = [{
    "id": 2,
    "problem": "Where would I not want a fox? (a problem from coommonsenseQA)",
    "options": {
        "a": "hen house", "b": "england", "c": "mountains", "d": "english hunt", "e": "california"
    },
    "answer": "a",
    "filtered": "xxxxxxxxxx"
}]

anno = Annotator(problems)
anno.start()
```

![](https://i.imgur.com/xxT1hEN.png)




### 2. Custom fields + skip + filter
+ **Custom fields**: add custom field in the format (field_name, type, max_length)
+ **Skip fields**: the fields which will not appear in the form but still in the preview so that they won't be edited. 
+ **Filter fields**: the fields that won't appear either in the form or in the preview 

```python
problems = [{
    "id": 2,
    "problem": "Where would I not want a fox? (a problem from coommonsenseQA)",
    "options": {
        "a": "hen house", "b": "england", "c": "mountains", "d": "english hunt", "e": "california"
    },
    "answer": "a",
    "filtered": "xxxxxxxxxx"
}]

custom_fields = [("rationale", str, 100)] 
skip_fields = ['id'] 
filter_fields = ["xxx"]

annotator = Annotator(problems, custom_fields=custom_fields, skip_fields=skip_fields, filter_fields=filter_fields)
annotator.start()
```
![](https://i.imgur.com/iRF90ja.png)





## References
+ [Jupyter Widgets - Using Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
+ [jupyter-innotater](https://github.com/ideonate/jupyter-innotater)