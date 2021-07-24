
# Polygons as iterables with 'lazy' attributes and methods

#### Previously we used class for constructing a single Polygon given number of edges and a circum-radius. 

#### Then we extended it to a class to construct a sequence of polygons given the number of edges of the largest polygon in the sequence (and assumed sequence is a continuously monotonous integer sequence without any skips or steps).

#### In this assignment, the Polygon sequence class is tweaked to work as an iterator. The class has to include special dunder methods -- `__iter__()` and `__next__()`. The `__iter__()` method returns the Polygon class instance i.e., it indicates that the iteration is taking place over specific class instance, and the `__next__()` defines what to return next when the iterator gets called. Exceptions are included to stop the iterator on one complete sweep over the sequence.

#### PolygonIterator creates a sequence of polygons given the number of edges/vertices of the largest polygon in the sequence.

#### The methods `__iter__()` and `__next__()` are added to make this class an iterator. While `__iter__()` returns the self, the `__next__()` returns the next polygon in the sequence.

#### Two methods, one using the Python's default `__next__()` special method, and another using custom method `goon()` performing the iterator logic, are included in the code. While the default `__next__()` can be simply called as next(class instance), the `goon()` is called as named operator just like any other function i.e., `class_instance.goon()`.

### Examples:

Link to the notebook file with examples:

[https://github.com/vgops75/session-11-PolygonIterator/blob/master/session11_PolygonIterator.ipynb]


#### `s1 = PolygonIterator(7, 5)` creates an instance of PolygonIterator and this contains sequences of polygons with number of edges starting from n = 3 (minimum) to 7, and a common circum_radius of R = 5 is assumed for the polygon sequences.

#### Try len(s1) to get the number of items making up the sequence object.
#### Try s1[index_value] to get a specific polygon. Since starting polygon has a minimum of 3 edges, the index will be 0 for 3 edge polygon, 1 for 4 edge polygon, ..., 4 for 7 edge polygon, and hence for `s1 = PolygonIterator(7, 5)`, s1[0] corresponds to 3 edge polygon, s1[4] corresponds to 7 edge polygon.

#### Try next(s1) to get the next in the iterable.

#### can do for loop to access each item, like below: -

```
s1 = PolygonIterator(7, 5)
for item in s1:
    if item:
        print(item)
    else:
        break
```



