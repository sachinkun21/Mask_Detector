
from utils.draw_bbox_cv2 import show_close_persons
from utils.draw_bbox_cv2 import plot_close_lines


def euclidean_distance(p1,p2):
    return ((p2[0]-p1[0])**2+ (p2[1]-p1[1])**2)**0.5

def calculate_distance(bbox_cords):
    close_persons = []
    for i in range(len(bbox_cords)):
        for j in range(i+1, len(bbox_cords)):
            person1 = bbox_cords[i]
            left, right, top, bottom = person1
            p1 = (left + right) // 2, (top + bottom) // 2

            person2 = bbox_cords[j]
            left, right, top, bottom = person2
            p2 = (left + right) // 2, (top + bottom) // 2
            dist = (euclidean_distance(p1,p2))
            if dist<100:
                close_persons.append((p1,p2))
    return close_persons

def calc_dist_and_plot_close(image_np, bbox_cords, im_height):
    close_persons = calculate_distance(bbox_cords)
    close_p = len(close_persons)
    show_close_persons(image_np, close_p, im_height)
    for p1, p2 in close_persons:
        plot_close_lines(p1,p2,image_np)



