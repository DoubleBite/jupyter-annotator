# jupyter json annotator


This package provides an annotation UI for arbitrary dataset in json format.


## Install
```
pip install jupyter-annotator
```


## Usage
```python
# Normal usage
from jupyter_annotator import Annotator
problems = [{
    "problem": "Where would I not want a fox? (a problem from coommonsenseQA)",
    "options": {
        "a": "hen house", "b": "england", "c": "mountains", "d": "english hunt", "e": "california"
    },
    "answer": "a"
}]

annotator = Annotator(problems)
annotator.start()
```


```python
# Add custom fields
from jupyter_annotator import Annotator
problems = [{
    "problem": "What is the perimeter of a rectangular field whose diagonal is 5 m and width is 3 m ?",
    "options": {
        "a":"20 m", "b":"15 m", "c":"14 m", "d":"10 m", "e":"25 m"
    },
    "answer": "c"
}]

custom_fields = [("rationale", str, 100)] # (field_name, type, max_length)
annotator = Annotator(problems, custom_fields=custom_fields)
annotator.start()
```

```python
# Skip fields
from jupyter_annotator import Annotator
problems = [{
    "id": 1,
    "problem": "Where would I not want a fox? (a problem from coommonsenseQA)",
    "options": {
        "a": "hen house", "b": "england", "c": "mountains", "d": "english hunt", "e": "california"
    },
    "answer": "a"
}]

filtered_fields = ['id'] 
annotator = Annotator(problems, filtered_fields=filtered_fields)
annotator.start()
```

+ Normal Usage
![](https://i.imgur.com/XyTxx9f.png)

+ Add custom fields
![](https://i.imgur.com/ZGulPVj.png)

+ Skip fields
![](https://i.imgur.com/6zT5lMR.png)



## References
+ [Jupyter Widgets - Using Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
+ [jupyter-innotater](https://github.com/ideonate/jupyter-innotater)