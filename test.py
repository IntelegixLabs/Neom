import pybboxes as pbx

voc_bbox = (182, 272, 506, 446)
W, H = 720, 720  # WxH of the image
res = pbx.convert_bbox(voc_bbox, from_type="bbox", to_type="yolo", image_size=(W,H))

print(res)