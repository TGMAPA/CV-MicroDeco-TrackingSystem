import numpy

def get_box_centroid(box):
    x1, y1, x2, y2 = box
    return int((x1 + x2)/2), int((y1 + y2)/2)


def calc_euclidean_distance(p1, p2):
    return numpy.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# threshold in pixel units
def are_two_points_near(p1, p2, threshold):
    # Calc distance and validate limit
    if calc_euclidean_distance(p1, p2) < threshold:
        return True
    return False