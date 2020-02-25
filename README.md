# jupyter json annotator

This package provides an annotation UI for arbitrary dataset in json format.


## Usage
```
from jupyter_annotator import Annotator

problems = [{
    "problem": "Where would I not want a fox? (a problem from coommonsenseQA)",
    "options": {
        "a": "hen house", "b": "england", "c": "mountains", "d": "english hunt", "e": "california"
    },
    "answer": "a"
}]

anno = Annotator(problems)
anno.start()
```
![](https://imgur.com/3swMqsa)

## References
+ [Jupyter Widgets - Using Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
+ [jupyter-innotater](https://github.com/ideonate/jupyter-innotater)