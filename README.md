# Complexity Sort

Sort sentences by how complex/unique they are.

```
$ python complexity.py
this is a random sentence
this is another random sentence
yet another similar random sentence
omg so unique a phrase
(ctrl-d)
```

gives output

```
['omg so unique a phrase\n', 7.89]
['yet another similar random sentence\n', 5.56]
['this is a random sentence\n', 3.8]
['this is another random sentence\n', 3.8]
```

## How it works

A uniqueness value is computed for every single word depending on how frequently it appears in sentences. The uniqueness value of a sentence depends on the uniqueness value of its words and its length. It can be tweaked depending on whether you want to prefer long sentences or short unique sentences.