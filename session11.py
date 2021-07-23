import math

# Regular Convex Polygon Object

class Polygon:
    '''
    This Polygon takes 2 parameters -- number of edges (N) and circum-radius (R), and the related parameters
    such as vertices, interior angle, edge length, apothem, area and perimeter are obtained using get methods.
    Access to modify by name operator is available only for num_edges and circum_rad, and any such
    modifications will reflect accordingly in the dependent parameters accessed by get_{attribute} methods.
    '''

    def __init__(self, num_edges=3, circum_rad=6):
        if not isinstance(num_edges, int):
            raise TypeError(f'"num_edges" is an integer; TypeError')
        if num_edges < 3:
            raise ValueError(f'Polygon has a minimum of 3 edges; ValueError')
        self.num_edges = num_edges
        self.circum_rad = circum_rad

    @property
    def get_num_edges(self):
        return self.num_edges

    @property
    def get_circum_rad(self):
        return self.circum_rad

    @property
    def get_vertices(self):
        return self.get_num_edges

    @property
    def get_int_angle(self):
        return (self.get_num_edges - 2) * 180 / self.get_num_edges

    @property
    def get_edge_length(self):
        return 2 * self.get_circum_rad * math.sin(math.pi / self.get_num_edges)

    @property
    def get_apothem(self):
        return self.get_circum_rad * math.cos(math.pi / self.get_num_edges)

    @property
    def get_area(self):
        return self.get_num_edges * self.get_edge_length * self.get_apothem / 2

    @property
    def get_perimeter(self):
        return self.get_num_edges * self.get_edge_length

    def __repr__(self):
        return f'Polygon(edges={self.get_num_edges}, rad={self.get_circum_rad})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.get_vertices == other.get_vertices and self.get_circum_rad == other.get_circum_rad:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self.get_vertices > other.get_vertices:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')

# Polygon Iterator containing sequence of Polygons

class PolygonIterator:
    '''
    This class takes in number of vertices for the largest polygon in the sequence. Currently the sequence type is chosen as list,
    but it can be changed later, if required. The SequencePolygon class also takes in a circum_radius and it is assumed to be common
    for all of the polygons in the sequence.
    '''

    def __init__(self, num_vertices=3, circum_rad=6):
        if not isinstance(num_vertices, int):
            raise TypeError(f'"num_vertices" is an integer; TypeError')
        if num_vertices < 3:
            raise ValueError(f'Polygon has a minimum of 3 vertices; ValueError')

        self._num_vertices = num_vertices
        self._circum_rad = circum_rad
        self._polygons = [Polygon(edges, self._circum_rad) for edges in range(3, self._num_vertices + 1)]
        self.__start = 0

    def __len__(self):
        return self._num_vertices - 2

    def __repr__(self):
        return f'PolygonIterator(iterable: edges={self._num_vertices}, fixed: rad={self._circum_rad})'

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.__start >= (self._num_vertices - 2):
                raise StopIteration
        except StopIteration:
            print(f'StopIteration: Iterator reached max_value.')
            return f''
        else:
            current = self.__start
            self.__start += 1
            return self._polygons[current]

    def goon(self):
        try:
            if not self._polygons:
                raise StopIteration
        except StopIteration:
            print(f'IndexError: Iterator reached max_value.')
            return f''
        else:
            return self._polygons.pop(0)

    def __getitem__(self, index):
        if index not in range(self._num_vertices - 2):
            raise IndexError(f'Index out of range')
        else:
            return self._polygons[index]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, key=lambda p: p.get_area / p.get_perimeter, reverse=True)
        return sorted_polygons[0]

